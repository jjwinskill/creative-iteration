---
name: creative-iteration
description: An agent-led idea generator that turns a vague want ("I want to do this thing but don't know what it should look like") into the best few ideas, seen from many outside perspectives. Agents fan out about 30 sketches from a fetched pool of real candidates or precedents, shaped by randomly drawn thinking moves from real people and trades, a judge filters them, the person picks from a short menu, and the picks are developed, attacked and delivered as an idea dossier ready for strategy and planning. Use whenever someone has a loose brief or a "what should I build / make / do" question and wants fresh, non-obvious ideas, for example "build grinder grindr", "show me a new way to build an electric guitar", "I've got a pile of scrap wood, what should I make", "I need an idea for a side project", or "help my daughter with reading", even if they never say "creative iteration". Not for planning or building an idea that's already chosen.
---

# Creative Iteration (v0.7)

**What it's for:** going from "I want to do this, but I don't know what it looks like" to the best few ideas. Strategy and planning come afterward, as a separate step.

**Why it works:** left alone, a model gives the obvious answer, and asking it for "ten wild ideas" gives the same ten every time. This skill brings outside perspective in from places the model doesn't control: a pool of real candidates or precedents fetched from published sources, randomly drawn thinking moves, constraints and seed material. Then it spends judgment on choosing, not generating. Mutation is cheap and dumb; selection does the work.

**Outside material beats instructions.** In the v0.5 tests, what widened the ideas was data from outside the model (a fetched pool, fetched checks). Telling agents to behave differently (tag your claims, avoid the typical, pick the least likely) changed little. When a stage needs more range, give it material, not rules.

**Who decides:** the person, at two short gates. People are bad at specifying what they want and good at reacting to what's in front of them, so the gates are menus, not questionnaires. Nothing expensive happens to an idea the person hasn't picked.

## The anchor: tight 0, fixed why, loose what

- **0, held tight:** the honest situation. Who it's for, everything that already exists (people, materials, code, past work), what hurts, the hard limits.
- **The why, fixed:** the goal that doesn't move, plus a **why-test** that says how we'd know an idea serves it.
- **The what, loose:** that's what this skill finds.

**The audience dial** (me / a few / many) says whose taste the ideas have to satisfy. **The drift dial** says how far to wander:

| Setting | The why is worded… | Ideas may… | The filter favors |
|---|---|---|---|
| **Refine** | as given | improve the person's idea, staying the same kind of thing | fit |
| **Stretch** (default) | as given | change form while serving the same why | fit, with distance from the obvious answer as the tiebreak |
| **Surprise** | one level up: the need under the request | be a different kind of thing entirely | distance, among ideas that fit and are feasible |

## Run folder

Make `runs/YYYY-MM-DD-<slug>/` in the current working folder unless the person names another place. Templates are in `references/templates.md`.

| File | Holds |
|---|---|
| `brief.md` | The intake answers, 0, the why and why-test, both dials, the tension register, the brief score, the obvious answer |
| `rounds/problems.md` | The problems found and the framing |
| `rounds/pool.md` | The numbered pool with source links, and the slices dealt |
| `rounds/fanout.md` | Every sketch, the unprompted lists, the wells, the filter's scores, the menu, the person's picks |
| `rounds/grounding.md` | The menu existence check (internal) |
| `rounds/priorart.md` | The prior-art check on each pick (originality briefs only) |
| `rounds/develop.md` | The developed concepts and the attack |
| `rounds/factcheck.md` | The dossier fact-check and the corrections made |
| `vault.md` | Ideas that didn't make it, why, and what would bring each one back |
| `dossier.md` | The output: the winner and the runners-up |
| `report.md` | The plain-English report |
| `metrics.json` | Agents, approximate tokens, minutes, sketches, groups, menu distances, wells, pool size and sources, fact-check counts |

## Separation rules, and why

These keep the outside perspective real and the choosing honest. Breaking one quietly turns the run back into one model agreeing with itself.

