"""
Paper 2 v6, follow-up: is the oriented spatial direction recoverable k-LOCALLY (not just globally)?

The global spectral embedding (v6_p2_spatial_direction.py) showed the slice's spatial coordinates live in the
graph Laplacian's low modes (corr ~0.94, R^2 ~0.93) -- so the INFORMATION is present. But a local deformation
needs a LOCAL frame at each event. Test: for each slice event, take its causal-data neighbourhood (smallest
'meeting heights' = nearest spatial neighbours), run classical MDS on the local distance matrix, and check
(via Procrustes) whether the local embedding recovers the TRUE local tangent frame (relative positions of the
neighbours). High alignment => ingredient (iii) is k-locally available => the directional deformation is
buildable locally; this is the decisive k-local test the no-go corollary asked for.
"""
import numpy as np
from scipy.spatial import procrustes
rng = np.random.default_rng(0)

def sprinkle(d, N, ht, hx):
    P = np.empty((N, d)); P[:, 0] = rng.uniform(-ht, ht, N)
    for k in range(1, d): P[:, k] = rng.uniform(-hx, hx, N)
    return P
def causal(P):
    t, x = P[:, 0], P[:, 1:]; N = len(P); R = np.zeros((N, N), dtype=np.float32)
    for i in range(N):
        dt = t - t[i]; dx2 = np.sum((x - x[i])**2, axis=1)
        R[i] = ((dt > 0) & (dt*dt - dx2 > 0)).astype(np.float32)
    return R
def meeting_heights(P, R, A, delta):
    notslab = (P[:, 0] >= delta).astype(np.float32); ha = R.T @ notslab
    nA = len(A); M = np.full((nA, nA), np.inf)
    for ia, a in enumerate(A):
        Ra = R[a] > 0
        for ib in range(ia+1, nA):
            cf = Ra & (R[A[ib]] > 0)
            if cf.any(): M[ia, ib] = M[ib, ia] = ha[cf].min()
    np.fill_diagonal(M, 0.0)
    return M
def cmds(Dsq, dim=2):
    n = len(Dsq); J = np.eye(n) - np.ones((n, n))/n
    B = -0.5 * J @ Dsq @ J
    w, V = np.linalg.eigh(B); idx = np.argsort(w)[::-1][:dim]
    return V[:, idx] * np.sqrt(np.clip(w[idx], 0, None))

print("="*80)
print("Paper 2 v6: is the spatial frame recoverable k-LOCALLY? (local MDS per event)")
print("="*80)
dspt = 3                                    # 2+1 spacetime: meeting height m ∝ d_spatial^dspt => Dsq=m^(2/dspt)
allR2 = []
for trial in range(4):
    P = sprinkle(3, 11000, 2.2, 2.2); R = causal(P)
    delta = 0.32
    A = np.where(np.abs(P[:, 0]) < delta/2)[0]; A = A[np.max(np.abs(P[A, 1:]), axis=1) < 1.6]
    M = meeting_heights(P, R, A, delta)
    Xtrue = P[A, 1:]
    kNN = 12
    for i in range(len(A)):
        nb = [j for j in np.argsort(M[i]) if np.isfinite(M[i, j]) and j != i][:kNN]
        if len(nb) < 6: continue
        idx = [i] + nb
        sub = M[np.ix_(idx, idx)].copy()
        fin = sub[np.isfinite(sub)]
        if fin.size < 0.5*sub.size: continue            # need mostly-finite local block
        sub[~np.isfinite(sub)] = fin.max()*1.2          # cap unmet pairs as "far"
        Dsq = sub**(2.0/dspt)               # convert meeting-height to squared spatial distance
        emb = cmds(Dsq, 2)
        true = Xtrue[idx]
        try:
            _, _, disp = procrustes(true - true.mean(0), emb - emb.mean(0))
            allR2.append(1 - disp)          # 1 - Procrustes disparity ~ fraction of local structure recovered
        except Exception:
            pass

allR2 = np.array(allR2)
print(f"\n   local-frame recovery over {len(allR2)} neighbourhoods (2+1):")
print(f"   1 - Procrustes disparity:  mean={allR2.mean():.2f}  median={np.median(allR2):.2f}  "
      f"frac>0.8={np.mean(allR2>0.8):.2f}")

print("\n" + "="*80)
print("VERDICT")
print("="*80)
q = allR2.mean()
if q > 0.8:
    print(f"- k-LOCAL SUCCESS: local MDS recovers the local tangent frame (mean {q:.2f}). The oriented spatial")
    print("  direction is available NOT just globally but k-LOCALLY, at each event, from order+counts. So")
    print("  ingredient (iii) is genuinely k-local -> the directional deformation is buildable. NOT a no-go.")
    print("  Remaining: assemble g^{ij}∂_jN with this local frame + the extracted metric, verify bracket")
    print("  closure, and the curved/continuum limit.")
elif q > 0.55:
    print(f"- k-LOCAL PARTIAL: local frame recovered but noisily (mean {q:.2f}). Direction is locally present")
    print("  but a clean local estimator needs work (consistent with Rideout-Wallden's spacelike-distance noise).")
else:
    print(f"- k-LOCAL WEAK (mean {q:.2f}): the local neighbourhood does not cleanly give a frame; the recovery")
    print("  may be an inherently GLOBAL (spectral) effect -- a real caveat for a k-local deformation.")
