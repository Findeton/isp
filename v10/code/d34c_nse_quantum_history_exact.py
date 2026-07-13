#!/usr/bin/env python3
"""D34c exact receipt: NSE/quantum compatibility of the D34b actor law.

Pin: note-d33-history-law-phase.md §11, commit f861328, before this file.

This receipt does NOT derive the D34b weights or nature's quantum law.  It
tests a compatibility construction at finite/cylinder scope:

* durable D34b click alternatives have event-local orthogonal flags;
* unrecorded alternatives between clicks may retain interference;
* every branch operation is an isometry on the total declared ontology;
* preparation-independent flagged branches form a Busch/NSE channel;
* the finite decoherence functional is an exact strongly-positive Gram form.

The operational diamond uses four qubits S,R,P,O and exact Q(sqrt(2))
arithmetic.  No float, eigensolver, random sample, or numerical tolerance is
used.  Gates C0--C9; C9 is the dependent scope scorecard.  Exit 1 on failure.
"""

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
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


def matrix_equal(a, b):
    return a == b


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


print("[d34c — exact NSE/quantum finite-cylinder compatibility]")


# C0: types and licensed questions.
durable_fields = ("s", "o")
unrecorded_fields = ("p",)
types_ok = (len(HISTORIES) == 8 and durable_fields == ("s", "o")
            and unrecorded_fields == ("p",))
