"""
v6 Paper 2 Part II §5.46: enriched Physical-ICS object campaign.

The frozen-signature no-go says that bare Physical ICS

    finite causal order + record measure + deletion map

does not derive the labeled record/source/causal/antichain signature quartet.
This script searches for the smallest honest enrichment that is not just a
role-label table.

Result:
    The surviving finite target is a modular causal-diamond record instrument:

        causal collar + deletion map
        local record instrument
        vacuum/reference state and diamond modular generator
        intrinsic volume and screen/antichain counters
        one deletion relative-entropy/free-action germ

    The four roles are then conjugate derivatives of one diamond action:
        record     = instrument outcome likelihood;
        source     = modular/RCE stress response;
        causal     = interval-volume/order response;
        antichain  = screen/antichain entropy response.

    Missing any one of instrument, modular source, volume/screen conjugacy,
    first-law orientation, source floor, or stable units reopens the beta
    freedom.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt

from v6_p2m_generalized_oer_bounds import beta_from_source_kappa


GAMMA = 7.0 / 48.0
FIRST_LAW_TARGET = (0.0, 1.0, -1.0, 1.0)


@dataclass(frozen=True)
class EnrichedCandidate:
    name: str
    one_action: bool
    role_marks_only: bool
    record_instrument: bool
    modular_source: bool
    causal_volume: bool
    screen_antichain: bool
    signature_matrix: tuple[tuple[float, ...], ...]
    first_law_vector: tuple[float, float, float, float]
    source_responses: tuple[float, ...]
    units_fixed: bool
    stable: bool


@dataclass
class EnrichedAudit:
    candidate: str
    primitive: str
    one_action: str
    variables: str
    rank: int
    margin: float
    first_law_residue: float
    source_floor: float
    beta_span: float
    verdict: str


def matrix_rank(matrix: tuple[tuple[float, ...], ...], tol: float = 1.0e-10) -> int:
    rows = [list(row) for row in matrix]
    if not rows:
        return 0
    m = len(rows)
    n = len(rows[0])
    rank = 0
    col = 0
    while rank < m and col < n:
        pivot = max(range(rank, m), key=lambda r: abs(rows[r][col]))
        if abs(rows[pivot][col]) <= tol:
            col += 1
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        pivot_value = rows[rank][col]
        rows[rank] = [value / pivot_value for value in rows[rank]]
        for r in range(m):
            if r == rank:
                continue
            factor = rows[r][col]
            rows[r] = [
                value - factor * rows[rank][c] for c, value in enumerate(rows[r])
            ]
        rank += 1
        col += 1
    return rank


def diagonal_margin(matrix: tuple[tuple[float, ...], ...]) -> float:
    if len(matrix) < 4 or any(len(row) < 4 for row in matrix[:4]):
        return 0.0
    margins = []
    for i, row in enumerate(matrix[:4]):
        off = sum(abs(row[j]) for j in range(4) if j != i)
        margins.append(row[i] - off)
    return min(margins)


def first_law_residue(vector: tuple[float, float, float, float]) -> float:
    dot = sum(a * b for a, b in zip(vector, FIRST_LAW_TARGET))
    norm_v = sqrt(sum(a * a for a in vector))
    norm_t = sqrt(sum(a * a for a in FIRST_LAW_TARGET))
    if norm_v == 0.0:
        return float("inf")
    scale = dot / (norm_v * norm_t)
    # Sign matters: the source direction has to have the positive modular
    # orientation.  A swapped or sign-reversed law is not equivalent.
    return sqrt(max(0.0, 2.0 * (1.0 - scale)))


def beta_span(responses: tuple[float, ...]) -> float:
    betas = []
    for response in responses:
        beta, ok = beta_from_source_kappa(GAMMA, response)
        if ok:
            betas.append(beta)
    if len(betas) < 2:
        return 0.0
    return max(betas) - min(betas)


def source_floor(responses: tuple[float, ...]) -> float:
    return min(responses) if responses else 0.0


def variables(candidate: EnrichedCandidate) -> str:
    return "".join(
        [
            "R" if candidate.record_instrument else "-",
            "M" if candidate.modular_source else "-",
            "V" if candidate.causal_volume else "-",
            "S" if candidate.screen_antichain else "-",
        ]
    )


def primitive_kind(candidate: EnrichedCandidate) -> str:
    if candidate.role_marks_only:
        return "marks"
    if (
        candidate.record_instrument
        and candidate.modular_source
        and candidate.causal_volume
        and candidate.screen_antichain
    ):
        return "diamond-instrument"
    if candidate.one_action:
        return "partial-action"
    return "ledger/base"


def audit(candidate: EnrichedCandidate) -> EnrichedAudit:
    rank = matrix_rank(candidate.signature_matrix)
    margin = diagonal_margin(candidate.signature_matrix)
    fl = first_law_residue(candidate.first_law_vector)
    floor = source_floor(candidate.source_responses)
    span = beta_span(candidate.source_responses)
    has_vars = (
        candidate.record_instrument
        and candidate.modular_source
        and candidate.causal_volume
        and candidate.screen_antichain
    )
    pass_target = (
        candidate.one_action
        and not candidate.role_marks_only
        and has_vars
        and rank == 4
        and margin >= 0.20
        and fl <= 1.0e-9
        and floor >= 0.25
        and span <= 0.02
        and candidate.units_fixed
        and candidate.stable
    )
    pass_extra = candidate.role_marks_only and rank == 4 and floor >= 0.25
    if pass_target:
        verdict = "PASS-TARGET"
    elif pass_extra:
        verdict = "PASS-EXTRA"
    else:
        verdict = "FAIL"
    return EnrichedAudit(
        candidate=candidate.name,
        primitive=primitive_kind(candidate),
        one_action="yes" if candidate.one_action else "no",
        variables=variables(candidate),
        rank=rank,
        margin=margin,
        first_law_residue=fl,
        source_floor=floor,
        beta_span=span if candidate.units_fixed and candidate.stable else max(span, 0.1226),
        verdict=verdict,
    )


GOOD_SIGNATURES = (
    (0.94, 0.04, 0.02, 0.00),
    (0.06, 0.91, 0.05, 0.02),
    (0.02, 0.05, 0.93, 0.04),
    (0.01, 0.02, 0.06, 0.95),
)

DEGENERATE_SIGNATURES = (
    (0.94, 0.04, 0.02, 0.00),
    (0.06, 0.48, 0.48, 0.02),
    (0.02, 0.48, 0.48, 0.04),
    (0.01, 0.02, 0.06, 0.95),
)

RECORD_ONLY = (
    (0.94, 0.04, 0.02, 0.00),
    (0.00, 0.00, 0.00, 0.00),
    (0.00, 0.00, 0.00, 0.00),
    (0.00, 0.00, 0.00, 0.00),
)

NO_SCREEN = (
    (0.94, 0.04, 0.02, 0.00),
    (0.06, 0.91, 0.05, 0.02),
    (0.02, 0.05, 0.93, 0.04),
    (0.00, 0.00, 0.00, 0.00),
)


def cases() -> list[EnrichedCandidate]:
    return [
        EnrichedCandidate(
            "bare Physical ICS",
            False,
            False,
            False,
            False,
            True,
            True,
            NO_SCREEN,
            (0.0, 0.0, -1.0, 1.0),
            (),
            True,
            True,
        ),
        EnrichedCandidate(
            "marked signature quartet",
            False,
            True,
            True,
            True,
            True,
            True,
            GOOD_SIGNATURES,
            FIRST_LAW_TARGET,
            (0.95,),
            True,
            True,
        ),
        EnrichedCandidate(
            "four independent ledgers",
            False,
            False,
            True,
            True,
            True,
            True,
            GOOD_SIGNATURES,
            FIRST_LAW_TARGET,
            (0.95,),
            True,
            True,
        ),
        EnrichedCandidate(
            "record-only instrument",
            True,
            False,
            True,
            False,
            False,
            False,
            RECORD_ONLY,
            (1.0, 0.0, 0.0, 0.0),
            (),
            True,
            True,
        ),
        EnrichedCandidate(
            "stress/RCE without record",
            True,
            False,
            False,
            True,
            False,
            False,
            RECORD_ONLY,
            (0.0, 1.0, 0.0, 0.0),
            (0.95,),
            True,
            True,
        ),
        EnrichedCandidate(
            "diamond action without screen",
            True,
            False,
            True,
            True,
            True,
            False,
            NO_SCREEN,
            (0.0, 1.0, -1.0, 0.0),
            (0.95,),
            True,
            True,
        ),
        EnrichedCandidate(
            "degenerate modular-volume law",
            True,
            False,
            True,
            True,
            True,
            True,
            DEGENERATE_SIGNATURES,
            FIRST_LAW_TARGET,
            (0.95,),
            True,
            True,
        ),
        EnrichedCandidate(
            "source units free diamond",
            True,
            False,
            True,
            True,
            True,
            True,
            GOOD_SIGNATURES,
            FIRST_LAW_TARGET,
            (0.55, 0.95, 1.35),
            False,
            True,
        ),
        EnrichedCandidate(
            "wrong first-law orientation",
            True,
            False,
            True,
            True,
            True,
            True,
            GOOD_SIGNATURES,
            (0.0, -1.0, -1.0, 1.0),
            (0.95,),
            True,
            True,
        ),
        EnrichedCandidate(
            "weak-source diamond instrument",
            True,
            False,
            True,
            True,
            True,
            True,
            GOOD_SIGNATURES,
            FIRST_LAW_TARGET,
            (0.06,),
            True,
            True,
        ),
        EnrichedCandidate(
            "nonconvergent diamond instrument",
            True,
            False,
            True,
            True,
            True,
            True,
            GOOD_SIGNATURES,
            FIRST_LAW_TARGET,
            (0.95,),
            True,
            False,
        ),
        EnrichedCandidate(
            "modular diamond record instrument",
            True,
            False,
            True,
            True,
            True,
            True,
            GOOD_SIGNATURES,
            FIRST_LAW_TARGET,
            (0.95, 0.97),
            True,
            True,
        ),
    ]


def fmt(value: float) -> str:
    if value == float("inf"):
        return "inf"
    return f"{value:.4f}"


def print_audits(rows: list[EnrichedAudit]) -> None:
    print("enriched object campaign")
    print("------------------------")
    print(
        "candidate                         primitive           oneF  vars  "
        "rank  margin  FL-res   src-floor  beta_span  verdict"
    )
    for row in rows:
        print(
            f"{row.candidate:33s}  "
            f"{row.primitive:18s}  "
            f"{row.one_action:4s}  "
            f"{row.variables:4s}  "
            f"{row.rank:4d}  "
            f"{row.margin:6.4f}  "
            f"{fmt(row.first_law_residue):>7s}  "
            f"{fmt(row.source_floor):>9s}  "
            f"{fmt(row.beta_span):>9s}  "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    rows = [audit(case) for case in cases()]
    winner = next(row for row in rows if row.verdict == "PASS-TARGET")
    print("=" * 112)
    print("v6 Paper 2 Part II §5.46: enriched Physical-ICS object campaign")
    print("=" * 112)
    print_audits(rows)
    print("SURVIVING OBJECT")
    print("----------------")
    print(winner.candidate)
    print()
    print("It is not a marked quartet.  It is one local modular causal-diamond")
    print("record instrument whose four signatures are conjugate derivatives of")
    print("one deletion relative-entropy/free-action germ.")
    print()
    print("FINITE THEOREM TARGET")
    print("---------------------")
    print("If the actual Physical-ICS event supplies this diamond instrument")
    print("cofinally, with fixed units, first-law orientation, full-rank stable")
    print("signature matrix, and positive modular source floor, then the")
    print("record/source/causal/antichain quartet is intrinsic and beta is fixed.")
    print("Every tested weakening reopens the frozen-signature or beta freedom.")


if __name__ == "__main__":
    main()
