"""
v6 Paper 3 section 57: invariant principle campaign for P_D.

Question:
    Is there an invariant physical principle that fixes the positive sealed
    record law P_D?

Finite answer:
    Not from the tested principles without supplying dynamical data.

    The campaign distinguishes two cases:

      * principles with no nontrivial intrinsic constraint select the uniform
        eventless law;
      * principles that select a nontrivial law require a supplied constraint,
        action, transition rate, duality map, moment, source, code, or empirical
        process.

    Thus the previous reductions are not failures of technique.  P_D is the
    dynamical content.  Branch A-full requires an actual process-law principle
    that outputs P_D, not another covariance or optimization rule.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import asinh, atanh, exp, log, tanh


Atom = tuple[int, ...]
Vector = list[float]


@dataclass(frozen=True)
class PrincipleAudit:
    target: str
    principle: str
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


def uniform(n: int) -> Vector:
    return [1.0 / (2**n)] * (2**n)


def l1(left: Vector, right: Vector) -> float:
    return sum(abs(a - b) for a, b in zip(left, right))


def entropy(law: Vector) -> float:
    return -sum(prob * log(prob) for prob in law if prob > 0.0)


def chain_law(j_left: float, j_right: float, h_mid: float = 0.0) -> Vector:
    return law_from_potential(
        3,
        lambda atom: j_left * atom[0] * atom[1]
        + j_right * atom[1] * atom[2]
        + h_mid * atom[1],
    )


def bridge_law(theta: float) -> Vector:
    return law_from_potential(2, lambda atom: theta * atom[0] * atom[1])


def moment_xz(law: Vector) -> float:
    return sum(prob * atom[0] * atom[-1] for prob, atom in zip(law, atoms(2)))


def theta_for_corr(corr: float) -> float:
    return atanh(corr)


def maxent_constraint_span() -> tuple[float, float, float]:
    laws = []
    thetas = []
    for corr in (0.2, 0.6, 0.9):
        theta = theta_for_corr(corr)
        thetas.append(theta)
        laws.append(bridge_law(theta))
    return min(thetas), max(thetas), max(l1(a, b) for a in laws for b in laws)


def locality_markov_span() -> float:
    laws = [chain_law(0.2, 0.2), chain_law(0.8, 0.8), chain_law(0.4, 1.0)]
    return max(l1(a, b) for a in laws for b in laws)


def symmetry_span() -> float:
    laws = [chain_law(j, j, 0.0) for j in (0.1, 0.7, 1.3)]
    return max(l1(a, b) for a in laws for b in laws)


def detailed_balance_span() -> float:
    # Any positive pi can be made reversible for a complete proposal by choosing
    # Metropolis-style rates.  Detailed balance alone therefore reads a supplied
    # pi/action.
    laws = [bridge_law(theta) for theta in (0.2, 1.0, 1.8)]
    return max(l1(a, b) for a in laws for b in laws)


def decimation(theta: float) -> float:
    return atanh(tanh(theta) ** 2)


def rg_fixed_values() -> tuple[float, float, float]:
    zero_residual = abs(decimation(0.0) - 0.0)
    one_residual = abs(decimation(1.0) - 1.0)
    big_residual = abs(decimation(5.0) - 5.0)
    return zero_residual, one_residual, big_residual


def self_dual_value() -> float:
    return 0.5 * asinh(1.0)


def max_caliber_span() -> tuple[float, float]:
    # Two-state stationary path law with flip probability q.  Max caliber fixes
    # q only when a mean flip count is supplied.
    def path_law(q: float) -> Vector:
        # paths of length 3 from a uniform initial bit
        weights = []
        for path in product((0, 1), repeat=3):
            flips = int(path[0] != path[1]) + int(path[1] != path[2])
            weights.append(0.5 * (q ** flips) * ((1.0 - q) ** (2 - flips)))
        return weights

    laws = [path_law(q) for q in (0.1, 0.3, 0.7)]
    return 0.5, max(l1(a, b) for a in laws for b in laws)


def least_action_span() -> float:
    # With a supplied source/correlation target, least action gives a member;
    # changing the source changes the member.
    laws = [bridge_law(theta_for_corr(corr)) for corr in (0.25, 0.55, 0.85)]
    return max(l1(a, b) for a in laws for b in laws)


def code_prior_span() -> tuple[float, float]:
    # A finite code-grid prior: "smallest nonzero coupling" depends on grid.
    laws = [bridge_law(epsilon) for epsilon in (0.01, 0.10)]
    return l1(laws[0], laws[1]), entropy(laws[0])


def empirical_error() -> tuple[float, float]:
    law = chain_law(0.5, -0.2)
    errors = []
    for samples in (100, 10000):
        counts = [round(samples * prob) for prob in law]
        counts[0] += samples - sum(counts)
        empirical = [count / samples for count in counts]
        errors.append(l1(empirical, law))
    return errors[0], errors[1]


def gibbs_variational_span() -> float:
    # Minimizing E[A]-H gives P propto exp(-A), but A is exactly the supplied
    # action/process data.
    laws = []
    for theta in (0.2, 0.8, 1.4):
        action = [-theta * atom[0] * atom[1] for atom in atoms(2)]
        weights = [exp(-value) for value in action]
        laws.append(normalize(weights))
    return max(l1(a, b) for a in laws for b in laws)


def score_geometry_closure_dependency() -> str:
    return "P_D input"


def audits() -> list[PrincipleAudit]:
    theta_min, theta_max, maxent_span = maxent_constraint_span()
    q_uniform, caliber_span = max_caliber_span()
    rg0, rg1, rg_big = rg_fixed_values()
    code_span, simple_entropy = code_prior_span()
    err_100, err_10000 = empirical_error()
    return [
        PrincipleAudit(
            "maximum entropy",
            "maximize H(P)",
            "unique law without constraints",
            "uniform/eventless",
            f"H={entropy(uniform(3)):.3f}",
            "FAIL-TRIVIAL",
        ),
        PrincipleAudit(
            "max entropy with moment",
            "fix E[xz]",
            "unique exponential law",
            "moment/correlation supplied",
            f"theta {theta_min:.3f}->{theta_max:.3f}, span={maxent_span:.3f}",
            "COND-MOMENT",
        ),
        PrincipleAudit(
            "local Markov blanket",
            "P factorizes over cliques",
            "collar/locality structure fixed",
            "clique couplings free",
            f"P span={locality_markov_span():.3f}",
            "FAIL-COUPLINGS",
        ),
        PrincipleAudit(
            "internal symmetry",
            "left/right and flip symmetries",
            "reduces parameters",
            "symmetric coupling remains free",
            f"P span={symmetry_span():.3f}",
            "FAIL-SYMMETRY",
        ),
        PrincipleAudit(
            "detailed balance",
            "reversible sealed transport",
            "consistent rates exist",
            "stationary law/action supplied",
            f"P span={detailed_balance_span():.3f}",
            "FAIL-READS-PI",
        ),
        PrincipleAudit(
            "RG/refinement fixed point",
            "1D decimation theta'=atanh(tanh^2 theta)",
            "uniform fixed point exact",
            "finite nontrivial fixed point absent",
            f"res {rg0:.1e}/{rg1:.3f}/{rg_big:.3f}",
            "FAIL-TRIVIAL-RG",
        ),
        PrincipleAudit(
            "self-duality",
            "sinh(2K)=1",
            "selects K in chosen model",
            "duality/action family supplied",
            f"Kc={self_dual_value():.4f}",
            "COND-FAMILY",
        ),
        PrincipleAudit(
            "maximum caliber",
            "maximize path entropy",
            "uniform q if unconstrained",
            "flip count/current supplied",
            f"q0={q_uniform:.1f}, span={caliber_span:.3f}",
            "COND-PATH-CONSTRAINT",
        ),
        PrincipleAudit(
            "least record action",
            "minimize work norm",
            "zero law without source",
            "nonzero source/correlation supplied",
            f"P span={least_action_span():.3f}",
            "COND-SOURCE",
        ),
        PrincipleAudit(
            "algorithmic simplicity",
            "shortest code / smallest coupling",
            "uniform or grid-minimal law",
            "code/grid not invariant",
            f"grid span={code_span:.3f}, H={simple_entropy:.3f}",
            "FAIL-CODE",
        ),
        PrincipleAudit(
            "Gibbs variational",
            "minimize E[A]-H",
            "unique P for supplied A",
            "A is the process law in disguise",
            f"P span={gibbs_variational_span():.3f}",
            "PASS-IF-A-SUPPLIED",
        ),
        PrincipleAudit(
            "cofinal frequencies",
            "record-count convergence",
            "identifies actual P",
            "identification not derivation",
            f"L1 {err_100:.3f}->{err_10000:.3f}",
            "IDENT-NOT-DERIVE",
        ),
        PrincipleAudit(
            "score geometry",
            "derive packet from P,C",
            "closes downstream machinery",
            "requires P_D first",
            score_geometry_closure_dependency(),
            "DOWNSTREAM",
        ),
        PrincipleAudit(
            "principle no-go",
            "invariance/optimization only",
            "restricts or identifies P",
            "does not select nontrivial P_D",
            "families survive",
            "THM-P-PRINCIPLE-NO-GO",
        ),
    ]


def print_audits(rows: list[PrincipleAudit]) -> None:
    print("P_D invariant-principle campaign")
    print("--------------------------------")
    print(
        "target                    principle                                    positive result                  "
        "obstruction                         value                         verdict"
    )
    for row in rows:
        print(
            f"{row.target:25s} "
            f"{row.principle:44s} "
            f"{row.positive_result:32s} "
            f"{row.obstruction:35s} "
            f"{row.value:29s} "
            f"{row.verdict}"
        )


def main() -> None:
    print("=" * 150)
    print("v6 Paper 3 section 57: invariant physical principle for P_D")
    print("=" * 150)
    rows = audits()
    print_audits(rows)
    print()
    print("VERDICT")
    print("-------")
    print("The tested invariant principles do not derive a nontrivial positive sealed")
    print("record law P_D.  With no nontrivial constraint they select the uniform")
    print("eventless law.  When they select a nontrivial law, a moment, action,")
    print("coupling, transition statistic, duality map, code, source, or empirical")
    print("process has already been supplied.")
    print()
    print("Therefore P_D is not downstream of score geometry, Markov blankets,")
    print("cocycle/refinement consistency, or generic optimization.  It is the")
    print("dynamical law itself.  Branch A-full requires a new physical principle")
    print("that generates the process law, not merely a criterion that organizes a")
    print("law after it is given.")


if __name__ == "__main__":
    main()
