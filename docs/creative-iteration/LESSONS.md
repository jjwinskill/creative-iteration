# What each run taught the skill

This is the record of what each test run taught Creative Iteration, from v0 to v0.6. We keep it so readers can see why each rule exists. Sections run in time order, oldest first.

## 2026-10-23 02:34 UTC: Run 1, a scaling lab (cook mode)

Shape: one Problems round and one Strategy round. 15 agents in all: a deck author, 3 cold samplers, 3 problem generators, 3 strategy generators, a wild card, an adversary and 3 judges. About 1M tokens, roughly 64k per agent, mostly fixed overhead.

What worked:
- **A sealed deck.** A fresh agent wrote it and the lead never read it. The draws were moves the lead would not have picked, and two of them shaped the winner and the runner-up.
- **The cold answers humbled the lead.** Two things the lead had scored as original came out of both cold samples unprompted.
- **Rediscovery.** All three problem generators reached the same core idea from unrelated moves. That suggests the idea was close to inevitable.
- **The wild card paid for what it taught.** Its idea lost, but it added a tension and survived as a footnote in the final whole.
- **The judges' combination question** ("what would beat your first pick?") produced the integrated winner.

Lessons:
- "Don't use any tools" lost an agent's report, because it could not hand back its answer. Fixed in the role prompts.
- Unanimous judges may share priors, not truth. Give each judge a different stake.
- The adversary volunteered a ranking. The adversary never ranks.
- A combined whole that comes out of judging must be attacked again.
- In cook mode, one cheap fresh judge should choose the framing.
- One set of cold answers can serve both stages.
- Anything the lead adds after judging is flagged as unjudged and goes into the next attack.
- Fewer, richer agents may beat more, thinner ones.
- Seed material from random wiki pages helped once. Kept for now.

## 2026-10-23 03:29 UTC: v0.1

The review of run 1: the run polished the person's idea instead of moving it, and the report leaked run vocabulary. Changes:
- **A drift dial** (refine / stretch / surprise). Run 1's why was worded at the level of the thing, so the run could only polish. In surprise, the why is restated as the need under the request.
- **A brief score** before spending agents. Below 7, fix the brief or ask.
- **A plain-English report** that ends every run in chat too.
- **A stability signal:** count the independent agents behind each part of the winner.
- **Judges with different stakes**, each with its own shuffle.
- **Nothing reaches the plan unattacked.**
- "Faster horse" became "the obvious answer".
- **Card tracking:** every draw is logged, and each card is credited with what it did. A card counts as a winner only for an element unique to it. Run 1's backfilled credits overstate the cards.

## 2026-10-23 04:13 UTC: Run 2, scrap wood (v0.1, surprise, cook)

Result: a flat day carousel plus a drying rack. It differs in kind from the obvious answer (a mudroom bench), which both cold answers gave almost word for word. 18 agents, about 1.2M tokens.

What worked:
- **The drift setting moved the result.** The winner was a different form serving a familiar need.
- **Judges with different stakes still agreed** on the same combination.
- **Re-attacking the combination found problems** (moisture, bearings, habit) the first attack missed.
- **The no-card control was a fair test.** It found the shared core alone. Four of twelve drawn cards produced something unique in the final. Six did nothing.

Lessons:
- The Gate 1 judge was not told about the drift setting and picked the frame the obvious answer lives in. Fixed.
- No judge noticed that a wall-hung wheel with open bins spills. The lead found it while writing the cut list. Being concrete is itself a test, so plans now get a fresh practitioner check.
- The pull of the obvious answer is strong. Even the wild card drifted toward the bench.
- Random wiki seeds helped once in four tries.
- Cards repeat across runs with a small deck.
- Cost rose with the controls and extra checks. Watch whether Stage 1 earns its cost.

## 2026-10-23 04:26 UTC: v0.2

The review: the winner was good, but the brief was too thin, so the answer fit a generic life and not the person's. Changes:
- **An intake before the brief:** up to five questions in one message, no follow-ups.
- **A distance judge** scores every raw idea 1 to 5 for distance from the obvious answer, cold answers included. Stats compare carded ideas, the control and cold answers across runs.

Run 3 reran the same wood brief with everything else fixed, so any gain would come from the intake.

## 2026-10-23 04:53 UTC: Run 3, a shed office (v0.2, surprise, cook)

Result: a Truchet-pattern wall, with a four-view blueprint, a parts list (about $146) and a plan. 19 agents, about 1.25M tokens.

What worked:
- **The intake.** Every agent aimed at the stated goal instead of a generic life. The brief scored 9 out of 10.
- **First distance numbers.** Card ideas averaged 4.25, the control 3, cold answers 1.5. One run, and confounded, but the first sign that cards widen the spread.
- **The re-attack found two killers** in the judges' unanimous pick.
- **The concrete plan and practitioner check** caught inlay, sanding and depth problems.

