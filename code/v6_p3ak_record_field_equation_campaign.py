"""
v6 Paper 3 section 47: sealed record field-equation campaign.

Question:
    Does the sealed Leibniz record process determine the physical possible-
    change law P_D, deletion/intervention, gamma, and beta?

Finite answer:
    No.  The sealed Leibniz process determines the structural record functor:
    atoms, Boolean algebra, restrictions, roles, U, and RN action units.  It
    does not determine the probability law or intervention law.

    Finite same-structure counterexamples:

      * Bernoulli product families on the same atoms vary gamma.
      * Stationary Markov families on the same atoms keep gamma fixed and vary
        correlation length/beta.
      * Markov gluing/no-silent-seam constraints hold for a continuum of
        transition parameters.
      * Same observational P admits different do-delete/intervention maps.

    Conditional positive theorem:
      If an intrinsic record action/potential S_D is supplied as a natural,
      local, role-blind functional on the sealed record functor, then the
      finite Gibbs/RN variational law

          P_D(a) = U_D(a) exp(-S_D(a)) / Z_D

      uniquely determines P_D.  Deletion still requires an intrinsic natural
      intervention/deletion transformation, or an equivalent deletion-response
      rule.  The pair (S_D, delta_D) is the record field equation.  If it is
      supplied externally, the result is branch B.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import exp, log


Vector = list[float]


@dataclass(frozen=True)
class FieldEquationAudit:
    target: str
    data: str
    invariant: str
    positive: str
    obstruction: str
    value: str
    verdict: str


def l1(left: Vector, right: Vector) -> float:
    return sum(abs(a - b) for a, b in zip(left, right))


def normalize(weights: Vector) -> Vector:
    total = sum(weights)
    return [weight / total for weight in weights]


def uniform(n: int) -> Vector:
    return [1.0 / n] * n


def binary_atoms(n: int) -> list[tuple[int, ...]]:
    return list(product((0, 1), repeat=n))


def bernoulli_law(n: int, p: float) -> Vector:
    return [
        (p ** sum(atom)) * ((1.0 - p) ** (n - sum(atom)))
        for atom in binary_atoms(n)
    ]


def event_density(n: int, law: Vector) -> float:
    atoms = binary_atoms(n)
    return sum(prob * (sum(atom) / n) for prob, atom in zip(law, atoms))


def bernoulli_gamma_span(n: int = 6) -> float:
    return max(event_density(n, bernoulli_law(n, p)) for p in (0.2, 0.5, 0.8)) - min(
        event_density(n, bernoulli_law(n, p)) for p in (0.2, 0.5, 0.8)
    )


def projective_bernoulli_error(p: float = 0.3) -> float:
    # Marginalizing a length-4 Bernoulli law to the first 3 bits gives the
    # length-3 Bernoulli law with the same p.
    law4 = bernoulli_law(4, p)
    atoms4 = binary_atoms(4)
    pushed = [0.0] * 8
    atoms3 = binary_atoms(3)
    index3 = {atom: i for i, atom in enumerate(atoms3)}
    for prob, atom in zip(law4, atoms4):
        pushed[index3[atom[:3]]] += prob
    return l1(pushed, bernoulli_law(3, p))


def markov_law(n: int, flip: float) -> Vector:
    atoms = binary_atoms(n)
    values = []
    for atom in atoms:
        prob = 0.5
        for left, right in zip(atom, atom[1:]):
            prob *= flip if left != right else (1.0 - flip)
        values.append(prob)
    return values


def adjacent_correlation(n: int, law: Vector) -> float:
    atoms = binary_atoms(n)
    corr = 0.0
    count = 0
    for prob, atom in zip(law, atoms):
        for left, right in zip(atom, atom[1:]):
            # Map 0,1 to -1,+1.
            corr += prob * ((2 * left - 1) * (2 * right - 1))
            count += 1
    return corr / (n - 1)


def beta_inverse_proxy(flip: float) -> float:
    corr = abs(1.0 - 2.0 * flip)
    if corr <= 0.0:
        return 0.0
    return -1.0 / log(corr)


def markov_beta_span() -> float:
    widths = [beta_inverse_proxy(flip) for flip in (0.1, 0.25, 0.4)]
    return max(widths) - min(widths)


def conditional_mutual_information_xyz(flip: float) -> float:
    # Three-bit stationary Markov chain X-Y-Z.
    law = markov_law(3, flip)
    atoms = binary_atoms(3)
    p_xyz = {(x, y, z): prob for prob, (x, y, z) in zip(law, atoms)}
    p_xy: dict[tuple[int, int], float] = {}
    p_yz: dict[tuple[int, int], float] = {}
    p_y: dict[int, float] = {}
    for (x, y, z), prob in p_xyz.items():
        p_xy[(x, y)] = p_xy.get((x, y), 0.0) + prob
        p_yz[(y, z)] = p_yz.get((y, z), 0.0) + prob
        p_y[y] = p_y.get(y, 0.0) + prob
    cmi = 0.0
    for (x, y, z), prob in p_xyz.items():
        if prob > 0.0:
            cmi += prob * log(prob * p_y[y] / (p_xy[(x, y)] * p_yz[(y, z)]))
    return cmi


def markov_cmi_max() -> float:
    return max(abs(conditional_mutual_information_xyz(flip)) for flip in (0.1, 0.25, 0.4))


def observational_joint() -> list[list[float]]:
    # X and Y are observed correlated.  This observational law does not by
    # itself say what intervention "delete X" means.
    return [[0.45, 0.05], [0.05, 0.45]]


def do_delete_maps_gap() -> float:
    joint = observational_joint()
    # Intervention 1: marginal delete X, leaving observed Y marginal.
    marginal_y = [joint[0][0] + joint[1][0], joint[0][1] + joint[1][1]]
    # Intervention 2: clamp the deleted record to the no-event branch X=0 and
    # use P(Y|X=0).
    row0 = sum(joint[0])
    clamp_y = [joint[0][0] / row0, joint[0][1] / row0]
    return l1(marginal_y, clamp_y)


def max_entropy_uniform_gap() -> float:
    # With only the record atom set and U, maximum entropy selects U.  This is
    # unique but dynamically empty for nontrivial event rates.
    return l1(uniform(4), normalize([1.0, 1.0, 1.0, 1.0]))


def gibbs_law(action: Vector) -> Vector:
    return normalize([exp(-value) for value in action])


def gibbs_first_order_error(action: Vector, law: Vector) -> float:
    # For P_i ∝ exp(-S_i), log(P_i/U_i) + S_i is constant.  This is the
    # finite Euler condition for minimizing D(P||U)+E_P[S].
    n = len(law)
    u = 1.0 / n
    values = [log(prob / u) + s for prob, s in zip(law, action)]
    mean = sum(values) / n
    return max(abs(value - mean) for value in values)


def gibbs_action_span() -> float:
    laws = [gibbs_law([0.0, scale, 2.0 * scale, 3.0 * scale]) for scale in (0.4, 1.0, 1.8)]
    return max(l1(left, right) for left in laws for right in laws)


def boundary_constraint_span() -> float:
    # Same action S=0, different supplied mean event constraints select
    # different Bernoulli p laws.  Constraints are boundary/source data, not
    # determined by the record functor.
    return bernoulli_gamma_span(6)


def audits() -> list[FieldEquationAudit]:
    law_markov_01 = markov_law(6, 0.1)
    law_markov_04 = markov_law(6, 0.4)
    action = [0.0, 0.7, 1.1, 1.9]
    law = gibbs_law(action)
    return [
        FieldEquationAudit(
            "same atoms different gamma",
            "binary record functor",
            "same At,U,restrictions",
            f"projective err={projective_bernoulli_error():.1e}",
            "Bernoulli p free",
            f"gamma span={bernoulli_gamma_span():.3f}",
            "FAIL-P-NOT-DERIVED",
        ),
        FieldEquationAudit(
            "same atoms different beta",
            "stationary Markov records",
            "same At,U,restrictions",
            f"gamma={event_density(6, law_markov_01):.3f}",
            f"corr span={abs(adjacent_correlation(6, law_markov_01) - adjacent_correlation(6, law_markov_04)):.3f}",
            f"beta^-1 span={markov_beta_span():.3f}",
            "FAIL-BETA-NOT-DERIVED",
        ),
        FieldEquationAudit(
            "no-silent seam family",
            "Markov X-Y-Z",
            "I(X;Z|Y)=0",
            f"CMI max={markov_cmi_max():.1e}",
            "transition parameter free",
            "q in {0.1,0.25,0.4}",
            "FAIL-SEAM-NOT-DYNAMICS",
        ),
        FieldEquationAudit(
            "same P different do-delete",
            "observed X,Y law",
            "same observational P",
            "both maps lawful",
            "intervention not in P",
            f"Y-response gap={do_delete_maps_gap():.3f}",
            "FAIL-DO-NOT-DERIVED",
        ),
        FieldEquationAudit(
            "maximum entropy",
            "atoms+U only",
            "maximize H",
            f"uniform gap={max_entropy_uniform_gap():.1e}",
            "selects trivial U",
            "no source/memory law",
            "PASS-TRIVIAL-NOT-PHYSICS",
        ),
        FieldEquationAudit(
            "boundary constraints",
            "same S=0",
            "mean event constraints",
            "unique exponential family",
            "constraint value supplied",
            f"gamma span={boundary_constraint_span():.3f}",
            "FAIL-CONSTRAINT-FREE",
        ),
        FieldEquationAudit(
            "Gibbs/RN variational law",
            "given action S",
            "min D(P||U)+E[S]",
            f"Euler err={gibbs_first_order_error(action, law):.1e}",
            "S is the dynamics",
            "P unique if S fixed",
            "PASS-CONDITIONAL-GIBBS",
        ),
        FieldEquationAudit(
            "action-scale family",
            "same atoms/action form",
            "scale S -> cS",
            "each has unique P",
            "scale not structural",
            f"P span={gibbs_action_span():.3f}",
            "FAIL-SCALE-FREE",
        ),
        FieldEquationAudit(
            "record field equation",
            "Leibniz functor + S,delta",
            "natural action+deletion",
            "P and do-response fixed",
            "physical S_D,delta open",
            "Einstein equation analogue",
            "THM-CONDITIONAL-FIELD-EQ",
        ),
    ]


def print_audits(rows: list[FieldEquationAudit]) -> None:
    print("sealed record field-equation campaign")
    print("-------------------------------------")
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
    print("v6 Paper 3 section 47: sealed record field-equation campaign")
    print("=" * 150)
    print_audits(audits())
    print()
    print("VERDICT")
    print("-------")
    print("The sealed Leibniz record process closes the finite kinematics, not the")
    print("dynamics.  Same atoms, U, roles, and restrictions admit different P laws,")
    print("different gamma, different beta, and different do-delete maps.")
    print()
    print("The finite positive theorem is conditional: once an intrinsic local record")
    print("action S_D is supplied, the RN/Gibbs variational law uniquely determines")
    print("P_D.  Deletion still requires an intrinsic natural deletion map delta_D.")
    print("The pair (S_D, delta_D) is the record field equation.  If either is chosen")
    print("externally, branch A-current is not physically closed.")


if __name__ == "__main__":
    main()
