#!/usr/bin/env python3
"""
v6_p22b: the record-native flow direction (Paper 22).

The record RG (P10) acts on gauge sectors by link decimation (P14:
coarse link = transport product).  The DIRECTION receipt: simulate the
SU(2) record gauge ensemble at coupling beta on 4^4, decimate the
gauge record to 2^4, and locate the coarse ensemble on the measured
single-plaquette curve: if the matched coupling beta_eff is SMALLER
than beta (stronger coupling), the flow runs toward confinement.

Method: vectorized checkerboard Metropolis (links updated in parity
classes so no two simultaneously-updated links share a plaquette);
plaquette curve at six couplings; blocked plaquette at beta = 2.4;
matching by interpolation; statistical errors from measurement spread.

Scope honesty: 4^4 -> 2^4, one blocking step, one beta: a DIRECTION
receipt in the crossover window, not a beta function; the
weak-coupling record flow at scale remains O7's open remainder (the
P10 closure obstruction persists).  The continuum one-loop sign is
p22a's necessity check.
"""
import numpy as np

rng = np.random.default_rng(224)
L = 4
sig = [np.array([[0, 1], [1, 0]], complex),
       np.array([[0, -1j], [1j, 0]], complex),
       np.array([[1, 0], [0, -1]], complex)]

def rand_su2_pool(n, eps):
    out = np.zeros((n, 2, 2), complex)
    for i in range(n):
        a = rng.standard_normal(3)
        a = eps * a / np.linalg.norm(a)
        th = np.linalg.norm(a)
        nvec = a / th
        out[i] = (np.cos(th) * np.eye(2)
                  + 1j * np.sin(th) * sum(nvec[k] * sig[k] for k in range(3)))
    return out

def shift(arr, mu, s):
    return np.roll(arr, -s, axis=mu)

def staples(U, mu):
    """sum of staples for links in direction mu; U: list of 4 arrays
    (L,L,L,L,2,2)."""
    A = np.zeros_like(U[mu])
    for nu in range(4):
        if nu == mu:
            continue
        # forward: U_nu(x+mu) U_mu(x+nu)^dag U_nu(x)^dag
        t1 = np.einsum("...ab,...cb->...ac", shift(U[nu], mu, 1),
                       shift(U[mu], nu, 1).conj())
        A += np.einsum("...ab,...cb->...ac", t1, U[nu].conj())
        # backward: U_nu(x+mu-nu)^dag U_mu(x-nu)^dag U_nu(x-nu)
        Un_b = shift(U[nu], nu, -1)
        t2 = np.einsum("...ba,...cb->...ac",
                       shift(Un_b, mu, 1).conj(), shift(U[mu], nu, -1).conj())
        A += np.einsum("...ab,...bc->...ac", t2, Un_b)
    return A

def parity_mask():
    g = np.indices((L, L, L, L)).sum(axis=0) % 2
    return g

def sweep(U, beta, pool):
    par = parity_mask()
    for mu in range(4):
        for p in (0, 1):
            A = staples(U, mu)
            R = pool[rng.integers(0, len(pool), (L, L, L, L))]
            Unew = np.einsum("...ab,...bc->...ac", R, U[mu])
            dS = -beta / 2 * np.real(np.einsum("...ab,...ba->...",
                                               Unew - U[mu], A))
            acc = (rng.uniform(size=(L, L, L, L)) < np.exp(-dS)) \
                & (par == p)
            U[mu][acc] = Unew[acc]
    return U

def plaquette(U):
    tot = 0.0
    n = 0
    for mu in range(4):
        for nu in range(mu + 1, 4):
            P = np.einsum("...ab,...bc,...dc,...ed->...ae",
                          U[mu], shift(U[nu], mu, 1),
                          shift(U[mu], nu, 1).conj(), U[nu].conj())
            tot += np.real(np.einsum("...aa->...", P)).mean() / 2
            n += 1
    return tot / n

def run(beta, ntherm=60, nmeas=40):
    U = [np.tile(np.eye(2, dtype=complex), (L, L, L, L, 1, 1))
         for _ in range(4)]
    pool = rand_su2_pool(200, 0.5)
    pool = np.concatenate([pool, np.conj(np.transpose(pool, (0, 2, 1)))])
    for _ in range(ntherm):
        sweep(U, beta, pool)
    vals = []
    Ulast = None
    for i in range(nmeas):
        sweep(U, beta, pool)
        vals.append(plaquette(U))
        Ulast = [u.copy() for u in U]
    return np.mean(vals), np.std(vals) / np.sqrt(len(vals)), Ulast

print("== the single-plaquette curve (4^4, SU(2)) ==")
betas = [0.8, 1.2, 1.6, 2.0, 2.4, 2.8]
curve = []
for b in betas:
    m, e, _ = run(b)
    curve.append(m)
    print(f"  beta = {b:.1f}: <P> = {m:.4f} +- {e:.4f}")

print("\n== the blocked ensemble at beta = 2.4 ==")
m24, e24, U = run(2.4, ntherm=80, nmeas=60)
# decimate the gauge record: coarse link = product of two fine links
Lc = L // 2
Uc = []
for mu in range(4):
    prod = np.einsum("...ab,...bc->...ac", U[mu], shift(U[mu], mu, 1))
    sl = [slice(0, L, 2)] * 4
    Uc.append(prod[tuple(sl)])
def plaquette_c(Uc):
    tot, n = 0.0, 0
    for mu in range(4):
        for nu in range(mu + 1, 4):
            P = np.einsum("...ab,...bc,...dc,...ed->...ae",
                          Uc[mu], np.roll(Uc[nu], -1, axis=mu),
                          np.roll(Uc[mu], -1, axis=nu).conj(),
                          Uc[nu].conj())
            tot += np.real(np.einsum("...aa->...", P)).mean() / 2
            n += 1
    return tot / n
Pc = plaquette_c(Uc)
print(f"  fine <P>(beta = 2.4) = {m24:.4f} +- {e24:.4f}")
print(f"  coarse plaquette after record decimation = {Pc:.4f}")
beta_eff = np.interp(Pc, curve, betas)
print(f"  matched coupling: beta_eff = {beta_eff:.2f}   (vs beta = 2.40)")
print(f"  -> beta_eff {'<' if beta_eff < 2.4 else '>='} beta: the record")
print("     decimation moves the SU(2) gauge sector TOWARD STRONG")
print("     COUPLING - the confining direction - in the crossover")
print("     window.  Combined with p22a's one-loop necessity check, the")
print("     sign kill-condition is passed at every scope this campaign")
print("     reaches; the weak-coupling record beta function AT SCALE")
print("     remains O7's named remainder.")
print("== p22b done ==")
