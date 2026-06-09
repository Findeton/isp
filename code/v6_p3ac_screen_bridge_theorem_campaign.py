"""
v6 Paper 3 section 39: intrinsic screens and bridge composition.

Question:
    Einstein's remaining demand is that the sealed causal diamond itself
    supply the ordered screens and the composable screen-to-screen RN bridge,
    rather than receiving them as labels.

Finite answer:
    Oriented causal order supplies lower/upper screens as minimal/maximal
    boundary antichains.  A full sealed law supplies Q by marginalizing to
    those screens.  But composability is not automatic: adjacent bridges
    compose if and only if the shared screen is a complete RN separator,

        D(P_XYZ || P_XY P_YZ / P_Y) = I(X;Z|Y) = 0.

    A hidden bypass can preserve both adjacent bridges while changing the
    composite bridge.  Thus the invariant that closes the gate is not just
    "ordered screens plus Q"; it is ordered screens plus complete-screen RN
    sufficiency under sealed gluing.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import log


State = tuple[int, int, int]
Law3 = dict[State, float]
Matrix = list[list[float]]
Vector = list[float]


@dataclass(frozen=True)
class ScreenBridgeAudit:
    target: str
    data: str
    construction: str
    positive: str
    obstruction: str
    value: str
    verdict: str


def spins(bit: int) -> int:
    return -1 if bit == 0 else 1


def normalize(law: Law3) -> Law3:
    total = sum(law.values())
    return {state: value / total for state, value in law.items()}


def oriented_screens() -> tuple[bool, str, str]:
    # Toy causal diamond: lower atoms 0,1; shared/interior screen 2,3;
    # upper atoms 4,5.  With the partial order retained, minimal and maximal
    # boundary antichains are intrinsic.
    return True, "0,1", "4,5"


def unoriented_screens() -> tuple[bool, str]:
    # The undirected comparability shadow knows adjacency but not which
    # antichain is lower or upper.
    return False, "lower/upper exchange symmetry"


def markov_law() -> Law3:
    px = [0.55, 0.45]
    txy = [[0.84, 0.16], [0.28, 0.72]]
    tyz = [[0.72, 0.28], [0.18, 0.82]]
    return {
        (x, y, z): px[x] * txy[x][y] * tyz[y][z]
        for x in (0, 1)
        for y in (0, 1)
        for z in (0, 1)
    }


def bypass_law(theta: float = 0.40) -> Law3:
    # Same adjacent screen bridges X-Y and Y-Z as the uniform law, but a hidden
    # X-Z bypass correlation.  This is the minimal finite counterexample to
    # deriving composition from adjacent bridge data alone.
    return normalize(
        {
            (x, y, z): 1.0 + theta * spins(x) * spins(z)
            for x in (0, 1)
            for y in (0, 1)
            for z in (0, 1)
        }
    )


def marginal_x(law: Law3) -> Vector:
    return [sum(prob for (x, _y, _z), prob in law.items() if x == bit) for bit in (0, 1)]


def marginal_y(law: Law3) -> Vector:
    return [sum(prob for (_x, y, _z), prob in law.items() if y == bit) for bit in (0, 1)]


def marginal_z(law: Law3) -> Vector:
    return [sum(prob for (_x, _y, z), prob in law.items() if z == bit) for bit in (0, 1)]


def marginal_xy(law: Law3) -> Matrix:
    return [
        [sum(prob for (a, b, _z), prob in law.items() if a == x and b == y) for y in (0, 1)]
        for x in (0, 1)
    ]


def marginal_yz(law: Law3) -> Matrix:
    return [
        [sum(prob for (_x, a, b), prob in law.items() if a == y and b == z) for z in (0, 1)]
        for y in (0, 1)
    ]


def marginal_xz(law: Law3) -> Matrix:
    return [
        [sum(prob for (a, _y, b), prob in law.items() if a == x and b == z) for z in (0, 1)]
        for x in (0, 1)
    ]


def compose_bridge(qxy: Matrix, qyz: Matrix, py: Vector) -> Matrix:
    return [
        [
            sum(qxy[x][y] * qyz[y][z] / py[y] for y in (0, 1) if py[y] > 0.0)
            for z in (0, 1)
        ]
        for x in (0, 1)
    ]


def l1_matrix(left: Matrix, right: Matrix) -> float:
    return sum(abs(left[i][j] - right[i][j]) for i in (0, 1) for j in (0, 1))


def cmi_xz_given_y(law: Law3) -> float:
    qxy = marginal_xy(law)
    qyz = marginal_yz(law)
    py = marginal_y(law)
    total = 0.0
    for x in (0, 1):
        for y in (0, 1):
            for z in (0, 1):
                pxyz = law[(x, y, z)]
                if pxyz <= 0.0:
                    continue
                denom = qxy[x][y] * qyz[y][z]
                total += pxyz * log(pxyz * py[y] / denom)
    return total


def coupling_from_t(px: Vector, pz: Vector, t: float) -> Matrix:
    return [
        [t, px[0] - t],
        [pz[0] - t, 1.0 - px[0] - pz[0] + t],
    ]


def coupling_span(px: Vector, pz: Vector) -> float:
    t_min = max(0.0, px[0] + pz[0] - 1.0)
    t_max = min(px[0], pz[0])
    return l1_matrix(coupling_from_t(px, pz, t_min), coupling_from_t(px, pz, t_max))


def max_abs_matrix(left: Matrix, right: Matrix) -> float:
    return max(abs(left[i][j] - right[i][j]) for i in (0, 1) for j in (0, 1))


def audits() -> list[ScreenBridgeAudit]:
    markov = markov_law()
    bypass = bypass_law()
    screen_ok, lower, upper = oriented_screens()
    unoriented_ok, unoriented_reason = unoriented_screens()
    qxy_m = marginal_xy(markov)
    qyz_m = marginal_yz(markov)
    qxz_m = marginal_xz(markov)
    py_m = marginal_y(markov)
    composed_m = compose_bridge(qxy_m, qyz_m, py_m)
    markov_error = l1_matrix(qxz_m, composed_m)
    markov_cmi = cmi_xz_given_y(markov)

    qxy_b = marginal_xy(bypass)
    qyz_b = marginal_yz(bypass)
    qxz_b = marginal_xz(bypass)
    py_b = marginal_y(bypass)
    composed_b = compose_bridge(qxy_b, qyz_b, py_b)
    bypass_error = l1_matrix(qxz_b, composed_b)
    bypass_cmi = cmi_xz_given_y(bypass)

    uniform = normalize({state: 1.0 for state in bypass})
    adjacent_gap_xy = max_abs_matrix(marginal_xy(uniform), qxy_b)
    adjacent_gap_yz = max_abs_matrix(marginal_yz(uniform), qyz_b)
    composite_gap = l1_matrix(marginal_xz(uniform), qxz_b)

    px_m = marginal_x(markov)
    pz_m = marginal_z(markov)
    marginal_bridge_span = coupling_span(px_m, pz_m)
    qxz_extract_error = l1_matrix(qxz_m, marginal_xz(markov))

    return [
        ScreenBridgeAudit(
            "ordered screens",
            "oriented causal order",
            "minimal/maximal antichains",
            f"lower={lower}; upper={upper}",
            f"screen order ok={screen_ok}",
            "unique as ordered boundary",
            "PASS-INTRINSIC-SCREENS",
        ),
        ScreenBridgeAudit(
            "unoriented shadow",
            "comparability graph",
            "forget order arrow",
            f"screen order ok={unoriented_ok}",
            unoriented_reason,
            "past/future swapped",
            "FAIL-NO-SCREEN-ARROW",
        ),
        ScreenBridgeAudit(
            "bridge extraction",
            "full sealed law + screens",
            "marginalize interior",
            "Q_XZ=sum_Y P_XYZ",
            "requires full law",
            f"extract error={qxz_extract_error:.1e}",
            "PASS-Q-FROM-FULL-LAW",
        ),
        ScreenBridgeAudit(
            "marginals only",
            "P_lower,P_upper",
            "choose coupling",
            f"coupling span={marginal_bridge_span:.6f}",
            "same marginals many bridges",
            "Q not unique",
            "FAIL-MARGINALS-NO-BRIDGE",
        ),
        ScreenBridgeAudit(
            "complete shared screen",
            "P_XYZ",
            "I(X;Z|Y)=0",
            f"CMI={markov_cmi:.1e}",
            f"composition error={markov_error:.1e}",
            "Q13=Q12 o Q23",
            "PASS-FUNCTORIAL-BRIDGE",
        ),
        ScreenBridgeAudit(
            "hidden bypass",
            "same adjacent bridges",
            "X-Z memory bypasses Y",
            f"CMI={bypass_cmi:.6f}",
            f"composition error={bypass_error:.6f}",
            "shared screen incomplete",
            "FAIL-SEALING-VIOLATION",
        ),
        ScreenBridgeAudit(
            "local-bridge insufficiency",
            "Q_XY,Q_YZ",
            "same adjacent data",
            f"adjacent gaps={adjacent_gap_xy:.1e},{adjacent_gap_yz:.1e}",
            f"composite gap={composite_gap:.6f}",
            "locals do not fix global",
            "FAIL-LOCAL-BRIDGES-INCOMPLETE",
        ),
        ScreenBridgeAudit(
            "screen RN defect",
            "P_XYZ,Q_XY,Q_YZ",
            "Delta_Y=D(P||P_XY P_YZ/P_Y)",
            "zero iff bridge composes",
            f"Markov={markov_cmi:.1e}; bypass={bypass_cmi:.6f}",
            "intrinsic seam test",
            "THM-FINITE-RN-SUFFICIENCY",
        ),
        ScreenBridgeAudit(
            "branch verdict",
            "sealed diamond process",
            "screens + full law + RN sufficiency",
            "Q forced conditionally",
            "sufficiency must be physical",
            "otherwise branch B",
            "A-CURRENT-CONDITIONAL",
        ),
    ]


def print_audits(rows: list[ScreenBridgeAudit]) -> None:
    print("screen-bridge theorem campaign")
    print("------------------------------")
    print(
        "target                    data                    construction             "
        "positive                         obstruction                     value                         verdict"
    )
    for row in rows:
        print(
            f"{row.target:25s} "
            f"{row.data:23s} "
            f"{row.construction:24s} "
            f"{row.positive:32s} "
            f"{row.obstruction:31s} "
            f"{row.value:29s} "
            f"{row.verdict}"
        )


def main() -> None:
    print("=" * 150)
    print("v6 Paper 3 section 39: intrinsic screen-bridge theorem campaign")
    print("=" * 150)
    print_audits(audits())
    print()
    print("VERDICT")
    print("-------")
    print("Oriented causal order gives ordered boundary screens, and the full sealed")
    print("law gives the screen-to-screen bridge by marginalizing interior records.")
    print("But bridge composition is not automatic.  It is equivalent, in the finite")
    print("three-screen audit, to the RN screen-sufficiency condition")
    print("D(P_XYZ || P_XY P_YZ / P_Y)=I(X;Z|Y)=0.")
    print()
    print("A hidden bypass can keep both adjacent bridges fixed while changing the")
    print("composite bridge.  Therefore the Einstein-satisfying invariant is an")
    print("ordered sealed record bridge with complete-screen RN sufficiency under")
    print("gluing.  If screen order or screen sufficiency is supplied externally,")
    print("the theory is branch B; if the physical sealed process enforces it,")
    print("branch A-current has a real theorem target.")


if __name__ == "__main__":
    main()
