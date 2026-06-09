"""
v6 Paper 3 section 60: unique process-law no-go.

Question:
    Can the current sealed-diamond ontology derive a unique nontrivial
    generative rule D -> P_D?  If not, can we prove that it cannot?

Answer:
    It cannot, from the current ontology.

    The proof is finite and structural.  The current ontology supplies
    skeletons, covariance/isomorphism, positivity, refinement/projectivity
    targets, collar/score reconstruction downstream, and no-silent-seam
    consistency.  It does not supply a numerical selector for a nontrivial
    process law.

    Counterexample:
        For every finite n and every theta in (0,1), define the exchangeable
        hidden-record law

            P_theta(x_1,...,x_n)
              = 1/2 prod_i (1 + theta x_i)/2
              + 1/2 prod_i (1 - theta x_i)/2.

        This is positive, permutation-invariant, projective under deleting
        records, nontrivially correlated for theta != 0, and gives coherent
        downstream score/RN/Fisher data.  Different theta values give different
        laws with the same structural sealed-diamond data.

    Therefore the current ontology cannot derive a unique nontrivial P_D.  A
    unique P_D requires an additional generative process law or numerical
    selector.  That is not a conditional answer; it is a no-go theorem for the
    current ontology.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import log


Atom = tuple[int, ...]
Vector = list[float]


@dataclass(frozen=True)
class UniqueLawAudit:
    target: str
    test: str
    result: str
    obstruction: str
    value: str
    verdict: str


def atoms(n: int) -> list[Atom]:
    return list(product((-1, 1), repeat=n))


def normalize(weights: Vector) -> Vector:
    total = sum(weights)
    return [weight / total for weight in weights]


def hidden_exchangeable_law(n: int, theta: float) -> Vector:
    law = []
    for atom in atoms(n):
        plus = 1.0
        minus = 1.0
        for spin in atom:
            plus *= (1.0 + theta * spin) / 2.0
            minus *= (1.0 - theta * spin) / 2.0
        law.append(0.5 * plus + 0.5 * minus)
    return law


def uniform(n: int) -> Vector:
    return [1.0 / (2**n)] * (2**n)


def l1(left: Vector, right: Vector) -> float:
    return sum(abs(a - b) for a, b in zip(left, right))


def kl(left: Vector, right: Vector) -> float:
    return sum(p * log(p / q) for p, q in zip(left, right) if p > 0.0)


def marginal(law: Vector, n: int, keep: tuple[int, ...]) -> Vector:
    kept_atoms = atoms(len(keep))
    index = {atom: i for i, atom in enumerate(kept_atoms)}
    result = [0.0 for _ in kept_atoms]
    for atom, probability in zip(atoms(n), law):
        result[index[tuple(atom[i] for i in keep)]] += probability
    return result


def projective_error(theta: float) -> float:
    law4 = hidden_exchangeable_law(4, theta)
    law3 = hidden_exchangeable_law(3, theta)
    return l1(marginal(law4, 4, (0, 1, 2)), law3)


def permutation_invariance_error(n: int, theta: float) -> float:
    law = hidden_exchangeable_law(n, theta)
    index = {atom: i for i, atom in enumerate(atoms(n))}
    max_gap = 0.0
    for atom in atoms(n):
        reversed_atom = tuple(reversed(atom))
        max_gap = max(max_gap, abs(law[index[atom]] - law[index[reversed_atom]]))
    return max_gap


def pair_corr(n: int, theta: float) -> float:
    law = hidden_exchangeable_law(n, theta)
    return sum(prob * atom[0] * atom[1] for prob, atom in zip(law, atoms(n)))


def one_site_mean(n: int, theta: float) -> float:
    law = hidden_exchangeable_law(n, theta)
    return sum(prob * atom[0] for prob, atom in zip(law, atoms(n)))


def family_span() -> float:
    laws = [hidden_exchangeable_law(4, theta) for theta in (0.2, 0.6, 0.9)]
    return max(l1(left, right) for left in laws for right in laws)


def positivity_min(theta: float) -> float:
    return min(hidden_exchangeable_law(5, theta))


def nontrivial_mutual_information(theta: float) -> float:
    law = hidden_exchangeable_law(2, theta)
    px = marginal(law, 2, (0,))
    pz = marginal(law, 2, (1,))
    total = 0.0
    for atom, probability in zip(atoms(2), law):
        ix = atoms(1).index((atom[0],))
        iz = atoms(1).index((atom[1],))
        total += probability * log(probability / (px[ix] * pz[iz]))
    return total


def mixture_law(n: int, theta: float, lam: float) -> Vector:
    p = hidden_exchangeable_law(n, theta)
    u = uniform(n)
    return [(1.0 - lam) * a + lam * b for a, b in zip(p, u)]


def mixture_projective_error(theta: float, lam: float) -> float:
    p4 = mixture_law(4, theta, lam)
    p3 = mixture_law(3, theta, lam)
    return l1(marginal(p4, 4, (0, 1, 2)), p3)


def mixture_span() -> float:
    laws = [mixture_law(4, 0.8, lam) for lam in (0.0, 0.4, 0.8)]
    return max(l1(left, right) for left in laws for right in laws)


def orbit_simplex_dimension(orbit_count: int) -> int:
    return orbit_count - 1


def same_receipts_span() -> tuple[float, float, float]:
    p = hidden_exchangeable_law(4, 0.3)
    q = hidden_exchangeable_law(4, 0.8)
    one_gap = max(
        l1(marginal(p, 4, (i,)), marginal(q, 4, (i,)))
        for i in range(4)
    )
    proj_gap = max(projective_error(0.3), projective_error(0.8))
    return one_gap, proj_gap, l1(p, q)


def empirical_distinguishability() -> tuple[float, float]:
    p = hidden_exchangeable_law(4, 0.3)
    q = hidden_exchangeable_law(4, 0.8)
    return kl(p, q), kl(q, p)


def audits() -> list[UniqueLawAudit]:
    one_gap, proj_gap, receipt_span = same_receipts_span()
    kl_pq, kl_qp = empirical_distinguishability()
    return [
        UniqueLawAudit(
            "explicit law family",
            "exchangeable hidden-record P_theta",
            "positive laws for all theta in (0,1)",
            "theta not selected",
            f"span={family_span():.3f}",
            "FAMILY",
        ),
        UniqueLawAudit(
            "covariance",
            "permutation invariance",
            "all P_theta invariant",
            "covariance does not fix theta",
            f"err={permutation_invariance_error(5,0.7):.1e}",
            "FAIL-UNIQUENESS",
        ),
        UniqueLawAudit(
            "projectivity",
            "delete one record",
            "marginals match smaller diamonds",
            "projectivity does not fix theta",
            f"err={projective_error(0.7):.1e}",
            "FAIL-UNIQUENESS",
        ),
        UniqueLawAudit(
            "positivity",
            "full support",
            "RN action finite",
            "positive interval remains",
            f"min P={positivity_min(0.9):.3e}",
            "FAIL-UNIQUENESS",
        ),
        UniqueLawAudit(
            "nontriviality",
            "pair modular dependence",
            "MI positive for theta != 0",
            "defect amplitude theta^2 free",
            f"MI={nontrivial_mutual_information(0.7):.3f}",
            "FAIL-UNIQUENESS",
        ),
        UniqueLawAudit(
            "same local receipts",
            "one-site means and projectivity",
            "receipts agree",
            "joint law differs",
            f"one gap={one_gap:.1e}, proj={proj_gap:.1e}, span={receipt_span:.3f}",
            "FAIL-RECEIPTS",
        ),
        UniqueLawAudit(
            "convex closure",
            "mix P_theta with uniform law",
            "positive/projective family persists",
            "continuum from any nontrivial law",
            f"proj={mixture_projective_error(0.8,0.4):.1e}, span={mixture_span():.3f}",
            "THM-MIXING-NO-GO",
        ),
        UniqueLawAudit(
            "orbit simplex",
            "laws constant on automorphism orbits",
            "dimension is orbit_count-1",
            "nontransitive skeletons give families",
            f"dim={orbit_simplex_dimension(3)} for 3 orbits",
            "THM-ORBIT-NO-GO",
        ),
        UniqueLawAudit(
            "uniform rule",
            "theta=0",
            "unique if maximal symmetry imposed",
            "eventless/trivial",
            f"corr={pair_corr(4,0.0):.1e}",
            "FAIL-TRIVIAL",
        ),
        UniqueLawAudit(
            "empirical fork",
            "cofinal records",
            "theta values distinguishable",
            "distinguishable is not impossible",
            f"KL={kl_pq:.3f}/{kl_qp:.3f}",
            "PREDICTIVE-FORK",
        ),
        UniqueLawAudit(
            "current ontology verdict",
            "sealed skeleton + structural axioms",
            "admits nontrivial law families",
            "no unique nontrivial derivation possible",
            "proved by family",
            "THM-UNIQUE-P-LAW-IMPOSSIBLE",
        ),
    ]


def print_audits(rows: list[UniqueLawAudit]) -> None:
    print("unique process-law no-go campaign")
    print("---------------------------------")
    print(
        "target                    test                                      result                          "
        "obstruction                         value                         verdict"
    )
    for row in rows:
        print(
            f"{row.target:25s} "
            f"{row.test:41s} "
            f"{row.result:31s} "
            f"{row.obstruction:35s} "
            f"{row.value:29s} "
            f"{row.verdict}"
        )


def main() -> None:
    print("=" * 150)
    print("v6 Paper 3 section 60: unique nontrivial process-law no-go")
    print("=" * 150)
    rows = audits()
    print_audits(rows)
    print()
    print("VERDICT")
    print("-------")
    print("A unique nontrivial generative rule D -> P_D cannot be derived from the")
    print("current sealed-diamond ontology.  The exchangeable hidden-record family")
    print("P_theta is positive, covariant, projective, and nontrivial for a continuum")
    print("of theta values.  Mixing any nontrivial admitted law with the uniform law")
    print("also preserves the structural clauses while producing a continuum.")
    print()
    print("Therefore the only unique law forced by pure symmetry is the uniform")
    print("eventless law.  Any unique nontrivial P_D requires an additional")
    print("generative process law or numerical selector.  In the current ontology,")
    print("Branch A-full is impossible; the honest status is Branch B or a new axiom.")


if __name__ == "__main__":
    main()