Lessons:
- **The framing leaked a solution.** It named one technique as an example, and four of five ideas used it. Framings state the problem and principle, never an example.
- **The decisive late fix came from the lead again.** Twice now. When an attack finds a fatal flaw, run a small round instead: two generators get the flaw and the whole, and a fresh judge picks. The lead stays out of design.
- Distance and feasibility trade off. The most distant idea died on material physics, as in run 2.
- Seeds were again the weakest input.
- Cost is creeping upward.

## 2026-10-23 05:20 UTC: v0.3, rescoped as an idea generator

The direction: go from "I want to do this but don't know what it looks like" to the best few ideas. Strategy and planning are a separate step. More ideas, the person at the decision points, and no compute spent on ideas the person would reject.
- **Output:** an idea dossier, with the winner and runners-up, each with its first cheap test and biggest risk. Plans and blueprints are out.
- **Fan-out:** four generators with three cards each, a no-card control and a wild card, about 16 sketches. Each agent's sketches must be different kinds of thing.
- **Problems:** two agents instead of four, with one framing paragraph.
- **A filter judge** replaces the distance judge. It groups duplicates and scores distance, feasibility and fit, feeding a menu of about 10.
- **Two human gates are the default:** the menu and the choice. Judges only in cook mode.
- **Develop only the picks,** then one adversary. The lead doesn't patch fatal flaws.
- Framings never name an example technique.

## 2026-10-23 05:47 UTC: Run 4, making a technical subject stick (v0.3, gated)

Result: a postmortem-reading habit with a first-party-sources-only rule, tested at once against four real postmortems. 16 agents, about 1.0M tokens.

What worked:
- **Breadth.** 16 sketches fell into 15 distinct ideas, with only three near-duplicate pairs.
- **The gates.** The person's picks steered development, and their answer about what they already used reframed every concept. Nothing was developed that they did not pick.
- **The adversary's cross-cutting finding** (the model is both source and judge of facts) became the winning requirement. Facts now come from fetched sources or running code, never model memory.

Lessons:
- **Cold answers were not cold.** Subagents inherit the project's files and memory, and one cold answer cited the person's private notes. Tell agents to ignore ambient context, or run them from a neutral directory.
- **The cards did not uniquely produce the winner.** The control reached the same group. Distance still favored the cards (3.25 vs. 2.67 this run; 3.6 vs. 2.8 across runs). This supported giving each agent many more cards and forcing it to diversify.
- **The deck was too small.** One card was drawn in three runs in a row.
- **A shell helper passed `--distance N` as one word,** so credits failed silently. Record credits from Python.
- Two human gates are slower in wall-clock time but cheaper and on target.

## 2026-10-23 v0.4 and deck v2

Deck v2 was built by 13 sealed authors and a sealed reviewer: 483 cards (423 moves, 60 constraints). About a third come from great thinkers. Of the moves with a known origin, 73% are non-US. Women are 36% of named people. Africa, South America and Oceania are thin next to Europe and Asia, and the new cards' facts were not checked against outside sources.

Run 5 below shaped v0.4:
1. **Gate 0, "Is this you?":** the person confirms the exact brief block before any agent runs. It holds their words verbatim, labeled assumptions with sources, and unknowns.
2. **No paraphrasing the intake.** Assumptions come only from this brief, never earlier runs or memory.
3. **The role question is always asked:** "what will you actually be doing during it?"
4. **A bonus stays a bonus,** and one generator ignores it.
5. **Every role prompt opens with:** "the brief is your only source of facts about the person."
6. **A bigger fan-out:** four generators with six sketches each, plus a six-sketch control and a wild card. About 31 sketches for the same agent count.
7. **The menu is about 8 items plus 2 wild slots** plus the obvious answer. One filter judge up to about 40 sketches, two above that.
8. **Gate 2 shows each concept's premises** and offers "go again clean".

## 2026-10-23 Run 5: a Halloween costume (v0.3 plus deck v2, gated)

Result: a giant costume prop, simplified by the person from a card-driven sketch.

The big lesson: **the lead polluted the brief three ways, and the agents faithfully built on the pollution.**
1. It filled an unanswered question from an earlier exercise ("full woodshop, $75"), so plywood showed up everywhere.
2. Its paraphrase added a false premise about who the costume would be dealing with, so every design solved a problem the person does not have.
3. Its framing promoted a bonus (a franchise theme) into a requirement, so every sketch came back on that theme.

The person caught all three at the gates. The fix is the brief-check gate, which shows exactly what agents will be told, with each fact's source. Nobody had asked about the person's role in the activity, so the intake needs a role question too.

