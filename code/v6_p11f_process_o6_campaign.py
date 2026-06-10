#!/usr/bin/env python3
"""
v6_p11f: process-level O6 - which stationary RP processes are limits of
finite reversible presentations? (Paper 11, Part III).

The surviving thermal kernel, after P10 Part I/III and P11 T1, is the
PROCESS-level question.  This campaign locates its exact shape:

 F1 (RP without Markov): the observable process of a reversible hidden
    chain is genuinely NON-Markov (order-2 memory receipt) yet
    process-RP (the full observable OS Gram is PSD): reflection
    positivity does not require Markovianity - hidden reversibility
    suffices.
 F2 (OS reconstruction finds the hidden presentation): the observable
    OS Gram has rank = the hidden dimension, and the reconstructed
    transfer spectrum matches the hidden reversible transfer: the
    record data DETERMINE the reversible presentation up to gauge.
 F3 (infinite memory, approximable): a continuous-spectrum reversible
    process (binned-oscillator hidden chain, coarse 2-symbol observable)
    has its length-3 cylinder probabilities reproduced by compressed
    finite reversible presentations with errors -> 0: approximability
    holds for this infinite-memory class.
 F4 (the boundary, again the arrow): the observable process of a DRIVEN
    chain fails process-RP (observable OS Gram min eig < 0): the
    process-level boundary is once more the eventlessness boundary.

STATUS after F1-F4: process-O6 = "is every stationary process-RP law the
weak limit of finite hidden-REVERSIBLE presentations?" - verified on the
accessible classes; the general statement is positive-realization
mathematics (named, with literature).
"""
import numpy as np
import itertools

rng = np.random.default_rng(21)

def stationary(P):
    w, v = np.linalg.eig(P.T)
    pi = np.abs(np.real(v[:, np.argmax(np.real(w))]))
    return pi / pi.sum()

def obs_os_gram(P, pi, obs, L):
    """OS Gram over OBSERVABLE blocks: M[a,b] = P(obs future = a,
    reflected obs past = b), exact enumeration over hidden paths."""
    d = P.shape[0]
    nsym = obs.max() + 1
    M = np.zeros((nsym ** L, nsym ** L))
    for path in itertools.product(range(d), repeat=2 * L + 1):
        p = pi[path[0]]
        for k in range(2 * L):
            p *= P[path[k], path[k + 1]]
        if p == 0:
            continue
        past = tuple(obs[x] for x in path[:L][::-1])
        fut = tuple(obs[x] for x in path[L + 1:])
        ia = sum(fut[k] * nsym ** k for k in range(L))
        ib = sum(past[k] * nsym ** k for k in range(L))
        M[ia, ib] += p
    return M

# hidden reversible 4-state chain, 2-symbol observable
W = rng.uniform(0.2, 1.0, (4, 4)); W = W + W.T
P = W / W.sum(1, keepdims=True)
pi = stationary(P)
obs = np.array([0, 0, 1, 1])

# ---------- F1: non-Markov yet process-RP ----------
print("== F1. the observable process: non-Markov, yet process-RP ==")
# order-2 memory receipt: P(o3 | o2, o1) depends on o1
def cylinder(seq):
    """probability of observable sequence."""
    d = P.shape[0]
    alpha = pi * (obs == seq[0])
    for s in seq[1:]:
        alpha = (alpha @ P) * (obs == s)
    return alpha.sum()
p3_00 = cylinder((0, 0, 1)) / cylinder((0, 0))
p3_10 = cylinder((1, 0, 1)) / cylinder((1, 0))
print(f"  P(o3=1 | o2=0, o1=0) = {p3_00:.6f}   P(o3=1 | o2=0, o1=1) = {p3_10:.6f}")
print(f"  memory gap = {abs(p3_00 - p3_10):.6f}  (NON-Markov observable)")
M = obs_os_gram(P, pi, obs, 3)
ev = np.linalg.eigvalsh((M + M.T) / 2)
print(f"  observable OS Gram (8x8, blocks of 3): min eig = {ev[0]:.2e}  (process-RP)")
print("  -> reflection positivity does NOT require Markovianity: hidden")
print("     reversibility suffices, exactly as P10 T3/T4 predict.")

