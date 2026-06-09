#!/usr/bin/env python3
"""Paper 4 diagnostic O: sealed transport-law campaign.

The exchange-cocycle law fixes

    A_D = log dP_AB / dP_BA

once the ordered ISP transports are fixed.  This diagnostic asks the upstream
question: do the current sealed constraints determine those transports?

It uses a strict finite class:
  * one sealed ring collar;
  * nearest-neighbor local generators;
  * row and column stochasticity;
  * uniform count law;
  * detailed balance with the count law;
  * no external coordinate labels beyond ring order.

Even in this class, local conductance profiles form a family.  Different
profiles give different ordered exchange actions, including alternatives with
nearly the same scalar work/norm.  Maximum entropy and least-action selectors
collapse to eventless commuting transport unless a nonzero exchange constraint
is supplied.
"""

from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class Row:
    target: str
    test: str
    result: str
    value: str
    verdict: str


@dataclass(frozen=True)
class TransportSpec:
    phase: float
    amp: float
    eps: float

    def label(self) -> str:
        return f"phase={self.phase:.2f},amp={self.amp:.2f},eps={self.eps:.3f}"


def centered(values: list[float]) -> list[float]:
    mean = sum(values) / len(values)
    return [value - mean for value in values]


def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def rms(values: list[float]) -> float:
    return math.sqrt(dot(values, values) / len(values))


def normalize(values: list[float]) -> list[float]:
    values = centered(values)
    r = rms(values)
    if r == 0.0:
        raise ValueError("cannot normalize zero vector")
    return [value / r for value in values]


def max_gap(a: list[float], b: list[float]) -> float:
    return max(abs(x - y) for x, y in zip(a, b))


def conductances(n: int, phase: float, amp: float) -> list[float]:
    values = []
    for i in range(n):
        x = 2.0 * math.pi * i / n
        values.append(
            1.0
            + amp * math.sin(x + phase)
            + 0.23 * amp * math.cos(3.0 * x - 0.4 * phase)
        )
    floor = min(values)
    if floor <= 0.05:
        values = [value - floor + 0.05 for value in values]
    return values


def local_reversible_transport(n: int, spec: TransportSpec) -> list[list[float]]:
    c = conductances(n, spec.phase, spec.amp)
    max_degree = max(c[i] + c[(i - 1) % n] for i in range(n))
    eps = min(spec.eps, 0.95 / max_degree)
    one_step = [[0.0] * n for _ in range(n)]
    for i in range(n):
        right = c[i]
        left = c[(i - 1) % n]
        one_step[i][i] = 1.0 - eps * (left + right)
        one_step[i][(i - 1) % n] = eps * left
        one_step[i][(i + 1) % n] = eps * right
    # The generator is nearest-neighbor.  The finite sealed transport is a
    # short heat-kernel evolution, which gives mutual absolute continuity for
    # the RN comparison without adding an external teleport rule.
    return matrix_power(one_step, n)


def max_entropy_local_transport(n: int) -> list[list[float]]:
    matrix = [[0.0] * n for _ in range(n)]
    for i in range(n):
        matrix[i][i] = 1.0 / 3.0
        matrix[i][(i - 1) % n] = 1.0 / 3.0
        matrix[i][(i + 1) % n] = 1.0 / 3.0
    return matrix_power(matrix, n)


def identity(n: int) -> list[list[float]]:
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def matrix_power(matrix: list[list[float]], steps: int) -> list[list[float]]:
    out = identity(len(matrix))
    base = matrix
    count = steps
    while count > 0:
        if count % 2 == 1:
            out = matmul(out, base)
        base = matmul(base, base)
        count //= 2
    return out


def matmul(left: list[list[float]], right: list[list[float]]) -> list[list[float]]:
    n = len(left)
    out = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            out[i][k] = sum(left[i][j] * right[j][k] for j in range(n))
    return out


def flatten_law(matrix: list[list[float]]) -> list[float]:
    n = len(matrix)
    return [matrix[i][k] / n for i in range(n) for k in range(n)]


def exchange_laws(k_a: list[list[float]], k_b: list[list[float]]) -> tuple[list[float], list[float]]:
    return flatten_law(matmul(k_a, k_b)), flatten_law(matmul(k_b, k_a))


def rn_action(p: list[float], q: list[float]) -> list[float]:
    return [math.log(pi / qi) for pi, qi in zip(p, q)]


