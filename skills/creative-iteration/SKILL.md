---
name: creative-iteration
description: An agent-led idea generator that turns a vague want ("I want to do this thing but don't know what it should look like") into the best few ideas, seen from many outside perspectives. Agents fan out about 30 sketches from a fetched pool of real candidates or precedents, the strongest are mutated through thinking moves drawn from real people and trades, a judge filters them, the person picks from a short menu, and the picks are developed, attacked and delivered as an idea dossier ready for strategy and planning. Use whenever someone has a loose brief or a "what should I build / make / do" question and wants fresh, non-obvious ideas, for example "build grinder grindr", "show me a new way to build an electric guitar", "I've got a pile of scrap wood, what should I make", "I need an idea for a side project", or "help my daughter with reading", even if they never say "creative iteration". Not for planning or building an idea that's already chosen.
---

# Creative Iteration (v0.12)

**What it's for:** going from "I want to do this, but I don't know what it looks like" to the best few ideas. Strategy and planning come afterward, as a separate step.

**Why it works:** left alone, a model gives the obvious answer, and asking it for "ten wild ideas" gives the same ten every time. This skill brings outside perspective in from places the model doesn't control: a pool of real candidates or precedents fetched from published sources, thinking moves drawn at random from real people, trades and traditions, and seed material. The moves work as **lenses, never content**: each is stripped to a one-sentence operator and applied to ideas that already fit, changing *how* they work. Then the skill spends judgment on choosing, not generating. Mutation is cheap and dumb; selection does the work.

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
| `rounds/references.md` | Principles and register distilled from the person's references (when they name any) |
| `rounds/problems.md` | The problems found and the framing |
| `rounds/pool.md` | The numbered pool (or subject and mechanism pools) with source links, and the slices dealt |
| `rounds/operators.md` | The drawn cards, their operators and the leak check |
| `rounds/fanout.md` | Every sketch, the unprompted lists, the wells, the filter's scores, the seeds and mutations, the menu, the person's picks |
| `rounds/grounding.md` | The menu existence check (internal) |
| `rounds/priorart.md` | The prior-art check on each pick (originality briefs only) |
| `rounds/develop.md` | The developed concepts and the attack |
| `rounds/factcheck.md` | The dossier fact-check and the corrections made |
| `vault.md` | Ideas that didn't make it, why, and what would bring each one back |
| `dossier.md` | The output: the winner and the runners-up |
| `report.md` | The plain-English report |
| `metrics.json` | Cost in dollars from `scripts/cost.py` (lead, lean, browse, per agent, with starting context), minutes, sketches, mutations, groups, menu bands and distances, wells, pool size and sources, fact-check counts |
| `agents/<role>/` | Each agent's own folder: its output file and anything it writes |
| `agents/block-full.md`, `agents/block-req.md` | The two brief blocks, written once; prompts point to them |
| `cache/` | The shared fetch cache, written only by `scripts/fetch.py` |

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
9. **Verify agents' claims, and lock picks.** Agents will satisfy a check any way they can on paper. In the guitar work, one passed a horn-width check by moving the points the check measured from, and two developers quietly changed outlines the person had picked. So:
   - checks measure the artifact itself, never an agent's own numbers or labels;
   - the lead re-runs every check before anything reaches the person;
   - a pick is **locked**: developers deepen it but don't swap its core (the central idea, the chosen item, the picked geometry). The lead compares each developed concept against the picked sketch, and any drift goes back.
10. **One folder per agent.** Agents that write files work in their own folder under the run (`agents/<role>/`) and don't read others', except files their prompt names. In the guitar run, agents sharing a scratch folder ran each other's scripts. In the v0.11 run, default agents wrote into the shared session scratchpad anyway, and one hit a script clash; the `ci-browse` type now states the rule in its system prompt. The one shared folder is `cache/`, and only `scripts/fetch.py` writes it.

Role prompts are in `references/roles.md`; shape briefs also follow `references/shape.md`. Models: haiku for cold answers, sonnet for everything else, and Opus for a picture judge.

## Cost

