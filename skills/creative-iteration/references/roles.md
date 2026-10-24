# Role prompts

Fill the `{…}` slots and spawn each role as a fresh agent. Give each one only what's listed; leaving the transcript out is what keeps them independent. Ask for short, plain reports.

Never tell a role agent "don't use any tools." In Claude Code that also stops it from handing its report back. Say "no research needed; deliver your answer as your final report" instead.

**The brief block** that every role gets is the one confirmed at Gate 0: the person's words verbatim, the labeled assumptions, and the unknowns. From Stage 2 on, it also carries the framing and the tension register. In *surprise*, also say plainly that the person asked to be surprised, and give the obvious answer.

Every role prompt opens with this line: *"The brief below is your only source of facts about the person. Ignore anything else you know or can see about them or this project, including names in file paths or your environment. Lines marked background are context, not requirements."*

Agents with web (retrieval, grounding, developers, the fact-checker) link every real-world specific they assert. Other agents work from memory and don't tag it; fetched checks downstream catch what memory gets wrong.

## Cold sampler (haiku), two

> {brief block, without the framing}. Give your single best answer to it, in about 150 words. No hedging, no list of options. No research needed; deliver your answer as your final report.

## Problem agent (sonnet), Stage 1

> {brief block}. You have three lenses, each a decision move from a real person or trade:
> 1. {source}: "{move}" It asks: "{asks}"
> 2. …
> 3. …
> {Seed, if drawn: unrelated seed material; use it if it opens anything: {title}: {extract}}
>
> Using each lens as a *way of deciding*, not a costume, find the biggest underlying problem in this brief: one problem per lens, three in all. For each, give the problem in one sentence, why it's the real problem, and the tension inside it. Then name one question you can't answer from the brief.

## Problem control (sonnet), Stage 1

The same prompt with the lenses and the seed removed: "Find the three biggest underlying problems…"

## Retrieval agent (sonnet, with web), Stage 1b

> {brief block}. Build a pool of about 80 real {candidates the person could choose / precedents: real works, designs, practices or projects that answered a nearby need}. Fetch at least 6 published sources (lists, prizes, archives, catalogs, collections) that span different regions, languages, eras and kinds; no more than about a quarter of the pool from any one region or tradition. Don't add entries from memory: every entry needs the URL it came from. Return a numbered list, one line each: the entry, a 10-word description, the source URL. Don't judge fit; range is the job.

## Sketch generator (sonnet), four in Stage 2

