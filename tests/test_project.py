"""Tests for the Outguessing the AI Bubble project.

Headline values are checked against the article's published Table 8
(100,000 trials, seed 20261108) with small tolerances for floating-point
and RNG-stream differences. Nothing here re-states a result from memory:
the expected values are the article's own computed outputs.
"""
import json
import math
import re
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from monte_carlo import BUCKET_PARAMS, COMPANIES, SCENARIO_PROBS, run_all
from scenarios import build_ranges, conditional_medians


def _is_prob(x):
    return isinstance(x, float) and 0.0 <= x <= 1.0


def test_scenario_probabilities_sum_to_one():
    assert abs(sum(SCENARIO_PROBS.values()) - 1.0) < 1e-12
    assert set(SCENARIO_PROBS) == {"Bear", "Base", "Bull"}


def test_determinism_same_seed_same_results():
    a, _, _ = run_all(n=20_000)
    b, _, _ = run_all(n=20_000)
    assert a == b


def test_mc1_matches_article_table8():
    res, _, _ = run_all()
    mc1 = res["MC1"]
    assert abs(mc1["median_2029"] - 1.79) < 0.01
    assert abs(mc1["p5_2029"] - 0.54) < 0.01
    assert abs(mc1["p95_2029"] - 4.05) < 0.01
    assert abs(mc1["p_lt_1_2029"] - 0.179) < 0.002
    assert abs(mc1["p_gt_1.5_2029"] - 0.619) < 0.002
    assert abs(mc1["p_lt_0.5_2029"] - 0.043) < 0.002
    medians = mc1["median_by_year"]
    assert abs(medians["2027"][0] - 1.44) < 0.01
    assert abs(medians["2028"][0] - 1.61) < 0.01


def test_mc2_matches_article_table8():
    res, _, _ = run_all()
    mc2 = res["MC2"]
    assert mc2["Amazon"]["p_fcf_negative"] > 0.99
    assert abs(mc2["Amazon"]["median_fcf_bn"] - (-51.6)) < 0.5
    assert abs(mc2["Google"]["p_fcf_negative"] - 0.588) < 0.005
    assert abs(mc2["Meta"]["p_fcf_negative"] - 0.526) < 0.005
    assert abs(mc2["Microsoft"]["p_fcf_negative"] - 0.010) < 0.005
    assert abs(mc2["Microsoft"]["median_fcf_bn"] - 33.0) < 0.5
    assert abs(mc2["joint"]["p_ge2_negative"] - 0.808) < 0.005
    assert abs(mc2["joint"]["expected_negative_count"] - 2.1) < 0.05


def test_mc3_matches_article_table8():
    res, _, _ = run_all()
    mc3 = res["MC3"]
    expected_medians = {"Leveraged tail": 102.29, "Profitable core": 105.51, "Diversified": 104.67}
    expected_p80 = {"Leveraged tail": 0.317, "Profitable core": 0.161, "Diversified": 0.003}
    for name, med in expected_medians.items():
        assert abs(mc3[name]["median_final"] - med) < 0.05
        assert abs(mc3[name]["p_below_80"] - expected_p80[name]) < 0.003
        assert _is_prob(mc3[name]["p_loss"])
        assert _is_prob(mc3[name]["p_below_80"])
        assert mc3[name]["p5_final"] < mc3[name]["median_final"] < mc3[name]["p95_final"]


def test_all_probabilities_in_unit_interval():
    res, _, _ = run_all()
    for name, v in res["MC2"].items():
        if name == "joint":
            continue
        assert _is_prob(v["p_fcf_negative"])
    assert _is_prob(res["MC2"]["joint"]["p_ge2_negative"])
    assert _is_prob(res["MC1"]["p_lt_1_2029"])
    assert _is_prob(res["MC1"]["p_gt_1.5_2029"])


def test_scenario_ranges_ordered():
    res, _, _ = run_all()
    ranges = build_ranges(res["MC3"])
    for name, r in ranges.items():
        assert r["worst_5th"] < r["base_median"] < r["best_95th"]
        assert 0.0 <= r["p_below_80"] <= 1.0


def test_conditional_medians_ordered_bear_lt_base_lt_bull():
    cond = conditional_medians(n=20_000)
    for name, scen in cond.items():
        assert scen["Bear"]["median_final"] < scen["Base"]["median_final"] < scen["Bull"]["median_final"]


def test_results_files_match_run_output():
    res, _, _ = run_all()
    saved = json.loads((PROJECT_ROOT / "results" / "monte_carlo_results.json").read_text())
    assert saved["seed"] == res["seed"]
    assert saved["MC1"]["median_2029"] == res["MC1"]["median_2029"]
    assert saved["MC3"]["Leveraged tail"]["median_final"] == res["MC3"]["Leveraged tail"]["median_final"]


def test_index_html_is_self_contained():
    html = (PROJECT_ROOT / "index.html").read_text()
    assert "outguessing" in html.lower()
    # No external resources: no CDN scripts, stylesheets, images, or fonts.
    assert not re.search(r'<script[^>]+src="https?://', html)
    assert not re.search(r'<link[^>]+href="https?://', html)
    assert not re.search(r'<img[^>]+src="https?://', html)
    assert "fonts.googleapis" not in html
    assert "not investment advice" in html.lower()
    assert "model estimate" in html.lower()
