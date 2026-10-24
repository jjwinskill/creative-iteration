"""Draw cards with real randomness, so the model never picks them.

Prints only the drawn cards, never the whole deck. An agent that has read the
deck is primed by it, and the draw stops being outside randomness.

With --run, every draw is appended to the skill's data/draws.jsonl, and
--credit records what a drawn card did for the run, so card effects can be
compared across runs with --stats.
"""
import argparse
import json
import secrets
import sys
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
DECK = SKILL / "deck" / "deck.json"
LOG = SKILL / "data" / "draws.jsonl"
WIKI = "https://en.wikipedia.org/api/rest_v1/page/random/summary"
EFFECTS = ("winner", "shortlisted", "taught", "none")
rng = secrets.SystemRandom()


def draw(cards, n, exclude):
    pool = [c for c in cards if c["id"] not in exclude]
    return rng.sample(pool, min(n, len(pool)))


def wiki_seed():
    req = urllib.request.Request(WIKI, headers={"User-Agent": "creative-iteration/0"})
    with urllib.request.urlopen(req, timeout=10) as res:
        page = json.load(res)
    return {"title": page["title"], "extract": page.get("extract", "")}


def append(record):
    record["at"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
    LOG.parent.mkdir(exist_ok=True)
    with LOG.open("a") as f:
        f.write(json.dumps(record) + "\n")


def mean(xs):
    return f"{sum(xs) / len(xs):.1f}" if xs else "n/a"


def stats():
    drawn, effects, distances = Counter(), defaultdict(Counter), defaultdict(list)
    for line in LOG.read_text().splitlines() if LOG.exists() else []:
        rec = json.loads(line)
        if rec["type"] == "draw":
            drawn.update(rec["moves"] + rec["constraints"] + rec["seeds"])
        elif rec["type"] == "credit":
            effects[rec["card"]][rec["effect"]] += 1
            if rec.get("distance"):
                distances[rec["card"]].append(rec["distance"])
    for card, n in drawn.most_common():
        tally = ", ".join(f"{e} {effects[card][e]}" for e in EFFECTS if effects[card][e])
        dist = f", distance {mean(distances[card])}" if distances[card] else ""
        print(f"{card}: drawn {n}" + (f" ({tally}{dist})" if tally else ""))
    carded = [d for card, ds in distances.items() if card in drawn for d in ds]
    print(f"\nmean distance: carded {mean(carded)}, control {mean(distances['control'])}, cold {mean(distances['cold'])}")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--moves", type=int, default=0)
    p.add_argument("--constraints", type=int, default=0)
    p.add_argument("--wiki", type=int, default=0, help="random Wikipedia summaries as seed material")
    p.add_argument("--exclude", default="", help="comma-separated ids already drawn this run")
    p.add_argument("--pick", default="", help="comma-separated options; returns one at random")
    p.add_argument("--run", default="", help="run slug; logs this draw or credit to draws.jsonl")
    p.add_argument("--stage", default="", help="stage and round, e.g. problems-1")
    p.add_argument("--credit", default="", help="a drawn card id (or wiki title) to credit")
    p.add_argument("--effect", choices=EFFECTS, help="what the credited card did for the run")
    p.add_argument("--note", default="", help="one line on how it did it")
    p.add_argument("--distance", type=int, choices=range(1, 6), help="distance judge's 1-5 score for the card's raw candidate")
    p.add_argument("--stats", action="store_true", help="print per-card draw and credit tallies")
    a = p.parse_args()

    if a.stats:
        stats()
        return
    if a.credit:
        if not (a.run and a.effect):
            p.error("--credit needs --run and --effect")
        append({"type": "credit", "run": a.run, "stage": a.stage, "card": a.credit, "effect": a.effect, "note": a.note, "distance": a.distance})
        return

    out = {}
    if a.moves or a.constraints:
        deck = json.loads(DECK.read_text())
        exclude = set(filter(None, a.exclude.split(",")))
        out["moves"] = draw(deck["moves"], a.moves, exclude)
        out["constraints"] = draw(deck["constraints"], a.constraints, exclude)
    if a.wiki:
        try:
            out["seeds"] = [wiki_seed() for _ in range(a.wiki)]
        except (urllib.error.URLError, TimeoutError) as err:
            print(f"wiki seed unavailable: {err}", file=sys.stderr)
    if a.pick:
        out["picked"] = rng.choice([o.strip() for o in a.pick.split(",") if o.strip()])
    if a.run:
        append({
            "type": "draw",
            "run": a.run,
            "stage": a.stage,
            "moves": [c["id"] for c in out.get("moves", [])],
            "constraints": [c["id"] for c in out.get("constraints", [])],
            "seeds": [s["title"] for s in out.get("seeds", [])],
            "picked": out.get("picked"),
        })
    json.dump(out, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
