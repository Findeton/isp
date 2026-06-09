"""
v6 Paper 3 section 44: canonical reference U campaign.

Question:
    Can the canonical compositional reference U be derived, or is it a hidden
    background choice?

Finite answer:
    U is not derived from eventlessness or product composition alone.  Both
    allow biased product-reference families.  U is derived in finite form once
    the base ontology is a sealed finite counting-measure functor:

      1. local outcomes are indivisible record atoms;
      2. no extra structure distinguishes atoms inside a sealed count fiber;
      3. the reference is invariant under internal relabelling;
      4. references compose by product/gluing;
      5. refinements split count fibers evenly or by canonical measure-
         preserving equal weights;
      6. the same reference is used by every role.

    Under those conditions U(A)=|A|/|Omega| is unique.  If orbit weights,
    biased vacua, unbalanced refinements, or role-dependent references are
    allowed, U is supplied and the construction is branch B.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations, product
from math import log


Vector = list[float]
Matrix = list[list[float]]


@dataclass(frozen=True)
class ReferenceAudit:
    target: str
    data: str
    invariant: str
    positive: str
    obstruction: str
    value: str
    verdict: str


def uniform(n: int) -> Vector:
    return [1.0 / n] * n


def entropy(p: Vector) -> float:
    return -sum(value * log(value) for value in p if value > 0.0)


def l1(left: Vector, right: Vector) -> float:
    return sum(abs(a - b) for a, b in zip(left, right))


def permute(p: Vector, permutation: tuple[int, ...]) -> Vector:
    return [p[permutation[i]] for i in range(len(p))]


def max_permutation_gap(p: Vector) -> float:
    return max(l1(p, permute(p, permutation)) for permutation in permutations(range(len(p))))


def product_ref(left: Vector, right: Vector) -> Vector:
    return [a * b for a in left for b in right]


def product_error(n: int, m: int) -> float:
    return l1(product_ref(uniform(n), uniform(m)), uniform(n * m))


def biased_product_family_span() -> float:
    biases = (0.2, 0.5, 0.8)
    # Each p defines a perfectly compositional product family on binary atoms,
    # so product composition alone cannot select p.
    return max(biases) - min(biases)


def eventless_residual_binary(p: float) -> float:
    joint = [[(1.0 - p) * (1.0 - p), (1.0 - p) * p], [p * (1.0 - p), p * p]]
    row = [sum(joint[0]), sum(joint[1])]
    col = [joint[0][0] + joint[1][0], joint[0][1] + joint[1][1]]
    return sum(
        joint[i][j] * log(joint[i][j] / (row[i] * col[j]))
        for i in range(2)
        for j in range(2)
        if joint[i][j] > 0.0
    )


def eventless_bias_span() -> float:
    return max(eventless_residual_binary(p) for p in (0.2, 0.5, 0.8))


def orbit_invariant_distribution(weight_first_orbit: float) -> Vector:
    w = weight_first_orbit
    return [w / 2.0, w / 2.0, (1.0 - w) / 2.0, (1.0 - w) / 2.0]


def orbit_symmetry_gap(p: Vector) -> float:
    # Group swaps 0<->1 and 2<->3 but does not mix the two orbits.
    perms = ((0, 1, 2, 3), (1, 0, 2, 3), (0, 1, 3, 2), (1, 0, 3, 2))
    return max(l1(p, permute(p, permutation)) for permutation in perms)


def orbit_weight_span() -> float:
    low = orbit_invariant_distribution(0.2)
    high = orbit_invariant_distribution(0.8)
    return l1(low, high)


def balanced_refinement_error(n: int = 3, split: int = 2) -> float:
    refined = uniform(n * split)
    pushed = [sum(refined[i * split + j] for j in range(split)) for i in range(n)]
    return l1(pushed, uniform(n))


def unbalanced_refinement_drift(fibers: tuple[int, ...] = (1, 2, 3)) -> float:
    total = sum(fibers)
    refined = uniform(total)
    pushed = []
    offset = 0
    for size in fibers:
        pushed.append(sum(refined[offset + j] for j in range(size)))
        offset += size
    return l1(pushed, uniform(len(fibers)))


def role_reference_span() -> float:
    record = uniform(4)
    source = [0.40, 0.20, 0.20, 0.20]
    return l1(record, source)


def max_entropy_gap() -> float:
    return entropy(uniform(4)) - entropy([0.40, 0.20, 0.20, 0.20])


def pushforward_refinement_error() -> float:
    # If a coarse atom has a canonical two-fold refinement, equal split is the
    # only role-free way to preserve its mass without adding a hidden label.
    coarse = [0.5, 0.5]
    refined_equal = [0.25, 0.25, 0.25, 0.25]
    pushed = [refined_equal[0] + refined_equal[1], refined_equal[2] + refined_equal[3]]
    return l1(coarse, pushed)


def audits() -> list[ReferenceAudit]:
    biased = [0.40, 0.20, 0.20, 0.20]
    return [
        ReferenceAudit(
            "counting reference",
            "4 indivisible atoms",
            "full relabelling invariance",
            f"uniform perm gap={max_permutation_gap(uniform(4)):.1e}",
            f"biased perm gap={max_permutation_gap(biased):.3f}",
            "U_i=1/4",
            "PASS-FULL-SYMMETRY-U",
        ),
        ReferenceAudit(
            "product composition",
            "Omega x Lambda",
            "U_Omega x U_Lambda",
            f"product error={product_error(3, 5):.1e}",
            "composition alone allows bias",
            f"bias span={biased_product_family_span():.3f}",
            "PASS-PRODUCT-BUT-NOT-ENOUGH",
        ),
        ReferenceAudit(
            "eventless vacuum",
            "independent product",
            "I(X;Z)=0",
            f"residual span={eventless_bias_span():.1e}",
            "biased products all eventless",
            f"bias span={biased_product_family_span():.3f}",
            "FAIL-EVENTLESS-NOT-UNIQUE",
        ),
        ReferenceAudit(
            "orbit-weight freedom",
            "two automorphism orbits",
            "orbit invariance only",
            f"orbit gap={orbit_symmetry_gap(orbit_invariant_distribution(0.2)):.1e}",
            f"weight span={orbit_weight_span():.3f}",
            "orbit weights free",
            "FAIL-ORBIT-WEIGHT-FREEDOM",
        ),
        ReferenceAudit(
            "maximum count entropy",
            "no constraints",
            "maximize H over atoms",
            f"entropy gap={max_entropy_gap():.6f}",
            "requires atom count measure",
            "uniform unique on atoms",
            "PASS-CONDITIONAL-MAXENT",
        ),
        ReferenceAudit(
            "balanced refinement",
            "equal atom split",
            "pushforward U_ref=U",
            f"error={balanced_refinement_error():.1e}",
            "balanced fibers required",
            "cofinal stable",
            "PASS-BALANCED-REFINEMENT",
        ),
        ReferenceAudit(
            "unbalanced refinement",
            "unequal split fibers",
            "uniform refined atoms",
            f"drift={unbalanced_refinement_drift():.3f}",
            "coarse U moves",
            "needs measure-preserving rule",
            "FAIL-UNBALANCED-REFINEMENT",
        ),
        ReferenceAudit(
            "fiber equal split",
            "given refinement map",
            "split parent mass equally",
            f"push error={pushforward_refinement_error():.1e}",
            "requires intrinsic refinement map",
            "not a later choice",
            "PASS-CONDITIONAL-FIBER-U",
        ),
        ReferenceAudit(
            "role-blind reference",
            "record/source roles",
            "same U",
            "record U uniform",
            f"role span={role_reference_span():.3f}",
            "role-specific U changes action",
            "FAIL-ROLE-U",
        ),
        ReferenceAudit(
            "canonical U theorem",
            "sealed count functor",
            "symmetry+product+refinement",
            "U(A)=|A|/|Omega|",
            "requires count atoms and maps",
            "derived if count functor base",
            "THM-CONDITIONAL-CANONICAL-U",
        ),
    ]


def print_audits(rows: list[ReferenceAudit]) -> None:
    print("canonical reference U campaign")
    print("------------------------------")
    print(
        "target                    data                    invariant               "
        "positive                         obstruction                     value                         verdict"
    )
    for row in rows:
        print(
            f"{row.target:25s} "
            f"{row.data:23s} "
            f"{row.invariant:23s} "
            f"{row.positive:32s} "
            f"{row.obstruction:31s} "
            f"{row.value:29s} "
            f"{row.verdict}"
        )


def main() -> None:
    print("=" * 150)
    print("v6 Paper 3 section 44: canonical reference U campaign")
    print("=" * 150)
    print_audits(audits())
    print()
    print("VERDICT")
    print("-------")
    print("U is not derived from eventlessness or product composition alone; biased")
    print("product references pass those tests.  U is derived only when the base is a")
    print("sealed finite counting-measure functor: indivisible record atoms, internal")
    print("relabeling symmetry, product composition, balanced or measure-preserving")
    print("refinement, and role-blind use of the same reference.")
    print()
    print("Thus the final primitive is not a chosen U.  It is the sealed count functor.")
    print("If the atom counts, refinement maps, or orbit weights are supplied after")
    print("the fact, branch A-current remains conditional.  If they are the physical")
    print("base, U(A)=|A|/|Omega| is derived.")


if __name__ == "__main__":
    main()
