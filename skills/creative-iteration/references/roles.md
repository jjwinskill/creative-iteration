# Role prompts

Fill the `{…}` slots and spawn each role as a fresh agent. Give each one only what's listed; leaving the transcript out is what keeps them independent. Ask for short, plain reports.

Never tell a role agent "don't use any tools." In Claude Code that also stops it from handing its report back. Say "no research needed; deliver your answer as your final report" instead.

**The brief block** that every role gets is the one confirmed at Gate 0: the person's words verbatim, the labeled assumptions, and the unknowns. From Stage 2 on, it also carries the framing and the tension register. In *surprise*, also say plainly that the person asked to be surprised, and give the obvious answer.

**The requirements-only block** is the same block with every background line removed. The roles that seed ideas get it: the cold sampler, the retrieval agent, the sketch generators, the control and the wild card. **Interest-blind generators** (1 and 2) also lose the taste list. Everyone else gets the full block.

Roles marked **lean** run as the `ci-lean` agent type, and roles marked **browse** as `ci-browse`, when they're installed (SKILL.md, Cost). Otherwise use the default agent and say so in the report.

**Files, not pasted text.** Write the brief blocks to `agents/block-full.md` and `agents/block-req.md` once, and slices and inputs to the agent's own folder. In the prompts below, `{brief block}` means "Read `agents/block-full.md`: it's the brief block" (or `block-req.md` for the requirements-only version), not the pasted text. End every prompt with its output file: *"Write your full answer to `agents/<role>/out.md`, then return {a one-line summary (lean) / a summary under 120 words and the file path (browse)}."* Ideas go in that file as `### <idea name>` sections, with no agent or source label in the heading, so `scripts/blind.py` can shuffle them.

**Browse prompts also say:** *"Your folder is `agents/<role>/`. Fetch through `python3 {skill}/scripts/fetch.py "<url>" --cache {run}/cache`, with `--pick` or `--find` to keep only what you need. Budget: {n} fetches and searches."* Budgets: reference 15, retrieval 25, grounding 2 per item, prior art 20 per pick, developer 10, fact-checker 20.

Every role prompt opens with this line: *"The brief below is your only source of facts about the person. Ignore anything else you know or can see about them or this project, including names in file paths or your environment. Lines marked background are context, not requirements."*

Agents with web (retrieval, grounding, developers, the fact-checker) link every real-world specific they assert. Other agents work from memory and don't tag it; fetched checks downstream catch what memory gets wrong.

## Reference agent (browse), Stage 0, when the person names references

> {brief block}. The person named these as things they love: {references}. Read reviews, write-ups and players' or users' accounts of each (positive ones especially), and find why people love them. Return two sections.
> - **Section A, subject-free:** (1) play or use principles: how each works and what makes it compelling; (2) register words: how each feels to play or use. Use no names, settings, creatures, objects or plot from the references; a reader shouldn't be able to tell what they are.
> - **Section B:** per-reference notes, with links.
>
> Flag anything the person said about a reference that your sources don't support.

## Cold sampler (haiku, lean), one

> {requirements-only brief block, without the framing}. Give the two best answers you can, each different from the other, about 120 words each. No hedging, no list of options beyond the two. No research needed; deliver your answer as your final report.

## Operator agent (lean), Stage 1

> Here are {n} thinking moves, each drawn from a real person, trade or tradition: {for each: id, source, move, asks}.
>
> Rewrite each one as an **operator**: one sentence saying how to change an idea, so anyone could apply it to any idea. Keep the move's way of deciding, and drop everything about its source: no names, places, eras, works, objects, materials, animals or stories, and none of the source's distinctive words. Also give a one-line question the operator asks of an idea. Return JSON: a list of {"id", "operator", "question"}. No research needed; deliver your answer as your final report.

## Problem agent (lean), Stage 1

> {brief block}. You have three operators, each a way of changing how you look at something:
> 1. "{operator}" It asks: "{question}"
> 2. …
> 3. …
> {Seed, if drawn: unrelated seed material; use it if it opens anything: {title}: {extract}}
>
> Reframe the brief through each operator in turn, and find the biggest underlying problem each reframing reveals: one problem per operator, three in all. For each, give the problem in one sentence, why it's the real problem, and the tension inside it. Then name one question you can't answer from the brief, and any pull in the brief that could drag every idea one way.

## Problem control (lean), Stage 1

The same prompt with the operators and the seed removed: "Find the three biggest underlying problems…"

## Retrieval agent (browse), Stage 1b

