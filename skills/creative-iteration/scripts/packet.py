"""Build a blind rating packet for people comparing two or more runs.

Each arm is a folder holding menu.md (numbered one-line ideas) and top3.md
(developed ideas as "### " sections). The script gives each arm's menu a
letter (X, Y, Z…), shuffles every developed idea into one list (A, B, C…),
normalises the idea-name styling so formatting can't reveal the arm, and
writes the key to a separate file the raters must not open.

    packet.py runs/plain runs/skill-a runs/skill-b --out packet.md --key key.json
"""
import argparse
import json
import re
import secrets
from pathlib import Path

rng = secrets.SystemRandom()
SMALL = {"a", "an", "the", "and", "or", "of", "to", "in", "on", "at", "for", "by", "with", "from", "as", "but"}


def title(s):
    words = s.strip().rstrip(".:").split()
    return " ".join(w if i and w.lower() in SMALL else w[:1].upper() + w[1:] for i, w in enumerate(words))


def menu_lines(path):
    out = []
    for m in re.finditer(r"(?m)^\d+\.\s+(?:\*\*(.+?)\*\*[:.]?)?\s*(.*)$", path.read_text()):
        name, rest = m.group(1), m.group(2).strip()
        rest = rest[:1].upper() + rest[1:]
        out.append(f"**{title(name)}.** {rest}" if name else rest)
    return out


def ideas(path):
    for part in re.split(r"(?m)^### ", path.read_text())[1:]:
        head, _, body = part.partition("\n")
        yield title(head), body.strip()


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("arms", nargs="+", type=Path)
    p.add_argument("--out", required=True, type=Path)
    p.add_argument("--key", required=True, type=Path)
    a = p.parse_args()
    arms = a.arms[:]
    rng.shuffle(arms)
    menu_letters = dict(zip(map(str, arms), "XYZWVU"))
    pool = [(str(arm), n, head, body) for arm in arms for n, (head, body) in enumerate(ideas(arm / "top3.md"), 1)]
    rng.shuffle(pool)
    letters = [chr(65 + i) for i in range(len(pool))]
    out = ["# Blind rating packet", "", f"{len(arms)} menus ({', '.join(menu_letters.values())}) and {len(pool)} developed ideas ({letters[0]}–{letters[-1]}), shuffled. Nothing here says which run made what.", ""]
    for arm in sorted(arms, key=lambda x: menu_letters[str(x)]):
        out += [f"## Menu {menu_letters[str(arm)]}", ""] + [f"{i}. {l}" for i, l in enumerate(menu_lines(arm / "menu.md"), 1)] + [""]
    out += ["---", "", "# Developed ideas", ""]
    key = {"menus": menu_letters, "ideas": {}}
    for letter, (arm, n, head, body) in zip(letters, pool):
        out += [f"### {letter}. {head}", "", body, ""]
        key["ideas"][letter] = {"arm": arm, "rank_in_arm": n}
    out += ["---", "", "## Your ratings", "1. Favourite menu:", "2. For each pair your coordinator gives you, which would you rather have, and why (one line)?",
            "3. Rank the developed ideas, best first:", "4. The one you'd actually choose:", "5. Anything that stands out:"]
    a.out.write_text("\n".join(out) + "\n")
    a.key.write_text(json.dumps(key, indent=1))
    print(f"wrote {a.out} and {a.key}")


if __name__ == "__main__":
    main()
