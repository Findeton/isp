"""
Paper 2 v6: can an ORIENTED spatial direction be recovered from causal order + counts on a slice?

Reduction (Paper 1 v6 §5.14): the only missing ingredient for GR dynamics is a k-local oriented spatial
direction on a maximal antichain. Test it via SPECTRAL EMBEDDING: build a spatial neighbour graph on the
slice from causal data (Rideout-Wallden-style 'meeting height' = earliest common-future event), then check
whether the graph Laplacian's low eigenvectors (Laplacian eigenmaps / Fiedler vector) recover the TRUE
spatial coordinates of the slice events (which the construction never sees). High correlation => an oriented
direction is recoverable from order+counts (ingredient iii available). Noise => toward the full no-go.
"""
import numpy as np
from numpy.linalg import eigh
rng = np.random.default_rng(0)

def sprinkle(d, N, half_t, half_x):
    P = np.empty((N, d)); P[:, 0] = rng.uniform(-half_t, half_t, N)
    for k in range(1, d): P[:, k] = rng.uniform(-half_x, half_x, N)
    return P

def causal(P):
    t, x = P[:, 0], P[:, 1:]; N = len(P); R = np.zeros((N, N), dtype=np.float32)
    for i in range(N):
        dt = t - t[i]; dx2 = np.sum((x - x[i])**2, axis=1)
        R[i] = ((dt > 0) & (dt*dt - dx2 > 0)).astype(np.float32)
    return R

def meeting_heights(P, R, A, delta):
    """M[a,b] = min count-height above slab of a common-future event of slice events a,b (~spatial dist)."""
    notslab = (P[:, 0] >= delta).astype(np.float32)
    ha = R.T @ notslab                              # above-slab ancestor count per event (height proxy)
    nA = len(A); M = np.full((nA, nA), np.inf)
    for ia, a in enumerate(A):
        Ra = R[a] > 0
        for ib in range(ia+1, nA):
            cf = Ra & (R[A[ib]] > 0)
            if cf.any():
                m = ha[cf].min(); M[ia, ib] = M[ib, ia] = m
    return M

def spectral_coords(M, kNN=8, n_modes=2):
    nA = len(M); W = np.zeros((nA, nA))
    for i in range(nA):
        order = np.argsort(M[i]); nb = [j for j in order if np.isfinite(M[i, j]) and j != i][:kNN]
        if nb:
            sc = np.median([M[i, j] for j in nb]) + 1e-9
            for j in nb:
                w = np.exp(-M[i, j]/sc); W[i, j] = max(W[i, j], w); W[j, i] = W[i, j]
    D = np.diag(W.sum(1)); L = D - W
    vals, vecs = eigh(L)                              # ascending; vecs[:,0]~const
    return vecs[:, 1:1+n_modes]

def r2_recover(coords_true, coords_emb):
    """R^2 of regressing each true coordinate on the embedding (best linear recovery)."""
    X = np.column_stack([coords_emb, np.ones(len(coords_emb))])
    r2s = []
    for c in coords_true.T:
        beta, *_ = np.linalg.lstsq(X, c, rcond=None)
        pred = X @ beta; ss = 1 - np.sum((c-pred)**2)/np.sum((c-c.mean())**2)
        r2s.append(ss)
    return r2s

print("="*80)
print("Paper 2 v6: spatial direction from causal order (spectral embedding of slice graph)")
print("="*80)

# ---- 1+1: recover the 1D spatial coordinate x from the Fiedler vector ----
print("\n[1+1] recover slice x-coordinate from Fiedler vector v2:")
corrs = []
for trial in range(6):
    P = sprinkle(2, 4000, 3.0, 3.0); R = causal(P)
    delta = 0.18
    A = np.where(np.abs(P[:, 0]) < delta/2)[0]
    A = A[np.abs(P[A, 1]) < 2.2]                      # central, avoid x-boundary
    M = meeting_heights(P, R, A, delta)
    v = spectral_coords(M, kNN=8, n_modes=1)
    c = np.corrcoef(v[:, 0], P[A, 1])[0, 1]
    corrs.append(abs(c))
print(f"   |A|~{len(A)};  |corr(v2, x_true)| over 6 trials = "
      f"{np.array2string(np.array(corrs), precision=2)}   mean={np.mean(corrs):.2f}")

# ---- 2+1: recover (x,y) from {v2,v3} ----
print("\n[2+1] recover slice (x,y) from {v2,v3} (Laplacian eigenmaps):")
r2x, r2y = [], []
for trial in range(4):
    P = sprinkle(3, 11000, 2.2, 2.2); R = causal(P)
    delta = 0.32
    A = np.where(np.abs(P[:, 0]) < delta/2)[0]
    A = A[np.max(np.abs(P[A, 1:]), axis=1) < 1.5]
    M = meeting_heights(P, R, A, delta)
    emb = spectral_coords(M, kNN=10, n_modes=2)
    r2 = r2_recover(P[A, 1:], emb)
    r2x.append(r2[0]); r2y.append(r2[1])
print(f"   |A|~{len(A)};  R^2 recovering x from (v2,v3): mean={np.mean(r2x):.2f};  "
      f"y: mean={np.mean(r2y):.2f}")
print(f"   (R^2 -> 1 means the 2 eigenmodes linearly span the true (x,y): full oriented frame recovered)")

print("\n" + "="*80)
print("VERDICT")
print("="*80)
c1 = np.mean(corrs); rr = 0.5*(np.mean(r2x)+np.mean(r2y))
if c1 > 0.6 and rr > 0.5:
    print(f"- SUCCESS (qualified): spatial coordinates ARE recovered from order+counts -- 1+1 |corr|={c1:.2f},")
    print(f"  2+1 mean R^2={rr:.2f}. The slice graph Laplacian's low modes give an ORIENTED spatial frame, so")
    print("  ingredient (iii) is AVAILABLE k-locally (spectrally). The directional deformation is buildable in")
    print("  principle; remaining work is locality/continuum-limit of the construction (spectral embedding is")
    print("  global, so a genuinely k-LOCAL version must be shown). NOT a no-go.")
elif c1 > 0.35 or rr > 0.3:
    print(f"- PARTIAL/NOISY: 1+1 |corr|={c1:.2f}, 2+1 R^2={rr:.2f} -- spatial direction is recoverable but noisy")
    print("  (consistent with Rideout-Wallden 'spacelike distance is hard'). Oriented direction exists in")
    print("  principle; whether a CLEAN k-local version does is open.")
else:
    print(f"- TOWARD NO-GO: 1+1 |corr|={c1:.2f}, 2+1 R^2={rr:.2f} ~ noise -- the causal-data slice graph does")
    print("  NOT recover an oriented spatial coordinate, so ingredient (iii) is not available by this route.")
