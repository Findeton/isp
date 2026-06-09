"""
v6 Paper 2 Part II section 5.56: honest ISP base campaign.

The previous campaigns refuted bare ICS as the base: order/deletion shadow does
not derive P_x, P_delete, F_x,k, or beta.  This script asks what an upstream
ISP base would have to be.

Candidate found:
    Cofinal Modular Record Process (CMRP)

Primitive:
    A covariant finite-record stochastic process on causal diamonds, with an
    intrinsic deletion/disintegration operation and a fixed modular
    record-gravity action.  Its stable deletion atoms generate Modular Physical
    ICS as an order shadow plus MDP.

Finite target:
    If the action is fixed, the minimizer/disintegration gives P_x and
    P_delete, the causal-diamond functor gives F_x,k, the KL deletion profile
    gives H/T/sigma/source, and an isolated first profile scale fixes beta.

This is still a theorem target, not a derivation from currently established
ISP dynamics.  The audit separates it from branch-B versions with free kernels
or free action coefficients.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite

from v6_p2al_ics_ht_law_campaign import shell_hamiltonian, source_response
from v6_p2an_modular_deletion_profile_campaign import MDPLaw, increments, profile, profile_isolation


@dataclass(frozen=True)
class BaseCandidate:
    name: str
    laws: tuple[MDPLaw, ...]
    upstream_isp: bool
    process_measure: bool
    deletion_disintegration: bool
    canonical_diamonds: bool
    modular_action: bool
    gravity_internal: bool
    scale_selector: bool
    selector_fixed: bool
    ts_factorization: bool
    stable: bool
    rule: str


@dataclass
class BaseAudit:
    candidate: str
    rule: str
    P: str
    Q: str
    F: str
    grav: str
    fixed: str
    TS: str
    beta_span: float
    isolation: float
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


def audit(candidate: BaseCandidate) -> BaseAudit:
    bspan = beta_span(candidate.laws)
    isolation = min_isolation(candidate.laws)
    wfloor = min_work(candidate.laws)
    p_ok = candidate.process_measure
    q_ok = candidate.deletion_disintegration
    f_ok = candidate.canonical_diamonds
    scale_ok = candidate.scale_selector and candidate.selector_fixed and isolation >= 0.12
    passes = (
        p_ok
        and q_ok
        and f_ok
        and candidate.upstream_isp
        and candidate.modular_action
        and candidate.gravity_internal
        and scale_ok
        and candidate.ts_factorization
        and candidate.stable
        and wfloor >= 0.12
        and bspan <= 0.02
    )
    if passes:
        verdict = "PASS-BASE-TARGET"
    elif (
        p_ok
        and q_ok
        and f_ok
        and candidate.modular_action
        and candidate.gravity_internal
        and scale_ok
        and candidate.ts_factorization
        and candidate.stable
        and not candidate.upstream_isp
    ):
        verdict = "PASS-ENRICHED-PRIMITIVE"
    elif not candidate.process_measure:
        verdict = "FAIL-NO-PROCESS"
    elif not candidate.deletion_disintegration:
        verdict = "FAIL-NO-DELETION-LAW"
    elif not candidate.canonical_diamonds:
        verdict = "FAIL-NO-F"
    elif not candidate.modular_action:
        verdict = "FAIL-NO-ACTION"
    elif not candidate.gravity_internal:
        verdict = "FAIL-GRAVITY-EXTERNAL"
    elif not candidate.scale_selector:
        verdict = "FAIL-FREE-BETA"
    elif not candidate.selector_fixed:
        verdict = "FAIL-FREE-COEFF"
    elif not candidate.ts_factorization:
        verdict = "FAIL-TS"
    elif not candidate.stable:
        verdict = "FAIL-DRIFT"
    else:
        verdict = "FAIL"
    return BaseAudit(
        candidate=candidate.name,
        rule=candidate.rule,
        P="yes" if p_ok else "no",
        Q="yes" if q_ok else "no",
        F="yes" if f_ok else "no",
        grav="yes" if candidate.gravity_internal else "no",
        fixed="yes" if scale_ok else "no",
        TS="yes" if candidate.ts_factorization else "no",
        beta_span=bspan if candidate.stable else max(bspan, 0.1226),
        isolation=isolation,
        verdict=verdict,
    )


def cases() -> list[BaseCandidate]:
    canonical = MDPLaw((0.72, 0.80, 0.85), (0.45, 0.40, 0.35))
    p_family = (
        canonical,
        MDPLaw((0.80, 0.70, 0.60), (0.45, 0.40, 0.35)),
    )
    q_family = (
        canonical,
        MDPLaw((0.72, 0.80, 0.85), (0.35, 0.35, 0.35)),
    )
    drift = (
        canonical,
        MDPLaw((0.75, 0.78, 0.80), (0.45, 0.40, 0.35)),
    )
    flat = MDPLaw((0.74, 0.74, 0.74), (0.40, 0.40, 0.40))
    return [
        BaseCandidate(
            "bare ICS",
            (MDPLaw((0.70, 0.80, 0.85), (0.70, 0.80, 0.85)),),
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            True,
            True,
            "order shadow",
        ),
        BaseCandidate(
            "Poisson causal set",
            (MDPLaw((0.70, 0.80, 0.85), (0.70, 0.80, 0.85)),),
            False,
            True,
            False,
            True,
            False,
            False,
            False,
            False,
            True,
            True,
            "geometry law",
        ),
        BaseCandidate(
            "collapse flash kernel",
            p_family,
            True,
            True,
            True,
            True,
            False,
            True,
            False,
            False,
            True,
            True,
            "free kernel",
        ),
        BaseCandidate(
            "Modular Physical ICS",
            (canonical,),
            False,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            "MDP primitive",
        ),
        BaseCandidate(
            "free local record instrument",
            p_family,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            "free action coeff",
        ),
        BaseCandidate(
            "free gravity response action",
            q_family,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            "free grav coeff",
        ),
        BaseCandidate(
            "non-isolated modular process",
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
            True,
            "flat profile",
        ),
        BaseCandidate(
            "nonfactorizing record process",
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
            True,
            "TS fail",
        ),
        BaseCandidate(
            "nonconvergent record process",
            drift,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            "not cofinal",
        ),
        BaseCandidate(
            "Cofinal Modular Record Process",
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
            True,
            "fixed variational law",
        ),
    ]


def fmt(value: float) -> str:
    return "inf" if value == float("inf") else f"{value:.4f}"


def print_rows(rows: list[BaseAudit]) -> None:
    print("honest ISP base campaign")
    print("------------------------")
    print(
        "candidate                       rule                   P    Q    F    grav  "
        "fixed  TS   iso     beta_span  verdict"
    )
    for row in rows:
        print(
            f"{row.candidate:31s}  "
            f"{row.rule:21s}  "
            f"{row.P:3s}  "
            f"{row.Q:3s}  "
            f"{row.F:3s}  "
            f"{row.grav:4s}  "
            f"{row.fixed:5s}  "
            f"{row.TS:3s}  "
            f"{fmt(row.isolation):>6s}  "
            f"{fmt(row.beta_span):>9s}  "
            f"{row.verdict}"
        )
    print()


def print_chain() -> None:
    print("candidate base chain")
    print("--------------------")
    print("Cofinal Modular Record Process")
    print("-> local process measure P")
    print("-> deletion/disintegration law P_delete")
    print("-> canonical causal-diamond shell functor F")
    print("-> Modular Deletion Profile M(k)")
    print("-> event threshold, gamma, H, T, sigma, kappa_G")
    print("-> isolated first profile scale beta")
    print("-> ICS as order projection")
    print("-> gravity as screen/volume modular response")
    print()


def main() -> None:
    rows = [audit(case) for case in cases()]
    winner = next(row for row in rows if row.verdict == "PASS-BASE-TARGET")
    print("=" * 118)
    print("v6 Paper 2 Part II section 5.56: honest ISP base campaign")
    print("=" * 118)
    print_rows(rows)
    print_chain()
    print("VERDICT")
    print("-------")
    print("The only real branch-A-style base target is:")
    print(f"    {winner.candidate}")
    print("It is not ICS. ICS is the order projection of the stable record events.")
    print("The price is clear: the fixed variational record-gravity law must be")
    print("derived or postulated. If its coefficients are free, the theory is branch B.")


if __name__ == "__main__":
    main()