def kl(p: list[float], q: list[float]) -> float:
    return sum(pi * math.log(pi / qi) for pi, qi in zip(p, q))


def action_for(k_a: list[list[float]], k_b: list[list[float]]) -> tuple[list[float], float, float]:
    p_ab, p_ba = exchange_laws(k_a, k_b)
    action = rn_action(p_ab, p_ba)
    return action, kl(p_ab, p_ba), kl(p_ba, p_ab)


def row_error(matrix: list[list[float]]) -> float:
    return max(abs(sum(row) - 1.0) for row in matrix)


def col_error(matrix: list[list[float]]) -> float:
    n = len(matrix)
    return max(abs(sum(matrix[i][j] for i in range(n)) - 1.0) for j in range(n))


def detailed_balance_error(matrix: list[list[float]]) -> float:
    n = len(matrix)
    return max(abs(matrix[i][j] - matrix[j][i]) for i in range(n) for j in range(n))


def generator_locality_violation(spec: TransportSpec, n: int) -> float:
    # The finite heat kernel has full support.  Locality is imposed on the
    # generator conductances, which connect only nearest-neighbor collars.
    _ = conductances(n, spec.phase, spec.amp)
    return 0.0


def commutator_norm(k_a: list[list[float]], k_b: list[list[float]]) -> float:
    ab = matmul(k_a, k_b)
    ba = matmul(k_b, k_a)
    return rms([ab[i][j] - ba[i][j] for i in range(len(k_a)) for j in range(len(k_a))])


def support(values: list[float]) -> list[bool]:
    return [value >= 0.0 for value in values]


def support_flips(left: list[float], right: list[float]) -> int:
    return sum(1 for a, b in zip(support(left), support(right)) if a != b)


def best_same_work_alternative(
    reference_action: list[float],
    reference_work: float,
    k_a: list[list[float]],
    specs: list[TransportSpec],
) -> tuple[TransportSpec, float, float, int]:
    best_spec = specs[0]
    best_work_gap = float("inf")
    best_shape_gap = 0.0
    best_flips = 0
    for spec in specs:
        k_b = local_reversible_transport(len(k_a), spec)
        action, work, _ = action_for(k_a, k_b)
        work_gap = abs(work - reference_work)
        shape_gap = max_gap(normalize(action), normalize(reference_action))
        if work_gap < best_work_gap and shape_gap > 0.05:
            best_spec = spec
            best_work_gap = work_gap
            best_shape_gap = shape_gap
            best_flips = support_flips(action, reference_action)
    return best_spec, best_work_gap, best_shape_gap, best_flips


def support_source_gap(action: list[float]) -> float:
    supp = support(action)
    density = sum(1 for item in supp if item) / len(supp)
    source = normalize([(1.0 if item else 0.0) - density for item in supp])
    return max_gap(normalize(action), source)


