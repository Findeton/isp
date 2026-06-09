"""
Feasibility probe for Paper 1 v6: 'Indivisible causal-set gravity'.
Tests the GEOMETRY-side claims that division events (records) can serve as the foliation-invariant
geometric substrate:

  (A) order + number = geometry:  from a Poisson sprinkling of a flat Minkowski causal diamond, recover
      the spacetime DIMENSION from the causal order alone (Myrheim-Meyer). If records carry the geometry,
      their causal order must encode d.  Expect d_recovered ~ 2 and ~ 4.

  (B) the make-or-break Lorentz condition:  a regular lattice has preferred spatial directions (hence a
      preferred frame -> breaks Lorentz); a Poisson sprinkling is isotropic in every frame (Bombelli-
      Henson-Sorkin). So the substrate is Lorentz-invariant IFF the division events Poisson-sprinkle.
      We quantify with a 4-fold anisotropy order parameter of nearest-neighbour link directions, in the
      rest frame and after a boost.

This does NOT test whether ISP's actual division events Poisson-sprinkle (that needs a relativistic ISP
model = the open step); it tests whether the substrate IDEA is geometrically consistent and isolates the
single condition the full calculation must check.
"""
import numpy as np
from scipy.optimize import brentq
from scipy.special import gammaln

rng = np.random.default_rng(11)

# ---------- (A) order+number=geometry : Myrheim-Meyer dimension from the causal order ----------
def mm_fraction(d):
    """Expected ordering fraction (relations / pairs) for a sprinkling in a d-dim causal interval."""
    # f(d) = 3 * Gamma(d/2+1) Gamma(d+1) / (2 Gamma(3d/2+1))   [Myrheim 1978 / Meyer]
    lg = gammaln
    return 1.5 * np.exp(lg(d/2+1) + lg(d+1) - lg(1.5*d+1))

def recover_dim(frac):
    return brentq(lambda d: mm_fraction(d) - frac, 0.5, 12.0)

def sprinkle_diamond(d, N):
    """Uniformly sprinkle N points in the causal diamond between origin and (1,0,..,0)."""
    if d == 2:                                  # null coords: unit square is the diamond
        uv = rng.random((N, 2))
        t = (uv[:,0] + uv[:,1]) / 2
        x = (uv[:,0] - uv[:,1]) / 2
        return np.column_stack([t, x])
    # d>=3: rejection-sample the Alexandrov interval between (0,0..) and (1,0,..)
    pts = []
    while len(pts) < N:
        t = rng.random()
        xs = rng.uniform(-1, 1, size=d-1)
        r = np.linalg.norm(xs)
        if r < t and r < (1 - t):               # inside both light cones
            pts.append(np.concatenate([[t], xs]))
    return np.array(pts)

def ordering_fraction(P):
    """Fraction of causally-related pairs (timelike order) in Minkowski (+,-,..,-)."""
    N = len(P)
    t = P[:,0]; x = P[:,1:]
    rel = 0
    for i in range(N):
        dt = t - t[i]
        dx2 = np.sum((x - x[i])**2, axis=1)
        related = (dt**2 - dx2 > 0)             # timelike separated
        related[i] = False
        rel += np.count_nonzero(related)
    return rel / (N*(N-1))                       # ordered pairs; /2 cancels (each pair counted both i,j)

print("="*74)
print("(A) order+number=geometry : recover spacetime dimension from causal order")
print("="*74)
for d, N in [(2, 2500), (3, 1800), (4, 1500)]:
    P = sprinkle_diamond(d, N)
    f = ordering_fraction(P)
    dhat = recover_dim(f)
    print(f"   true d = {d}:   ordering fraction = {f:.4f}  (theory {mm_fraction(d):.4f})   "
          f"->  recovered d = {dhat:.2f}")
print("   => the causal ORDER of the events alone encodes the dimension/geometry. records -> geometry OK.\n")

# ---------- (B) Lorentz condition : lattice has a preferred frame, Poisson does not ----------
def nn_link_angles(P):
    """Euclidean nearest-neighbour direction angle for each point (in the given frame)."""
    N = len(P); ang = np.empty(N)
    for i in range(N):
        dd = P - P[i]; dd[i] = 1e9
        j = np.argmin(np.einsum('ij,ij->i', dd, dd))
        ang[i] = np.arctan2(P[j,1]-P[i,1], P[j,0]-P[i,0])
    return ang

def anisotropy(P):
    """4-fold order parameter |<exp(4 i theta)>| : ~1 = preferred directions, ~0 = isotropic."""
    th = nn_link_angles(P)
    return np.abs(np.mean(np.exp(4j*th)))

def boost(P, beta):
    g = 1/np.sqrt(1-beta**2)
    t, x = P[:,0], P[:,1]
    return np.column_stack([g*(t - beta*x), g*(x - beta*t)])

# square lattice and Poisson set, same count, in a (t,x) patch
M = 45
gx, gy = np.meshgrid(np.linspace(0,1,M), np.linspace(0,1,M))
lattice = np.column_stack([gx.ravel(), gy.ravel()])
poisson = rng.random((M*M, 2))

print("="*74)
print("(B) Lorentz condition : preferred-frame test (4-fold anisotropy of NN links)")
print("="*74)
for name, S in [("regular lattice", lattice), ("Poisson sprinkle", poisson)]:
    a0 = anisotropy(S)
    aB = anisotropy(boost(S, 0.6))
    tag = "PREFERRED FRAME (breaks Lorentz)" if a0 > 0.3 else "isotropic (Lorentz-OK)"
    print(f"   {name:>16}:  anisotropy rest = {a0:.3f} | boosted = {aB:.3f}   -> {tag}")
print("   => only a POISSON sprinkling is frame-neutral. So the substrate is Lorentz-invariant")
print("      IFF ISP's division events Poisson-sprinkle -- the single open condition the full")
print("      relativistic-ISP calculation must check.")
