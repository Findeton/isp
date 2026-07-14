#!/usr/bin/env python3
"""D34d finite quantum predictive-state receipt.

Pin: note-d34d-predictive-state-clock-status.md / commit 77defcd.

This exact receipt uses the D34c operational diamond formula and real qubit
carrier states to decide what a quantum predictive state must retain.  It does
not read fine-history diagonals as probabilities and does not claim the absent
timed/direct-integral quantum lift.

The central controls are:

* coherent and path-recorded diamond histories have the same durable s record
  and the same path-basis diagonal, but different future output laws;
* a tomographically complete real-qubit state closes all declared local
  one-step instruments;
* a reduced carrier density matrix is not sufficient if a discarded old
  environment can interact again—the joint boundary/process memory is then
  required;
* a genuinely disconnected environment factors out exactly.

All arithmetic is fractions.  Gates Q1--Q6 are substantive; Q7 is the
dependent scorecard.  Exit 1 on any failure.
"""

from fractions import Fraction as F
from itertools import product
import hashlib
import sys

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


def zeros(n, m):
    return [[F(0) for _ in range(m)] for _ in range(n)]


def eye(n):
    out = zeros(n, n)
    for i in range(n):
        out[i][i] = F(1)
    return out


def transpose(a):
    return [list(row) for row in zip(*a)]


def mm(a, b):
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt]
            for row in a]


