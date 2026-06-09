"""
v6 Paper 3 section 43: RN action conservation campaign.

Question:
    Is RN action conservation an extra law, or is it forced by sealed measure
    composition?

Finite answer:
    In the finite sealed-measure setting it is forced.  If local record laws
    are probability measures over finite sealed diamonds, references compose
    by the same sealed gluing rule, and action is an additive function of
    Radon-Nikodym likelihood ratios, then the action density is log(dP/dU),
    up to one global unit.

    The resulting KL/RN action satisfies exact sealed conservation:

        D(P_XYZ || U_XYZ)
        =
        D(P_XYZ || G_Y P) + D(G_Y P || U_XYZ),

    where G_Y P = P_XY P_YZ/P_Y is the eventless glued law.  The first term is
    the seam residual I(X;Z|Y).  Non-log scores, noncompositional references,
    and local unit rescalings fail.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import log, sqrt

from v6_p3ac_screen_bridge_theorem_campaign import (
    Law3,
    bypass_law,
    marginal_xy,
    marginal_y,
    marginal_yz,
    markov_law,
    spins,
)


Vector = list[float]
Law2 = list[list[float]]


@dataclass(frozen=True)
class RNAudit:
    target: str
    data: str
    invariant: str
    positive: str
    obstruction: str
    value: str
    verdict: str


def normalize(law: Law3) -> Law3:
    total = sum(law.values())
    return {state: value / total for state, value in law.items()}


def uniform3() -> Law3:
    return {(x, y, z): 1.0 / 8.0 for x in (0, 1) for y in (0, 1) for z in (0, 1)}


def tilted_bypass_law(theta: float = 0.35) -> Law3:
    base = markov_law()
    return normalize(
        {
            state: value * (1.0 + theta * spins(state[0]) * spins(state[2]))
            for state, value in base.items()
        }
    )


def biased_noncompositional_ref(theta: float = 0.35) -> Law3:
    return normalize(
        {
            (x, y, z): 1.0 + theta * spins(x) * spins(y) * spins(z)
            for x in (0, 1)
            for y in (0, 1)
            for z in (0, 1)
        }
    )


def kl(p: Law3, q: Law3) -> float:
    return sum(value * log(value / q[state]) for state, value in p.items() if value > 0.0)


def kl2(p: Law2, q: Law2) -> float:
    return sum(
        p[i][j] * log(p[i][j] / q[i][j])
        for i in range(2)
        for j in range(2)
        if p[i][j] > 0.0
    )


def kl1(p: Vector, q: Vector) -> float:
    return sum(pi * log(pi / qi) for pi, qi in zip(p, q) if pi > 0.0)


def glue_y(p: Law3) -> Law3:
    pxy = marginal_xy(p)
    pyz = marginal_yz(p)
    py = marginal_y(p)
    return {
        (x, y, z): pxy[x][y] * pyz[y][z] / py[y]
        for x in (0, 1)
        for y in (0, 1)
        for z in (0, 1)
    }


def marginal_xz(p: Law3) -> Law2:
    return [
        [sum(value for (a, _y, b), value in p.items() if a == x and b == z) for z in (0, 1)]
        for x in (0, 1)
    ]


def reference_xy() -> Law2:
    return [[0.25, 0.25], [0.25, 0.25]]


def reference_y() -> Vector:
    return [0.5, 0.5]


def chain_conservation_error(p: Law3, u: Law3) -> float:
    g = glue_y(p)
    return abs(kl(p, u) - kl(p, g) - kl(g, u))


def local_bridge_action_error(p: Law3) -> float:
    g = glue_y(p)
    pxy = marginal_xy(p)
    pyz = marginal_yz(p)
    py = marginal_y(p)
    # For the uniform compositional reference, the glued action equals the
    # inclusion-exclusion action of adjacent bridges.
    local = kl2(pxy, reference_xy()) + kl2(pyz, reference_xy()) - kl1(py, reference_y())
    return abs(kl(g, uniform3()) - local)


def nonlinear_score_error(p: Law3) -> float:
    g = glue_y(p)
    total = sqrt(kl(p, uniform3()))
    seam = sqrt(kl(p, g))
    glued = sqrt(kl(g, uniform3()))
    return abs(total - seam - glued)


def local_scale_error(p: Law3, seam_scale: float = 1.7, glued_scale: float = 0.8) -> float:
    g = glue_y(p)
    total = kl(p, uniform3())
    seam = seam_scale * kl(p, g)
    glued = glued_scale * kl(g, uniform3())
    return abs(total - seam - glued)


def global_scale_error(p: Law3, scale: float = 1.4426950408889634) -> float:
    g = glue_y(p)
    return abs(scale * kl(p, uniform3()) - scale * kl(p, g) - scale * kl(g, uniform3()))


def cauchy_error(kind: str) -> float:
    values = (0.55, 0.8, 1.25, 1.9)

    def f(value: float) -> float:
        if kind == "log":
            return log(value)
        if kind == "linear":
            return value - 1.0
        if kind == "sqrtlog":
            return sqrt(abs(log(value)))
        if kind == "squarelog":
            return log(value) ** 2
        raise ValueError(kind)

    return max(abs(f(a * b) - f(a) - f(b)) for a in values for b in values)


def product_law(p: Vector, q: Vector) -> Law2:
    return [[pi * qj for qj in q] for pi in p]


def rn_product_error() -> float:
    p1 = [0.35, 0.65]
    u1 = [0.50, 0.50]
    p2 = [0.20, 0.80]
    u2 = [0.45, 0.55]
    joint_p = product_law(p1, p2)
    joint_u = product_law(u1, u2)
    return abs(kl2(joint_p, joint_u) - kl1(p1, u1) - kl1(p2, u2))


def action_values(p: Law3) -> tuple[float, float, float]:
    g = glue_y(p)
    seam = kl(p, g)
    glued = kl(g, uniform3())
    total = kl(p, uniform3())
    return total, seam, glued


def audits() -> list[RNAudit]:
    markov = markov_law()
    bypass = tilted_bypass_law()
    total, seam, glued = action_values(bypass)
    noncomp_ref = biased_noncompositional_ref()
    return [
        RNAudit(
            "RN product origin",
            "independent sealed product",
            "d(P1xP2)/d(U1xU2)",
            "RN densities multiply",
            "log turns product into sum",
            f"add error={rn_product_error():.1e}",
            "PASS-RN-MULTIPLICATIVE",
        ),
        RNAudit(
            "log uniqueness",
            "likelihood ratios",
            "f(ab)=f(a)+f(b)",
            f"log error={cauchy_error('log'):.1e}",
            f"linear error={cauchy_error('linear'):.3f}",
            "only c log survives",
            "PASS-LOG-UNIQUE",
        ),
        RNAudit(
            "eventless conservation",
            "Markov seam",
            "D(P||U)=D(P||G)+D(G||U)",
            f"error={chain_conservation_error(markov, uniform3()):.1e}",
            "seam term vanishes",
            "exact eventless action",
            "PASS-RN-CONSERVATION",
        ),
        RNAudit(
            "eventful conservation",
            "hidden bypass",
            "total=seam+glued",
            f"total={total:.6f}",
            f"seam={seam:.6f}; glued={glued:.6f}",
            f"error={chain_conservation_error(bypass, uniform3()):.1e}",
            "PASS-RN-SPLIT",
        ),
        RNAudit(
            "local bridge action",
            "glued law",
            "XY+YZ-Y inclusion",
            f"error={local_bridge_action_error(bypass):.1e}",
            "requires compositional U",
            "local action account",
            "PASS-LOCAL-ACTION",
        ),
        RNAudit(
            "non-log score",
            "sqrt KL",
            "try additive score",
            f"error={nonlinear_score_error(bypass):.6f}",
            "breaks conservation",
            "score not action",
            "FAIL-NONLOG-ACTION",
        ),
        RNAudit(
            "local unit scales",
            "role/seam scales",
            "scale terms separately",
            f"error={local_scale_error(bypass):.6f}",
            "local units create/erase action",
            "only global unit allowed",
            "FAIL-LOCAL-UNITS",
        ),
        RNAudit(
            "global unit convention",
            "bits vs nats",
            "one global scale",
            f"error={global_scale_error(bypass):.1e}",
            "unit not physical",
            "global convention only",
            "PASS-GLOBAL-UNIT",
        ),
        RNAudit(
            "bad reference",
            "noncompositional U",
            "triple-biased reference",
            f"error={chain_conservation_error(bypass, noncomp_ref):.6f}",
            "reference carries hidden seam action",
            "U must compose",
            "FAIL-NONCOMPOSITIONAL-U",
        ),
        RNAudit(
            "branch verdict",
            "sealed measure functor",
            "compositional U + log RN",
            "action conservation theorem",
            "physical status of functor remains",
            "RN action not separate axiom",
            "A-CURRENT-BASE-CANDIDATE",
        ),
    ]


def print_audits(rows: list[RNAudit]) -> None:
    print("RN action conservation campaign")
    print("-------------------------------")
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
    print("v6 Paper 3 section 43: RN action conservation campaign")
    print("=" * 150)
    print_audits(audits())
    print()
    print("VERDICT")
    print("-------")
    print("RN action conservation is a theorem of finite sealed measure composition")
    print("once the reference law is compositional and action density is additive in")
    print("Radon-Nikodym likelihood ratios.  RN derivatives multiply under product")
    print("composition, and the logarithm is the unique additive regraduation up to")
    print("one global unit.")
    print()
    print("The remaining primitive is not a separate action-conservation axiom.  It")
    print("is the sealed measure functor with a canonical compositional reference U.")
    print("If U or the measure functor is supplied externally, branch A-current is")
    print("still conditional.  If they are the base ontology, RN action conservation")
    print("is derived.")


if __name__ == "__main__":
    main()