1. **Never read `deck/deck.json`.** Draw with `scripts/draw.py` and see only what it prints. Knowing the deck primes you, and the draw stops being outside randomness.
2. **Use the script for random choices** (`--pick`), and for shuffles.
3. **The lead never judges its own ideas.** It orchestrates, merges and writes. Fresh agents score, and the person picks.
4. **Framings state the problem and the principle, never an example technique, and they keep the person's priorities exactly as stated.** In run 3, one example in the framing ("resaw and bookmatch") showed up in four of five ideas. In run 5, "extra points for Pokémon" became "the real job is to pair with Greninja," and all 16 sketches came back Pokémon. A bonus stays a bonus: when the intake marks something as a bonus, one sketch generator is told to ignore it entirely.
5. **Judges see ideas unlabeled and shuffled,** with the cold answers mixed in.
6. **The brief block is the agents' only source of facts.** Every role prompt says so, and tells the agent to ignore anything else it knows about the person or this project, including names in file paths or the environment. Agents inherit project and memory context: run 4's "cold" answers cited the person's files, and in the Pi run a problem agent took the person's name from the home-folder path. **The lead scrubs it:** before passing any agent's output on, remove names and details about the person that aren't in the brief block, and log the removal.
7. **The lead doesn't patch fatal flaws.** If the attack finds one in a developed concept, show it to the person with the flaw named. Or, in cook mode, run a small fix round (two generators get the concept and the flaw, and the filter judge picks). In two earlier runs, the decisive late fix was the lead's, which kept the cards out of it. Correcting a *fact* the fact-check marks wrong is different, and the lead does that (see Output).
8. **Real-world specifics come from fetched sources, not model memory.** The pool is fetched, the menu is checked for existence, the developers check source fidelity, and the dossier is fact-checked. Generators may work from memory; nothing reaches the person as fact until a fetched source backs it. Don't make agents tag their memory claims: in the v0.5 test, about 119 such tags changed no decisions.

Role prompts are in `references/roles.md`. Models: haiku for cold answers, sonnet for everything else.

## Stage 0: Intake and brief

**Say the scope first.** If the request asks for more than ideas (a plan, a design, a build), say in the intake message that this run finds and develops the idea, and that planning is a separate step afterward (see Handoff).

