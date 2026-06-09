"""
v6 Paper 3 section 56: P_D and C_D origin campaign.

Question:
    After conditional score geometry reduces Branch A-full to deriving the
    positive record law P_D and intrinsic collar sigma-algebra C_D, can those
    be derived?

Finite answer:
    Conditionally for C_D, not from kinematics alone for P_D.

    Given a positive law P_D, an intrinsic collar can be selected when there is
    a unique exact minimal Markov blanket / separator C_D:

        I(left; right | C_D) = 0

    with a refinement-stable minimality rule.  This is a real relational
    criterion: the collar is the record carried by the diamond that screens the
    two sides in eventless transport.

    But P_D itself is not derived from support, symmetry, or the separator.
    Same support and same collar can carry different couplings.  Also C_D can
    fail to be unique, or become threshold-dependent in approximate cases.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product
from math import exp, log


Atom = tuple[int, ...]
Vector = list[float]


@dataclass(frozen=True)
class PCOriginAudit:
    target: str
    relational_test: str
    positive_result: str
    obstruction: str
    value: str
    verdict: str


def atoms(n: int) -> list[Atom]:
    return list(product((-1, 1), repeat=n))


def normalize(weights: Vector) -> Vector:
    total = sum(weights)
    return [weight / total for weight in weights]


def law_from_potential(n: int, potential) -> Vector:
    return normalize([exp(potential(atom)) for atom in atoms(n)])


def chain_law(j_left: float, j_right: float) -> Vector:
    return law_from_potential(3, lambda atom: j_left * atom[0] * atom[1] + j_right * atom[1] * atom[2])


def weak_chain_law() -> Vector:
    return chain_law(0.08, 0.08)


def marginal(law: Vector, n: int, keep: tuple[int, ...]) -> dict[tuple[int, ...], float]:
    result: dict[tuple[int, ...], float] = {}
    for atom, probability in zip(atoms(n), law):
        key = tuple(atom[i] for i in keep)
        result[key] = result.get(key, 0.0) + probability
    return result


def entropy(distribution: dict[tuple[int, ...], float]) -> float:
    return -sum(prob * log(prob) for prob in distribution.values() if prob > 0.0)


def conditional_mutual_information(
    law: Vector,
    n: int,
    left: tuple[int, ...],
    right: tuple[int, ...],
    cond: tuple[int, ...],
) -> float:
    l_c = marginal(law, n, left + cond)
    r_c = marginal(law, n, right + cond)
    c = marginal(law, n, cond)
    l_r_c = marginal(law, n, left + right + cond)
    total = 0.0
    for atom in atoms(n):
        lk = tuple(atom[i] for i in left)
        rk = tuple(atom[i] for i in right)
        ck = tuple(atom[i] for i in cond)
        lck = lk + ck
        rck = rk + ck
        lrck = lk + rk + ck
        p = l_r_c[lrck]
        total += p * log(p * c[ck] / (l_c[lck] * r_c[rck]))
    return total


def all_subsets(indices: tuple[int, ...]) -> list[tuple[int, ...]]:
    result = [()]
    for size in range(1, len(indices) + 1):
        result.extend(combinations(indices, size))
    return result


def exact_blanket_candidates(law: Vector, n: int, left: tuple[int, ...], right: tuple[int, ...], pool: tuple[int, ...]) -> list[tuple[int, ...]]:
    candidates = []
    for cond in all_subsets(pool):
        if conditional_mutual_information(law, n, left, right, cond) < 1.0e-10:
            candidates.append(cond)
    minimal = []
    for cond in candidates:
        if not any(set(other).issubset(cond) and set(other) != set(cond) for other in candidates):
            minimal.append(cond)
    return minimal


def unique_chain_blanket() -> tuple[float, float, int]:
    law = chain_law(0.7, -0.5)
    cmi_empty = conditional_mutual_information(law, 3, (0,), (2,), ())
    cmi_y = conditional_mutual_information(law, 3, (0,), (2,), (1,))
    candidates = exact_blanket_candidates(law, 3, (0,), (2,), (1,))
    return cmi_empty, cmi_y, len(candidates)


def same_collar_different_p_span() -> float:
    laws = [chain_law(0.3, 0.3), chain_law(0.9, 0.9), chain_law(0.3, 1.1)]
    return max(sum(abs(a - b) for a, b in zip(left, right)) for left in laws for right in laws)


def same_support_same_collar_blankets() -> int:
    law = chain_law(0.4, 0.9)
    return len(exact_blanket_candidates(law, 3, (0,), (2,), (1,)))


def approximate_blanket_counts() -> tuple[int, int]:
    law = weak_chain_law()
    pool = (1,)
    loose = [
        cond for cond in all_subsets(pool) if conditional_mutual_information(law, 3, (0,), (2,), cond) < 1.0e-3
    ]
    strict = [
        cond for cond in all_subsets(pool) if conditional_mutual_information(law, 3, (0,), (2,), cond) < 1.0e-8
    ]
    return len(loose), len(strict)


def graph_minimal_separators() -> tuple[int, str]:
    # Graph: L-A-C-R and L-B-C-R.  Inclusion-minimal separators between L and R
    # are {C} and {A,B}.  This shows that separator uniqueness is a theorem
    # target, not automatic.
    separators = [{"C"}, {"A", "B"}]
    return len(separators), "{C} and {A,B}"


def cofinal_frequency_errors() -> tuple[float, float]:
    law = chain_law(0.7, -0.5)
    # Deterministic rounded-count proxy for finite empirical convergence.
    errors = []
    for samples in (100, 10000):
        counts = [round(samples * p) for p in law]
        diff = samples - sum(counts)
        counts[0] += diff
        empirical = [count / samples for count in counts]
        errors.append(sum(abs(a - b) for a, b in zip(empirical, law)))
    return errors[0], errors[1]


def symmetry_not_p() -> float:
    laws = [chain_law(j, j) for j in (0.1, 0.6, 1.2)]
    return max(sum(abs(a - b) for a, b in zip(left, right)) for left in laws for right in laws)


def support_not_p() -> float:
    laws = [chain_law(0.2, -0.1), chain_law(1.0, -0.9)]
    return sum(abs(a - b) for a, b in zip(laws[0], laws[1]))


def audits() -> list[PCOriginAudit]:
    cmi_empty, cmi_y, candidate_count = unique_chain_blanket()
    loose_count, strict_count = approximate_blanket_counts()
    sep_count, sep_names = graph_minimal_separators()
    err_100, err_10000 = cofinal_frequency_errors()
    return [
        PCOriginAudit(
            "exact collar criterion",
            "I(left;right|C)=0",
            "chain middle screens sides",
            "requires exact positive P",
            f"I0={cmi_empty:.3f}, IC={cmi_y:.1e}",
            "PASS-MARKOV-BLANKET",
        ),
        PCOriginAudit(
            "unique minimal collar",
            "minimal exact separator",
            "one candidate in chain",
            "not generic",
            f"candidates={candidate_count}",
            "PASS-IN-CHAIN",
        ),
        PCOriginAudit(
            "same collar different law",
            "same Markov blanket",
            "C remains middle variable",
            "couplings remain free",
            f"P span={same_collar_different_p_span():.3f}",
            "FAIL-P-FREE",
        ),
        PCOriginAudit(
            "same support attack",
            "full positive support",
            "support unchanged",
            "law changes substantially",
            f"P span={support_not_p():.3f}",
            "FAIL-SUPPORT",
        ),
        PCOriginAudit(
            "symmetry attack",
            "left/right symmetric chain",
            "symmetry preserved",
            "coupling still free",
            f"P span={symmetry_not_p():.3f}",
            "FAIL-SYMMETRY",
        ),
        PCOriginAudit(
            "approximate collar",
            "thresholded CMI",
            "loose thresholds find candidates",
            "threshold changes answer",
            f"loose={loose_count}, strict={strict_count}",
            "FAIL-THRESHOLD",
        ),
        PCOriginAudit(
            "separator nonuniqueness",
            "graph minimal separators",
            "separators exist",
            "minimal separator need not be unique",
            f"{sep_count}: {sep_names}",
            "FAIL-C-UNIQUENESS",
        ),
        PCOriginAudit(
            "cofinal frequencies",
            "empirical record counts",
            "P can be identified from process",
            "identification is not derivation",
            f"L1 {err_100:.3f}->{err_10000:.3f}",
            "IDENT-P-NOT-DERIVE",
        ),
        PCOriginAudit(
            "P/C closure theorem",
            "actual P plus unique exact C",
            "conditional score geometry closes",
            "conditional on process law",
            "one route",
            "THM-CONDITIONAL-PC",
        ),
        PCOriginAudit(
            "origin status",
            "sealed kinematics alone",
            "cannot derive P; C can fail uniqueness",
            "needs physical process law",
            "A-full open",
            "OPEN-PROCESS-LAW",
        ),
    ]


def print_audits(rows: list[PCOriginAudit]) -> None:
    print("P_D and C_D origin campaign")
    print("---------------------------")
    print(
        "target                    relational test               positive result                  "
        "obstruction                         value                         verdict"
    )
    for row in rows:
        print(
            f"{row.target:25s} "
            f"{row.relational_test:29s} "
            f"{row.positive_result:32s} "
            f"{row.obstruction:35s} "
            f"{row.value:29s} "
            f"{row.verdict}"
        )


def main() -> None:
    print("=" * 150)
    print("v6 Paper 3 section 56: P_D and C_D origin campaign")
    print("=" * 150)
    rows = audits()
    print_audits(rows)
    print()
    print("VERDICT")
    print("-------")
    print("Given an actual positive record law P_D, a unique exact minimal Markov")
    print("blanket is a good intrinsic collar C_D when it exists.  This supplies the")
    print("collar needed by conditional score geometry.")
    print()
    print("But P_D is not derived from support, symmetry, or the separator.  The same")
    print("support and same collar admit different couplings.  Approximate collars")
    print("need thresholds, and minimal separators can be nonunique.  Cofinal record")
    print("counts can identify P_D from a process, but they do not derive the process")
    print("law.  Branch A-full therefore needs a physical process law that generates")
    print("P_D and makes C_D unique.")


if __name__ == "__main__":
    main()
