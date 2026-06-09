"""
Test of the conjecture  "magic = indivisibility"  (RISP/ISP <-> quantum-information resource theory).

Part 1: Barandes' OWN representation. A unitary step U is represented by the stochastic matrix
        Gamma = |U|^2 (entrywise squared modulus; doubly stochastic for unitary U). The process is
        DIVISIBLE (Markovian) iff |U_m...U_1|^2 == |U_m|^2 ... |U_1|^2 (Chapman-Kolmogorov).
        "Indivisibility" = L1 violation of that. We compare it to a magic monotone (stabilizer
        2-Renyi entropy, Leone-Oliviero-Hamma 2022) across random circuits.
        Question: does computational-basis indivisibility track magic?

Part 2: The phase-space (discrete Wigner, Gross 2006) representation, qutrit d=3. Clifford gates act
        as permutations of phase space (positive + divisible); non-Clifford gates inject Wigner
        NEGATIVITY. Magic monotone = mana = log sum|W|. We verify (i) stabilizer states have W>=0,
        (ii) Clifford gate propagators on phase space are permutations (mana-preserving), (iii) a
        non-Clifford gate makes mana>0 and a non-permutation propagator.

Self-checking: Part 2 asserts the Gross axioms so a wrong convention can't produce a wrong claim.
"""
import numpy as np
from functools import reduce
from itertools import product

np.set_printoptions(precision=4, suppress=True, linewidth=140)
rng = np.random.default_rng(7)

# ============================ PART 1 : qubits ============================
I2 = np.eye(2, dtype=complex)
H  = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
S  = np.array([[1, 0], [0, 1j]], dtype=complex)
T  = np.array([[1, 0], [0, np.exp(1j*np.pi/4)]], dtype=complex)
Xg = np.array([[0, 1], [1, 0]], dtype=complex)

def kron(*ms): return reduce(np.kron, ms)
def embed1(g, q, n):
    ops = [I2]*n; ops[q] = g; return kron(*ops)
def cnot(c, t, n):
    P0 = np.diag([1,0]).astype(complex); P1 = np.diag([0,1]).astype(complex)
    a = [I2]*n; a[c] = P0
    b = [I2]*n; b[c] = P1; b[t] = Xg
    return kron(*a) + kron(*b)

PAULI = {'I':I2, 'X':Xg, 'Y':np.array([[0,-1j],[1j,0]]), 'Z':np.diag([1,-1]).astype(complex)}
def all_paulis(n):
    return [kron(*[PAULI[c] for c in combo]) for combo in product('IXYZ', repeat=n)]

def sre2(psi, n, paulis):
    d = 2**n
    s = 0.0
    for P in paulis:
        ev = np.real(np.vdot(psi, P @ psi))
        xi = ev*ev/d
        s += xi*xi
    val = -np.log2(d*s)
    return max(val, 0.0)  # clip tiny negative numerical

def indiv(steps):
    """L1 Chapman-Kolmogorov violation of the |U|^2 representation. steps: time-ordered (steps[0] first)."""
    dim = steps[0].shape[0]
    Utot  = reduce(lambda acc, U: U @ acc, steps, np.eye(dim, dtype=complex))
    Gtrue = np.abs(Utot)**2
    Gmark = reduce(lambda acc, U: (np.abs(U)**2) @ acc, steps, np.eye(dim))
    return np.abs(Gtrue - Gmark).sum()

print("="*78)
print("PART 1 — Barandes computational-basis indivisibility  vs  magic (SRE)")
print("="*78)