Priced from its transcripts, the v0.11 run cost **$31.80**: the lead (the orchestrating session) $13.24, 14 default browsing agents $16.41, and 15 lean agents $2.15. Plain Claude answered the same brief for **$2.54**. The cards are cheap: the operator, problem, mutation and wild-card agents together cost about $0.40, so keep them. The money goes to the lead's context and to browsing agents. Four fifths of the browsing went on checks and development after the menu, much of it repeated searching. The full analysis is in `docs/creative-iteration/COST.md`. The aim is about half the v0.11 cost for a gated run.

**Three agent types:**
- **`ci-lean`** (`agents/ci-lean.md`), for roles that need no web: cold sampler, operator agent, problem agents, generators, the control, wild card, filter, mutation agents, judges and adversary. It starts at about 4k tokens instead of 54k.
- **`ci-browse`** (`agents/ci-browse.md`), for roles that need the web: reference, retrieval, grounding, prior art, developers and fact-checker. It carries five tools instead of the full set, keeps to its own folder and to a call budget, fetches through the cache, and returns a short summary.
- **The default agent** only when one of these isn't installed (see the README). Say so in the report.

**Keep the lead thin.** The lead re-reads its whole context on every call, so whatever enters its context is paid for again on every call after that. In the v0.11 run, its average context was 260k tokens over 141 calls.
- **Write the brief blocks to files once** (`agents/block-full.md`, `agents/block-req.md`), along with slices and inputs. Prompts point to the files instead of pasting them.
- **Agents write their own output files** (`agents/<role>/out.md`) and return one line (lean) or a summary under 120 words (browse). The lead reads a file only for what its next step needs.
- **Never retype an agent's output.** Build judge inputs with `scripts/blind.py` (it shuffles and labels sections from agents' files), and assemble round files from agents' files with the shell (`cat`, a heading per agent). The lead writes only its own part: tables, decisions and the person's words. In the v0.11 run, the lead retyped about 120k characters of round files.
- **Batch file work into one shell call,** and use scripts to count or extract from big files rather than reading them in.

**Spend browsing where it decides something.**
- **One shared fetch cache.** Every browsing agent fetches through `scripts/fetch.py` with the run's `cache/` folder, keeping only the fields or snippets it needs. In the v0.11 run, the same search results were fetched up to five times by different agents.
- **Call budgets** go in each browsing prompt (`references/roles.md`): retrieval 25, grounding 2 per item, prior art 20 per pick, developer 10, fact-checker 20. The v0.11 developers made 22–45 calls each, mostly repeating the prior-art searches.
- **Closeness is checked at the menu** (see the grounding pass), so a pick that's a near copy of something real is flagged before anyone develops it. In the v0.11 run, a pick that the person cut at Gate 2 as too close to an existing work had already cost a prior-art agent and a developer.
- **One prior-art pass covers near relatives too** (Stage 4a), so there's no second closeness pass. **Developers get its file** and don't search the catalog again.

**Measure it.** At the end, run `scripts/cost.py --since <the run's start> --json agents/cost.json`. It prices the lead and every subagent from Claude Code's own transcripts, by model, with cache reads, cache writes and output separated. Put the totals in `metrics.json` and the report. Token counts from the Agent tool aren't comparable across runs: some are a final context size, others a sum over calls.

## Stage 0: Intake and brief

**Say the scope first.** If the request asks for more than ideas (a plan, a design, a build), say in the intake message that this run finds and develops the idea, and that planning is a separate step afterward (see Handoff).

**Grill, lightly.** Intake is a short interview in rounds, adapted from Matt Pocock's `grilling` skill (github.com/mattpocock/skills). The goal is to draw out the requirements the person didn't think to say, not to settle every detail. In both the Pi and pinball runs, the fact that decided the run surfaced only at a gate: the person's kids, and the missing hook and feel.
- **Map the brief as a tree.** Some answers open new questions: "who are the others?" only makes sense after "who else plays?"; "what should a hand-shaped body feel like?" only after "is comfort the point?". The **frontier** is every question whose prerequisites are settled.
- **Ask the whole frontier in one round,** numbered, one thing per question, in the intake template in `references/templates.md`. Give each question a **recommended answer**, worded so "yes" accepts it.
- **Recommendations come only from the person's own words or a labeled default,** never from the lead's taste, earlier runs or memory. Mark each one *(from your words)* or *(default)*. Give **no recommendation** for taste questions (the hook, the feel, the no list, what they love). Ask those open, because a "yes" to the lead's guess there becomes the lead's taste. Run 5's pollution came from exactly this kind of guess.
- **Facts are the lead's job; decisions are the person's.** Don't ask for anything you can look up, such as what a reference is or how it's built. Send the reference agent or a quick search instead.
- **Stop at three rounds,** or sooner when the frontier holds only questions whose answers wouldn't change which ideas win. The *what* stays loose, because that's what the run finds. Grilling is about the 0, the why and the limits, not the solution.

