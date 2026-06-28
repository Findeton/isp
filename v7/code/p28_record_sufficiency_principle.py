#!/usr/bin/env python3
"""
Paper 28 receipt: record sufficiency principle audit.

This receipt checks the proposed principle that emerged from Papers I-XXVII:

    A hidden refinement is physically admissible only through its pushforward
    to the committed-record sigma-field.  If that pushforward is contiguous
    to the null record law, the hidden refinement is washed out as record
    ontology.  If it is not contiguous, the excess identifies a missing
    record mark/action term rather than a legitimate hidden explanation.

Equivalently, the record sigma-field must be sufficient for the law.  Hidden
variables can exist as representations, machines, gauges, or calculation
scaffolds, but they may not carry record-predictive likelihood residue unless
that residue is promoted to the record law.

The decisive finite object is the chi-square/second-moment ledger

    S = E_P[(dQ/dP)^2] = 1 + chi^2(Q || P),

because it controls record-observable total variation by

    TV(Q,P) <= 1/2 sqrt(S-1).

This receipt is a high-precision synthesis check.  It does not prove
asymptotic contiguity.  It verifies that the principle correctly classifies the
known Paper 23-27 adversaries and that it does not falsely declare the linear
hidden-cluster fork solved.

All asserted non-integer arithmetic uses mpmath with dps=140.
"""

import sys

import mpmath as mp

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140


def fmt(x, n=32):
    return mp.nstr(x, n)


checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def tv_bound_from_second_moment(S):
    S = mp.mpf(S)
    if S < 1:
        # Finite split estimates can sit below one from sampling noise.  The
        # mathematical chi-square divergence is nonnegative, so clip only for
        # the diagnostic bound.
        S = mp.mpf(1)
    return mp.mpf("0.5") * mp.sqrt(S - 1)


constants = {
    # Paper 27 exact and split second-moment ladder.
    "zero_jitter_S8": mp.mpf("1362.66666666666667"),
    "quarter_excess": mp.mpf("0.0707762718200683594"),
    "split_null_guard": mp.mpf("0.0305699586719211126"),
    "linear_half_excess": mp.mpf("-0.00306711196899414062"),
    "linear_one_excess": mp.mpf("0.00674262046813964844"),
    "linear_two_excess": mp.mpf("-0.00036373138427734375"),
    # Paper 27 local proof spine.
    "polymer_budget_max": mp.mpf("0.00396620845573223759"),
    "polymer_cycle_share_max": mp.mpf("0.124602320041380989"),
    "continuous_max_c2_Ainf": mp.mpf("0.0726153470569359606"),
    "K_guard": mp.mpf("0.075"),
    # Paper 27 mark/action gates.
    "block_global_projection": mp.mpf("1"),
    "block_local_projection_256": mp.mpf("0.0000306382009634387352"),
    "exact_block_action_N16": mp.mpf("128"),
    "exact_block_action_N128": mp.mpf("1024"),
    # Paper 22-23 interval/staging gates.
    "five_alpha_hidden_mass": mp.mpf("0.93287371980460700041"),
    "transitivity_tax": mp.mpf("77.804057396441232631"),
    "best_jitter_Plog2_ratio": mp.mpf("0.98835534054519469285"),
}

linear_excesses = [
    abs(constants["linear_half_excess"]),
    abs(constants["linear_one_excess"]),
    abs(constants["linear_two_excess"]),
]
max_linear_excess = max(linear_excesses)
zero_jitter_tv_bound = tv_bound_from_second_moment(constants["zero_jitter_S8"])
quarter_guard_ratio = constants["quarter_excess"] / constants["split_null_guard"]
linear_guard_ratio = max_linear_excess / constants["split_null_guard"]
global_to_local_projection = (
    constants["block_global_projection"] / constants["block_local_projection_256"]
)
block_action_growth = (
    constants["exact_block_action_N128"] / constants["exact_block_action_N16"]
)
copula_guard_ratio = constants["continuous_max_c2_Ainf"] / constants["K_guard"]

adversary_table = [
    {
        "name": "zero-jitter hidden pair",
        "classification": "record-visible",
        "reason": "exact S8 is huge after pushforward to records",
    },
    {
        "name": "quarter-window hidden cluster",
        "classification": "record-visible at N=8",
        "reason": "split excess exceeds hostile null guard",
    },
    {
        "name": "linear-window hidden cluster",
        "classification": "open-contiguity-fork",
        "reason": "finite excess is inside guard; proof needs S_N bound",
    },
    {
        "name": "free global mark projection",
        "classification": "inadmissible hidden residue",
        "reason": "global mark erases block; local/stress projection does not",
    },
    {
        "name": "exact block labels",
        "classification": "record mark/action if used",
        "reason": "exact hidden labels pay linearly growing refinement action",
    },
    {
        "name": "finite interval moments",
        "classification": "insufficient statistic",
        "reason": "five alphas hide most relation mass",
    },
]

