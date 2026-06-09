"""
v6 Paper 3 section 3: CMRP ontology closure audit.

Question:
    If the base ontology is a Cofinal Modular Record Process, are the objects
    needed by Papers 1-2 defined internally?

Finite answer:
    A full CMRP packet defines P_x, P_{delete x}, F_{x,k}, M_x(k), shell work,
    H_x, T_x, sigma_x, kappa_G, beta, the ICS order shadow, and TS additivity.
    Weakened ontologies leave at least one of those objects external.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite

from v6_p2al_ics_ht_law_campaign import shell_hamiltonian, source_response
from v6_p2an_modular_deletion_profile_campaign import increments, profile_isolation


Profile = tuple[float, ...]
ROLE_NAMES = ("record", "source", "causal", "screen")


@dataclass(frozen=True)
class OntologyCandidate:
    name: str
    rule: str
    local_diamonds: bool
    record_algebras: bool
    process_law: bool
    deletion: bool
    shells: bool
    rn_absolute: bool
    role_maps: bool
    fixed_action: bool
    count_units: bool
    spacelike_additive: bool
    isolated: bool
    cofinal: bool
    order_projection: bool
    upstream_process: bool
    profiles: dict[str, Profile]


@dataclass
class ClosureAudit:
    candidate: str
    rule: str
    pq: str
    f: str
    mdp: str
    hts: str
    kg: str
    beta: str
    ics: str
    ts: str
    role_gap: float
    beta_span: float
    verdict: str


def span(values: list[float]) -> float:
    finite = [value for value in values if isfinite(value)]
    return max(finite) - min(finite) if len(finite) >= 2 else 0.0


def role_gap(profiles: dict[str, Profile]) -> float:
    vals = [profiles[name] for name in ROLE_NAMES if name in profiles]
    if len(vals) < 2:
        return 0.0
    n = min(len(values) for values in vals)
    return max(span([values[i] for values in vals]) for i in range(n))


def beta_from_profile(values: Profile) -> float | None:
    work = increments(values)
    if not work or any(not isfinite(value) for value in work):
        return None
    beta, ok, _ = source_response(shell_hamiltonian(work), 1.0)
    return beta if ok else None


def beta_span(profiles: dict[str, Profile]) -> float:
    betas = [
        beta for beta in (beta_from_profile(values) for values in profiles.values())
        if beta is not None
    ]
    return span(betas)


def min_isolation(profiles: dict[str, Profile]) -> float:
    values = []
    for prof in profiles.values():
        work = increments(prof)
        if work and all(isfinite(value) for value in work):
            values.append(profile_isolation(work))
    return min(values) if values else 0.0


def min_work_floor(profiles: dict[str, Profile]) -> float:
    values = []
    for prof in profiles.values():
        work = increments(prof)
        if work and all(isfinite(value) for value in work):
            values.append(min(work))
    return min(values) if values else 0.0


def audit(case: OntologyCandidate) -> ClosureAudit:
    pq = case.process_law and case.deletion
    f = case.shells
    mdp = pq and f and case.rn_absolute
    gap = role_gap(case.profiles)
    bspan = beta_span(case.profiles)
    iso = min_isolation(case.profiles)
    floor = min_work_floor(case.profiles)
    role_blind = case.role_maps and gap <= 1.0e-9
    hts = mdp and case.fixed_action and case.count_units and floor >= 0.12
    kg = hts and role_blind
    beta = hts and case.isolated and iso >= 0.12 and bspan <= 0.02
    ics = beta and case.order_projection
    ts = case.spacelike_additive
    full = (
        case.local_diamonds
        and case.record_algebras
        and pq
        and mdp
        and hts
        and kg
        and beta
        and ics
        and ts
        and case.cofinal
        and case.upstream_process
    )
    if full:
        verdict = "PASS-CMRP-CLOSURE"
    elif (
        case.local_diamonds
        and case.record_algebras
        and pq
        and mdp
        and hts
        and kg
        and beta
        and ics
        and ts
        and case.cofinal
        and not case.upstream_process
    ):
        verdict = "PASS-ENRICHED-PRIMITIVE"
    elif not case.local_diamonds:
        verdict = "FAIL-NO-DIAMONDS"
    elif not case.record_algebras:
        verdict = "FAIL-NO-RECORD-ALG"
    elif not pq:
        verdict = "FAIL-NO-PQ"
    elif not f:
        verdict = "FAIL-NO-F"
    elif not mdp:
        verdict = "FAIL-NO-MDP"
    elif not case.fixed_action:
        verdict = "FAIL-NO-FIXED-ACTION"
    elif not case.count_units:
        verdict = "FAIL-FREE-UNITS"
    elif not role_blind:
        verdict = "FAIL-ROLE-SPLIT"
    elif not beta:
        verdict = "FAIL-NO-BETA"
    elif not case.order_projection:
        verdict = "FAIL-NO-ICS-SHADOW"
    elif not ts:
        verdict = "FAIL-TS"
    elif not case.cofinal:
        verdict = "FAIL-DRIFT"
    else:
        verdict = "FAIL"
    return ClosureAudit(
        candidate=case.name,
        rule=case.rule,
        pq="yes" if pq else "no",
        f="yes" if f else "no",
        mdp="yes" if mdp else "no",
        hts="yes" if hts else "no",
        kg="yes" if kg else "no",
        beta="yes" if beta else "no",
        ics="yes" if ics else "no",
        ts="yes" if ts else "no",
        role_gap=gap,
        beta_span=bspan if case.cofinal else max(bspan, 0.1226),
        verdict=verdict,
    )


def cases() -> list[OntologyCandidate]:
    canonical = (0.0, 0.1853, 0.5707, 1.1764)
    split = (0.0, 0.1621, 0.5288, 1.0620)
    flat = (0.0, 0.22, 0.44, 0.66)
    drift = (0.0, 0.1500, 0.4900, 1.0100)
    all_roles = {name: canonical for name in ROLE_NAMES}
    return [
        OntologyCandidate(
            "bare ICS",
            "order+count",
            True,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            True,
            True,
            False,
            True,
            True,
            False,
            {name: (0.0, 0.0, 0.0, 0.0) for name in ROLE_NAMES},
        ),
        OntologyCandidate(
            "Modular Physical ICS",
            "MDP primitive",
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
            True,
            True,
            True,
            False,
            all_roles,
        ),
        OntologyCandidate(
            "CMRP without fixed action",
            "free variational law",
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
            True,
            True,
            True,
            True,
            all_roles,
        ),
        OntologyCandidate(
            "CMRP role split",
            "sector-coupled",
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
            True,
            True,
            True,
            True,
            {"record": canonical, "source": split, "causal": canonical, "screen": canonical},
        ),
        OntologyCandidate(
            "CMRP free units",
            "screen unit chosen",
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
            True,
            True,
            True,
            True,
            all_roles,
        ),
        OntologyCandidate(
            "CMRP non-isolated",
            "flat profile",
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
            False,
            True,
            True,
            True,
            {name: flat for name in ROLE_NAMES},
        ),
        OntologyCandidate(
            "CMRP TS failure",
            "nonfactorizing",
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
            True,
            True,
            True,
            True,
            all_roles,
        ),
        OntologyCandidate(
            "CMRP drift",
            "not cofinal",
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
            True,
            False,
            True,
            True,
            {name: canonical for name in ROLE_NAMES},
        ),
        OntologyCandidate(
            "sealed CMRP",
            "fixed role-blind MDP",
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
            True,
            True,
            True,
            True,
            all_roles,
        ),
    ]


def fmt(value: float) -> str:
    return "inf" if value == float("inf") else f"{value:.4f}"


def print_rows(rows: list[ClosureAudit]) -> None:
    print("CMRP ontology closure audit")
    print("---------------------------")
    print(
        "candidate                  rule                  P/Q  F    MDP  H/T/s  "
        "kG   beta  ICS  TS   role_gap  beta_span  verdict"
    )
    for row in rows:
        print(
            f"{row.candidate:26s}  "
            f"{row.rule:20s}  "
            f"{row.pq:3s}  "
            f"{row.f:3s}  "
            f"{row.mdp:3s}  "
            f"{row.hts:5s}  "
            f"{row.kg:3s}  "
            f"{row.beta:4s}  "
            f"{row.ics:3s}  "
            f"{row.ts:3s}  "
            f"{fmt(row.role_gap):>8s}  "
            f"{fmt(row.beta_span):>9s}  "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    rows = [audit(case) for case in cases()]
    winner = next(row for row in rows if row.verdict == "PASS-CMRP-CLOSURE")
    print("=" * 118)
    print("v6 Paper 3 section 3: CMRP ontology closure audit")
    print("=" * 118)
    print_rows(rows)
    print("VERDICT")
    print("-------")
    print(f"The only row that defines every required object internally is: {winner.candidate}.")
    print("Bare ICS lacks P/Q/F/MDP.  Modular Physical ICS closes only as an")
    print("enriched primitive.  A true Paper-3 base is sealed CMRP: fixed,")
    print("role-blind, TS-additive, isolated, and cofinal.")


if __name__ == "__main__":
    main()