# (a) the killer example: H then H is pure Clifford, zero magic, yet indivisible
p1 = all_paulis(1)
steps_HH = [embed1(H,0,1), embed1(H,0,1)]
psi_HH = reduce(lambda acc,U: U@acc, steps_HH, np.eye(2,dtype=complex))[:,0]
print(f"(a) H·H (Clifford):           indiv = {indiv(steps_HH):.3f}   SRE(out) = {sre2(psi_HH,1,p1):.3f}")
# a single diagonal T at the end (magic) vs its indivisibility
steps_TH = [embed1(H,0,1), embed1(T,0,1)]
psi_TH = reduce(lambda acc,U: U@acc, steps_TH, np.eye(2,dtype=complex))[:,0]
print(f"(b) T·H (T=magic, diagonal):  indiv = {indiv(steps_TH):.3f}   SRE(out) = {sre2(psi_TH,1,p1):.3f}")
print("    -> Clifford H ALONE generates indivisibility; the magic gate T (diagonal) adds none.\n")

# (c) ensemble: random Clifford circuits with k inserted T-gates; correlate indiv vs SRE
def random_circuit(n, depth, kT):
    steps = []
    cliff1 = [H, S]
    for _ in range(depth):
        if n >= 2 and rng.random() < 0.4:
            c, t = rng.choice(n, size=2, replace=False)
            steps.append(cnot(int(c), int(t), n))
        else:
            steps.append(embed1(cliff1[rng.integers(len(cliff1))], int(rng.integers(n)), n))
    # insert kT T-gates at random positions
    for _ in range(kT):
        pos = rng.integers(len(steps)+1)
        steps.insert(pos, embed1(T, int(rng.integers(n)), n))
    return steps

n, depth, trials = 3, 8, 120
pn = all_paulis(n)
rows = {}
allI, allM = [], []
for kT in range(0, 5):
    Is, Ms = [], []
    for _ in range(trials):
        steps = random_circuit(n, depth, kT)
        psi = reduce(lambda acc,U: U@acc, steps, np.eye(2**n,dtype=complex))[:,0]
        Iv, Mv = indiv(steps), sre2(psi, n, pn)
        Is.append(Iv); Ms.append(Mv); allI.append(Iv); allM.append(Mv)
    rows[kT] = (np.mean(Is), np.std(Is), np.mean(Ms), np.std(Ms))

print(f"  random circuits  n={n}, depth={depth}, {trials} trials each:")
print(f"  {'#T-gates':>8} | {'indiv mean±sd':>20} | {'SRE(magic) mean±sd':>22}")
for kT,(im,isd,mm,msd) in rows.items():
    print(f"  {kT:>8} | {im:>9.2f} ± {isd:>6.2f}   | {mm:>10.3f} ± {msd:>7.3f}")
cc = np.corrcoef(allI, allM)[0,1]
print(f"\n  Pearson correlation(indiv, magic) over all {len(allI)} circuits = {cc:+.3f}")
print(f"  Clifford-only (k=0) indiv mean = {rows[0][0]:.2f}  while its magic = {rows[0][2]:.3f}")
print("  VERDICT P1: computational-basis indivisibility is LARGE for zero-magic Clifford circuits")
print("             and does not cleanly track magic -> 'magic = (Barandes) indivisibility' is FALSE.\n")

# ============================ PART 2 : qutrit discrete Wigner ============================
print("="*78)
print("PART 2 — phase-space (discrete Wigner) representation, qutrit d=3")
print("="*78)
d = 3
w = np.exp(2j*np.pi/d)
Z = np.diag([w**j for j in range(d)])
X = np.zeros((d,d), complex)
for j in range(d): X[(j+1) % d, j] = 1.0          # X|j> = |j+1>
tau = np.exp((d+1)*np.pi*1j/d)                      # tau^2 = w  (odd d)

def matpow(M,k):
    R = np.eye(d, dtype=complex)
    for _ in range(k % d): R = M @ R
    return R

def D(a, b):                                        # Weyl displacement
    return (tau**(a*b)) * (matpow(X,a) @ matpow(Z,b))

pts = [(a,b) for a in range(d) for b in range(d)]
A0 = sum(D(a,b) for (a,b) in pts) / d               # phase-point operator at origin
A = {(a,b): D(a,b) @ A0 @ D(a,b).conj().T for (a,b) in pts}