Cards vs. the control were 3.4 vs. 3.3 this run, since the pollution flattened the spread. Across all runs it is 3.5 vs. 3.0, with cold answers at 1.3.

## 2026-10-23 Run 6: picking a book to pair with an essay (v0.4, gated)

- **Gate 0 worked.** It confirmed the brief with no corrections, and the lead added no pollution.
- **For the first time the two cold answers disagreed,** which marks a wide-open space.
- **31 sketches, with gravity wells.** A few canonical novels each appeared three or four times. The cards produced every outlier.
- **The filter caught 5 sketches with inaccurate plot details.** Generators invent specifics about real works.
- **The person asked for source fidelity,** so each pick was checked overnight against fetched summaries and criticism. Ratings ran from central to a stretch, with links. One pick's central theme turned out to be cursory in its source, so it was reshaped. This is now part of the developer role and Gate 2.

Parking lot from this run, for later versions:
- A grounded rating of how central each pick's thesis is to its source (central, significant, cursory or a stretch), so the person can speak with authority.
- Gate 1 as a conversation: the person's own angles shape development.
- Generators should mark how confident they are in each detail.

## Parking lot for v0.4 (from the person, 2026-10-23)

- Expand the deck broadly. v0.3 drew 16 moves per run from 48 cards, so repeats were heavy.
- Have each agent handle many cards and be forced to pick diverse options.
- Bring the judge back for a preliminary pass, and present only the winners.
- Carried over: better seed material than random wiki pages; a lite mode for quick decisions; a resume mode that re-enters a run from real-world feedback.

## 2026-10-23 22:00 UTC: v0.5 A/B/C test (wells, grounding, retrieval)

Each variant ran once on the book-pairing brief, in cook mode and isolated sessions, then everything was judged blind.
- **Retrieval (C) won.** It had the highest distance (3.60) and 3 of the 4 top-rated ideas, with no wrong claims. Outside data moves results. Instructions to agents mostly don't.
- **Wells come from generators' own candidate lists** and repeat across runs. A map built from cold samples missed them, and one well won variant A.
- **Per-claim memory tags and enforced tool use were inert:** 119 tags, 0 decisions. The menu grounding pass was cheap and useful.
- **Run 6 (v0.4) still had the best reader appeal (3.60).** The variants bought breadth, not quality, except C.
- **v0.5 plan:** the retrieved pool, a well map from candidate lists, a well ledger, 3 lenses with a pool, a final dossier fact-check, and the rule that sketches must be the kind of thing the brief asks for.

## 2026-10-23 23:57 UTC: v0.5 first real run, a Raspberry Pi and an old monitor (gated)

The person chose the Patchwork Booth and said at the menu, "oh these are starting to get good!!!" 19 agents, 1.43M tokens, 50 minutes.
- **The pool did the widening again** (control 4.0 vs. cards 4.1). Wells from unprompted lists worked: all 5 generators named the 4 obvious builds, and none won. Grounding and the fact-check each caught one wrong claim.
- **A backstory became a requirement.** A failed earlier project turned into "debuggable with a multimeter" in the framing. The person caught it.
- **One constraint swallowed a generator.** It was applied to all six sketches.
- **Wild slots went meaningless in surprise mode.**
- **The adversary's "fatal" really meant "fatal unless."**
- A fact that decided the winner (another person in the household) surfaced only at Gate 2, because the intake bundled two questions into one.
- **A problem agent took the person's name** from a home-folder path.

## v0.6

Built from the Pi run:
- **Context stays context.** Only the why, the no list and stated limits are requirements. Everything else is labeled background.
- **One thing per intake question,** with "who else" asked on its own.
- **A constraint shapes exactly 2 sketches,** not 6.
- **Drift-aware wild slots.** In surprise mode, the two best fits below the cut.
- **An adversary label, "fatal unless <premise>,"** shown to the person as a question at Gate 2.
- **The lead scrubs agent output** of names and details about the person that are not in the brief block.
- **Still to look into:** what spawned agents inherit from their environment, the source of the name leak.

## 2026-10-24 UTC: v0.6 first run, new guitar technology (gated)

The brief asked for an original piece of guitar technology that has never been done, then a design for it. 20 agents, about 1.4M tokens, 45 minutes.
- **"Fatal unless" worked.** Three questions at Gate 2 and two replies surfaced a requirement nobody had stated, ruled one pick out honestly, and settled the choice.
- **Labeling an example as background worked.** The person's own example idea was exactly the well: both cold answers and all five unprompted lists. It stayed off the main menu.
- **Labeling style as background didn't.** A musical style marked as background still pulled about 7 of 12 menu items toward one family of effects.
- **The novelty check was too shallow** for a brief whose core requirement was originality. Menu items got 1–2 searches each. The winner's closest prior art (an expired patent and some studio plugins built on the same principle) surfaced only later.
- **The intake bundled questions again,** although the skill said not to.
- **The lead wrote a full design plan in the run,** with no stage gating, attacking or fact-checking it.