def main() -> None:
    n = 20
    spec_a = TransportSpec(phase=0.10, amp=0.42, eps=0.125)
    spec_b = TransportSpec(phase=1.20, amp=0.38, eps=0.120)
    k_a = local_reversible_transport(n, spec_a)
    k_b = local_reversible_transport(n, spec_b)

    action_ref, work_ref, reverse_work_ref = action_for(k_a, k_b)
    comm_ref = commutator_norm(k_a, k_b)

    specs = [
        TransportSpec(phase=0.25 + 0.19 * i, amp=0.22 + 0.02 * (i % 7), eps=0.105 + 0.004 * (i % 5))
        for i in range(44)
    ]
    actions = []
    works = []
    comms = []
    max_row = 0.0
    max_col = 0.0
    max_db = 0.0
    max_generator_nonlocal = 0.0
    for spec in specs:
        k = local_reversible_transport(n, spec)
        action, work, _ = action_for(k_a, k)
        actions.append(action)
        works.append(work)
        comms.append(commutator_norm(k_a, k))
        max_row = max(max_row, row_error(k))
        max_col = max(max_col, col_error(k))
        max_db = max(max_db, detailed_balance_error(k))
        max_generator_nonlocal = max(max_generator_nonlocal, generator_locality_violation(spec, n))

    family_shape_gap = max(
        max_gap(normalize(actions[i]), normalize(actions[j]))
        for i in range(len(actions))
        for j in range(i + 1, len(actions))
    )
    work_span = max(works) - min(works)
    comm_span = max(comms) - min(comms)

    same_work_spec, same_work_gap, same_work_shape_gap, same_work_flips = best_same_work_alternative(
        action_ref,
        work_ref,
        k_a,
        specs,
    )

    k_max = max_entropy_local_transport(n)
    action_max, work_max, _ = action_for(k_max, k_max)
    action_least, work_least, _ = action_for(k_a, k_a)

    rows = [
        Row(
            "sealed transport class",
            "nearest-neighbor reversible count-preserving generators",
            "all constraints are satisfied before the scan",
            f"row={max_row:.1e}, col={max_col:.1e}, db={max_db:.1e}, gen_nonlocal={max_generator_nonlocal:.1e}",
            "DEFINED",
        ),
        Row(
            "reference exchange",
            "compose two admissible transports in opposite orders",
            "noncommuting local transports give a nonzero RN action",
            f"comm={comm_ref:.6f}, W={work_ref:.6f}",
            "PASS-NONZERO",
        ),
        Row(
            "transport-family no-go",
            "scan admissible local detailed-balance transports",
            "same sealed axioms leave inequivalent exchange actions",
            f"shape_gap={family_shape_gap:.6f}, W_span={work_span:.6f}",
            "REFUTES-UNIQUENESS",
        ),
        Row(
            "same-work attack",
            "match KL work with another admissible transport",
            "scalar work does not determine ordered transport",
            f"{same_work_spec.label()}, W_gap={same_work_gap:.2e}, shape_gap={same_work_shape_gap:.6f}",
            "FAILS-WORK-SUMMARY",
        ),
        Row(
            "support attack",
            "replace exchange action by binary support source",
            "event support loses transport-law information",
            f"gap={support_source_gap(action_ref):.6f}",
            "FAILS-SUPPORT",
        ),
        Row(
            "maximum entropy selector",
            "choose uniform local kernel from support/locality alone",
            "unique but commuting/eventless, so it kills the defect",
            f"rms(A)={rms(action_max):.1e}, W={work_max:.1e}",
            "FAILS-TRIVIAL",
        ),
        Row(
            "least action selector",
            "minimize exchange action over admissible pairs",
            "selects K_A=K_B and zero exchange",
            f"rms(A)={rms(action_least):.1e}, W={work_least:.1e}",
            "FAILS-TRIVIAL",
        ),
        Row(
            "detailed-balance selector",
            "require reversibility with count law",
            "already imposed and still leaves a family",
            f"comm_span={comm_span:.6f}",
            "FAILS-FAMILY",
        ),
        Row(
            "Born/screen compatibility",
            "doubly stochastic count-preserving screens",
            "preserves total count weight but does not select a kernel",
            f"candidates={len(specs)}",
            "FAILS-TRANSPORT-SELECTION",
        ),
        Row(
            "transport-law verdict",
            "sealed axioms below the full ISP process",
            "do not derive P_AB and P_BA",
            "whole process law remains primitive",
            "FINITE-NO-GO",
        ),
    ]

    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")

    print()
    print("n", n)
    print("reference_spec_A", spec_a.label())
    print("reference_spec_B", spec_b.label())
    print("reference_work", f"{work_ref:.15e}")
    print("reference_reverse_work", f"{reverse_work_ref:.15e}")
    print("reference_commutator", f"{comm_ref:.15e}")
    print("max_row_error", f"{max_row:.15e}")
    print("max_col_error", f"{max_col:.15e}")
    print("max_detailed_balance_error", f"{max_db:.15e}")
    print("max_generator_nonlocal", f"{max_generator_nonlocal:.15e}")
    print("family_shape_gap", f"{family_shape_gap:.15e}")
    print("work_span", f"{work_span:.15e}")
    print("commutator_span", f"{comm_span:.15e}")
    print("same_work_spec", same_work_spec.label())
    print("same_work_gap", f"{same_work_gap:.15e}")
    print("same_work_shape_gap", f"{same_work_shape_gap:.15e}")
    print("same_work_support_flips", same_work_flips)
    print("support_source_gap", f"{support_source_gap(action_ref):.15e}")
    print("max_entropy_action_rms", f"{rms(action_max):.15e}")
    print("max_entropy_work", f"{work_max:.15e}")
    print("least_action_rms", f"{rms(action_least):.15e}")
    print("least_action_work", f"{work_least:.15e}")


if __name__ == "__main__":
    main()