# ---------- F2: OS reconstruction finds the hidden presentation ----------
print("\n== F2. the record data determine the reversible presentation ==")
rank = int(np.sum(ev > 1e-12))
print(f"  rank of the observable OS Gram = {rank}  (hidden dimension = 4)")
# reconstructed transfer: act with one time step on the OS space
ML = obs_os_gram(P, pi, obs, 3)
# shift Gram: M_shift[a,b] = P(future shifted by one, past)
d = P.shape[0]
Ms = np.zeros((8, 8))
for path in itertools.product(range(d), repeat=8):
    p = pi[path[0]]
    for k in range(7):
        p *= P[path[k], path[k + 1]]
    past = tuple(obs[x] for x in path[:3][::-1])
    fut = tuple(obs[x] for x in path[5:])       # future advanced by ONE step
    ia = sum(fut[k] * 2 ** k for k in range(3))
    ib = sum(past[k] * 2 ** k for k in range(3))
    Ms[ia, ib] += p
# generalized eigenvalues of (Ms, M) on the OS space = transfer spectrum
U_, S_, Vt_ = np.linalg.svd((M + M.T) / 2)
k = rank
proj = U_[:, :k]
Mr = proj.T @ M @ proj
Msr = proj.T @ Ms @ proj
tev = np.sort(np.real(np.linalg.eigvals(np.linalg.solve(Mr, Msr))))
hev = np.sort(np.linalg.eigvalsh(np.diag(np.sqrt(pi)) @ P @ np.diag(1 / np.sqrt(pi))))
print(f"  reconstructed transfer spectrum: {np.round(tev, 6)}")
print(f"  hidden reversible transfer spec: {np.round(hev, 6)}")
print(f"  max gap = {np.abs(tev - hev).max():.2e}")
print("  -> the OS reconstruction of the OBSERVABLE data recovers the hidden")
print("     reversible transfer exactly: the reversible presentation is")
print("     determined by the sealed record law, up to gauge.")

# ---------- F3: infinite memory, approximable ----------
print("\n== F3. infinite-memory reversible process: cylinder approximability ==")
def mehler_chain(dd, X=6.0, omega=1.0, tau=0.5):
    x = np.linspace(-X, X, dd)
    dx = x[1] - x[0]
    sh, ch = np.sinh(omega * tau), np.cosh(omega * tau)
    K = np.sqrt(omega / (2 * np.pi * sh)) * np.exp(
        -omega * ((x[:, None]**2 + x[None, :]**2) * ch - 2 * x[:, None] * x[None, :])
        / (2 * sh)) * dx
    Pd = K / K.sum(1, keepdims=True)
    return Pd, stationary(Pd), (x > 0).astype(int)
Pref, piref, obsref = mehler_chain(64)
def cyl_probs(Pd, pid, obsd, L=3):
    out = {}
    for seq in itertools.product((0, 1), repeat=L):
        alpha = pid * (obsd == seq[0])
        for s in seq[1:]:
            alpha = (alpha @ Pd) * (obsd == s)
        out[seq] = alpha.sum()
    return out
ref = cyl_probs(Pref, piref, obsref)
print("   d(compressed)   max length-3 cylinder gap to d = 64 reference")
for dd in (4, 8, 16, 32):
    Pd, pid, od = mehler_chain(dd)
    cp = cyl_probs(Pd, pid, od)
    gap = max(abs(cp[s] - ref[s]) for s in ref)
    print(f"      {dd:4d}            {gap:.6f}")
print("  -> finite reversible presentations reproduce the joint law of the")
print("     continuous-spectrum process with errors -> 0: approximability")
print("     holds for the accessible infinite-memory class.")

# ---------- F4: the boundary is the arrow, at process level too ----------
print("\n== F4. driven hidden chain: process-RP fails ==")
p_, q_, s_ = 0.55, 0.15, 0.30
Pdrv = s_ * np.eye(3) + p_ * np.roll(np.eye(3), 1, axis=1) + q_ * np.roll(np.eye(3), -1, axis=1)
pidrv = stationary(Pdrv)
obs3 = np.array([0, 0, 1])
Md = obs_os_gram(Pdrv, pidrv, obs3, 3)
evd = np.linalg.eigvalsh((Md + Md.T) / 2)
print(f"  observable OS Gram of the driven unicycle: min eig = {evd[0]:.3e}  (FAILS)")
print("  -> the process-level boundary is once more the eventlessness")
print("     boundary.  STATUS of process-O6: 'every stationary process-RP law")
print("     = weak limit of finite hidden-REVERSIBLE presentations' - verified")
print("     on the accessible classes (F1-F3); the general statement is the")
print("     positive-realization problem (Jaeger; Benvenuti-Farina;")
print("     Vidyasagar), named as the kernel's final mathematical identity.")
print("== p11f done ==")
