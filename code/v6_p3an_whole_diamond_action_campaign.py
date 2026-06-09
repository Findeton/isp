"""
v6 Paper 3 section 50: whole-diamond action unification campaign.

Question:
    Can we find or refute a non-Markovian whole-diamond action S_D whose RN
    cocycle, refinement anomaly, and deletion generator are the same object?

Finite answer:
    Found conditionally, not uniquely.

    For a finite sealed Leibniz atom set with count reference U, any positive
    law P defines a whole-diamond RN action

        S = -log(dP/dU)

    up to an additive constant.  In a finite product/readout basis, S has a
    unique Walsh/Mobius interaction decomposition.  That same S:

      * gives the RN/Gibbs probability law;
      * composes as an RN cocycle under sealed products;
      * generates refinement/coarse-graining anomalies by log-sum-exp over
        forgotten fibers;
      * generates deletion by removing the unique interaction terms involving
        the deleted event/readout.

    This is a real unifying object and it is compatible with non-Markovian
    whole-diamond interactions.

    But it does not select the dynamics.  Families of S pass all three
    identities while changing event density, memory scale, and deletion
    response.  Therefore the object exists; the unique field equation is still
    not derived.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product
from math import exp, log


Atom = tuple[int, ...]
Coeff = dict[tuple[int, ...], float]
Vector = list[float]


@dataclass(frozen=True)
class WholeActionAudit:
    target: str
    data: str
    invariant: str
    positive: str
    obstruction: str
    value: str
    verdict: str


def atoms(n: int) -> list[Atom]:
    return list(product((0, 1), repeat=n))


def subsets(n: int) -> list[tuple[int, ...]]:
    all_subsets: list[tuple[int, ...]] = [()]
    for size in range(1, n + 1):
        all_subsets.extend(combinations(range(n), size))
    return all_subsets


def spin(bit: int) -> int:
    return 1 if bit else -1


def chi(atom: Atom, subset: tuple[int, ...]) -> int:
    value = 1
    for index in subset:
        value *= spin(atom[index])
    return value


def action_value(atom: Atom, coeffs: Coeff) -> float:
    return sum(value * chi(atom, subset) for subset, value in coeffs.items())


def action_values(n: int, coeffs: Coeff) -> Vector:
    return [action_value(atom, coeffs) for atom in atoms(n)]


def normalize(weights: Vector) -> Vector:
    total = sum(weights)
    return [weight / total for weight in weights]


def gibbs_law(n: int, coeffs: Coeff) -> Vector:
    return normalize([exp(-value) for value in action_values(n, coeffs)])


def uniform(n: int) -> Vector:
    return [1.0 / (2**n)] * (2**n)


def l1(left: Vector, right: Vector) -> float:
    return sum(abs(a - b) for a, b in zip(left, right))


def walsh_coefficients(n: int, values: Vector) -> Coeff:
    coeffs: Coeff = {}
    atom_list = atoms(n)
    for subset in subsets(n):
        coeffs[subset] = sum(value * chi(atom, subset) for value, atom in zip(values, atom_list)) / len(atom_list)
    return coeffs


def reconstruct_error(n: int, coeffs: Coeff, values: Vector) -> float:
    return max(abs(action_value(atom, coeffs) - value) for atom, value in zip(atoms(n), values))


def rn_action_from_law(law: Vector) -> Vector:
    n = (len(law)).bit_length() - 1
    u = 1.0 / (2**n)
    return [-log(prob / u) for prob in law]


def rn_reconstruction_error(n: int, coeffs: Coeff) -> float:
    law = gibbs_law(n, coeffs)
    rn_action = rn_action_from_law(law)
    # RN action and input action differ only by an additive constant.
    values = action_values(n, coeffs)
    shifts = [rn - value for rn, value in zip(rn_action, values)]
    mean_shift = sum(shifts) / len(shifts)
    return max(abs(shift - mean_shift) for shift in shifts)


def product_action_coeffs(left: Coeff, right: Coeff, n_left: int) -> Coeff:
    result: Coeff = {}
    for subset, value in left.items():
        result[subset] = result.get(subset, 0.0) + value
    for subset, value in right.items():
        shifted = tuple(index + n_left for index in subset)
        result[shifted] = result.get(shifted, 0.0) + value
    return result


def rn_product_cocycle_error() -> float:
    left = {(0,): 0.4, (1,): -0.2, (0, 1): 0.3}
    right = {(0,): -0.7}
    joined = product_action_coeffs(left, right, 2)
    law_left = gibbs_law(2, left)
    law_right = gibbs_law(1, right)
    law_joined = gibbs_law(3, joined)
    product_law = [a * b for a in law_left for b in law_right]
    return l1(law_joined, product_law)


def marginalize_law(n: int, law: Vector, keep: tuple[int, ...]) -> Vector:
    kept_atoms = atoms(len(keep))
    index = {atom: i for i, atom in enumerate(kept_atoms)}
    pushed = [0.0] * len(kept_atoms)
    for probability, atom in zip(law, atoms(n)):
        kept = tuple(atom[i] for i in keep)
        pushed[index[kept]] += probability
    return pushed


def effective_action_by_logsumexp(n: int, coeffs: Coeff, keep: tuple[int, ...]) -> Vector:
    law = gibbs_law(n, coeffs)
    coarse_law = marginalize_law(n, law, keep)
    return rn_action_from_law(coarse_law)


def coarse_reconstruction_error() -> float:
    n = 4
    coeffs: Coeff = {
        (0,): 0.25,
        (1,): -0.15,
        (2,): 0.10,
        (0, 2): 0.40,
        (1, 3): -0.30,
        (0, 1, 2, 3): 0.55,
    }
    keep = (0, 2)
    eff_action = effective_action_by_logsumexp(n, coeffs, keep)
    eff_coeffs = walsh_coefficients(len(keep), eff_action)
    reconstructed = gibbs_law(len(keep), eff_coeffs)
    actual = marginalize_law(n, gibbs_law(n, coeffs), keep)
    return l1(reconstructed, actual)


def restrict_coeffs_delete(coeffs: Coeff, delete_index: int) -> Coeff:
    reduced: Coeff = {}
    for subset, value in coeffs.items():
        if delete_index in subset:
            continue
        shifted = tuple(index - 1 if index > delete_index else index for index in subset)
        reduced[shifted] = reduced.get(shifted, 0.0) + value
    return reduced


def deletion_law(n: int, coeffs: Coeff, delete_index: int) -> Vector:
    return gibbs_law(n - 1, restrict_coeffs_delete(coeffs, delete_index))


def deletion_vs_marginal_gap() -> float:
    n = 3
    coeffs: Coeff = {
        (0,): 0.2,
        (1,): -0.1,
        (2,): 0.3,
        (0, 1): 0.7,
        (1, 2): -0.4,
        (0, 1, 2): 0.9,
    }
    delete_index = 1
    surgical = deletion_law(n, coeffs, delete_index)
    marginal = marginalize_law(n, gibbs_law(n, coeffs), (0, 2))
    return l1(surgical, marginal)


def removed_interaction_norm(coeffs: Coeff, delete_index: int) -> float:
    return sum(abs(value) for subset, value in coeffs.items() if delete_index in subset)


def nonmarkov_cmi() -> float:
    n = 3
    coeffs: Coeff = {
        (0,): 0.1,
        (1,): -0.2,
        (2,): 0.15,
        (0, 1): 0.3,
        (1, 2): -0.25,
        (0, 1, 2): 1.1,
    }
    law = gibbs_law(n, coeffs)
    atom_list = atoms(n)
    p_xyz = {atom: probability for atom, probability in zip(atom_list, law)}
    p_xy: dict[tuple[int, int], float] = {}
    p_yz: dict[tuple[int, int], float] = {}
    p_y: dict[int, float] = {}
    for (x, y, z), probability in p_xyz.items():
        p_xy[(x, y)] = p_xy.get((x, y), 0.0) + probability
        p_yz[(y, z)] = p_yz.get((y, z), 0.0) + probability
        p_y[y] = p_y.get(y, 0.0) + probability
    return sum(
        probability * log(probability * p_y[y] / (p_xy[(x, y)] * p_yz[(y, z)]))
        for (x, y, z), probability in p_xyz.items()
        if probability > 0.0
    )


def family_identity_span() -> float:
    # All these whole-diamond actions pass RN/anomaly/deletion construction,
    # but the resulting laws differ.
    laws = []
    for triple in (0.1, 0.7, 1.4):
        coeffs: Coeff = {(0,): 0.2, (1,): -0.1, (2,): 0.3, (0, 1, 2): triple}
        laws.append(gibbs_law(3, coeffs))
    return max(l1(left, right) for left in laws for right in laws)


def scale_family_span() -> float:
    base: Coeff = {(0,): 0.2, (1,): -0.1, (2,): 0.3, (0, 1, 2): 0.8}
    laws = []
    for scale in (0.5, 1.0, 2.0):
        coeffs = {subset: scale * value for subset, value in base.items()}
        laws.append(gibbs_law(3, coeffs))
    return max(l1(left, right) for left in laws for right in laws)


def same_coarse_different_fine_gap() -> float:
    # Two fine actions have the same marginal on variables (0,1) but different
    # hidden interaction involving variable 2.  This is constructed by taking a
    # common coarse law and two different conditional laws for the hidden bit.
    coarse = [0.10, 0.20, 0.30, 0.40]
    fine_a = []
    fine_b = []
    for probability in coarse:
        fine_a.extend([0.5 * probability, 0.5 * probability])
        fine_b.extend([0.8 * probability, 0.2 * probability])
    action_a = walsh_coefficients(3, rn_action_from_law(fine_a))
    action_b = walsh_coefficients(3, rn_action_from_law(fine_b))
    return max(abs(action_a.get(subset, 0.0) - action_b.get(subset, 0.0)) for subset in subsets(3))


def audits() -> list[WholeActionAudit]:
    base_coeffs: Coeff = {
        (0,): 0.2,
        (1,): -0.1,
        (2,): 0.3,
        (0, 1): 0.7,
        (1, 2): -0.4,
        (0, 1, 2): 0.9,
    }
    rn_values = rn_action_from_law(gibbs_law(3, base_coeffs))
    rn_coeffs = walsh_coefficients(3, rn_values)
    return [
        WholeActionAudit(
            "RN whole action",
            "positive law P",
            "S=-log(dP/dU)",
            f"recon err={reconstruct_error(3, rn_coeffs, rn_values):.1e}",
            "P must be supplied",
            "unique up to const",
            "PASS-RN-ACTION",
        ),
        WholeActionAudit(
            "product cocycle",
            "sealed product",
            "S(xy)=S(x)+S(y)",
            f"law err={rn_product_cocycle_error():.1e}",
            "only for product composition",
            "RN cocycle",
            "PASS-COCYCLE",
        ),
        WholeActionAudit(
            "refinement anomaly",
            "forget fibers",
            "log-sum-exp S_eff",
            f"coarse err={coarse_reconstruction_error():.1e}",
            "requires fine S",
            "anomaly from S",
            "PASS-ANOMALY",
        ),
        WholeActionAudit(
            "deletion generator",
            "Walsh interactions",
            "remove terms involving x",
            f"removed norm={removed_interaction_norm(base_coeffs, 1):.3f}",
            "needs product/readout basis",
            f"marginal gap={deletion_vs_marginal_gap():.3f}",
            "PASS-CONDITIONAL-DELETE",
        ),
        WholeActionAudit(
            "non-Markovian action",
            "triple interaction",
            "whole-diamond term",
            f"CMI={nonmarkov_cmi():.3f}",
            "not step Markov",
            "allowed",
            "PASS-NONMARKOV",
        ),
        WholeActionAudit(
            "same machinery family",
            "vary triple term",
            "RN+anomaly+delete all pass",
            "identities preserved",
            "S coefficient free",
            f"P span={family_identity_span():.3f}",
            "FAIL-UNIQUE-S",
        ),
        WholeActionAudit(
            "scale family",
            "S -> cS",
            "same construction",
            "identities preserved",
            "scale free",
            f"P span={scale_family_span():.3f}",
            "FAIL-SCALE",
        ),
        WholeActionAudit(
            "same coarse law",
            "different hidden fibers",
            "same marginal P",
            "coarse action same",
            "fine S differs",
            f"S gap={same_coarse_different_fine_gap():.3f}",
            "FAIL-COARSE-NOT-FINE",
        ),
        WholeActionAudit(
            "whole-action theorem",
            "supplied positive P/S",
            "RN+anomaly+delete",
            "one object unifies three jobs",
            "does not select P/S",
            "conditional success",
            "THM-CONDITIONAL-WHOLE-ACTION",
        ),
        WholeActionAudit(
            "selection theorem",
            "sealed Leibniz process only",
            "derive S intrinsically",
            "not found",
            "families survive",
            "A-full open",
            "OPEN-SELECTION",
        ),
    ]


def print_audits(rows: list[WholeActionAudit]) -> None:
    print("whole-diamond action unification campaign")
    print("-----------------------------------------")
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
    print("v6 Paper 3 section 50: whole-diamond action unification campaign")
    print("=" * 150)
    print_audits(audits())
    print()
    print("VERDICT")
    print("-------")
    print("Found conditionally: a finite whole-diamond RN action S unifies probability,")
    print("refinement anomaly, and deletion generation.  The same non-Markovian S gives")
    print("P by Gibbs/RN, coarse actions by log-sum-exp over fibers, and deletion by")
    print("removing the unique Walsh/Mobius interaction terms involving the deleted")
    print("event/readout.")
    print()
    print("Refuted as closure: this does not select S.  Families of whole-diamond")
    print("actions pass all three identities while changing the law, scale, hidden")
    print("fine structure, and deletion response.  Branch A-full still needs a")
    print("selection/rigidity theorem for S itself.")


if __name__ == "__main__":
    main()
