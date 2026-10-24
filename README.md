# Creative Iteration

A suite of agent-led tools for the hard first step of making something: getting from "I want to do this, but I don't know what it looks like" to an idea worth building. The first tool is the **Creative Iteration** skill for Claude Code, an idea generator. Strategy and planning tools are planned to follow it.

> **Status: experimental (v0.7).** This is a working research project, not a finished product. It has had eleven runs on eight briefs, and every run changed the method. Expect rough edges, high token use, and rules that will keep changing.

## Why it exists

Ask a language model for ideas and you get the obvious answer. Ask it for "ten wild ideas" and you get the same ten every time. The research agrees:
- Preference-tuned models collapse toward typical answers (Zhang et al., *Verbalized Sampling*, 2025).
- Different models give strikingly similar "creative" answers (Wenger & Kenett, *We're Different, We're the Same*, 2025).
- People who brainstorm with a model converge on each other's ideas (Anderson, Shah & Kreminski, 2024).

So this skill treats the model as cheap, dumb mutation and spends its judgment on **selection**. The variation comes from **outside the model**:
- a pool of real candidates or precedents fetched from published sources
- thinking moves drawn at random (by the operating system, never the model) from a deck of real people, trades and traditions
- random seed material

Then fresh agents filter, judge and attack, and the person steers at two short menus, because people are bad at specifying what they want and good at reacting to what's in front of them.

## How a run goes
1. **Intake.** Up to five short questions. The person's answers go to every agent verbatim, and the person confirms the brief ("Is this you?").
2. **Problems.** Two agents look for the real problem under the request, one with drawn moves and one without.
3. **The pool.** One agent fetches about 80 real entries from at least six sources across regions, eras and kinds. A script deals each idea agent its own random slice.
4. **Fan-out.** Four agents with drawn moves, one no-card control and one wild card write about 30 sketches.
5. **Filter.** A fresh judge scores every sketch, unlabeled and shuffled, for distance from the obvious answer, feasibility and fit. The answers every model reaches for ("wells") are flagged, not deleted.
6. **Gate 1.** The person picks two or three from a short menu.
7. **Develop and attack.** Each pick is developed, checked against real sources, and attacked by an adversary. When the brief demands something new, a prior-art search on each pick (patents, products, plugins, papers, forums, and the same principle in other fields) comes first.
8. **Gate 2.** The person chooses.
9. **The dossier.** The winner and the runners-up are fact-checked and written up as an idea dossier. That's where this skill stops: planning is a separate step, and the dossier is its brief.

It can also run in **cook mode**, where judges with different stakes make the gate decisions.

## Why diverse voices matter here
This method only works if the outside perspective is actually outside. A deck of moves drawn from the same few Western, mostly male thinkers would push every run toward the same corner. That's the homogeneity this project exists to escape. So the deck is deliberately broad:
- **Thinkers and trades:** it pairs thinkers with crafts, trades, folk practice, ecology, play and infrastructure.
- **Origin:** most moves of known origin are from outside the US.
- **US voices:** these lean toward communities of color and working-class traditions.

The tests bear this out. In the strongest variant, 6 of 10 menu items came from outside the Anglo-European canon. In a blind comparison of 40 ideas, all four top-rated ones did too. In the first real run of the current version, 10 of 12 menu items came from precedents outside the US and UK.

Breadth brings a responsibility: a one-line "move" can flatten a living tradition. So the deck's attributions are paraphrased inspirations, not quotations or endorsements, and have been reviewed so that cultural and religious practices are described accurately and respectfully. They haven't been independently verified one by one. If a card misrepresents a person or a tradition, please open an issue.

## What the tests have shown so far
- **Outside material beats instructions.** What widened the ideas was fetched data (the pool, the fact-checks). Telling agents to behave differently (tag your claims, avoid the typical, pick the least likely) changed little.
- **The pool is the engine.** With a fetched pool, even the no-card control lands nearly as far from the obvious answer as the carded agents.
- **Wells are real and predictable.** In the Raspberry Pi run, all five idea agents named the same four builds (an arcade, a smart mirror, a photo frame, a media center) before seeing their pools. None of them won.
- **Fact-checking catches what memory gets wrong.** Every final dossier is checked against fetched sources. In tests, it found a confident wrong claim in two of five final documents, and unflagged guesses in every one.

The full record of what each run taught the skill is in [`docs/creative-iteration/LESSONS.md`](docs/creative-iteration/LESSONS.md). A complete example run, with every round, the dossier and a post-mortem, is in [`docs/creative-iteration/examples/pi-monitor/`](docs/creative-iteration/examples/pi-monitor/).

## The road to 1.0
- **Run v0.6 on more briefs,** especially gift choices, trips, team rituals and fundraisers, and the *refine* setting, which hasn't been tested.
- **Verify the deck** card by card, and fill its thin regions (Africa, South America and Oceania are underrepresented).
- **Gate 1 as a conversation,** so the person's own angles shape development, not just their picks.
- **Cheaper runs.** A typical run uses 19–29 agents and 1.4–1.9M tokens. A lite mode for quick decisions is planned.
- **Cross-model runs,** to test whether mixing models widens the ideas further, given that models share wells.
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

Then ask Claude Code something like "I've got a pile of scrap wood, what should I make?" and the skill picks it up. Runs are written to `runs/` in your working folder.

**One rule for running it:** the session orchestrating a run must never read `deck/deck.json`. It only draws cards through `scripts/draw.py`. Reading the deck primes the model, and the draw stops being outside randomness. Reading the deck yourself is fine.

## Layout
| Path | What it is |
|---|---|
| `skills/creative-iteration/SKILL.md` | The method |
| `skills/creative-iteration/references/` | Agent prompts (`roles.md`), the judging rubric (`click.md`) and file templates (`templates.md`) |
| `skills/creative-iteration/scripts/` | `draw.py` (random cards, logging, credits, stats) and `deal.py` (random pool slices) |
| `skills/creative-iteration/deck/deck.json` | The move and constraint deck |
| `skills/creative-iteration/data/` | Your local draw log and well ledger (the answers models keep reaching for, by kind of brief). Created on first use, never committed |
| `docs/creative-iteration/` | Lessons from every run, and an example run |

## License
MIT. See [LICENSE](LICENSE).
