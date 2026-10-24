# Run folder templates

## An intake round (Stage 0)

Each question asks one thing: one question mark, with no "and" or comma list joining two asks. If a question needs two answers, it's two questions, or one waits for a later round. Round 1 always includes the role and who-else questions. At most three rounds.

```markdown
<Round 1 only, if the request asks for a plan, design or build: one line saying this run finds and develops the idea, and planning is a separate step after.>

**Round N.** <one line: what this round settles, and what it opens next>

**Q1 · Your role:** <what will you be doing with it, day to day?>
Recommended: <answer> *(from your words: "…")* — or *(default)*

**Q2 · Who else:** <who else will use it, see it, or live with it?>
Recommended: <answer> *(from your words / default)*

**Q3 · <Label>:** <one question>
<For taste questions (the hook, the feel, the no list, what they love): no recommendation; ask it open.>

Reply with "yes" to take a recommendation, or answer in your own words.
```

<Audience-facing work: across the rounds, cover who the others are, the hook and the feel. Log every round and every reply verbatim in brief.md.>

## brief.md

```markdown
# <Working name>

## Intake (each round, questions and replies verbatim)
Round 1: Q1 <question> → "<reply>" …

## Brief block (exactly what agents receive; confirmed at Gate 0)
**Their words:** <intake answers verbatim, each labeled requirement or background>
(The requirements-only version, for the idea-seeding roles, drops every background line and every (background) tension.)
**Assumptions:** <assumption>, source: <inferred from "…" / default>
**Unknowns:** <gap>: open
**Gate 0 reply (verbatim):** "…"

## 0: the situation (held tight)
- Who: …
- What exists: …
- What hurts: …
- Hard limits: …

## The why (fixed)
<One or two sentences.>
**Why-test:** <how we'd know an idea serves it>

## Audience: me | a few | many
## Drift: refine | stretch | surprise (said / assumed)
## No list
- …

## Tension register
| # | Pulls this way | Pulls that way |
|---|---|---|
| T1 | … | … |
| T2 (background) | … | … |

## References
| Reference | Seed or taste | How it's used |
|---|---|---|

## Checks (one per limit and no-list item)
| Requirement | How it's checked (code / fetched source / calibrated threshold / the person judges) | Pass line |
|---|---|---|

## Brief score: N/10
- Room to move / nothing missing from 0 / audience confirmed / four or more tensions: …

## The obvious answer (two cold answers)
1. …
2. …

## Known wells (from data/wells.md, this kind of brief)
- … (or "none yet")
```

## rounds/pool.md

```markdown
# Pool: candidates | precedents | subjects + precedents
(With two pools, one table each: the subject pool, then the mechanism pool, each dealt separately.)
Sources (N): <name, URL> …
| # | Entry | One line | Source |
|---|---|---|---|
## Slices (deal.py output)
g1: … · g2: … · g3: … · g4: … · control: … · wild: …
```

## rounds/references.md (when the person names references)

```markdown
# References
## Section A (subject-free; becomes requirements)
Principles: 1. … · Register: …
## Section B (judges, developers and adversary only)
<per reference: notes with links>
Unsupported claims by the person: …
```

## rounds/problems.md

```markdown
# Problems
Draws: … (seed: …)
| Problem | From (card or control) | Tension inside it |
|---|---|---|
## Framing
<One paragraph: the real problem and the principle a good idea must honor. No example techniques.>
```

## rounds/fanout.md

```markdown
# Fan-out
Draws: generator 1: moves …, constraint …; … ; wild card: …, seed …, tension …

## Unprompted lists (each agent's 3–4 before its slice, with typicality guesses)
| Agent | Candidates (guess %) |
|---|---|

## Sketches (filter scores; blind labels from the script)
| Label | Source (card / control / wild / cold) | Pool # | Sketch (one line) | Group | Distance | Feasible | Fit | Forced | Pull | Well |
|---|---|---|---|---|---|---|---|---|---|---|

## Wells this run
| Well | Why (ledger / 3+ unprompted lists / both cold) |
|---|---|

## Menu (shown at Gate 1)
1. <one line>, distance N
… (about 8)
Wild slot A: <the highest-distance feasible idea>
Wild slot B: <the next>
Convergent lane: <up to 2 wells, labeled, with where they came from>
Reference: the obvious answer, <one line>

## Gate 1 (verbatim)
Picks: … · Vetoes: … · Note: "…"
```

## rounds/develop.md

```markdown
# Develop
## <Concept name>
<Developer's concept>
**Attack:** <reason>: fatal / fatal unless <premise> / scar
## Gate 2 (verbatim)
"…"
```

## dossier.md

```markdown
# Idea dossier: <brief name>

## The choice: <name>
- What it is: …
- Why it fits: …
- Distance from the obvious answer: N, <one line>
- What it would take: …
- Cheapest first test (within a week): …
- Biggest risk: …
- Prior art (originality briefs): <rating>, <closest prior art, with links>

## Runners-up
### <name>
(same fields, shorter)

## Also on the shelf
<Notable vault items and what would bring each back.>
```

## rounds/priorart.md (originality briefs)

```markdown
# Prior art
| Pick | Rating (known / known in principle, new in form / no prior found) | Closest prior art, with links | Narrowest surviving novelty claim |
|---|---|---|---|
Queries tried: …
Unreachable sources, and the hand searches to close the gap: …
```

## rounds/grounding.md and rounds/factcheck.md

```markdown
# Grounding (internal)
| Menu item | Verified / unverified / wrong | Link | Nuance |
|---|---|---|---|

# Fact-check
Claims N · verified N · unsupported N (flagged N) · wrong N
| Claim | Status | Source | Correction made |
|---|---|---|---|
```

## vault.md

```markdown
# Seed vault
| Idea | Stage | Why it didn't make it | It comes back if… |
|---|---|---|---|
```

## report.md

```markdown
# <Name>: report

## What happened
1. … (plain words, one line per step)

## What you gave me
## The winner and the runners-up
## How each differs from the obvious answer
- <idea>: stands out / modest, because …
## What got filtered out
## Would another run land here?
- Stable: … · Fragile: …
## How good the brief was: N/10
## What the cards did
| Card | Credit (winner / shortlisted / taught / none) | Distance | How |
|---|---|---|---|
Control vs. cards: mean distance <cards> vs. <control> vs. cold <cold>; menu slots won: cards N, control N
## Cost
```
