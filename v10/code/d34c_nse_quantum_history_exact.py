#!/usr/bin/env python3
"""D34c exact receipt: A-local actor/quantum sewing for the D34b law.

Pin: note-d33-history-law-phase.md §11, commit f861328, before this file.

This receipt does NOT derive the D34b weights or nature's quantum law.  It
tests a compatibility construction on A's local-ring stopping algebra through
depth two; incoming remote receptions are deliberately coarse-grained:

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


print("[d34c — exact A-local actor/quantum sewing]")


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


def actor_seed():
    return {
        "active": ("A", "B"),
        "neighbors": {"A": {"B"}, "B": {"A"}},
        "births": 0,
        "rings": {"A": 0, "B": 0},
        "last": {},
        "events": (),
    }


def copy_actor_state(s):
    return {
        "active": tuple(s["active"]),
        "neighbors": {a: set(xs) for a, xs in s["neighbors"].items()},
        "births": s["births"],
        "rings": dict(s["rings"]),
        "last": dict(s["last"]),
        "events": tuple(s["events"]),
    }


def actor_options(s):
    ns = sorted(s["neighbors"]["A"])
    child = f"A/{s['births'] + 1}"
    return ([('b', child, F(1, 4))]
            + [('i', x, F(1, 4 * len(ns))) for x in ns]
            + [('n', None, F(1, 2))])


def actor_step(s, option):
    kind, target, weight = option
    z = copy_actor_state(s)
    z["rings"]["A"] += 1
    eid = f"A#r{z['rings']['A']}"
    if kind == "b":
        z["births"] += 1
        z["active"] = tuple(sorted(z["active"] + (target,)))
        z["neighbors"].setdefault("A", set()).add(target)
        z["neighbors"][target] = {"A"}
        z["rings"][target] = 0
    touched = ("A",) if kind == "n" else ("A", target)
    preds = tuple(sorted({z["last"][a] for a in touched if a in z["last"]}))
    event = (eid, kind, target, preds)
    z["events"] += (event,)
    for a in touched:
        z["last"][a] = eid
    return z, weight


depth1_paths = [actor_step(actor_seed(), o) for o in actor_options(actor_seed())]
depth2_paths = []
for s1, m1 in depth1_paths:
    for option in actor_options(s1):
        s2, w2 = actor_step(s1, option)
        depth2_paths.append((s2, m1 * w2))

mass1 = {s["events"]: m for s, m in depth1_paths}
mass2 = {s["events"]: m for s, m in depth2_paths}
classical_restriction = all(
    sum((m for evs, m in mass2.items() if evs[:1] == prefix), F(0)) == mass
    for prefix, mass in mass1.items()
)
row_normalization = all(
    sum((w for _, _, w in actor_options(s)), F(0)) == 1
    for s, _ in depth1_paths
)
all_m_identity = all(
    F(1, 4) + m * F(1, 4 * m) + F(1, 2) == 1
    for m in range(1, 65)
)
after_birth = next(s for s, _ in depth1_paths if s["events"][0][1] == "b")
degree_two_weights = sorted(
    w for k, _, w in actor_options(after_birth) if k == "i"
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


def interaction_branches(v, ring, target):
    pathq, outq = PATH_Q[ring], OUT_Q[ring]
    v = acnot(v, ACTOR_Q["A"], ACTOR_Q[target])
    rows = []
    for sval in (0, 1):
        vs = aproject(v, ACTOR_Q[target], sval)
        vs = az(vs, pathq)
        for pval in (0, 1):
            vp = aproject(vs, pathq, pval)
            vp = acz(vp, ACTOR_Q["A"], pathq)
            vp = ah(vp, pathq)
            vp = acnot(vp, pathq, outq)
            for oval in (0, 1):
                rows.append(((sval, pval, oval), aproject(vp, outq, oval)))
    return rows


def mailbox_key(mailboxes):
    return tuple(sorted((a, tuple(box)) for a, box in mailboxes.items()))


def factorized_flag_inner(left, right):
    """Inner product on tensor_a H_mailbox(a), never a global flag atom."""
    for actor in set(left) | set(right):
        if tuple(left.get(actor, ())) != tuple(right.get(actor, ())):
            return ZERO
    return ONE


def write_event_flag(mailboxes, event, internal):
    eid, kind, target, preds = event
    out = {a: list(box) for a, box in mailboxes.items()}
    if kind == "b":
        out.setdefault(target, [])
        token = (eid, kind, target, preds, None, None)
        touched = ("A", target)
    elif kind == "i":
        sval, _, oval = internal
        token = (eid, kind, target, preds, sval, oval)
        touched = ("A", target)
    else:
        token = (eid, kind, None, preds, None, None)
        touched = ("A",)
    for a in touched:
        out.setdefault(a, []).append(token)
    return out


def quantum_branches(events, mass):
    rows = [{
        "v": list(actor_initial),
        "mailboxes": {"A": [], "B": []},
        "internals": (),
        "flag_prefixes": (),
    }]
    for ring, event in enumerate(events, 1):
        kind, target = event[1], event[2]
        nxt = []
        for row in rows:
            if kind == "b":
                variants = [(None, acry(row["v"], ACTOR_Q["A"],
                                         ACTOR_Q[target]))]
            elif kind == "i":
                variants = interaction_branches(row["v"], ring, target)
            else:
                variants = [(None, list(row["v"]))]
            for internal, vnew in variants:
                boxes = write_event_flag(row["mailboxes"], event, internal)
                fkey = mailbox_key(boxes)
                nxt.append({
                    "v": vnew,
                    "mailboxes": boxes,
                    "internals": row["internals"] + (internal,),
                    "flag_prefixes": row["flag_prefixes"] + (fkey,),
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
            flag_ip = factorized_flag_inner(
                branches[i]["mailboxes"], branches[j]["mailboxes"]
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
    return (row["events"][:n], row["flag_prefixes"][n - 1],
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


flag_factor_ok = True
flag_groups = defaultdict(list)
for row in qbranches2:
    flag_groups[mailbox_key(row["mailboxes"])].append(row)
for rows in flag_groups.values():
    signatures = {
        (r["events"], tuple(durable_internal(x) for x in r["internals"]))
        for r in rows
    }
    flag_factor_ok &= len(signatures) == 1

# Mailbox semantics: shared tokens on birth/interaction, idle on A only;
# passive targets never advance an actor-local ring.
mailbox_semantics = True
for row in qbranches2:
    boxes = row["mailboxes"]
    for event, internal in zip(row["events"], row["internals"]):
        eid, kind, target, preds = event
        if kind == "i":
            token = (eid, kind, target, preds, internal[0], internal[2])
            mailbox_semantics &= token in boxes["A"] and token in boxes[target]
        elif kind == "b":
            token = (eid, kind, target, preds, None, None)
            mailbox_semantics &= token in boxes["A"] and token in boxes[target]
        else:
            token = (eid, kind, None, preds, None, None)
            mailbox_semantics &= token in boxes["A"]
            mailbox_semantics &= all(token not in box for a, box in boxes.items()
                                     if a != "A")
for state, _ in depth2_paths:
    mailbox_semantics &= all(r == 0 for a, r in state["rings"].items()
                             if a != "A")

# The actual first interaction block carries the diamond interference on A,B.
first_i_key = next(k for k in mass1 if k[0][1] == "i")
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
birth_key = next(k for k in mass1 if k[0][1] == "b")
idle_key = next(k for k in mass1 if k[0][1] == "n")
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

# Quantum remote factorization and construction-order gauge, carried on the
# abstract flagged channel because the tensor identity is dimension-free.
def product_flagged_channel(rhoa, rhob):
    rhoab = kron_matrix(rhoa, rhob)
    out = zeros(36, 36)
    for wa, va in zip(weights, w_kinds):
        for wb, vb in zip(weights, w_kinds):
            vv = kron_matrix(va, vb)
            out = madd(out, mscale(wa * wb,
                                   mm(mm(vv, rhoab), transpose(vv))))
    return out


def partial_trace_second(a, da, db):
    return [[sum((a[i * db + k][j * db + k] for k in range(db)), ZERO)
             for j in range(da)] for i in range(da)]


remote_joint = product_flagged_channel(rhop, rho0)
remote_product = kron_matrix(density_channel_flagged(rhop),
                             density_channel_flagged(rho0))
remote_quantum_ok = remote_joint == remote_product
remote_quantum_ok &= partial_trace_second(remote_joint, 6, 6) \
    == density_channel_flagged(rhop)
disjoint_commute = True
for ua in test_unitaries:
    for ub in test_unitaries:
        left = kron_matrix(ua, I2)
        right = kron_matrix(I2, ub)
        disjoint_commute &= mm(left, right) == mm(right, left)

actor_norm = sum((sum(row, ZERO) for row in d_actor2), ZERO) == ONE
actor_counts = (len(mass1), len(mass2), len(qbranches1), len(qbranches2))
check(
    "C8 ACTION-LEVEL A-LOCAL ACTOR/QUANTUM SEWING [exact]: complete "
    "A-initiated ring cylinders (incoming remote receptions coarse-grained) "
    "carry Ulam birth, changing degree/target, passive "
    "reception and predecessors; idle I, D24 birth and actual A-target "
    "diamond operations are composed into class branches. Tensor-factor "
    "mailboxes preserve p-interference, recover every classical mass, and "
    "the genuine second instrument restricts depth 2->1. Quantum remote "
    "channels tensor-factor and disjoint events commute",
    sum(mass1.values(), F(0)) == 1 and sum(mass2.values(), F(0)) == 1
    and classical_restriction and row_normalization and all_m_identity
    and degree_two_weights and actor_norm and shadow_ok and labels_unique
    and quantum_restriction and flag_factor_ok and mailbox_semantics
    and interaction_signature and event_ops_tied
    and remote_quantum_ok and disjoint_commute,
    f"classical/quantum depth counts={actor_counts}; degree2 i=1/8+1/8; "
    "quantum 108->10; shadow/reception/flags/remote exact",
)


# C9: dependent scorecard.
ok9 = FAIL == 0
check(
    "C9 CLAIM CEILING [dependent scorecard]: earned only A-LOCAL DEPTH-2 "
    "ACTOR/QUANTUM SEWING plus the algebraic finite-local-prefix induction "
    "for a chosen operation/flag family. Not earned: the full timed D34b "
    "quantum law, graph-sector superposition, "
    "derived weights or operations, a preferred basis, coherent "
    "superposition across distinct durable growth histories, infinite "
    "quantum-measure/profinite extension, dynamic joining, Lorentz cones, "
    "dimension, or THE universe law",
    ok9,
    "C1-C8 green; C0/C9 scorecards; local-ring stopping only; "
    "D34b weights remain chosen and NSE posited",
)


print()
print(f"ALL CHECKS PASS ({PASS}/{PASS + FAIL}: C1-C8 substantive; C0/C9 dependent scorecards)"
      if FAIL == 0 else
      f"CHECKS FAILED ({PASS} pass, {FAIL} fail)")
sys.exit(0 if FAIL == 0 else 1)
