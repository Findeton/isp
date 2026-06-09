"""
v6 Paper 2 Part II §5.47: Einstein order-shadow audit.

The enriched-object campaign found the modular causal-diamond record
instrument (MCDI).  This audit states the Einstein version of the test:

    the causal set is not the primitive object;
    it is the order-shadow of the primitive object.

Deleting one primitive event must therefore have one constrained response:

    record click response;
    modular/source response;
    interval-volume/order response;
    screen/antichain response.

If the causal set is only an order-shadow, projecting an MCDI event to order
forgets the conjugate variables, and the frozen-signature no-go returns.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt

from v6_p2m_generalized_oer_bounds import beta_from_source_kappa


GAMMA = 7.0 / 48.0
FIRST_LAW_MVS = (1.0, -1.0, 1.0)


@dataclass(frozen=True)
class ShadowCandidate:
    name: str
    primitive: str
    same_deletion_atom: bool
    order_shadow_only: bool
    one_action: bool
    role_marks: bool
    # Signed deletion response in the order:
    # record, modular/source, interval-volume/order, screen/antichain.
    deletion_vector: tuple[float, float, float, float]
    source_family: tuple[float, ...]
    stable: bool


@dataclass
class ShadowAudit:
    candidate: str
    primitive: str
    same_atom: str
    one_action: str
    vector_floor: float
    first_law_residue: float
    beta_span: float
    verdict: str


def component_floor(vector: tuple[float, float, float, float]) -> float:
    record, modular, volume, screen = vector
    # The interval-volume component has the opposite sign in the chosen
    # first-law orientation; its magnitude still has to be seen by deletion.
    return min(record, modular, abs(volume), screen)


def first_law_residue(vector: tuple[float, float, float, float]) -> float:
    _, modular, volume, screen = vector
    response = (modular, volume, screen)
    norm_r = sqrt(sum(value * value for value in response))
    norm_t = sqrt(sum(value * value for value in FIRST_LAW_MVS))
    if norm_r == 0.0:
        return float("inf")
    dot = sum(a * b for a, b in zip(response, FIRST_LAW_MVS))
    cos = dot / (norm_r * norm_t)
    return sqrt(max(0.0, 2.0 * (1.0 - cos)))


def beta_span(source_family: tuple[float, ...]) -> float:
    betas = []
    for source in source_family:
        beta, ok = beta_from_source_kappa(GAMMA, source)
        if ok:
            betas.append(beta)
    if len(betas) < 2:
        return 0.0
    return max(betas) - min(betas)


def audit(candidate: ShadowCandidate) -> ShadowAudit:
    floor = component_floor(candidate.deletion_vector)
    residue = first_law_residue(candidate.deletion_vector)
    span = beta_span(candidate.source_family)
    pass_target = (
        candidate.same_deletion_atom
        and not candidate.order_shadow_only
        and candidate.one_action
        and not candidate.role_marks
        and floor >= 0.25
        and residue <= 1.0e-9
        and span <= 0.02
        and candidate.stable
    )
    pass_extra = candidate.role_marks and floor >= 0.25
    if pass_target:
        verdict = "PASS-TARGET"
    elif pass_extra:
        verdict = "PASS-EXTRA"
    else:
        verdict = "FAIL"
    return ShadowAudit(
        candidate=candidate.name,
        primitive=candidate.primitive,
        same_atom="yes" if candidate.same_deletion_atom else "no",
        one_action="yes" if candidate.one_action else "no",
        vector_floor=floor,
        first_law_residue=residue,
        beta_span=span if candidate.stable else max(span, 0.1226),
        verdict=verdict,
    )


def cases() -> list[ShadowCandidate]:
    return [
        ShadowCandidate(
            "bare causal-set order shadow",
            "order-shadow",
            True,
            True,
            False,
            False,
            (0.0, 0.0, -0.80, 0.80),
            (),
            True,
        ),
        ShadowCandidate(
            "role-marked causal atom",
            "marked-atom",
            True,
            False,
            False,
            True,
            (0.90, 0.90, -0.90, 0.90),
            (0.90,),
            True,
        ),
        ShadowCandidate(
            "split source geometry",
            "two-atom",
            False,
            False,
            True,
            False,
            (0.90, 0.90, -0.90, 0.90),
            (0.90,),
            True,
        ),
        ShadowCandidate(
            "record click without modular source",
            "partial-diamond",
            True,
            False,
            True,
            False,
            (0.90, 0.00, -0.90, 0.90),
            (),
            True,
        ),
        ShadowCandidate(
            "modular diamond without record",
            "partial-diamond",
            True,
            False,
            True,
            False,
            (0.00, 0.90, -0.90, 0.90),
            (0.90,),
            True,
        ),
        ShadowCandidate(
            "wrong first-law shadow",
            "diamond-germ",
            True,
            False,
            True,
            False,
            (0.90, -0.90, -0.90, 0.90),
            (0.90,),
            True,
        ),
        ShadowCandidate(
            "free source-unit diamond",
            "diamond-germ",
            True,
            False,
            True,
            False,
            (0.90, 0.90, -0.90, 0.90),
            (0.55, 0.90, 1.35),
            True,
        ),
        ShadowCandidate(
            "nonconvergent MCDI shadow",
            "MCDI",
            True,
            False,
            True,
            False,
            (0.90, 0.90, -0.90, 0.90),
            (0.90,),
            False,
        ),
        ShadowCandidate(
            "modular diamond record instrument",
            "MCDI",
            True,
            False,
            True,
            False,
            (0.92, 0.94, -0.94, 0.94),
            (0.94, 0.96),
            True,
        ),
    ]


def fmt(value: float) -> str:
    return "inf" if value == float("inf") else f"{value:.4f}"


def print_audits(rows: list[ShadowAudit]) -> None:
    print("Einstein order-shadow audit")
    print("---------------------------")
    print(
        "candidate                           primitive       same  oneF  "
        "floor   FL-res   beta_span  verdict"
    )
    for row in rows:
        print(
            f"{row.candidate:35s}  "
            f"{row.primitive:14s}  "
            f"{row.same_atom:4s}  "
            f"{row.one_action:4s}  "
            f"{fmt(row.vector_floor):>6s}  "
            f"{fmt(row.first_law_residue):>7s}  "
            f"{fmt(row.beta_span):>9s}  "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    rows = [audit(case) for case in cases()]
    print("=" * 112)
    print("v6 Paper 2 Part II §5.47: Einstein order-shadow audit")
    print("=" * 112)
    print_audits(rows)
    print("VERDICT")
    print("-------")
    print("The causal set should be read as the order-shadow of the physical")
    print("event, not as the whole event.  The primitive event must be the")
    print("same deletion atom for record, modular source, interval volume, and")
    print("screen/antichain response.  The modular diamond record instrument")
    print("is the only tested candidate that passes without role marks.")


if __name__ == "__main__":
    main()
