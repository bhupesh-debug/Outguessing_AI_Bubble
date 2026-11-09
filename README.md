# Outguessing the AI Bubble

[![Research: 7 Nov 2026](https://img.shields.io/badge/research-7%20Nov%202026-blue)](docs/research-report.md)
[![Article: 8 Nov 2026](https://img.shields.io/badge/article-8%20Nov%202026-blue)](docs/article.md)
[![Monte Carlo: 100,000 trials](https://img.shields.io/badge/Monte%20Carlo-100%2C000%20trials%20%C3%97%203-green)](src/monte_carlo.py)
[![Seed: 20261108](https://img.shields.io/badge/seed-20261108-lightgrey)](results/monte_carlo_results.json)
[![Tests: 10 passing](https://img.shields.io/badge/tests-10%20passing-brightgreen)](tests/test_project.py)
[![License: research & education](https://img.shields.io/badge/license-research%20%26%20education-yellow)](README.md)

> **Verdict, in one sentence:** a bubble is **forming in the financing of AI infrastructure** — about **$1.4 trillion** of future revenue commitments raised against about **$950 billion** of equity and debt — concentrated in a leveraged tail, while the technology itself is real, the revenue is growing, and a pop is **not yet proven**.

**This is research and education, not investment advice.** Every market number here comes from the November 7, 2026 research review or a primary source named in the text; teaching numbers are labelled as such. Nothing in this project is a forecast, a recommendation to buy or sell anything, or a guarantee.

## Try it live

**[Open the interactive simulator](index.html)** — adjust the scenario, the lab sector's revenue per $1 of compute, hyperscaler capex, and your allocation across the three positions, and watch the Monte Carlo distributions move. It runs entirely in your browser (10,000 seeded draws, no server, no tracking).

## What this project is

This repository turns the article [*Outguessing the AI Bubble*](docs/article.md) (Bhupesh Chandra Dimri, November 8, 2026, 31 pages) into runnable, checkable work. The article applies the outguessing framework — reading incentives, anticipating counter-moves, testing beliefs against evidence — to the AI market as it stood on November 7, 2026. The framework comes from William Poundstone's *Rock Breaks Scissors* (Little, Brown and Company, June 2014, 320 pp, ISBN 978-0-316-22806-0); the dust-jacket principle is that people cannot act randomly and display unconscious patterns. Only verified book facts are used; everything beyond them is labelled as established theory or as the project's own teaching examples.

The article's own structure is preserved here: **hypothesis → five worked tools → three simulations → observation protocol → scenarios → Monte Carlo → SWOT → recommendation → what to avoid → conclusion**, plus the First Diagnostic Question in its own paper.

## The hypothesis

> **H:** The AI infrastructure build is a **financing bubble in the leveraged tail, not a technology bubble**: end-user cash flow will arrive too slowly to service the roughly $1.4 trillion of circular revenue commitments on schedule, so the leveraged tail — Oracle, the neoclouds, and the supplier-guaranteed deals — reprices within 24 months, while the profitable hyperscaler core absorbs the shock and the technology itself survives and gets cheaper.
>
> **H₀:** The build is self-funding on schedule: commitments convert to cash as written, labs' revenue per dollar of compute keeps rising past $1.50, and any price falls are ordinary volatility.

The article's own Bayesian exercise put the chance of a correction in the financing layer within 12 months at **32%** — a teaching number, not a market price. Full confirm/falsify conditions: [HYPOTHESIS.md](HYPOTHESIS.md).

## What the research found — claim verdicts

| Claim | Verdict |
|---|---|
| Frontier training costs hundreds of millions to >$1bn; returns incremental not exponential | **Partly confirmed** — GPT-4 $78m compute, Gemini Ultra ~$192m, Llama 3.1 405B ~$170m (Stanford AI Index 2025); cost per fixed capability collapsed >280× |
| Oracle ~$300bn AI commitment | **Partly confirmed** — $300bn is OpenAI's purchase obligation *to* Oracle; Oracle RPO $455bn +359% at Aug 31, 2025; total debt ~$111bn; Moody's Baa2 / S&P BBB negative |
| Circular financing (NVIDIA / hyperscalers / labs) | **Confirmed as structure** — IMF GFSR Oct 13, 2026: 14 deals, $300bn equity + $650bn debt → $1.4tn commitments; BIS Bulletin 137: 55.2% of AI investment from other AI firms |
| Hyperscaler capex | **Confirmed** — $416bn in 2025 (+66%); 2026 guidance ~$645bn+ |
| End of "free" AI and thin wrappers | **Partly confirmed** — per-token prices fell; thin wrappers failing, workflow-deep products thriving |

Full evidence: [data/claim_verdicts.csv](data/claim_verdicts.csv) and the research report.

## Monte Carlo — actually run, not illustrated

Three simulations, **100,000 trials each, fixed seed 20261108**, run in [`src/monte_carlo.py`](src/monte_carlo.py). Re-run them with `python run.py`. Results in [`results/monte_carlo_results.json`](results/monte_carlo_results.json); method and limitations in [MONTE_CARLO.md](MONTE_CARLO.md).

| Simulation | Headline result (computed) | Probability that matters | Reading |
|---|---|---|---|
| **MC-1: Lab self-funding** | Median revenue per $1 of compute in 2029: **1.79** (5th–95th: 0.54–4.05) | P(below 1.0) = **17.9%**; P(above 1.5) = **61.9%** | Most likely self-funding by 2029, with a wide spread |
| **MC-2: Hyperscaler cash** | Median 2026 free cash flow: Amazon **−$51.6bn**; Google −$3.4bn; Meta −$0.7bn; Microsoft +$33.0bn | P(2+ of 4 cash-negative) = **80.8%** | The 2026 build is mostly not self-funding on guidance |
| **MC-3: Positions** | Median $100 after 12 months: tail **$102.29**; core $105.51; diversified $104.67 | P(losing >20%): tail **31.7%**; core 16.1%; diversified **0.3%** | The tail's median is fine; its downside is a cliff |

## Scenarios — base / best / worst

| Scenario | Probability | $100 after 12 months — Worst / Base / Best (model estimates) |
|---|---|---|
| **Bear** — correction in the financing layer | 32% | Tail $25.54 / $50.02 / $74.54 · Core $63.61 / $80.00 / $96.48 · Diversified $83.75 / $92.01 / $100.27 |
| **Base** — the build arrives late | 45% | Tail $88.67 / $105.05 / $121.40 · Core $98.17 / $108.01 / $117.97 · Diversified $101.06 / $106.00 / $110.93 |
| **Bull** — revenue arrives on schedule | 23% | Tail $115.32 / $139.99 / $164.60 · Core $101.83 / $114.97 / $128.05 · Diversified $102.44 / $109.01 / $115.60 |
| **Surprise overlays** (no point probability — a surprise is by definition unpriced) | — | **S-1 shock** (downside): booked revenue < half the run-rate. **Inference economics jump** (upside): revenue per $1 of compute jumps. **Power binds first** (physical): interconnection queues, transformer lead times beyond 144 weeks, moratoria. |

Scenario-weighted ranges (all three scenarios mixed): tail $34.90 / $102.29 / $151.64 · core $69.89 / $105.51 / $121.77 · diversified $86.92 / $104.67 / $112.52. Full detail: [SCENARIOS.md](SCENARIOS.md).

## SWOT — the shape of the table

Strengths are about the **technology and the profitable core**; weaknesses and threats are about the **financing and the leveraged tail**. That asymmetry is the article's whole argument in one table. Full analysis: [SWOT.md](SWOT.md).

- **Strengths:** cloud revenue +39–103% YoY in Q3 2026; NVIDIA Data Center $115.2bn FY2025 (+142%); Anthropic's first adjusted operating profit; capability cost down >280×.
- **Weaknesses:** no audited lab financials; no disclosed GPU utilisation; only 6% of organisations attribute ≥5% of EBIT to AI; GPUs economically obsolete in 2–3 years on the bear case; extreme concentration.
- **Opportunities:** inference economics improving; custom silicon diversifying supply; workflow-deep products thriving; enterprise AI still early.
- **Threats:** $1.4tn circular commitments; Oracle ~$105–112bn debt, negative free cash flow, negative outlooks, $248bn off-balance-sheet leases; power as the binding constraint; valuations priced on run-rates, not audited GAAP revenue.

## Recommendation — in one sentence

> Treat the core and the tail as different assets, own the workflow rather than the model call, and let the markers — not the headlines — decide when the thesis changes.

Seven actions and ten traps to avoid, each with the reason it hurts and the replacement move: [RECOMMENDATION.md](RECOMMENDATION.md).

## What this project cannot do — read before quoting it

- **Could not verify:** audited OpenAI/Anthropic financials (none exist publicly); GPU utilisation (no hyperscaler discloses it); exact Oracle contract terms (not in any public filing).
- The simulations inherit every weakness of their inputs. MC-1 blends two anchors that measure different things; MC-2/MC-3 distributions are assumptions, not measurements; the three simulations are not independent — a bad prospectus moves all three at once, so their probabilities cannot simply be multiplied. A Monte Carlo cannot discover a risk nobody put into the model — the power constraint appears nowhere in these numbers.
- The 32% posterior, the scenario probabilities, and the scenario returns are **teaching numbers**, not market prices. The single most informative marker is the first audited OpenAI and Anthropic prospectus.

## How to run it

```bash
python -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python run.py          # re-runs all three Monte Carlos + scenario ranges
.venv/bin/python -m pytest tests/ -v   # 10 tests, all passing
```

Outputs: `results/monte_carlo_results.json`, `results/scenario_ranges.json`, `charts/fig6_montecarlo.png` (the article's Figure 6, reproduced).

## Contents

| File | What it is |
|---|---|
| [README.md](README.md) | This file |
| [index.html](index.html) | Interactive simulator (the live site homepage) — self-contained, no external requests |
| [HYPOTHESIS.md](HYPOTHESIS.md) | Testable hypothesis with confirm/falsify conditions |
| [SCENARIOS.md](SCENARIOS.md) | All six scenarios with triggers, ranges, and tripwires |
| [MONTE_CARLO.md](MONTE_CARLO.md) | Method, distributions, assumptions, limitations, results |
| [SWOT.md](SWOT.md) | Full SWOT analysis, every line traceable to the research |
| [RECOMMENDATION.md](RECOMMENDATION.md) | Recommendation, what to avoid, conclusion |
| [DIAGNOSTIC_QUESTION.md](DIAGNOSTIC_QUESTION.md) | The First Diagnostic Question, verbatim and unanswered |
| [src/monte_carlo.py](src/monte_carlo.py) | The three simulations (seed 20261108, 100,000 trials each) |
| [src/scenarios.py](src/scenarios.py) | Base/best/worst ranges + scenario-conditional medians |
| [data/](data/) | Claim verdicts, scenarios, and Monte Carlo inputs (CSV/JSON) |
| [docs/article.md](docs/article.md) | The full article text (Markdown twin of the 31-page paper) |
| [docs/research-report.md](docs/research-report.md) | The deep-research report the article is built on (7 Nov 2026) |
| [docs/diagnostic-question-paper.md](docs/diagnostic-question-paper.md) | The companion paper holding the book material and the diagnostic question |

## Sources

- Dimri, B. C. (2026, November 8). *Outguessing the AI Bubble* (31 pp). The article this project is built from.
- Dimri, B. C. (2026, November 7). *AI Bubble Critical Analysis* — deep-research report (the evidence base).
- Dimri, B. C. (2026, November 8). *The First Diagnostic Question — Outguessing the AI Bubble* (companion paper).
- Poundstone, W. (2014). *Rock Breaks Scissors*. Little, Brown and Company. (Framework; verified bibliographic facts only.)
- IMF (2026, Oct 13). Global Financial Stability Report press briefing. · BIS Bulletin No. 137 (2026, Oct 1). · Stanford HAI, AI Index Report 2025. · Platformonomics (2026, Feb 25). · Epoch AI, Cottier et al., arXiv:2405.21015.

## Author

**Bhupesh Chandra Dimri** — Financial Analyst, JPMorgan Chase (Jul 2025–present); M.S. Accounting Analytics & Data Technology, Pace University (Dec 2025). GitHub: [bhupesh-debug](https://github.com/bhupesh-debug) · Contact: bhupesh7cd@gmail.com
