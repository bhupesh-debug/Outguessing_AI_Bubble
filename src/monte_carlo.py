"""Monte Carlo simulations for *Outguessing the AI Bubble*.

Copied verbatim (logic unchanged) from the script that produced the article's
Figure 6 and Table 8 (~/workspace/outguess/monte_carlo_ai_bubble.py), with only
the output paths pointed at this project's own ``results/`` and ``charts/``
folders, and the simulation wrapped in :func:`run_all` so tests can import it.

All inputs come from the 7 Nov 2026 deep-research report
(``research_notes/ai-bubble-critical-analysis-20261107-2204/report.md``)
or from the article's own teaching numbers, and every input is labelled
as such in the article text. Nothing here is invented: where a distribution
is an assumption, the article says so and names the anchor.

MC-1: Lab-sector self-funding — revenue per $1 of compute, 2027-2029.
  Anchors (research, secondary, labelled): Anthropic $2.08 revenue per $1 of
  compute (Q2 2026); OpenAI ~$0.59 (spends $1.69 per $1 earned, 2025).
  R0 ~ Normal(1.30, 0.50) truncated to [0.20, 3.00]; annual growth
  g ~ Normal(0.15, 0.25) truncated to [-0.50, 1.00].
MC-2: Hyperscaler 2026 free cash flow — how many of the four burn cash?
  Inputs (research, Platformonomics verified live): 2025 OCF ($bn) Amazon
  139.5, Google 164.7, Meta 115.8, Microsoft 160.5; 2026 capex guidance
  ($bn) Amazon 200, Google 180, Meta 125, Microsoft 140 (the "+" on
  Microsoft's 140+ is noted; 140 is used as the base).
  OCF_2026 = OCF_2025 * (1 + g), g ~ Normal(0.10, 0.08); capex =
  guidance * U(0.95, 1.10).
MC-3: Scenario-weighted 12-month outcome, $100 notional, three positions.
  Scenario probabilities are working assumptions anchored on the article's
  own Bayesian teaching posterior (32% chance of a correction in the AI
  financing layer within 12 months, Tool 3): Bear 32%, Base 45%, Bull 23%.
  Scenario returns are teaching assumptions, labelled in the article; the
  Bear tail loss (-50%) is a moderate reading of the dot-com base rates
  (NASDAQ -78% peak-to-trough; Cisco -86% to -90%).

Seed fixed for reproducibility.
"""
import json
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

SEED = 20261108
N = 100_000

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUT = PROJECT_ROOT / "charts" / "fig6_montecarlo.png"
RES = PROJECT_ROOT / "results" / "monte_carlo_results.json"

# Scenario probabilities: Bear 32%, Base 45%, Bull 23% (article, Tool 3).
SCENARIO_PROBS = {"Bear": 0.32, "Base": 0.45, "Bull": 0.23}

# (bear mu, bear sd, base mu, base sd, bull mu, bull sd) in percent.
# Teaching assumptions, labelled in the article.
BUCKET_PARAMS = {
    "Leveraged tail":   ((-50, 15), (5, 10), (40, 15)),
    "Profitable core":  ((-20, 10), (8, 6), (15, 8)),
    "Diversified":      ((-8, 5), (6, 3), (9, 4)),
}

COMPANIES = {
    "Amazon":    {"ocf_2025": 139.5, "capex_2026": 200.0},
    "Google":    {"ocf_2025": 164.7, "capex_2026": 180.0},
    "Meta":      {"ocf_2025": 115.8, "capex_2026": 125.0},
    "Microsoft": {"ocf_2025": 160.5, "capex_2026": 140.0},
}


def trunc_normal(mu, sigma, lo, hi, size, rng):
    x = rng.normal(mu, sigma, size)
    return np.clip(x, lo, hi)


