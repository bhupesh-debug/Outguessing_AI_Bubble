# All Scenarios — Outguessing the AI Bubble

Scenarios are weather forecasts for a picnic: you pack for rain even when sunshine is the likelier outcome, because the cost of being wet is larger than the cost of carrying an umbrella. Six scenarios cover this market. The first three are the main paths — Base, Bull, and Bear — with probability framings anchored on the article's own Bayesian exercise, which put a correction in the financing layer within 12 months at 32 percent (Tool 3, a teaching number, not a market price): Bear 32 percent, Base 45 percent, Bull 23 percent. Those three are working assumptions that sum to 100 percent, stated so that the reader can argue with them. The last three are surprise overlays: each can arrive inside any of the three main paths, and each is framed by its triggers rather than a false-precision probability.

Source: *Outguessing the AI Bubble* (Dimri, Nov 8, 2026), Table 7. Ranges below are computed by this project's Monte Carlo (seed 20261108, 100,000 trials; see [MONTE_CARLO.md](MONTE_CARLO.md) and `results/scenario_ranges.json`). **Every range is a model estimate, not a fact.**

## How to read the ranges

- **Worst / Base / Best** for a scenario = the 5th percentile / median / 95th percentile of the $100 outcome **under that scenario held fixed** (conditional medians, computed in `src/scenarios.py`).
- **Scenario-weighted** = all three scenarios mixed at 32/45/23 — the range you actually face if you do not know which scenario arrives.

## 1. Base — the build arrives late (45%, working assumption; the modal outcome)

| | Triggers |
|---|---|
| What has to happen | S-1s show revenue below run-rate but not catastrophic; Oracle free cash flow stays negative one more year; capex growth slows toward cloud revenue growth. |

**What follows:** the tail reprices mildly — spreads widen, Oracle and neocloud equities flat to down; the core absorbs a capex slowdown; hiring tightens first in the tail; the build continues at a slower pace.

**$100 after 12 months (model estimates):**

| Position | Worst (5th) | Base (median) | Best (95th) |
|---|---|---|---|
| Leveraged tail | $88.67 | $105.05 | $121.40 |
| Profitable core | $98.17 | $108.01 | $117.97 |
| Diversified | $101.06 | $106.00 | $110.93 |

**Default plan:** assume the revenue arrives late, size the tail so the bad branch is survivable, and keep building.

## 2. Bull — revenue arrives on schedule (23%, working assumption)

| | Triggers |
|---|---|
| What has to happen | S-1s show margins recovering; Anthropic sustains profit; revenue per $1 of compute stays above $1.50 and rising; cloud revenue outgrows capex. |

**What follows:** the bubble thesis dissolves; the leveraged tail rallies hardest, because it was priced for distress; capex continues; the episode is re-remembered as a boom.

**$100 after 12 months (model estimates):**

| Position | Worst (5th) | Base (median) | Best (95th) |
|---|---|---|---|
| Leveraged tail | $115.32 | $139.99 | $164.60 |
| Profitable core | $101.83 | $114.97 | $128.05 |
| Diversified | $102.44 | $109.01 | $115.60 |

**Preparation needed:** none beyond not having sold everything in fear. The Bull case is the reward for being early and right.

## 3. Bear — correction in the financing layer (32%, the Bayesian teaching posterior from Tool 3)

| | Triggers |
|---|---|
| What has to happen | S-1 booked revenue far below run-rates; Oracle downgraded; a Stargate or Abilene financing delayed or restructured; credit spreads widen materially. |

**What follows:** the leveraged tail reprices first, as telecom vendor-financing did in 2001; neocloud or SPV defaults become possible; the profitable core absorbs a capex slowdown; the technology survives and gets cheaper.

**$100 after 12 months (model estimates):**

| Position | Worst (5th) | Base (median) | Best (95th) |
|---|---|---|---|
| Leveraged tail | $25.54 | $50.02 | $74.54 |
| Profitable core | $63.61 | $80.00 | $96.48 |
| Diversified | $83.75 | $92.01 | $100.27 |

**Preparation needed:** this is the case that demands preparation in advance, because repricings in leveraged tails happen fast and the exit narrows while you are still deciding. Size the tail so the 5th-percentile outcome is a bad year, not a ruinous one.

## 4. Downside surprise — the S-1 shock (low probability, high impact; conditional wildcard)

| | Triggers |
|---|---|
| What has to happen | Booked revenue less than half the quoted run-rate; Oracle cut to one notch above junk; a major financing pulled outright. |

**What follows:** forced selling in the tail; stress reaches private credit and non-bank lenders, the tail the IMF warned about; banks stay resilient under the IMF's own stress test; the repricing is sharp but contained.

**Why no point probability:** a surprise is by definition the event the model did not price. It is framed by triggers, not by a false-precision number.

## 5. Upside surprise — inference economics jump (plausible; conditional wildcard)

| | Triggers |
|---|---|
| What has to happen | Revenue per $1 of compute jumps (Anthropic's $2.08 keeps rising); a DeepSeek-style efficiency gain; custom silicon cuts costs sharply. |

**What follows:** revenue arrives ahead of schedule; the Sequoia gap closes from the revenue side; the bubble thesis dissolves faster than in the Bull case; the winners are the efficient, not the biggest spenders.

## 6. Physical surprise — power binds first (plausible, most missed; conditional wildcard)

| | Triggers |
|---|---|
| What has to happen | Interconnection queues lengthen; transformer lead times extend beyond 144 weeks; state moratoria; power prices spike. |

**What follows:** the build slows regardless of how much capital is available; power and grid owners gain pricing power; timelines stretch rather than collapse; the constraint nobody modelled becomes the story.

**Note:** this is the one surprise the Monte Carlo cannot see at all — the power constraint appears nowhere in the simulations' inputs ([MONTE_CARLO.md](MONTE_CARLO.md), "What the simulations cannot do").

## Scenario-weighted ranges (all three main paths mixed at 32/45/23)

| Position | Worst (5th) | Base (median) | Best (95th) | P(losing money) | P(losing >20%) |
|---|---|---|---|---|---|
| Leveraged tail | $34.90 | $102.29 | $151.64 | 46.2% | 31.7% |
| Profitable core | $69.89 | $105.51 | $121.77 | 36.3% | 16.1% |
| Diversified | $86.92 | $104.67 | $112.52 | 31.6% | 0.3% |

Read the table as a set of tripwires, not a forecast. The lesson of the weighted row is the whole point of the exercise: the tail's median is fine, and its downside is a cliff. Diversification barely changes the median outcome, and it nearly eliminates the catastrophic branch.

## What changes the call

| Evidence | Moves you toward |
|---|---|
| First audited OpenAI / Anthropic S-1s | Either side — the single most informative marker |
| Oracle free cash flow print (positive vs still negative) | Bull (positive) / Bear (negative) |
| Oracle or neocloud downgrade / default | Bear, fast |
| Cloud revenue outgrowing capex for 2+ quarters | Bull |
| Credit spreads widening materially | Bear |
| DeepSeek-style efficiency gain / custom silicon at scale | Upside surprise |
| Interconnection queues lengthening / moratoria | Physical surprise |

A clear-eyed observer prepares for all six rather than betting on one. The three surprises are the reason the preparation is general rather than specific: you cannot hedge a power moratorium with a put option on Oracle, but you can avoid depending on any single lab, cloud, or subsidy for your income.