# --- self-checks (Gross axioms) ---
for u in pts:
    assert np.allclose(A[u], A[u].conj().T), "A(u) not Hermitian"
    assert np.allclose(np.trace(A[u]), 1.0), "Tr A(u) != 1"
assert np.allclose(sum(A[u] for u in pts), d*np.eye(d)), "sum A(u) != d I"
for u in pts:
    for v in pts:
        assert np.allclose(np.trace(A[u]@A[v]), d*(u==v)), "orthogonality fails"
print("  Gross axioms verified (Hermitian, Tr=1, sum=dI, Tr[A_u A_v]=d delta).")

def wig(rho):
    return np.array([[np.real(np.trace(A[(a,b)] @ rho))/d for b in range(d)] for a in range(d)])
def mana(rho):
    W = wig(rho); return np.log(np.sum(np.abs(W)))
def ket(v):
    v = np.array(v, complex); v /= np.linalg.norm(v); return np.outer(v, v.conj())

# stabilizer states must have W >= 0
z0 = ket([1,0,0])                                   # |0>, stabilizer
Wm = wig(z0)
assert Wm.min() > -1e-10, f"|0> has negative Wigner (convention bug): min={Wm.min()}"
print(f"  |0> (stabilizer):           min W = {Wm.min():+.4f}  -> W>=0 OK,  mana = {mana(z0):+.4f}")

# Clifford gates
F = np.array([[w**(j*k) for k in range(d)] for j in range(d)], complex)/np.sqrt(d)   # qutrit Fourier (Clifford)
plus = ket((F @ np.array([1,0,0],complex)))          # F|0> = |+>, stabilizer
print(f"  F|0> (Clifford on stab):    min W = {wig(plus).min():+.4f}  ,  mana = {mana(plus):+.4f}")
print(f"  Z|0> (Pauli/Clifford):      mana = {mana(ket(Z@np.array([1,0,0],complex))):+.4f}")

# non-Clifford diagonal gate (qutrit 'T'); apply to the stabilizer |+>
V = np.diag([1, 1, np.exp(2j*np.pi/9)])              # non-Clifford
psi_magic = V @ (F @ np.array([1,0,0],complex))
rho_magic = ket(psi_magic)
print(f"  V·F|0> (V non-Clifford):    min W = {wig(rho_magic).min():+.4f}  ,  mana = {mana(rho_magic):+.4f}")
# the famous 'strange state' for reference (max-magic qutrit)
strange = ket([0,1,-1])
print(f"  strange state (1,-1)/sqrt2: min W = {wig(strange).min():+.4f}  ,  mana = {mana(strange):+.4f}")

# --- gate propagators on phase space:  M(u,v) = (1/d) Tr[A(u) U A(v) U^dag] ---
def propagator(U):
    M = np.zeros((len(pts), len(pts)))
    for i,u in enumerate(pts):
        for j,v in enumerate(pts):
            M[i,j] = np.real(np.trace(A[u] @ U @ A[v] @ U.conj().T))/d
    return M
def is_perm(M, tol=1e-7):
    entrywise01 = ((np.abs(M) < tol) | (np.abs(M-1) < tol)).all()
    return bool(entrywise01 and np.allclose(M.sum(0), 1) and np.allclose(M.sum(1), 1))

for name, U in [("F (Clifford)", F), ("Z (Clifford)", Z), ("V (non-Clifford)", V)]:
    M = propagator(U)
    print(f"  propagator[{name:>17}]: permutation? {is_perm(M)!s:>5} | most-negative entry = {M.min():+.4f}")

print("\n  VERDICT P2: in the phase-space representation Clifford gates are POSITIVE PERMUTATIONS")
print("             (mana-preserving, divisible); the non-Clifford gate injects NEGATIVITY (mana>0).")
print("             => magic = Wigner negativity = obstruction to a POSITIVE, DIVISIBLE classical rep,")
print("                which lives in phase space, NOT in Barandes' computational-basis indivisibility.")