The first round always includes the **role question** and the **who-else question**. In the Pi run, "which room, and who else uses it?" got an answer to the room only. In the guitar run, the lead bundled "skills, tools and budget" into one question.
- **their role:** what will *they* actually be doing during it? In run 5, nobody asked, and every design solved a job the person doesn't have.
- **who else:** who else will use it, see it, or live with it?
- who it's for
- where it lives or what it has to fit
- the glad moment (a year from now, what makes them glad they did it?)
- the no list
- what they want out of making it
- **the occasion,** when there is one (a holiday, a season, a launch): it's a requirement, not just a deadline. In the gift run, Christmas only set the date, and nothing checked that ideas suited a Christmas gift.

**Audience-facing work** is anything other people will play, read, watch, wear or be pitched: a game, a theme, a name, a story, a costume. For it, the grilling always covers these three, in whichever round their prerequisites allow:
- **who the others are:** ages, and what they're into. In the pinball run, "just the three of us" hid that one player was the person's kid.
- **the hook:** what would make them want to try it, from the name or one-line pitch alone?
- **the register:** what should it feel like?

The pinball run lost two full rounds to these. Its menus went esoteric (nobody could tell what the themes were), then domestic (graspable, but no pull), then kid comedy (pull, wrong feel). The person's reference machines carried all three answers implicitly, and nothing asked for them.

Skip any already answered, and fill whatever is left after the last round with marked assumptions. Infer the drift setting if it isn't given, and ask about it only if the brief points both ways.

**Context stays context.** Only the why, the no list, the stated limits, the hook and the register are requirements. Everything else the person tells you (a past project that failed, a story about how they work) is **background**: label it that way in the brief block. In the Pi run, a story about a pedal that died at debugging became problem 1 for both problem agents and then a principle in the framing, and most sketches argued for themselves as multimeter-testable. It's the same failure as run 5's bonus, through a new door.

**Assumptions come only from this brief, never from earlier runs or memory.** In run 5, the lead filled an unanswered question with "a full woodshop, $75" from an earlier exercise, and every agent reached for plywood. When a gap would bend the ideas (materials, budget, skills), mark it **unknown** and tell the agents the method is open, rather than guessing from context.

Write `brief.md` with a **tension register** (pairs of demands that pull against each other; at least four), and **score the brief** 1–10:
- Room to move for the drift setting?
- Nothing missing from 0?
- Audience confirmed?
- Four or more real tensions?

Below 7, fix it or ask.

**Turn limits into checks.** Write a **checks** list in `brief.md`: each limit and no-list item, and how it will be checked.
- **By code or a fetched source** wherever it can be measured: a size, a weight, a budget, a date, a word count, "never been done".
- **With a threshold calibrated on real examples** wherever the word is qualitative: "durable", "readable", "light", "comfortable". Measure real things that clearly pass and clearly fail, and set the line between them.
- **Marked "the person judges"** only when nothing can be measured: taste, feel, the hook.

In the guitar work, "durable" and "realistic to build" stayed words through the whole fan-out. They became checks (a horn-strength index calibrated on real guitars, minimum wood under the neck pocket) only after the person flagged weak horns. The filter, the developers and the adversary all work from this list.

**Build the brief block**, the only text agents get about the person. It has three labeled parts:
- **Their words:** the intake answers verbatim, never paraphrased, each labeled **requirement** (the why, the no list, limits) or **background**. Run 5's paraphrase turned "trick-or-treating with the kids" into "handling kids and candy."
- **Assumptions:** each one marked with where it came from (inferred from their words, or a default).
- **Unknowns:** gaps left open on purpose (for example, "making method: open").

