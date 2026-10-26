"""Build the Gate 1 menu mechanically from the filter's scores.

The lead writes the filter's scores to one JSON file and this script applies
the menu rules, so the lead neither hand-picks nor re-types the menu:
drop dead ideas, any "no" on a requirement and transplants; keep one per
duplicate group; fill the three bands; cover at least four kinds; break
ties by script.

    menu.py scores.json --out rounds/menu.md --json agents/menu.json [--refine]

scores.json is a list of ideas:
    {"label", "name", "source": "own" | "cold" | "generator" | "control" | "wild" | "mutation",
     "group", "kind", "distance": 1-5, "familiarity": "likely" | "maybe" | "unlikely",
     "feasibility": "fine" | "risky" | "dead", "fit": {"<requirement>": "yes" | "partly" | "no"},
     "transplant": bool, "pull": 1-5, "well": bool}

"own" is the person's own design or idea, used in refine mode.
"""
import argparse
import json
import secrets

rng = secrets.SystemRandom()
BANDS = (("familiar", "Familiar and strong"), ("twist", "A twist on the familiar"), ("out_there", "Out there"))


def fit_yes(i):
    return sum(v == "yes" for v in i["fit"].values())


def full_fit(i):
    return all(v == "yes" for v in i["fit"].values())


def rank_key(i):
    return (fit_yes(i), i["distance"], i["pull"], i["_tie"])


def eligible(items):
    keep = [i for i in items if i["feasibility"] != "dead" and "no" not in i["fit"].values() and not i["transplant"]]
    best = {}
    for i in sorted(keep, key=lambda x: (fit_yes(x), x["pull"], x["_tie"]), reverse=True):
        best.setdefault(i["group"], i)
    return list(best.values())


def build(items, refine, size):
    for i in items:
        i["_tie"] = rng.random()
    pool = eligible(items)
    bands = {b: [] for b, _ in BANDS}
    familiar = sorted((i for i in pool if i["well"] or i["source"] in ("cold", "own")), key=lambda i: (fit_yes(i), i["pull"], i["_tie"]), reverse=True)
    must = [i for i in familiar if i["source"] == "own"][:1] if refine else []
    cold = [i for i in familiar if i["source"] == "cold"][:1]
    bands["familiar"] = (must + cold + [i for i in familiar if i not in must + cold])[:3]
    used = set(map(id, bands["familiar"]))
    far = [i for i in pool if id(i) not in used and i["source"] != "mutation" and i["distance"] >= 4 and i["familiarity"] == "unlikely" and full_fit(i)]
    twists = sorted((i for i in pool if i["source"] == "mutation" and id(i) not in used), key=rank_key, reverse=True)
    if refine:
        out_room = min(2, len(far))
        bands["twist"] = twists[: max(0, size - len(bands["familiar"]) - out_room)]
    else:
        bands["twist"] = twists[:4]
        out_room = max(3, size - len(bands["familiar"]) - len(bands["twist"]))
    bands["out_there"] = sorted(far, key=rank_key, reverse=True)[:out_room]
    menu = [i for b, _ in BANDS for i in bands[b]]
    kinds = {i["kind"] for i in menu}
    spare = sorted((i for i in pool if id(i) not in set(map(id, menu)) and i["kind"] not in kinds), key=rank_key, reverse=True)
    while len(kinds) < 4 and spare and bands["out_there"]:
        new = spare.pop(0)
        if new["kind"] in kinds:
            continue
        old = min(bands["out_there"], key=lambda i: (i["pull"], i["_tie"]))
        bands["out_there"][bands["out_there"].index(old)] = new
        kinds = {i["kind"] for b in bands.values() for i in b}
    return bands, kinds, pool


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("scores")
    p.add_argument("--out", required=True)
    p.add_argument("--json", required=True)
    p.add_argument("--size", type=int, default=10)
    p.add_argument("--refine", action="store_true", help="the person's own design leads the familiar band; fewer out-there slots")
    a = p.parse_args()
    items = json.load(open(a.scores))
    bands, kinds, pool = build(items, a.refine, a.size)
    lines = ["## Menu (shown at Gate 1, built by scripts/menu.py)", ""]
    n = 0
    for b, title in BANDS:
        lines.append(f"**{title}:**")
        for i in bands[b]:
            n += 1
            tag = " · the obvious answer" if i["source"] == "cold" else " · your own design" if i["source"] == "own" else " · well" if i["well"] else ""
            lines.append(f'{n}. {i["label"]} {i["name"]} · distance {i["distance"]}{tag}')
        lines.append("")
    lines.append(f"Kinds covered: {len(kinds)} ({', '.join(sorted(kinds))}). Eligible ideas: {len(pool)} of {len(items)}.")
    if len(kinds) < 4:
        lines.append("Fewer than four kinds were available among eligible ideas.")
    open(a.out, "w").write("\n".join(lines) + "\n")
    json.dump({b: [i["label"] for i in bands[b]] for b, _ in BANDS} | {"kinds": sorted(kinds)}, open(a.json, "w"), indent=1)
    print("\n".join(lines))


if __name__ == "__main__":
    main()
