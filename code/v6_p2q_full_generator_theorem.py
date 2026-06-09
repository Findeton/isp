"""
v6 Paper 2 Part II §5.29: full-generator theorem audit.

This diagnostic sharpens §5.28.  The literal generator matrix A is not the
invariant object, because a change of latent feature basis A -> A O with O
orthogonal leaves all role statistics unchanged.  The invariant full
role-generator law is the Gram/response matrix

    J = A A^T = Cov(T | click).

The finite theorem tested here is:

    full Gram response law fixed or convergent
    + positive source deletion component
    + ACV/cost margins
    => beta fixed or convergent.

The opposite is also tested: the non-source role Gram, support, and visible
receipts do not determine beta if the source row of J can still move.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import cos, sin

from v6_p2j_lr_decisive_tests import acv_actual_event_law_audit
from v6_p2m_generalized_oer_bounds import beta_from_source_kappa, deletion_vector


ROLE_COUNT = 4
SOURCE_INDEX = 1
GAMMA = 7.0 / 48.0


@dataclass
class GeneratorLaw:
    rows: list[list[float]]
    role_complete: bool = True
    support_id: str = "seven-click-support"
    internal_coupling: float = 0.015


@dataclass
class TheoremAudit:
    case: str
    role_complete: bool
    same_support: bool
    full_gram_span: float
    nonsource_gram_span: float
    source_coord_span: float
    source_kappa_span: float
    beta_span: float
    acv: bool
    verdict: str


def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def gram(rows: list[list[float]]) -> list[list[float]]:
    return [[dot(row_i, row_j) for row_j in rows] for row_i in rows]


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [
        [sum(row[k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for row in a
    ]


def rotation_01_23(theta: float, phi: float) -> list[list[float]]:
    c0, s0 = cos(theta), sin(theta)
    c1, s1 = cos(phi), sin(phi)
    return [
        [c0, -s0, 0.0, 0.0],
        [s0, c0, 0.0, 0.0],
        [0.0, 0.0, c1, -s1],
        [0.0, 0.0, s1, c1],
    ]


def right_rotate(rows: list[list[float]], theta: float, phi: float) -> list[list[float]]:
    return matmul(rows, rotation_01_23(theta, phi))


def base_rows(source_strength: float = 0.95) -> list[list[float]]:
    return [
        [0.95, 0.05, 0.02, 0.00],
        [0.08, source_strength, 0.05, 0.02],
        [0.03, 0.06, 0.96, 0.04],
        [0.02, 0.04, 0.08, 0.98],
    ]


def convergent_rows(step: float) -> list[list[float]]:
    return [
        [0.95 + 0.02 * step, 0.05, 0.02, 0.00],
        [0.08, 0.92 + 0.03 * step, 0.05, 0.02],
        [0.03, 0.06, 0.96 + 0.01 * step, 0.04],
        [0.02, 0.04, 0.08, 0.98 + 0.01 * step],
    ]


def collapsed_rows(source_strength: float) -> list[list[float]]:
    return [
        [0.95, 0.05, 0.02, 0.00],
        [0.02, source_strength, 0.01, 0.00],
        [0.03, 0.06, 0.96, 0.04],
        [0.02, 0.04, 0.08, 0.98],
    ]


def matrix_span(mats: list[list[list[float]]]) -> float:
    out = 0.0
    for i in range(len(mats[0])):
        for j in range(len(mats[0][0])):
            values = [mat[i][j] for mat in mats]
            out = max(out, max(values) - min(values))
    return out


def source_coord_span(laws: list[GeneratorLaw]) -> float:
    out = 0.0
    for col in range(ROLE_COUNT):
        values = [law.rows[SOURCE_INDEX][col] for law in laws]
        out = max(out, max(values) - min(values))
    return out


def nonsource_gram(g: list[list[float]]) -> list[list[float]]:
    ids = [0, 2, 3]
    return [[g[i][j] for j in ids] for i in ids]


def kappa_beta_acv(law: GeneratorLaw) -> tuple[float, float, bool]:
    g = gram(law.rows)
    _, _, _, _, _, eps_j, _, _, acv_passes = acv_actual_event_law_audit(
        g,
        0.80,
        law.internal_coupling,
    )
    d = deletion_vector(g)
    source_kappa = d[SOURCE_INDEX] - 4.0 * eps_j
    beta, cost_passes = beta_from_source_kappa(GAMMA, source_kappa)
    return source_kappa, beta, acv_passes and cost_passes and source_kappa > 0.0


def audit(case: str, laws: list[GeneratorLaw]) -> TheoremAudit:
    grams = [gram(law.rows) for law in laws]
    nongrams = [nonsource_gram(g) for g in grams]
    kappas = []
    betas = []
    acv_flags = []
    for law in laws:
        kappa, beta, acv = kappa_beta_acv(law)
        kappas.append(kappa)
        betas.append(beta)
        acv_flags.append(acv)

    full_span = matrix_span(grams)
    nonsource_span = matrix_span(nongrams)
    kappa_span = max(kappas) - min(kappas)
    beta_span = max(betas) - min(betas)
    role_complete = all(law.role_complete for law in laws)
    same_support = len({law.support_id for law in laws}) == 1
    acv = all(acv_flags)
    source_span = source_coord_span(laws)

    passes = (
        role_complete
        and same_support
        and acv
        and (
            (full_span <= 1e-12 and beta_span <= 1e-12)
            or (full_span <= 0.07 and kappa_span <= 0.05 and beta_span <= 0.02)
        )
    )
    return TheoremAudit(
        case=case,
        role_complete=role_complete,
        same_support=same_support,
        full_gram_span=full_span,
        nonsource_gram_span=nonsource_span,
        source_coord_span=source_span,
        source_kappa_span=kappa_span,
        beta_span=beta_span,
        acv=acv,
        verdict="PASS" if passes else "FAIL",
    )


def audits() -> list[TheoremAudit]:
    base = base_rows(0.95)
    orthogonal_gauge = [
        GeneratorLaw(right_rotate(base, theta, phi))
        for theta, phi in [(0.00, 0.00), (0.25, -0.15), (-0.35, 0.20), (0.50, 0.35)]
    ]
    same_full_gram = [GeneratorLaw(base_rows(0.95)) for _ in range(4)]
    three_role_only = [
        GeneratorLaw(base_rows(strength))
        for strength in [0.55, 0.75, 0.95, 1.15]
    ]
    hidden_source = [
        GeneratorLaw(base_rows(strength), role_complete=False)
        for strength in [0.55, 0.75, 0.95, 1.15]
    ]
    convergent_full_gram = [
        GeneratorLaw(convergent_rows(step))
        for step in [1.00, 0.50, 0.25, 0.00]
    ]
    nonconvergent_full_gram = [
        GeneratorLaw(base_rows(strength))
        for strength in [0.55, 1.15, 0.65, 1.05]
    ]
    weak_source = [
        GeneratorLaw(collapsed_rows(strength))
        for strength in [0.04, 0.05, 0.06, 0.05]
    ]
    return [
        audit("orthogonal gauge", orthogonal_gauge),
        audit("same full Gram", same_full_gram),
        audit("three-role only", three_role_only),
        audit("hidden source", hidden_source),
        audit("convergent full Gram", convergent_full_gram),
        audit("nonconvergent Gram", nonconvergent_full_gram),
        audit("weak source row", weak_source),
    ]


def print_audits(rows: list[TheoremAudit]) -> None:
    print("full-generator theorem audit")
    print("----------------------------")
    print(
        "case                  role  support  ACV   J_span  J3_span  "
        "A_src_span  kappa_span  beta_span  verdict"
    )
    for row in rows:
        print(
            f"{row.case:21s}  "
            f"{('yes' if row.role_complete else 'no'):4s}  "
            f"{('yes' if row.same_support else 'no'):7s}  "
            f"{('PASS' if row.acv else 'FAIL'):4s}  "
            f"{row.full_gram_span:7.4f}  "
            f"{row.nonsource_gram_span:7.4f}  "
            f"{row.source_coord_span:10.4f}  "
            f"{row.source_kappa_span:10.4f}  "
            f"{row.beta_span:9.4f}  "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    rows = audits()
    print("=" * 104)
    print("v6 Paper 2 Part II §5.29: full-generator theorem audit")
    print("=" * 104)
    print_audits(rows)
    print("VERDICT")
    print("-------")
    print("A fixed full Gram law J=A A^T fixes d_source and beta, even when")
    print("the displayed source row of A changes by latent orthogonal gauge.")
    print("Fixing only the non-source role Gram does not fix beta. A-full")
    print("therefore needs a cofinal full Gram/role law, not literal matrix")
    print("coordinates and not support plus three role readouts.")


if __name__ == "__main__":
    main()
