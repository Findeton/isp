"""
v6 Paper 2 Part II §5.33: nonlinear Frechet gate.

Branch A cannot let the threshold operation smuggle in state-dependent
nonlinear terms.  This diagnostic separates three issues that can otherwise
look alike in finite receipts:

    1. fixed linear local score: allowed;
    2. state-dependent/adaptive threshold: order-sensitive;
    3. nonlinear Frechet term in the score: not a linear local event law.

The finite tests are:
    - second-difference residue of the score map near the clicked state;
    - two-operation order residue for x/y threshold updates;
    - local support and pre-threshold source-role flags.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt
from typing import Callable


Vector = list[float]
ScoreMap = Callable[[Vector], Vector]


@dataclass
class NonlinearCandidate:
    name: str
    score: ScoreMap
    local: bool
    source_stage: str
    role_complete: bool
    adaptive_threshold: bool = False


@dataclass
class NonlinearAudit:
    candidate: str
    role_complete: bool
    source_stage: str
    local: bool
    adaptive_threshold: bool
    frechet_residue: float
    order_residue: float
    verdict: str


def norm(v: Vector) -> float:
    return sqrt(sum(x * x for x in v))


def add(a: Vector, b: Vector) -> Vector:
    return [x + y for x, y in zip(a, b)]


def sub(a: Vector, b: Vector) -> Vector:
    return [x - y for x, y in zip(a, b)]


def scale(c: float, v: Vector) -> Vector:
    return [c * x for x in v]


def frechet_residue(score: ScoreMap, p: Vector, h: Vector) -> float:
    """Second difference normalized by |h|^2."""
    plus = score(add(p, h))
    minus = score(sub(p, h))
    mid = score(p)
    second = sub(add(plus, minus), scale(2.0, mid))
    denom = max(norm(h) ** 2, 1e-15)
    return norm(second) / denom


def threshold_update(score: ScoreMap, p: Vector, idx: int) -> Vector:
    q = p[:]
    s = score(q)[idx]
    q[idx] = 1.0 if s >= 0.0 else 0.0
    return q


def order_residue(score: ScoreMap, p: Vector) -> float:
    xy = threshold_update(score, threshold_update(score, p, 0), 1)
    yx = threshold_update(score, threshold_update(score, p, 1), 0)
    return norm(sub(xy, yx))


def fixed_linear_local(p: Vector) -> Vector:
    return [p[0] - 0.50, p[1] - 0.50]


def linear_nonlocal_cross(p: Vector) -> Vector:
    return [p[0] + 0.65 * p[1] - 0.90, p[1] + 0.65 * p[0] - 0.90]


def nonlinear_local(p: Vector) -> Vector:
    return [p[0] - 0.50 + 0.80 * (p[0] - 0.50) ** 2, p[1] - 0.50 + 0.80 * (p[1] - 0.50) ** 2]


def adaptive_threshold(p: Vector) -> Vector:
    adaptive = 0.35 * (p[0] + p[1])
    return [p[0] - 0.50 - adaptive, p[1] - 0.50 - adaptive]


def nonlinear_source_hidden(p: Vector) -> Vector:
    hidden_source = 0.75 * p[0] * p[1]
    return [p[0] - 0.50 + hidden_source, p[1] - 0.50 + hidden_source]


def candidates() -> list[NonlinearCandidate]:
    return [
        NonlinearCandidate("fixed linear local", fixed_linear_local, True, "pre", True),
        NonlinearCandidate("linear nonlocal cross", linear_nonlocal_cross, False, "pre", True),
        NonlinearCandidate("nonlinear local score", nonlinear_local, True, "pre", True),
        NonlinearCandidate("adaptive threshold", adaptive_threshold, True, "pre", True, True),
        NonlinearCandidate("hidden nonlinear source", nonlinear_source_hidden, True, "post", True),
        NonlinearCandidate("record-only linear", fixed_linear_local, True, "absent", False),
    ]


def audit(candidate: NonlinearCandidate) -> NonlinearAudit:
    p = [0.55, 0.40]
    h = [0.07, -0.04]
    f_res = frechet_residue(candidate.score, p, h)
    o_res = order_residue(candidate.score, p)
    passes = (
        candidate.role_complete
        and candidate.source_stage == "pre"
        and candidate.local
        and not candidate.adaptive_threshold
        and f_res <= 1e-12
        and o_res <= 1e-12
    )
    return NonlinearAudit(
        candidate=candidate.name,
        role_complete=candidate.role_complete,
        source_stage=candidate.source_stage,
        local=candidate.local,
        adaptive_threshold=candidate.adaptive_threshold,
        frechet_residue=f_res,
        order_residue=o_res,
        verdict="PASS" if passes else "FAIL",
    )


def print_audits(rows: list[NonlinearAudit]) -> None:
    print("nonlinear Frechet gate")
    print("----------------------")
    print(
        "candidate                roles  source  local  adapt  "
        "Frechet_res  order_res  verdict"
    )
    for row in rows:
        print(
            f"{row.candidate:24s}  "
            f"{('yes' if row.role_complete else 'no'):5s}  "
            f"{row.source_stage:6s}  "
            f"{('yes' if row.local else 'no'):5s}  "
            f"{('yes' if row.adaptive_threshold else 'no'):5s}  "
            f"{row.frechet_residue:11.3e}  "
            f"{row.order_residue:9.3e}  "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    rows = [audit(candidate) for candidate in candidates()]
    print("=" * 104)
    print("v6 Paper 2 Part II §5.33: nonlinear Frechet gate")
    print("=" * 104)
    print_audits(rows)
    print("VERDICT")
    print("-------")
    print("Branch A allows fixed linear local threshold scores.  Linear")
    print("nonlocal cross-terms, adaptive thresholds, hidden nonlinear source")
    print("terms, and record-only scores fail before the scale theorem.")


if __name__ == "__main__":
    main()
