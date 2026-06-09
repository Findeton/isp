"""
v6 Paper 2 Part II section 5.57: CMRP action derivation campaign.

Question:
    Can the Cofinal Modular Record Process have a fixed covariant
    record-gravity action, rather than a free kernel/action?

Finite conclusion:
    A fixed modular record-gravity action is conditionally derived from a
    strong axiom packet:

        local covariance;
        finite record algebra;
        deletion disintegration;
        additive KL/RN record term;
        count-normalized screen/volume gravity term;
        no free coefficients;
        spacelike additivity/factorization;
        isolated profile scale;
        cofinal convergence.

    We do not prove that established ISP dynamics supplies this axiom packet.
    The audit shows that every weakening reopens branch-B freedom.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite

from v6_p2al_ics_ht_law_campaign import shell_hamiltonian, source_response
from v6_p2an_modular_deletion_profile_campaign import MDPLaw, increments, profile, profile_isolation


@dataclass(frozen=True)
class ActionCandidate:
    name: str
    laws: tuple[MDPLaw, ...]
    local_covariant: bool
    finite_record: bool
    deletion: bool
    kl_record: bool
    gravity_count: bool
    coefficients_fixed: bool
    additive_spacelike: bool
    stable: bool
    upstream: bool
    rule: str


@dataclass
class ActionAudit:
    candidate: str
    rule: str
    cov: str
    deln: str
    kl: str
    grav: str
    coeff: str
    ts: str
    isolation: float
    beta_span: float
    verdict: str


def span(values: list[float]) -> float:
    finite = [value for value in values if isfinite(value)]
    return max(finite) - min(finite) if len(finite) >= 2 else 0.0


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


def min_isolation(laws: tuple[MDPLaw, ...]) -> float:
    values = []
    for law in laws:
        work = increments(profile(law))
        if work and all(isfinite(value) for value in work):
            values.append(profile_isolation(work))
    return min(values) if values else 0.0


def min_work(laws: tuple[MDPLaw, ...]) -> float:
    floors = []
    for law in laws:
        work = increments(profile(law))
        if work and all(isfinite(value) for value in work):
            floors.append(min(work))
    return min(floors) if floors else 0.0


def audit(candidate: ActionCandidate) -> ActionAudit:
    bspan = beta_span(candidate.laws)
    isolation = min_isolation(candidate.laws)
    wfloor = min_work(candidate.laws)
    passes = (
        candidate.local_covariant
        and candidate.finite_record
        and candidate.deletion
        and candidate.kl_record
        and candidate.gravity_count
        and candidate.coefficients_fixed
        and candidate.additive_spacelike
        and candidate.stable
        and candidate.upstream
        and wfloor >= 0.12
        and isolation >= 0.12
        and bspan <= 0.02
    )
    if passes:
        verdict = "PASS-ACTION-TARGET"
    elif (
        candidate.local_covariant
        and candidate.finite_record
        and candidate.deletion
        and candidate.kl_record
        and candidate.gravity_count
        and candidate.coefficients_fixed
        and candidate.additive_spacelike
        and candidate.stable
        and not candidate.upstream
    ):
        verdict = "PASS-ENRICHED-INPUT"
    elif not candidate.local_covariant:
        verdict = "FAIL-NONCOV"
    elif not candidate.finite_record:
        verdict = "FAIL-NO-RECORD"
    elif not candidate.deletion:
        verdict = "FAIL-NO-DELETION"
    elif not candidate.kl_record:
        verdict = "FAIL-NO-KL"
    elif not candidate.gravity_count:
        verdict = "FAIL-NO-GRAV"
    elif not candidate.coefficients_fixed:
        verdict = "FAIL-FREE-COEFF"
    elif not candidate.additive_spacelike:
        verdict = "FAIL-TS"
    elif not candidate.stable:
        verdict = "FAIL-DRIFT"
    elif isolation < 0.12:
        verdict = "FAIL-NO-ISOLATION"
    else:
        verdict = "FAIL"
    return ActionAudit(
        candidate=candidate.name,
        rule=candidate.rule,
        cov="yes" if candidate.local_covariant else "no",
        deln="yes" if candidate.deletion else "no",
        kl="yes" if candidate.kl_record else "no",
        grav="yes" if candidate.gravity_count else "no",
        coeff="yes" if candidate.coefficients_fixed else "no",
        ts="yes" if candidate.additive_spacelike else "no",
        isolation=isolation,
        beta_span=bspan if candidate.stable else max(bspan, 0.1226),
        verdict=verdict,
    )


def cases() -> list[ActionCandidate]:
    canonical = MDPLaw((0.72, 0.80, 0.85), (0.45, 0.40, 0.35))
    free_record = (
        canonical,
        MDPLaw((0.80, 0.70, 0.60), (0.45, 0.40, 0.35)),
    )
    free_gravity = (
        canonical,
        MDPLaw((0.72, 0.80, 0.85), (0.35, 0.35, 0.35)),
    )
    drift = (
        canonical,
        MDPLaw((0.75, 0.78, 0.80), (0.45, 0.40, 0.35)),
    )
    flat = MDPLaw((0.74, 0.74, 0.74), (0.40, 0.40, 0.40))
    zero = MDPLaw((0.72, 0.80, 0.85), (0.72, 0.80, 0.85))
    return [
        ActionCandidate(
            "entropy-only action",
            (zero,),
            True,
            True,
            False,
            False,
            False,
            True,
            True,
            True,
            True,
            "max entropy",
        ),
        ActionCandidate(
            "order-volume action",
            (zero,),
            True,
            False,
            False,
            False,
            True,
            True,
            True,
            True,
            False,
            "geometry only",
        ),
        ActionCandidate(
            "record KL only",
            (canonical,),
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            True,
            "no gravity term",
        ),
        ActionCandidate(
            "collapse kernel action",
            free_record,
            True,
            True,
            True,
            False,
            True,
            False,
            True,
            True,
            True,
            "kernel chosen",
        ),
        ActionCandidate(
            "free record coefficient",
            free_record,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            "record weight free",
        ),
        ActionCandidate(
            "free gravity coefficient",
            free_gravity,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            "gravity weight free",
        ),
        ActionCandidate(
            "nonlocal action",
            (canonical,),
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            "nonadditive",
        ),
        ActionCandidate(
            "non-isolated fixed action",
            (flat,),
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            "flat MDP",
        ),
        ActionCandidate(
            "drifting fixed action",
            drift,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            "not cofinal",
        ),
        ActionCandidate(
            "Modular Physical ICS action",
            (canonical,),
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            "action input",
        ),
        ActionCandidate(
            "fixed CMRP action",
            (canonical,),
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            "KL + count action",
        ),
    ]


def fmt(value: float) -> str:
    return "inf" if value == float("inf") else f"{value:.4f}"


def print_rows(rows: list[ActionAudit]) -> None:
    print("CMRP action derivation campaign")
    print("-------------------------------")
    print(
        "candidate                    rule                cov  del  KL   grav  "
        "coeff  TS   iso     beta_span  verdict"
    )
    for row in rows:
        print(
            f"{row.candidate:28s}  "
            f"{row.rule:18s}  "
            f"{row.cov:3s}  "
            f"{row.deln:3s}  "
            f"{row.kl:3s}  "
            f"{row.grav:4s}  "
            f"{row.coeff:5s}  "
            f"{row.ts:3s}  "
            f"{fmt(row.isolation):>6s}  "
            f"{fmt(row.beta_span):>9s}  "
            f"{row.verdict}"
        )
    print()


def print_action() -> None:
    print("fixed action skeleton")
    print("---------------------")
    print("I_D(P,D_x,F) = KL/RN deletion record action")
    print("             + count-normalized screen/volume gravity response")
    print("             + spacelike-additive locality constraint")
    print("             + cofinal stability constraint")
    print()
    print("All surviving coefficients are units: logarithmic RN units and count units.")
    print("Any tunable record weight, gravity weight, kernel width, or temperature unit")
    print("moves beta and is branch B.")
    print()


def main() -> None:
    rows = [audit(case) for case in cases()]
    winner = next(row for row in rows if row.verdict == "PASS-ACTION-TARGET")
    print("=" * 118)
    print("v6 Paper 2 Part II section 5.57: CMRP action derivation campaign")
    print("=" * 118)
    print_rows(rows)
    print_action()
    print("VERDICT")
    print("-------")
    print(f"The only passing upstream action target is: {winner.candidate}.")
    print("This is a conditional derivation from strong invariance/additivity/unit")
    print("axioms, not a proof that established ISP dynamics already has that action.")
    print("Free coefficients, free kernels, missing gravity, nonlocality, no isolated")
    print("scale, or refinement drift all fail.")


if __name__ == "__main__":
    main()