def run_all(seed=SEED, n=N):
    """Run MC-1, MC-2 and MC-3 and return the results dict (no file writes)."""
    rng = np.random.default_rng(seed)

    # ---------------- MC-1: revenue per $1 of compute ----------------
    r0 = trunc_normal(1.30, 0.50, 0.20, 3.00, n, rng)
    r = r0.copy()
    yearly = {"2026 (starting ratio)": (float(np.median(r0)), float(np.percentile(r0, 5)), float(np.percentile(r0, 95)))}
    for yr in (2027, 2028, 2029):
        g = trunc_normal(0.15, 0.25, -0.50, 1.00, n, rng)
        r = r * (1.0 + g)
        yearly[str(yr)] = (float(np.median(r)), float(np.percentile(r, 5)), float(np.percentile(r, 95)))
    mc1 = {
        "median_by_year": yearly,
        "p_lt_1_2029": float(np.mean(r < 1.0)),
        "p_gt_1.5_2029": float(np.mean(r > 1.5)),
        "p_lt_0.5_2029": float(np.mean(r < 0.5)),
        "median_2029": float(np.median(r)),
        "p5_2029": float(np.percentile(r, 5)),
        "p95_2029": float(np.percentile(r, 95)),
    }
    r2029 = r.copy()

    # ---------------- MC-2: hyperscaler 2026 free cash flow ----------------
    mc2 = {}
    neg_counts = np.zeros(n, dtype=int)
    for name, v in COMPANIES.items():
        g = rng.normal(0.10, 0.08, n)
        ocf = v["ocf_2025"] * (1.0 + g)
        cx = v["capex_2026"] * rng.uniform(0.95, 1.10, n)
        fcf = ocf - cx
        neg_counts += (fcf < 0).astype(int)
        mc2[name] = {
            "p_fcf_negative": float(np.mean(fcf < 0)),
            "median_fcf_bn": float(np.median(fcf)),
            "p5_fcf_bn": float(np.percentile(fcf, 5)),
            "p95_fcf_bn": float(np.percentile(fcf, 95)),
        }
    mc2["joint"] = {
        "p_ge2_negative": float(np.mean(neg_counts >= 2)),
        "p_all4_negative": float(np.mean(neg_counts == 4)),
        "p_none_negative": float(np.mean(neg_counts == 0)),
        "p_exactly1_negative": float(np.mean(neg_counts == 1)),
        "expected_negative_count": float(np.mean(neg_counts)),
    }

    # ---------------- MC-3: scenario-weighted 12-month outcome ----------------
    scen_p = np.array([SCENARIO_PROBS["Bear"], SCENARIO_PROBS["Base"], SCENARIO_PROBS["Bull"]])
    scen = rng.choice(3, size=n, p=scen_p)  # 0=Bear, 1=Base, 2=Bull
    mc3 = {}
    finals = {}
    for name, ((bmu, bsd), (amu, asd), (umu, usd)) in BUCKET_PARAMS.items():
        mu = np.where(scen == 0, bmu, np.where(scen == 1, amu, umu))
        sd = np.where(scen == 0, bsd, np.where(scen == 1, asd, usd))
        ret = np.clip(rng.normal(mu, sd, n), -95, 150) / 100.0
        final = 100.0 * (1.0 + ret)
        finals[name] = final
        mc3[name] = {
            "median_final": float(np.median(final)),
            "p5_final": float(np.percentile(final, 5)),
            "p95_final": float(np.percentile(final, 95)),
            "p_loss": float(np.mean(final < 100)),
            "p_below_80": float(np.mean(final < 80)),
            "mean_final": float(np.mean(final)),
        }

    return {"seed": seed, "trials": n, "MC1": mc1, "MC2": mc2, "MC3": mc3}, r2029, finals


def make_figure(r2029, finals):
    """Reproduce the article's Figure 6 (two panels) into charts/."""
    NAVY = "#2f5d8a"
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 3.8))
    ax = axes[0]
    ax.hist(r2029, bins=60, color=NAVY, alpha=0.85, edgecolor="white", linewidth=0.3)
    ax.axvline(1.0, color="#b00020", linewidth=1.6, label="Self-funding line (R = 1.0)")
    ax.axvline(1.5, color="#2e7d32", linewidth=1.6, linestyle="--", label="Healthy line (R = 1.5)")
    ax.axvline(np.median(r2029), color="black", linewidth=1.2, linestyle=":", label=f"Median {np.median(r2029):.2f}")
    ax.set_xlabel("Lab-sector revenue per $1 of compute, 2029")
    ax.set_ylabel("Trials")
    ax.set_title("(a) MC-1: self-funding ratio, 2029", fontsize=10)
    ax.legend(fontsize=7.5)
    ax.grid(axis="y", alpha=0.3)

    ax = axes[1]
    colors = {"Leveraged tail": "#b00020", "Profitable core": NAVY, "Diversified": "#2e7d32"}
    for name, col in colors.items():
        ax.hist(finals[name], bins=60, color=col, alpha=0.55, edgecolor="white",
                linewidth=0.3, label=name, density=True)
    ax.axvline(100, color="black", linewidth=1.4, linestyle="--", label="Starting $100")
    ax.set_xlabel("Value of $100 after 12 months ($)")
    ax.set_ylabel("Density")
    ax.set_title("(b) MC-3: scenario-weighted outcomes", fontsize=10)
    ax.legend(fontsize=7.5)
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT, dpi=200)
    plt.close(fig)
    return OUT


def main():
    results, r2029, finals = run_all()
    RES.parent.mkdir(parents=True, exist_ok=True)
    with open(RES, "w") as f:
        json.dump(results, f, indent=2)
    fig_path = make_figure(r2029, finals)
    print("Results:", RES)
    print("Figure:", fig_path)
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
