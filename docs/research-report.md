# Critical Analysis: Is the AI Market in a Bubble?
## Formation, financing, and the risk of a pop — evidence to 7 November 2026

**Date of research:** 7 November 2026
**Disclaimer: This is research and education, not investment advice.** Figures are as reported by the sources named; run-rate, booked (GAAP) revenue, commitments, and cash actually spent are different things and are kept separate below. Where a figure comes only from a leak, a press report, or a secondary aggregator, that is stated. No figure that could not be traced to a named source is presented as fact.

## Summary — answer first

**Verdict: bubble *forming in the financing layer*, not yet proven to be *near popping* — and not a simple repeat of 2000.**

- The strongest, best-documented facts are about **spending and leverage, not about demand collapsing**: frontier training now costs tens to hundreds of millions per run and is heading toward $1bn+; the four largest hyperscalers spent **$416bn on capex in 2025 (+66%)** and guided to roughly **$645–725bn in 2026**; and the IMF (13 Oct 2026) counts **14 circular deals since 2023 — ~$300bn equity + ~$650bn debt for ~$1.4tn of future revenue commitments**.
- The counter-evidence is also real and is what separates this from 2000: the biggest spenders are **highly profitable** (NVIDIA Data Center revenue $115.2bn in FY2025, +142%; Microsoft, Alphabet, Amazon cloud revenue grew 39–103% YoY in Q3 2026), cloud/AI revenue is growing fast in absolute terms, and Anthropic reported its **first positive adjusted operating profit in Q2 2026**. OpenAI is still deeply loss-making, but its revenue run-rate rose from ~$20bn (end-2025) to ~$50bn (end-Sep 2026).
- The gap that matters is therefore **timing and concentration, not zero revenue**: Sequoia's arithmetic (June 2024) implied ~$600bn/yr of end-user AI revenue was needed to justify the then-current infrastructure spend, against <$20bn of visible run-rate revenue at the time. That gap has narrowed in revenue terms but widened in capex terms. The IMF calls an AI correction one of its three top global risks, but explicitly says it is a *risk scenario*, not a forecast — and that under a severe stress test including an AI correction, the banking sector as a whole remained resilient.
- The most bubble-like segment is the **leveraged, concentrated tail** — Oracle, neoclouds, and suppliers financing a small number of private labs — not the hyperscaler core. A correction, if it comes, is most likely to hit that tail first, as telecom vendor-financing did in 2001, while the underlying technology survives.

| Claim | Verdict |
|---|---|
| 1. Frontier training costs hundreds of millions to >$1bn; returns incremental not exponential | **Partly confirmed** — hundreds of millions confirmed; >$1bn for a *single* run is projected, not yet documented; "incremental" is true in the scaling-law (log) sense, false if measured as cost per unit of capability, which has collapsed |
| 2. Oracle ~$300bn AI commitment | **Partly confirmed** — $300bn is OpenAI's *purchase obligation to Oracle*, not Oracle's own spend; ~5 years from 2027, 4.5 GW; Oracle's own borrowing and capex surge are confirmed, but Oracle never named OpenAI or $300bn in a filing |
| 3. Circular financing NVIDIA / hyperscalers / OpenAI / Anthropic | **Confirmed as a structure; partly confirmed as a bubble mechanism** — the loops are disclosed and quantified by IMF/BIS; no regulator has found fraudulent round-tripping; how much is "circular" vs normal vendor business cannot be settled from deal structure alone |
| 4. Massive hyperscaler data-centre capex | **Confirmed** — $416bn in 2025, guidance far higher in 2026; financed mostly from operating cash flow plus rapidly rising debt; utilisation is *not* publicly disclosed, so return evidence is indirect (cloud revenue growth, backlogs) |
| 5. End of "free" AI and thin wrappers | **Partly confirmed** — per-token prices have *fallen* sharply; total bills, subscription tiers and limits have tightened; thin wrappers are failing in large numbers while workflow-deep products (Cursor, Claude Code) thrive; AI hiring demand is strong for senior/AI roles, weaker for entry-level |

---

## 1. Frontier training costs and capability gains per dollar

### Verdict: Partly confirmed

### What the best sources say about cost

No frontier lab publishes an audited training-run cost. All figures are outside estimates, and they measure different things — compute-only for the final run, amortised hardware + energy, or total development cost including staff and failed runs. That distinction explains most disagreements.

