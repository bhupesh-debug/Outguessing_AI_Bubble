"""Scenario ranges for *Outguessing the AI Bubble*.

Builds the base / best / worst 12-month ranges for each of the three
positions, from the Monte Carlo outputs and from the article's own scenario
returns. Definitions, stated in SCENARIOS.md and in the simulator:

- **Worst** = 5th percentile of the scenario-weighted $100 outcome (MC-3).
- **Base**  = median of the scenario-weighted $100 outcome (MC-3).
- **Best**  = 95th percentile of the scenario-weighted $100 outcome (MC-3).

Scenario-conditional medians are computed by re-running the MC-3 return
draws with the scenario fixed (Bear / Base / Bull), using a separate
deterministic RNG stream (seed + 1) so the headline results are untouched.

Scenario returns are the article's TEACHING ASSUMPTIONS (labelled as such in
the article): the Bear tail loss (-50%) is a moderate reading of the dot-com
base rates (NASDAQ -78% peak-to-trough; Cisco -86% to -90%).
"""
import json
from pathlib import Path

import numpy as np

from monte_carlo import BUCKET_PARAMS, SCENARIO_PROBS, SEED

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RES = PROJECT_ROOT / "results" / "scenario_ranges.json"

N = 100_000

# Article Table 7 scenario returns (teaching assumptions), in percent.
# (bear mu, bear sd, base mu, base sd, bull mu, bull sd) — same as BUCKET_PARAMS.
SCENARIO_RETURNS = {
    name: {"Bear": (p[0][0], p[0][1]), "Base": (p[1][0], p[1][1]), "Bull": (p[2][0], p[2][1])}
    for name, p in BUCKET_PARAMS.items()
}


def conditional_medians(n=N, seed=SEED + 1):
    """Median $100 outcome per bucket under each scenario held fixed."""
    rng = np.random.default_rng(seed)
    out = {}
    for name, ((bmu, bsd), (amu, asd), (umu, usd)) in BUCKET_PARAMS.items():
        out[name] = {}
        for scen, (mu, sd) in zip(("Bear", "Base", "Bull"), ((bmu, bsd), (amu, asd), (umu, usd))):
            ret = np.clip(rng.normal(mu, sd, n), -95, 150) / 100.0
            final = 100.0 * (1.0 + ret)
            out[name][scen] = {
                "median_final": float(np.median(final)),
                "p5_final": float(np.percentile(final, 5)),
                "p95_final": float(np.percentile(final, 95)),
            }
    return out


def build_ranges(mc3):
    """Worst / Base / Best ranges from the scenario-weighted MC-3 outputs."""
    ranges = {}
    for name, v in mc3.items():
        ranges[name] = {
            "worst_5th": round(v["p5_final"], 2),
            "base_median": round(v["median_final"], 2),
            "best_95th": round(v["p95_final"], 2),
            "p_loss": round(v["p_loss"], 4),
            "p_below_80": round(v["p_below_80"], 4),
            "mean_final": round(v["mean_final"], 2),
        }
    return ranges


def main():
    mc_path = PROJECT_ROOT / "results" / "monte_carlo_results.json"
    with open(mc_path) as f:
        mc = json.load(f)
    ranges = build_ranges(mc["MC3"])
    cond = conditional_medians()
    payload = {
        "seed": SEED,
        "trials": N,
        "scenario_probabilities": SCENARIO_PROBS,
        "scenario_returns_percent": {
            name: {s: {"mean": m, "sd": sd} for s, (m, sd) in rets.items()}
            for name, rets in SCENARIO_RETURNS.items()
        },
        "ranges_scenario_weighted": ranges,
        "conditional_medians_by_scenario": cond,
    }
    RES.parent.mkdir(parents=True, exist_ok=True)
    with open(RES, "w") as f:
        json.dump(payload, f, indent=2)
    print("Scenario ranges:", RES)
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
