"""Flag operators that still carry their card's subject.

An operator should say how to change an idea, in words free of its card's
source story. Any distinctive word an operator shares with the card's
source (its person, place, work or story) is a leak, and the lead sends the
operator back for another rewrite. Words shared with the card's move are
listed for review only: the move's principle words are often fine, but a
concrete noun from it (a dike, a loom) is a leak too.

    leakcheck.py operators.json

operators.json is a list of {"id", "source", "move", "operator"}.
Exits 1 if anything is flagged.
"""
import json
import re
import sys

COMMON = set("""
a about after again all also an and any are around as at away back be because been before being
between both but by can could do does each even every few for from get give go had has have her
here him his how idea ideas if in into is it its just keep let like make makes many may more most
much must new no not now of off on once one only or other our out over own part parts people
person rather same see set should small so some such take than that the their them then there
these they thing things this those through time to toward turn under until up use very want was
way ways we well were what when where which while who whole why will with within without would you
your instead small large first last next every something someone others another whatever
""".split())


def words(text):
    return {w for w in re.findall(r"[a-z][a-z'-]{4,}", text.lower()) if w not in COMMON}


def main():
    cards = json.load(open(sys.argv[1]))
    flagged = 0
    for c in cards:
        op = words(c["operator"])
        leak = op & words(c.get("source", ""))
        review = (op & words(c.get("move", ""))) - leak
        status = "LEAK " + ", ".join(sorted(leak)) if leak else "ok"
        if review:
            status += "  (shared with the move, review: " + ", ".join(sorted(review)) + ")"
        flagged += bool(leak)
        print(f'{c["id"]}: {status}')
    sys.exit(1 if flagged else 0)


if __name__ == "__main__":
    main()
