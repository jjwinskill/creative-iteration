# Creative Iteration

Creative Iteration is a [Claude Code](https://claude.com/claude-code) skill that turns a vague want ("I've got a pile of scrap wood, what should I make?") into a few strong, checked ideas. It runs a pipeline of fresh agents. They fetch real precedents, write about 30 sketches, reshape the strongest through randomly drawn thinking moves, and score them blind. The person picks from a short menu, and the picks are developed, attacked and fact-checked into an idea dossier. It's the first tool in a planned suite; strategy and planning tools are meant to follow.

> **Status: experimental (v0.13).** This is a working research project, not a finished product. It has had seventeen runs on thirteen briefs, including two comparisons against plain Claude, and every run changed the method. v0.13 itself hasn't had a full run yet. Expect rough edges, high token use, and rules that will keep changing.

## At a glance
- **What it is:** one orchestrating session, 18 agent role prompts, three custom agent types and eight Python scripts.
- **The idea:** variation comes from outside the model (fetched sources and the operating system's randomness). Fresh agents and the person do the choosing.
- **The evidence:** seventeen recorded runs. Most of the skill's rules name the run that caused them ([LESSONS.md](docs/creative-iteration/LESSONS.md)).
- **The cost:** measured in dollars from Claude Code's own transcripts. The v0.12 run cost $22.83, 28% less than the v0.11 run's $31.80. Plain Claude costs about $2.50 a brief.
- **An honest result:** in a blind test on a gift brief, plain Claude's ideas ranked best, on about a seventeenth of the tokens. The next version was rebuilt around what that test showed.

## Why it exists
Ask a language model for ideas and you get the obvious answer. Ask it for "ten wild ideas" and you get the same ten every time. The research agrees:
- Preference-tuned models collapse toward typical answers (Zhang et al., *Verbalized Sampling*, 2025).
- Different models give strikingly similar "creative" answers (Wenger & Kenett, *We're Different, We're the Same*, 2025).
- People who brainstorm with a model converge on each other's ideas (Anderson, Shah & Kreminski, 2024).

So this skill treats the model as cheap, dumb mutation and spends its judgment on **selection**. The person steers at two short menus, because people are bad at specifying what they want and good at reacting to what's in front of them.

## How a run goes

```
a vague want
  -> Intake      up to 3 rounds of questions; every limit becomes a check
  -> Gate 0      the person confirms the brief: "Is this you?"
  -> Cold answer a cheap agent gives the obvious answer, the yardstick for distance
  -> Operators   10 drawn moves rewritten as subject-free lenses, leak-checked
  -> Problems    2 agents look for the real problem under the request
  -> Pool        1 agent fetches ~80 real precedents from 6+ sources
  -> Fan-out     4 generators, a control and a wild card write ~30 sketches
  -> Filter      a blind judge scores every sketch and the obvious answer
  -> Mutation    the 6 strongest ideas x 2 operators each = 12 mutations
  -> Menu        ~10 items in 3 bands, each checked against a real source
  -> Gate 1      the person picks 2 or 3
  -> Develop     prior art (novelty briefs), 1 developer per pick, 1 adversary
  -> Gate 2      the person chooses
  -> Dossier     the winner and runners-up, fact-checked
```

- **Intake** asks numbered questions, most with a recommended answer you can accept with "yes" (adapted from Matt Pocock's grilling skill). References the person names are distilled into subject-free principles, so their subjects don't steer the ideas.
- **The menu** has three bands: familiar and strong (always including the obvious answer), a twist on the familiar, and out there. A veto triggers a light redo that still meets every earlier requirement.
- **The run stops at the dossier.** Planning is a separate step, and the dossier is its brief.
- **Other modes:** in *cook mode*, a judge with three different stakes makes the gate decisions. *Refine mode* keeps the person's own design, runs fewer generators and spends more on checks. *Shape briefs* (a guitar body, a chair back) use a shape template ([`references/shape.md`](skills/creative-iteration/references/shape.md)).

## What's technically interesting
- **Agent orchestration.** The lead session orchestrates and never judges its own ideas. Each role is a fresh agent that gets only the inputs [`references/roles.md`](skills/creative-iteration/references/roles.md) lists for it, so agents stay independent. Recorded runs spawned 14 to 36 subagents, mostly on Sonnet.
- **Three purpose-built agent types.** `ci-lean` carries only Read and Write, and starts at about 3.7k tokens of context instead of the default agent's 54k. `ci-browse` carries five tools, a call budget and a shared fetch cache, and starts at about 6k. `ci-shape` adds Bash and a render budget for shape templates.
- **Randomness the model can't steer.** Scripts draw the cards, deal pool slices, shuffle judge inputs and break menu ties with the operating system's random source (`secrets.SystemRandom`). The orchestrator never reads the deck of 423 moves, because reading it would prime the model.
- **Mutation through thinking moves, with a leak check.** Each drawn move is rewritten as a one-sentence operator with no names, places or story, and `leakcheck.py` flags any distinctive word it still shares with its source. Operators then reshape the six strongest ideas, including a well and the obvious answer, into twelve mutations that keep their fit.
- **A blind filter and a scripted menu.** A fresh judge scores every sketch, shuffled and unlabeled, for distance from the obvious answer (1–5), familiarity, feasibility, fit to each requirement, pull, duplicates and transplants (an idea that just dresses up its input). `menu.py` builds the menu from those scores, so the lead doesn't hand-pick. Answers every model reaches for ("wells") are flagged, not deleted.
- **Checks against reality, not memory.** A grounding agent checks that every menu item exists. On novelty briefs, a prior-art agent per pick searches patents, products, papers and forums, and lists the sources it couldn't reach. A fact-checker marks every real-world claim in the dossier verified, unsupported or wrong.
- **Rules against agents gaming the run.** [`SKILL.md`](skills/creative-iteration/SKILL.md) has ten separation rules, most tied to a failure seen in a run. Checks measure the artifact, never an agent's own numbers: one agent passed a width check by moving the points it measured from. Picks are locked so developers can't swap their core, and each agent works in its own folder.
- **Cost measured in dollars, and cut.** `cost.py` prices the lead and every subagent from Claude Code's transcripts, with cache reads, cache writes and output priced separately. The v0.11 run's $31.80 was 42% the lead, 52% browsing agents and about 1% the card stages. v0.12 added `ci-browse`, a shared fetch cache, call budgets and a thinner lead, and its run cost $22.83 on a different brief. The lead was still 43% of that, over 137 calls, so v0.13 scripts the menu and aims for under about 70. See [COST.md](docs/creative-iteration/COST.md).
- **Shape templates instead of freehand drawing.** Agents writing raw SVG produced 33 outlines that passed every size check, and the person rejected all 33 as "boxy blobs." A template of named anatomy points and a type designer's curve rule reproduced real guitars within a few millimetres. All 30 designs made with it read as guitars, and the person kept seven.
- **A blind test mode.** `packet.py` turns runs on the same brief into a shuffled, relabeled rating packet, with the key kept separate.

## What the tests have shown so far
- **Outside material beats instructions.** What widened the ideas was fetched data (the pool, the fact-checks). Telling agents to behave differently (tag your claims, avoid the typical) changed little: in one test, 119 claim tags changed no decisions.
- **The pool is the engine; cards as content were not.** With a fetched pool, the no-card control landed as far from the obvious answer as the carded agents in every run. In the blind gift test, the carded arm ranked last, so since v0.11 cards are only lenses on ideas that already fit.
- **Agents literalize inputs.** A taste list became tropes, a card's story became a prop, a reference's subject became a theme.
- **Wells are real and predictable.** In the Raspberry Pi run, all five idea agents named the same four builds (an arcade, a smart mirror, a photo frame, a media center) before seeing their pools. None of them won.
- **Fact-checking catches what memory gets wrong.** In tests, it found a confident wrong claim in two of five final documents, and unflagged guesses in every one.

## How it was built
It grew one version at a time, each built from the run before. Each run ends with a post-mortem, and the next version's rules cite what went wrong. v0.1 to v0.5 predate this repo; from v0.7 on, each version's commit message names the run behind it.

| Version | What changed |
|---|---|
| v0.1–v0.3 | A drift dial, a brief score, an intake, then a rescope to idea generation with two human gates and a dossier |
| v0.4 | Gate 0 ("Is this you?"), the person's words passed verbatim, a 483-card deck from 13 sealed authors |
| v0.5 | A fetched pool, a well map, a dossier fact-check (the pool won a three-way test) |
| v0.6–v0.7 | Background kept out of requirements, "fatal unless" attacks, a prior-art stage, a handoff to planning |
| v0.8 | The hook and feel at intake, distilled references, balanced redos, a pull score |
| v0.9–v0.10 | Grilling at intake, limits turned into checks, shape templates, locked picks, one folder per agent |
| v0.11 | Cards become leak-checked operators used only in mutation, a three-band menu, lean agents |
| v0.12 | Cost measured in dollars (its run cost 28% less), `ci-browse`, a shared fetch cache, a thinner lead |
| v0.13 | Refine mode, the obvious answer always on the menu, `ci-shape`, a scripted menu, a blind test mode |

## Why diverse voices matter here
This method only works if the outside perspective is actually outside. A deck drawn from the same few Western, mostly male thinkers would push every run toward the same corner. So the deck pairs thinkers with crafts, trades, folk practice, ecology, play and infrastructure; most moves of known origin are from outside the US; and its US voices lean toward communities of color and working-class traditions. In the strongest test variant, 6 of 10 menu items came from outside the Anglo-European canon. In the Raspberry Pi run, 10 of 12 came from precedents outside the US and UK.

A one-line "move" can flatten a living tradition. The deck's attributions are paraphrased inspirations, not quotations or endorsements, and have been reviewed for accuracy and respect, but not independently verified one by one. If a card misrepresents a person or a tradition, please open an issue.

## Examples
- "I've got a pile of scrap wood, what should I make?" In an early scrap-wood run, both cold answers gave a mudroom bench almost word for word. The pick was a flat day carousel with a drying rack: a different form serving the same need.
- "Show me a new way to build an electric guitar."
- "I need an idea for a side project."

**A complete run** is in [`docs/creative-iteration/examples/pi-monitor/`](docs/creative-iteration/examples/pi-monitor/), with every round, the dossier and a post-mortem. The brief: a Raspberry Pi 4, an old monitor with a dead stand, a cheap USB mic and $100. The obvious answer was a RetroPie couch arcade. One agent fetched 86 precedents, six agents wrote 31 sketches, and the person chose the **Patchwork Booth**: press one button, tell a one-minute story, and it becomes a stitched patch on a quilt that grows on the screen. It took 50 minutes and cost $11.96.

## The road to 1.0
- **Run v0.13 on more briefs,** especially gift choices, trips, team rituals and fundraisers, and test refine mode.
- **Verify the deck** card by card, and fill its thin regions (Africa, South America and Oceania).
- **Gate 1 as a conversation,** so the person's own angles shape development, not just their picks.
- **Cheaper runs.** Runs have cost $9–32 at list prices. A lite mode for quick decisions is planned.
- **Cross-model runs,** to test whether mixing models widens the ideas, given that models share wells.
- **A resume mode** that re-enters a run with real-world feedback ("we built it; here's what happened").
- **Better agent isolation.** Agents still pick up details about the person from their environment, such as names in file paths.
- **The rest of the suite:** strategy and planning skills that take an idea dossier forward.

## Install
Requires [Claude Code](https://claude.com/claude-code) and Python 3.

```bash
git clone https://github.com/jjwinskill/creative-iteration.git
```

```bash
ln -s "$PWD/creative-iteration/skills/creative-iteration" ~/.claude/skills/creative-iteration
```

Recommended: install the skill's three agent types, which cut most agents' starting context from about 54k tokens to about 4k–6k. One is for roles that need no web, one for roles that browse, and one for shape-template roles. Start a new Claude Code session afterward so they're picked up.

```bash
mkdir -p ~/.claude/agents && for a in ci-lean ci-browse ci-shape; do ln -s "$PWD/creative-iteration/skills/creative-iteration/agents/$a.md" ~/.claude/agents/$a.md; done
```

Then ask Claude Code something like "I've got a pile of scrap wood, what should I make?" and the skill picks it up. Runs are written to `runs/` in your working folder.

**One rule for running it:** the session orchestrating a run must never read `deck/deck.json`. It only draws cards through `scripts/draw.py`. Reading the deck primes the model, and the draw stops being outside randomness. Reading the deck yourself is fine.

## Layout
| Path | What it is |
|---|---|
| `skills/creative-iteration/SKILL.md` | The method |
| `skills/creative-iteration/references/` | Agent prompts (`roles.md`), the judging rubric (`click.md`), shape briefs (`shape.md`) and file templates (`templates.md`) |
| `skills/creative-iteration/scripts/` | `draw.py` (cards), `deal.py` (pool slices), `leakcheck.py`, `blind.py` (judge inputs), `fetch.py` (shared cache), `cost.py`, `menu.py` and `packet.py` |
| `skills/creative-iteration/agents/` | The `ci-lean`, `ci-browse` and `ci-shape` agent types |
| `skills/creative-iteration/deck/deck.json` | The deck of thinking moves (its constraint cards are no longer drawn) |
| `skills/creative-iteration/data/` | Your local draw log and well ledger. Created on first use, never committed |
| `docs/creative-iteration/` | Lessons from every run (`LESSONS.md`), the cost analysis (`COST.md`) and an example run |

## License
MIT. See [LICENSE](LICENSE).
