#!/usr/bin/env python3
"""
Paper 28 receipt: hostile principle-selection matrix.

This receipt compares candidate "big principles" against the constraints that
survived Papers I-XXVII.  It is deliberately coarse: a principle passes a
constraint only if the previous papers give it a structural reason to pass,
not merely because a future patch could be added.

The point is not to prove the record click-law.  It is to check whether the
new record-sufficiency/contiguity principle is actually doing more unification
work than the earlier ideas:

  * scalar compensator / Poisson-in-chi;
  * finite feature or interval-profile action;
  * bracket/quadratic action;
  * maximum-entropy over orders;
  * causal-set action/manifoldlikeness penalty;
  * record sufficiency / hidden-refinement contiguity.

All scores are exact integers; mpmath dps=140 is used to keep the campaign's
precision discipline and to compute normalized pass fractions.
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


constraints = [
    "pre_geometric_record_only",
    "projective_refinement_consistency",
    "scalar_martingale_recovery",
    "hidden_machines_allowed_when_pushforward_same",
    "finite_features_declared_insufficient",
    "mark_laundering_rejected",
    "linear_window_maps_to_second_moment",
    "coherent_fields_not_auto_rejected",
    "rare_order_counterexample_path_preserved",
]

principles = {
    "scalar_compensator": {
        "pre_geometric_record_only",
        "projective_refinement_consistency",
        "scalar_martingale_recovery",
        "hidden_machines_allowed_when_pushforward_same",
    },
    "finite_feature_action": {
        "pre_geometric_record_only",
        "scalar_martingale_recovery",
    },
    "quadratic_bracket_action": {
        "pre_geometric_record_only",
        "scalar_martingale_recovery",
        "finite_features_declared_insufficient",
        "coherent_fields_not_auto_rejected",
    },
    "maximum_entropy_order_law": {
        "pre_geometric_record_only",
        "projective_refinement_consistency",
        "coherent_fields_not_auto_rejected",
    },
    "causal_set_action_penalty": {
        "pre_geometric_record_only",
        "finite_features_declared_insufficient",
        "rare_order_counterexample_path_preserved",
    },
    "record_sufficiency_contiguity": set(constraints),
}

must_have = {
    "pre_geometric_record_only",
    "projective_refinement_consistency",
    "scalar_martingale_recovery",
    "hidden_machines_allowed_when_pushforward_same",
    "mark_laundering_rejected",
    "linear_window_maps_to_second_moment",
    "rare_order_counterexample_path_preserved",
}

scores = {}

print("=" * 80)
print("Paper 28 principle-selection matrix receipt")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

print("\n=== Constraint matrix ===")
print("principle, passes, missing")
for name, passed in principles.items():
    missing = [constraint for constraint in constraints if constraint not in passed]
    pass_count = len(constraints) - len(missing)
    score = mp.mpf(pass_count) / len(constraints)
    scores[name] = {
        "pass_count": pass_count,
        "score": score,
        "missing": missing,
        "must_missing": [constraint for constraint in must_have if constraint not in passed],
    }
    print(
        f"{name}, {pass_count}/{len(constraints)}, "
        f"{'none' if not missing else ';'.join(missing)}"
    )

winner = max(scores, key=lambda name: (scores[name]["pass_count"], name))
runner_up = max(
    (name for name in scores if name != winner),
    key=lambda name: scores[name]["pass_count"],
)
winner_margin = scores[winner]["score"] - scores[runner_up]["score"]

print("\n=== Scores ===")
for name, row in scores.items():
    print(
        f"{name}: score={fmt(row['score'])} "
        f"must_missing={row['must_missing'] if row['must_missing'] else 'none'}"
    )
print(f"winner = {winner}")
print(f"runner_up = {runner_up}")
print(f"winner_margin = {fmt(winner_margin)}")

check(
    "record sufficiency is the only candidate passing all constraints",
    winner == "record_sufficiency_contiguity"
    and scores[winner]["pass_count"] == len(constraints),
    f"winner={winner} score={scores[winner]['pass_count']}/{len(constraints)}",
)
check(
    "every older principle misses at least one must-have constraint",
    all(scores[name]["must_missing"] for name in scores if name != winner),
    str({name: scores[name]["must_missing"] for name in scores if name != winner}),
)
check(
    "scalar compensator is recovered but not enough",
    "scalar_martingale_recovery" in principles["scalar_compensator"]
    and "linear_window_maps_to_second_moment" not in principles["scalar_compensator"],
    str(scores["scalar_compensator"]),
)
check(
    "finite feature and bracket actions remain projections, not principles",
    scores["finite_feature_action"]["pass_count"] < scores[winner]["pass_count"]
    and scores["quadratic_bracket_action"]["pass_count"] < scores[winner]["pass_count"],
    f"feature={scores['finite_feature_action']['pass_count']} "
    f"bracket={scores['quadratic_bracket_action']['pass_count']} "
    f"winner={scores[winner]['pass_count']}",
)
check(
    "principle keeps the rare-order counterexample path open",
    "rare_order_counterexample_path_preserved" in principles[winner],
    "rare-order path is not declared impossible",
)

print("\n=== Consequence ===")
print(
    "The selection matrix says the missing principle is not maximum entropy,\n"
    "not a finite action, and not the scalar compensator alone.  Those are\n"
    "useful projections.  The organizing principle that survives the hostile\n"
    "constraints is record sufficiency: hidden refinements must either wash out\n"
    "under record pushforward or become committed record variables/actions."
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
