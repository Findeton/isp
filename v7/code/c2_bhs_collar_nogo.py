"""
v7 C2 deferral probe -- why discharging Paper VII's covariance premise is BLOCKED on discreteness.

Paper VII's microcausality inheritance is CONDITIONAL on one premise: the holonomy diamond
coarse-grains, under an emergent Lorentz action, to a POINT-LOCAL self-adjoint Lorentz-scalar
seal density (collar -> 0). The premise factors into three legs:
   (P-Lor)    the causal ORDER / sigma-arrow descends Lorentz-invariantly;
   (P-point)  the diamond's finite-valency COLLAR coarse-grains to a point;
   (P-scalar) the seal is a scalar under the emergent Lorentz action.

This probe shows the honest split: leg (P-Lor) REDUCES (a real, small win), but leg (P-point) is
BLOCKED by the corpus's own Bombelli-Henson-Sorkin (BHS) result -- a Poisson sprinkling admits NO
Lorentz-invariant finite-valency graph. So point-locality of the seal collar cannot come from
discreteness alone; recovering it imports the unbuilt matter sector / an emergent Lorentz group on
operators (the field's open emergence-of-Lorentz core). => Paper VII stays CONDITIONAL.

Checks (1+1 Minkowski, mpmath/numpy):
  (C1) s^2 = -t^2 + x^2 is boost-invariant  -> the causal order is Lorentz-invariant [(P-Lor) reduces].
  (C2) the k-nearest-neighbour COLLAR of a point is FRAME-DEPENDENT under a boost (BHS no-go in
       action): the "nearest neighbours" in the rest frame are NOT the nearest in a boosted frame.
  (C3) the causal order (who is in the past/future light cone) is INVARIANT under the same boost --
       isolating that the sigma-ARROW descends LI while the finite COLLAR pick does not.

Pre-geometric note: this is a probe of the EMERGENT-geometry leg of an avowedly conditional premise;
it documents what discreteness can and cannot supply, it is not used as a derivation input.
"""
import numpy as np

PASS = {}


def head(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)


def boost(eta, T, X):
    """active Lorentz boost with rapidity eta in 1+1: t' = cosh t - sinh x, x' = -sinh t + cosh x."""
    c, s = np.cosh(eta), np.sinh(eta)
    return c * T - s * X, -s * T + c * X


rng = np.random.default_rng(7)
eta = 0.9  # boost rapidity

# Poisson sprinkling: N points uniform in a spacetime box around the origin
N = 400
T = rng.uniform(-3, 3, N)
X = rng.uniform(-3, 3, N)
s2 = -T**2 + X**2                      # interval^2 from the origin

# ---------------------------------------------------------------------------
head("(C1) s^2 = -t^2 + x^2 is boost-invariant => the causal order is Lorentz-invariant")
Tb, Xb = boost(eta, T, X)
s2b = -Tb**2 + Xb**2
max_dev = float(np.max(np.abs(s2 - s2b)))
print("  max |s^2 - s'^2| over %d sprinkled points under rapidity %.1f = %.2e" % (N, eta, max_dev))
PASS["(C1) (P-Lor) s^2 boost-invariant to ~machine precision (causal order descends LI)"] = max_dev < 1e-10

# ---------------------------------------------------------------------------
head("(C2) the k-nearest COLLAR is FRAME-DEPENDENT (BHS: no LI finite-valency graph)")
# "collar" = the k nearest neighbours of the origin by Euclidean coordinate distance in a frame.
k = 5
d_rest = np.sqrt(T**2 + X**2)               # coordinate distance in the rest frame
d_boost = np.sqrt(Tb**2 + Xb**2)            # coordinate distance in the boosted frame
collar_rest = set(np.argsort(d_rest)[:k].tolist())
collar_boost = set(np.argsort(d_boost)[:k].tolist())
overlap = collar_rest & collar_boost
print("  k=%d nearest to origin in REST frame:    %s" % (k, sorted(collar_rest)))
print("  k=%d nearest to origin in BOOSTED frame: %s" % (k, sorted(collar_boost)))
print("  overlap = %d of %d  => the collar pick CHANGES under boost (frame-dependent)" % (len(overlap), k))
PASS["(C2) (P-point) the k-nearest collar is frame-DEPENDENT (BHS no-go: no LI finite-valency graph)"] = (
    collar_rest != collar_boost)

# ---------------------------------------------------------------------------
head("(C3) the causal ORDER is INVARIANT under the same boost (sigma-arrow LI, collar not)")
# past = timelike-and-earlier: s^2 < 0 AND t < 0 (in each frame); future: s^2 < 0 AND t > 0.
past_rest = set(np.where((s2 < 0) & (T < 0))[0].tolist())
fut_rest = set(np.where((s2 < 0) & (T > 0))[0].tolist())
past_boost = set(np.where((s2b < 0) & (Tb < 0))[0].tolist())
fut_boost = set(np.where((s2b < 0) & (Tb > 0))[0].tolist())
print("  |past| rest=%d boost=%d  (same set: %s)" % (len(past_rest), len(past_boost), past_rest == past_boost))
print("  |future| rest=%d boost=%d  (same set: %s)" % (len(fut_rest), len(fut_boost), fut_rest == fut_boost))
PASS["(C3) (P-Lor) the causal order (past/future light cone) is boost-INVARIANT -- the arrow descends LI"] = (
    past_rest == past_boost and fut_rest == fut_boost)

# decisive contrast: the SAME boost leaves the causal order fixed but moves the collar -- so
# point-locality of the seal cannot be inherited from the LI substrate by a finite collar.
PASS["(C2/C3 contrast) order LI but collar frame-dependent => point-locality NOT from discreteness alone"] = (
    (past_rest == past_boost) and (collar_rest != collar_boost))

# ---------------------------------------------------------------------------
head("MACHINE CHECKS")
ok = True
for kk, v in PASS.items():
    print("  [%s] %s" % ("PASS" if v else "FAIL", kk))
    ok = ok and v
print("\n  " + ("ALL CHECKS PASS" if ok else "*** SOME CHECK FAILED ***"))
assert ok, "a check failed"
print("=" * 78)
print("DONE.  The sigma-arrow / causal order descends Lorentz-invariantly (P-Lor reduces), but the")
print("       finite-valency seal COLLAR is frame-dependent (BHS no-go), so collar->0 point-locality")
print("       cannot come from discreteness alone.  Discharging Paper VII's premise is BLOCKED on the")
print("       emergence-of-Lorentz core -- Paper VII stays CONDITIONAL; only a premise-sharpening note.")
print("=" * 78)
