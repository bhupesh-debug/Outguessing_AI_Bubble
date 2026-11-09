"""Run the full pipeline: Monte Carlo simulations + scenario ranges."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from monte_carlo import main as mc_main
from scenarios import main as scen_main

if __name__ == "__main__":
    mc_main()
    scen_main()
    print("Pipeline complete: results/monte_carlo_results.json, results/scenario_ranges.json, charts/fig6_montecarlo.png")
