"""
v6 Paper 2 Part II §5.26: full-law p_source audit.

The previous diagnostics show that same support and positive visible margins do
not fix beta. This audit asks the sharper question:

Can p_source, or more invariantly d_source=(J u)_source, vary while the full
role-complete local likelihood law is the same?

Answer in this finite model:
- same support/reduced receipts: yes, d_source can vary;
- same full role-cumulant law: no, J fixes d_source;
- different decompositions with the same J may relabel p_source, but beta does
  not move because d_source is unchanged.
"""

from __future__ import annotations

from dataclasses import dataclass

from v6_p2j_lr_decisive_tests import acv_actual_event_law_audit
from v6_p2m_generalized_oer_bounds import (
    U_DELETE,
    beta_from_source_kappa,
    deletion_vector,
    role_jacobian,
)


@dataclass
class LawInstance:
    nominal_source_private: float
    support_id: str
    role_complete: bool
    jacobian: list[list[float]]
    internal_coupling: float


@dataclass
class FamilyAudit:
    case: str
    same_support: bool
    same_full_role_law: bool
    role_complete: bool
    acv_all: bool
    kappa_span: float
    beta_span: float
    nominal_p_span: float
    verdict: str


def matrix_fingerprint(matrix: list[list[float]]) -> tuple[tuple[float, ...], ...]:
    return tuple(tuple(round(x, 12) for x in row) for row in matrix)


def full_law_fingerprint(row: LawInstance) -> tuple[tuple[float, ...], ...] | None:
    if not row.role_complete:
        return None
    return matrix_fingerprint(row.jacobian)


def source_kappa_and_beta(row: LawInstance) -> tuple[float, float, bool]:
    _, _, _, _, _, eps_j, _, _, acv_passes = acv_actual_event_law_audit(
        row.jacobian,
        0.80,
        row.internal_coupling,
    )
    d = deletion_vector(row.jacobian)
    source_kappa = d[1] - 4.0 * eps_j
    beta, cost_passes = beta_from_source_kappa(7.0 / 48.0, source_kappa)
    return source_kappa, beta, acv_passes and cost_passes and source_kappa > 0.0


def audit_family(case: str, rows: list[LawInstance]) -> FamilyAudit:
    support_ids = {row.support_id for row in rows}
    full_ids = {full_law_fingerprint(row) for row in rows}
    kappas = []
    betas = []
    acv_flags = []
    nominal = []
    for row in rows:
        kappa, beta, passes = source_kappa_and_beta(row)
        kappas.append(kappa)
        betas.append(beta)
        acv_flags.append(passes)
        nominal.append(row.nominal_source_private)
    same_support = len(support_ids) == 1
    same_full = None not in full_ids and len(full_ids) == 1
    role_complete = all(row.role_complete for row in rows)
    kappa_span = max(kappas) - min(kappas)
    beta_span = max(betas) - min(betas)
    nominal_p_span = max(nominal) - min(nominal)
    acv_all = all(acv_flags)
    passes = same_full and role_complete and acv_all and kappa_span <= 1e-12 and beta_span <= 1e-12
    return FamilyAudit(
        case=case,
        same_support=same_support,
        same_full_role_law=same_full,
        role_complete=role_complete,
        acv_all=acv_all,
        kappa_span=kappa_span,
        beta_span=beta_span,
        nominal_p_span=nominal_p_span,
        verdict="PASS" if passes else "FAIL",
    )


def source_amplitude_rows() -> list[LawInstance]:
    rows = []
    for p_source in [0.350, 0.550, 0.750, 0.950, 1.200]:
        rows.append(
            LawInstance(
                nominal_source_private=p_source,
                support_id="seven-click-support",
                role_complete=True,
                jacobian=role_jacobian(0.030, [0.820, p_source, 0.960, 1.020], 0.003),
                internal_coupling=0.015,
            )
        )
    return rows


def identical_full_law_rows() -> list[LawInstance]:
    jacobian = role_jacobian(0.030, [0.820, 0.950, 0.960, 1.020], 0.003)
    return [
        LawInstance(
            nominal_source_private=0.950,
            support_id="seven-click-support",
            role_complete=True,
            jacobian=jacobian,
            internal_coupling=0.015,
        )
        for _ in range(5)
    ]


def decomposition_gauge_rows() -> list[LawInstance]:
    """Same J and same beta while a nominal decomposition label is varied."""
    jacobian = role_jacobian(0.030, [0.820, 0.950, 0.960, 1.020], 0.003)
    return [
        LawInstance(
            nominal_source_private=p_source,
            support_id="seven-click-support",
            role_complete=True,
            jacobian=jacobian,
            internal_coupling=0.015,
        )
        for p_source in [0.350, 0.550, 0.750, 0.950, 1.200]
    ]


def hidden_source_extension_rows() -> list[LawInstance]:
    rows = []
    for p_source in [0.350, 0.550, 0.750, 0.950, 1.200]:
        rows.append(
            LawInstance(
                nominal_source_private=p_source,
                support_id="seven-click-support",
                role_complete=False,
                jacobian=role_jacobian(0.030, [0.820, p_source, 0.960, 1.020], 0.003),
                internal_coupling=0.015,
            )
        )
    return rows


def print_audits(rows: list[FamilyAudit]) -> None:
    print("full-law p_source audit")
    print("-----------------------")
    print(
        "case                   support  full_law  role_full  ACV   "
        "p_span  kappa_span  beta_span  verdict"
    )
    for row in rows:
        print(
            f"{row.case:22s}  "
            f"{('yes' if row.same_support else 'no'):7s}  "
            f"{('yes' if row.same_full_role_law else 'no'):8s}  "
            f"{('yes' if row.role_complete else 'no'):9s}  "
            f"{('PASS' if row.acv_all else 'FAIL'):4s}  "
            f"{row.nominal_p_span:6.3f}  "
            f"{row.kappa_span:10.4f}  "
            f"{row.beta_span:9.4f}  "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    rows = [
        audit_family("same support only", source_amplitude_rows()),
        audit_family("identical full law", identical_full_law_rows()),
        audit_family("decomposition gauge", decomposition_gauge_rows()),
        audit_family("hidden source ext", hidden_source_extension_rows()),
    ]
    print("=" * 100)
    print("v6 Paper 2 Part II §5.26: full-law p_source audit")
    print("=" * 100)
    print_audits(rows)
    print("VERDICT")
    print("-------")
    print("A same full role-complete law fixes J, hence fixes d_source=(J u)_source")
    print("and beta. Same support or hidden-source extensions do not. A varied")
    print("nominal p_source is harmless only when J is unchanged; then it is a")
    print("decomposition gauge label, not a physical scale freedom.")


if __name__ == "__main__":
    main()