**Make a second, requirements-only version** for the roles that seed ideas (the cold samplers, the retrieval agent, the sketch generators, the control and the wild card): the same block with every background line removed. Labels alone don't stop background from steering. In the guitar run, "shoegaze" was labeled background, and still about 7 of 12 menu items were reverb or ambience ideas. Tensions drawn from background are left out of it too: mark them **(background)** in the register. The full block goes to everyone else: the problem agents, the filter, the judges, the developers and the adversary. Background helps judge fit; it shouldn't seed the ideas. Gate 0 shows the full block.

**References come in two kinds,** and the grilling settles which kind each one is:
- **A seed** is a reference the person wants the result *derived from* ("inspired by the Parker Fly"). It's a requirement, and the idea-seeding roles get the real thing: its geometry, text or specs, not a description. Distance is then measured from the seed, and the pushes away from it create the originality. In the guitar work, agents given a description of the Fly drifted to "some kind of strange in between," while agents seeded from its fitted outline produced the designs the person kept.
- **A taste reference** is something they love for how it plays or feels ("pins I admire for how they're made"). It's handled as below.

**Taste references** are background, so their subjects don't seed the ideas. But they carry what the person values, so distill it first. One **reference agent** (browse) reads reviews and write-ups of each, and returns two subject-free lists:
- **play or use principles:** how it works, and why people love it
- **register words:** how it feels

Both lists become requirements, marked "distilled from the references." The names, the subjects and the person's quotes about them stay background, and Section B of the agent's report (per-reference notes with links) goes only to the judging and developing roles. In the pinball run, the principles alone kept the loops strong, but with no register, the tone drifted.

**Quote check.** Before Gate 0, scan every requirement line for a taste reference's subject (seeds are meant to be seen): its names, settings, creatures and objects. Split any such line. The principle becomes the requirement, in your words, marked as a paraphrase for the person to approve at Gate 0. The verbatim quote moves to background. In the pinball run, two requirement lines quoted the person describing their references ("overload a nuclear reactor", "battling of the monsters"), and those subjects became two of the run's four wells.

**Gate 0: "Is this you?"** Show the person the brief block and ask them to correct anything wrong, in one quick reply. This is the cheapest gate in the run and catches the lead's mistakes before every agent inherits them. Skip it only if the person explicitly says to. Log the reply verbatim.

**Cold answers:** one lean cold sampler (haiku) gives two different answers to the brief, with no operators or pool. That's **the obvious answer**, the reference for distance, and plain Claude's strongest move. In the gift experiment, plain Claude's well-worn letters book was the person's favourite gift, so the obvious answers also become **seeds** for the mutation round (Stage 3b).

**Known wells:** open this skill's `data/wells.md`, your own well ledger, and copy the section matching this kind of brief into `brief.md`, if one exists. Wells are answers models keep reaching for. The ledger is about model habits, not the person, so it doesn't break rule 6. It starts empty and grows with your runs; it's local and never committed.

## Stage 1: Operators and problems

**Turn cards into operators first.** Cards carry a perspective (how a real person, trade or tradition decides) wrapped in a vivid story. In the gift experiment, the story leaked: a card about a duel produced duel gifts, and one about a piano roll produced a piano roll. Meanwhile the cards that worked were the ones whose move was a verb: *a small steady force over time*, *share the upkeep among those who benefit*, *let the owner decide the form*. So no agent sees a card. Draw all the run's moves at once (`draw.py --moves 10 --wiki 1 --run <slug> --stage operators`), and give them to one lean **operator agent**. It rewrites each move as an **operator**: one sentence about *how to change an idea*, with no names, places, objects, materials or story from its source. Then run `scripts/leakcheck.py` on its output. It flags any distinctive word an operator shares with its card's source or move; re-run the agent on flagged ones. Constraint cards are no longer drawn: in the gift and Pi runs, every constraint became the idea's setting or material.

Assign operators in draw order: 3 to the problem stage, 6 to the mutation round, and 1 to the wild card.

**Problems (two lean agents, in parallel):**
- **One problem agent** reframes the brief through each of its three operators: one underlying problem per operator.
- **One control** finds three problems with no operators.

