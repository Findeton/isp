"""
v6 Paper 3 section 59: P_D contradiction campaign.

Question:
    What physical impossibility forces a unique non-uniform positive sealed
    record law P_D?  Equivalently, what contradiction occurs if two different
    positive laws are allowed on the same sealed-diamond skeleton?

Finite answer:
    No contradiction follows from finite probability coherence, support,
    symmetry, Markov collars, projectivity, score geometry, detailed balance,
    or empirical distinguishability alone.  Two positive laws can be coherent,
    refinement-consistent, share the same collar, share the same low-order
    observables, and still differ.

    A contradiction appears only after adding an identity/completeness
    principle:

        the same sealed physical diamond must include the full objective
        record law P_D, not merely the same skeleton/collar/support.

    With that principle, two different P_D are not two laws for the same
    object; they are two different physical diamonds or two different branches.
    Without it, Branch A does not close.  Branch B is an admissible family of
    process laws.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import exp, log


Atom = tuple[int, ...]
Vector = list[float]


@dataclass(frozen=True)
class ContradictionAudit:
    target: str
    same_data: str
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


def bridge_law(theta: float) -> Vector:
    return law_from_potential(2, lambda atom: theta * atom[0] * atom[1])


def chain_law(left: float, right: float) -> Vector:
    return law_from_potential(3, lambda atom: left * atom[0] * atom[1] + right * atom[1] * atom[2])


def bernoulli_law(n: int, field: float) -> Vector:
    return law_from_potential(n, lambda atom: field * sum(atom))


def l1(left: Vector, right: Vector) -> float:
    return sum(abs(a - b) for a, b in zip(left, right))


def kl(left: Vector, right: Vector) -> float:
    return sum(p * log(p / q) for p, q in zip(left, right) if p > 0.0)


def marginal(law: Vector, n: int, keep: tuple[int, ...]) -> dict[tuple[int, ...], float]:
    result: dict[tuple[int, ...], float] = {}
    for atom, probability in zip(atoms(n), law):
        key = tuple(atom[i] for i in keep)
        result[key] = result.get(key, 0.0) + probability
    return result


def marginal_l1(
    left: Vector,
    right: Vector,
    n: int,
    keep: tuple[int, ...],
) -> float:
    lm = marginal(left, n, keep)
    rm = marginal(right, n, keep)
    keys = set(lm) | set(rm)
    return sum(abs(lm.get(key, 0.0) - rm.get(key, 0.0)) for key in keys)


def conditional_mutual_information(
    law: Vector,
    n: int,
    left: tuple[int, ...],
    right: tuple[int, ...],
    cond: tuple[int, ...],
) -> float:
    p_lc = marginal(law, n, left + cond)
    p_rc = marginal(law, n, right + cond)
    p_c = marginal(law, n, cond)
    p_lrc = marginal(law, n, left + right + cond)
    total = 0.0
    for atom in atoms(n):
        lk = tuple(atom[i] for i in left)
        rk = tuple(atom[i] for i in right)
        ck = tuple(atom[i] for i in cond)
        lck = lk + ck
        rck = rk + ck
        lrck = lk + rk + ck
        p = p_lrc[lrck]
        total += p * log(p * p_c[ck] / (p_lc[lck] * p_rc[rck]))
    return total


def support_same(left: Vector, right: Vector) -> bool:
    return all((p > 0.0) == (q > 0.0) for p, q in zip(left, right))


def bridge_same_marginals() -> tuple[float, float, float]:
    p = bridge_law(0.3)
    q = bridge_law(1.1)
    one_site_gap = max(marginal_l1(p, q, 2, (0,)), marginal_l1(p, q, 2, (1,)))
    return one_site_gap, l1(p, q), kl(p, q)


def chain_same_collar() -> tuple[float, float, float]:
    p = chain_law(0.4, 0.7)
    q = chain_law(1.1, 0.2)
    cmi_p = conditional_mutual_information(p, 3, (0,), (2,), (1,))
    cmi_q = conditional_mutual_information(q, 3, (0,), (2,), (1,))
    return max(abs(cmi_p), abs(cmi_q)), l1(p, q), kl(p, q)


def projective_family() -> tuple[float, float]:
    p3 = bernoulli_law(3, 0.4)
    p2 = bernoulli_law(2, 0.4)
    q3 = bernoulli_law(3, 1.2)
    q2 = bernoulli_law(2, 1.2)
    err = max(
        sum(abs(a - b) for a, b in zip(list(marginal(p3, 3, (0, 1)).values()), p2)),
        sum(abs(a - b) for a, b in zip(list(marginal(q3, 3, (0, 1)).values()), q2)),
    )
    return err, l1(p2, q2)


def detailed_balance_possible_span() -> float:
    laws = [bridge_law(theta) for theta in (0.2, 1.0)]
    return l1(laws[0], laws[1])


def downstream_span() -> tuple[float, float]:
    p = bridge_law(0.3)
    q = bridge_law(1.1)
    # Fisher information for bridge score xz is Var(xz).
    def fisher(law: Vector) -> float:
        vals = [atom[0] * atom[1] for atom in atoms(2)]
        mean = sum(prob * val for prob, val in zip(law, vals))
        return sum(prob * (val - mean) ** 2 for prob, val in zip(law, vals))

    return abs(fisher(p) - fisher(q)), abs(kl(p, [0.25] * 4) - kl(q, [0.25] * 4))


def empirical_distinguishability() -> tuple[float, float]:
    p = bridge_law(0.3)
    q = bridge_law(1.1)
    return kl(p, q), kl(q, p)


def all_events_same_implies_same() -> float:
    # If all atomic probabilities agree, the law is equal.  This is a
    # tautology showing that full P_D is complete, not a derivation of P_D.
    p = bridge_law(0.7)
    q = p[:]
    return l1(p, q)


def simultaneous_law_contradiction() -> float:
    # If one asserts P(A)=p and P(A)=q for the same event A in the same law,
    # contradiction is just |p-q|.  This requires the identity principle that
    # both claims refer to the same objective law.
    p = bridge_law(0.3)[0]
    q = bridge_law(1.1)[0]
    return abs(p - q)


def audits() -> list[ContradictionAudit]:
    one_site_gap, bridge_span, bridge_kl = bridge_same_marginals()
    collar_gap, chain_span, chain_kl = chain_same_collar()
    projective_err, projective_span = projective_family()
    fisher_span, entropy_span = downstream_span()
    kl_pq, kl_qp = empirical_distinguishability()
    return [
        ContradictionAudit(
            "probability coherence",
            "same finite atom set",
            "both laws normalized and positive",
            "coherence permits alternatives",
            f"support same={support_same(bridge_law(0.3), bridge_law(1.1))}",
            "NO-CONTRADICTION",
        ),
        ContradictionAudit(
            "same low-order records",
            "same one-site marginals",
            "local receipts agree",
            "joint bridge differs",
            f"marg gap={one_site_gap:.1e}, P span={bridge_span:.3f}",
            "FAIL-LOW-ORDER",
        ),
        ContradictionAudit(
            "same exact collar",
            "same Markov blanket C",
            "I(L;R|C)=0 for both",
            "couplings differ",
            f"CMI={collar_gap:.1e}, P span={chain_span:.3f}",
            "FAIL-COLLAR",
        ),
        ContradictionAudit(
            "same projective rule form",
            "Bernoulli field family",
            "refinement exact for both",
            "field parameter differs",
            f"proj err={projective_err:.1e}, span={projective_span:.3f}",
            "FAIL-PROJECTIVE",
        ),
        ContradictionAudit(
            "detailed balance",
            "reversible transport possible",
            "both can be stationary laws",
            "rates/action differ",
            f"P span={detailed_balance_possible_span():.3f}",
            "FAIL-DB",
        ),
        ContradictionAudit(
            "downstream machinery",
            "same skeleton, different P",
            "score/Fisher/RN all computable",
            "outputs differ, no contradiction",
            f"Fisher gap={fisher_span:.3f}, RN gap={entropy_span:.3f}",
            "PREDICTIVE-FORK",
        ),
        ContradictionAudit(
            "empirical records",
            "cofinal sampling",
            "laws distinguishable in limit",
            "distinguishable is not impossible",
            f"KL={kl_pq:.3f}/{kl_qp:.3f}",
            "EMPIRICAL-FORK",
        ),
        ContradictionAudit(
            "complete probabilities",
            "all atomic probabilities same",
            "then laws identical",
            "tautological completeness",
            f"L1={all_events_same_implies_same():.1e}",
            "PASS-TAUTOLOGY",
        ),
        ContradictionAudit(
            "simultaneous assignment",
            "same event same objective law",
            "P(A)=p and P(A)=q conflicts",
            "requires law-identity axiom",
            f"|p-q|={simultaneous_law_contradiction():.3f}",
            "PASS-IF-P-IDENTITY",
        ),
        ContradictionAudit(
            "Leibniz record identity",
            "same physical diamond includes P_D",
            "two P_D become two objects",
            "identity principle is added",
            "not kinematic theorem",
            "COND-IDENTITY-AXIOM",
        ),
        ContradictionAudit(
            "contradiction no-go",
            "same skeleton without P_D",
            "families remain admissible",
            "no impossibility found",
            f"KL example={bridge_kl:.3f}/{chain_kl:.3f}",
            "THM-NO-CONTRADICTION",
        ),
    ]


def print_audits(rows: list[ContradictionAudit]) -> None:
    print("P_D contradiction campaign")
    print("--------------------------")
    print(
        "target                    same data                         positive result                  "
        "obstruction                         value                         verdict"
    )
    for row in rows:
        print(
            f"{row.target:25s} "
            f"{row.same_data:33s} "
            f"{row.positive_result:32s} "
            f"{row.obstruction:35s} "
            f"{row.value:29s} "
            f"{row.verdict}"
        )


def main() -> None:
    print("=" * 150)
    print("v6 Paper 3 section 59: P_D contradiction campaign")
    print("=" * 150)
    rows = audits()
    print_audits(rows)
    print()
    print("VERDICT")
    print("-------")
    print("No finite contradiction was found from allowing two different positive")
    print("laws on the same sealed skeleton.  They can be coherent, positive,")
    print("projective, symmetric, detailed-balanced, and share the same collar.")
    print("They become empirically distinguishable and give different downstream")
    print("score/action/source receipts, but that is a predictive fork, not a")
    print("logical impossibility.")
    print()
    print("A contradiction appears only if one adds the identity principle that the")
    print("same sealed physical diamond includes the full objective law P_D.  Then")
    print("two different laws are not two laws for one object; they are two different")
    print("physical objects or two branch-B parameter choices.  This is a possible")
    print("Branch-A axiom, not a theorem from sealed kinematics.")


if __name__ == "__main__":
    main()
