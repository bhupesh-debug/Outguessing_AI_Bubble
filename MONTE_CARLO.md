# Monte Carlo Simulations — Outguessing the AI Bubble

A Monte Carlo simulation is a way of asking "what if?" a hundred thousand times. You describe the uncertainty in each input as a range, roll the dice on all of them at once, and look at the spread of outcomes instead of a single guess. It is like testing a bridge design against ten thousand different storms instead of one: you learn not just whether it stands, but how often it falls and by how much.

The three simulations below were actually run in Python — **100,000 trials each, fixed seed 20261108**, script in [`src/monte_carlo.py`](src/monte_carlo.py) — and every input comes from the research review or from the article's own teaching numbers, stated next to the result it feeds. **Nothing in this section is a forecast.** It is a measurement of how wide the range of honest outcomes is, given what is known today.

Reproduce everything with `python run.py`. Outputs: `results/monte_carlo_results.json`, `results/scenario_ranges.json`, `charts/fig6_montecarlo.png` (the article's Figure 6).

## MC-1: Does the lab sector pay for its own compute?

**The question that decides the bubble** is whether the labs' revenue covers the compute they buy.

**Inputs.** The research review gives two anchors, pointing in opposite directions: Anthropic reported about **$2.08 of revenue per $1 of compute** in Q2 2026, while OpenAI was reported to spend **$1.69 per $1 earned** in 2025, or about **$0.59 of revenue per $1 of cost**. Both figures are secondary reports, not audited filings, and they measure slightly different things, so the simulation starts the sector ratio at a distribution rather than a point: Normal(1.30, 0.50), truncated to [0.20, 3.00], which spans both anchors. Each year the ratio grows by a factor drawn from Normal(0.15, 0.25), truncated to [−0.50, +1.00]: inference efficiency gains are large — the cost of a fixed level of capability fell more than 280 times in 18 months — but revenue per unit of compute improves more slowly than capability per dollar, so 15 percent a year is a deliberately conservative mean, stated as an assumption.

**Computed result:**

| Year | Median revenue per $1 of compute | 5th–95th percentile |
|---|---|---|
| 2026 (starting ratio) | 1.30 | 0.48–2.12 |
| 2027 | 1.44 | — |
| 2028 | 1.61 | — |
| 2029 | **1.79** | **0.54–4.05** |

- Probability the sector is still below self-funding in 2029 (ratio under 1.0): **17.9%**
- Probability it is above the research's healthy threshold of 1.50: **61.9%**
- Probability it is below 0.50 — deeply underwater: **4.3%**

**Read plainly:** on these inputs the lab sector most likely covers its compute from revenue by 2029, but nearly one run in five does not, and the spread is wide enough that the median is not the story. The result leans on the assumed 15 percent annual improvement: if efficiency gains stall, the failure probability rises fast.

## MC-2: Do the hyperscalers burn cash in 2026?

**Inputs** (research, Platformonomics verified live): 2025 operating cash flow of $139.5bn (Amazon), $164.7bn (Google), $115.8bn (Meta), $160.5bn (Microsoft), against 2026 capex guidance of $200bn, $180bn, $125bn, and $140bn respectively (Microsoft's guidance is $140bn-plus; 140 is used as the base). Operating cash flow in 2026 is modelled as 2025 cash flow grown by Normal(0.10, 0.08) — a stated assumption, conservative against cloud revenue growth of 39–103% but realistic for cash flow, which grows more slowly than revenue. Capital spending is modelled as guidance × Uniform(0.95, 1.10), because guidance in this cycle has repeatedly been beaten upward.

**Computed result:**

| Company | P(free cash flow negative in 2026) | Median 2026 FCF ($bn) | 5th–95th ($bn) |
|---|---|---|---|
| Amazon | **~100%** | **−51.6** | −74.6 to −28.3 |
| Google | 58.8% | −3.4 | −28.4 to +21.8 |
| Meta | 52.6% | −0.7 | −18.4 to +16.9 |
| Microsoft | 1.0% | +33.0 | +9.7 to +56.4 |

Jointly: probability that **two or more of the four burn cash in 2026 is 80.8%**, with an expected count of **2.1** cash-burning hyperscalers; probability all four burn cash is 0.3%; probability none does is effectively zero.

**Read plainly:** the research review's line survives the test and gets a number — the 2026 build is mostly not self-funding on guidance, and Amazon is the certainty, not the question, because $200bn of guided spending against $139.5bn of 2025 operating cash flow leaves a gap no plausible growth rate closes. The caveat is the modelled cash-flow growth: a stronger cloud year than the assumed 10 percent would improve all four, and the simulation cannot see a demand shock that cuts cash flow instead.

## MC-3: What does each position actually risk over 12 months?

**Inputs.** Scenario probabilities anchored on the article's own Bayesian exercise: Bear 32%, Base 45%, Bull 23%. Scenario returns are teaching assumptions, labelled as such: the leveraged tail returns −50% in the Bear case (a moderate reading of the dot-com base rates — NASDAQ down 78% peak-to-trough, Cisco down 86–90% and never regaining its peak), +5% in the Base case, +40% in the Bull case; the profitable core −20% / +8% / +15%; a diversified position (half core, half cash at +4%) −8% / +6% / +9%. Each return is drawn with a spread around its scenario mean; the outcome is the value of $100 after 12 months.

**Computed result:**

| Position | Median $100 after 12 months | 5th–95th | P(losing money) | P(losing >20%) |
|---|---|---|---|---|
| Leveraged tail | **$102.29** | $34.90–$151.64 | 46.2% | **31.7%** |
| Profitable core | **$105.51** | $69.89–$121.77 | 36.3% | 16.1% |
| Diversified | **$104.67** | $86.92–$112.52 | 31.6% | **0.3%** |

**Read plainly:** the tail's median is fine, and its downside is a cliff. Diversification barely changes the median outcome, and it nearly eliminates the catastrophic branch. An expected value that hides that difference is not an analysis; it is a trap.

## Summary table (article Table 8)

| Simulation | Headline result (computed) | Probability that matters | Reading |
|---|---|---|---|
| MC-1: Lab self-funding | Median revenue per $1 of compute in 2029: 1.79 (5th–95th: 0.54–4.05) | P(below 1.0) = 17.9%; P(above 1.5) = 61.9% | Most likely self-funding by 2029, with a wide spread |
| MC-2: Hyperscaler cash | Median 2026 FCF: Amazon −$51.6bn; Google −$3.4bn; Meta −$0.7bn; Microsoft +$33.0bn | P(2+ of 4 cash-negative) = 80.8% | The 2026 build is mostly not self-funding on guidance |
| MC-3: Positions | Median $100 after 12 months: tail $102.29; core $105.51; diversified $104.67 | P(losing >20%): tail 31.7%; core 16.1%; diversified 0.3% | The tail's median is fine; its downside is a cliff |

All figures are the actual outputs of the simulation script (100,000 trials each, seed 20261108), not illustrations. The re-run in this repository reproduces the article's results file exactly.

## What the simulations cannot do

The simulations inherit every weakness of their inputs, and the honest thing is to name them:

1. The starting ratio in MC-1 blends two anchors that measure different things (Anthropic's revenue per $1 of compute against OpenAI's total spend per $1 earned), so the true starting point is wider than the model admits.
2. The cash-flow growth and scenario returns in MC-2 and MC-3 are assumed distributions, not measured ones, and a different assumption moves the answers.
3. The three simulations are **not independent**: a bad prospectus would move all three at once, so their probabilities cannot simply be multiplied.
4. A Monte Carlo cannot discover a risk nobody put into the model — the power constraint, for example, appears nowhere in these numbers.

The simulations are a way of pricing the uncertainty you can name, not a way of naming the uncertainty you cannot.

## Where outguessing fails, and where it must stop

1. **Adaptation:** the moment NVIDIA learns that observers read its customer deals as a demand signal, it changes how it announces them, and the tell moves. The model decays the moment it is published.
2. **Regime breaks:** a new chip architecture, a power moratorium, or a war, and yesterday's incentive map is a historical document, not a guide.
3. **Overfitting:** fourteen deals feel like a system, and the IMF itself counted fourteen; but fourteen observations are not a law (Tversky & Kahneman, 1974).
4. **False precision:** a probability carried to two decimal places on a guessed prior is theatre, not analysis. The 32% posterior is a teaching number, not a market price.
5. **The ethical boundary:** outguessing is for reading incentives and improving your own decisions, not for manipulating people, manufacturing urgency, or presenting a guess as a guarantee.
