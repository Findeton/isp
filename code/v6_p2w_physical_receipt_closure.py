"""
v6 Paper 2 Part II §5.35: physical receipt closure gate.

The previous gates decide whether beta is derived by an A-full event law.  This
final finite receipt checks that the same derived beta can be used everywhere
Branch A needs it:

    energy/heating bound;
    vacuum no-events;
    source count equals geometry/event count;
    TS loop residue;
    cofinal beta stability.

This is not an independent selector.  It is the final consistency receipt for
the finite A-full survivors.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ReceiptCandidate:
    name: str
    beta: float
    beta_span: float
    event_count: int
    source_count: int
    geometry_count: int
    vacuum_events: int
    ts_residue: float


@dataclass
class ReceiptAudit:
    candidate: str
    heating: float
    energy: str
    vacuum: str
    source: str
    ts: str
    beta: str
    verdict: str


def heating(beta: float) -> float:
    if beta <= 0.0:
        return float("inf")
    return beta ** 4 / 4.0


def audit(candidate: ReceiptCandidate) -> ReceiptAudit:
    h = heating(candidate.beta)
    energy_pass = h <= 0.25
    vacuum_pass = candidate.vacuum_events == 0
    source_pass = (
        candidate.event_count > 0
        and candidate.source_count == candidate.event_count
        and candidate.geometry_count == candidate.event_count
    )
    ts_pass = candidate.ts_residue <= 1e-12
    beta_pass = candidate.beta > 0.0 and candidate.beta_span <= 0.02
    passes = energy_pass and vacuum_pass and source_pass and ts_pass and beta_pass
    return ReceiptAudit(
        candidate=candidate.name,
        heating=h,
        energy="PASS" if energy_pass else "FAIL",
        vacuum="PASS" if vacuum_pass else "FAIL",
        source="PASS" if source_pass else "FAIL",
        ts="PASS" if ts_pass else "FAIL",
        beta="PASS" if beta_pass else "FAIL",
        verdict="PASS" if passes else "FAIL",
    )


def candidates() -> list[ReceiptCandidate]:
    return [
        ReceiptCandidate("finite A-full toy", 0.6179, 0.0060, 7, 7, 7, 0, 0.0),
        ReceiptCandidate("exact A-full toy", 0.6169, 0.0000, 7, 7, 7, 0, 0.0),
        ReceiptCandidate("support-only no beta", 0.0, float("inf"), 7, 0, 7, 0, 0.0),
        ReceiptCandidate("source mismatch", 0.6179, 0.0060, 7, 6, 7, 0, 0.0),
        ReceiptCandidate("vacuum leak", 0.6179, 0.0060, 7, 7, 7, 2, 0.0),
        ReceiptCandidate("nonlocal TS residue", 0.6179, 0.0060, 7, 7, 7, 0, 0.7071),
        ReceiptCandidate("hot beta", 1.6000, 0.0060, 7, 7, 7, 0, 0.0),
        ReceiptCandidate("nonconvergent beta", 0.6179, 0.1226, 7, 7, 7, 0, 0.0),
    ]


def print_audits(rows: list[ReceiptAudit]) -> None:
    print("physical receipt closure gate")
    print("-----------------------------")
    print(
        "candidate              heating  energy  vacuum  source  TS     beta   verdict"
    )
    for row in rows:
        h = "inf" if row.heating == float("inf") else f"{row.heating:7.4f}"
        print(
            f"{row.candidate:22s}  "
            f"{h:>7s}  "
            f"{row.energy:6s}  "
            f"{row.vacuum:6s}  "
            f"{row.source:6s}  "
            f"{row.ts:5s}  "
            f"{row.beta:5s}  "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    rows = [audit(candidate) for candidate in candidates()]
    print("=" * 104)
    print("v6 Paper 2 Part II §5.35: physical receipt closure gate")
    print("=" * 104)
    print_audits(rows)
    print("VERDICT")
    print("-------")
    print("The A-full finite survivors pass the physical receipt closure.")
    print("Missing beta, source mismatch, vacuum leakage, nonlocal TS residue,")
    print("excess heating, or nonconvergent beta each fails independently.")


if __name__ == "__main__":
    main()