Merge them. Update the tension register, and write **one framing paragraph**: the real problem and the principle a good idea must honor (rule 4). **Principles come only from requirements.** A problem drawn from background stays a tension, never a principle. If a problem agent warns about a pull in the brief (in the gift run, it warned that her reading would pull ideas toward book themes), carry the warning into the framing as a tension, not a clause. The person sees the framing at Gate 1 and can correct it.

## Stage 1b: The pool (one retrieval agent)

In the v0.5 test, a fetched pool was the only change that widened the ideas *and* produced the best-rated ones. One **retrieval agent** (browse) builds a numbered pool of about **80 real entries, each with its source URL**, from **at least 6 published sources** that span different regions, eras and kinds. The pool takes one of three forms:
- **Candidates,** when the brief chooses among real things (books, places, products, gifts, recipes, people, events). Each entry is something the person could pick. For books, that might mean international prizes across languages, national canons, translated-fiction and genre award lists.
- **Precedents,** when the brief asks for something to make or do. Each entry is a real work, design, practice or project, from anywhere, that answered a nearby need, **plus one line on what it does**, in words free of its props. Sketches borrow how a precedent works, never its objects or traditions, unless the brief asks for them. In the gift run, a Wagner morning piece and Japanese wish strips came through the pool as props, and the developers then pushed the gifts even closer to them.
- **Subjects plus precedents,** when the brief asks for a subject the audience has to recognize: a theme, a setting, a name, a topic. Build **two pools**:
  - a **subject pool** (about 60) of things the audience already knows and likes, across media and culture, that this medium hasn't used
  - a **mechanism pool** (about 60) of far-flung precedents for how it could work

  Each sketch takes its subject from its subject slice and its mechanics from its mechanism slice. In the pinball run, one far-flung pool did both jobs, and its precedents became the subjects: a steppe horseback game, a Foucault pendulum, an Edo clockwork archer. The loops were strong, and nobody could tell what the themes were.

Write it to `rounds/pool.md`. Then deal slices by script, so the lead never picks who sees what: `scripts/deal.py --pool <N> --hands g1:15 g2:15 g3:15 g4:15 control:15 wild:5`. With two pools, deal each separately. Record the slices in `pool.md`.

## Stage 2: Fan-out (about 30 sketches, no cards)

**No cards in the fan-out.** Across five runs, generators given cards landed no further from the obvious answer than generators without them (3.58 vs. 3.62 in the gift run), and in a blind test their ideas ranked last. Cards now work later, on ideas that already fit (Stage 3b).

