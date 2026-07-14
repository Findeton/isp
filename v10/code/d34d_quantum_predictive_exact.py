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

All arithmetic is fractions.  Gates Q1--Q9 are substantive; Q10 is the
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
rank_from_block_proof = 0
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
    rank_from_block_proof += 1


# The path-recorded experiment is a distinct functional constructed by an
# orthogonal receiver, not a second reading of the coherent diagonal.
D_RECORDED = [
    [D[i][j] if HISTORIES[i][1] == HISTORIES[j][1] else F(0)
     for j in range(len(HISTORIES))]
    for i in range(len(HISTORIES))
]


def incidence_probability(functional, s, o):
    ids = [HISTORIES.index((s, p, o)) for p in (0, 1)]
    return sum(functional[i][j] for i in ids for j in ids)


coherent_joint = {
    (s, o): incidence_probability(D, s, o)
    for s, o in product((0, 1), repeat=2)
}
recorded_joint = {
    (s, o): incidence_probability(D_RECORDED, s, o)
    for s, o in product((0, 1), repeat=2)
}
recorded_functional_ok = (
    D_RECORDED == transpose(D_RECORDED)
    and sum(sum(row) for row in D_RECORDED) == 1
    and all(D_RECORDED[i][j] == (F(1, 8) if i == j else F(0))
            for i in range(8) for j in range(8))
)
q1_ok = (
    hermitian and normalized and block_psd_rank and rank_from_block_proof == 4
    and coherent_joint == {
        (0, 0): F(0), (0, 1): F(1, 2),
        (1, 0): F(1, 2), (1, 1): F(0),
    }
    and all(p == F(1, 4) for p in recorded_joint.values())
    and recorded_functional_ok
)
check(
    "Q1 D34c FUNCTIONAL RECONSTRUCTION [exact]: the 8x8 history functional "
    "is normalized, Hermitian and four rank-one positive blocks; coherent "
    "path coarse graining gives joint (0,1/2,1/2,0); the independently built "
    "orthogonal-receiver functional D_rec=delta_(p,p')D is normalized/positive "
    "and gives four 1/4 cells",
    q1_ok,
    f"rank={rank_from_block_proof}; coherent={coherent_joint}; recorded={recorded_joint}",
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
# Q3: cross-context durable-record insufficiency, distinct from the fixed-
# process operational Markov test in Q8.

# Observer projection retains only s.  Two complete states above one visible s
# (coherent path versus inaccessible path record/environment) have unequal
# next visible output instruments, so this projection is not lumpable.
record_projection_operationally_insufficient = all(
    coherent_output[s] != recorded_output[s] for s in (0, 1)
)
classical_shadow_same = all(
    tuple(coherent_carrier[s][i][i] for i in range(2))
    == tuple(RHO_MIXED[i][i] for i in range(2))
    for s in (0, 1)
)
q3_ok = record_projection_operationally_insufficient and classical_shadow_same
check(
    "Q3 DURABLE-RECORD OPERATIONAL INSUFFICIENCY ACROSS PAST INSTRUMENTS "
    "[exact, rescoped]: the projection to durable s merges the coherent and "
    "path-recorded contexts; a future H/output test separates them although "
    "their classical path shadows agree. This cross-context result is not by "
    "itself non-Markovianity of one fixed process",
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
    "Q4 REBIT TOMOGRAPHIC EFFECT SET [exact, scoped]: for a real-symmetric "
    "rho=[[a,b],[b,c]], P0,P1,P+ give a,c,(a+c+2b)/2 and reconstruct "
    "b=p+-(p0+p1)/2. This is single-state rebit tomography, not a multi-time "
    "instrument/process-closure theorem or a general complex-qubit result",
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
    "state rather than only the record's reduced density matrix. Retaining E "
    "and eliminating E are distinct architectures",
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
    "Q7 BASELINE QUANTUM SCORECARD [dependent, rescoped after round 1]: the "
    "diamond, D_rec, record-insufficiency, rebit tomography, returning-boundary "
    "and disconnected-factor witnesses pass. Cross-context insufficiency and "
    "state tomography do not yet establish one fixed non-Markov process; the "
    "causal-break replacement gate follows",
    q7_ok,
    "round-1 survivor: D34c RECORD INSUFFICIENCY + REBIT BOUNDARY WITNESSES",
)


# ---------------------------------------------------------------------------
# Q8: one fixed three-slot process and an operational causal break.

def causal_break_p0_reprepare_p0(joint):
    """Select P=0, discard P, and reprepare P=0; return prob and joint PE."""
    # Basis |P,E>; P=0 block is indices 0,1.
    probability = joint[0][0] + joint[1][1]
    if probability == 0:
        raise ValueError("zero causal-break outcome")
    rho_e = [[joint[e][f] / probability for f in range(2)]
             for e in range(2)]
    return probability, kron(P0, rho_e)


# One fixed process: initial correlated PE state, two allowed PAST instrument
# choices I_P or X_P, the SAME middle causal-break outcome/repreparation, and
# the SAME future CNOT(E->P) plus P readout.
past_i_joint = RHO_CORRELATED
past_x_joint = conjugate_permutation(RHO_CORRELATED, X_LOCAL)
past_x_is_anti = past_x_joint == RHO_ANTICORRELATED

break_prob_i, break_joint_i = causal_break_p0_reprepare_p0(past_i_joint)
break_prob_x, break_joint_x = causal_break_p0_reprepare_p0(past_x_joint)
break_local_i = partial_trace_second(break_joint_i, 2, 2)
break_local_x = partial_trace_second(break_joint_x, 2, 2)

future_i_joint = conjugate_permutation(break_joint_i, CNOT_E_TO_P)
future_x_joint = conjugate_permutation(break_joint_x, CNOT_E_TO_P)
future_i_local = partial_trace_second(future_i_joint, 2, 2)
future_x_local = partial_trace_second(future_x_joint, 2, 2)

q8_ok = (
    past_x_is_anti
    and break_prob_i == break_prob_x == F(1, 2)
    and break_local_i == break_local_x == P0
    and future_i_local == P0 and future_x_local == P1
)
check(
    "Q8 FIXED THREE-SLOT OPERATIONAL NON-MARKOV WITNESS [exact]: in one "
    "process, past choices I_P/X_P are followed by the same nonzero P=0 "
    "causal-break outcome and the same P=0 repreparation (probability 1/2 in "
    "both). The fixed future CNOT(E->P) then gives certain P=0 versus certain "
    "P=1. Future statistics retain past-instrument dependence after the causal "
    "break, establishing instrument-specific quantum process memory",
    q8_ok,
    "break probs=1/2,1/2; middle reduced state=P0,P0; future=P0,P1",
)


# ---------------------------------------------------------------------------
# Q9: architecture fork and universal product-factor identity.

# If E is retained, the joint PE density is the state and the displayed
# future update is an ordinary deterministic Markov map.  If E is eliminated,
# the equal reduced P0 middle states with different futures require a reduced
# multi-time process description.  These are alternatives, not synonyms.
joint_boundary_distinguishes = break_joint_i != break_joint_x
reduced_middle_same = break_local_i == break_local_x
reduced_future_differs = future_i_local != future_x_local

# Algebraic product theorem: Tr[(E local tensor I)(rho local tensor sigma)]
# = Tr(E rho) Tr(sigma) = Tr(E rho) for every trace-one sigma.  The matrix
# regression uses a generic rational, nondiagonal trace-one factor in addition
# to Q6's finite battery; the displayed factorization carries the universal
# claim.  Initially correlated cross-component states are outside this product
# theorem and must be retained through their reduced/joint state as licensed.
sigma_generic = [[F(2, 3), F(1, 6)], [F(1, 6), F(1, 3)]]
rho_generic = [[F(3, 4), F(1, 4)], [F(1, 4), F(1, 4)]]
effect_generic = [[F(2, 3), F(1, 6)], [F(1, 6), F(1, 3)]]
product_identity = (
    trace(sigma_generic) == 1
    and born(kron(effect_generic, eye(2)), kron(rho_generic, sigma_generic))
    == born(effect_generic, rho_generic) * trace(sigma_generic)
    and partial_trace_second(kron(rho_generic, sigma_generic), 2, 2)
    == rho_generic
)

q9_ok = (
    joint_boundary_distinguishes and reduced_middle_same
    and reduced_future_differs and product_identity
)
check(
    "Q9 JOINT-BOUNDARY / REDUCED-PROCESS FORK [exact + algebraic theorem]: "
    "retaining E gives distinct joint PE predictive states and a closed unitary "
    "update; eliminating E gives identical middle P states but different "
    "futures and therefore reduced process memory. Forever disconnected "
    "trace-one product factors obey the universal tensor/partial-trace identity; "
    "initially correlated or returning factors are not silently discarded",
    q9_ok,
    "joint states differ; reduced middle same; future differs; generic product exact",
)


# ---------------------------------------------------------------------------
# Q10: repaired quantum scorecard.

q10_ok = PASS == 9 and FAIL == 0
check(
    "Q10 REPAIRED QUANTUM SCORECARD [dependent]: D34c supplies exact coherent "
    "and path-recorded functionals; durable s is insufficient across declared "
    "past instruments; Q8 separately proves operational non-Markovianity for "
    "one fixed three-slot process after a causal break. A joint boundary state "
    "Markovizes that finite process, while eliminating it requires reduced "
    "multi-time memory. Rebit tomography remains single-state/instrument-"
    "specific. No timed quantum law, universal finite Markov order, complex-"
    "qubit closure or bounded SHARD memory is claimed",
    q10_ok,
    "maximum noun: FINITE FIXED-PROCESS QUANTUM MEMORY + REBIT BOUNDARY-STATE "
    "CHARACTERIZATION",
)

summary = (
    f"gates={PASS}/{PASS + FAIL}; D-rank={rank_from_block_proof}; "
    f"coherent={coherent_joint}; recorded={recorded_joint}; "
    "causal_break=P0,P0->P0|P1; returning_environment=I/2->P0|P1; "
    "remote_factor=exact"
)
digest = hashlib.sha256(summary.encode("utf-8")).hexdigest()
print(f"[SUMMARY] {summary}")
print(f"[RECEIPT-SHA256] {digest}")
print(f"[VERDICT] {'PASS' if FAIL == 0 else 'FAIL'} — {PASS}/{PASS + FAIL}")
sys.exit(1 if FAIL else 0)
