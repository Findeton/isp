#!/usr/bin/env python3
"""D34c exact receipt: finite typed-DAG actor/quantum sewing.

Pin: note-d33-history-law-phase.md §11, commit f861328, before this file.

This receipt does NOT derive the D34b weights or nature's quantum law.  It
tests a compatibility construction on finite typed D34b wire-DAGs.  The
original consecutive-A depth-two skeleton is retained as one exact specimen;
incoming receptions, a two-tip merge and a disconnected actor factor are
separate explicit specimens.  No timed incoming-event marginal is claimed:

* durable D34b click alternatives have event-local orthogonal flags;
* unrecorded alternatives between clicks may retain interference;
* every branch operation is an isometry on the total declared ontology;
* preparation-independent flagged branches form a Busch/NSE channel;
* the finite decoherence functional is an exact strongly-positive Gram form.

The operational diamond uses four qubits S,R,P,O and exact Q(sqrt(2))
arithmetic.  No float, eigensolver, random sample, or numerical tolerance is
used.  Gates C0--C9; C9 is the dependent scope scorecard.  Exit 1 on failure.
"""

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
import math
import sys


@dataclass(frozen=True)
class Q2:
    """a + b sqrt(2), a,b rational."""

    a: F = F(0)
    b: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, "a", F(self.a))
        object.__setattr__(self, "b", F(self.b))

    @staticmethod
    def lift(x):
        return x if isinstance(x, Q2) else Q2(F(x), F(0))

    def __add__(self, other):
        z = Q2.lift(other)
        return Q2(self.a + z.a, self.b + z.b)

    __radd__ = __add__

    def __neg__(self):
        return Q2(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-Q2.lift(other))

    def __rsub__(self, other):
        return Q2.lift(other) - self

    def __mul__(self, other):
        z = Q2.lift(other)
        return Q2(self.a * z.a + 2 * self.b * z.b,
                  self.a * z.b + self.b * z.a)

    __rmul__ = __mul__

    def __truediv__(self, other):
        z = Q2.lift(other)
        if z.b != 0 or z.a == 0:
            raise ValueError("receipt divides only by nonzero rationals")
        return Q2(self.a / z.a, self.b / z.a)

    def __bool__(self):
        return self.a != 0 or self.b != 0

    def text(self):
        if self.b == 0:
            return str(self.a)
        if self.a == 0:
            return f"{self.b}*sqrt2"
        return f"{self.a}+{self.b}*sqrt2"


ZERO = Q2()
ONE = Q2(1)
HALF = Q2(F(1, 2))
ROOT_HALF = Q2(0, F(1, 2))  # sqrt(2)/2 = 1/sqrt(2)

PASS = 0
FAIL = 0


def check(label, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "[PASS]"
    else:
        FAIL += 1
        tag = "[FAIL]"
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))


def zeros(rows, cols):
    return [[ZERO for _ in range(cols)] for _ in range(rows)]


def eye(n):
    out = zeros(n, n)
    for i in range(n):
        out[i][i] = ONE
    return out


def transpose(a):
    return [list(row) for row in zip(*a)]


def mm(a, b):
    if len(a[0]) != len(b):
        raise ValueError("matrix shape")
    bt = transpose(b)
    return [[sum((x * y for x, y in zip(row, col)), ZERO)
             for col in bt] for row in a]


def mv(a, v):
    return [sum((x * y for x, y in zip(row, v)), ZERO) for row in a]


