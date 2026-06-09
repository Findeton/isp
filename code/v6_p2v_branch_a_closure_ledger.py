"""
v6 Paper 2 Part II §5.34: Branch-A closure ledger.

This script aggregates the finite gates added in §5.23-§5.33.

It does not claim to prove the interacting ISP event law.  It answers the
finite question:

    Which branch candidates survive every currently actionable Branch-A gate?

The only survivor is a finite A-full toy class with:
    - full pre-threshold four-role Gram;
    - one local operator origin;
    - microcausal TS projectors;
    - fixed linear local score;
    - positive, cofinally stable source deletion response.

All reduced/support/post-source/nonlocal/nonlinear/nonconvergent candidates
fail at least one gate.
"""

from __future__ import annotations

from dataclasses import dataclass

from v6_p2r_full_role_gram_derivation import audit as gram_audit
from v6_p2r_full_role_gram_derivation import candidate_laws as gram_candidates
from v6_p2s_local_operator_origin import audit as operator_audit
from v6_p2s_local_operator_origin import candidate_laws as operator_candidates
from v6_p2t_microcausal_ts_gate import audit as ts_audit
from v6_p2t_microcausal_ts_gate import candidates as ts_candidates
from v6_p2u_nonlinear_frechet_gate import audit as nonlinear_audit
from v6_p2u_nonlinear_frechet_gate import candidates as nonlinear_candidates


@dataclass
class ClosureCandidate:
    name: str
    gram_case: str
    operator_case: str
    ts_case: str
    nonlinear_case: str
    theorem_status: str


@dataclass
class ClosureAudit:
    name: str
    gram: str
    operator: str
    ts: str
    nonlinear: str
    beta_span: float
    theorem_status: str
    verdict: str


def by_name(rows: list[tuple[str, object]], audit_fn) -> dict[str, object]:
    return {name: audit_fn(name, payload) for name, payload in rows}


def by_candidate_name(rows: list[object], audit_fn) -> dict[str, object]:
    return {candidate.name: audit_fn(candidate) for candidate in rows}


def closure_candidates() -> list[ClosureCandidate]:
    return [
        ClosureCandidate(
            "finite A-full toy",
            "full LR/OER Gram",
            "convergent single O",
            "local rotated scalar",
            "fixed linear local",
            "finite pass; interacting derivation open",
        ),
        ClosureCandidate(
            "exact A-full toy",
            "exact full Gram",
            "exact single local O",
            "local full scalar",
            "fixed linear local",
            "finite pass; interacting derivation open",
        ),
        ClosureCandidate(
            "support-only reduced",
            "support only",
            "record-only O",
            "diagonal receipt only",
            "record-only linear",
            "no source/full Gram",
        ),
        ClosureCandidate(
            "post-selected source",
            "post-selected source",
            "post-selected source",
            "post-source local",
            "hidden nonlinear source",
            "source too late",
        ),
        ClosureCandidate(
            "independent source operator",
            "exact full Gram",
            "independent source Q",
            "local full scalar",
            "fixed linear local",
            "coupled source, not one local operator",
        ),
        ClosureCandidate(
            "nonlocal TS tail",
            "exact full Gram",
            "exact single local O",
            "nonlocal source tail",
            "fixed linear local",
            "microcausality fails",
        ),
        ClosureCandidate(
            "state nonlinear rule",
            "exact full Gram",
            "exact single local O",
            "state nonlinear local",
            "nonlinear local score",
            "Frechet linearity fails",
        ),
        ClosureCandidate(
            "adaptive threshold rule",
            "exact full Gram",
            "exact single local O",
            "local full scalar",
            "adaptive threshold",
            "threshold moves with state",
        ),
        ClosureCandidate(
            "nonconvergent full law",
            "nonconvergent full",
            "nonconvergent single O",
            "local full scalar",
            "fixed linear local",
            "cofinal beta stability fails",
        ),
        ClosureCandidate(
            "weak-source full law",
            "weak full source",
            "weak source single O",
            "local full scalar",
            "fixed linear local",
            "positive source floor fails",
        ),
    ]


def audits() -> list[ClosureAudit]:
    gram_rows = by_name(gram_candidates(), gram_audit)
    op_rows = by_name(operator_candidates(), operator_audit)
    ts_rows = by_candidate_name(ts_candidates(), ts_audit)
    non_rows = by_candidate_name(nonlinear_candidates(), nonlinear_audit)

    out = []
    for candidate in closure_candidates():
        g = gram_rows[candidate.gram_case]
        o = op_rows[candidate.operator_case]
        t = ts_rows[candidate.ts_case]
        n = non_rows[candidate.nonlinear_case]
        all_pass = all(
            row.verdict == "PASS"
            for row in [g, o, t, n]
        )
        verdict = "COND" if all_pass else "FAIL"
        out.append(
            ClosureAudit(
                name=candidate.name,
                gram=g.verdict,
                operator=o.verdict,
                ts=t.verdict,
                nonlinear=n.verdict,
                beta_span=g.beta_span if hasattr(g, "beta_span") else float("inf"),
                theorem_status=candidate.theorem_status,
                verdict=verdict,
            )
        )
    return out


def print_audits(rows: list[ClosureAudit]) -> None:
    print("Branch-A finite closure ledger")
    print("------------------------------")
    print(
        "candidate                    Gram  Op    TS    Lin   beta_span  verdict  status"
    )
    for row in rows:
        beta = "inf" if row.beta_span == float("inf") else f"{row.beta_span:9.4f}"
        print(
            f"{row.name:28s}  "
            f"{row.gram:5s}  "
            f"{row.operator:5s}  "
            f"{row.ts:5s}  "
            f"{row.nonlinear:5s}  "
            f"{beta:>9s}  "
            f"{row.verdict:7s}  "
            f"{row.theorem_status}"
        )
    print()


def main() -> None:
    rows = audits()
    print("=" * 112)
    print("v6 Paper 2 Part II §5.34: Branch-A closure ledger")
    print("=" * 112)
    print_audits(rows)
    finite_survivors = [row.name for row in rows if row.verdict == "COND"]
    print("FINITE SURVIVORS")
    print("----------------")
    for name in finite_survivors:
        print(f"- {name}")
    print()
    print("FINAL FINITE VERDICT")
    print("--------------------")
    print("Every currently actionable finite Branch-A loophole has a gate.")
    print("Only A-full toy laws survive all gates, and they remain conditional:")
    print("the actual interacting ISP event law still has to derive the full")
    print("pre-threshold four-role Gram from one local microcausal linear operator.")


if __name__ == "__main__":
    main()