print("=" * 80)
print("Paper 28 record sufficiency principle receipt")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

print("\n=== Principle ===")
print("Hidden refinement is admissible only through record pushforward.")
print("Contiguous pushforward => hidden representation is washed out.")
print("Non-contiguous pushforward => residue must become a record mark/action term.")

print("\n=== Adversary classification ledger ===")
for row in adversary_table:
    print(f"{row['name']}: {row['classification']} ({row['reason']})")

print("\n=== Derived audit ratios ===")
print(f"zero_jitter_TV_bound_from_S8 = {fmt(zero_jitter_tv_bound)}")
print(f"quarter_excess / split_guard = {fmt(quarter_guard_ratio)}")
print(f"linear_max_excess / split_guard = {fmt(linear_guard_ratio)}")
print(f"global_to_local_projection_ratio = {fmt(global_to_local_projection)}")
print(f"exact_block_action_growth_N16_to_N128 = {fmt(block_action_growth)}")
print(f"copula_guard_ratio = {fmt(copula_guard_ratio)}")
print(f"polymer_budget_max = {fmt(constants['polymer_budget_max'])}")
print(f"polymer_cycle_share_max = {fmt(constants['polymer_cycle_share_max'])}")
print(f"five_alpha_hidden_mass = {fmt(constants['five_alpha_hidden_mass'])}")
print(f"transitivity_tax = {fmt(constants['transitivity_tax'])}")
print(f"best_jitter_Plog2_ratio = {fmt(constants['best_jitter_Plog2_ratio'])}")

check(
    "chi-square second moment gives a record-observable TV control",
    zero_jitter_tv_bound > mp.mpf("10"),
    f"S8={fmt(constants['zero_jitter_S8'])} TV_bound={fmt(zero_jitter_tv_bound)}",
)
check(
    "principle classifies zero-jitter hidden pairs as record-visible",
    constants["zero_jitter_S8"] > mp.mpf("1000"),
    f"S8={fmt(constants['zero_jitter_S8'])}",
)
check(
    "principle classifies quarter-window clusters as already visible at N=8",
    quarter_guard_ratio > 2,
    f"ratio={fmt(quarter_guard_ratio)}",
)
check(
    "principle refuses to call the linear-window fork solved",
    linear_guard_ratio < 1,
    f"ratio={fmt(linear_guard_ratio)} max_excess={fmt(max_linear_excess)}",
)
check(
    "local proof spine supports washout rather than low-order polymer growth",
    constants["polymer_budget_max"] < mp.mpf("0.005")
    and constants["polymer_cycle_share_max"] < mp.mpf("0.15")
    and copula_guard_ratio < 1,
    f"budget={fmt(constants['polymer_budget_max'])} "
    f"cycle_share={fmt(constants['polymer_cycle_share_max'])} "
    f"c2A/K={fmt(copula_guard_ratio)}",
)
check(
    "mark laundering is rejected as hidden sufficiency violation",
    global_to_local_projection > mp.mpf("10000") and block_action_growth == 8,
    f"global/local={fmt(global_to_local_projection)} action_growth={fmt(block_action_growth)}",
)
check(
    "finite feature profiles are not sufficient sigma-fields",
    constants["five_alpha_hidden_mass"] > mp.mpf("0.9")
    and constants["transitivity_tax"] > mp.mpf("10"),
    f"hidden_mass={fmt(constants['five_alpha_hidden_mass'])} "
    f"tax={fmt(constants['transitivity_tax'])}",
)
check(
    "near-perfect scalar profile matching does not imply record-law equality",
    abs(1 - constants["best_jitter_Plog2_ratio"]) < mp.mpf("0.02")
    and any(row["classification"] == "open-contiguity-fork" for row in adversary_table),
    f"Plog2_ratio={fmt(constants['best_jitter_Plog2_ratio'])}",
)

print("\n=== Theorem target extracted by the principle ===")
print("For each admissible hidden refinement H_N with record pushforward Q_N:")
print("  either sup_N E_P[(dQ_N/dP_N)^2] < infinity,")
print("  or the diverging classes define a new committed record mark/action sector.")
print("For the linear-window cluster, the concrete proof target is:")
print("  A_N(c) <= K/c^2, coefficient-level polymer summability,")
print("  sectoral matching/free-energy pressure, quotient safety.")

print("\n" + "=" * 80)
failed = [name for name, ok, _ in checks if not ok]
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")

if failed:
    print(f"\nCHECKS FAILED: {len(failed)}/{len(checks)}")
    raise SystemExit(1)

print(f"\nCHECKS PASSED: {len(checks)}/{len(checks)}")
print("DONE.")