> {brief block}. Known wells, answers models keep reaching for: {wells, or "none yet"}. Don't propose them or close variants.
>
> **Step 1, before reading further:** name the 3–4 answers you'd give to this brief unprompted, each with a guess at how likely a typical model would be to suggest it (0–100%). Don't use them below unless they're in your slice.
>
> **Step 2.** Your pool slice (real {candidates / precedents}, fetched from published sources):
> {numbered entries with their one-line descriptions}
>
> You have three lenses and one hard constraint:
> 1. {source}: "{move}" It asks: "{asks}"
> 2. … 3. …
> Constraint: "{constraint}"
>
> Write **six idea sketches**. Each one is built from an entry in your slice (name its number), and each is {the kind of thing the brief asks for}. Use every lens to shape at least one sketch, even when it seems a poor fit; the strange fits are the point. Each sketch under 60 words, and each a *different kind of thing* from your other five. For each: what it is, which entry, why it serves the why, and in one line, how the lens shaped it. Exactly two of the six are shaped by the constraint; the other four ignore it. All six respect the no list. Don't bend an entry to make an idea work; if an entry won't carry it, pick another.
> {In *surprise*, for one generator: None of your six may be the obvious kind of thing ({obvious answer's kind}) or any version of it.}
> {When the intake marks a bonus, for one generator: Ignore {the bonus} entirely; none of your six may use it.}
> No research needed; deliver your answer as your final report.

## Sketch control (sonnet), Stage 2

The same prompt with the lenses and the constraint removed. It keeps its slice, the wells, step 1, the sketch count and the different-kinds rule, so the only difference is the cards.

## Wild card (sonnet), Stage 2

> {brief block}. Attack this tension: "{picked tension}". Your lens: {source}: "{move}". Seed material: {title}: {extract}. Five pool entries: {entries}. Build from one of them.
>
> Propose the strangest idea you can defend in one sentence. Don't make it sensible. Then answer: what does it reveal about the problem that the sensible ideas miss? Did it surface a tension that isn't on the list, dissolve one, or suggest the what should move? You're judged on that answer, not on whether the idea would win.

## Filter judge (sonnet), Stage 3

> {brief block}. The obvious answer is: {a cold answer}. Here are {n} idea sketches, shuffled and unlabeled: {every sketch, the wild card's, and both cold answers}.
>
> For each sketch give:
> - the duplicate group (give near-identical ideas the same group letter)
> - distance from the obvious answer, 1–5 (1 = the same thing; 2 = the same kind of thing, improved; 3 = a different form serving the same need; 4 = a different kind of thing serving the same need; 5 = a different need entirely)
> - feasibility within the stated limits: fine / risky / dead, with one reason
> - fit to the why: yes / partly / no
> - forced fit: yes if the sketch bends its source (a book, a precedent) to make the idea work, else no
>
> Be terse: one line per sketch. Don't rank.

## Grounding agent (sonnet, with web), after the filter

> Here are {n} menu items: {one line each}. For each, make about one fetch: does the thing exist, and is its key specific (author, the plot point, the practice, the place) right? Mark it verified / unverified / wrong, with the link and one line of nuance if the specific is off. Be quick; the deep check comes later.

## Fact-checker (sonnet, with web), after the dossier

> Here is a document: {dossier.md}. List every checkable claim about the real world: names, titles, dates, plot events, quotes, historical facts, critics' views, claims about other people's work. Skip opinions and the analogies themselves. Verify each against fetched sources (two for plot claims). Mark each verified / unsupported / wrong, and say whether the document already flagged it. Report the counts, every wrong claim with a source link and a corrected line, and every unflagged unsupported claim.

## Developer (sonnet), one per pick, Stage 4

> {brief block}. The person picked this idea: {sketch}. {Their note, if any.}
>
> Develop it into a short concept (under 250 words):
> - what it is
> - how it works
> - why it fits the why
> - what it would take (materials, skills, time, money) within the limits
> - the cheapest first test against reality, doable in a week
> - the biggest risk
> - **the premises it depends on:** the facts about the person or situation that, if wrong, would sink it
> - **when the idea rests on a source** (a book, a person, a product, a historical event): a **source-fidelity check**. Fetch at least two real sources and link them. Summarize what the source is actually about. Rate how central the idea is to it: central / significant / cursory / stretch, with evidence. Mark anything unverified, and reshape the idea toward the most faithful angle if the original is a stretch. Use web search and fetch; never model memory for these claims.
>
> Keep what made the sketch distinctive. Don't sand it down into the obvious answer. If the idea depends on facts about the world, say where they'll come from: a primary source that gets fetched and quoted, or code that runs. Never model memory.

## Adversary (sonnet), Stage 4

> {brief block}. Here are {n} developed concepts: {concepts}.
>
> Try to kill each one. For each, give the single strongest reason it fails for this person and this why, and label it: **fatal**; **fatal unless** <one premise about the person that, if true, saves it>; or a **scar** it could live with if labeled honestly. Use "fatal unless" whenever a fact the brief doesn't give would settle it. Be specific and practical. Don't rank them; judging belongs to someone else.

## Judges (sonnet or better), cook mode only, three in parallel

Each gets a different **stake**: what they care about, not a costume.
1. **The audience:** a member of the audience on the dial.
2. **The practitioner:** someone who does this kind of work.
3. **The skeptic of the brief:** suspects the brief aims at the wrong thing.

Shuffle the order separately for each judge.

> {brief block}. Your stake: {stake}. Ideas, shuffled and unlabeled: {menu items or concepts, with attacks at Gate 2}. {Paste the scoring section and "Distance" from click.md.} Rank them, and say what combination would beat your first pick, if one would.

## Walker (sonnet), when a stage stalls

> Here is a why: {why}. Here are the tensions nobody has resolved: {tensions}. You haven't seen any earlier work, and that's the point. What's actually being asked? Restate the problem so one tension disappears, and say what the restatement assumes.
