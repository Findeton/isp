"""
v6 Paper 2 Part II §5.32: microcausal TS gate.

The finite scalar TS receipt in §5.12 used diagonal projectors.  Branch A
needs more: threshold operations must be local microcausal projectors, and
arbitrary spacelike ordering loops must have no residue.

This pure-Python diagnostic builds a three-cell spacelike finite algebra.  It
checks:
    1. pairwise commutator norms of threshold projectors;
    2. maximum permutation-loop residue P_pi(0)P_pi(1)P_pi(2);
    3. whether the source/readout roles are pre-threshold local objects.

Nonlocal tails and preferred-slice orderings are rejected even if they look
small, because their residues are finite and order-sensitive.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations
from math import sqrt


Matrix = list[list[complex]]

I2: Matrix = [[1.0, 0.0], [0.0, 1.0]]
PZ: Matrix = [[1.0, 0.0], [0.0, 0.0]]
PX: Matrix = [[0.5, 0.5], [0.5, 0.5]]


@dataclass
class TSCandidate:
    name: str
    projectors: list[Matrix]
    source_stage: str
    local_supports: list[set[int]]
    role_complete: bool
    nonlinear: bool = False


@dataclass
class TSAudit:
    candidate: str
    role_complete: bool
    source_stage: str
    local: bool
    nonlinear: bool
    comm_norm: float
    loop_residue: float
    verdict: str


def zeros(n: int, m: int) -> Matrix:
    return [[0.0j for _ in range(m)] for _ in range(n)]


def eye(n: int) -> Matrix:
    out = zeros(n, n)
    for i in range(n):
        out[i][i] = 1.0
    return out


def matmul(a: Matrix, b: Matrix) -> Matrix:
    n, k, m = len(a), len(b), len(b[0])
    out = zeros(n, m)
    for i in range(n):
        for j in range(m):
            out[i][j] = sum(a[i][r] * b[r][j] for r in range(k))
    return out


def matsub(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def fro_norm(a: Matrix) -> float:
    return sqrt(sum(abs(x) ** 2 for row in a for x in row))


def kron(a: Matrix, b: Matrix) -> Matrix:
    out = zeros(len(a) * len(b), len(a[0]) * len(b[0]))
    for i in range(len(a)):
        for j in range(len(a[0])):
            for k in range(len(b)):
                for l in range(len(b[0])):
                    out[i * len(b) + k][j * len(b[0]) + l] = a[i][j] * b[k][l]
    return out


def kron3(a: Matrix, b: Matrix, c: Matrix) -> Matrix:
    return kron(kron(a, b), c)


def cell_projector(cell: int, p: Matrix) -> Matrix:
    ops = [I2, I2, I2]
    ops[cell] = p
    return kron3(ops[0], ops[1], ops[2])


def two_cell_projector(first: int, p_first: Matrix, second: int, p_second: Matrix) -> Matrix:
    ops = [I2, I2, I2]
    ops[first] = p_first
    ops[second] = p_second
    return kron3(ops[0], ops[1], ops[2])


def rank_one_projector(v: list[complex]) -> Matrix:
    n = sqrt(sum(abs(x) ** 2 for x in v))
    u = [x / n for x in v]
    return [[u[i] * u[j].conjugate() for j in range(len(u))] for i in range(len(u))]


def rotated_projector(theta: float, phase: complex = 1.0) -> Matrix:
    return rank_one_projector([sqrt(max(0.0, 1.0 - theta * theta)), phase * theta])


def max_commutator(projectors: list[Matrix]) -> float:
    out = 0.0
    for i in range(len(projectors)):
        for j in range(i + 1, len(projectors)):
            comm = matsub(matmul(projectors[i], projectors[j]), matmul(projectors[j], projectors[i]))
            out = max(out, fro_norm(comm))
    return out


def max_loop_residue(projectors: list[Matrix]) -> float:
    products = []
    for perm in permutations(range(len(projectors))):
        p = eye(len(projectors[0]))
        for idx in perm:
            p = matmul(p, projectors[idx])
        products.append(p)
    out = 0.0
    for i in range(len(products)):
        for j in range(i + 1, len(products)):
            out = max(out, fro_norm(matsub(products[i], products[j])))
    return out


def support_is_local(candidate: TSCandidate) -> bool:
    return all(support == {i} for i, support in enumerate(candidate.local_supports))


def audit(candidate: TSCandidate) -> TSAudit:
    comm = max_commutator(candidate.projectors)
    loop = max_loop_residue(candidate.projectors)
    local = support_is_local(candidate)
    passes = (
        candidate.role_complete
        and candidate.source_stage == "pre"
        and local
        and not candidate.nonlinear
        and comm <= 1e-12
        and loop <= 1e-12
    )
    return TSAudit(
        candidate=candidate.name,
        role_complete=candidate.role_complete,
        source_stage=candidate.source_stage,
        local=local,
        nonlinear=candidate.nonlinear,
        comm_norm=comm,
        loop_residue=loop,
        verdict="PASS" if passes else "FAIL",
    )


def candidates() -> list[TSCandidate]:
    local_full = TSCandidate(
        "local full scalar",
        [cell_projector(0, PZ), cell_projector(1, PZ), cell_projector(2, PZ)],
        "pre",
        [{0}, {1}, {2}],
        True,
    )
    local_rotated = TSCandidate(
        "local rotated scalar",
        [
            cell_projector(0, rotated_projector(0.30)),
            cell_projector(1, rotated_projector(0.20, 1.0j)),
            cell_projector(2, rotated_projector(0.25)),
        ],
        "pre",
        [{0}, {1}, {2}],
        True,
    )
    diagonal_receipt_only = TSCandidate(
        "diagonal receipt only",
        [cell_projector(0, PZ), cell_projector(1, PZ), cell_projector(2, PZ)],
        "absent",
        [{0}, {1}, {2}],
        False,
    )
    nonlocal_tail = TSCandidate(
        "nonlocal source tail",
        [
            two_cell_projector(0, PZ, 1, PX),
            cell_projector(1, PZ),
            cell_projector(2, PZ),
        ],
        "pre",
        [{0, 1}, {1}, {2}],
        True,
    )
    preferred_slice = TSCandidate(
        "preferred-slice update",
        [
            two_cell_projector(0, PZ, 1, PX),
            two_cell_projector(0, PX, 1, PZ),
            cell_projector(2, PZ),
        ],
        "pre",
        [{0, 1}, {0, 1}, {2}],
        True,
    )
    post_source = TSCandidate(
        "post-source local",
        [cell_projector(0, PZ), cell_projector(1, PZ), cell_projector(2, PZ)],
        "post",
        [{0}, {1}, {2}],
        True,
    )
    nonlinear = TSCandidate(
        "state nonlinear local",
        [cell_projector(0, PZ), cell_projector(1, PZ), cell_projector(2, PZ)],
        "pre",
        [{0}, {1}, {2}],
        True,
        nonlinear=True,
    )
    return [
        local_full,
        local_rotated,
        diagonal_receipt_only,
        nonlocal_tail,
        preferred_slice,
        post_source,
        nonlinear,
    ]


def print_audits(rows: list[TSAudit]) -> None:
    print("microcausal TS gate")
    print("-------------------")
    print(
        "candidate                roles  source  local  nonlinear  "
        "comm_norm  loop_residue  verdict"
    )
    for row in rows:
        print(
            f"{row.candidate:24s}  "
            f"{('yes' if row.role_complete else 'no'):5s}  "
            f"{row.source_stage:6s}  "
            f"{('yes' if row.local else 'no'):5s}  "
            f"{('yes' if row.nonlinear else 'no'):9s}  "
            f"{row.comm_norm:9.3e}  "
            f"{row.loop_residue:12.3e}  "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    rows = [audit(candidate) for candidate in candidates()]
    print("=" * 104)
    print("v6 Paper 2 Part II §5.32: microcausal TS gate")
    print("=" * 104)
    print_audits(rows)
    print("VERDICT")
    print("-------")
    print("Local threshold projectors give zero pairwise and loop residue")
    print("for arbitrary spacelike orderings.  Diagonal receipts, nonlocal")
    print("tails, post-source updates, preferred-slice couplings, and")
    print("state-nonlinear rules do not satisfy the full Branch-A gate.")


if __name__ == "__main__":
    main()
