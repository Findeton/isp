"""
v6 Paper 3 section 58: process-law boundary campaign.

Question:
    If invariant optimization principles do not fix P_D, what would count as a
    genuine physical process law rather than branch-B parameter selection?

Finite answer:
    A principle fixes P_D only when it is a generative rule for all finite
    sealed diamonds, with projective/refinement consistency, positivity,
    nontrivial defects, unique collars, and no free coefficients.  This is a
    legitimate Branch-A theorem target.  But finite audits show that dropping
    any one of these clauses reopens families.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import exp, log


Atom = tuple[int, ...]
Vector = list[float]


@dataclass(frozen=True)
class BoundaryAudit:
    target: str
    required_clause: str
    positive_result: str
    failure_if_absent: str
    value: str
    verdict: str


def atoms(n: int) -> list[Atom]:
    return list(product((-1, 1), repeat=n))


def normalize(weights: Vector) -> Vector:
    total = sum(weights)
    return [weight / total for weight in weights]


def law_from_potential(n: int, potential) -> Vector:
    return normalize([exp(potential(atom)) for atom in atoms(n)])


def l1(left: Vector, right: Vector) -> float:
    return sum(abs(a - b) for a, b in zip(left, right))


def marginal(law: Vector, n: int, keep: tuple[int, ...]) -> Vector:
    kept_atoms = list(product((-1, 1), repeat=len(keep)))
    index = {atom: i for i, atom in enumerate(kept_atoms)}
    result = [0.0 for _ in kept_atoms]
    for atom, probability in zip(atoms(n), law):
        result[index[tuple(atom[i] for i in keep)]] += probability
    return result


def projective_error(theta: float) -> float:
    # A projective family with independent spins is consistent exactly.
    law3 = law_from_potential(3, lambda atom: theta * (atom[0] + atom[1] + atom[2]))
    law2 = law_from_potential(2, lambda atom: theta * (atom[0] + atom[1]))
    return l1(marginal(law3, 3, (0, 1)), law2)


def projective_family_span() -> float:
    laws = [law_from_potential(2, lambda atom, t=t: t * (atom[0] + atom[1])) for t in (0.2, 0.8, 1.5)]
    return max(l1(a, b) for a in laws for b in laws)


def nontrivial_defect_span() -> float:
    laws = [law_from_potential(2, lambda atom, t=t: t * atom[0] * atom[1]) for t in (0.3, 0.9, 1.4)]
    return max(l1(a, b) for a in laws for b in laws)


def positivity_boundary_span() -> float:
    laws = [law_from_potential(2, lambda atom, t=t: t * atom[0] * atom[1]) for t in (1.0, 3.0, 6.0)]
    return max(l1(a, b) for a in laws for b in laws)


def coefficient_family_span() -> float:
    laws = [
        law_from_potential(3, lambda atom, a=a, b=b: a * atom[0] * atom[1] + b * atom[1] * atom[2])
        for a, b in ((0.4, 0.4), (0.8, 0.4), (0.4, 1.0))
    ]
    return max(l1(a, b) for a in laws for b in laws)


def deterministic_generator_error() -> float:
    # A toy complete rule: independent fair law for every finite diamond.
    # It is fully generative/projective but trivial.
    return projective_error(0.0)


def empirical_fit_span() -> float:
    # Three supplied empirical correlations generate three different laws.
    laws = []
    for corr in (0.2, 0.5, 0.8):
        theta = 0.5 * log((1.0 + corr) / (1.0 - corr))
        laws.append(law_from_potential(2, lambda atom, t=theta: t * atom[0] * atom[1]))
    return max(l1(a, b) for a in laws for b in laws)


def audits() -> list[BoundaryAudit]:
    return [
        BoundaryAudit(
            "generative law",
            "outputs P_D for every sealed D",
            "well-defined process object",
            "otherwise P_D is input",
            "binary yes/no",
            "REQ-GENERATIVE",
        ),
        BoundaryAudit(
            "projective consistency",
            "marginals match refinements",
            f"toy error={deterministic_generator_error():.1e}",
            "consistent families still vary",
            f"span={projective_family_span():.3f}",
            "REQ-PROJECTIVE-NOT-ENOUGH",
        ),
        BoundaryAudit(
            "positivity",
            "P_D(a)>0",
            "RN actions finite",
            "near-degenerate limits still allowed",
            f"span={positivity_boundary_span():.3f}",
            "REQ-POSITIVE-NOT-ENOUGH",
        ),
        BoundaryAudit(
            "nontrivial defect",
            "modular factorization fails",
            "events possible",
            "defect amplitude remains free",
            f"span={nontrivial_defect_span():.3f}",
            "REQ-DEFECT-NOT-ENOUGH",
        ),
        BoundaryAudit(
            "unique collar",
            "exact minimal Markov blanket",
            "feeds score geometry",
            "does not set couplings",
            f"span={coefficient_family_span():.3f}",
            "REQ-COLLAR-NOT-ENOUGH",
        ),
        BoundaryAudit(
            "no free coefficients",
            "all numbers derived by rule",
            "would close Branch A",
            "missing in tested candidates",
            "decisive",
            "REQ-NO-FREE-COEFF",
        ),
        BoundaryAudit(
            "trivial complete rule",
            "uniform P_D for all D",
            "closes formally",
            "no events/sources/beta",
            "eventless",
            "FAIL-CLOSES-EMPTY",
        ),
        BoundaryAudit(
            "empirical process rule",
            "fit P_D from records",
            "identifies law operationally",
            "correlations supplied by nature",
            f"span={empirical_fit_span():.3f}",
            "IDENT-NOT-PRINCIPLE",
        ),
        BoundaryAudit(
            "Branch-A law target",
            "generative+projective+positive+nontrivial+unique collar+no coeffs",
            "would fix P_D",
            "not found in finite campaign",
            "the final theorem",
            "OPEN-UNIQUE-PROCESS-LAW",
        ),
    ]


def print_audits(rows: list[BoundaryAudit]) -> None:
    print("process-law boundary campaign")
    print("-----------------------------")
    print(
        "target                    required clause                                      positive result                  "
        "failure if absent                  value                         verdict"
    )
    for row in rows:
        print(
            f"{row.target:25s} "
            f"{row.required_clause:52s} "
            f"{row.positive_result:32s} "
            f"{row.failure_if_absent:34s} "
            f"{row.value:29s} "
            f"{row.verdict}"
        )


def main() -> None:
    print("=" * 150)
    print("v6 Paper 3 section 58: process-law boundary campaign")
    print("=" * 150)
    rows = audits()
    print_audits(rows)
    print()
    print("VERDICT")
    print("-------")
    print("A principle that fixes P_D must be a complete generative process law, not")
    print("a consistency or optimization principle applied after the fact.  It must")
    print("output positive P_D for every sealed finite diamond, commute with")
    print("refinement, produce nontrivial defects, give unique collars, and contain")
    print("no free coefficients.  The uniform law satisfies the formal parts but is")
    print("empty.  Nontrivial audited families keep free coefficients.  Therefore the")
    print("final Branch-A theorem target is a unique nontrivial process-law theorem.")


if __name__ == "__main__":
    main()
