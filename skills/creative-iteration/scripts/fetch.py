"""Fetch a URL through the run's shared cache, and print a compact view of it.

Every browsing agent fetches through this script, so a page or API result is
downloaded once per run, and later agents read the cached copy. It prints the
cached file's path, then the content: for JSON, only the keys you pick (from a
top-level list or a "data" list); otherwise the page's main text with HTML
stripped, or only snippets around a term, cut to --max characters.

    fetch.py "https://api.example.org/search?q=..." --cache runs/<slug>/cache --pick name,type,text
    fetch.py "https://en.wikipedia.org/wiki/..." --cache runs/<slug>/cache --max 6000
    fetch.py "https://en.wikipedia.org/wiki/..." --cache runs/<slug>/cache --find "scale length"

Exit status 2 on a network error (the message says which), so agents can note
the source as unreachable.
"""
import argparse
import hashlib
import html
import json
import os
import re
import sys
import time
import urllib.request


def get(url, cache, sleep):
    os.makedirs(cache, exist_ok=True)
    key = hashlib.sha1(url.encode()).hexdigest()[:16]
    path = os.path.join(cache, key + ".raw")
    if os.path.exists(path):
        return path, True
    req = urllib.request.Request(url, headers={"User-Agent": "creative-iteration/0.12", "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            body = r.read()
    except Exception as e:  # report and let the agent move on
        sys.stderr.write(f"unreachable: {url}: {e}\n")
        sys.exit(2)
    with open(path, "wb") as f:
        f.write(body)
    with open(os.path.join(cache, "index.tsv"), "a") as f:
        f.write(f"{key}\t{url}\n")
    time.sleep(sleep)
    return path, False


def page_text(text):
    main = re.search(r"(?is)<(main|article)\b.*?</\1>", text)
    text = main.group(0) if main else text
    text = re.sub(r"(?is)<(script|style|nav|header|footer)\b.*?</\1>", " ", text)
    text = html.unescape(re.sub(r"<[^>]+>", " ", text))
    return re.sub(r"\s+", " ", text).strip()


def view(raw, pick, limit, find):
    text = raw.decode("utf-8", "replace")
    try:
        data = json.loads(text)
    except ValueError:
        text = page_text(text)
        if find:
            hits = [m.start() for m in re.finditer(re.escape(find), text, re.I)]
            snippets = [text[max(0, h - 200):h + 300] for h in hits[:8]]
            return f"{len(hits)} matches for {find!r}\n" + "\n---\n".join(snippets)[:limit]
        return text[:limit]
    if pick:
        keys = pick.split(",")
        items = data if isinstance(data, list) else data.get("data", [data]) if isinstance(data, dict) else [data]
        rows = [{k: item.get(k) for k in keys if k in item} for item in items if isinstance(item, dict)]
        extra = {k: data[k] for k in ("total_cards", "total", "has_more") if isinstance(data, dict) and k in data}
        return json.dumps(dict(extra, items=rows), ensure_ascii=False)[:limit]
    return json.dumps(data, ensure_ascii=False)[:limit]


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("url")
    ap.add_argument("--cache", required=True, help="the run's cache folder, runs/<slug>/cache")
    ap.add_argument("--pick", help="for JSON: comma-separated keys to keep from each item")
    ap.add_argument("--find", help="for pages: print only snippets around this term")
    ap.add_argument("--max", type=int, default=4000, help="characters to print (default 4000)")
    ap.add_argument("--sleep", type=float, default=0.1, help="pause after a network fetch, to respect rate limits")
    a = ap.parse_args()
    path, hit = get(a.url, a.cache, a.sleep)
    print(f"{'cached' if hit else 'fetched'}: {path}")
    print(view(open(path, "rb").read(), a.pick, a.max, a.find))
