"""
v6 Paper 2 Part II §5.45: frozen signature theorem audit.

Frozen theorem:
    Does bare finite Physical ICS data

        (finite causal order, record measure, deletion map)

    uniquely derive the record/source/causal/antichain signature quartet?

No further theorem-target migration is allowed here.  The script either finds
the quartet from automorphism-invariant data or prints a counterexample.

Result:
    The frozen theorem is false for bare Physical ICS.  A finite positive
    collar with symmetric or unlabeled record channels has the same
    order/measure/deletion data but no invariant way to choose a source
    signature.  In an unlabeled distinct-channel collar, different source
    assignments give different beta values.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations

from v6_p2m_generalized_oer_bounds import beta_from_source_kappa


GAMMA = 7.0 / 48.0


@dataclass(frozen=True)
class FrozenICS:
    name: str
    # Diagonal covariance of primitive record channels.
    covariance_diag: tuple[float, ...]
    # Deletion response amplitude of primitive channels.
    deletion_response: tuple[float, ...]
    # Whether role names are part of the input data.  Bare Physical ICS has
    # this set to False.
    role_marks: tuple[str, ...] | None


@dataclass
class FrozenAudit:
    candidate: str
    automorphisms: int
    orbits: list[list[int]]
    marked: str
    unique_quartet: str
    source_intrinsic: str
    beta_span: float
    verdict: str


def preserves(data: FrozenICS, perm: tuple[int, ...]) -> bool:
    cov_ok = all(
        data.covariance_diag[i] == data.covariance_diag[perm[i]]
        for i in range(len(perm))
    )
    del_ok = all(
        data.deletion_response[i] == data.deletion_response[perm[i]]
        for i in range(len(perm))
    )
    if data.role_marks is None:
        mark_ok = True
    else:
        mark_ok = all(data.role_marks[i] == data.role_marks[perm[i]] for i in range(len(perm)))
    return cov_ok and del_ok and mark_ok


def automorphisms(data: FrozenICS) -> list[tuple[int, ...]]:
    n = len(data.covariance_diag)
    return [perm for perm in permutations(range(n)) if preserves(data, perm)]


def channel_orbits(n: int, autos: list[tuple[int, ...]]) -> list[list[int]]:
    seen: set[int] = set()
    out: list[list[int]] = []
    for i in range(n):
        if i in seen:
            continue
        orbit = sorted({perm[i] for perm in autos})
        seen.update(orbit)
        out.append(orbit)
    return out


def beta_span_for_source_choices(data: FrozenICS, source_choices: list[int]) -> float:
    betas = []
    for index in source_choices:
        beta, ok = beta_from_source_kappa(GAMMA, data.deletion_response[index])
        if ok:
            betas.append(beta)
    return max(betas) - min(betas) if len(betas) >= 2 else 0.0


def audit(data: FrozenICS) -> FrozenAudit:
    autos = automorphisms(data)
    orbits = channel_orbits(len(data.covariance_diag), autos)
    marked = data.role_marks is not None
    has_four = len(data.covariance_diag) >= 4
    all_singletons = has_four and all(len(orbit) == 1 for orbit in orbits[:4])
    required_marks = ("record", "source", "causal", "antichain")
    marks_ok = marked and tuple(data.role_marks[:4]) == required_marks

    if marks_ok:
        source_choices = [data.role_marks.index("source")]
    elif all_singletons and has_four:
        source_choices = list(range(4))
    elif has_four:
        source_choices = list(orbits[0])
    else:
        source_choices = []

    beta_span = beta_span_for_source_choices(data, source_choices)
    unique_quartet = marks_ok
    source_intrinsic = marks_ok
    verdict = "PASS-EXTRA" if marks_ok else "FAIL"
    return FrozenAudit(
        candidate=data.name,
        automorphisms=len(autos),
        orbits=orbits,
        marked="yes" if marked else "no",
        unique_quartet="yes" if unique_quartet else "no",
        source_intrinsic="yes" if source_intrinsic else "no",
        beta_span=beta_span,
        verdict=verdict,
    )


def cases() -> list[FrozenICS]:
    return [
        FrozenICS(
            "bare symmetric Physical ICS",
            (1.0, 1.0, 1.0, 1.0),
            (0.70, 0.70, 0.70, 0.70),
            None,
        ),
        FrozenICS(
            "bare distinct but unlabeled ICS",
            (0.80, 1.10, 1.45, 1.90),
            (0.20, 0.55, 0.95, 1.35),
            None,
        ),
        FrozenICS(
            "bare three-signature ICS",
            (0.80, 1.10, 1.45),
            (0.20, 0.55, 0.95),
            None,
        ),
        FrozenICS(
            "marked signature quartet",
            (0.80, 1.10, 1.45, 1.90),
            (0.20, 0.95, 0.55, 1.35),
            ("record", "source", "causal", "antichain"),
        ),
        FrozenICS(
            "wrong marked quartet",
            (0.80, 1.10, 1.45, 1.90),
            (0.20, 0.95, 0.55, 1.35),
            ("record", "causal", "source", "antichain"),
        ),
    ]


def fmt(value: float) -> str:
    return f"{value:.4f}"


def print_audits(rows: list[FrozenAudit]) -> None:
    print("frozen signature theorem audit")
    print("------------------------------")
    print(
        "candidate                       aut  orbits                 marked  "
        "quartet  source  beta_span  verdict"
    )
    for row in rows:
        orbit_text = ";".join("".join(str(i) for i in orbit) for orbit in row.orbits)
        print(
            f"{row.candidate:31s}  "
            f"{row.automorphisms:3d}  "
            f"{orbit_text:21s}  "
            f"{row.marked:6s}  "
            f"{row.unique_quartet:7s}  "
            f"{row.source_intrinsic:6s}  "
            f"{fmt(row.beta_span):>9s}  "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    rows = [audit(case) for case in cases()]
    distinct_span = next(
        row.beta_span for row in rows if row.candidate == "bare distinct but unlabeled ICS"
    )
    print("=" * 104)
    print("v6 Paper 2 Part II §5.45: frozen signature theorem audit")
    print("=" * 104)
    print_audits(rows)
    print("COUNTEREXAMPLE")
    print("--------------")
    print("The bare distinct but unlabeled Physical ICS has trivial channel")
    print("automorphism orbits but no role marks.  All four channels are invariant")
    print("as channels, yet no invariant says which singleton is source.  Assigning")
    print(f"the source role to different singletons gives beta span {distinct_span:.4f}.")
    print()
    print("VERDICT")
    print("-------")
    print("The frozen theorem is false for bare Physical ICS.  Order, record")
    print("measure, and deletion map can identify invariant channels or orbits,")
    print("but they do not by themselves identify the physical source signature.")
    print("A marked signature quartet can pass only because the role marks are")
    print("extra input.  Thus pure Branch A fails unless Physical ICS is enlarged")
    print("to include, or an interacting theorem derives, those role marks.")


if __name__ == "__main__":
    main()
