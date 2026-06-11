#!/usr/bin/env python3
"""
v6_p30i: the d = 2 floor THEOREM (Paper 30, NR campaign).

THEOREM (the d = 2 floor).  Every positive word in two 2x2 positive
definite letters has real spectrum.  (So the complex-spectrum
phenomenon - and the (NR) question - genuinely begins at d >= 3.)

PROOF.  Normalize determinants to 1 (scalars do not affect spectral
reality).  A symmetric PD matrix of det 1 is exp(S) with S symmetric
traceless: a hyperbolic Mobius transformation (transvection) whose
boundary fixed points are its eigendirections - two ORTHOGONAL
directions, so the axis passes through the basepoint i of the
upper half-plane (the geodesic with endpoints p, q has i on it iff
pq = -1, which orthogonality gives).  Two distinct axes through a
common interior point CROSS, so the four boundary fixed points
interleave: xiA+, xiB+, xiA-, xiB- in cyclic order.  Let J be the
closed boundary arc from xiA+ to xiB+ not containing the repellers.
North-south dynamics: A moves every point of J toward xiA+ (staying
in J), B moves every point of J toward xiB+ (staying in J) - J is
invariant under BOTH letters, hence under every positive word.  A
continuous map of a closed arc into itself has a fixed point: the
word has a real eigendirection, and a real 2x2 matrix with one real
eigenvalue has two.  QED.

 (i)   interleaving receipt: the four boundary fixed points
       alternate for random PD pairs (the axes cross at i);
 (ii)  invariant-arc receipt: A(J) inside J and B(J) inside J,
       sampled densely;
 (iii) word receipt: random positive words have a real
       eigendirection INSIDE J and fully real spectra - including
       long words and extreme conditioning.
"""
import numpy as np

rng = np.random.default_rng(308)

def rand_pd(rng, spread=2.0):
    th = rng.uniform(0, np.pi)
    c, s = np.cos(th), np.sin(th)
    R = np.array([[c, -s], [s, c]])
    lam = np.exp(spread * rng.standard_normal())
    return R @ np.diag([lam, 1 / lam]) @ R.T   # det = 1

def boundary_pts(A):
    # eigendirections as boundary points x = v0/v1 of RP^1
    lam, V = np.linalg.eigh(A)
    # attracting = larger eigenvalue direction
    plus, minus = V[:, 1], V[:, 0]
    def proj(v):
        return np.inf if abs(v[1]) < 1e-300 else v[0] / v[1]
    return proj(plus), proj(minus)

def circ(x):
    # map RP^1 (R cup inf) to angle in [0, pi)
    return np.pi / 2 if np.isinf(x) else np.arctan(x) % np.pi

def interleaved(a_p, a_m, b_p, b_m):
    # check A,B endpoint alternation on the circle [0, pi)
    pts = sorted([(circ(a_p), "A"), (circ(a_m), "A"),
                  (circ(b_p), "B"), (circ(b_m), "B")])
    labels = [p[1] for p in pts]
    return labels in (["A", "B", "A", "B"], ["B", "A", "B", "A"])

# ---------- (i) interleaving ----------
print("== (i) the axes cross: boundary fixed points interleave ==")
ok = 0
for _ in range(500):
    A, B = rand_pd(rng), rand_pd(rng)
    ap, am = boundary_pts(A)
    bp, bm = boundary_pts(B)
    ok += interleaved(ap, am, bp, bm)
print(f"  interleaving holds in {ok}/500 random PD pairs")
print("  -> symmetric PD axes all pass through the basepoint, so")
print("     distinct axes cross and their endpoints alternate -")
print("     the geometric premise, receipted.")

# ---------- (ii) the invariant arc ----------
print("\n== (ii) the invariant arc J ==")
def mobius(M, x):
    if np.isinf(x):
        return np.inf if abs(M[1, 0]) < 1e-300 else M[0, 0] / M[1, 0]
    den = M[1, 0] * x + M[1, 1]
    return np.inf if abs(den) < 1e-300 else (M[0, 0] * x + M[0, 1]) / den

def in_arc(x, lo, hi):
    # closed arc from lo to hi (angles, increasing mod pi)
    t = circ(x)
    if lo <= hi:
        return lo - 1e-12 <= t <= hi + 1e-12
    return t >= lo - 1e-12 or t <= hi + 1e-12

viol = 0
trials = 300
for _ in range(trials):
    A, B = rand_pd(rng), rand_pd(rng)
    ap, am = boundary_pts(A)
    bp, bm = boundary_pts(B)
    if not interleaved(ap, am, bp, bm):
        continue
    # J = arc between A+ and B+ not containing A-,B-
    ta, tb = circ(ap), circ(bp)
    # choose orientation of J avoiding the repellers
    cands = [(ta, tb), (tb, ta)]
    J = None
    for lo, hi in cands:
        if not in_arc(am, lo, hi) and not in_arc(bm, lo, hi):
            J = (lo, hi)
    if J is None:
        continue
    lo, hi = J
    for t in np.linspace(0, 1, 25):
        ang = (lo + t * ((hi - lo) % np.pi)) % np.pi
        x = np.inf if abs(ang - np.pi / 2) < 1e-12 else np.tan(ang)
        for M in (A, B):
            if not in_arc(mobius(M, x), lo, hi):
                viol += 1
print(f"  J-invariance violations over {trials} pairs x 25 boundary")
print(f"  points x both letters: {viol}")
print("  -> A(J) and B(J) stay inside J: every positive word maps J")
print("     into itself; the interval fixed point is forced.")

# ---------- (iii) word receipts ----------
print("\n== (iii) words: real spectra with eigendirection in J ==")
bad_spec, bad_loc, n_tested = 0, 0, 0
worst_im = 0.0
for _ in range(400):
    A, B = rand_pd(rng), rand_pd(rng)
    ap, am = boundary_pts(A)
    bp, bm = boundary_pts(B)
    if not interleaved(ap, am, bp, bm):
        continue
    ta, tb = circ(ap), circ(bp)
    J = None
    for lo, hi in ((ta, tb), (tb, ta)):
        if not in_arc(am, lo, hi) and not in_arc(bm, lo, hi):
            J = (lo, hi)
    if J is None:
        continue
    n_tested += 1
    L = rng.integers(3, 15)
    w = rng.integers(0, 2, L)
    M = np.eye(2)
    for ch in w:
        M = M @ (A if ch == 0 else B)
    ev, V = np.linalg.eig(M)
    worst_im = max(worst_im,
                   float(np.abs(ev.imag).max() / np.abs(ev).max()))
    if np.abs(ev.imag).max() > 1e-9 * np.abs(ev).max():
        bad_spec += 1
        continue
    # real eigendirection inside J?
    found = False
    for k in range(2):
        v = V[:, k].real
        if np.linalg.norm(v) > 1e-12 and in_arc(
                np.inf if abs(v[1]) < 1e-300 else v[0] / v[1], *J):
            found = True
    bad_loc += not found
print(f"  words tested: {n_tested};  nonreal spectra: {bad_spec};")
print(f"  max |Im|/rho seen: {worst_im:.1e};")
print(f"  real eigendirection found inside J: failures = {bad_loc}")
print("  -> THE THEOREM, live: every positive word in two PD 2x2")
print("     letters has real spectrum, with the fixed direction in")
print("     the invariant arc exactly where the proof puts it.  The")
print("     complex-spectrum phenomenon - and (NR) - begins at")
print("     d >= 3.")
print("== p30i done ==")
