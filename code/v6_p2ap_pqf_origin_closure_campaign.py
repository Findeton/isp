"""
v6 Paper 2 Part II section 5.55: P/Q/F origin closure campaign.

Question:
    Can bare Physical ICS fix the three missing Modular Deletion Profile
    inputs?

        F_{x,k}             canonical shell filtration;
        P_x                 retained-event local law;
        P_{delete x}        deleted-event local law.

Answer of the finite campaign:
    F has a partial positive result: once an order-rank shell functor is
    specified, F is a finite function of the pointed causal order.  But bare
    order does not select a unique physical shell functor among competing
    invariant choices.

    P_x and P_{delete x} are not functions of bare order/deletion shadow.
    Same-order finite families vary P_x or P_{delete x} while changing MDP and
    beta.  Deletion-map pushforward gives zero contrast, not an event law.

    Therefore the full fix is not "bare ICS derives P/Q/F"; it is the
    strengthened primitive: Modular Physical ICS supplies a canonical
    causal-diamond deletion germ with P, Q, and F intrinsically.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite

from v6_p2al_ics_ht_law_campaign import shell_hamiltonian, source_response
from v6_p2an_modular_deletion_profile_campaign import MDPLaw, increments, profile


@dataclass(frozen=True)
class OriginCase:
    target: str
    candidate: str
    laws: tuple[MDPLaw, ...]
    derives_target: bool
    target_unique: bool
    branch_a_internal: bool
    rule: str


@dataclass
class OriginAudit:
    target: str
    candidate: str
    rule: str
    derives: str
    unique: str
    internal: str
    profile_span: float
    beta_span: float
    verdict: str


def span(values: list[float]) -> float:
    finite = [value for value in values if isfinite(value)]
    return max(finite) - min(finite) if len(finite) >= 2 else 0.0


def profile_span(laws: tuple[MDPLaw, ...]) -> float:
    if len(laws) < 2:
        return 0.0
    profiles = [profile(law) for law in laws]
    first = profiles[0]
    return max(max(abs(a - b) for a, b in zip(first, prof)) for prof in profiles[1:])


def beta_span(laws: tuple[MDPLaw, ...]) -> float:
    betas: list[float] = []
    for law in laws:
        work = increments(profile(law))
        if not work or any(not isfinite(value) for value in work):
            continue
        beta, ok, _ = source_response(shell_hamiltonian(work), 1.0)
        if ok:
            betas.append(beta)
    return span(betas)


def min_work(law: MDPLaw) -> float:
    work = increments(profile(law))
    finite = [value for value in work if isfinite(value)]
    return min(finite) if finite else 0.0


def audit(case: OriginCase) -> OriginAudit:
    mspan = profile_span(case.laws)
    bspan = beta_span(case.laws)
    work_floor = min(min_work(law) for law in case.laws)
    passes = (
        case.derives_target
        and case.target_unique
        and case.branch_a_internal
        and work_floor >= 0.12
        and mspan <= 0.02
        and bspan <= 0.02
    )
    if passes:
        verdict = "PASS-CONDITIONAL"
    elif case.target == "F" and case.derives_target and case.target_unique:
        verdict = "PASS-F-ONLY"
    elif not case.target_unique:
        verdict = f"FAIL-NONUNIQUE-{case.target}"
    elif not case.derives_target:
        verdict = f"FAIL-NO-{case.target}"
    elif not case.branch_a_internal:
        verdict = "FAIL-EXTERNAL"
    else:
        verdict = "FAIL"
    return OriginAudit(
        target=case.target,
        candidate=case.candidate,
        rule=case.rule,
        derives="yes" if case.derives_target else "no",
        unique="yes" if case.target_unique else "no",
        internal="yes" if case.branch_a_internal else "no",
        profile_span=mspan,
        beta_span=bspan,
        verdict=verdict,
    )


def cases() -> list[OriginCase]:
    canonical = MDPLaw((0.72, 0.80, 0.85), (0.45, 0.40, 0.35))
    p_family = (
        canonical,
        MDPLaw((0.80, 0.70, 0.60), (0.45, 0.40, 0.35)),
    )
    q_family = (
        canonical,
        MDPLaw((0.72, 0.80, 0.85), (0.35, 0.35, 0.35)),
    )
    f_family = (
        canonical,
        MDPLaw((0.72, 0.80, 0.85), (0.45, 0.40, 0.35), (2, 1, 0)),
        MDPLaw((0.72, 0.80, 0.85), (0.45, 0.40, 0.35), (1, 2, 0)),
    )
    pushforward_zero = MDPLaw((0.72, 0.80, 0.85), (0.72, 0.80, 0.85))
    return [
        OriginCase(
            "P",
            "order-only maximum entropy",
            (pushforward_zero,),
            False,
            True,
            False,
            "uniform/order law",
        ),
        OriginCase(
            "P",
            "same order P-family",
            p_family,
            False,
            False,
            False,
            "P varies",
        ),
        OriginCase(
            "P",
            "retained record law in germ",
            (canonical,),
            True,
            True,
            True,
            "P primitive",
        ),
        OriginCase(
            "Q",
            "deletion pushforward",
            (pushforward_zero,),
            False,
            True,
            False,
            "Q=D_*P",
        ),
        OriginCase(
            "Q",
            "same order Q-family",
            q_family,
            False,
            False,
            False,
            "Q varies",
        ),
        OriginCase(
            "Q",
            "deleted RN law in germ",
            (canonical,),
            True,
            True,
            True,
            "Q primitive",
        ),
        OriginCase(
            "F",
            "chosen order-rank functor",
            (canonical,),
            True,
            True,
            False,
            "rank shells chosen",
        ),
        OriginCase(
            "F",
            "competing shell functors",
            f_family,
            True,
            False,
            False,
            "rank choice free",
        ),
        OriginCase(
            "F",
            "canonical shell functor in germ",
            (canonical,),
            True,
            True,
            True,
            "F primitive",
        ),
    ]


def fmt(value: float) -> str:
    return "inf" if value == float("inf") else f"{value:.4f}"


def print_rows(rows: list[OriginAudit]) -> None:
    print("P/Q/F origin closure")
    print("--------------------")
    print(
        "target  candidate                    rule                derives  unique  "
        "internal  Mspan   beta_span  verdict"
    )
    for row in rows:
        print(
            f"{row.target:6s}  "
            f"{row.candidate:28s}  "
            f"{row.rule:18s}  "
            f"{row.derives:7s}  "
            f"{row.unique:6s}  "
            f"{row.internal:8s}  "
            f"{fmt(row.profile_span):>6s}  "
            f"{fmt(row.beta_span):>9s}  "
            f"{row.verdict}"
        )
    print()


def print_witnesses() -> None:
    print("witnesses")
    print("---------")
    for label, laws in (
        (
            "P no-go: same order/F/Q, different P",
            (
                MDPLaw((0.72, 0.80, 0.85), (0.45, 0.40, 0.35)),
                MDPLaw((0.80, 0.70, 0.60), (0.45, 0.40, 0.35)),
            ),
        ),
        (
            "Q no-go: same order/F/P, different Q",
            (
                MDPLaw((0.72, 0.80, 0.85), (0.45, 0.40, 0.35)),
                MDPLaw((0.72, 0.80, 0.85), (0.35, 0.35, 0.35)),
            ),
        ),
        (
            "F no-go: same order/P/Q, different shell functor",
            (
                MDPLaw((0.72, 0.80, 0.85), (0.45, 0.40, 0.35)),
                MDPLaw((0.72, 0.80, 0.85), (0.45, 0.40, 0.35), (2, 1, 0)),
            ),
        ),
    ):
        print(label)
        for i, law in enumerate(laws, start=1):
            prof = profile(law)
            work = increments(prof)
            beta, ok, _ = source_response(shell_hamiltonian(work), 1.0)
            print(
                f"  law {i}: M={tuple(round(value, 4) for value in prof)}, "
                f"w={tuple(round(value, 4) for value in work)}, "
                f"beta={beta:.4f}, ok={ok}"
            )
    print()


def main() -> None:
    rows = [audit(case) for case in cases()]
    print("=" * 118)
    print("v6 Paper 2 Part II section 5.55: P/Q/F origin closure campaign")
    print("=" * 118)
    print_rows(rows)
    print_witnesses()
    print("CLOSURE")
    print("-------")
    print("P_x is falsified as an order-only output: same order/F/Q allows")
    print("different retained laws and different beta.")
    print("P_delete is falsified as a deletion-shadow output: same order/F/P")
    print("allows different deleted laws and different beta; pushforward deletion")
    print("has zero contrast.")
    print("F_x,k has a partial positive result: an order-rank shell functor can")
    print("derive a filtration, but bare order does not select the physical functor.")
    print("The full positive row is Modular Physical ICS, where P, Q, and F are")
    print("intrinsic pieces of the same causal-diamond deletion germ.")


if __name__ == "__main__":
    main()