- **Stanford AI Index Report 2025** (summarised at https://galileo.ai/blog/llm-model-training-cost , read 7 Nov 2026, index): GPT-3 (2020) ~$4.6m; **GPT-4 (2023) $78m in compute** (AI Index estimate, 21bn petaFLOPS) / **$78–100m+** in press summaries; **Gemini Ultra 1.0 ~$191–192m**; **Meta Llama 3.1 405B ~$170m**. The Index notes a 287,000× increase since the first Transformer (2017, ~$670). OpenAI CEO Sam Altman said GPT-4 cost "more than $100 million" (Wall Street Journal, 2023, via Stanford summaries).
- **Epoch AI, Cottier et al., "The rising costs of training frontier AI models", arXiv:2405.21015, first posted 31 May 2024, revised 7 Feb 2025** (via https://aiforsocialgood.ca/blog/the-cost-of-artificial-intelligence-analyzing-the-impact-on-businesses-consumers-and-society and https://the-variables.com/en/articles/serving-a-gpt-35-class-model-got-280-times-cheaper-building-a-frontier-one-crossed-100-million ): amortised hardware + energy cost of the *final* run has grown **~2.4× per year since 2016**; on that trend the largest runs pass **$1bn by ~2027**. In Epoch's accounting GPT-4 is ~$40m amortised vs $78m at cloud prices — i.e. the same model can legitimately be quoted at $40m, $78m or >$100m depending on the cost base. Total development cost splits roughly: hardware 47–67%, research/engineering staff 29–49%, energy 2–6%.
- **Anthropic CEO Dario Amodei, Lex Fridman Podcast #452 (2024)**, via https://www.datacenterdynamics.com/en/news/anthropic-ceo-ai-training-data-centers-to-be-10bn-in-2026-100bn-from-2027/ : frontier companies are "roughly $1 billion scale, plus or minus a factor of three" *now*; "next year we're going to go to a few billion, and then 2026, we may go to above $10 billion. And probably by 2027, [the] ambition [is] to build $100 billion dollar clusters." **Critical correction:** Amodei was talking about *clusters / data-centre build cost*, not a single training run. Secondary coverage routinely conflates the two. The $100bn figure is therefore not evidence that a single model cost $100bn.
- **DeepSeek V3, technical report, Dec 2024:** $5.58m for the final training run on 2,048 H800 GPUs over 55 days. Widely cited as a counter-example — but it counts only the final run, not prior R&D, data, staff, or failed runs, and DeepSeek had access to a large pre-existing cluster. It proves efficiency gains are possible; it does not prove frontier training is cheap.
- **Later, unverified estimates:** secondary aggregators put GPT-5 (2025) at $300–500m and Claude Opus 4 at $200m+. No primary disclosure supports a precise figure; treat as estimates, not facts.

**Bottom line on cost:** "Hundreds of millions" for a frontier run in 2024–25 is confirmed by Stanford/Epoch. "Over a billion" is a *projection* for ~2027 (Epoch) or a statement about cluster scale (Amodei), not a documented single-run cost to date.

### What about "incremental rather than exponential" returns?

This half of the claim needs a definition, because two true statements point in opposite directions:

1. **Per unit of compute, gains are diminishing (logarithmic).** Scaling laws are power laws: doubling compute gives a predictable but *less than doubling* improvement in loss/benchmarks. That is the standard reading in the literature and the reason Amodei himself adds the caveat: if $100bn clusters are "still not enough… either we need even more scale, or we need to develop some way of doing it more efficiently."
2. **Per dollar, capability has got dramatically cheaper — because inference efficiency has outrun training-cost growth.** Stanford AI Index 2025, Ch.1 Fig.1.3.23: the cost of querying a model at GPT-3.5 level (64.8 on MMLU) fell from **$20.00 per million tokens in Nov 2022 to $0.07 in Oct 2024 — a >280-fold reduction in ~18 months**. Epoch AI, cited by the Index, found inference prices falling 9–900× per year depending on task. In other words, *building* the frontier gets more expensive while *using* a given level of capability gets far cheaper. Both can be true at once.
3. **Benchmark convergence:** Stanford AI Index 2025 also found the performance gap between frontier (closed) and open models narrowing sharply (e.g. Llama 3.1 405B reached GPT-4-level training compute ~16 months later). That supports "incremental at the frontier" — the next model is better, but not by the multiples seen in 2020–23, and rivals catch up in months.

**Verdict restated:** The cost escalation is confirmed; the >$1bn single-run claim is not yet confirmed; "incremental returns" is confirmed *if* it means diminishing returns to additional training compute at the frontier, and contradicted *if* it means capability per dollar is stagnating — it is falling fast at fixed capability.

---

## 2. Oracle — the ~$300bn commitment

### Verdict: Partly confirmed (the number is real as a reported purchase obligation; the framing "Oracle committed $300bn" is backwards)

### What exactly was committed, to whom, over what timeframe?

- **The $300bn is OpenAI's obligation to Oracle, not Oracle's spend.** The Wall Street Journal reported in September 2025 that OpenAI agreed to buy roughly **$300bn of computing power from Oracle over about five years, starting in 2027**, requiring **4.5 gigawatts** of power. OpenAI confirmed the scale on 23 Sep 2025, writing that the July 2025 partnership to develop up to 4.5 GW of additional Stargate capacity "represents a partnership that exceeds $300 billion between the two companies over the next five years" (via https://www.useluminix.com/reports/company-overviews/oracle-ai-debt-openai-contract/source/0 and https://zandigital.in/openai-compute-commitments-revenue ).
- **Oracle itself has never named OpenAI or $300bn in an SEC filing.** The only Oracle filing that sizes the economics is its **8-K of 30 June 2025**: CEO Safra Catz said Oracle had signed multiple large cloud agreements "including one that is expected to contribute **more than $30 billion in annual revenue starting in FY28**" (Oracle fiscal year beginning 1 June 2027), and warned amounts ultimately recognised "may vary". A flat $30bn/yr × 5 years = $150bn; $300bn over 5 years implies a $60bn average — i.e. the contract must ramp steeply, or the two numbers measure different things (revenue recognised vs total purchase obligation). The discrepancy is unresolved in public filings.
- **Backlog (Remaining Performance Obligations, RPO):** Oracle reported RPO of **$455bn at 31 Aug 2025, up 359% YoY** (Q1 FY2026 results, Sep 2025). Secondary tallies put RPO at $523bn (Nov 2025), $552.6bn (Feb 2026), $638bn (May 2026) and $664bn (31 Aug 2026) — these later figures were not re-verified from filings in this run. RPO is contracted revenue not yet recognised; it is not cash, and Oracle does not break it down by customer.
- **Stargate context:** Announced 21 Jan 2025 by OpenAI, SoftBank, Oracle and MGX: **$500bn intended investment over four years, $100bn to be deployed immediately**, goal 10 GW initially, later up to 30 GW. That is an *intention / joint-venture ambition*, not a signed purchase obligation and not Oracle RPO. The Abilene, Texas site is built and owned by Crusoe, furnished and operated by Oracle. Reports in 2026 that Oracle/OpenAI cancelled an Abilene expansion amid financing challenges and shifting demand forecasts are secondary only (via https://www.investwhat.in/india/market-analysis/26789/oracles-300-billion-bet-on-openai-the-hidden-risk-investors-are-missing ) — flag as reported friction, not confirmed.

### How is it financed? (Debt — yes, heavily)

- **Oracle capex:** $6.9bn in FY2024 (secondary tally) → **$21.2bn in FY2025** → guided ~$35bn for FY2026 in Sep 2025, then ~$50bn, with trailing capex reaching $55.7bn by the close of FY2026 and FY2027 guidance of $90–95bn in secondary tallies (https://btw.media/en/oracle-financing-ledger-ai-buildout ). The direction — a multi-fold, guidance-beating ramp — is consistent across sources; the latest figures are secondary.
- **Debt:** **$18.0bn six-tranche senior bond sale completed 26 Sep 2025** (Oracle 8-K, coupons 4.45% due 2030 to 6.10% due 2065); **$25.0bn eight-tranche + $500m floater priced 2 Feb 2026**; a plan announced 1 Feb 2026 to raise **$45–50bn gross in calendar 2026**, roughly half equity-linked, including a $5bn mandatory convertible preferred and a $20bn at-the-market programme. Total debt was ~**$105–111.6bn at Aug 2025**, up from $84.5bn a year earlier. Free cash flow turned negative from fiscal Q4 2025 as capex outran operating cash flow.
- **Credit reaction:** Moody's (Baa2) and S&P (BBB) moved Oracle to **negative outlook** in 2025, warning leverage could exceed 4× debt-to-EBITDA by 2027–28; Barclays downgraded Oracle debt to underweight in Nov 2025; five-year CDS spreads reached their highest since the 2008–09 crisis / ~128bp in Dec 2025 (secondary reports — direction consistent, exact level varies by source/date). Oracle shares fell ~36% from their ~$346 September 2025 peak by early December 2025.
- **Leases:** Oracle disclosed **$248bn in additional lease commitments**, substantially all data-centre/cloud, starting Q3 FY26–FY28, 15–19 year terms, not yet on the balance sheet (secondary via InvestWhat). This is the off-balance-sheet layer the IMF flags.

### Electricity / power demands and risks

- The Oracle/OpenAI deal alone needs **4.5 GW** — roughly seven large nuclear plants' output, or power for ~3.5–4 million homes on the usual rule of thumb. Stargate's ambition is up to 30 GW.
- System-wide, the **IEA, "Energy and AI", 10 Apr 2025** (https://www.iea.org/reports/energy-and-ai ): global data-centre electricity **415 TWh in 2024 → ~945 TWh by 2030**; US **~183 TWh in 2024 → ~425 TWh by 2030 (+130%)**, accounting for close to half of all US electricity demand growth. Lawrence Berkeley National Laboratory (Dec 2024) put US data centres at 176 TWh in 2023 (4.4% of US electricity), 325–580 TWh by 2028. Risks are therefore physical, not just financial: grid interconnection queues (2,285 GW in the US at end-2025, per LBNL "Queued Up 2026"), transformer lead times of 128–144 weeks, and state moratoria / delay costs. Power, not silicon, is now cited by multiple sources as the binding constraint on the next generation.

---

## 3. Circular financing

### Verdict: Confirmed as a structure; partly confirmed as a bubble mechanism

### Definition

Circular (vendor) financing = a supplier provides capital (equity, loan, guarantee, or cloud credits) to a customer, and the customer uses it to buy the supplier's product. Part of the supplier's booked revenue is its own money returning. At its worst it shades into round-tripping — swapping money to inflate revenue without real profit. The two are distinguished by whether real end-user demand ultimately pays for the capacity, which cannot be judged from deal structure alone.

### The authoritative quantification — IMF and BIS, October 2026

- **IMF, Global Financial Stability Report, Oct 2026, press briefing 13 Oct 2026** — opened live, https://www.imf.org/en/news/articles/2026/10/13/tr-101326-press-briefing-transcript-global-financial-stability-report-annual-meetings-2026 : analysis of **14 public transactions since 2023** finds **"$300 billion in equity" + "$650 billion in debt, including in off-balance sheet vehicles"** "in exchange for **$1.4 trillion of future revenue commitments**". The IMF warns of a "triple whammy" if monetisation weakens: equity values fall, debt becomes harder to service, and promised revenue may not materialise. It does *not* call the deals fraudulent, and does *not* forecast a correction.
- **BIS Bulletin No.137, "Circular relationships among AI firms", 1 Oct 2026** (via https://www.alpeshpatel.com/blog/the-1-4-trillion-circle-what-the-imf-the-bis-and-the-filings-actually-say-about-ai-s-circular-fin and https://snowshagal.com/reports/en/20261030_Snowshagal_Research_No12_AI_Circular_Financing_EN ): mapping 1,246 AI firms, 2021–2025, **55.2% of investment into AI firms came from other AI firms**, and **46.4% of AI-to-AI deal value (16.1% by count) involved an investor who was also a supplier or customer**. The BIS explicitly does *not* call these deals inherently unsound, and lists four rational reasons: suppliers may understand a customer's prospects better than outside investors; funding a customer smooths demand for capital-heavy products; customers invest in suppliers to secure scarce inputs; shared stakes protect both sides in custom-chip / custom-data-centre builds. Note: 46.4% is the share of *deal value where a commercial relationship also exists*, not proof that 46.4% of cash flowed back to suppliers.
- Bank of Korea estimate (via secondary): circular deals make up **47% of Oracle's cloud backlog and 41% of Microsoft's** — secondary, not verified from the Bank of Korea primary.

### Trace the actual deals

| Loop | Money out (investor → lab / cloud) | What comes back | Status / caveat |
|---|---|---|---|
| **NVIDIA → OpenAI** | Letter of intent 22 Sep 2025: invest **up to $100bn** progressively as 10 GW of NVIDIA systems deployed, first GW targeted H2 2026. **Never signed** — NVIDIA's own filing warned "no assurance" of a definitive agreement; WSJ reported talks "on ice" Jan 2026. Replaced Feb 2026 by **$30bn equity** in OpenAI's $110bn round (closed $122bn, 31 Mar 2026, post-money $852bn), alongside SoftBank $30bn and Amazon up to $50bn. Separately, **17 Aug 2026: NVIDIA guarantees up to $105bn** for SB Energy's PORTS-Pike campus in Pike County, Ohio, leased to OpenAI for 20 years, exclusive NVIDIA hardware; first guarantees not expected until fiscal 2029, exposure falls as OpenAI pays rent. Jensen Huang put OpenAI's plans at ~$600bn of NVIDIA compute through 2030 (secondary). | OpenAI fills capacity with NVIDIA chips; NVIDIA books chip revenue | The "$100bn NVIDIA invested in OpenAI" headline is wrong as a statement of cash spent — $30bn is the equity actually committed in the replacement round. Do not add $100bn + $30bn + $105bn together; they are successive / different instruments. Sources: https://applescoop.org/story/ai-circular-money-nvidia-openai-deals-explained ; https://aistockwire.com/blog/ai-circular-deals-nvidia-microsoft-openai-explained |
| **Microsoft → OpenAI** | Investment since $1bn in 2019; reported ~27% stake worth ~$135bn (secondary, valuation-dependent). OpenAI committed to an **extra ~$250bn of Azure** services in the renegotiated 2025–26 relationship (secondary tally in https://zandigital.in/openai-compute-commitments-revenue — total OpenAI compute contracts ~$720bn across six deals: Oracle ~$300bn, Microsoft ~$250bn, AWS ~$138bn, CoreWeave $22.4bn, Cerebras >$10bn). Microsoft's FY2026 revenue from OpenAI was reported at $24.1bn, ~7% of Microsoft's $331.8bn total (secondary). | Azure revenue; OpenAI is Microsoft's largest AI customer and also a competitor via its own products | The $250bn figure is a reported commitment, not a filed contract value. Microsoft does not segment OpenAI revenue in its 10-K. |
| **Amazon / Google → Anthropic** | Amazon: $4bn (2023–24) + further investment; Anthropic primarily on AWS (Trainium). Google: $2.3bn+. Reported: Anthropic plans **>$100bn on AWS over 10 years** (secondary). | Anthropic buys AWS/GCP compute; Claude sold via Bedrock/Vertex (Anthropic books gross, partner share as cost) | Long-standing, pre-dates the 2025 circularity debate; cloud credits + equity are normal for a startup's cloud deal, but scale is now very large. |
| **Microsoft + NVIDIA → Anthropic (Nov 2025)** | Reported: Microsoft up to **$5bn**, NVIDIA up to **$10bn** into Anthropic; Anthropic pledges **$30bn of Azure spend** on NVIDIA systems. NVIDIA separately in talks (Sep 2026, Reuters via secondary) to anchor Anthropic's IPO with up to $10bn. | Azure + NVIDIA revenue | Reported via sources familiar with the matter; not a filed definitive agreement at the time of reporting. Treat as reported, not confirmed. |
| **NVIDIA → CoreWeave** | NVIDIA shareholder since before IPO, +$2bn Jan 2026 (secondary); **Sep 2025: NVIDIA agreed to buy $6.3bn of CoreWeave's unused capacity** through Apr 2032. | CoreWeave buys NVIDIA systems; NVIDIA backstops unsold capacity | This is the clearest "supplier guarantees its own demand" example. CoreWeave CEO called NVIDIA's stake a rounding error vs its $25bn+ balance sheet — a scale argument, not a denial. |
| **OpenAI → Broadcom / AMD** | Oct 2025: OpenAI–Broadcom 10 GW custom-chip deal through 2029; OpenAI–AMD deal also announced 2025 (26 GW total planned capacity with NVIDIA/AMD/Broadcom, secondary). | Diversifies OpenAI away from NVIDIA-only; creates new supplier loops | Shows labs are *not* locked to one supplier — a point against a single-loop story. |
| **Cloud credits (older layer)** | Microsoft $1bn Azure credits to OpenAI (2019), Google/Amazon credits to startups generally | Labs spend credits on that cloud, then convert to paid contracts | Normal startup subsidy; becomes "circular" only when the credit-funded spend is counted as the cloud's growth without end-user revenue behind it. No evidence presented that credits alone drive the current numbers. |

### How much is genuinely circular vs normal vendor-customer business?

- **Scale check:** NVIDIA Data Center revenue was **$115.2bn in FY2025** (primary, above) and a reported $193.7bn in FY2026 (secondary). A $30bn equity stake in one customer, even if fully recycled into chip purchases, is material but not a majority of NVIDIA's revenue. Microsoft's reported $24.1bn OpenAI revenue is ~7% of Microsoft's total. The loops are therefore **concentrated, not economy-wide**.
- **No fraud finding:** No regulator, auditor, or filing in the sources reviewed alleges round-tripping as accounting fraud. Jensen Huang called the circular label "ridiculous"; Michael Burry and others call the risk real. Both can be describing the same disclosed deals and disagreeing about what happens if demand disappoints.
- **The honest test (from the BIS/IMF framing):** circularity matters if, and only if, the capacity cannot be paid for from real end-user cash flow when the financing stops. That is why the IMF's "triple whammy" is conditional on monetisation weakening. The best single gauge cited in secondary analysis is **lab revenue per $1 of compute** — Anthropic was reported at **$2.08 of revenue per $1 of compute in Q2 2026** (secondary, via Alpesh Patel summary) — above $1.50 and rising is presented as healthy; falling below $1 would be a warning. That figure is not independently verified here.

---

## 4. Hyperscaler data-centre capex — Microsoft, Google, Amazon (and Meta)

### Verdict: Confirmed

### Scale — verified live

**Platformonomics, "CAPEX Trends: Analysis of 2025's Record Expenditures", 25 Feb 2026** — opened live, https://platformonomics.com/2026/02/follow-the-capex-2025-retrospective/ :

| Company | 2025 capex | Change | 2025 operating cash flow | 2026 guidance capex |
|---|---|---|---|---|
| Amazon | $134.7bn | +61% | $139.5bn | $200bn |
| Google (Alphabet) | $91.5bn | +74% | $164.7bn | $180bn |
| Meta | $72.2bn | +84% | $115.8bn | $125bn |
| Microsoft | $118bn | +56% | $160.5bn | $140bn+ |
| **Four-company total** | **$416bn** | **+66% (from $251bn in 2024)** | — | **~$645bn+** |

Definitions matter: figures include PP&E plus finance-lease infrastructure for Amazon, Meta and Microsoft (Microsoft ~$29bn, ~25% of its spend, via finance lease in 2025). Amazon's total includes ~$38bn of retail (non-AWS) capex; **AWS-specific capex was $96.5bn (+81%)**, 72% of Amazon's total. Google's is the "cleanest" (no finance leases) but the most opaque by business line. All four spent a record share of revenue on capex in 2025 — Meta 44%, Microsoft 39%. Cumulative spend by the four passed $1.6tn, on pace to pass $2tn in 2026.

Other tallies disagree on totals because of those definitions: a second source (Shield Operations, Mar 2026) put the four at $260bn in 2025 using a narrower (cash-only, different fiscal years) definition — **do not mix the two totals**. The Platformonomics $416bn is the more complete (incl. leases) measure and is the one verified live here. Later 2026 guidance in other secondary sources is higher still (combined $660–690bn for the "Big Five" incl. Oracle, or $720–745bn for Amazon/Alphabet/Microsoft/Meta) — direction is consistent, exact total depends on definitions and on guidance revisions.

### How is it financed?

- **Mostly operating cash flow — so far.** In 2025 each hyperscaler's operating cash flow still covered (or nearly covered) its capex: Amazon $139.5bn vs $134.7bn, Google $164.7bn vs $91.5bn, Meta $115.8bn vs $72.2bn, Microsoft $160.5bn vs $118bn. Free cash flow (OCF − capex) has already inflected downward at Amazon and Meta, and Platformonomics notes "in 2026, all but Microsoft could be burning cash" on those guidances.
- **Debt is rising fast as the gap opens.** Secondary tallies: hyperscaler bond issuance ~$17bn in 2024 → **$109bn in 2025 → $194bn in H1 2026 alone** (via blog summary, not verified from Dealogic primary). IMF Oct 2026: hyperscalers' share of global investment-grade bond issuance rose from <1% to **10% since 2024**. Alphabet issued a 100-year bond in 2025 that was ~10× oversubscribed (Platformonomics). Meta's $27bn Louisiana Hyperion project sits in an SPV (Meta 20%, committed to pay to use, guarantees returns if the lease is not renewed; auditor disputes Meta's "no control" claim). This is the off-balance-sheet layer to watch.
- **Depreciation is the quiet lever:** hyperscalers depreciate GPUs over 4–6 years (Meta extended server life to 5.5 years in 2025, adding ~$1.00 to EPS; Amazon shortened some server lives to 5 years, +$1.4bn depreciation in 2025). Short investor Michael Burry has argued the real economic life is closer to 2–3 years, overstating profits by ~$176bn in 2026–28 (secondary, via Substack summary — an *argument*, not a filing). If true, reported margins overstate the return on this capex.

### Utilisation / return evidence so far

- **No hyperscaler publicly discloses data-centre or GPU utilisation.** That is a material gap: the central question — is capacity being used and paid for? — cannot be answered directly from filings.
- **Indirect evidence is strong on revenue, mixed on profit:**
  - **Cloud revenue, Q3 2026 (filings, 28–29 Oct 2026, via FourWeekMBA arithmetic):** AWS **$46.0bn (+39% YoY)**, Azure **$33.2bn (+48%)**, Google Cloud **$30.7bn (+103%)**; combined $109.9bn in the quarter, up $39.3bn YoY. Azure surpassed $75bn in FY2025 (+34%, first disclosure) and $100bn in the 12 months to June 2026. AWS FY2025 cloud revenue ~$128.7bn. Google Cloud FY2025 ~$59bn. These are *total* cloud revenues, not AI-only — AI is not segmented — so they prove demand for cloud, not that AI alone pays for AI capex.
  - **Backlogs:** Microsoft commercial RPO $627bn at Q3 FY2026 (+99% YoY) and $678bn at Q4 FY2026 (+43–84% depending on the measure/source — sources disagree on the exact % because of segment restatement); Oracle RPO $455bn (above). Backlogs are promises, not cash.
  - **Capacity, not demand, as the constraint:** Microsoft's earnings calls in 2024–25 repeatedly said Azure growth was capacity-constrained; its late-2024 "Big Pause" (slowing builds, abandoning gigawatts of leases) was reversed a quarter later. That pattern — pausing, then re-accelerating — is consistent with supply bottlenecks, not with empty data centres, but it is not utilisation data.
  - **Profitability of the labs (the end customers):** OpenAI booked $13.07bn revenue in 2025 against a $20.92bn operating loss (leaked audited accounts via Fortune, Jun 2026); Anthropic ~$4.5bn GAAP revenue in 2025, first positive adjusted operating profit in Q2 2026 (~$0.57bn on ~$11.5bn revenue, Bloomberg via secondary). The labs are therefore *starting* to cover compute from revenue in Anthropic's case, not yet in OpenAI's — a divergence that matters more than any single average.
- **Sequoia's gap, updated:** David Cahn, Sequoia, "AI's $600B Question", June 2024 (via https://github.com/dizzymii/ai-engineering-brain/blob/HEAD/24%20-%20Trajectory%20&%20Navigation/Deep%20Dive%20-%20Bubble%20or%20Boom.md ): Nvidia DC run-rate ×2 (rest of data-centre TCO) ×2 (50% gross margin) = ~$600bn/yr end-user revenue needed, vs <$20bn visible then. Secondary updates put the requirement at ~$840bn (end-2025) and ~$1.5tn (mid-2026) as capex outran revenue growth. Cahn himself frames it as a *timing* argument — revenue will come, capital is years ahead — not as proof of a bubble. Gartner (Oct 2026, via secondary): ~$1tn AI infra spend in 2026, +$6tn in 2027–30, but only $3.6tn attributable enterprise/consumer AI revenue, a $4.9tn gap — secondary, not verified from Gartner primary.

---

## 5. Developer impact: is the era of "free" AI and thin wrappers ending?

### Verdict: Partly confirmed — but the price story is the opposite of the simple version

### API pricing: per-token prices are falling; total bills are rising

- **Per-token list prices have collapsed at fixed capability** (Stanford, above: >280× in ~18 months for GPT-3.5-level). GPT-5 was launched at ~$1.25–1.75/million input tokens, far below GPT-4's $30–60 at launch in 2023. Competition (OpenAI vs Anthropic vs Google vs open models) constrains flagship price rises.
- **What is rising is *consumption per task* and *the bill for heavy use*.** Agentic / coding workflows consume 10–100× the tokens of a single chat turn; a $20/month subscription can represent $150–450 of compute for an intensive coding user (secondary estimates). Providers have responded not mainly by raising list prices but by: (i) **tighter limits / pay-per-token overflow** — e.g. Cursor replaced its 500-fast-requests Pro plan with a $20 credit pool pegged to API pricing on 16 June 2025, weeks after raising $900m at a $9.9bn valuation (via https://www.ghostmesh.online/ai-reports/ai-bait-and-switch-pricing.html ); (ii) **removing bundled tokens** — Anthropic removed bundled tokens from enterprise seat deals in Apr 2026, shifting to pay-per-token (The Register, via secondary); (iii) **cutting free tiers** — OpenAI eliminated free API credits in mid-2025; Google cut its Gemini free tier (up to 10,000 requests/day for Gemini 2.5 Pro) in Dec 2025 (both secondary, via GhostMesh); (iv) **higher paid tiers** — ChatGPT Pro $200/mo, Claude Max $100–200/mo, Google AI Ultra $249.99/mo. The last three are list prices widely reported; the free-tier dates are secondary and should be checked against provider pricing pages before being quoted as fact.
- **The subsidy is documented, if imprecisely:** OpenAI was reported to spend **$1.69 per $1 earned in 2025** (WSJ, Nov 2025, via secondary) and **$1.35 in 2024** (The Information, Oct 2024); Altman publicly said the company loses money on $200/mo ChatGPT Pro. Anthropic's compute share of revenue was reported to fall from 71% in Q1 2026 to 56% in Q2 2026 as it turned profitable (WSJ, 20 May 2026, via secondary). These are leaked/reported figures, not audited filings — OpenAI and Anthropic publish no audited financials as private companies (confidential S-1s were filed in June 2026 by both; public prospectuses had not been published at the time of research).

### Startup funding for wrappers: a shakeout, not a shutdown of AI funding

- **Thin wrappers are failing in large numbers.** Jasper AI: $125m Series A Oct 2022 at $1.5bn valuation; revenue ~$120m in 2023 → ~$55m in 2024 (−54%). Builder.ai: raised >$445m (incl. Microsoft's M12), filed for bankruptcy May 2025 after investigators found actual revenue ~$55m vs claimed $165m. SimpleClosure's 2025 shutdown report (via secondary) found AI wrappers had a 2.5× YoY increase in Series A shutdowns; 966 US startups closed in 2024 (+25.6%). Google's VP for global startups, Darren Mowry, said in Feb 2026 that thin wrappers are "in serious trouble": "If you're really just counting on the back-end model to do all the work… the industry doesn't have a lot of patience for that anymore" (TechCrunch via https://kyberintel.com/blog/ai-wrapper-extinction-event/ ).
- **But AI funding overall has not dried up — it has concentrated.** Total AI VC was ~$190–200bn in 2025, ~50–53% of all VC (secondary, Crunchbase/PitchBook via https://buildooor.com/research/ai-cannibalization-loop ). In Q1 2026 alone, OpenAI, Anthropic and xAI took $172bn between them — 67% of AI VC that quarter (via https://dev.to/thebitforge/bootstrapping-in-the-age-of-claude-code-how-ai-quietly-killed-the-old-startup-playbook-47do — secondary, treat as indicative). In developer tools in 2025, the largest deal took ~46% of the category's funding, the top 3 took 72%, the top 10 took 96%.
- **What survives is workflow, data, or distribution — not the model call.** Cursor: $1bn ARR in 18 months, ~$2bn by Mar 2026, $29.3bn valuation — a forked VS Code editor with codebase-aware context, multi-file editing, and switching costs, not a chatbot skin. Claude Code: $1bn run-rate by Nov 2025, $2.5bn by Feb 2026, driven by enterprise coding. Harvey (legal, proprietary workflows/data) is the other name repeatedly cited as a survivor. The lesson is not "wrappers die" but "thin wrappers die; wrappers that own workflow, state, or proprietary data can become the product".

### Hiring demand for AI skills: strong, but bifurcated

- **Demand is rising and pays a premium:** PwC Global AI Jobs Barometer 2026 (15 Jun 2026, >1bn job ads, six continents): AI specialist postings **+68.9% in 2025 vs +8.6% for the market as a whole**; wage premium for AI skills within the same occupation **62%** (56% in 2025, 25% earlier). Lightcast via Stanford AI Index 2026: US postings requiring AI skills reached **2.5% in 2025, +55% YoY**. LinkedIn Jobs on the Rise (US, two years running): **AI Engineer #1**, AI Consultant/Strategist #2; WEF Future of Jobs 2025: AI/ML specialists +82% by 2030, data scientists the fastest-growing role (+113%). Forward Deployed Engineer postings up >1,000% YoY (Lightcast via Fortune, secondary).
- **Entry-level is the exception:** Stanford Digital Economy Lab, updated Aug 2026 with ADP payroll data: employment of **22–25-year-olds in AI-exposed occupations trails the rest by 19%**; software developers aged 22–25 down ~20% from their late-2022 peak. The pattern is fewer hires, not more firings, and experienced workers are unaffected or growing. "Prompt engineer" as a standalone title is fading; the durable skills are RAG, agents, fine-tuning, evaluation, and quality control of AI output.

---

## Overall analysis: bubble forming, near popping, or neither?

**Best-supported reading: a bubble is forming in the *financing* of AI infrastructure, concentrated in leveraged and circular deals, while the *technology and its core revenue* are real and growing. That is not the same as "a bubble about to pop" — and the evidence does not yet show a pop in progress.**

For a bubble forming:
- Capex is running roughly an order of magnitude ahead of *direct* AI end-user revenue on Sequoia's arithmetic, and the gap widened as capex accelerated in 2025–26.
- Financing has shifted from cash flow toward debt, leases, SPVs, and supplier guarantees (Oracle, Meta Hyperion, NVIDIA's $105bn Ohio guarantee, CoreWeave's $6.3bn backstop). The IMF's $1.4tn of future commitments against $950bn of equity + debt is the systemic version of the same fact.
- Valuations are stretched at the top: S&P 500 ~23× forward earnings in early 2026, the most demanding since the dot-com era (Apollo, via secondary); private AI valuations (OpenAI $852bn post-money Mar 2026, reportedly raising at ~$1.4tn; Anthropic $965bn post-money May 2026, IPO reportedly targeting ~$2tn) are priced on run-rates, not audited GAAP revenue.
- Enterprise ROI is weak in the aggregate: MIT NANDA (Aug 2025) found ~95% of GenAI pilots with no measurable P&L impact (preliminary, and criticised on methodology — see below); McKinsey State of AI 2026 found only 6% of organisations attribute ≥5% of EBIT to AI. If enterprise buyers do not convert pilots to P&L, the revenue that must service the $1.4tn will not arrive on schedule.

Against a pop being imminent / inevitable:
- **Revenue is real and accelerating, not hypothetical.** Cloud revenue grew 39–103% YoY in Q3 2026; OpenAI's run-rate went $20bn → $50bn in nine months; Anthropic's went $9bn → $65bn in seven months (run-rates, not GAAP — but the direction is corroborated by quarterly revenue: Anthropic $4.8bn in Q1 2026 → $11.5bn in Q2). NVIDIA's Data Center revenue more than doubled in a year, from a profitable base.
- **The spenders can afford to be wrong for longer than the bears can stay solvent.** Microsoft, Alphabet, Amazon and Meta generated $139–165bn each in operating cash flow in 2025. A capex disappointment dents free cash flow and buybacks; it does not, on its own, bankrupt them.
- **No demand collapse is visible yet.** Capacity, not demand, was the stated constraint on Azure growth in 2024–25; inference prices falling 280× is a *demand-expanding* force (cheaper capability → more use), even as it squeezes margins.
- **The IMF's own stress test** (Oct 2026) found the banking sector as a whole resilient to a severe scenario including an AI correction. That is not a clean bill of health — it flags a tail of undercapitalised banks exposed to NBFIs — but it is not a 2008-style systemic warning.

The most likely path, on this evidence, is **uneven**: the leveraged tail (Oracle, neoclouds, the most circular deals) reprices first if lab revenue disappoints or rates rise; the profitable core absorbs a capex slowdown and continues; the technology survives and gets cheaper. That is a *correction with a fat tail*, not a single "pop" date.

### A note on the MIT 95% figure — use it carefully
The "95% of AI pilots fail" headline is a misquotation. MIT NANDA's *The GenAI Divide* (Aug 2025) reported ~95% of *reviewed enterprise GenAI pilots* showed no measurable P&L impact, based on ~300 public deployments, 52 organisation interviews and 153 leader surveys, and labelled the findings *preliminary*. A 2026 line-by-line critique (Rob Wiblin, 80,000 Hours, Feb/Apr 2026) argues the denominator was misread — roughly four in five surveyed organisations had never run a custom task-specific pilot at all — so "95% fail" overstates failure among pilots actually run. McKinsey (2026) corroborates the *direction* (only 37% report any EBIT impact, 6% report ≥5%) without supporting the exact 95%. Quote MIT as "no measurable P&L impact in ~95% of pilots reviewed, preliminary, disputed" — not as "95% of AI projects fail".

---

## Comparison with the dot-com crash of 2000

| Dimension | Dot-com (1995–2002) | AI (2022–present) | Verdict |
|---|---|---|---|
| **Peak valuation** | NASDAQ P/E ~200× at peak (Mar 2000); NASDAQ 5,048 → 1,114 by Oct 2002 (−78%, ~$5tn lost) | NASDAQ 100 ~26× forward earnings (late 2025, Bloomberg via secondary) vs >80× at dot-com peak; S&P 500 ~23× forward (early 2026); NVIDIA ~70× forward P/E, ~35× sales at 2024 peak; Cisco was 130× earnings, 30× sales in Mar 2000 | **Less extreme at index level; extreme at the top** |
| **Revenue reality** | Pets.com: $619k revenue, $147m IPO; most darlings pre-revenue, valued on "eyeballs" | NVIDIA $130.5bn revenue FY2025 (+114%), $72.9bn net income; Microsoft/ Alphabet/Amazon/Meta highly profitable; OpenAI $13.07bn booked revenue 2025; Anthropic ~$4.5bn GAAP 2025, $11.5bn in Q2 2026 alone | **Real revenue today — the single biggest difference** |
| **Who bears the debt?** | Telecoms / dot-coms themselves: WorldCom ($11bn fraud, bankruptcy 2002), Global Crossing ($25bn debt at bankruptcy); banks and bondholders took losses; retail investors in equities | Mixed: hyperscalers mostly from cash flow (so shareholders via lower FCF/buybacks); **Oracle, neoclouds and labs via debt, leases, SPVs and supplier guarantees** (the leveraged tail); private credit / NBFIs increasingly exposed (IMF Oct 2026). Retail exposure is mainly via index funds (NVIDIA ~8% of S&P 500, secondary) | **Debt is more concentrated in a leveraged tail; less in the core, more in non-banks** |
| **Infrastructure overbuild** | $500bn+ fibre/telecom overinvestment 1998–2001; fibre lay dark for years, then was lit and used for decades | $500bn+ AI data-centre/GPU capex committed 2023–25; $416bn by four hyperscalers in 2025 alone; Stargate $500bn ambition | **Similar scale and similar timing risk** |
| **Asset durability** | Fibre: decades of useful life once laid; obsolescence slow | GPUs: depreciated 4–6 years, economically obsolete in 2–3 years on the bear case; power infrastructure lasts longer | **AI assets depreciate far faster — a correction strands value sooner** |
| **Adoption speed** | US internet users 18m (1995) → 124m (2000) | ChatGPT 100m users in 2 months (fastest ever); 88% of organisations use AI in ≥1 function (McKinsey 2025–26); AI in 24.6% of US businesses' functions (Goldman, via secondary) | **Faster adoption, but monetisation lags adoption in both eras** |
| **What survived?** | Amazon fell >90% and survived; Cisco fell ~86–90% and never regained its 2000 peak; the internet won, most investors lost | Unknown — but the analogous prediction is: the *capability* survives and gets cheaper; the *leveraged builders* are the ones at risk, not the technology | **Same lesson, different losers likely** |
| **Rate / macro trigger** | Fed raised rates 6× in 1999–2000; crash coincided with tightening | Fastest rate-hike cycle in 40 years (2022–23); AI rally persisted through it; risk now is higher-for-longer yields + AI disappointment together (IMF's "triple whammy") | **AI has so far been rate-resilient; that resilience is not guaranteed** |
| **Financing pattern** | Equity issuance, IPO proceeds, VC capital | Operating cash flow + corporate debt + circular vendor financing | **Circular/vendor financing is the closest rhyme — and the IMF/BIS have now named it as such** |

**Conclusion of the comparison:** The dot-com analogy is strongest for the *telecom* layer (vendor-financed infrastructure built ahead of demand, concentrated in a few builders), not for the *stock* layer (pre-revenue story stocks). Apollo chief economist Torsten Sløk's point (via secondary) that today's top-10 S&P 500 trade at higher multiples than their 1990s counterparts, and Deutsche Bank's finding that some AI startup price-to-sales ratios exceed the ~30× reached by Microsoft/Oracle in 2000, show the valuation risk has not disappeared — it has moved to private markets and to the infrastructure layer.

---

## What would confirm or refute the bubble thesis in the next 6–12 months

### Confirm the bubble thesis (watch for 3+ of these together)
1. **Lab revenue disappoints vs run-rate:** OpenAI's / Anthropic's public S-1s (expected late 2026) show booked GAAP revenue materially below the run-rates quoted pre-IPO (e.g. OpenAI <$36bn for 2026 vs the FT-reported company expectation; Anthropic's run-rate falling back toward its $4.5bn 2025 GAAP base), or quarterly revenue growth stalls while compute commitments keep rising.
2. **Cash burn does not narrow:** OpenAI's cumulative cash burn stays on the $115bn-through-2029 path (WSJ Nov 2025) with no credible path to profitability by 2029–30; Anthropic's Q2 2026 adjusted profit proves one-off (reverts to loss in Q3–Q4).
3. **Oracle / neocloud stress:** Oracle free cash flow stays negative, RPO growth stalls or reverses, Moody's/S&P downgrade Oracle to one notch above junk or below (BBB−/Baa3), CDS spreads widen further, or a Stargate / Ohio / Abilene financing is delayed, downsized, or restructured.
4. **Hyperscaler capex outruns cloud revenue for 2+ quarters:** Capex grows faster than cloud revenue *and* free cash flow turns negative at 2+ of Amazon/Google/Meta/Microsoft, with buybacks cut and debt issuance rising — i.e. the build is no longer self-funding.
5. **NVIDIA deceleration + concentration:** NVIDIA Data Center revenue growth decelerates sharply (e.g. from triple-digit to <20% YoY) *and* customer concentration is disclosed as rising, or a major customer (OpenAI/Anthropic) delays/cancels a committed deployment.
6. **Credit spreads widen:** AI-related corporate bond spreads widen materially vs investment-grade average (they were ~115bp vs ~78bp in Sep 2026, secondary), or a neocloud / AI SPV defaults or restructures.
7. **Enterprise ROI stays flat:** McKinsey 2027 / MIT follow-up still finds <10% of organisations with ≥5% EBIT impact from AI, and S&P finds POC abandonment still rising.

### Refute the bubble thesis (watch for 3+ of these together)
1. **Audited profitability arrives:** OpenAI's S-1 shows gross margin recovering (from 33% in 2025) and operating losses narrowing as a share of revenue; Anthropic sustains positive adjusted operating profit for 2+ quarters and revenue per $1 of compute stays >$1.50 and rising.
2. **RPO converts to cash:** Oracle and Microsoft report RPO converting to recognised revenue on schedule, Oracle free cash flow turns positive, and its outlook is stabilised (not downgraded).
3. **Cloud revenue keeps outgrowing capex:** AWS/Azure/Google Cloud revenue growth stays ≥30–40% YoY while capex growth slows to <20%, restoring free cash flow.
4. **Inference economics improve:** Lab inference cost per dollar of revenue falls (e.g. Anthropic's compute share of revenue falls below 50% and stays there), driven by efficiency (DeepSeek-style, custom silicon, inference optimisation) rather than by price rises to customers.
5. **Power is delivered:** Interconnection queues shrink, 4.5 GW Oracle/OpenAI and Ohio campuses hit milestones on time, and data-centre electricity forecasts are met without a spike in power prices or moratoria.
6. **Breadth, not concentration:** AI revenue spreads beyond OpenAI/Anthropic (the reported ~70% share of AI revenue at major tech companies, via Steve Eisman, falls), and mid-size wrappers / vertical AI companies reach sustained profitability.

**Single most informative marker:** the first *audited* OpenAI and Anthropic prospectuses. Run-rates are marketing; GAAP revenue, gross margin, and cash burn in an S-1 are the first numbers that cannot be annualised from a good month.

---

## Practical implications for students and developers

*Education, not career or investment advice. The through-line from the evidence is: own the problem and the workflow, not the model call.*

1. **Learn fundamentals before wrappers.** Data structures, systems, databases, networking, statistics, and evaluation matter more, not less, when models are cheap and interchangeable. The durable skill in the hiring data is not "prompting" (fading as a title) but *putting LLMs into products reliably*: RAG, agents, fine-tuning, evaluation, observability, and cost control. PwC's 62% wage premium is for AI skills *within* an occupation — i.e. AI + a domain, not AI alone.
2. **Optimise for cost, not just capability.** Inference now dominates training cost over a model's life (OpenAI inference spend was reported at $2.3bn in 2024, ~15× GPT-4's training cost; $8.4bn in 2025, projected $14.1bn in 2026, secondary via Sacra). Learn to: choose the smallest model that passes an eval, cache, batch, use structured output, measure tokens per task, and abstract the model call so you can swap providers when prices move. A developer who can cut a bill 10× without losing quality is more valuable than one who can call the most expensive model.
3. **Solve a real-world problem; do not build a thin wrapper.** The graveyard (Jasper, Builder.ai, "chat with your PDF") is companies whose entire product was a system prompt. The survivors (Cursor, Claude Code, Harvey) own workflow state, proprietary data, integrations, or a distribution channel that the model provider cannot ship as a checkbox. Ask: "If the lab ships this natively tomorrow, what is left?" If the answer is nothing, do not build it as a business; build it as a portfolio project and move on.
4. **Expect the "free" tier to be a funnel, not a foundation.** Build on the assumption that free credits, generous limits, and $20 flat-rate plans will tighten (they already have, in the cases documented above). Design for pay-per-token from day one, put a cost ceiling and a kill-switch in every product, and never promise a customer a flat price you cannot hedge.
5. **Diversify providers and skills.** Do not tie a career or a product to a single lab, a single cloud, or a single framework. The labs are also each other's customers, competitors, and investors — that concentration is the systemic risk in Section 3. Learn open models (Llama, etc.) alongside closed APIs, and learn the *evaluation* that lets you prove one is good enough.
6. **Entry-level is harder — compensate with proof, not credentials.** The Stanford/ADP finding (22–25-year-olds in AI-exposed roles trailing by 19%) means a degree alone is a weaker signal than it was. Ship something, measure it (cost, latency, accuracy, user outcome), and be able to explain the trade-off in an interview. That is also, not coincidentally, how you demonstrate the ROI that enterprises say is missing.
7. **Watch the markers in the previous section as a student, not just as an investor.** If Oracle is downgraded, if an S-1 disappoints, or if hyperscaler capex is cut, hiring for AI roles will tighten first in the leveraged tail (neoclouds, labs, wrapper startups) and last in the profitable core (cloud, enterprise software). Keep a core skill (software, data, cloud) that is employable with or without an AI boom.

---

## Could not verify / open questions

- **No audited financials for OpenAI or Anthropic** were available at the time of research. All revenue/loss figures for them are leaked accounts, investor materials, or run-rates reported by FT/Reuters/Bloomberg/WSJ via secondary summaries. The $70bn OpenAI run-rate reported in Sep 2026 was investor arithmetic, not a company disclosure (TechCrunch, 8 Oct 2026). Anthropic's $100bn run-rate (Sep 2026, via TechTimes) and its $2tn IPO valuation are single-source / secondary and should not be quoted as fact.
- **No public GPU / data-centre utilisation figures** from any hyperscaler or neocloud. Return on capex is therefore inferred from cloud revenue and backlogs, not measured.
- **The exact $300bn Oracle/OpenAI contract terms** (price per MW, take-or-pay, termination, start date) are not in any public filing. Oracle's RPO is not broken down by customer.
- **Later 2026 figures** (Oracle RPO $638–664bn, hyperscaler 2026 capex $660–745bn, NVIDIA FY2026 Data Center $193.7bn, Gartner's $4.9tn gap) come from secondary aggregators / tallies in search results dated after the primary filings they summarise. They are directionally consistent but were not re-verified from primary filings in this run; where they are used, they are labelled secondary.
- **The video that prompted this mission was not provided** (no link, title, or transcript in the mission text), so claims are verified against the mission's written summary of the video, not against the video itself. If the video made a specific figure not covered here (e.g. a named $ amount for a named deal), it may not be addressed.
- **"Free AI ending" dates** (OpenAI free credits mid-2025, Gemini free-tier cuts Dec 2025, Anthropic bundled-token removal Apr 2026) are from low-quality secondary sources (GhostMesh, Substack). They are plausible and mutually consistent, but should be checked against the providers' current pricing pages before being cited in teaching material.

---

## Sources

*Read 7 Nov 2026 unless otherwise stated. "Verified live" = opened via browser_open in this run; "index" = found via browser_search and read in search results.*

### Primary / authoritative — verified live
- IMF, Global Financial Stability Report press briefing, 13 Oct 2026 — https://www.imf.org/en/news/articles/2026/10/13/tr-101326-press-briefing-transcript-global-financial-stability-report-annual-meetings-2026 — verified live. 14 deals, $300bn equity / $650bn debt / $1.4tn commitments; AI correction as top risk; P/E vs dot-com distinction.
- Platformonomics, "CAPEX Trends: Analysis of 2025's Record Expenditures", 25 Feb 2026 — https://platformonomics.com/2026/02/follow-the-capex-2025-retrospective/ — verified live. Four hyperscalers $416bn in 2025, company breakdowns, 2026 guidance.
- NVIDIA, Q4 & Fiscal 2025 earnings release, 26 Feb 2025 — https://nvidianews.nvidia.com/_gallery/download_pdf/67bf85d73d633281c6875f57/ — verified live. FY25 revenue $130.5bn, Data Center $115.2bn (+142%).

### Primary / authoritative — via reputable summaries (index)
- Stanford HAI, AI Index Report 2025 — via https://galileo.ai/blog/llm-model-training-cost and https://aiforsocialgood.ca/blog/the-cost-of-artificial-intelligence-analyzing-the-impact-on-businesses-consumers-and-society — training costs, 280× inference-cost fall.
- Epoch AI, Cottier et al., arXiv:2405.21015 (May 2024, rev. Feb 2025) — via the same sources — 2.4×/yr training-cost growth, >$1bn by 2027.
- IEA, "Energy and AI", 10 Apr 2025 — https://www.iea.org/reports/energy-and-ai — 415 TWh (2024) → 945 TWh (2030) global; US ~425 TWh by 2030.
- BIS Bulletin No.137, "Circular relationships among AI firms", 1 Oct 2026 — via https://www.alpeshpatel.com/blog/the-1-4-trillion-circle-what-the-imf-the-bis-and-the-filings-actually-say-about-ai-s-circular-fin and https://snowshagal.com/reports/en/20261030_Snowshagal_Research_No12_AI_Circular_Financing_EN — 55.2% / 46.4% figures.
- MIT Project NANDA, "The GenAI Divide: State of AI in Business 2025", Aug 2025 — via https://www.cloudzero.com/blog/enterprise-ai-roi/ and https://coffeecupai.com/blog/95-ai-failure-stat-one-year-later-junk/ — 95% pilots, no measurable P&L; 2026 critique.
- McKinsey, State of AI 2025 / 2026 — via secondary summaries — 88% adoption, 6% with ≥5% EBIT impact.
- PwC, Global AI Jobs Barometer 2026, 15 Jun 2026 — via https://dev.to/ilinmaks/the-ai-job-market-in-2026-who-gets-hired-what-they-earn-and-which-roles-are-fading-3fk2 — 62% wage premium.
- Sequoia Capital, David Cahn, "AI's $600B Question", Jun 2024 — via https://github.com/dizzymii/ai-engineering-brain/blob/HEAD/24%20-%20Trajectory%20&%20Navigation/Deep%20Dive%20-%20Bubble%20or%20Boom.md — $600bn revenue requirement.

### Company / deal reporting — index (secondary, with primary where noted)
- Oracle/OpenAI $300bn: https://zandigital.in/openai-compute-commitments-revenue ; https://www.useluminix.com/reports/company-overviews/oracle-ai-debt-openai-contract/source/0 ; Oracle 8-K 30 Jun 2025 (>$30bn/yr from FY28) and 26 Sep 2025 ($18bn bond) as cited therein.
- Oracle financing ledger: https://btw.media/en/oracle-financing-ledger-ai-buildout — $18bn Sep 2025, $25bn Feb 2026, $45–50bn 2026 plan, RPO $455bn → $664bn.
- NVIDIA–OpenAI / circular deals: https://applescoop.org/story/ai-circular-money-nvidia-openai-deals-explained ; https://aistockwire.com/blog/ai-circular-deals-nvidia-microsoft-openai-explained ; https://www.vantagemarkets.com/en/market-analysis/ai-financing-bubble-nvidia-openai-circular-deals-explained/
- Amodei $1bn / $10bn / $100bn clusters: https://www.datacenterdynamics.com/en/news/anthropic-ceo-ai-training-data-centers-to-be-10bn-in-2026-100bn-from-2027/
- OpenAI revenue / losses: https://explodingtopics.com/blog/openai-revenue ; https://inference-desk.vercel.app/openai-twenty-billion-gap-was-arithmetic/ (FT 8 Oct 2026, $50bn run-rate vs $70bn investor arithmetic); https://www.fool.com/investing/2026/08/27/openai-is-reportedly-targeting-an-ipo-debut-above/
- Anthropic revenue / profit: https://www.techtimes.com/articles/327747/20260919/anthropic-hits-100b-ipo-targets-november-safety-lead-says-no-alignment-plan-exists.htm ; https://firstpagesage.com/seo-blog/anthropic-profitability-analysis-statistics/ — treat run-rate / IPO figures as secondary.
- Cloud Q3 2026: https://fourweekmba.com/ai-google-cloud-added-15-6b-in-a-year-more-than-aws-or-azure/ ; https://coolpowerindex.com/investment/
- Dot-com comparison: https://www.onceuponamodel.com/DotCom_vs_AI_Bubble.html ; https://galacapital.com/en/ai-bubble-vs-dot-com-crash/ ; https://www.payaries.com/blog/is-ai-a-bubble-evidence-for-and-against ; https://aibubblefaq.com/guides/ai-bubble-vs-dot-com-bubble
- Wrappers / hiring: https://www.machinebrief.com/news/death-of-ai-wrapper-startups-wont-survive-2026 ; https://kyberintel.com/blog/ai-wrapper-extinction-event/ ; https://www.ghostmesh.online/ai-reports/ai-bait-and-switch-pricing.html ; https://buildooor.com/research/ai-cannibalization-loop
- Working notes for this mission: notes/source-imf-bis.md, notes/source-capex-nvidia.md, notes/source-training-oracle.md, notes/source-revenue-wrappers.md in this research directory.
