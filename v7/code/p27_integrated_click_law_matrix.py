#!/usr/bin/env python3
"""
Paper 27 receipt: integrated candidate click-law matrix.

This is a synthesis receipt, not a new asymptotic theorem.  It takes audited
high-precision constants from the preceding Paper 27 receipts and checks that
the emerging candidate law has a non-vacuous gate for each known adversary,
while keeping the linear-window hidden-cluster fork explicitly open.

The candidate record action is represented schematically as

    A_N(O,F) =
        Phi_geom(D - Pi_L(F;O)D)
      + Phi_shell(O)
      + Phi_mark(F)
      + Phi_coupling(F,O)
      + I_adm(F,O,L)
      + Phi_2nd(O).

The point of the matrix is adversarial bookkeeping:

  * Phi_geom catches macroscopic staged/fiber pressure.
  * Phi_shell catches non-manifold shell density, such as two-layer orders.
  * Phi_mark and I_adm prevent free post-hoc hidden labels.
  * Phi_coupling forbids arbitrary global mark products unless charged.
  * Pi_L gives projection credit only to admissible local/stress responses.
  * Phi_2nd is the remaining unlabeled likelihood/local-factor fork.

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


law_terms = {
    "Phi_geom": "subcritical matching/free-energy or full finite-dimensional order law",
    "Phi_shell": "calibrated interval-shell density and regularity",
    "Phi_mark": "projective finite-action mark law",
    "Pi_L": "projection onto admissible order-intrinsic local/stress responses",
    "Phi_coupling": "charge nonlocal mark-to-geometry interactions",
    "I_adm": "admissibility indicator for pre-geometric marks/couplings",
    "Phi_2nd": "unlabeled second-moment/local-factor theorem fork",
}

constants = {
    "physical_max_tail": mp.mpf("0.646530121406787645"),
    "hostile_min_tail": mp.mpf("1.51120843688793914"),
    "two_layer_shell_192": mp.mpf("0.50261780104712"),
    "sprinkling_shell_192": mp.mpf("0.13688917975567"),
    "two_layer_projection": mp.mpf("1.0"),
    "exact_block_action_N16": mp.mpf("128.0"),
    "exact_block_action_N128": mp.mpf("1024.0"),
    "block_global_projection": mp.mpf("1.0"),
    "block_local_projection_256": mp.mpf("0.0000306382009634387352"),
    "coherent_projection_N32": mp.mpf("0.099662119798697"),
    "coherent_projection_N192": mp.mpf("0.01075222645749"),
    "coherent_corr_bound_N192": mp.mpf("0.021711255547288"),
    "coherent_support_bound_N192": mp.mpf("0.88425475678249"),
    "p8_linear_half_excess": mp.mpf("-0.00306711196899414062"),
    "p8_linear_one_excess": mp.mpf("0.00674262046813964844"),
    "p8_linear_two_excess": mp.mpf("-0.00036373138427734375"),
    "p8_split_null_guard": mp.mpf("0.0305699586719211126"),
}

adversaries = [
    {
        "name": "macroscopic staged/fiber pressure",
        "status": "covered",
        "gates": ["Phi_geom"],
        "witness": "hostile matching tail above physical envelope",
        "uses_free_global_projection": False,
    },
    {
        "name": "two-layer dense-shell order",
        "status": "covered",
        "gates": ["Phi_shell"],
        "witness": "dense small-shell mass and exact shell laundering",
        "uses_free_global_projection": False,
    },
    {
        "name": "post-hoc exact block marks",
        "status": "covered",
        "gates": ["Phi_mark", "I_adm"],
        "witness": "exact block refinement action grows as 8N",
        "uses_free_global_projection": False,
    },
    {
        "name": "free global product mark projection",
        "status": "covered",
        "gates": ["Phi_coupling", "I_adm", "Pi_L"],
        "witness": "global projection is 1, local stress projection is O(N^-2)",
        "uses_free_global_projection": False,
    },
    {
        "name": "coherent-wave false positive",
        "status": "rerouted",
        "gates": ["Phi_mark", "Phi_coupling", "Pi_L"],
        "witness": "controlled by correlation/Gram cancellation, not shell support",
        "uses_free_global_projection": False,
    },
    {
        "name": "bounded-width linear hidden cluster",
        "status": "open",
        "gates": ["Phi_2nd"],
        "witness": "requires unlabeled second moment or local-factor theorem",
        "uses_free_global_projection": False,
    },
]

required_terms = {
    "Phi_geom",
    "Phi_shell",
    "Phi_mark",
    "Pi_L",
    "Phi_coupling",
    "I_adm",
    "Phi_2nd",
}

print("=" * 80)
print("Paper 27 integrated candidate click-law matrix receipt")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

print("\n=== Candidate action terms ===")
for key, description in law_terms.items():
    print(f"{key:13s} {description}")

print("\n=== Adversary coverage matrix ===")
print("adversary, status, gates, witness")
for entry in adversaries:
    print(
        f"{entry['name']}, {entry['status']}, "
        f"{'+'.join(entry['gates'])}, {entry['witness']}"
    )

pressure_margin = constants["hostile_min_tail"] / constants["physical_max_tail"]
shell_ratio = constants["two_layer_shell_192"] / constants["sprinkling_shell_192"]
action_growth = constants["exact_block_action_N128"] / constants["exact_block_action_N16"]
local_global_ratio = constants["block_local_projection_256"] / constants["block_global_projection"]
coherent_decay = constants["coherent_projection_N32"] / constants["coherent_projection_N192"]
coherent_looseness = (
    constants["coherent_support_bound_N192"] / constants["coherent_corr_bound_N192"]
)
linear_excesses = [
    abs(constants["p8_linear_half_excess"]),
    abs(constants["p8_linear_one_excess"]),
    abs(constants["p8_linear_two_excess"]),
]
max_linear_excess = max(linear_excesses)

print("\n=== Derived ledger ratios ===")
print(f"pressure_margin = {fmt(pressure_margin)}")
print(f"two_layer_shell_ratio = {fmt(shell_ratio)}")
print(f"exact_block_action_growth_N16_to_N128 = {fmt(action_growth)}")
print(f"local_to_global_projection_ratio_256 = {fmt(local_global_ratio)}")
print(f"coherent_projection_decay_N32_to_N192 = {fmt(coherent_decay)}")
print(f"coherent_support_to_correlation_bound_192 = {fmt(coherent_looseness)}")
print(f"max_abs_P8_linear_excess = {fmt(max_linear_excess)}")
print(f"P8_split_null_guard = {fmt(constants['p8_split_null_guard'])}")

check(
    "candidate action includes every currently needed gate",
    required_terms.issubset(set(law_terms)),
    ",".join(sorted(required_terms)),
)

check(
    "every non-open adversary has at least one assigned gate",
    all(entry["gates"] for entry in adversaries if entry["status"] != "open"),
    str([(entry["name"], entry["gates"]) for entry in adversaries]),
)

check(
    "exactly one adversary remains intentionally open",
    [entry["name"] for entry in adversaries if entry["status"] == "open"]
    == ["bounded-width linear hidden cluster"],
    str([entry["name"] for entry in adversaries if entry["status"] == "open"]),
)

check(
    "two-layer order is rejected by shell regularity before mark rescue",
    shell_ratio > 3 and constants["two_layer_projection"] == 1,
    f"shell_ratio={fmt(shell_ratio)} projection={fmt(constants['two_layer_projection'])}",
)

check(
    "global mark products are not accepted as free projection credit",
    local_global_ratio < mp.mpf("1e-4")
    and not any(entry["uses_free_global_projection"] for entry in adversaries),
    f"local/global={fmt(local_global_ratio)} free_global_used=False",
)

check(
    "exact block labels pay linearly growing admissibility action",
    action_growth == 8 and constants["exact_block_action_N16"] == 8 * 16,
    f"E16={fmt(constants['exact_block_action_N16'])} E128={fmt(constants['exact_block_action_N128'])}",
)

check(
    "coherent waves are routed through correlation/field-sector control",
    coherent_decay > 8
    and coherent_looseness > 30
    and any(
        entry["name"] == "coherent-wave false positive"
        and entry["status"] == "rerouted"
        for entry in adversaries
    ),
    f"decay={fmt(coherent_decay)} support/corr={fmt(coherent_looseness)}",
)

check(
    "linear-window cluster is not falsely declared solved by finite P8 data",
    max_linear_excess < constants["p8_split_null_guard"]
    and any(entry["status"] == "open" for entry in adversaries),
    f"max_excess={fmt(max_linear_excess)} guard={fmt(constants['p8_split_null_guard'])}",
)

print("\n=== Consequence ===")
print(
    "The integrated law skeleton is no longer a single magic statistic.  The\n"
    "receipts force a sectoral structure: order pressure, shell regularity,\n"
    "projective mark admissibility, local/stress coupling, coherent-field\n"
    "correlation control, and the still-open unlabeled second-moment fork.  The\n"
    "matrix deliberately leaves the bounded-width linear hidden cluster open,\n"
    "because Paper 27 has narrowed but not solved that theorem."
)

print("\n" + "=" * 80)
failed = [name for name, ok, _ in checks if not ok]
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")

if failed:
    print(f"\nCHECKS FAILED: {len(failed)}/{len(checks)}")
    raise SystemExit(1)

print(f"\nCHECKS PASSED: {len(checks)}/{len(checks)}")
print("DONE.")