def madd(a, b):
    return [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def mscale(c, a):
    return [[c * x for x in row] for row in a]


def inner(v, w):
    # Every matrix/vector in this receipt is real.  Q2 is closed under it.
    return sum((x * y for x, y in zip(v, w)), ZERO)


def basis(n, j):
    v = [ZERO] * n
    v[j] = ONE
    return v


def matrix_from_apply(n, fn):
    cols = [fn(basis(n, j)) for j in range(n)]
    return transpose(cols)


def kron_matrix(a, b):
    return [[a[i][j] * b[r][c]
             for j in range(len(a[0])) for c in range(len(b[0]))]
            for i in range(len(a)) for r in range(len(b))]


def rank_rational(a):
    """Exact row rank for a matrix whose Q2 entries are rational."""
    rows = []
    for row in a:
        if any(x.b != 0 for x in row):
            raise ValueError("rank_rational received irrational entry")
        rows.append([x.a for x in row])
    rank = 0
    col = 0
    while rank < len(rows) and col < len(rows[0]):
        pivot = next((r for r in range(rank, len(rows))
                      if rows[r][col] != 0), None)
        if pivot is None:
            col += 1
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        p = rows[rank][col]
        rows[rank] = [x / p for x in rows[rank]]
        for r in range(len(rows)):
            if r == rank or rows[r][col] == 0:
                continue
            q = rows[r][col]
            rows[r] = [x - q * y for x, y in zip(rows[r], rows[rank])]
        rank += 1
        col += 1
    return rank


NQ = 4
DIM = 1 << NQ
S, R, P, O = range(4)


def mask(q):
    return 1 << (NQ - 1 - q)


def bit(i, q):
    return 1 if i & mask(q) else 0


def apply_h(v, q):
    out = [ZERO] * len(v)
    m = mask(q)
    for i in range(len(v)):
        if not i & m:
            j = i | m
            out[i] = ROOT_HALF * (v[i] + v[j])
            out[j] = ROOT_HALF * (v[i] - v[j])
    return out


def apply_z(v, q):
    return [(-x if bit(i, q) else x) for i, x in enumerate(v)]


def apply_x(v, q):
    out = [ZERO] * len(v)
    m = mask(q)
    for i, x in enumerate(v):
        out[i ^ m] = x
    return out


def apply_cnot(v, control, target):
    out = [ZERO] * len(v)
    tm = mask(target)
    for i, x in enumerate(v):
        out[i ^ tm if bit(i, control) else i] = x
    return out


def apply_cz(v, q1, q2):
    return [(-x if bit(i, q1) and bit(i, q2) else x)
            for i, x in enumerate(v)]


def project_qubit(v, q, value):
    return [x if bit(i, q) == value else ZERO for i, x in enumerate(v)]


def apply_local_matrix(v, q, a2):
    out = [ZERO] * len(v)
    m = mask(q)
    for i in range(len(v)):
        if i & m:
            continue
        j = i | m
        out[i] = a2[0][0] * v[i] + a2[0][1] * v[j]
        out[j] = a2[1][0] * v[i] + a2[1][1] * v[j]
    return out


I2 = eye(2)
X2 = [[ZERO, ONE], [ONE, ZERO]]
Z2 = [[ONE, ZERO], [ZERO, -ONE]]
P0 = [[ONE, ZERO], [ZERO, ZERO]]
P1 = [[ZERO, ZERO], [ZERO, ONE]]


def op_a(v):
    return apply_cnot(v, S, R)


def op_b(v):
    return apply_z(v, P)


def op_c(v):
    return apply_cz(v, S, P)


def op_hp(v):
    return apply_h(v, P)


def op_dcopy(v):
    return apply_cnot(v, P, O)


def op_hs(v):
    return apply_h(v, S)


OPS = {
    "a": matrix_from_apply(DIM, op_a),
    "b": matrix_from_apply(DIM, op_b),
    "c": matrix_from_apply(DIM, op_c),
    "hp": matrix_from_apply(DIM, op_hp),
    "dcopy": matrix_from_apply(DIM, op_dcopy),
    "hs": matrix_from_apply(DIM, op_hs),
}


def sequence_operator(names):
    out = eye(DIM)
    for name in names:
        out = mm(OPS[name], out)
    return out


initial = basis(DIM, 0)
initial = apply_h(initial, S)
initial = apply_h(initial, P)

HISTORIES = list(product((0, 1), repeat=3))  # (s,p,o)


def branch_full(order, s, p, o):
    v = list(initial)
    for name in order:
        v = op_a(v) if name == "a" else op_b(v)
    v = project_qubit(v, R, s)
    v = project_qubit(v, P, p)
    v = op_c(v)
    v = op_hp(v)
    v = op_dcopy(v)
    return project_qubit(v, O, o)


def branch_sp(order, s, p):
    v = list(initial)
    for name in order:
        v = op_a(v) if name == "a" else op_b(v)
    return project_qubit(project_qubit(v, R, s), P, p)


def branch_s(order, s):
    v = list(initial)
    for name in order:
        v = op_a(v) if name == "a" else op_b(v)
    return project_qubit(v, R, s)


def gram(vectors):
    return [[inner(v, w) for w in vectors] for v in vectors]


def incidence_coarse(dmat, labels, keyfn):
    groups = sorted(set(keyfn(x) for x in labels))
    pos = {g: i for i, g in enumerate(groups)}
    inc = zeros(len(groups), len(labels))
    for j, label in enumerate(labels):
        inc[pos[keyfn(label)]][j] = ONE
    return groups, mm(mm(inc, dmat), transpose(inc)), inc


print("[d34c — exact finite typed-DAG actor/quantum sewing]")


# C0: types and licensed questions.
durable_fields = ("s", "o")
unrecorded_fields = ("p",)
types_ok = (len(HISTORIES) == 8 and durable_fields == ("s", "o")
            and unrecorded_fields == ("p",))
check(
    "C0 TYPE LEDGER [dependent declaration]: D34b clock/mark law, durable click fields, "
    "unrecorded path alternatives, class-operator branches, the quantum "
    "functional, and the NSE closure are separate objects; only decoherent "
    "record questions are licensed probabilities",
    types_ok,
    "8 histories; durable=(s,o); unrecorded=(p)",
)


# C1: construction-order gauge and a noncommuting negative control.
ab_commutes = mm(OPS["a"], OPS["b"]) == mm(OPS["b"], OPS["a"])
branches_ab = [branch_full(("a", "b"), *h) for h in HISTORIES]
branches_ba = [branch_full(("b", "a"), *h) for h in HISTORIES]
d_ab = gram(branches_ab)
d_ba = gram(branches_ba)
shared_noncommutes = mm(OPS["a"], OPS["hs"]) != mm(OPS["hs"], OPS["a"])
shared_state_diff = mv(mm(OPS["a"], OPS["hs"]), initial) != mv(
    mm(OPS["hs"], OPS["a"]), initial
)
check(
    "C1 EXACT DIAMOND / ORDER GAUGE: disjoint incomparable a=CNOT(S,R) "
    "and b=Z(P) commute, and ab/ba give identical branch vectors and D; "
    "a shared-S H/CNOT reorder is a differing noncommuting control",
    ab_commutes and branches_ab == branches_ba and d_ab == d_ba
    and shared_noncommutes and shared_state_diff,
    "ab=ba exact; 8/8 branches equal; shared-carrier control differs",
)


# C2: exact formula, normalization, Hermiticity, Gram positivity and blocks.
formula_ok = True
for i, (s, p, o) in enumerate(HISTORIES):
    for j, (ss, pp, oo) in enumerate(HISTORIES):
        sign = -1 if (p * (1 + s + o) + pp * (1 + ss + oo)) % 2 else 1
        expected = Q2(F(sign, 8)) if s == ss and o == oo else ZERO
        formula_ok &= d_ab[i][j] == expected

hermitian = d_ab == transpose(d_ab)
normalized = sum((sum(row, ZERO) for row in d_ab), ZERO) == ONE
block_ok = True
for s, o in product((0, 1), repeat=2):
    ids = [HISTORIES.index((s, p, o)) for p in (0, 1)]
    block = [[d_ab[i][j] for j in ids] for i in ids]
    eta = -1 if (1 + s + o) % 2 else 1
    vplus = [ONE, Q2(eta)]
    vzero = [ONE, Q2(-eta)]
    block_ok &= mv(block, vplus) == [Q2(F(1, 4)) * x for x in vplus]
    block_ok &= mv(block, vzero) == [ZERO, ZERO]
rank = rank_rational(d_ab)

groups_so, d_so, inc_so = incidence_coarse(
    d_ab, HISTORIES, lambda h: (h[0], h[2])
)
groups_s, d_s_from_full, inc_s = incidence_coarse(
    d_ab, HISTORIES, lambda h: h[0]
)
_, d_s_via_so, _ = incidence_coarse(d_so, groups_so, lambda h: h[0])
coarse_associative = d_s_from_full == d_s_via_so
check(
    "C2 STRONGLY-POSITIVE FUNCTIONAL [exact]: D equals the pinned signed "
    "formula, is Hermitian and normalized, is a branch-vector Gram matrix, "
    "has four 2x2 blocks with eigenvalues (1/4,0), and incidence coarse "
    "graining is additive/associative",
    formula_ok and hermitian and normalized and block_ok and rank == 4
    and coarse_associative,
    "D=8x8; rank=4; spectrum={1/4 x4,0 x4}; sum(D)=1",
)


# C3: real interference and the recorded-path control.
prob_so = {g: d_so[i][i] for i, g in enumerate(groups_so)}
expected_so = {
    (0, 0): ZERO, (0, 1): HALF,
    (1, 0): HALF, (1, 1): ZERO,
}
diag_only = {}
for s, o in product((0, 1), repeat=2):
    diag_only[(s, o)] = sum(
        (d_ab[HISTORIES.index((s, p, o))][HISTORIES.index((s, p, o))]
         for p in (0, 1)), ZERO
    )

# Explicit orthogonal path receiver Q.  After the p projector, CNOT(P->Q)
# with Q initially |0> maps each four-qubit branch v_p to v_p tensor |p>.
# The modeled future acts on the first four factors only, so Q is support-
# excluded thereafter.  This independently constructs, rather than imposes,
# the recorded functional.
def append_path_receiver(v, p):
    out = [ZERO] * (2 * len(v))
    for i, x in enumerate(v):
        out[2 * i + p] = x
    return out


recorded_vectors = [
    append_path_receiver(branches_ab[i], HISTORIES[i][1])
    for i in range(len(HISTORIES))
]
d_path_recorded = gram(recorded_vectors)
masked_expected = [
    [d_ab[i][j] if HISTORIES[i][1] == HISTORIES[j][1] else ZERO
     for j in range(len(HISTORIES))]
    for i in range(len(HISTORIES))
]
_, recorded_so, _ = incidence_coarse(
    d_path_recorded, HISTORIES, lambda h: (h[0], h[2])
)
recorded_prob = {g: recorded_so[i][i] for i, g in enumerate(groups_so)}
offdiag_nonzero = sum(
    bool(d_ab[i][j]) for i in range(8) for j in range(8) if i != j
)
check(
    "C3 GENUINE INTERFERENCE: summing the unrecorded path at amplitude "
    "level gives P(s,o)=1/2 delta(o,1-s); diagonal-only reading gives "
    "1/4 in all four cells; an orthogonal path record deletes the "
    "off-diagonals and produces that diagonal law",
    prob_so == expected_so
    and all(x == Q2(F(1, 4)) for x in diag_only.values())
    and all(x == Q2(F(1, 4)) for x in recorded_prob.values())
    and d_path_recorded == masked_expected and offdiag_nonzero == 8,
    "coherent=(0,1/2,1/2,0); explicit Q-receiver=(1/4)x4; "
    "Gram=masked D; offdiag=8",
)


# C4: direct functionals at earlier cuts versus exact pushdown.
labels_sp = list(product((0, 1), repeat=2))
d_sp_direct = gram([branch_sp(("a", "b"), *h) for h in labels_sp])
groups_sp, d_sp_from_full, _ = incidence_coarse(
    d_ab, HISTORIES, lambda h: (h[0], h[1])
)
labels_s = [0, 1]
d_s_direct = gram([branch_s(("a", "b"), s) for s in labels_s])
_, d_s_from_sp, _ = incidence_coarse(d_sp_direct, labels_sp, lambda h: h[0])
check(
    "C4 FINITE CYLINDER RESTRICTION: the directly computed s, (s,p), "
    "and (s,p,o) functionals agree exactly under incidence pushdown; "
    "future unitary evolution and exhaustive later alternatives do not "
    "alter an earlier cylinder functional",
    groups_sp == labels_sp and d_sp_from_full == d_sp_direct
    and d_s_from_sp == d_s_direct and d_s_from_full == d_s_direct,
    "(s,p,o)->(s,p)->s exact; dimensions 8->4->2",
)


# C5: seal durability and source-value preservation are distinct.
u_future = sequence_operator(("b", "c", "hp", "dcopy"))
u_total = sequence_operator(("a", "b", "c", "hp", "dcopy"))


def lifted_local(a2, q):
    return matrix_from_apply(DIM, lambda v: apply_local_matrix(v, q, a2))


matrix_units = (
    [[ONE, ZERO], [ZERO, ZERO]],
    [[ZERO, ONE], [ZERO, ZERO]],
    [[ZERO, ZERO], [ONE, ZERO]],
    [[ZERO, ZERO], [ZERO, ONE]],
)
full_r_stable = True
each_future_stable = True
for eij in matrix_units:
    ar = lifted_local(eij, R)
    full_r_stable &= mm(mm(transpose(u_future), ar), u_future) == ar
    for name in ("b", "c", "hp", "dcopy"):
        unow = OPS[name]
        each_future_stable &= mm(mm(transpose(unow), ar), unow) == ar

source_value_stable = True
for ps in (P0, P1):
    aps = lifted_local(ps, S)
    source_value_stable &= mm(mm(transpose(u_total), aps), u_total) == aps
x_s = lifted_local(X2, S)
source_phase_changes = mm(mm(transpose(u_total), x_s), u_total) != x_s
x_r = lifted_local(X2, R)
xrxs = mm(x_r, x_s)
relational_changes = mm(mm(transpose(OPS["c"]), xrxs), OPS["c"]) != xrxs
check(
    "C5 SUPPORT-EXCLUDED LOCAL RECEIVER [exact, scoped]: after a creates "
    "R, each modeled future operation separately fixes the full local R "
    "matrix algebra because R is never touched. Source Z-value projectors "
    "survive while phase content disperses; a relational R-S observable "
    "changes, so this is quarantine/local durability, not sealed holonomy",
    full_r_stable and each_future_stable and source_value_stable
    and source_phase_changes and relational_changes,
    "R: 4/4 units fixed by 4/4 future ops; S:P0/P1 fixed,X changed; "
    "X_R X_S changes",
)


# C6: exact Busch-form flagged lift at D34b weights.
weights = (Q2(F(1, 4)), Q2(F(1, 4)), Q2(F(1, 2)))
test_unitaries = (I2, X2, Z2)


def flagged_isometry(flag, u2):
    out = zeros(6, 2)
    for r in range(2):
        for c in range(2):
            out[2 * flag + r][c] = u2[r][c]
    return out


w_kinds = [flagged_isometry(k, u) for k, u in enumerate(test_unitaries)]
orthogonal_ranges = True
for i, wi in enumerate(w_kinds):
    for j, wj in enumerate(w_kinds):
        target = I2 if i == j else zeros(2, 2)
        orthogonal_ranges &= mm(transpose(wi), wj) == target


def density_channel_flagged(rho):
    out = zeros(6, 6)
    for w, vk in zip(weights, w_kinds):
        out = madd(out, mscale(w, mm(mm(vk, rho), transpose(vk))))
    return out


rho0 = [[ONE, ZERO], [ZERO, ZERO]]
rho1 = [[ZERO, ZERO], [ZERO, ONE]]
rhop = [[HALF, HALF], [HALF, HALF]]
rhom = [[HALF, -HALF], [-HALF, HALF]]


def msub(a, b):
    return [[x - y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def square2(a):
    return mm(a, a)


def flagged_distance_certificate(rho, sigma, sqrt_c):
    delta = msub(rho, sigma)
    cmat = square2(delta)
    c = cmat[0][0]
    if cmat != [[c, ZERO], [ZERO, c]] or sqrt_c * sqrt_c != c:
        return False
    out_delta = msub(density_channel_flagged(rho),
                     density_channel_flagged(sigma))
    for k, w in enumerate(weights):
        block = [[out_delta[2 * k + i][2 * k + j]
                  for j in range(2)] for i in range(2)]
        expected = mscale(w, mm(mm(test_unitaries[k], delta),
                                transpose(test_unitaries[k])))
        if block != expected:
            return False
        if square2(block) != mscale(w * w * c, I2):
            return False
    # Each 2x2 traceless block has trace norm 2*w*sqrt(c).  The trace
    # distance is half their sum = sqrt(c) because sum weights = one.
    return sum(weights, ZERO) * sqrt_c == sqrt_c


nse_regression = (
    flagged_distance_certificate(rho0, rho1, ONE)
    and flagged_distance_certificate(rhop, rhom, ONE)
    and flagged_distance_certificate(rho0, rhop, ROOT_HALF)
)
check(
    "C6 ABSTRACT NSE / BUSCH LEMMA: fixed weights (1/4,1/4,1/2) multiply "
    "isometries with mutually orthogonal durable flag ranges. Exact "
    "noncommuting test pairs preserve trace distance; analytically the "
    "block trace norm sums to ||Delta||_1 for every input pair",
    sum(weights, ZERO) == ONE and orthogonal_ranges and nse_regression,
    "W_i^dag W_j=delta_ij I; three exact pair certificates; all-state "
    "block-norm theorem; fixed classical seed/graph sector",
)


# C7: the flags and preparation-independence are load-bearing.
def unitary_channel(u, rho):
    return mm(mm(u, rho), transpose(u))


def unflagged_dephase(rho):
    return mscale(HALF, madd(rho, unitary_channel(Z2, rho)))


unflag_plus = unflagged_dephase(rhop)
unflag_minus = unflagged_dephase(rhom)
unflag_contracts = unflag_plus == unflag_minus == [[HALF, ZERO], [ZERO, HALF]]

def state_reading_rule(rho):
    """Forbidden control: inspect <Z>, choose I for >=0 and X otherwise."""
    z = rho[0][0] - rho[1][1]
    if z.b != 0:
        raise ValueError("comparison witness must be rational")
    u = I2 if z.a >= 0 else X2
    return unitary_channel(u, rho)


# On rho0/rho1 both outputs are rho0, while the equal mixture has <Z>=0
# and is left as I/2.  Hence F((rho0+rho1)/2) != (F(rho0)+F(rho1))/2.
rho_mix = mscale(HALF, madd(rho0, rho1))
f0 = state_reading_rule(rho0)
f1 = state_reading_rule(rho1)
fmix = state_reading_rule(rho_mix)
affine_rhs = mscale(HALF, madd(f0, f1))
nonlinear = f0 == rho0 and f1 == rho0 and fmix == rho_mix
nonlinear &= fmix != affine_rhs
check(
    "C7 NEGATIVE CONTROLS: forgetting the flag in 1/2(I rho I + Z rho "
    "Z) sends |+> and |-> to the same state (distance 1 -> 0); a "
    "preparation-dependent branch rule fails affine linearity. Branch "
    "isometries alone are insufficient without retained flags and fixed "
    "weights",
    unflag_contracts and nonlinear,
    "unflagged D:1->0; state-dependent F(I/2)=I/2 != |0><0|",
)


# C8: actual A-local D34b actor cylinder, sequential quantum operations,
# factorized mailboxes, and remote quantum factorization.  Scope is the
# A-initiated local-ring stopping algebra through depth two—not timed X_T.


def actor_seed(pairs=(("A", "B"),)):
    actors = sorted({a for pair in pairs for a in pair})
    neighbors = {a: set() for a in actors}
    for a, b in pairs:
        neighbors[a].add(b)
        neighbors[b].add(a)
    return {
        "active": tuple(actors),
        "neighbors": neighbors,
        "births": {a: 0 for a in actors},
        "rings": {a: 0 for a in actors},
        "last": {},
        "events": (),
    }


def copy_actor_state(s):
    return {
        "active": tuple(s["active"]),
        "neighbors": {a: set(xs) for a, xs in s["neighbors"].items()},
        "births": dict(s["births"]),
        "rings": dict(s["rings"]),
        "last": dict(s["last"]),
        "events": tuple(s["events"]),
    }


def actor_options(s, initiator):
    ns = sorted(s["neighbors"][initiator])
    child = f"{initiator}/{s['births'][initiator] + 1}"
    return ([('b', child, F(1, 4))]
            + [('i', x, F(1, 4 * len(ns))) for x in ns]
            + [('n', None, F(1, 2))])


def actor_step(s, initiator, option):
    kind, target, weight = option
    z = copy_actor_state(s)
    z["rings"][initiator] += 1
    eid = f"{initiator}#r{z['rings'][initiator]}"
    if kind == "b":
        z["births"][initiator] += 1
        z["active"] = tuple(sorted(z["active"] + (target,)))
        z["neighbors"].setdefault(initiator, set()).add(target)
        z["neighbors"][target] = {initiator}
        z["births"][target] = 0
        z["rings"][target] = 0
    touched = (initiator,) if kind == "n" else (initiator, target)
    preds = tuple(sorted({z["last"][a] for a in touched if a in z["last"]}))
    event = (eid, initiator, kind, target, preds)
    z["events"] += (event,)
    for a in touched:
        z["last"][a] = eid
    return z, weight


depth1_paths = [actor_step(actor_seed(), "A", o)
                for o in actor_options(actor_seed(), "A")]
depth2_paths = []
for s1, m1 in depth1_paths:
    for option in actor_options(s1, "A"):
        s2, w2 = actor_step(s1, "A", option)
        depth2_paths.append((s2, m1 * w2))

mass1 = {s["events"]: m for s, m in depth1_paths}
mass2 = {s["events"]: m for s, m in depth2_paths}
classical_restriction = all(
    sum((m for evs, m in mass2.items() if evs[:1] == prefix), F(0)) == mass
    for prefix, mass in mass1.items()
)
row_normalization = all(
    sum((w for _, _, w in actor_options(s, "A")), F(0)) == 1
    for s, _ in depth1_paths
)
all_m_identity = F(1, 4) + F(1, 4) + F(1, 2) == 1
after_birth = next(s for s, _ in depth1_paths if s["events"][0][2] == "b")
degree_two_weights = sorted(
    w for k, _, w in actor_options(after_birth, "A") if k == "i"
) == [F(1, 8), F(1, 8)]


# Universal activated-carrier reference for this bounded cylinder.
AQ = 8
ADIM = 1 << AQ
ACTOR_Q = {"A": 0, "B": 1, "A/1": 2, "A/2": 3}
PATH_Q = {1: 4, 2: 6}
OUT_Q = {1: 5, 2: 7}


def amask(q):
    return 1 << (AQ - 1 - q)


def abit(i, q):
    return 1 if i & amask(q) else 0


def ah(v, q):
    out = [ZERO] * len(v)
    m = amask(q)
    for i in range(len(v)):
        if not i & m:
            j = i | m
            out[i] = ROOT_HALF * (v[i] + v[j])
            out[j] = ROOT_HALF * (v[i] - v[j])
    return out


def az(v, q):
    return [(-x if abit(i, q) else x) for i, x in enumerate(v)]


def acnot(v, control, target):
    out = [ZERO] * len(v)
    tm = amask(target)
    for i, x in enumerate(v):
        out[i ^ tm if abit(i, control) else i] = x
    return out


def acz(v, q1, q2):
    return [(-x if abit(i, q1) and abit(i, q2) else x)
            for i, x in enumerate(v)]


def aproject(v, q, value):
    return [x if abit(i, q) == value else ZERO for i, x in enumerate(v)]


def acry(v, control, target, c=Q2(F(4, 5)), s=Q2(F(3, 5))):
    out = [ZERO] * len(v)
    tm = amask(target)
    for i in range(len(v)):
        if i & tm:
            continue
        j = i | tm
        if abit(i, control):
            out[i] = c * v[i] - s * v[j]
            out[j] = s * v[i] + c * v[j]
        else:
            out[i], out[j] = v[i], v[j]
    return out


actor_initial = basis(ADIM, 0)
actor_initial = ah(actor_initial, ACTOR_Q["A"])
actor_initial = ah(actor_initial, PATH_Q[1])
actor_initial = ah(actor_initial, PATH_Q[2])


def sqrt_fraction_q2(x):
    x = F(x)
    rn, rd = math.isqrt(x.numerator), math.isqrt(x.denominator)
    if rn * rn == x.numerator and rd * rd == x.denominator:
        return Q2(F(rn, rd))
    half = x / 2
    rn, rd = math.isqrt(half.numerator), math.isqrt(half.denominator)
    if rn * rn == half.numerator and rd * rd == half.denominator:
        return Q2(0, F(rn, rd))
    raise ValueError(f"sqrt outside Q(sqrt2): {x}")


def interaction_branches(v, interaction_index, initiator, target):
    pathq, outq = PATH_Q[interaction_index], OUT_Q[interaction_index]
    v = acnot(v, ACTOR_Q[initiator], ACTOR_Q[target])
    rows = []
    for sval in (0, 1):
        vs = aproject(v, ACTOR_Q[target], sval)
        vs = az(vs, pathq)
        for pval in (0, 1):
            vp = aproject(vs, pathq, pval)
            vp = acz(vp, ACTOR_Q[initiator], pathq)
            vp = ah(vp, pathq)
            vp = acnot(vp, pathq, outq)
            for oval in (0, 1):
                rows.append(((sval, pval, oval), aproject(vp, outq, oval)))
    return rows


def canonical_graph(events):
    """Typed DAG key with auxiliary serialization erased."""
    return tuple(sorted(events, key=lambda event: event[0]))


def event_record_key(records):
    return tuple(sorted(records.items()))


def physical_record_key(events, records):
    return canonical_graph(events), event_record_key(records)


def factorized_record_inner(left_events, left_records,
                            right_events, right_records):
    """Product inner product over fresh event-record factors.

    Event incidence is a classical typed graph sector.  Each event node carries
    one bounded local outcome factor; no actor owns an append-only mailbox.
    """
    if canonical_graph(left_events) != canonical_graph(right_events):
        return ZERO
    for eid in set(left_records) | set(right_records):
        if left_records.get(eid) != right_records.get(eid):
            return ZERO
    return ONE


def write_event_record(records, event, internal):
    """Allocate one fresh bounded record factor for one typed graph node."""
    eid, _, kind, _, _ = event
    out = dict(records)
    if eid in out:
        raise ValueError("event record slot reused")
    durable = None if kind != "i" else (internal[0], internal[2])
    # Initiator, target and at most two predecessor links live in the typed
    # incidence relation.  Local quantum evidence is the bounded alphabet
    # {birth, idle, interaction x (s,o)}; p is deliberately absent.
    out[eid] = (kind, durable)
    return out


def quantum_branches(events, mass, initial=None):
    initial = actor_initial if initial is None else initial
    rows = [{
        "v": list(initial),
        "records": {},
        "internals": (),
        "record_prefixes": (),
    }]
    interaction_index = 0
    for event in events:
        _, initiator, kind, target, _ = event
        if initiator not in ACTOR_Q or (target is not None
                                        and target not in ACTOR_Q):
            raise ValueError("finite carrier does not contain typed actor")
        if kind == "i":
            interaction_index += 1
        nxt = []
        for row in rows:
            if kind == "b":
                variants = [(None, acry(row["v"], ACTOR_Q[initiator],
                                         ACTOR_Q[target]))]
            elif kind == "i":
                variants = interaction_branches(
                    row["v"], interaction_index, initiator, target
                )
            else:
                variants = [(None, list(row["v"]))]
            for internal, vnew in variants:
                records = write_event_record(row["records"], event, internal)
                rkey = physical_record_key(
                    tuple(events[:len(row["internals"]) + 1]), records
                )
                nxt.append({
                    "v": vnew,
                    "records": records,
                    "internals": row["internals"] + (internal,),
                    "record_prefixes": row["record_prefixes"] + (rkey,),
                })
        rows = nxt
    scale = sqrt_fraction_q2(mass)
    for row in rows:
        row["v"] = [scale * x for x in row["v"]]
        row["events"] = tuple(events)
        row["mass"] = mass
    return rows


qbranches1 = []
for state, mass in depth1_paths:
    qbranches1.extend(quantum_branches(state["events"], mass))
qbranches2 = []
for state, mass in depth2_paths:
    qbranches2.extend(quantum_branches(state["events"], mass))


def actor_functional(branches):
    out = zeros(len(branches), len(branches))
    for i in range(len(branches)):
        for j in range(len(branches)):
            flag_ip = factorized_record_inner(
                branches[i]["events"], branches[i]["records"],
                branches[j]["events"], branches[j]["records"],
            )
            if flag_ip:
                out[i][j] = inner(branches[i]["v"], branches[j]["v"])
    return out


d_actor1 = actor_functional(qbranches1)
d_actor2 = actor_functional(qbranches2)


def classical_shadow_from_d(dmat, branches):
    out = {}
    groups = defaultdict(list)
    for i, row in enumerate(branches):
        groups[row["events"]].append(i)
    for key, ids in groups.items():
        out[key] = sum((dmat[i][j] for i in ids for j in ids), ZERO)
    return out


shadow1 = classical_shadow_from_d(d_actor1, qbranches1)
shadow2 = classical_shadow_from_d(d_actor2, qbranches2)
shadow_ok = shadow1 == {k: Q2(v) for k, v in mass1.items()}
shadow_ok &= shadow2 == {k: Q2(v) for k, v in mass2.items()}


def prefix_label(row, n):
    return (canonical_graph(row["events"][:n]),
            row["record_prefixes"][n - 1],
            row["internals"][:n])


labels1 = [prefix_label(row, 1) for row in qbranches1]
label1_pos = {label: i for i, label in enumerate(labels1)}
labels_unique = len(label1_pos) == len(labels1)
inc21 = zeros(len(qbranches1), len(qbranches2))
for j, row in enumerate(qbranches2):
    inc21[label1_pos[prefix_label(row, 1)]][j] = ONE
d_actor2_down = mm(mm(inc21, d_actor2), transpose(inc21))
quantum_restriction = d_actor2_down == d_actor1


def durable_internal(x):
    return None if x is None else (x[0], x[2])


def durable_signature(row):
    return (canonical_graph(row["events"]),
            tuple(durable_internal(x) for x in row["internals"]))


# Equality of the fresh-record partition and the durable physical-signature
# partition is checked in both directions, with p deliberately omitted.
record_partition_ok = True
for left in qbranches2:
    for right in qbranches2:
        same_records = physical_record_key(
            left["events"], left["records"]
        ) == physical_record_key(right["events"], right["records"])
        record_partition_ok &= same_records == (
            durable_signature(left) == durable_signature(right)
        )

# Each event allocates one bounded local evidence factor and never mutates an
# earlier factor.  Typed incidence contains at most two predecessor links.
fresh_record_capacity = True
allowed_contents = {
    ("b", None), ("n", None),
    *(("i", (s, o)) for s, o in product((0, 1), repeat=2)),
}
for row in qbranches2:
    fresh_record_capacity &= len(row["records"]) == len(row["events"])
    fresh_record_capacity &= set(row["records"].values()) <= allowed_contents
    fresh_record_capacity &= all(len(event[4]) <= 2 for event in row["events"])
    final_items = set(event_record_key(row["records"]))
    for _, prefix_items in row["record_prefixes"]:
        fresh_record_capacity &= set(prefix_items) <= final_items

# Outgoing targets are passive: only A's private initiated ring advances in
# this conditioned skeleton, while the shared event belongs to both wires via
# typed incidence.
outgoing_target_passive = True
for state, _ in depth2_paths:
    outgoing_target_passive &= all(
        r == 0 for a, r in state["rings"].items() if a != "A"
    )

# The actual first interaction block carries the diamond interference on A,B.
first_i_key = next(k for k in mass1 if k[0][2] == "i")
ids_i = [i for i, row in enumerate(qbranches1) if row["events"] == first_i_key]
coherent_i = {}
diagonal_i = {}
for sval, oval in product((0, 1), repeat=2):
    ids = [i for i in ids_i
           if qbranches1[i]["internals"][0][0] == sval
           and qbranches1[i]["internals"][0][2] == oval]
    coherent_i[(sval, oval)] = sum(
        (d_actor1[i][j] for i in ids for j in ids), ZERO
    )
    diagonal_i[(sval, oval)] = sum((d_actor1[i][i] for i in ids), ZERO)
interaction_signature = coherent_i == {
    (0, 0): ZERO, (0, 1): Q2(F(1, 8)),
    (1, 0): Q2(F(1, 8)), (1, 1): ZERO,
}
interaction_signature &= all(v == Q2(F(1, 16)) for v in diagonal_i.values())

# Birth and idle are genuinely different actor operations and have no
# spectator diamond alternatives.  For the initial |+> parent, D24 g=9/25
# gives P(child=1)=9/50; the branch carries classical mass 1/4.
birth_key = next(k for k in mass1 if k[0][2] == "b")
idle_key = next(k for k in mass1 if k[0][2] == "n")
birth_rows = [r for r in qbranches1 if r["events"] == birth_key]
idle_rows = [r for r in qbranches1 if r["events"] == idle_key]
child_q = ACTOR_Q["A/1"]
birth_child_one = sum(
    (x * x for i, x in enumerate(birth_rows[0]["v"]) if abit(i, child_q)), ZERO
)
event_ops_tied = len(birth_rows) == 1 and len(idle_rows) == 1
event_ops_tied &= birth_child_one == Q2(F(9, 200))  # mass 1/4 * 9/50
event_ops_tied &= idle_rows[0]["v"] == [ROOT_HALF * x for x in actor_initial]
c45, s35 = Q2(F(4, 5)), Q2(F(3, 5))
event_ops_tied &= c45 * c45 + s35 * s35 == ONE

# Generic exact qubit operations used for the arbitrary-input instrument and
# the actual disconnected-actor specimens below.
def gmask(nq, q):
    return 1 << (nq - 1 - q)


def gbit(i, nq, q):
    return 1 if i & gmask(nq, q) else 0


def gh(v, nq, q):
    out = [ZERO] * len(v)
    m = gmask(nq, q)
    for i in range(len(v)):
        if not i & m:
            j = i | m
            out[i] = ROOT_HALF * (v[i] + v[j])
            out[j] = ROOT_HALF * (v[i] - v[j])
    return out


def gz(v, nq, q):
    return [(-x if gbit(i, nq, q) else x) for i, x in enumerate(v)]


def gcnot(v, nq, control, target):
    out = [ZERO] * len(v)
    tm = gmask(nq, target)
    for i, x in enumerate(v):
        out[i ^ tm if gbit(i, nq, control) else i] = x
    return out


def gcz(v, nq, q1, q2):
    return [(-x if gbit(i, nq, q1) and gbit(i, nq, q2) else x)
            for i, x in enumerate(v)]


def gproject(v, nq, q, value):
    return [x if gbit(i, nq, q) == value else ZERO
            for i, x in enumerate(v)]


def gcry(v, nq, control, target,
         c=Q2(F(4, 5)), s=Q2(F(3, 5))):
    out = [ZERO] * len(v)
    tm = gmask(nq, target)
    for i in range(len(v)):
        if i & tm:
            continue
        j = i | tm
        if gbit(i, nq, control):
            out[i] = c * v[i] - s * v[j]
            out[j] = s * v[i] + c * v[j]
        else:
            out[i], out[j] = v[i], v[j]
    return out


def from_columns(cols):
    return transpose(cols)


def operator_closure(ops):
    width = len(ops[0][0])
    out = zeros(width, width)
    for op in ops:
        out = madd(out, mm(transpose(op), op))
    return out


# Correct C_(x,r,p) -> K_(x,r) -> W_x typing on a universal local sector:
# actor slots A,B,C,D are the common 16-dimensional input.  At degree two B,C
# are existing targets and D is the next fresh child; birth acts on A,D while
# interaction acts on A,B or A,C after adjoining fresh P,O.
BASE_DIM = 16
birth_operator = matrix_from_apply(
    BASE_DIM, lambda v: gcry(v, 4, 0, 3)
)
idle_operator = eye(BASE_DIM)


def embed_interaction_input(j):
    # Preserve A,B,C,D; append P=|+>, O=|0>.
    out = [ZERO] * 64
    out[j << 2] = ROOT_HALF
    out[(j << 2) | 2] = ROOT_HALF
    return out


def interaction_class_operator(target, sval, pval, oval):
    cols = []
    for j in range(BASE_DIM):
        v = embed_interaction_input(j)
        v = gcnot(v, 6, 0, target)
        v = gproject(v, 6, target, sval)
        v = gz(v, 6, 4)
        v = gproject(v, 6, 4, pval)
        v = gcz(v, 6, 0, 4)
        v = gh(v, 6, 4)
        v = gcnot(v, 6, 4, 5)
        cols.append(gproject(v, 6, 5, oval))
    return from_columns(cols)


interaction_k = {}
interaction_closure = {}
for target in (1, 2):
    ks = []
    for sval, oval in product((0, 1), repeat=2):
        c0 = interaction_class_operator(target, sval, 0, oval)
        c1 = interaction_class_operator(target, sval, 1, oval)
        kso = madd(c0, c1)  # p is summed coherently, before Gram squaring.
        interaction_k[(target, sval, oval)] = kso
        ks.append(kso)
    interaction_closure[target] = operator_closure(ks)

birth_closure = mm(transpose(birth_operator), birth_operator)
idle_closure = mm(transpose(idle_operator), idle_operator)
event_instruments_are_isometries = (
    birth_closure == eye(BASE_DIM)
    and idle_closure == eye(BASE_DIM)
    and interaction_closure[1] == eye(BASE_DIM)
    and interaction_closure[2] == eye(BASE_DIM)
)
durable_result_not_isometry = any(
    mm(transpose(op), op) != eye(BASE_DIM)
    for op in interaction_k.values()
)
scheduler_degree1 = madd(
    madd(mscale(Q2(F(1, 4)), birth_closure),
         mscale(Q2(F(1, 4)), interaction_closure[1])),
    mscale(Q2(F(1, 2)), idle_closure),
)
scheduler_degree2 = madd(
    madd(mscale(Q2(F(1, 4)), birth_closure),
         mscale(Q2(F(1, 8)), interaction_closure[1])),
    madd(mscale(Q2(F(1, 8)), interaction_closure[2]),
         mscale(Q2(F(1, 2)), idle_closure)),
)
scheduler_operator_complete = (
    scheduler_degree1 == eye(BASE_DIM)
    and scheduler_degree2 == eye(BASE_DIM)
)


# Harden the original conditioned consecutive-A specimen.
actor_norm = sum((sum(row, ZERO) for row in d_actor2), ZERO) == ONE
actor_counts = (len(mass1), len(mass2), len(qbranches1), len(qbranches2))
incidence_structure = actor_counts == (3, 10, 10, 108)
incidence_structure &= all(
    sum((inc21[i][j] for i in range(len(inc21))), ZERO) == ONE
    for j in range(len(inc21[0]))
)
incidence_structure &= all(any(inc21[i][j] for j in range(len(inc21[0])))
                           for i in range(len(inc21)))
check(
    "C8 CONSECUTIVE-A-INITIATED DEPTH-2 ACTION-SEWING [exact, "
    "conditioned specimen]: with non-A events suppressed, Ulam birth, "
    "changing degree/target, outgoing-target passive reception and "
    "predecessors are exact; idle, D24 birth and actual-target interaction "
    "operations compose. Every classical shadow is recovered and the real "
    "second instrument restricts 108->10",
    sum(mass1.values(), F(0)) == 1 and sum(mass2.values(), F(0)) == 1
    and classical_restriction and row_normalization and all_m_identity
    and degree_two_weights and actor_norm and shadow_ok and labels_unique
    and quantum_restriction and incidence_structure
    and outgoing_target_passive and interaction_signature and event_ops_tied,
    "conditioned/no incoming events; counts=(3,10,10,108); "
    "degree2 i=1/8+1/8; 108->10 exact",
)

check(
    "C9 BOUNDED EVENT RECORDS + ACTUAL-FAMILY NSE INSTRUMENT [exact]: each "
    "event creates one fresh bounded outcome factor and bounded-degree typed "
    "links; no actor mailbox grows. The durable signature and record "
    "partitions coincide modulo p. Correctly typed K_(x,r)=sum_p C_(x,r,p) "
    "gives W_x^dag W_x=I for idle, D24 birth and both interaction targets; "
    "degree-1/2 scheduler closures are I for arbitrary inputs",
    fresh_record_capacity and record_partition_ok
    and event_instruments_are_isometries and durable_result_not_isometry
    and scheduler_operator_complete and all_m_identity,
    "one factor/event; local alphabet=6; indegree<=2; operator closures "
    "16x16 exact; fresh degree-2 birth slot distinct from both targets; "
    "m*(1/4m)=1/4 for every positive m",
)


def physical_actor_state_key(state):
    return (
        tuple(state["active"]),
        tuple(sorted((a, tuple(sorted(xs)))
                     for a, xs in state["neighbors"].items())),
        tuple(sorted(state["births"].items())),
        tuple(sorted(state["rings"].items())),
        tuple(sorted(state["last"].items())),
        canonical_graph(state["events"]),
    )


def branch_vector_map(rows):
    return {
        (physical_record_key(row["events"], row["records"]),
         row["internals"]): row["v"]
        for row in rows
    }


# Incoming reception: B rings, touches A, and changes A's carrier/record wire
# without consuming A's private ring; A's next event inherits B#r1.
incoming_state, _ = actor_step(
    actor_seed(), "B", ("i", "A", F(1, 4))
)
incoming_then_a, _ = actor_step(
    incoming_state, "A", ("n", None, F(1, 2))
)
incoming_initial = basis(ADIM, 0)
incoming_initial = ah(incoming_initial, ACTOR_Q["B"])
incoming_initial = ah(incoming_initial, PATH_Q[1])
incoming_initial = ah(incoming_initial, PATH_Q[2])
incoming_rows = quantum_branches(
    incoming_then_a["events"], F(1), initial=incoming_initial
)
incoming_sum = [sum((row["v"][i] for row in incoming_rows), ZERO)
                for i in range(ADIM)]
incoming_a_one = sum(
    (x * x for i, x in enumerate(incoming_sum)
     if abit(i, ACTOR_Q["A"])), ZERO
)
incoming_ok = (
    incoming_state["rings"]["A"] == 0
    and incoming_state["rings"]["B"] == 1
    and incoming_state["last"]["A"] == "B#r1"
    and incoming_state["last"]["B"] == "B#r1"
    and incoming_then_a["rings"]["A"] == 1
    and incoming_then_a["events"][-1][4] == ("B#r1",)
    and len(incoming_rows) == 8
    and all(len(row["records"]) == 2 for row in incoming_rows)
    and inner(incoming_sum, incoming_sum) == ONE
    and incoming_a_one == HALF
)

# Two independent private tips merge into one shared interaction.  Swapping
# the incomparable idles is gauge; the final interaction has both predecessors.
merge_ab, _ = actor_step(actor_seed(), "A", ("n", None, F(1)))
merge_ab, _ = actor_step(merge_ab, "B", ("n", None, F(1)))
merge_ab, _ = actor_step(merge_ab, "A", ("i", "B", F(1)))
merge_ba, _ = actor_step(actor_seed(), "B", ("n", None, F(1)))
merge_ba, _ = actor_step(merge_ba, "A", ("n", None, F(1)))
merge_ba, _ = actor_step(merge_ba, "A", ("i", "B", F(1)))
merge_event = next(e for e in merge_ab["events"] if e[0] == "A#r2")
merge_rows_ab = quantum_branches(merge_ab["events"], F(1))
merge_rows_ba = quantum_branches(merge_ba["events"], F(1))
merge_ok = (
    merge_event[4] == ("A#r1", "B#r1")
    and physical_actor_state_key(merge_ab) == physical_actor_state_key(merge_ba)
    and branch_vector_map(merge_rows_ab) == branch_vector_map(merge_rows_ba)
)
check(
    "C10 INCOMING RECEPTION + TWO-TIP MERGE / ACTOR GAUGE [exact]: an "
    "incoming i(B,A) advances B but not A, changes A's carrier and becomes "
    "A's next predecessor. Independent A#r1/B#r1 tips then merge at "
    "i(A,B); both incomparable serializations give the identical typed DAG, "
    "fresh records and quantum class branches",
    incoming_ok and merge_ok,
    "incoming A-ring 0->0, P(A=1) 0->1/2; merge preds={A#r1,B#r1}; "
    "serialization erased exactly",
)


# Actual disconnected actors: A performs the diamond interaction on B while P
# performs the D24 birth on P/1.  The two event maps use disjoint carriers.
REMOTE_Q = 6
REMOTE_DIM = 1 << REMOTE_Q


def remote_interaction_full(v):
    v = gcnot(v, REMOTE_Q, 0, 1)
    v = gz(v, REMOTE_Q, 2)
    v = gcz(v, REMOTE_Q, 0, 2)
    v = gh(v, REMOTE_Q, 2)
    return gcnot(v, REMOTE_Q, 2, 3)


def remote_interaction_class(v, sval, pval, oval):
    v = gcnot(v, REMOTE_Q, 0, 1)
    v = gproject(v, REMOTE_Q, 1, sval)
    v = gz(v, REMOTE_Q, 2)
    v = gproject(v, REMOTE_Q, 2, pval)
    v = gcz(v, REMOTE_Q, 0, 2)
    v = gh(v, REMOTE_Q, 2)
    v = gcnot(v, REMOTE_Q, 2, 3)
    return gproject(v, REMOTE_Q, 3, oval)


def remote_birth_full(v):
    return gcry(v, REMOTE_Q, 4, 5)


remote_operator_commutes = all(
    remote_birth_full(remote_interaction_full(basis(REMOTE_DIM, j)))
    == remote_interaction_full(remote_birth_full(basis(REMOTE_DIM, j)))
    for j in range(REMOTE_DIM)
)
remote_initial = basis(REMOTE_DIM, 0)
for q in (0, 2, 4):
    remote_initial = gh(remote_initial, REMOTE_Q, q)
remote_labels = list(product((0, 1), repeat=3))
remote_order_ib = [
    remote_birth_full(remote_interaction_class(remote_initial, *h))
    for h in remote_labels
]
remote_order_bi = [
    remote_interaction_class(remote_birth_full(remote_initial), *h)
    for h in remote_labels
]
remote_d = zeros(8, 8)
for i, left in enumerate(remote_labels):
    for j, right in enumerate(remote_labels):
        if left[0] == right[0] and left[2] == right[2]:
            remote_d[i][j] = inner(remote_order_ib[i], remote_order_ib[j])

remote_ab, _ = actor_step(
    actor_seed((("A", "B"), ("P", "Q"))),
    "A", ("i", "B", F(1)),
)
remote_ab, _ = actor_step(
    remote_ab, "P", ("b", "P/1", F(1)),
)
remote_ba, _ = actor_step(
    actor_seed((("A", "B"), ("P", "Q"))),
    "P", ("b", "P/1", F(1)),
)
remote_ba, _ = actor_step(
    remote_ba, "A", ("i", "B", F(1)),
)


def remote_record_key(events, internal):
    records = {}
    for event in events:
        event_internal = internal if event[2] == "i" else None
        records = write_event_record(records, event, event_internal)
    return physical_record_key(events, records)


remote_record_orders_equal = all(
    remote_record_key(remote_ab["events"], h)
    == remote_record_key(remote_ba["events"], h)
    for h in remote_labels
)
remote_actor_ok = (
    remote_operator_commutes
    and remote_order_ib == remote_order_bi
    and remote_d == d_ab
    and physical_actor_state_key(remote_ab) == physical_actor_state_key(remote_ba)
    and remote_record_orders_equal
    and all(len(event[4]) == 0 for event in remote_ab["events"])
)
check(
    "C11 ACTUAL DISCONNECTED ACTOR FACTOR / REMOTE MARGINAL [exact]: on "
    "A--B disjoint from P--Q, the actual A-target diamond and P-to-P/1 D24 "
    "birth commute on every carrier basis vector. Both serializations give "
    "the same typed actor state and class branches; the remote unitary leaves "
    "the complete local diamond functional unchanged",
    remote_actor_ok,
    "actual interaction x birth; 64/64 basis commutation; 8/8 branches; "
    "joint local marginal=D_diamond",
)

finite_dag_theorem_hypotheses = (
    fresh_record_capacity and record_partition_ok
    and event_instruments_are_isometries and scheduler_operator_complete
    and incoming_ok and merge_ok and remote_actor_ok
)
check(
    "C12 FINITE TYPED-DAG / DOWN-SET THEOREM [algebraic proof + exact "
    "specimens]: Gram positivity follows from class vectors with one fresh "
    "bounded event factor per node. Exhaustive extension restricts because "
    "sum_x q_x W_x^dag W_x=I; induction covers every finite down-set. "
    "Record-disjoint incomparable maps commute, while shared-wire order and "
    "two-tip merges are physical",
    finite_dag_theorem_hypotheses,
    "conditioned A tree + incoming reception + merge + disconnected actors; "
    "full timed direct integral not consumed",
)


# C13: dependent scorecard.
ok13 = FAIL == 0
check(
    "C13 CLAIM CEILING [dependent scorecard]: earned only FINITE TYPED-DAG "
    "ACTOR/QUANTUM SEWING WITH BOUNDED EVENT RECORDS plus conditional finite-"
    "down-set induction for the chosen operation family. Not earned: the "
    "timed operator-valued D34b measure or infinite incoming marginal, "
    "untimed/profinite restriction, graph-sector superposition, derived "
    "weights/operations/basis/NSE, sealing, joining, Lorentz cones, "
    "dimension, or THE universe law",
    ok13,
    "C1-C12 green; C0/C13 scorecards; D34b weights and operations chosen; "
    "NSE remains a posited selector",
)


print()
print(f"ALL CHECKS PASS ({PASS}/{PASS + FAIL}: C1-C12 substantive; C0/C13 dependent scorecards)"
      if FAIL == 0 else
      f"CHECKS FAILED ({PASS} pass, {FAIL} fail)")
sys.exit(0 if FAIL == 0 else 1)