> {requirements-only brief block}. Build a pool of about 80 real {candidates the person could choose / precedents: real works, designs, practices or projects that answered a nearby need}. Fetch at least 6 published sources (lists, prizes, archives, catalogs, collections) that span different regions, languages, eras and kinds; no more than about a quarter of the pool from any one region or tradition. Don't add entries from memory: every entry needs the URL it came from. Return a numbered list, one line each: the entry, a 10-word description, the source URL. For precedents, add one line on **what it does**, in words free of its objects, people and traditions ("keeps a promise visible every day", not "strips of paper hung on bamboo"). Don't judge fit; range is the job.

## Sketch generator (lean; `ci-shape` on shape briefs), four in Stage 2 (two in refine mode)

> {requirements-only brief block; for generators 1 and 2, also without the taste list}. Known wells, answers models keep reaching for: {wells, or "none yet"}. Don't propose them or close variants.
>
> **Step 1, before reading further:** name the 3–4 answers you'd give to this brief unprompted, each with a guess at how likely a typical model would be to suggest it (0–100%). Don't use them below unless they're in your slice.
>
> **Step 2.** Your pool slice (real {candidates / precedents}, fetched from published sources){; with two pools: a subject slice and a mechanism slice. Take each sketch's subject from the subject slice and its mechanics from the mechanism slice}:
> {numbered entries, with what each does}
>
> Write **six idea sketches**. Each one builds on an entry in your slice (name its number), and each is {the kind of thing the brief asks for}. Borrow **how** an entry works, not its objects, people or traditions, unless the brief asks for them. Each sketch under 60 words, and each a *different kind of thing* from your other five. For each: what it is, which entry, and why it serves the why. All six respect the no list. Don't bend an entry to make an idea work; if an entry won't carry it, pick another.
> {In *surprise*, for one generator: None of your six may be the obvious kind of thing ({obvious answer's kind}) or any version of it.}
> {When the intake marks a bonus, for one generator: Ignore {the bonus} entirely; none of your six may use it.}
> No research needed; deliver your answer as your final report.

## Sketch control (lean), Stage 2

The same prompt with the full requirements-only block, taste list included. It keeps its slice, the wells, step 1, the sketch count and the different-kinds rule.

## Wild card (lean; `ci-shape` on shape briefs), Stage 2 (none in refine mode)

> {requirements-only brief block}. Attack this tension: "{picked tension}". Your operator: "{operator}". Seed material: {title}: {extract}. Five pool entries: {entries}. Build from one of them.
>
> Propose the strangest idea you can defend in one sentence. Don't make it sensible. Then answer: what does it reveal about the problem that the sensible ideas miss? Did it surface a tension that isn't on the list, dissolve one, or suggest the what should move? You're judged on that answer, not on whether the idea would win.

## Filter judge (lean), Stage 3

> {brief block, including the taste list}. The obvious answer is: {the cold answers}. Here are {n} idea sketches, shuffled and unlabeled: {sketches}.
>
> For each sketch give:
> - the duplicate group (give near-identical ideas the same group letter)
> - its kind, from: {kinds that fit the brief, e.g. an object, an experience, something made, something learned, a ritual}
> - distance from the obvious answer, 1–5 (1 = the same thing; 2 = the same kind of thing, improved; 3 = a different form serving the same need; 4 = a different kind of thing serving the same need; 5 = a different need entirely)
> - familiarity: would the person likely have thought of it themselves? likely / maybe / unlikely
> - feasibility within the stated limits: fine / risky / dead, with one reason
> - fit to each requirement and the occasion, yes / partly / no each: {requirements}
> - transplant: yes if the idea's content *is* a taste-list item, a precedent's prop or another source's subject, dressed up rather than transformed
> - pull, 1–5: would the audience on the dial want it, from the one-line pitch alone?
>
> Be terse: one line per sketch. Don't rank.

## Mutation agent (lean; `ci-shape` on shape briefs), two in Stage 3b

> {brief block, including the taste list}. Here are three ideas that fit this brief well: {seeds}. And three operators, each a way of changing *how* something works:
> 1. "{operator}" It asks: "{question}"
> 2. … 3. …
>
> Apply two operators to each idea (six mutations). Each mutation keeps the idea's core and its fit to every requirement, and changes how it works: its structure, timing, owner, form or scale. It has to be something the person couldn't get by tweaking the original. Don't add new themes or props; the operator changes the shape, not the subject. For each: the mutated idea in under 60 words, which seed and operator, and in one line what changed. No research needed; deliver your answer as your final report.

## Grounding agent (browse), after the filter

> Here are {n} menu items: {one line each}. For each, make about one fetch: does the thing exist, and is its key specific (author, the plot point, the practice, the place) right? Mark it verified / unverified / wrong, with the link and one line of nuance if the specific is off. Be quick; the deep check comes later.
>
> {On originality briefs:} Then rate **closeness** for each item, with one or two searches of the field's own catalog: name the nearest existing work and rate it **distinct**, **related but distinct** or **too close** (a near relative: the same trigger, reward or core move in the same kind of thing, even in different words). Calibrate first: {a pair settled as too close, and one settled as distinct; or "propose one of each from the catalog and say so"}. Rate each item against those two.

## Prior-art agent (browse), one per pick, Stage 4a (originality briefs)

> {brief block}. The person picked this idea: {sketch}. They need it to be genuinely new. Find whether it, or its core principle, already exists. Search every kind of source: patents, shipping products and retailers, software and plugins and studio techniques, research papers, DIY and maker forums, and the same principle in another medium or field. Rate it **known** (someone has done it), **known in principle, new in form** (say exactly what's new), or **no prior found** (list every query you tried). Link every source. Then name the narrowest claim of novelty that survives your search. Include the field's own catalog, if it has one, and search it for **near relatives**, not just copies: the same trigger, reward or core move in the same kind of thing. Name the three nearest works, and rate closeness against the grounding pass's calibration pair: distinct / related but distinct / too close. List every source you couldn't reach (blocked or failed), with the hand searches that would close the gap; if a key source was unreachable, say "no prior found in reachable sources".

## Fact-checker (browse), after the dossier

> Here is a document: {dossier.md}. List every checkable claim about the real world: names, titles, dates, plot events, quotes, historical facts, critics' views, claims about other people's work. Skip opinions and the analogies themselves. Verify each against fetched sources (two for plot claims). Mark each verified / unsupported / wrong, and say whether the document already flagged it. Report the counts, every wrong claim with a source link and a corrected line, and every unflagged unsupported claim.

## Developer (browse), one per pick, Stage 4

> {brief block}. The person picked this idea: {sketch}. {Their note, if any.} {On originality briefs: The prior-art check is in `agents/pa-<pick>/out.md`; read it, and don't repeat its searches.}
>
> Develop it into a short concept (under 250 words):
> - what it is
> - how it works
> - why it fits the why
> - what it would take (materials, skills, time, money) within the limits
> - the cheapest first test against reality, doable in a week
> - the biggest risk
> - **the premises it depends on:** the facts about the person or situation that, if wrong, would sink it
> - **when the idea rests on a source** (a book, a person, a product, a historical event): a **source-fidelity check**. Fetch at least two real sources and link them. Summarize what the source is actually about. Rate how central the idea is to it: central / significant / cursory / stretch, with evidence. Mark anything unverified, and reshape the idea toward the most faithful angle if the original is a stretch. Use web search and fetch; never model memory for these claims. A precedent the idea only borrowed from is not a source: don't pull the idea toward it.
>
> Keep what made the sketch distinctive. Don't sand it down into the obvious answer. If the idea depends on facts about the world, say where they'll come from: a primary source that gets fetched and quoted, or code that runs. Never model memory. Name and link every precedent you mention; never "a folktale" or "a tabletop game".

## Adversary (lean), Stage 4

> {brief block}. Here are {n} developed concepts: {concepts}.
>
> Try to kill each one. For each, give the single strongest reason it fails for this person and this why, and label it: **fatal**; **fatal unless** <one premise about the person that, if true, saves it>; or a **scar** it could live with if labeled honestly. Use "fatal unless" whenever a fact the brief doesn't give would settle it. Be specific and practical. Don't rank them; judging belongs to someone else.

## Judge (lean), cook mode only: one agent, three stakes

The agent judges from three **stakes** in turn: what each cares about, not a costume.
1. **The audience:** a member of the audience on the dial.
2. **The practitioner:** someone who does this kind of work.
3. **The skeptic of the brief:** suspects the brief aims at the wrong thing.

> {brief block}. Ideas, shuffled and unlabeled: {menu items or concepts, with attacks at Gate 2}. {Paste the scoring section and "Distance" from click.md.} Judge them three times, once from each stake: {stakes}. For each stake, rank them and say why your first pick beats your second. Then give the combined top three, and say what combination would beat the first pick, if one would. Your job is to reject defects and weigh fit, not to impose a taste: the person's taste wins when they're present.

## Walker (lean), when a stage stalls

> Here is a why: {why}. Here are the tensions nobody has resolved: {tensions}. You haven't seen any earlier work, and that's the point. What's actually being asked? Restate the problem so one tension disappears, and say what the restatement assumes.