- **Four sketch generators,** each with its pool slice and the known wells. Before it reads its slice, each names the 3–4 answers it would give unprompted, each with a guess at how likely a typical model would suggest it (0–100%). Those lists feed the well map. (Slices don't overlap, so only the unprompted lists can show many agents reaching for the same thing.) Then it writes **six sketches**, each built from an entry in its slice, and each a *different kind of thing* from the other five.
- **Two of the four are interest-blind.** When the brief carries a **taste list** (what the person or audience loves: hobbies, genres, favourite things), generators 1 and 2 get the brief without it. In the gift run, her current genre (romance) turned into romance tropes in every menu, and the person found them "overly saccharine". The filter, judges and developers still see the taste list, so fit is judged against it.
- **One control,** with a slice and the known wells and the full brief, under the same rules.
- **One wild card.** It gets its operator, the seed and 5 pool entries, and attacks a tension picked by the script. It writes one strange sketch and says what it reveals.

**Shape briefs** (a body, a profile, a part, a piece of furniture) need a **shape template**, never freehand drawing. In the v0.9 guitar run, agents wrote raw SVG coordinates: all 33 outlines passed the size checks, and the person rejected all 33 as "boxy blobs." A side project then built a guitar template that worked: 30 of 30 designs read as guitars, and the person kept seven as starting points. Follow `references/shape.md`, which covers:
- the template: named anatomy points and a curve rule, proven by reproducing real examples
- seeds: start from one real exemplar and push it
- checks calibrated on real objects
- a picture judge that only rejects defects
- true-scale sheets, locked picks, and development in layers (outline, then carve, then hardware)

**If no proven template exists for this kind of object, don't improvise one inside the run.** Run the idea search in words: what the shape does, which precedent it builds from, and its key proportions. Then offer building the template as its own project, before any drawing.

**Every sketch must be the kind of thing the brief asks for** (if it asks for a book, a book). In the v0.5 test, one generator wrote five sketches about how to run the blog series instead.

In *surprise*, one generator is told not to propose the obvious kind of thing. **When the intake marks anything as a bonus, another generator is told to ignore that bonus entirely** (rule 4); pick both by `--pick`. Sketches are short (under about 80 words): what it is, which pool entry it builds from, and why it serves the why.

## Stage 3: Filter, mutation and menu

**3a. Filter.** One fresh, lean **filter judge** gets every sketch plus the two cold answers, shuffled and unlabeled by `scripts/blind.py` from the agents' own files (each sketch a `### <idea name>` section), with the key kept for the lead. For each, it gives:
- the **duplicate group** it belongs to
- its **kind** (for a gift: an object, an experience, something made, something learned, a ritual; name the kinds that fit the brief)
- **distance** from the obvious answer, 1–5
- **familiarity,** likely / maybe / unlikely: would the person have thought of it themselves?
- **feasibility** within the 0 (fine / risky / dead), with one reason
- **fit** to each requirement and the occasion (yes / partly / no each)
- **transplant:** yes if the idea's content *is* a taste-list item, a precedent's prop or a card's subject, dressed up instead of transformed
- **pull,** 1–5: would the audience on the dial want it, from the one-line pitch alone?

With more than about 40 sketches, split them across two filter judges and have the second also group duplicates across the whole list. Otherwise use one judge.

**Map the wells** (the lead, mechanically). A sketch is a **well** when its central idea or chosen item:
- is in the known wells from the ledger,
- appears in the unprompted lists of 3 or more agents, or
- matches both cold answers.

Wells are kept, never discarded: likeness isn't badness.

**3b. Mutation: the lens round.** This is where the cards' perspectives come in: they change *how* a strong idea works, while its fit stays. Choose **six seeds** mechanically: the six highest-pull ideas with "yes" fit on every requirement and no transplant flag, including at least one well and one cold answer. If fewer than six have "yes" on everything (in the v0.11 run, none did), take ideas with no "no" on any requirement, ranked by pull and then by count of "yes", and log it. Two lean **mutation agents** each get three seeds and three operators. Each applies two operators to each of its seeds: six mutations per agent, twelve in all. A mutation keeps the seed's core and its fit, changes *how* it works, and must be something the person couldn't get by tweaking the seed (a different structure, timing, owner, form or scale). For example, a book of letters from her friends, put through "a small steady force over time", becomes one letter arriving each week through the year.

**3c. Score the mutations.** The filter judge scores the twelve mutations on the same rubric, with their seeds alongside for comparison.

**Build the menu for range.** Drop anything dead, any "no" on a requirement, and transplants; keep one per duplicate group. Show about **10 items in three bands**, so the person can see the novelty they're trading for:
- **Familiar and strong** (up to 3): wells and cold answers with strong fit, labeled as such. They're honest options.
- **A twist on the familiar** (about 4): the best mutations.
- **Out there** (at least 3): distance 4+, familiarity "unlikely", fit "yes".

Cover at least four different kinds across the menu. Within a band, order by fit, then distance, then **pull**, and only then by script. Show the obvious answer as a labeled reference.

**Grounding pass:** one grounding agent (browse) checks every menu item with about one fetch each: does the thing exist, and is its key specific right? It marks each **verified / unverified / wrong**. Drop "wrong" items and refill from the next in the band; label "unverified" ones. Write it to `rounds/grounding.md`. It's internal: the person sees only the word "unverified".

**On originality briefs, grounding also rates closeness.** For each item, with one or two searches of the field's own catalog, it names the nearest existing work and rates it **distinct**, **related but distinct** or **too close**. "Too close" means a near relative: the same trigger, reward or core move in the same kind of thing, even if the wording differs. **Calibrate it first** on one pair the brief or a past run settled as too close, and one as distinct. If no such pair exists, the agent proposes one from the catalog and says so. Show "too close" on the menu with the relative named; the person decides. In the v0.11 run, the menu check looked only for exact copies, and the person cut a pick at Gate 2 as "far too close" to an existing work, after it had been fully developed. Stage 4a still does the deep check.

The full scored list is always available on request.

## Gate 1: the menu (the person)

Show the framing and the menu, each item in one line with its distance. Ask the person to **pick two or three, veto any, and add a note** if they like. Log their words verbatim.

**Cook mode:** one lean judge agent holding three stakes (`references/roles.md`) picks the top three instead, using `references/click.md`, and gets the grounding notes. In the gift run, three separate judges per gate cost about 200k, mostly fixed context.

**A model's taste isn't the person's.** In the guitar work, a picture judge marked down two of the person's three favourite designs; its suggested threshold would have rejected everything they liked. So model judges and the filter **reject defects** (dead, no-fit, failed checks, blobs) and never cut for taste, and the **pull** score only breaks ties. In cook mode, the report says plainly that the picks reflect a model's taste, and keeps the runners-up close enough that the person can overrule them.

**When the person vetoes the menu,** the redo has to keep every requirement, not just the new one. In the pinball run, each veto note became the loudest requirement, and each round overcorrected: esoteric, then domestic, then kid comedy. The person quit from fatigue. So:
1. **Log the note verbatim** as a requirement in both versions of the brief block, and update the why-test.
2. **Carry forward what they said worked** (for example, "the loops are great") as a requirement too, so it isn't lost.
3. **Run a light redo first:** two sketch generators and the control, with fresh slices, aimed at the correction. That's about 18 sketches for a third of the cost. Run a full fan-out only if the person asks for it, or vetoes the light redo's menu too.
4. **The filter scores fit against every requirement separately** (yes / partly / no each). Anything with a "no" on any requirement leaves the menu, whichever round added that requirement.

## Stage 4a: Prior art (originality briefs only)

When the why, the why-test or the no list demands novelty ("never been done", "original", "the first"), the novelty claim is the requirement that matters most, so check it deeply before anything is developed. In the guitar run, the menu check made 1–2 searches per item and found nothing. The winner's closest prior art (an expired patent for the same trigger, plus studio plugins built on the same principle) surfaced only afterward, while the plan was being written.

**One prior-art agent per pick** (browse), in parallel. Each searches every kind of source:
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

**The same pass covers near relatives,** with the calibrated closeness rating from the grounding pass (distinct / related but distinct / too close), and names the three nearest works. In the v0.11 run, a separate closeness pass after Gate 2 cost about as much again as the prior-art pass and found what a near-relative search would have found the first time. It works within its call budget, fetching through the cache.

It also searches the field's own catalog (every field that has one), and **lists every source it couldn't reach**, with the hand searches that would close the gap (where to look, and which terms). With a key source unreachable, "no prior found" becomes "**no prior found in reachable sources**", and Gate 2 shows the hand-search list. In the pinball run, the main pinball databases blocked automated fetches, so the check could only clear the themes in the sources it could reach.

Write it to `rounds/priorart.md` (assembled from the agents' files), and give each pick's prior-art file to its developer, who reshapes toward the genuinely new part without repeating the searches. A "known" pick goes to Gate 2 labeled as such, not dropped: the person decides.

## Stage 4: Develop and attack

- **One developer per pick** expands the sketch into a short concept: what it is, how it works, why it fits the why, what it would take, the cheapest first test against reality, and the biggest risk. The person's note goes in the prompt, along with the prior-art file on originality briefs. A precedent the idea only borrowed from is not a source: **don't pull the idea toward it.** In the gift run, the developers' fidelity step pushed two gifts closer to a Wagner piece and Japanese wish strips, which the person read as props. Developers **name and link** every precedent they mention (the v0.11 fact-check found "a tabletop RPG" and "a folktale" left vague), and keep to a budget of 10 fetches: in the v0.11 run, the developers were the most expensive agents, mostly repeating prior-art searches.
- **Revisions after Gate 2 resume the same developer** (SendMessage), so it keeps its context instead of starting again.
- **One adversary** then attacks all the concepts at once, without ranking them: the strongest reason each one fails, labeled **fatal**, **fatal unless** (a premise about the person that, if true, saves it), or a **scar**. In the Pi run, all three picks were called fatal for want of one fact each, and one sentence from the person settled it.

## Gate 2: the choice (the person)

Show each "fatal unless" as a **question to the person** before anything else. Then show each developed concept with its attack, its **prior-art rating** on originality briefs, its **source-fidelity rating** when it rests on a source (run 6: this is what lets the person speak with authority, and it reshaped two of four picks), and **the premises it depends on** (the developer lists them), so a wrong assumption is visible at a glance. The person chooses one, a combination, or **"go again clean"**: a fresh fan-out after correcting whatever premise was wrong. A combination they ask for goes back through the adversary once.

**Cook mode:** the judge agent chooses, from its three stakes. If they converge on a combination, it gets attacked once.

## Output: the idea dossier

Write `dossier.md`: the chosen idea, then the runners-up. Each with:
- what it is
- why it fits
- distance from the obvious answer
- what it would take
- the cheapest first test against reality
- the biggest risk

Include the vault, and on originality briefs, the prior-art rating with its links.

**Fact-check the dossier.** One fact-checker (browse) checks every real-world claim in `dossier.md` against fetched sources and marks it verified, unsupported or wrong. The lead fixes every wrong line, marks unflagged unsupported ones "unverified", and logs both in `rounds/factcheck.md`. In the v0.5 test, this pass found the only wrong claim in four documents, a confident plot line a developer wrote, plus 9 gaps the documents hadn't flagged.

## Handoff: this skill doesn't plan

The run ends at the fact-checked dossier. **Don't write a plan, a design or a build inside the run,** even when the person asked for one. In the guitar run, the lead went on to write a 1,600-word design plan in the same session. It was well researched, but no stage gated it, attacked it or fact-checked it.

Instead, end the report with the handoff: the dossier is the brief for planning. Offer the person the planning step as a separate run, using the suite's planning skill when it exists. Until then, offer a fresh session that takes `dossier.md` as its brief, so planning starts clean rather than inheriting this run's agents and framing.

## Card tracking

- **Log every draw** with `--run` and `--stage operators`.
- **After the run, credit every card by what its operator did,** with the distance of the idea it shaped:
  - `winner`: a mutation or framing it shaped led to the chosen idea
  - `shortlisted`: a mutation it shaped made the menu
  - `taught`: it changed the framing or the tensions
  - `none`

  `draw.py --run <slug> --stage <stage> --credit <id> --effect <effect> --distance N --note "…"`
- **Credit unmutated sketches as `control`, and the cold answers as `cold`.**
- `--stats` compares the distance of operator-shaped ideas against the others and the cold answers across runs. That's how we learn whether the lens widens the spread.

## Reporting

Write `report.md` and end in chat with the same content, in **plain words**: run vocabulary stays in the files. The report answers, in order:
1. **What happened:** short, numbered, in order.
2. **What you gave me.**
3. **The winner and the runners-up,** two or three sentences each.
4. **How each differs from the obvious answer:** *stands out* or *modest*.
5. **What got filtered out,** and why.
6. **Would another run land here?** The stable parts (several agents reached them) and the fragile ones.
7. **How good the brief was.**
8. **What the operators and the pool did:** which operators' mutations reached the menu or won; each mutation's distance against its seed; how many menu items came from far-flung pool entries; the wells found.
9. **Cost:** dollars from `scripts/cost.py`, split into the lead, lean agents and browsing agents, with minutes. Compare it with the v0.11 run ($31.80) and with plain Claude on a similar brief (about $2.50), and name the most expensive agent.
10. **What's next:** the handoff to planning (see Handoff).

## Afterward

- Run `scripts/cost.py`, then write `metrics.json`.
- Add any new wells to `data/wells.md`, and bump the run count on wells seen again. Create the file if it's missing: one `## <kind of brief>` section per kind, each a table of well, runs, and how it showed up. A well goes in when it shows up in two or more runs, or when one run marks it a well. Wells are kept, never deleted.
- If you maintain the skill, append what the run taught it to your own run log, timestamped with `date -u`. The public record of past runs is `docs/creative-iteration/LESSONS.md` in this repo.