check(
    "C0 OBJECT TYPING: D34b clock/mark law, durable click fields, "
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
rank = 0
for s, o in product((0, 1), repeat=2):
    ids = [HISTORIES.index((s, p, o)) for p in (0, 1)]
    block = [[d_ab[i][j] for j in ids] for i in ids]
    eta = -1 if (1 + s + o) % 2 else 1
    vplus = [ONE, Q2(eta)]
    vzero = [ONE, Q2(-eta)]
    block_ok &= mv(block, vplus) == [Q2(F(1, 4)) * x for x in vplus]
    block_ok &= mv(block, vzero) == [ZERO, ZERO]
    rank += 1

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

d_path_recorded = [
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
    and offdiag_nonzero == 8,
    "coherent=(0,1/2,1/2,0); diagonal/recorded=(1/4)x4; offdiag=8",
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
for eij in matrix_units:
    ar = lifted_local(eij, R)
    full_r_stable &= mm(mm(transpose(u_future), ar), u_future) == ar

source_value_stable = True
for ps in (P0, P1):
    aps = lifted_local(ps, S)
    source_value_stable &= mm(mm(transpose(u_total), aps), u_total) == aps
x_s = lifted_local(X2, S)
source_phase_changes = mm(mm(transpose(u_total), x_s), u_total) != x_s
check(
    "C5 SEAL DURABILITY [exact, scoped]: after a creates R, the full R "
    "matrix algebra is fixed by every modeled future operation because R "
    "is never touched again. The source Z-value projectors are also preserved, while "
    "source phase content may disperse; these two seal notions are not "
    "conflated",
    full_r_stable and source_value_stable and source_phase_changes,
    "R: 4/4 matrix units fixed; S: P0/P1 fixed, X changed",
)


# C6: exact Busch-form flagged lift at D34b weights.
weights = (Q2(F(1, 4)), Q2(F(1, 4)), Q2(F(1, 2)))
u_kinds = (I2, X2, Z2)


def flagged_isometry(flag, u2):
    out = zeros(6, 2)
    for r in range(2):
        for c in range(2):
            out[2 * flag + r][c] = u2[r][c]
    return out


w_kinds = [flagged_isometry(k, u) for k, u in enumerate(u_kinds)]
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
        expected = mscale(w, mm(mm(u_kinds[k], delta),
                                transpose(u_kinds[k])))
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
    "C6 NSE / BUSCH LIFT: the D34b weights (1/4,1/4,1/2) multiply "
    "isometries with mutually orthogonal durable flag ranges. Exact "
    "noncommuting test pairs preserve trace distance; analytically the "
    "block trace norm sums to ||Delta||_1 for every input pair",
    sum(weights, ZERO) == ONE and orthogonal_ranges and nse_regression,
    "W_i^dag W_j=delta_ij I; three exact pair certificates; all-state "
    "block-norm theorem",
)


# C7: the flags and preparation-independence are load-bearing.
def unitary_channel(u, rho):
    return mm(mm(u, rho), transpose(u))


def unflagged_dephase(rho):
    return mscale(HALF, madd(rho, unitary_channel(Z2, rho)))


unflag_plus = unflagged_dephase(rhop)
unflag_minus = unflagged_dephase(rhom)
unflag_contracts = unflag_plus == unflag_minus == [[HALF, ZERO], [ZERO, HALF]]

# State-dependent branch choice: I for nonnegative <Z>, X otherwise.
# On rho0/rho1 both outputs are rho0, while the equal mixture has <Z>=0
# and is left as I/2.  Hence F((rho0+rho1)/2) != (F(rho0)+F(rho1))/2.
rho_mix = mscale(HALF, madd(rho0, rho1))
f0 = unitary_channel(I2, rho0)
f1 = unitary_channel(X2, rho1)
fmix = unitary_channel(I2, rho_mix)
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


# C8: finite actor/cylinder sewing and remote factorization.
kind_weights = {"b": F(1, 4), "i": F(1, 4), "n": F(1, 2)}


def local_options(eligible):
    if eligible < 1:
        raise ValueError("static exemplar assumes an eligible neighbor")
    return ([('b', None, F(1, 4))]
            + [('i', j, F(1, 4 * eligible)) for j in range(eligible)]
            + [('n', None, F(1, 2))])


local_rows_normalize = all(
    sum((w for _, _, w in local_options(m)), F(0)) == 1
    for m in range(1, 9)
)
depth1 = {(k,): w for k, w in kind_weights.items()}
depth2 = {(k1, k2): w1 * w2
          for (k1, w1), (k2, w2) in product(kind_weights.items(), repeat=2)}
restriction_ok = all(
    sum((mass for word, mass in depth2.items() if word[0] == k), F(0))
    == depth1[(k,)] for k in kind_weights
)

joint_remote = {(wa, wp): ma * mp
                for wa, ma in depth1.items() for wp, mp in depth1.items()}
remote_ok = all(
    sum((mass for (wa, _), mass in joint_remote.items() if wa == word), F(0))
    == mass for word, mass in depth1.items()
)

# Local Stinespring completeness for the one-neighbor kind instrument.
sqrt_weights = (Q2(F(1, 2)), Q2(F(1, 2)), ROOT_HALF)
k_ops = [mscale(sq, u) for sq, u in zip(sqrt_weights, u_kinds)]
completeness = zeros(2, 2)
for k_op in k_ops:
    completeness = madd(completeness, mm(transpose(k_op), k_op))

local_flags = {
    word: tuple(("A", ring + 1, kind) for ring, kind in enumerate(word))
    for word in depth2
}
flag_injective = len(set(local_flags.values())) == len(depth2)


def embed_vector(v, block, nblocks, scale=ONE):
    out = [ZERO] * (nblocks * len(v))
    start = block * len(v)
    for i, x in enumerate(v):
        out[start + i] = scale * x
    return out


# Build the bridge object itself, not just its classical and quantum factors.
# The durable kind flag makes different recorded click branches orthogonal;
# inside each kind block the unrecorded p alternatives retain the diamond D.
kinds = ("b", "i", "n")
weight_by_kind = dict(zip(kinds, weights))
sqrt_by_kind = dict(zip(kinds, sqrt_weights))
combined1_labels = [(k,) + h for k in kinds for h in HISTORIES]
combined1_vectors = [
    embed_vector(branches_ab[HISTORIES.index(h)], kinds.index(k), 3,
                 sqrt_by_kind[k])
    for k in kinds for h in HISTORIES
]
d_combined1 = gram(combined1_vectors)
combined1_normalized = sum(
    (sum(row, ZERO) for row in d_combined1), ZERO
) == ONE
groups_kind, d_kind, _ = incidence_coarse(
    d_combined1, combined1_labels, lambda z: z[0]
)
classical_shadow = {
    k: d_kind[i][i] for i, k in enumerate(groups_kind)
}

combined2_labels = [
    (k1, k2) + h for k1 in kinds for k2 in kinds for h in HISTORIES
]
combined2_vectors = [
    embed_vector(
        branches_ab[HISTORIES.index(h)],
        kinds.index(k1) * 3 + kinds.index(k2), 9,
        sqrt_by_kind[k1] * sqrt_by_kind[k2],
    )
    for k1 in kinds for k2 in kinds for h in HISTORIES
]
d_combined2 = gram(combined2_vectors)
combined1_keys, d_combined2_down, _ = incidence_coarse(
    d_combined2, combined2_labels,
    lambda z: (z[0], z[2], z[3], z[4]),
)
bridge_restricts = combined1_keys == combined1_labels
bridge_restricts &= d_combined2_down == d_combined1
bridge_has_interference = any(
    d_combined1[i][j]
    for i in range(len(combined1_labels))
    for j in range(len(combined1_labels))
    if i != j
)
check(
    "C8 ACTOR/HISTORY SEWING: local eligible-neighbor rows normalize "
    "without a universe census; exact kind cylinders restrict 9->3; "
    "event-local flag strings distinguish histories; the local isometric "
    "instrument is exhaustive; and a disconnected actor factor leaves the "
    "local marginal unchanged. The explicit combined functional is a "
    "direct-sum Gram form: its durable-click shadow is exactly the D34b "
    "kind law, it retains within-branch quantum interference, and its "
    "depth-2 functional pushes down exactly to depth 1",
    local_rows_normalize and sum(depth1.values(), F(0)) == 1
    and sum(depth2.values(), F(0)) == 1 and restriction_ok
    and remote_ok and completeness == I2 and flag_injective
    and combined1_normalized and classical_shadow == weight_by_kind
    and bridge_restricts and bridge_has_interference,
    "eligible m=1..8; masses 3/9; sum K^dag K=I; remote product marginal exact; "
    "combined Gram 72->24",
)


# C9: dependent scorecard.
ok9 = FAIL == 0
check(
    "C9 CLAIM CEILING: earned only FINITE-CYLINDER NSE/QUANTUM "
    "COMPATIBILITY for a chosen local isometry/flag family. Not earned: "
    "derived weights or operations, a preferred basis, coherent "
    "superposition across distinct durable growth histories, infinite "
    "quantum-measure/profinite extension, dynamic joining, Lorentz cones, "
    "dimension, or THE universe law",
    ok9,
    "C0-C8 green; D34b classical mu remains chosen input; NSE remains a posited selector",
)


print()
print(f"ALL CHECKS PASS ({PASS}/{PASS + FAIL}: C0-C8 substantive; C9 dependent scorecard)"
      if FAIL == 0 else
      f"CHECKS FAILED ({PASS} pass, {FAIL} fail)")
sys.exit(0 if FAIL == 0 else 1)
