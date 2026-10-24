# The click and novelty: the judging rubric

In gated mode the person judges at the gates. This rubric is for the cook-mode judges, and it's background for the adversary and the filter judge. Paste the scoring section into every cook-mode judge's prompt.

## Where it comes from

- **Insight feels right because it often is.** Salvi, Bricolo, Kounios, Bowden and Beeman (2016) found that answers reached by insight were right more often than answers worked out step by step. The theory: insight surfaces all at once, after the unconscious work is done.
- **The aha is relief and certainty, not surprise.** Danek and Wiley (2017) had people rate their own ahas. Pleasure, relief and certainty predicted them; surprise did not. So surprise is measured separately, as novelty.
- **The aha is a compression event.** Schmidhuber: interestingness is compression progress, when many observations collapse into one rule. "Oh, that's how the API works" is a dozen weird behaviors becoming one sentence.
- **Constraints resolving together is coherence.** Thagard and Verbeurgt (1998) formalized coherence as satisfying the most weighted positive and negative constraints among elements. Christopher Alexander (*Notes on the Synthesis of Form*, 1964): good form is the absence of misfits between the form and its context.
- **Self-reported confidence is poorly calibrated** in language models, so certainty is measured as agreement among independent judges.

## Scoring a whole (judges)

Score each candidate against the brief's tension register. You see the candidates shuffled and unlabeled; one may be the plain answer anyone would give.

| Signal | Question | Score |
|---|---|---|
| **Release** | Which named tensions does it resolve, and how many new parts did it add to do it? | List them. Resolving many tensions with few parts is strong. One new part per tension is an **epicycle**, the anti-click. |
| **Gift** | Does it solve something that isn't on the register at all, a benefit nobody asked it for? | Name it, or "none." This is the strongest single signal. |
| **Fit** | Does it pass the brief's why-test for the audience on the dial? | Yes / partly / no, with one sentence why. |
| **Coherence** | Do its parts reinforce each other, or merely coexist? | Name the reinforcing pairs, and any part that clashes. |
| **Scars** | After the adversary's attack, what weakness is left? Can it be labeled honestly and lived with? | List them. |

Then **rank all candidates** and say in two sentences why your first pick beats your second. Then say in one or two sentences what combination of candidates would beat your first pick, if one would. When judges converge on a combination, it becomes the next integrated whole. Don't report a confidence percentage; your ranking, compared with the other judges', is the confidence.

## Novelty (the lead computes it)

For each whole, check whether its central idea appears in any cold sample or is a well (the ledger, or the unprompted lists of 3 or more agents). If neither, it's novel. If either, it's typical: that's fine for a ticket, but weak for differentiation work. Say which.

## Distance (judges, when the drift setting is stretch or surprise)

How far is this candidate from the plain answer anyone would give? Say "same kind of thing, improved", "a different form serving the same need", or "a different kind of thing entirely", with one sentence why. In *surprise*, rank candidates that click by distance first.

## Verdict (the lead)

A whole **clicks** when all of these hold:
- At least two of the three judges rank it first.
- It beats the obvious answer.
- Its release has more tensions resolved than parts added.
- It survived the adversary with only scars that can be labeled.

Report click and novelty separately.

**Stability.** For each element of the winner, count how many independent agents produced it (generators, cold samplers, judges' combinations). Elements found two or more times are stable, and another run would likely find them again. An element that came from a single pick, the lead's or one agent's, is fragile, and another run could land elsewhere. Put both lists in the report. When nothing clicks, read the judges' disagreements: they usually name the tension that the framing got wrong, and that tension is what the walk should work on.

## Tripwires (sycophancy)

Treat any of these as a warning sign, not a click:
- The pick pleases the person but resolves nothing new.
- Everyone agreed and no one was attacked.
- The winner is the first idea generated.
- The winner adds a part for every constraint.
