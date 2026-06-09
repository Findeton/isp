"""
v6 Paper 3 section 49: stronger record-field rigidity campaign.

Question:
    Do the stronger plausible principles close Branch A-full by deriving a
    unique natural record field equation (S_D, delta_D)?

Stronger candidates tested:
    1. natural transformation uniqueness;
    2. RN cocycle rigidity;
    3. deletion-action duality;
    4. refinement/anomaly cancellation;
    5. self-consistency fixed points;
    6. gravity/screen response rigidity;
    7. simultaneous consistency of the above finite constraints.

Finite answer:
    The campaign finds no finite uniqueness theorem.  Each candidate either
    gives a conditional positive if an extra object is supplied, or leaves a
    visible parameter family.  The clean remaining target is a genuine
    rigidity theorem: the natural action cohomology must be one-dimensional
    after all physical constraints, the anomaly equations must isolate its
    scale, and deletion must be generated uniquely by the same action.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import exp, log


Vector = list[float]


@dataclass(frozen=True)
class RigidityAudit:
    target: str
    data: str
    invariant: str
    positive: str
    obstruction: str
    value: str
    verdict: str


def atoms(n: int) -> list[tuple[int, ...]]:
    return list(product((0, 1), repeat=n))


def l1(left: Vector, right: Vector) -> float:
    return sum(abs(a - b) for a, b in zip(left, right))


def normalize(weights: Vector) -> Vector:
    total = sum(weights)
    return [weight / total for weight in weights]


def event_count(atom: tuple[int, ...]) -> int:
    return sum(atom)


def transition_count(atom: tuple[int, ...]) -> int:
    return sum(1 for left, right in zip(atom, atom[1:]) if left != right)


def feature_rank(n: int = 5) -> int:
    # Nonconstant local scalar features in the binary chain: event count and
    # transition count are independent.  Constant terms are normalization.
    rows = [[float(event_count(atom)), float(transition_count(atom))] for atom in atoms(n)]
    # Rank of two columns by checking non-collinearity after centering.
    means = [sum(row[j] for row in rows) / len(rows) for j in range(2)]
    centered = [[row[j] - means[j] for j in range(2)] for row in rows]
    det_witness = 0.0
    for a in centered:
        for b in centered:
            det_witness = max(det_witness, abs(a[0] * b[1] - a[1] * b[0]))
    return 2 if det_witness > 1.0e-12 else 1


def bernoulli_log_rn(atom: tuple[int, ...], p: float) -> float:
    n = len(atom)
    k = event_count(atom)
    probability = (p**k) * ((1.0 - p) ** (n - k))
    reference = 2.0 ** (-n)
    return log(probability / reference)


def cocycle_product_error(p: float = 0.3) -> float:
    max_error = 0.0
    for left in atoms(3):
        for right in atoms(2):
            joined = left + right
            max_error = max(
                max_error,
                abs(bernoulli_log_rn(joined, p) - bernoulli_log_rn(left, p) - bernoulli_log_rn(right, p)),
            )
    return max_error


def cocycle_family_span() -> float:
    values_low = [bernoulli_log_rn(atom, 0.2) for atom in atoms(5)]
    values_high = [bernoulli_log_rn(atom, 0.8) for atom in atoms(5)]
    return max(abs(a - b) for a, b in zip(values_low, values_high))


def correlated_joint() -> list[list[float]]:
    return [[0.45, 0.05], [0.05, 0.45]]


def deletion_action_duality_gap() -> float:
    joint = correlated_joint()
    marginal_y = [joint[0][0] + joint[1][0], joint[0][1] + joint[1][1]]
    row0 = sum(joint[0])
    clamp_y = [joint[0][0] / row0, joint[0][1] / row0]
    return l1(marginal_y, clamp_y)


def markov_law(n: int, q: float) -> Vector:
    law = []
    for atom in atoms(n):
        probability = 0.5
        for left, right in zip(atom, atom[1:]):
            probability *= q if left != right else (1.0 - q)
        law.append(probability)
    return law


def markov_projective_error(q: float = 0.25) -> float:
    n = 5
    law_n = markov_law(n, q)
    law_m = markov_law(n - 1, q)
    pushed = [0.0] * (2 ** (n - 1))
    index = {atom: i for i, atom in enumerate(atoms(n - 1))}
    for probability, atom in zip(law_n, atoms(n)):
        pushed[index[atom[:-1]]] += probability
    return l1(pushed, law_m)


def beta_inverse_proxy(q: float) -> float:
    corr = abs(1.0 - 2.0 * q)
    if corr <= 0.0:
        return 0.0
    return -1.0 / log(corr)


def anomaly_free_beta_span() -> float:
    values = [beta_inverse_proxy(q) for q in (0.1, 0.25, 0.4)]
    return max(values) - min(values)


def logistic(a: float, x: float) -> float:
    return 1.0 / (1.0 + exp(-a * (x - 0.5)))


def fixed_points(a: float) -> list[float]:
    roots: list[float] = []
    samples = 1000
    prev_x = 0.0
    prev_f = logistic(a, prev_x) - prev_x
    for i in range(1, samples + 1):
        x = i / samples
        f = logistic(a, x) - x
        if abs(f) < 1.0e-6:
            roots.append(x)
        elif prev_f * f < 0.0:
            lo, hi = prev_x, x
            for _ in range(60):
                mid = 0.5 * (lo + hi)
                fm = logistic(a, mid) - mid
                if (logistic(a, lo) - lo) * fm <= 0.0:
                    hi = mid
                else:
                    lo = mid
            roots.append(0.5 * (lo + hi))
        prev_x, prev_f = x, f
    unique: list[float] = []
    for root in roots:
        if not unique or abs(root - unique[-1]) > 1.0e-4:
            unique.append(root)
    return unique


def fixed_point_count_span() -> int:
    counts = [len(fixed_points(a)) for a in (2.0, 8.0)]
    return max(counts) - min(counts)


def width_objective(ell: float, c: float) -> float:
    # A toy information/cost objective with heat at small width and
    # gravity/screen blur at large width.  The response coefficient c moves
    # the optimum unless it is derived.
    info = ell
    cost = 1.0 + 0.12 / (ell**4) + c * (ell**2)
    return info / cost


def optimum_width(c: float) -> float:
    best_ell = 0.5
    best_value = width_objective(best_ell, c)
    for i in range(1, 3501):
        ell = 0.5 + i * (3.5 / 3500)
        value = width_objective(ell, c)
        if value > best_value:
            best_ell, best_value = ell, value
    return best_ell


def gravity_response_beta_span() -> float:
    betas = [1.0 / optimum_width(c) for c in (0.03, 0.08, 0.20)]
    return max(betas) - min(betas)


def simultaneous_family_span() -> float:
    # Detailed balance, no-silent Markov seams, projective consistency, and
    # role-blind U all hold for this q-family.  The memory scale still varies.
    return anomaly_free_beta_span()


def action_generated_deletion_condition_gap() -> float:
    # If deletion is required to be the KL projection, marginal deletion is
    # selected; if deletion is required to remove the positive branch, clamp
    # deletion is selected.  Both can be phrased as action-generated unless the
    # generator condition is fixed.
    return deletion_action_duality_gap()


def audits() -> list[RigidityAudit]:
    return [
        RigidityAudit(
            "natural action space",
            "binary record functor",
            "natural local scalars",
            f"rank={feature_rank()}",
            "rank greater than 1",
            "event+transition",
            "FAIL-NATURAL-NOT-UNIQUE",
        ),
        RigidityAudit(
            "RN cocycle family",
            "Bernoulli products",
            "A(xy)=A(x)+A(y)",
            f"cocycle err={cocycle_product_error():.1e}",
            "p parameter free",
            f"span={cocycle_family_span():.3f}",
            "FAIL-COCYCLE-NOT-RIGID",
        ),
        RigidityAudit(
            "deletion-action duality",
            "same correlated P",
            "action-generated deletion",
            "two generators natural",
            "generator condition free",
            f"response gap={deletion_action_duality_gap():.3f}",
            "FAIL-DUALITY-NOT-UNIQUE",
        ),
        RigidityAudit(
            "anomaly cancellation",
            "stationary Markov family",
            "projective consistency",
            f"push err={markov_projective_error():.1e}",
            "q parameter survives",
            f"beta span={anomaly_free_beta_span():.3f}",
            "FAIL-ANOMALY-NOT-ENOUGH",
        ),
        RigidityAudit(
            "self-consistency",
            "tests depend on P",
            "p=F_a(p)",
            "fixed points exist",
            "map/slope free",
            f"count span={fixed_point_count_span()}",
            "FAIL-FIXED-POINT-FREE",
        ),
        RigidityAudit(
            "gravity response",
            "screen/work objective",
            "info per cost",
            "interior optima",
            "response coeff free",
            f"beta span={gravity_response_beta_span():.3f}",
            "FAIL-GRAVITY-COEFF-FREE",
        ),
        RigidityAudit(
            "simultaneous constraints",
            "DB+Markov+cofinal+U",
            "all consistency tests",
            "family survives",
            "memory scale free",
            f"beta span={simultaneous_family_span():.3f}",
            "FAIL-COMBINED-FAMILY",
        ),
        RigidityAudit(
            "action-deletion generator",
            "same S/P",
            "delete from action",
            "projection or clamp",
            "generator convention free",
            f"gap={action_generated_deletion_condition_gap():.3f}",
            "FAIL-GENERATOR-FREE",
        ),
        RigidityAudit(
            "rigidity theorem target",
            "sealed Leibniz process",
            "H^1 unique + anomaly isolate + deletion generated",
            "would close A-full",
            "not found finitely",
            "target named",
            "OPEN-RIGIDITY-THEOREM",
        ),
    ]


def print_audits(rows: list[RigidityAudit]) -> None:
    print("stronger record-field rigidity campaign")
    print("---------------------------------------")
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
    print("v6 Paper 3 section 49: stronger record-field rigidity campaign")
    print("=" * 150)
    print_audits(audits())
    print()
    print("VERDICT")
    print("-------")
    print("The stronger candidate principles do not produce a finite uniqueness")
    print("theorem.  Natural local actions have more than one generator, RN cocycles")
    print("come in parameter families, anomaly cancellation and simultaneous Markov")
    print("consistency leave beta free, self-consistency depends on the chosen map,")
    print("gravity/screen response depends on a coefficient, and deletion-action")
    print("duality depends on a generator convention.")
    print()
    print("Truth boundary: Branch A-full needs a genuine rigidity theorem tying all")
    print("three facts at once: one-dimensional natural action cohomology, isolated")
    print("anomaly-free scale, and a unique deletion generator.  This finite campaign")
    print("does not find it; it names the exact theorem that would be needed.")


if __name__ == "__main__":
    main()
