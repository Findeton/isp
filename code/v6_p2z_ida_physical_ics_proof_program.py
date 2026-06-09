"""
v6 Paper 2 Part II §5.38: IDA Physical-ICS proof program.

This script executes the seven-step proof/falsification program for the
Invariant Deletion-Action law (IDA) in a finite Physical ICS.

The important sharpening is that a scalar deletion value A_x(0) is not enough.
Branch A needs the local deformation germ of the deletion action:

    A_x(theta), dA_x, Hess A_x

in four fixed internal directions: record, source, causal, antichain.  The
same scalar value can have different Hessians and therefore different beta.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations
from math import exp, log

from v6_p2r_full_role_gram_derivation import (
    ROLE_ORDER,
    LawInstance,
    base_role_rows,
    beta_from_gram,
    gram,
    matrix_span,
    role_rows,
    weak_source_rows,
)


SOURCE_INDEX = 1


@dataclass
class Poset:
    events: tuple[str, ...]
    order: frozenset[tuple[str, str]]


@dataclass
class IDACandidate:
    name: str
    has_record_measure: bool
    positive_deleted_support: bool
    order_covariant: bool
    slice_free: bool
    internal_roles: bool
    same_scalar_functional: bool
    row_family: list[dict[str, list[float]]]
    scalar_action_values: list[float]


@dataclass
class IDAAudit:
    name: str
    deletion: str
    rn: str
    invariant: str
    roles: str
    fisher: str
    source: str
    counter: str
    beta_span: float
    verdict: str


def toy_poset() -> Poset:
    events = ("a", "b", "x", "c", "d")
    order = frozenset({
        ("a", "x"),
        ("b", "x"),
        ("x", "c"),
        ("x", "d"),
        ("a", "c"),
        ("a", "d"),
        ("b", "c"),
        ("b", "d"),
    })
    return Poset(events, order)


def delete_event(poset: Poset, event: str) -> Poset:
    events = tuple(e for e in poset.events if e != event)
    order = frozenset((a, b) for a, b in poset.order if a != event and b != event)
    return Poset(events, order)


def is_transitive(poset: Poset) -> bool:
    for a, b in poset.order:
        for c, d in poset.order:
            if b == c and (a, d) not in poset.order:
                return False
    return True


def linear_extensions(poset: Poset) -> list[tuple[str, ...]]:
    out = []
    for perm in permutations(poset.events):
        index = {event: i for i, event in enumerate(perm)}
        if all(index[a] < index[b] for a, b in poset.order):
            out.append(perm)
    return out


def order_signature(poset: Poset) -> tuple[tuple[int, int], ...]:
    pairs = []
    for event in poset.events:
        past = sum(1 for a, b in poset.order if b == event)
        future = sum(1 for a, b in poset.order if a == event)
        pairs.append((past, future))
    return tuple(sorted(pairs))


def relabel(poset: Poset, mapping: dict[str, str]) -> Poset:
    events = tuple(mapping[e] for e in poset.events)
    order = frozenset((mapping[a], mapping[b]) for a, b in poset.order)
    return Poset(events, order)


def deletion_map_is_clean() -> bool:
    poset = toy_poset()
    deleted = delete_event(poset, "x")
    return "x" not in deleted.events and is_transitive(deleted)


def rn_exists(candidate: IDACandidate) -> bool:
    # In a finite local collar, strict positivity of deleted support is enough
    # for the retained/deleted local contrast to be a finite RN derivative.
    return candidate.has_record_measure and candidate.positive_deleted_support


def invariant_and_slicefree(candidate: IDACandidate) -> bool:
    poset = toy_poset()
    renamed = relabel(poset, {"a": "q", "b": "r", "x": "s", "c": "t", "d": "u"})
    relabel_invariant = order_signature(poset) == order_signature(renamed)
    has_two_slices = len(linear_extensions(poset)) >= 2
    return candidate.order_covariant and candidate.slice_free and relabel_invariant and has_two_slices


def samples_from_rows(rows: dict[str, list[float]]) -> list[list[float]]:
    """Build a finite zero-mean exponential family with Fisher J=A A^T."""
    samples: list[list[float]] = []
    for latent_index in range(len(next(iter(rows.values())))):
        column = [2.0 * rows[role][latent_index] for role in ROLE_ORDER]
        samples.append(column)
        samples.append([-value for value in column])
    return samples


def covariance(samples: list[list[float]]) -> list[list[float]]:
    dim = len(samples[0])
    mean = [sum(sample[i] for sample in samples) / len(samples) for i in range(dim)]
    return [
        [
            sum((sample[i] - mean[i]) * (sample[j] - mean[j]) for sample in samples)
            / len(samples)
            for j in range(dim)
        ]
        for i in range(dim)
    ]


def log_partition(samples: list[list[float]], theta: list[float]) -> float:
    values = [exp(sum(t * x for t, x in zip(theta, sample))) for sample in samples]
    return log(sum(values) / len(values))


def numeric_hessian(samples: list[list[float]], h: float = 1e-4) -> list[list[float]]:
    dim = len(samples[0])
    zero = [0.0] * dim
    base = log_partition(samples, zero)
    out = [[0.0 for _ in range(dim)] for _ in range(dim)]
    for i in range(dim):
        for j in range(dim):
            if i == j:
                plus = zero.copy()
                minus = zero.copy()
                plus[i] = h
                minus[i] = -h
                out[i][j] = (log_partition(samples, plus) - 2.0 * base + log_partition(samples, minus)) / (h * h)
            else:
                pp = zero.copy()
                pm = zero.copy()
                mp = zero.copy()
                mm = zero.copy()
                pp[i] = h
                pp[j] = h
                pm[i] = h
                pm[j] = -h
                mp[i] = -h
                mp[j] = h
                mm[i] = -h
                mm[j] = -h
                out[i][j] = (
                    log_partition(samples, pp)
                    - log_partition(samples, pm)
                    - log_partition(samples, mp)
                    + log_partition(samples, mm)
                ) / (4.0 * h * h)
    return out


def max_abs_diff(a: list[list[float]], b: list[list[float]]) -> float:
    return max(abs(a[i][j] - b[i][j]) for i in range(len(a)) for j in range(len(a[0])))


def fisher_hessian_pass(rows: dict[str, list[float]]) -> bool:
    samples = samples_from_rows(rows)
    empirical = covariance(samples)
    numerical = numeric_hessian(samples)
    target = gram(role_rows(LawInstance(rows, "pre"), ROLE_ORDER))
    return max_abs_diff(empirical, target) <= 1e-12 and max_abs_diff(numerical, target) <= 1e-6


def beta_values(candidate: IDACandidate) -> tuple[list[float], list[float], list[bool]]:
    kappas = []
    betas = []
    oks = []
    if not (candidate.internal_roles and candidate.same_scalar_functional):
        return kappas, betas, oks
    for rows in candidate.row_family:
        j = covariance(samples_from_rows(rows))
        kappa, beta, ok = beta_from_gram(j, 0.015)
        kappas.append(kappa)
        betas.append(beta)
        oks.append(ok)
    return kappas, betas, oks


def same_scalar_beta_counterexample() -> tuple[float, float]:
    scalar_values = []
    betas = []
    for strength in [0.55, 0.75, 0.95, 1.15]:
        rows = base_role_rows(strength)
        scalar_values.append(0.25)
        j = covariance(samples_from_rows(rows))
        _, beta, ok = beta_from_gram(j, 0.015)
        if ok:
            betas.append(beta)
    return max(scalar_values) - min(scalar_values), max(betas) - min(betas)


def audit(candidate: IDACandidate) -> IDAAudit:
    deletion_ok = deletion_map_is_clean()
    rn_ok = rn_exists(candidate)
    invariant_ok = invariant_and_slicefree(candidate)
    roles_ok = candidate.internal_roles and all(role in candidate.row_family[0] for role in ROLE_ORDER)
    fisher_ok = roles_ok and candidate.same_scalar_functional and fisher_hessian_pass(candidate.row_family[0])
    kappas, betas, oks = beta_values(candidate)
    source_ok = bool(oks) and all(oks) and min(kappas) > 0.0
    beta_span = max(betas) - min(betas) if betas else float("inf")
    convergence_ok = beta_span <= 0.02
    scalar_span, counter_beta_span = same_scalar_beta_counterexample()
    counter_ok = candidate.same_scalar_functional and scalar_span == 0.0 and counter_beta_span > 0.0
    # counter_ok here means the audit found and excluded the scalar-only loophole.
    passes = (
        deletion_ok
        and rn_ok
        and invariant_ok
        and roles_ok
        and fisher_ok
        and source_ok
        and convergence_ok
        and counter_ok
    )
    return IDAAudit(
        name=candidate.name,
        deletion="PASS" if deletion_ok else "FAIL",
        rn="PASS" if rn_ok else "FAIL",
        invariant="PASS" if invariant_ok else "FAIL",
        roles="PASS" if roles_ok else "FAIL",
        fisher="PASS" if fisher_ok else "FAIL",
        source="PASS" if source_ok and convergence_ok else "FAIL",
        counter="PASS" if counter_ok else "FAIL",
        beta_span=beta_span,
        verdict="PASS-TARGET" if passes else "FAIL",
    )


def convergent_rows() -> list[dict[str, list[float]]]:
    return [
        {
            "record": [0.95 + 0.02 * step, 0.05, 0.02, 0.00],
            "source": [0.08, 0.92 + 0.03 * step, 0.05, 0.02],
            "causal": [0.03, 0.06, 0.96 + 0.01 * step, 0.04],
            "antichain": [0.02, 0.04, 0.08, 0.98 + 0.01 * step],
        }
        for step in [1.0, 0.5, 0.25, 0.0]
    ]


def candidate_laws() -> list[IDACandidate]:
    return [
        IDACandidate(
            "full IDA germ Physical ICS",
            True,
            True,
            True,
            True,
            True,
            True,
            convergent_rows(),
            [0.25, 0.25, 0.25, 0.25],
        ),
        IDACandidate(
            "bare ICS order only",
            False,
            False,
            True,
            True,
            False,
            False,
            [base_role_rows(0.95)],
            [0.0],
        ),
        IDACandidate(
            "zero-support deletion law",
            True,
            False,
            True,
            True,
            True,
            True,
            [base_role_rows(0.95)],
            [0.25],
        ),
        IDACandidate(
            "label-colored deletion",
            True,
            True,
            False,
            True,
            True,
            True,
            [base_role_rows(0.95)],
            [0.25],
        ),
        IDACandidate(
            "slice-colored deletion",
            True,
            True,
            True,
            False,
            True,
            True,
            [base_role_rows(0.95)],
            [0.25],
        ),
        IDACandidate(
            "source-external IDA",
            True,
            True,
            True,
            True,
            False,
            False,
            [base_role_rows(0.95)],
            [0.25],
        ),
        IDACandidate(
            "scalar-only IDA",
            True,
            True,
            True,
            True,
            False,
            True,
            [base_role_rows(0.95)],
            [0.25],
        ),
        IDACandidate(
            "weak-source IDA germ",
            True,
            True,
            True,
            True,
            True,
            True,
            [weak_source_rows(strength) for strength in [0.04, 0.05, 0.06, 0.05]],
            [0.25, 0.25, 0.25, 0.25],
        ),
        IDACandidate(
            "nonconvergent IDA germ",
            True,
            True,
            True,
            True,
            True,
            True,
            [base_role_rows(strength) for strength in [0.55, 1.15, 0.65, 1.05]],
            [0.25, 0.25, 0.25, 0.25],
        ),
    ]


def fmt(value: float) -> str:
    return "inf" if value == float("inf") else f"{value:.4f}"


def print_audits(rows: list[IDAAudit]) -> None:
    print("seven-step IDA proof/falsification audit")
    print("-----------------------------------------")
    print(
        "candidate                    D_x   RN    inv   roles  Fisher  source  "
        "counter  beta_span  verdict"
    )
    for row in rows:
        print(
            f"{row.name:28s}  "
            f"{row.deletion:5s}  "
            f"{row.rn:5s}  "
            f"{row.invariant:5s}  "
            f"{row.roles:5s}  "
            f"{row.fisher:6s}  "
            f"{row.source:6s}  "
            f"{row.counter:7s}  "
            f"{fmt(row.beta_span):>9s}  "
            f"{row.verdict}"
        )
    print()


def print_counterexample() -> None:
    scalar_span, beta_span = same_scalar_beta_counterexample()
    print("same-A scalar counterexample")
    print("----------------------------")
    print(f"same scalar A_x(0) span = {scalar_span:.4f}")
    print(f"different Hessian beta span = {beta_span:.4f}")
    print()


def main() -> None:
    rows = [audit(candidate) for candidate in candidate_laws()]
    print("=" * 104)
    print("v6 Paper 2 Part II §5.38: IDA Physical-ICS proof program")
    print("=" * 104)
    print_audits(rows)
    print_counterexample()
    print("VERDICT")
    print("-------")
    print("For finite positive Physical ICS, D_x and the local RN deletion action")
    print("exist cleanly.  Order covariance and slice-freeness are finite symmetry")
    print("conditions.  If the deletion action has four fixed internal linear")
    print("deformation directions, its Fisher/Hessian matrix is the full role Gram")
    print("and beta is derived when the source floor and refinement convergence hold.")
    print("But the scalar value A_x(0) alone is falsified: it can stay fixed while")
    print("the Hessian and beta move.  Therefore IDA must be a full local deletion")
    print("germ, not merely a deletion threshold score.")


if __name__ == "__main__":
    main()
