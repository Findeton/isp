"""
v6 Paper 3 section 48: candidate record field-equation campaign.

Question:
    Can Einsteinian invariance principles derive the actual record field
    equation (S_D, delta_D), rather than merely requiring one?

Finite answer:
    The usual candidates do not close the dynamics:

      * full relabelling symmetry selects only the trivial uniform law;
      * event-count actions leave a free chemical-potential coefficient;
      * local pair/Markov actions leave free field and memory coefficients;
      * detailed balance, no-silent seams, and projective consistency leave
        continuous transition families;
      * finite criticality/self-duality is model-specific and not a general
        sealed-record invariant;
      * natural deletion admits multiple natural intervention maps.

    Conditional positive theorem:
      Branch A-current needs a unique natural record field action: a fixed
      scalar functional S_D and deletion natural transformation delta_D
      derived from the sealed Leibniz process itself.  The finite campaign
      finds no such uniqueness theorem from the listed invariances.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import exp, log


Vector = list[float]


@dataclass(frozen=True)
class CandidateAudit:
    target: str
    data: str
    invariant: str
    positive: str
    obstruction: str
    value: str
    verdict: str


def normalize(weights: Vector) -> Vector:
    total = sum(weights)
    return [weight / total for weight in weights]


def l1(left: Vector, right: Vector) -> float:
    return sum(abs(a - b) for a, b in zip(left, right))


def atoms(n: int) -> list[tuple[int, ...]]:
    return list(product((0, 1), repeat=n))


def event_count(atom: tuple[int, ...]) -> int:
    return sum(atom)


def transitions(atom: tuple[int, ...]) -> int:
    return sum(1 for left, right in zip(atom, atom[1:]) if left != right)


def gibbs_from_features(n: int, h: float = 0.0, j: float = 0.0) -> Vector:
    weights = []
    for atom in atoms(n):
        action = h * event_count(atom) + j * transitions(atom)
        weights.append(exp(-action))
    return normalize(weights)


def event_density(n: int, law: Vector) -> float:
    return sum(prob * event_count(atom) / n for prob, atom in zip(law, atoms(n)))


def transition_density(n: int, law: Vector) -> float:
    return sum(prob * transitions(atom) / (n - 1) for prob, atom in zip(law, atoms(n)))


def relabel_invariant_action_gap(n: int = 4) -> float:
    # Full permutation of all atoms admits only constant action if no readout
    # structure is distinguished.
    law = normalize([exp(-0.0)] * (2 ** n))
    return l1(law, [1.0 / (2 ** n)] * (2 ** n))


def event_count_gamma_span(n: int = 8) -> float:
    densities = [event_density(n, gibbs_from_features(n, h=h)) for h in (-1.0, 0.0, 1.0)]
    return max(densities) - min(densities)


def pair_memory_span(n: int = 8) -> float:
    memories = [transition_density(n, gibbs_from_features(n, j=j)) for j in (-1.0, 0.0, 1.0)]
    return max(memories) - min(memories)


def local_feature_dimension() -> int:
    # On a binary nearest-neighbor chain with translation-invariant one- and
    # two-site terms, the role-preserving local scalar feature space contains:
    # constant, event count, transition count.  Two nonconstant coefficients
    # remain before adding a field equation.
    return 3


def stationary_markov_transition(flip: float) -> list[list[float]]:
    return [[1.0 - flip, flip], [flip, 1.0 - flip]]


def detailed_balance_error(flip: float) -> float:
    pi = [0.5, 0.5]
    k = stationary_markov_transition(flip)
    return abs(pi[0] * k[0][1] - pi[1] * k[1][0])


def detailed_balance_span() -> float:
    flips = (0.1, 0.25, 0.4)
    return max(abs((1.0 - 2.0 * q)) for q in flips) - min(abs((1.0 - 2.0 * q)) for q in flips)


def cmi_markov(flip: float) -> float:
    # X-Y-Z stationary Markov chain.
    law = {}
    for x, y, z in atoms(3):
        p = 0.5
        p *= flip if x != y else (1.0 - flip)
        p *= flip if y != z else (1.0 - flip)
        law[(x, y, z)] = p
    p_xy: dict[tuple[int, int], float] = {}
    p_yz: dict[tuple[int, int], float] = {}
    p_y: dict[int, float] = {}
    for (x, y, z), p in law.items():
        p_xy[(x, y)] = p_xy.get((x, y), 0.0) + p
        p_yz[(y, z)] = p_yz.get((y, z), 0.0) + p
        p_y[y] = p_y.get(y, 0.0) + p
    return sum(
        p * log(p * p_y[y] / (p_xy[(x, y)] * p_yz[(y, z)]))
        for (x, y, z), p in law.items()
        if p > 0.0
    )


def projective_pair_error(n: int = 5, h: float = 0.6, j: float = 0.7) -> float:
    # Fixed-boundary-free finite nearest-neighbor Gibbs measures are not exactly
    # projective under marginalization unless they are represented by a
    # compatible transfer process.  This tests whether "local action form" alone
    # already gives cofinal consistency.
    law_n = gibbs_from_features(n, h, j)
    law_m = gibbs_from_features(n - 1, h, j)
    pushed = [0.0] * (2 ** (n - 1))
    index = {atom: i for i, atom in enumerate(atoms(n - 1))}
    for p, atom in zip(law_n, atoms(n)):
        pushed[index[atom[:-1]]] += p
    return l1(pushed, law_m)


def transfer_projective_error(flip: float = 0.25) -> float:
    # The stationary Markov transfer law is projective.
    n = 5
    law_n = []
    for atom in atoms(n):
        p = 0.5
        for left, right in zip(atom, atom[1:]):
            p *= flip if left != right else (1.0 - flip)
        law_n.append(p)
    law_m = []
    for atom in atoms(n - 1):
        p = 0.5
        for left, right in zip(atom, atom[1:]):
            p *= flip if left != right else (1.0 - flip)
        law_m.append(p)
    pushed = [0.0] * (2 ** (n - 1))
    index = {atom: i for i, atom in enumerate(atoms(n - 1))}
    for p, atom in zip(law_n, atoms(n)):
        pushed[index[atom[:-1]]] += p
    return l1(pushed, law_m)


def finite_criticality_span() -> float:
    # In a 1D finite binary chain, the transition susceptibility is smooth and
    # its broad maximum shifts with the scanned window.  Here we report that
    # the finite transition density changes substantially across candidate J.
    values = [transition_density(10, gibbs_from_features(10, j=j)) for j in (0.2, 0.8, 1.4)]
    return max(values) - min(values)


def deletion_gap() -> float:
    # Same observational correlated law; two role-blind natural interventions:
    # marginalize deleted variable, or condition it to the no-event value.
    joint = [[0.45, 0.05], [0.05, 0.45]]
    marginal_y = [joint[0][0] + joint[1][0], joint[0][1] + joint[1][1]]
    row0 = sum(joint[0])
    clamp_y = [joint[0][0] / row0, joint[0][1] / row0]
    return l1(marginal_y, clamp_y)


def minimum_disturbance_metric_span() -> float:
    # Under total variation, marginal deletion may be closest to preserving Y;
    # under a metric that penalizes event-branch survival, clamp deletion can be
    # preferred.  The metric choice is extra structure.
    return deletion_gap()


def action_scale_gamma_span(n: int = 8) -> float:
    densities = [event_density(n, gibbs_from_features(n, h=scale)) for scale in (0.2, 0.8, 1.6)]
    return max(densities) - min(densities)


def audits() -> list[CandidateAudit]:
    return [
        CandidateAudit(
            "full relabelling",
            "bare Leibniz atoms",
            "all atom permutations",
            f"uniform gap={relabel_invariant_action_gap():.1e}",
            "only constant action",
            "P=U",
            "PASS-TRIVIAL-ONLY",
        ),
        CandidateAudit(
            "event-count action",
            "event readout E",
            "S=h sum E",
            "local/additive",
            "h free",
            f"gamma span={event_count_gamma_span():.3f}",
            "FAIL-FREE-H",
        ),
        CandidateAudit(
            "pair-memory action",
            "nearest restrictions",
            "S=J transitions",
            "local/role-blind",
            "J free",
            f"memory span={pair_memory_span():.3f}",
            "FAIL-FREE-J",
        ),
        CandidateAudit(
            "local feature space",
            "binary chain",
            "translation local scalars",
            f"dim={local_feature_dimension()}",
            "two nonconstant coefficients",
            "needs dynamics",
            "FAIL-FEATURE-SPACE",
        ),
        CandidateAudit(
            "detailed balance",
            "stationary U",
            "pi_i K_ij=pi_j K_ji",
            f"err={detailed_balance_error(0.25):.1e}",
            "flip parameter free",
            f"corr span={detailed_balance_span():.3f}",
            "FAIL-DB-NOT-ENOUGH",
        ),
        CandidateAudit(
            "no-silent seam",
            "Markov X-Y-Z",
            "I(X;Z|Y)=0",
            f"CMI={cmi_markov(0.25):.1e}",
            "transition parameter free",
            "family survives",
            "FAIL-SEAM-FAMILY",
        ),
        CandidateAudit(
            "local Gibbs form",
            "finite chain action",
            "nearest-neighbor S",
            "well-defined finite P",
            "not automatically cofinal",
            f"push err={projective_pair_error():.3f}",
            "FAIL-LOCAL-NOT-COFINAL",
        ),
        CandidateAudit(
            "transfer process",
            "stationary Markov K",
            "cofinal consistency",
            f"push err={transfer_projective_error():.1e}",
            "K parameter free",
            "q free",
            "PASS-COFINAL-BUT-FREE",
        ),
        CandidateAudit(
            "finite criticality",
            "1D finite chain",
            "susceptibility/transition scan",
            "detects response",
            "no isolated universal point",
            f"response span={finite_criticality_span():.3f}",
            "FAIL-CRITICALITY-FREE",
        ),
        CandidateAudit(
            "natural deletion",
            "same observed P",
            "role-blind maps",
            "multiple natural maps",
            "no unique do-law",
            f"gap={deletion_gap():.3f}",
            "FAIL-DELETE-FREE",
        ),
        CandidateAudit(
            "minimal disturbance",
            "delete response",
            "minimize change",
            "can pick a map",
            "metric/cost free",
            f"metric span={minimum_disturbance_metric_span():.3f}",
            "FAIL-METRIC-FREE",
        ),
        CandidateAudit(
            "action scale",
            "same action form",
            "S -> cS",
            "each law valid",
            "global scale free",
            f"gamma span={action_scale_gamma_span():.3f}",
            "FAIL-SCALE-FREE",
        ),
        CandidateAudit(
            "unique field equation",
            "sealed Leibniz process",
            "natural S_D and delta_D",
            "would close branch A",
            "not derived by tested invariants",
            "open theorem",
            "OPEN-UNIQUE-FIELD-EQ",
        ),
    ]


def print_audits(rows: list[CandidateAudit]) -> None:
    print("candidate record field-equation campaign")
    print("----------------------------------------")
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
    print("v6 Paper 3 section 48: candidate record field-equation campaign")
    print("=" * 150)
    print_audits(audits())
    print()
    print("VERDICT")
    print("-------")
    print("The tested Einsteinian invariances do not derive a unique (S_D, delta_D).")
    print("Full relabelling gives only the trivial uniform law.  Once event/readout")
    print("structure is admitted, local additive actions leave free coefficients,")
    print("Markov/no-silent/detailed-balance/cofinality leave free transition laws,")
    print("and natural deletion leaves multiple intervention maps.")
    print()
    print("The remaining branch-A theorem must derive a unique natural local action")
    print("and deletion transformation from the sealed Leibniz process itself.  This")
    print("campaign finds no finite uniqueness theorem from the listed principles.")


if __name__ == "__main__":
    main()
