"""Merge agents' idea files into one shuffled, unlabeled list for a judge.

Each input file holds ideas as sections that start with a "### " heading
naming the idea only (the agents are asked to write them that way, with no
agent or source label in the heading). The script shuffles every
section from every file, gives each a blind label (S01, S02, ...), writes
the list for the judge, and writes the key that maps labels back to their
source. The lead never retypes an agent's ideas or picks their order.

    blind.py agents/g1/out.md agents/g2/out.md ... agents/cold/out.md \
        --out agents/filter/input.md --key agents/filter/key.json --prefix S
"""
import argparse
import json
import re
import secrets


def sections(path):
    text = open(path, encoding="utf-8").read()
    parts = re.split(r"(?m)^### ", text)[1:]
    for p in parts:
        title, _, body = p.partition("\n")
        yield title.strip(), body.strip()


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("files", nargs="+")
    ap.add_argument("--out", required=True)
    ap.add_argument("--key", required=True)
    ap.add_argument("--prefix", default="S", help="label prefix (S for sketches, M for mutations)")
    a = ap.parse_args()
    items = [(f, t, b) for f in a.files for t, b in sections(f)]
    if not items:
        raise SystemExit("no '### ' sections found")
    secrets.SystemRandom().shuffle(items)
    key, lines = {}, []
    for i, (f, title, body) in enumerate(items, 1):
        label = f"{a.prefix}{i:02d}"
        key[label] = dict(file=f, title=title)
        lines.append(f"### {label}: {title}\n{body}\n")
    open(a.out, "w", encoding="utf-8").write("\n".join(lines))
    json.dump(key, open(a.key, "w"), indent=1)
    print(f"{len(items)} items from {len(a.files)} files -> {a.out}")
