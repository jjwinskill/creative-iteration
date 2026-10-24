# Post-mortem: v0.5's first real run (Raspberry Pi + old monitor)

Fri Oct 23 2026, 23:57 UTC. Gated, with the person at both gates. The run files are in this folder.

**Result:** The person chose the **Patchwork Booth** (a button and ring light in a cigar box; press it, tell a one-minute story, and it becomes a patch on a quilt that grows on the old monitor). Their reaction at the menu: "oh these are starting to get good!!!"

**Cost:** 19 agents, about 1.43M tokens and 50 minutes, 13 of them waiting at the gates. Cheaper than any of the A/B/C variants (1.5–1.9M).

## What v0.5 changed, and whether it worked
| Change | Verdict | Evidence |
|---|---|---|
| Fetched pool (precedents) | **Works, second time running** | Control distance 4.0 vs. cards 4.1: the pool did the widening. 10 of 12 menu items came from precedents outside the US and UK. The winner draws on Chilean arpilleras and Medellín. |
| Wells from unprompted lists | **Works** | All 5 generators named the same 4 wells: arcade, smart mirror or dashboard, photo frame, media centre. That's exactly the four I predicted privately. None won, and they stayed visible in the convergent lane. |
| Menu grounding check | **Earned its keep** | It dropped one item that rested on a Hong Kong slow-TV broadcast nobody could find. |
| Dossier fact-check | **Earned its keep** | 29 claims: 1 wrong (fixed), 3 unflagged guesses (marked). |
| 3 moves per agent | **Mixed** | Fine overall, but see problem 3. |

## What went wrong
1. **A backstory became a requirement.** The "what killed the last one" answer (the Rat clone) became problem 1 for both problem agents. The lead's framing then turned it into a principle ("faults found step by step with a multimeter"), so most sketches argued for multimeter-testability and two made debugging their whole point. **Josh caught it at Gate 1.** It's the same failure as the run 5 bonus, through a new door: context promoted to a constraint.
2. **The fact that decided the winner wasn't in the brief.** The kids came up only at Gate 2. My intake bundled "which room, and who else uses that room?" into one question, and the person answered the room half ("no real bearing"), so the who-else half was lost. That's my fault, not the skill's.
3. **One constraint swallowed its generator.** "Smell and touch only" applied to all six sketches, so all six became scent machines and the judge folded four of them into one group. That's about four wasted sketches.
4. **The wild slots stopped meaning anything in surprise mode.** Surprise orders the menu by distance, so the main list already held every distance-5 idea, and the wild slots became just the next two in line. The winner arrived through one of them.
5. **"Fatal" hid "fatal unless".** The adversary called all three picks fatal, each for want of a fact about the person. One sentence from them resolved it in 2 minutes. The label overstated the problem.
6. **Rule 6 leak, again.** A problem agent used the person's name, which the brief never gave. It came from inherited context.

## What I'd change for v0.6
1. **Context stays context.** Only the why, the no list and stated limits may become principles in the framing. Background stories inform, and the framing names them as background. Ask "what killed the last one" as color, not as a problem to solve.
2. **One question, one thing.** Never bundle intake questions. Always ask "who else will use or see it?" on its own.
3. **A constraint shapes two sketches, not six.**
4. **Wild slots take what the drift setting underweights.** In refine or stretch, the highest distance. In surprise, the best fit below the cut.
5. **The adversary labels "fatal unless <premise>"** separately from plain fatal. Gate 2 then shows those as questions for the person.
6. **The rule 6 leak:** test whether role prompts can carry a stronger line, or whether agents should be spawned with less inherited context. Needs a look at what they inherit.

**Stable across both v0.5 runs:** outside material widens ideas; instructions don't. The pool is the engine.
