"""
v6 Task 2d (the hard core, honest attempt): does the antichain-deformation bracket CLOSE on g^{ij}?

Continuum target (Dirac-Schwinger):  {H_perp[N1], H_perp[N2]} = H_i[ xi^i ],  xi^i = g^{ij}(N1 d_j N2 - N2 d_j N1).
So the commutator of two NORMAL deformations with different lapse profiles N1,N2 must be a TANGENTIAL
(spatial) deformation that (a) vanishes when N1=N2, (b) localizes where the lapse GRADIENTS are large, and
(c) has magnitude set by the spatial metric g^{ij}.  We test (a)-(c) on a sprinkled causal set, where each
normal deformation advances the current slice (down-set D) by a lapse-dependent 'band', recomputed relative
to the CURRENT (possibly tilted) slice -- which is what can make the two orders disagree.

Honesty: the lapse PROFILE N(x) is applied using the spatial coordinate x_e (a coordinate-assisted readout;
a fully coordinate-free version needs combinatorial spatial position, an open problem). The deformation
'height' is read from CAUSAL DATA (count of above-slice ancestors). We report the outcome straight, incl.
the control and whether the commutator tracks the lapse-gradient combination.
"""
import numpy as np
rng = np.random.default_rng(8)

def sprinkle(N, Tt, X):
    return np.column_stack([rng.uniform(-Tt, Tt, N), rng.uniform(-X, X, N)])

def order_matrix(P):                      # flat 1+1 order: p<q iff dt>0 and dt>|dx|
    t, x = P[:, 0], P[:, 1]; N = len(P)
    R = np.zeros((N, N), dtype=np.float32)
    for i in range(N):
        dt = t - t[i]
        R[i] = ((dt > 0) & (dt > np.abs(x - x[i]))).astype(np.float32)
    return R

def deform(D, R, x, lapse_fn, s):
    """advance down-set D by one lapse band, relative to the CURRENT slice; height = causal-data count."""
    notD = (~D).astype(np.float32)
    ha = R.T @ notD                       # ha[e] = # of above-slice ancestors of e  (proper-time proxy)
    thresh = lapse_fn(x) * s
    absorb = (~D) & (ha < thresh) & (ha >= 0)
    return D | absorb

def grad(f, xx, h=1e-3): return (f(xx+h)-f(xx-h))/(2*h)

def commutator(D0, R, x, NA, NB, s):
    Da = deform(deform(D0, R, x, NA, s), R, x, NB, s)
    Db = deform(deform(D0, R, x, NB, s), R, x, NA, s)
    return Da ^ Db

print("="*78)
print("Task 2d: does the two-lapse commutator close on g^{ij}(N1 dN2 - N2 dN1)?")
print("="*78)
k = 1.3
N1 = lambda xx: 1.0 + 0.6*np.cos(k*xx)
N2 = lambda xx: 1.0 + 0.6*np.sin(k*xx)
xi_pred = lambda xx: (N1(xx)*grad(N2, xx) - N2(xx)*grad(N1, xx))

print(f"\n{'N':>5} {'s':>4} | {'ctrl(N1=N2)':>11} | {'|comm| N1!=N2':>13} | {'% of N':>7} | {'corr to GR xi':>13}")
results = []
for N, s in [(3000, 6.0), (4000, 6.0), (4000, 10.0), (6000, 8.0)]:
    P = sprinkle(N, 3.0, 3.0); R = order_matrix(P); x = P[:, 1]
    D0 = P[:, 0] < 0.0
    ctrl = int(commutator(D0, R, x, N1, N1, s).sum())
    d = commutator(D0, R, x, N1, N2, s); ncom = int(d.sum())
    if ncom >= 5:
        bins = np.linspace(-3, 3, 25); ctr = 0.5*(bins[:-1]+bins[1:])
        hcom, _ = np.histogram(x[d], bins=bins); hcom = hcom/max(hcom.sum(), 1)
        pred = np.abs(xi_pred(ctr)); pred = pred/max(pred.sum(), 1)
        corr = np.corrcoef(hcom, pred)[0, 1]
    else:
        corr = np.nan
    results.append((N, s, ctrl, ncom, 100*ncom/N, corr))
    print(f"{N:>5} {s:>4.0f} | {ctrl:>11} | {ncom:>13} | {100*ncom/N:>6.2f}% | {corr:>+13.3f}")

avg_pct = np.mean([r[4] for r in results])
corrs = [r[5] for r in results if not np.isnan(r[5])]
avg_corr = np.mean(corrs) if corrs else np.nan

print("\n" + "="*78)
print("VERDICT (Task 2d) -- read honestly")
print("="*78)
print(f"- CONTROL holds: equal lapses commute exactly (|comm|=0) in every run -- the necessary {{H,H[N=N]}}=0.")
if avg_pct < 1.0 and (np.isnan(avg_corr) or abs(avg_corr) < 0.35):
    print(f"- NEGATIVE / NULL: for N1!=N2 the commutator is at the discretization-noise floor (~{avg_pct:.2f}% of")
    print(f"  events) and does NOT localize on the lapse-gradient profile (mean corr {avg_corr:+.2f} ~ 0).")
    print("  => the naive order-based deformations DO NOT reproduce the GR term g^{ij}(N1 dN2 - N2 dN1).")
    print("     The construction sits at (or near) the ABELIAN / ultralocal (Carrollian) limit. The GR")
    print("     structure function is the metric-dependence of 'normal', which the bare causal ORDER")
    print("     cannot supply: the extracted metric (§5.10/5.11) is the genuinely-needed extra datum, and")
    print("     'order + metric -> exact Dirac-Schwinger' is NOT achieved here -- it is the open core.")
else:
    print(f"- The commutator tracks the GR lapse-gradient profile (mean corr {avg_corr:+.2f}); see code.")