Ask up to **five questions in one message**, chosen from the gaps that would change the ideas most, **written in the intake template** in `references/templates.md`: one slot per question, one thing per slot. In the Pi run, "which room, and who else uses it?" got an answer to the room only, and the fact that decided the winner (the person's kids) surfaced at Gate 2. In the guitar run, the rule was in the skill and the lead still bundled "skills, tools and budget" into one question. **Always include the role question and the who-else question.**
- **their role:** what will *they* actually be doing during it? In run 5, nobody asked, and every design solved a job the person doesn't have.
- **who else:** who else will use it, see it, or live with it?
- who it's for
- where it lives or what it has to fit
- the glad moment (a year from now, what makes them glad they did it?)
- the no list
- what they want out of making it

Skip any already answered, don't follow up, and fill the rest with marked assumptions. Infer the drift setting if it isn't given.

**Context stays context.** Only the why, the no list and the stated limits are requirements. Everything else the person tells you (a past project that failed, a story about how they work) is **background**: label it that way in the brief block. In the Pi run, a story about a pedal that died at debugging became problem 1 for both problem agents and then a principle in the framing, and most sketches argued for themselves as multimeter-testable. It's the same failure as run 5's bonus, through a new door.

**Assumptions come only from this brief, never from earlier runs or memory.** In run 5, the lead filled an unanswered question with "a full woodshop, $75" from an earlier exercise, and every agent reached for plywood. When a gap would bend the ideas (materials, budget, skills), mark it **unknown** and tell the agents the method is open, rather than guessing from context.

Write `brief.md` with a **tension register** (pairs of demands that pull against each other; at least four), and **score the brief** 1–10:
- Room to move for the drift setting?
- Nothing missing from 0?
- Audience confirmed?
- Four or more real tensions?

Below 7, fix it or ask.

**Build the brief block**, the only text agents get about the person. It has three labeled parts:
- **Their words:** the intake answers verbatim, never paraphrased, each labeled **requirement** (the why, the no list, limits) or **background**. Run 5's paraphrase turned "trick-or-treating with the kids" into "handling kids and candy."
- **Assumptions:** each one marked with where it came from (inferred from their words, or a default).
- **Unknowns:** gaps left open on purpose (for example, "making method: open").

**Make a second, requirements-only version** for the roles that seed ideas (the cold samplers, the retrieval agent, the sketch generators, the control and the wild card): the same block with every background line removed. Labels alone don't stop background from steering. In the guitar run, "shoegaze" was labeled background, and still about 7 of 12 menu items were reverb or ambience ideas. Tensions drawn from background are left out of it too: mark them **(background)** in the register. The full block goes to everyone else: the problem agents, the filter, the judges, the developers and the adversary. Background helps judge fit; it shouldn't seed the ideas. Gate 0 shows the full block.

**Gate 0: "Is this you?"** Show the person the brief block and ask them to correct anything wrong, in one quick reply. This is the cheapest gate in the run and catches the lead's mistakes before every agent inherits them. Skip it only if the person explicitly says to. Log the reply verbatim.

**Cold answers:** two cold samplers (haiku) answer the brief with no cards. That's **the obvious answer**, the reference for distance. (Six cold samplers cost about 340k tokens in the v0.5 test and still missed the real wells, so two is enough.)

**Known wells:** open this skill's `data/wells.md`, your own well ledger, and copy the section matching this kind of brief into `brief.md`, if one exists. Wells are answers models keep reaching for. The ledger is about model habits, not the person, so it doesn't break rule 6. It starts empty and grows with your runs; it's local and never committed.

## Stage 1: Problems (two agents)

Draw three moves (`draw.py --moves 3 --wiki 1 --run <slug> --stage problems`). Two agents run in parallel:
- **One problem agent** writes one underlying problem per card.
- **One no-card control** writes three problems.

Merge them. Update the tension register, and write **one framing paragraph**: the real problem and the principle a good idea must honor (rule 4). **Principles come only from requirements.** A problem drawn from background stays a tension, never a principle. The person sees the framing at Gate 1 and can correct it.

## Stage 1b: The pool (one retrieval agent)

In the v0.5 test, a fetched pool was the only change that widened the ideas *and* produced the best-rated ones. One **retrieval agent** (sonnet, with web) builds a numbered pool of about **80 real entries, each with its source URL**, from **at least 6 published sources** that span different regions, eras and kinds. The pool takes one of two forms:
- **Candidates,** when the brief chooses among real things (books, places, products, gifts, recipes, people, events). Each entry is something the person could pick. For books, that might mean international prizes across languages, national canons, translated-fiction and genre award lists.
- **Precedents,** when the brief asks for something to make or do. Each entry is a real work, design, practice or project, from anywhere, that answered a nearby need. Sketches build *from* precedents; they don't copy them.

Write it to `rounds/pool.md`. Then deal slices by script, so the lead never picks who sees what: `scripts/deal.py --pool <N> --hands g1:15 g2:15 g3:15 g4:15 control:15 wild:5`. Record the slices in `pool.md`.

## Stage 2: Fan-out (about 30 sketches)

Draw `--moves 13 --constraints 4 --wiki 1 --run <slug> --stage fanout`, then assign in draw order (the draw is already random):
- **Four sketch generators.** Each gets **three moves**, one constraint, its pool slice and the known wells. Before it reads its slice, it names the 3–4 answers it would give unprompted, each with a guess at how likely a typical model would suggest it (0–100%). Those lists feed the well map. (Slices don't overlap, so only the unprompted lists can show many agents reaching for the same thing.) Then it writes **six sketches**, each built from an entry in its slice. Each move shapes at least one sketch, **the constraint shapes exactly two**, and each sketch is a *different kind of thing* from the other five. (In the Pi run, "smell and touch only" applied to all six, so all six came back as scent machines and four were merged as duplicates.) Three moves, not six: the pool already widens, and in the v0.5 test, cards stacked on slices over-constrained the generators (fit 5/24 with cards vs. 3/6 for the control).
- **One no-card control.** It gets a slice and the known wells, and writes six sketches under the same rules.
- **One wild card.** It gets the 13th move, the seed and 5 pool entries, and attacks a tension picked by the script. It writes one strange sketch and says what it reveals.

**Every sketch must be the kind of thing the brief asks for** (if it asks for a book, a book). In the v0.5 test, one generator wrote five sketches about how to run the blog series instead.

In *surprise*, one generator is told not to propose the obvious kind of thing. **When the intake marks anything as a bonus, another generator is told to ignore that bonus entirely** (rule 4); pick both by `--pick`. Sketches are short (under about 80 words): what it is, which pool entry it builds from, why it serves the why, and which move shaped it.

## Stage 3: Filter, wells and menu

One fresh **filter judge** gets every sketch plus the two cold answers, shuffled and unlabeled. For each, it gives:
- the **duplicate group** it belongs to
- **distance** from the obvious answer, 1–5
- **feasibility** within the 0 (fine / risky / dead), with one reason
- **fit** to the why (yes / partly / no)
- **forced fit:** yes, if the sketch bends its pool entry to make the idea work

With more than about 40 sketches, split them across two filter judges and have the second also group duplicates across the whole list. Otherwise use one judge.

**Map the wells** (the lead, mechanically). A sketch is a **well** when its central idea or chosen item:
- is in the known wells from the ledger,
- appears in the unprompted lists of 3 or more agents, or
- matches both cold answers.

In the v0.5 test, wells came from what generators reached for, and they repeated across runs (*Middlemarch*, *War and Peace*, *Remains of the Day*), while a map built from cold samples missed them. Wells are kept, never discarded: likeness isn't badness.

**Build the menu:** drop anything dead or no-fit, and keep one per duplicate group.
- **About 8 non-well items** ordered by the drift setting's preference. Forced fits rank below clean fits at equal distance.
- **Plus 2 wild slots** for what the main ordering underweights, so it still reaches the person. In *refine* and *stretch*, the two highest-distance feasible ideas below the cut. In *surprise*, where the main list is already ordered by distance, the two best fits below the cut. (In the Pi run, surprise mode's wild slots became just the next two in line, and the winner came from one of them.)
- **Plus a convergent lane:** up to 2 wells, the strongest, labeled "well" with where they came from. They compete like everything else.
- **Plus the obvious answer** as a labeled reference.

**Grounding pass:** one grounding agent (sonnet, with web) checks every menu item with about one fetch each: does the thing exist, and is its key specific right? It marks each **verified / unverified / wrong**. Drop "wrong" items and refill from the next in order; label "unverified" ones. Write it to `rounds/grounding.md`. It's internal: the person sees only the word "unverified". It costs about one agent, and in the v0.5 test it changed two decisions. On originality briefs, it also notes any sign that the idea itself already exists; that's a first screen only, and Stage 4a does the real check.

The full scored list is always available on request.

## Gate 1: the menu (the person)

Show the framing and the menu, each item in one line with its distance. Ask the person to **pick two or three, veto any, and add a note** if they like. Log their words verbatim.

**Cook mode:** three judges with different stakes (`references/roles.md`) pick the top three instead, using `references/click.md`. They get the grounding notes.

## Stage 4a: Prior art (originality briefs only)

When the why, the why-test or the no list demands novelty ("never been done", "original", "the first"), the novelty claim is the requirement that matters most, so check it deeply before anything is developed. In the guitar run, the menu check made 1–2 searches per item and found nothing. The winner's closest prior art (an expired patent for the same trigger, plus studio plugins built on the same principle) surfaced only afterward, while the plan was being written.

**One prior-art agent per pick** (sonnet, with web), in parallel. Each searches every kind of source:
- patents
- shipping products and retailers
- software, plugins and studio techniques
- research papers
- DIY and maker forums
- **the same principle in another medium or field**

It rates the pick with links:
- **known:** someone has done it
- **known in principle, new in form:** the idea exists elsewhere; this form or medium is new
- **no prior found:** list the queries tried

Write it to `rounds/priorart.md`, and give each rating to that pick's developer, who reshapes toward the genuinely new part. A "known" pick goes to Gate 2 labeled as such, not dropped: the person decides.

## Stage 4: Develop and attack

- **One developer per pick** expands the sketch into a short concept: what it is, how it works, why it fits the why, what it would take, the cheapest first test against reality, and the biggest risk. The person's note goes in the prompt, along with the prior-art rating on originality briefs.
- **One adversary** then attacks all the concepts at once, without ranking them: the strongest reason each one fails, labeled **fatal**, **fatal unless** (a premise about the person that, if true, saves it), or a **scar**. In the Pi run, all three picks were called fatal for want of one fact each, and one sentence from the person settled it.

## Gate 2: the choice (the person)

Show each "fatal unless" as a **question to the person** before anything else. Then show each developed concept with its attack, its **prior-art rating** on originality briefs, its **source-fidelity rating** when it rests on a source (run 6: this is what lets the person speak with authority, and it reshaped two of four picks), and **the premises it depends on** (the developer lists them), so a wrong assumption is visible at a glance. The person chooses one, a combination, or **"go again clean"**: a fresh fan-out after correcting whatever premise was wrong. A combination they ask for goes back through the adversary once.

**Cook mode:** the judges choose. If they converge on a combination, it gets attacked once.

## Output: the idea dossier

Write `dossier.md`: the chosen idea, then the runners-up. Each with:
- what it is
- why it fits
- distance from the obvious answer
- what it would take
- the cheapest first test against reality
- the biggest risk

Include the vault, and on originality briefs, the prior-art rating with its links.

**Fact-check the dossier.** One fact-checker (sonnet, with web) checks every real-world claim in `dossier.md` against fetched sources and marks it verified, unsupported or wrong. The lead fixes every wrong line, marks unflagged unsupported ones "unverified", and logs both in `rounds/factcheck.md`. In the v0.5 test, this pass found the only wrong claim in four documents, a confident plot line a developer wrote, plus 9 gaps the documents hadn't flagged.

## Handoff: this skill doesn't plan

The run ends at the fact-checked dossier. **Don't write a plan, a design or a build inside the run,** even when the person asked for one. In the guitar run, the lead went on to write a 1,600-word design plan in the same session. It was well researched, but no stage gated it, attacked it or fact-checked it.

Instead, end the report with the handoff: the dossier is the brief for planning. Offer the person the planning step as a separate run, using the suite's planning skill when it exists. Until then, offer a fresh session that takes `dossier.md` as its brief, so planning starts clean rather than inheriting this run's agents and framing.

## Card tracking

- **Log every draw** with `--run` and `--stage`.
- **After the run, credit every card and seed:**
  - `winner`: the chosen idea came from its sketch
  - `shortlisted`: it made the menu
  - `taught`: it changed the framing or the tensions
  - `none`

  Each credit includes the sketch's distance: `draw.py --run <slug> --stage <stage> --credit <id> --effect <effect> --distance N --note "…"`.
- **Credit the control's sketches as `control`, and the cold answers as `cold`.**
- `--stats` compares card-driven distance against the control and the cold answers across runs. That's how we learn whether the cards widen the spread.

## Reporting

Write `report.md` and end in chat with the same content, in **plain words**: run vocabulary stays in the files. The report answers, in order:
1. **What happened:** short, numbered, in order.
2. **What you gave me.**
3. **The winner and the runners-up,** two or three sentences each.
4. **How each differs from the obvious answer:** *stands out* or *modest*.
5. **What got filtered out,** and why.
6. **Would another run land here?** The stable parts (several agents reached them) and the fragile ones.
7. **How good the brief was.**
8. **What the cards and the pool did:** credits and distance; the control vs. the cards; how many menu items came from far-flung pool entries; the wells found.
9. **Cost:** agents, approximate tokens and minutes.
10. **What's next:** the handoff to planning (see Handoff).

## Afterward

- Write `metrics.json`.
- Add any new wells to `data/wells.md`, and bump the run count on wells seen again. Create the file if it's missing: one `## <kind of brief>` section per kind, each a table of well, runs, and how it showed up. A well goes in when it shows up in two or more runs, or when one run marks it a well. Wells are kept, never deleted.
- If you maintain the skill, append what the run taught it to your own run log, timestamped with `date -u`. The public record of past runs is `docs/creative-iteration/LESSONS.md` in this repo.
