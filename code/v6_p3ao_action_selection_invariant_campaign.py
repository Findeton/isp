"""
v6 Paper 3 section 51: invariant S_D selection campaign.

Question:
    Is there an intrinsic invariant condition on sealed finite diamonds that
    makes the whole-diamond action S_D unique?

Finite answer:
    Not from the structural invariants tested here.

    The positive result from section 50 remains true: once a positive law P_D
    is supplied, S_D=-log(dP_D/dU_D) is unique up to an additive constant and
    unifies RN density, refinement anomaly, and deletion surgery.

    But the Einsteinian selection question is harder: can the sealed diamond
    itself select S_D?

    The finite obstruction is representation-theoretic.  Let A_D be the finite
    atom set and G_D its internal automorphism group.  Covariance only says
    that S_D is constant on G_D-orbits.  Therefore the invariant action space
    has dimension |A_D/G_D|, or |A_D/G_D|-1 after quotienting additive
    constants.  If the action is unique, the group is transitive and S_D is
    only the uniform/vacuum law.  If nontrivial events are possible, there are
    at least two orbits and hence a continuous family of invariant actions.

    The rest of the campaign tests stronger natural conditions: product
    cocycles, refinement stability, no-silent-seam cycle closure, fixed KL
    scale, isolated defects, max-entropy, self-duality, and full RN data.  Each
    either leaves a family, selects only the trivial law, or succeeds only after
    an extra equation/constraint/family has already been supplied.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations, product
from math import asinh, exp, log, pi, sin, cos


Atom = tuple[int, ...]
Vector = list[float]


@dataclass(frozen=True)
class SelectionAudit:
    target: str
    invariant_condition: str
    positive_result: str
    obstruction: str
    diagnostic_value: str
    verdict: str


def atoms(n: int) -> list[Atom]:
    return list(product((0, 1), repeat=n))


def spin(bit: int) -> int:
    return 1 if bit else -1


def normalize(weights: Vector) -> Vector:
    total = sum(weights)
    return [weight / total for weight in weights]


def law_from_values(values: Vector) -> Vector:
    return normalize([exp(-value) for value in values])


def l1(left: Vector, right: Vector) -> float:
    return sum(abs(a - b) for a, b in zip(left, right))


def mean(values: Vector) -> float:
    return sum(values) / len(values)


def rms_centered(values: Vector) -> float:
    m = mean(values)
    return (sum((value - m) ** 2 for value in values) / len(values)) ** 0.5


def center_and_normalize(values: Vector) -> Vector:
    m = mean(values)
    centered = [value - m for value in values]
    scale = rms_centered(centered)
    return [value / scale for value in centered]


def hamming(atom: Atom) -> int:
    return sum(atom)


def permute_atom(atom: Atom, perm: tuple[int, ...]) -> Atom:
    return tuple(atom[i] for i in perm)


def bitflip_atom(atom: Atom, mask: Atom) -> Atom:
    return tuple(bit ^ flip for bit, flip in zip(atom, mask))


def orbit_count_under_permutations(n: int) -> int:
    atom_list = atoms(n)
    seen: set[Atom] = set()
    perms = list(permutations(range(n)))
    count = 0
    for atom in atom_list:
        if atom in seen:
            continue
        count += 1
        orbit = {permute_atom(atom, perm) for perm in perms}
        seen.update(orbit)
    return count


def orbit_count_under_perms_and_flips(n: int) -> int:
    atom_list = atoms(n)
    seen: set[Atom] = set()
    perms = list(permutations(range(n)))
    masks = atom_list
    count = 0
    for atom in atom_list:
        if atom in seen:
            continue
        count += 1
        orbit = {
            bitflip_atom(permute_atom(atom, perm), mask)
            for perm in perms
            for mask in masks
        }
        seen.update(orbit)
    return count


def rank_shell_family_span(n: int) -> float:
    laws = []
    for theta_1, theta_2 in ((0.2, 0.0), (0.7, 0.0), (0.2, 0.25), (-0.3, 0.4)):
        values = [theta_1 * hamming(atom) + theta_2 * hamming(atom) ** 2 for atom in atoms(n)]
        laws.append(law_from_values(values))
    return max(l1(left, right) for left in laws for right in laws)


def product_scale_span(n: int) -> float:
    laws = []
    for theta in (0.15, 0.75, 1.50):
        values = [theta * sum(spin(bit) for bit in atom) for atom in atoms(n)]
        laws.append(law_from_values(values))
    return max(l1(left, right) for left in laws for right in laws)


def seam_cycle_span() -> tuple[float, float]:
    # A two-site boundary coupling J is an exact potential.  Hence every closed
    # action cycle has zero work, but J is still free.
    laws = []
    residuals = []
    cycle = [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]
    for coupling in (0.1, 0.8, 1.6):
        values = [coupling * spin(atom[0]) * spin(atom[1]) for atom in atoms(2)]
        law = law_from_values(values)
        laws.append(law)
        action = {atom: value for atom, value in zip(atoms(2), values)}
        residuals.append(sum(action[cycle[i + 1]] - action[cycle[i]] for i in range(len(cycle) - 1)))
    return max(abs(residual) for residual in residuals), max(l1(left, right) for left in laws for right in laws)


def normalized_direction_span(n: int) -> float:
    rank = [float(hamming(atom)) for atom in atoms(n)]
    quad = [float((hamming(atom) - n / 2) ** 2) for atom in atoms(n)]
    u = center_and_normalize(rank)
    v = center_and_normalize(quad)
    laws = []
    for angle in (0.0, pi / 5.0, 2.0 * pi / 5.0):
        values = [cos(angle) * a + sin(angle) * b for a, b in zip(u, v)]
        laws.append(law_from_values(values))
    return max(l1(left, right) for left in laws for right in laws)


def isolated_defect_interval_span() -> tuple[float, float]:
    # Triple whole-diamond interactions create a non-Markovian defect for an
    # open interval of coefficients.  Openness is stability, not uniqueness.
    laws = []
    cmi_values = []
    for triple in (0.6, 1.0, 1.4):
        values = [triple * spin(atom[0]) * spin(atom[1]) * spin(atom[2]) for atom in atoms(3)]
        law = law_from_values(values)
        laws.append(law)
        cmi_values.append(conditional_mutual_information(law))
    return min(cmi_values), max(l1(left, right) for left in laws for right in laws)


def conditional_mutual_information(law: Vector) -> float:
    p_xyz = {atom: probability for atom, probability in zip(atoms(3), law)}
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


def mean_hamming_for_theta(n: int, theta: float) -> float:
    law = law_from_values([theta * hamming(atom) for atom in atoms(n)])
    return sum(prob * hamming(atom) for prob, atom in zip(law, atoms(n)))


def theta_for_mean_hamming(n: int, target_mean: float) -> float:
    lo, hi = -10.0, 10.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if mean_hamming_for_theta(n, mid) > target_mean:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def max_entropy_external_constraint_span(n: int) -> tuple[float, float, float]:
    theta_low = theta_for_mean_hamming(n, 1.5)
    theta_high = theta_for_mean_hamming(n, 2.5)
    law_low = law_from_values([theta_low * hamming(atom) for atom in atoms(n)])
    law_high = law_from_values([theta_high * hamming(atom) for atom in atoms(n)])
    return theta_low, theta_high, l1(law_low, law_high)


def self_dual_ising_value() -> float:
    # Square-lattice Ising self-duality would give sinh(2K)=1.  This is a
    # real selector only after the lattice, duality map, and Ising family have
    # already been supplied.
    return 0.5 * asinh(1.0)


def full_law_rn_recon_error(n: int) -> float:
    values = [0.3 * hamming(atom) - 0.4 * spin(atom[0]) * spin(atom[-1]) for atom in atoms(n)]
    law = law_from_values(values)
    u = 1.0 / len(law)
    rn = [-log(prob / u) for prob in law]
    shifts = [a - b for a, b in zip(rn, values)]
    shift = mean(shifts)
    return max(abs(item - shift) for item in shifts)


def audits() -> list[SelectionAudit]:
    n = 4
    shell_orbits = orbit_count_under_permutations(n)
    transitive_orbits = orbit_count_under_perms_and_flips(n)
    seam_residual, seam_span = seam_cycle_span()
    min_cmi, defect_span = isolated_defect_interval_span()
    theta_low, theta_high, maxent_span = max_entropy_external_constraint_span(n)
    return [
        SelectionAudit(
            "full internal symmetry",
            "all atom relabelings/bit flips",
            f"orbit dim={transitive_orbits}",
            "only constant S; no event/defect",
            "nontriv dim=0",
            "FAIL-NONTRIVIAL",
        ),
        SelectionAudit(
            "causal-rank covariance",
            "permutation-invariant shells",
            f"orbit dim={shell_orbits}",
            "rank-shell coefficients free",
            f"P span={rank_shell_family_span(n):.3f}",
            "FAIL-SHELL-FAMILY",
        ),
        SelectionAudit(
            "product composition",
            "S(D1+D2)=S1+S2",
            "cocycle exact",
            "local action scale remains free",
            f"P span={product_scale_span(n):.3f}",
            "FAIL-SCALE",
        ),
        SelectionAudit(
            "refinement stability",
            "log-sum-exp coarse action",
            "functorial for any fine S",
            "does not choose fine S",
            "identity-level",
            "FAIL-SELECTION",
        ),
        SelectionAudit(
            "no silent seams",
            "closed action cycles vanish",
            f"cycle residual={seam_residual:.1e}",
            "exact potentials can have any coupling",
            f"P span={seam_span:.3f}",
            "FAIL-COUPLING-FREE",
        ),
        SelectionAudit(
            "fixed KL/action unit",
            "normalize ||S|| after constants",
            "scale can be fixed",
            "direction in invariant space remains free",
            f"P span={normalized_direction_span(n):.3f}",
            "FAIL-DIRECTION-FREE",
        ),
        SelectionAudit(
            "isolated defect",
            "positive non-Markovian CMI",
            f"min CMI={min_cmi:.3f}",
            "open interval, not a point",
            f"P span={defect_span:.3f}",
            "FAIL-OPEN-FAMILY",
        ),
        SelectionAudit(
            "maximum entropy",
            "least biased law",
            "uniform if no constraint",
            "nontrivial law needs supplied moment",
            f"theta={theta_low:.3f}/{theta_high:.3f}, span={maxent_span:.3f}",
            "FAIL-CONSTRAINT-EXTERNAL",
        ),
        SelectionAudit(
            "self-duality/criticality",
            "fixed point of supplied dual map",
            f"Kc={self_dual_ising_value():.4f}",
            "requires chosen graph/family/duality",
            "conditional point",
            "COND-NOT-INTRINSIC",
        ),
        SelectionAudit(
            "full RN data",
            "P_D supplied by diamond",
            "S=-log(dP/dU) unique",
            "tautological unless P_D is derived",
            f"recon err={full_law_rn_recon_error(n):.1e}",
            "PASS-IF-P-SUPPLIED",
        ),
        SelectionAudit(
            "finite no-go",
            "G-invariant sealed diamond only",
            "S constant on orbits",
            "unique nonconstant S impossible without extra equations",
            "|A/G|-1 degrees",
            "THM-INVARIANT-NO-GO",
        ),
        SelectionAudit(
            "remaining opening",
            "derive the equation F_D(S)=0",
            "would select S if unique",
            "F_D is the missing dynamics",
            "not found here",
            "OPEN-FIELD-EQUATION",
        ),
    ]


def print_audits(rows: list[SelectionAudit]) -> None:
    print("invariant S_D selection campaign")
    print("--------------------------------")
    print(
        "target                    invariant condition             positive result              "
        "obstruction                         diagnostic value              verdict"
    )
    for row in rows:
        print(
            f"{row.target:25s} "
            f"{row.invariant_condition:31s} "
            f"{row.positive_result:28s} "
            f"{row.obstruction:35s} "
            f"{row.diagnostic_value:29s} "
            f"{row.verdict}"
        )


def main() -> None:
    print("=" * 150)
    print("v6 Paper 3 section 51: invariant whole-action selection campaign")
    print("=" * 150)
    rows = audits()
    print_audits(rows)
    print()
    print("VERDICT")
    print("-------")
    print("Refuted for the structural sealed-diamond invariants tested here.")
    print("Automorphism invariance gives a vector space of orbit-constant actions.")
    print("If there is one orbit, S is only the uniform/vacuum law.  If there are")
    print("several orbits, nontrivial invariant actions exist but form a continuous")
    print("family after the additive constant is removed.")
    print()
    print("The stronger conditions do not repair this by themselves.  Cocycle,")
    print("refinement, no-silent-seam, action-unit, isolated-defect, and maximum-")
    print("entropy tests either leave families or require an externally supplied")
    print("constraint/equation/family.  A self-dual point can be selected only after")
    print("a graph, duality map, and action family have already been chosen.")
    print()
    print("Therefore the missing Branch-A object is not another invariant adjective")
    print("on sealed diamonds.  It is an intrinsic record field equation F_D(S)=0,")
    print("derived from the physical process, with a unique nontrivial solution.")


if __name__ == "__main__":
    main()