def madd(a, b):
    return [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def mscale(c, a):
    return [[c * x for x in row] for row in a]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def born(effect, rho):
    return trace(mm(effect, rho))


def kron(a, b):
    return [[a[i][j] * b[r][c]
             for j in range(len(a[0])) for c in range(len(b[0]))]
            for i in range(len(a)) for r in range(len(b))]


def partial_trace_second(rho, da, db):
    out = zeros(da, da)
    for i in range(da):
        for j in range(da):
            out[i][j] = sum(rho[i * db + k][j * db + k]
                            for k in range(db))
    return out


def hadamard_density(rho):
    # H rho H, with the two 1/sqrt(2) factors combined into exact 1/2.
    s = ((1, 1), (1, -1))
    return [[F(1, 2) * sum(s[i][a] * rho[a][b] * s[j][b]
                           for a in range(2) for b in range(2))
             for j in range(2)] for i in range(2)]


def conjugate_permutation(rho, permutation):
    """U rho U^T for U|j>=|permutation[j]>."""
    n = len(permutation)
    out = zeros(n, n)
    for i in range(n):
        for j in range(n):
            out[permutation[i]][permutation[j]] += rho[i][j]
    return out


print("[d34d — exact finite quantum predictive-state status]")


# ---------------------------------------------------------------------------
# Q1: reconstruct the D34c diamond functional directly from its formula.

HISTORIES = list(product((0, 1), repeat=3))  # (s,p,o)
D = zeros(8, 8)
for i, (s, p, o) in enumerate(HISTORIES):
    for j, (ss, pp, oo) in enumerate(HISTORIES):
        if s == ss and o == oo:
            parity = p * (1 + s + o) + pp * (1 + ss + oo)
            D[i][j] = F(-1 if parity % 2 else 1, 8)

hermitian = D == transpose(D)
normalized = sum(sum(row) for row in D) == 1
block_psd_rank = True
rank = 0
for s, o in product((0, 1), repeat=2):
    ids = [HISTORIES.index((s, p, o)) for p in (0, 1)]
    block = [[D[i][j] for j in ids] for i in ids]
    # Each block is 1/8 vv^T: nonnegative diagonal, zero determinant,
    # nonzero trace.  The blocks have disjoint support, so total rank is four.
    det = block[0][0] * block[1][1] - block[0][1] * block[1][0]
    block_psd_rank &= (
        block[0][0] >= 0 and block[1][1] >= 0
        and det == 0 and block[0][0] + block[1][1] == F(1, 4)
    )
    rank += 1


def coarse_probability(s, o, keep_path_coherence):
    ids = [HISTORIES.index((s, p, o)) for p in (0, 1)]
    if keep_path_coherence:
        return sum(D[i][j] for i in ids for j in ids)
    return sum(D[i][i] for i in ids)


coherent_joint = {
    (s, o): coarse_probability(s, o, True)
    for s, o in product((0, 1), repeat=2)
}
recorded_joint = {
    (s, o): coarse_probability(s, o, False)
    for s, o in product((0, 1), repeat=2)
}
q1_ok = (
    hermitian and normalized and block_psd_rank and rank == 4
    and coherent_joint == {
        (0, 0): F(0), (0, 1): F(1, 2),
        (1, 0): F(1, 2), (1, 1): F(0),
    }
    and all(p == F(1, 4) for p in recorded_joint.values())
)
check(
    "Q1 D34c FUNCTIONAL RECONSTRUCTION [exact]: the 8x8 history functional "
    "is normalized, Hermitian and four rank-one positive blocks; coherent "
    "path coarse graining gives joint (0,1/2,1/2,0), while recording/dephasing "
    "the path gives four 1/4 cells",
    q1_ok,
    f"rank={rank}; coherent={coherent_joint}; recorded={recorded_joint}",
)


# ---------------------------------------------------------------------------
# Q2: the carrier state that the durable classical record omits.

P0 = [[F(1), F(0)], [F(0), F(0)]]
P1 = [[F(0), F(0)], [F(0), F(1)]]
RHO_PLUS = [[F(1, 2), F(1, 2)], [F(1, 2), F(1, 2)]]
RHO_MINUS = [[F(1, 2), F(-1, 2)], [F(-1, 2), F(1, 2)]]
RHO_MIXED = [[F(1, 2), F(0)], [F(0), F(1, 2)]]

# After the diamond CZ and conditioning on durable s, the path carrier is
# |-> for s=0 and |+> for s=1.  H then output-copy reads o=1-s.
coherent_carrier = {0: RHO_MINUS, 1: RHO_PLUS}
coherent_output = {}
recorded_output = {}
same_path_diagonal = True
for s in (0, 1):
    same_path_diagonal &= (
        coherent_carrier[s][0][0] == RHO_MIXED[0][0]
        and coherent_carrier[s][1][1] == RHO_MIXED[1][1]
    )
    after_h = hadamard_density(coherent_carrier[s])
    dephased_after_h = hadamard_density(RHO_MIXED)
    coherent_output[s] = (born(P0, after_h), born(P1, after_h))
    recorded_output[s] = (born(P0, dephased_after_h),
                          born(P1, dephased_after_h))

q2_ok = (
    same_path_diagonal
    and coherent_output == {0: (F(0), F(1)), 1: (F(1), F(0))}
    and recorded_output == {
        0: (F(1, 2), F(1, 2)), 1: (F(1, 2), F(1, 2))
    }
    and all(F(1, 2) * coherent_output[s][o] == coherent_joint[(s, o)]
            for s, o in product((0, 1), repeat=2))
    and all(F(1, 2) * recorded_output[s][o] == recorded_joint[(s, o)]
            for s, o in product((0, 1), repeat=2))
)
check(
    "Q2 DURABLE RECORD IS NOT THE QUANTUM PREDICTIVE STATE [exact]: for a "
    "fixed durable s, the coherent and path-recorded alternatives have the "
    "same path-basis diagonal, but H/output gives deterministic o=1-s versus "
    "a uniform output; the carrier coherence is operational future memory",
    q2_ok,
    f"coherent outputs={coherent_output}; dephased outputs={recorded_output}",
)


# ---------------------------------------------------------------------------
# Q3: operational/instrument lumpability, not classical diagonal lumpability.

# Observer projection retains only s.  Two complete states above one visible s
# (coherent path versus inaccessible path record/environment) have unequal
# next visible output instruments, so this projection is not lumpable.
quantum_lumpability_fails = all(
    coherent_output[s] != recorded_output[s] for s in (0, 1)
)
classical_shadow_same = all(
    tuple(coherent_carrier[s][i][i] for i in range(2))
    == tuple(RHO_MIXED[i][i] for i in range(2))
    for s in (0, 1)
)
q3_ok = quantum_lumpability_fails and classical_shadow_same
check(
    "Q3 QUANTUM OBSERVABLE NON-LUMPABILITY [exact]: the projection to the "
    "durable classical s record merges operationally different complete "
    "states; an allowed future H/output instrument separates them even though "
    "their classical path shadows agree",
    q3_ok,
    "same visible s and Z diagonal; future laws deterministic vs (1/2,1/2)",
)


# ---------------------------------------------------------------------------
# Q4: exact finite tomography for the declared real-qubit carrier algebra.

PPLUS = RHO_PLUS
EFFECTS = (P0, P1, PPLUS)


def signature(rho):
    return tuple(born(e, rho) for e in EFFECTS)


def reconstruct_real_symmetric(sig):
    p0, p1, pp = sig
    offdiag = pp - (p0 + p1) / 2
    return [[p0, offdiag], [offdiag, p1]]


TEST_STATES = (
    RHO_PLUS,
    RHO_MINUS,
    RHO_MIXED,
    P0,
    P1,
    [[F(3, 4), F(1, 4)], [F(1, 4), F(1, 4)]],
)
tomography_ok = all(reconstruct_real_symmetric(signature(rho)) == rho
                    for rho in TEST_STATES)
signature_injective = all(
    (signature(a) == signature(b)) == (a == b)
    for a in TEST_STATES for b in TEST_STATES
)
q4_ok = tomography_ok and signature_injective
check(
    "Q4 FINITE OPERATIONAL PREDICTIVE CLOSURE [exact, scoped]: P0, P1 and "
    "P+ statistics reconstruct every tested real symmetric qubit state "
    "exactly, so retaining that carrier density matrix is sufficient for the "
    "declared real one-qubit future instrument algebra",
    q4_ok,
    f"{len(TEST_STATES)} states; 3-effect signatures reconstruct/inject exactly",
)


# ---------------------------------------------------------------------------
# Q5: reduced state is not enough if an old environment can return.

# Basis is |P,E> = 00,01,10,11.  These two diagonal joint states both reduce
# to I/2 on P.  CNOT(E->P) maps the correlated state to P=0 and the
# anticorrelated state to P=1.
RHO_CORRELATED = zeros(4, 4)
RHO_CORRELATED[0][0] = F(1, 2)  # 00
RHO_CORRELATED[3][3] = F(1, 2)  # 11
RHO_ANTICORRELATED = zeros(4, 4)
RHO_ANTICORRELATED[1][1] = F(1, 2)  # 01
RHO_ANTICORRELATED[2][2] = F(1, 2)  # 10

# Index bits P,E; flip P when E=1.
CNOT_E_TO_P = (0, 3, 2, 1)
corr_after = conjugate_permutation(RHO_CORRELATED, CNOT_E_TO_P)
anti_after = conjugate_permutation(RHO_ANTICORRELATED, CNOT_E_TO_P)
corr_reduced_before = partial_trace_second(RHO_CORRELATED, 2, 2)
anti_reduced_before = partial_trace_second(RHO_ANTICORRELATED, 2, 2)
corr_reduced_after = partial_trace_second(corr_after, 2, 2)
anti_reduced_after = partial_trace_second(anti_after, 2, 2)

q5_ok = (
    corr_reduced_before == anti_reduced_before == RHO_MIXED
    and corr_reduced_after == P0
    and anti_reduced_after == P1
)
check(
    "Q5 RETURNING-ENVIRONMENT NEGATIVE CONTROL [exact]: two joint boundary "
    "states have the same reduced carrier I/2, but a later local collar "
    "interaction sends them to certain P=0 and certain P=1; when old factors "
    "can return, the predictive state must retain the joint boundary/process "
    "memory rather than only the record's reduced density matrix",
    q5_ok,
    "before: both I/2; after CNOT(E->P): P0 vs P1",
)


# ---------------------------------------------------------------------------
# Q6: truly disconnected remote state factors out.  This is the positive
# operational-equivalence/locality control and the limit of the Q5 warning.

remote_states = (P0, P1, RHO_PLUS, RHO_MIXED)
local_states = (RHO_PLUS, RHO_MINUS, RHO_MIXED)
remote_factor_ok = True
for local in local_states:
    for remote in remote_states:
        joint = kron(local, remote)
        remote_factor_ok &= partial_trace_second(joint, 2, 2) == local
        for effect in EFFECTS:
            remote_factor_ok &= born(kron(effect, eye(2)), joint) == born(effect, local)

# Disjoint local/remote maps commute.  Use exact X permutations on two bits.
X_LOCAL = (2, 3, 0, 1)
X_REMOTE = (1, 0, 3, 2)
commute_permutations = tuple(X_LOCAL[X_REMOTE[i]] for i in range(4)) == tuple(
    X_REMOTE[X_LOCAL[i]] for i in range(4)
)
q6_ok = remote_factor_ok and commute_permutations
check(
    "Q6 DISCONNECTED OPERATIONAL LOCALITY [exact]: every normalized remote "
    "factor traces out of the local predictive state and all declared local "
    "future probabilities; disjoint local/remote operations commute. Remote "
    "states are safely omitted only while no future interaction reconnects them",
    q6_ok,
    "3 local x 4 remote states x 3 effects exact; X_local X_remote commute",
)


# ---------------------------------------------------------------------------
# Q7: dependent scorecard.

q7_ok = PASS == 6 and FAIL == 0
check(
    "Q7 CLAIM SCORECARD [dependent]: the D34c finite diamond admits an "
    "operational predictive-state reading, and its durable classical shadow "
    "can be non-Markov because it omits coherence/correlation. The sufficient "
    "state is the carrier or returning boundary/process state licensed by the "
    "future algebra—not necessarily one record's density matrix. This does not "
    "construct the timed direct integral, prove finite memory for every SHARD "
    "law, or reduce quantum memory to a classical hidden chain",
    q7_ok,
    "maximum noun: FINITE D34c OPERATIONAL PREDICTIVE-STATE CHARACTERIZATION",
)

summary = (
    f"gates={PASS}/{PASS + FAIL}; D-rank={rank}; "
    f"coherent={coherent_joint}; recorded={recorded_joint}; "
    "returning_environment=I/2->P0|P1; remote_factor=exact"
)
digest = hashlib.sha256(summary.encode("utf-8")).hexdigest()
print(f"[SUMMARY] {summary}")
print(f"[RECEIPT-SHA256] {digest}")
print(f"[VERDICT] {'PASS' if FAIL == 0 else 'FAIL'} — {PASS}/{PASS + FAIL}")
sys.exit(1 if FAIL else 0)
