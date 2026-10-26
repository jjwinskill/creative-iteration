# What a run costs, and how v0.12 cuts it

Every number here was priced from Claude Code's own transcripts (`scripts/cost.py`): the lead session plus every subagent, by model, at list prices, with cache reads, cache writes and output priced separately. Earlier metrics files counted tokens in different ways (some a final context size, some a sum over calls), so they can't be compared. These can.

## Every sandbox session so far

| Session | Skill | Lead | Subagents | Total |
|---|---|---|---|---|
| Pi monitor | v0.5 | $7.29 | 19 agents, $4.67 | $11.96 |
| Guitar tech (next run) | v0.6 | $6.32 | 20, $4.19 | $10.51 |
| Variant tests A, B, C | v0.6 | $6.13–8.14 | 22–29, $3.01–4.70 | $9.14–12.51 |
| Pinball, three rounds | v0.7 | $13.88 | 36, $13.26 | $27.14 |
| Guitar shape | v0.9 | $6.04 | 14, $6.84 | $12.89 |
| Shape tooling (side project) | — | $31.84 | 60, $26.91 | $58.75 |
| Gift test, plain Claude | — | $0.86 | 0 | $0.86 |
| Gift test, two skill arms | v0.10 | $14.37 | 43, $9.29 | $23.65 |
| **Gated design run** | **v0.11** | **$13.24** | **29, $18.56** | **$31.80** |
| Plain Claude, same brief | — | $2.54 | 0 | $2.54 |

Lead sessions include any chat after the run, so they run a little high.

## Where the v0.11 run's $31.80 went

| Part | Cost | Share |
|---|---|---|
| The lead (Opus), 141 calls, average context 260k tokens | $13.24 | 42% |
| 14 default browsing agents | $16.41 | 52% |
| 15 lean agents | $2.15 | 7% |
| of which the cards: operator, problem, mutation and wild-card agents | about $0.40 | about 1% |

- **The cards aren't the cost.** Running every card stage costs about forty cents. Dropping them would save nothing worth having.
- **Browsing after the menu was most of the agent spend.** Prior art $4.24, development $6.69 and a second closeness pass $3.17, against $3.46 for every agent up to the menu.
- **Developers repeated the prior-art searches.** They were the most expensive agents ($0.88–2.61 each, 22–45 calls). Identical search results were fetched up to five times across prior-art, closeness and developer agents.
- **A doomed pick was fully worked.** The person cut one pick at Gate 2 as too close to an existing work. Its prior art and development had already cost $1.69, and a cheap adversary had flagged it first.
- **Each browsing call carried 54k tokens of fixed context:** the full tool set and system prompt, before the agent read its task. Over 363 calls, that's about $5.
- **The lead paid to re-read itself.** Each call re-reads the whole context: cache reads were $7.28 of the lead's $13.24. It retyped about 120k characters of round files from agents' reports, which were output tokens at Opus prices, and every one of them stayed in the context afterward.
- **Up to the menu, the skill cost about $8.60,** including the lead, against plain Claude's $2.54. After the menu came another $23.

## The v0.12 plan, keeping the cards

| Lever | What changes | Estimated saving on a run like v0.11 |
|---|---|---|
| `ci-browse` agent type | Five tools instead of the full set; its own folder; a call budget; returns a short summary | about $4.50 (fixed context 54k down to roughly 10k a call; to be measured) |
| One prior-art pass that covers near relatives | No second closeness pass | about $2.50 |
| Developers read the prior-art file, budget of 10 fetches | No repeated catalog searches | about $3 |
| Closeness rated at the menu | A near copy is flagged before anyone develops it | $1.70 when it happens |
| Shared fetch cache (`scripts/fetch.py`) | Each page fetched once a run; agents keep only the fields or snippets they need | Smaller tool results, so fewer cache writes; part of the lines above |
| A thin lead | Blocks and inputs in files; agents write their own outputs; `scripts/blind.py` builds judge inputs; no retyping | about $5 (fewer output tokens and a smaller context on every call) |
| **Total** | | **about $15–17 instead of $31.80** |

Plain Claude stays the honest baseline for comparison, at about $2.50 a brief. A gated skill run will always cost more, because it fetches a pool, runs gates and checks prior art. The question each run should answer is whether the extra buys ideas the person keeps.

## How to check it

Every run ends with `scripts/cost.py --since <start> --json agents/cost.json`. The report gives the total, the lead/lean/browse split and the most expensive agent. The next run tests the estimates above: if `ci-browse` doesn't start near 10k tokens, or the lead's average context doesn't fall, the levers get revisited.