## v0.7

Built from the guitar run:
- **A prior-art stage** for briefs that demand novelty. One agent per pick searches patents, products, plugins and studio techniques, papers, forums, and the same principle in other fields. It rates each pick known, known in principle but new in form, or no prior found, before development.
- **Idea-seeding roles get a requirements-only brief.** Background lines and background tensions are removed for the cold samplers, the retrieval agent, the generators, the control and the wild card.
- **An intake template:** one slot per question, one thing per slot.
- **An explicit handoff.** The run ends at the fact-checked dossier. Planning is a separate step that takes the dossier as its brief.

## 2026-10-24 UTC: v0.7 first run, an original pinball theme (gated)

The brief asked for a pinball theme no machine has used, with a novel toy and a list of shots, built as a home machine. The person named four reference machines for how they play, not their subjects. 36 agents, about 3.1M tokens, 94 minutes, because of two redos.
- **Requirements-only generators worked.** With the reference machines hidden from the idea-seeding roles, their genre didn't pull the menu. All 11 first-round items had a real loop with an ending.
- **The prior-art stage worked,** and rated both picks' toys "known in principle, new in form" while their themes were clear. But the field's main databases blocked automated fetches.
- **Three rounds swung.** Round 1 was esoteric: pool precedents became the subjects. Round 2 was graspable but domestic. Round 3 had hooks, but leaned to children's comedy. Each veto note became the loudest requirement, and nothing held the earlier ones.
- **The brief lacked three things audience-facing work needs:** legibility, a hook, and a register. The references carried all three implicitly. Hiding them stopped their subjects steering, but also hid their tone.
- **Requirement lines that quoted the person describing a reference carried its subject,** and two of the run's four wells came from those quotes.
- **11 ideas tied at the top of the filter,** so a shuffle chose the menu.

## v0.8

Built from the pinball run:
- **Intake for audience-facing work:** up to seven questions, always including who the others are, the hook, and the feel.
- **References are distilled** by a reference agent into subject-free play principles and register words, which become requirements. Names, subjects and quotes stay background.
- **A quote check:** a requirement line that names a reference's subject is split into the principle (a requirement) and the quote (background).
- **Two pools for subject briefs:** subjects the audience already knows that the medium hasn't used, and far-flung precedents for the mechanics.
- **Vetoes:** a light redo first, carrying forward what worked, and the filter scores fit against every requirement separately.
- **A pull score** (would the audience want it from the pitch alone?) breaks ties before any shuffle.
- **Prior art lists unreachable sources** and the hand searches to close the gap.

## v0.9

- **Light grilling at intake:** up to three rounds of questions, each with a recommended answer drawn only from the person's words or a labeled default. Taste questions are asked open.
- **A first visual mode:** agents drew each sketch as an SVG outline, rendered onto a contact sheet.

## 2026-10-24 UTC: v0.9 first run, a new guitar body shape (gated, paused at Gate 1)

The brief, grown by three grill rounds from one line to about 20 requirements, asked for an original electric guitar body and headstock inspired by a named guitar.
- **Grilling worked.** No gate surfaced a missing fact about the person. But qualitative limits ("durable", "realistic to build") stayed words instead of becoming checks.
- **Freehand drawing failed completely.** All 33 agent-drawn outlines passed the size checks, and the person rejected all 33 as boxy blobs. The checks measured size, not shape, and the filter judged the words, not the pictures.
- **A side project fixed the drawing.** An anatomy template (named points plus a type-designer's curve rule) reproduced real guitars within a few millimetres. Every agent design made with it read as a guitar, and the person kept seven as starting points.
- **What made it work:** start from one real exemplar and push, instead of averaging; checks calibrated on real objects; a picture judge used only to reject defects (it disagreed with the person on taste); locked picks, after agents quietly changed picked outlines and gamed a check; and per-agent folders, after agents sharing one ran each other's scripts.

## v0.10 (current)

Built from the guitar work:
- **Shape briefs use a proven template,** never freehand drawing (`references/shape.md`). With no template for the object, the run stays in words and offers building one as its own project.
- **References are seeds or taste.** A reference the person wants the result derived from is a seed: the idea agents get the real thing. A taste reference is distilled as in v0.8.
- **Limits become checks:** measured where possible, calibrated on real examples where qualitative, and judged by the person only when nothing can be measured.
- **Verify agents and lock picks.** Checks measure the artifact, the lead re-runs them, and developers deepen a pick without swapping its core.
- **One folder per agent.**
- **Model judges reject defects but don't choose for taste,** and cook-mode reports say the picks reflect a model's taste.

v0.10 hasn't had a full run yet.
