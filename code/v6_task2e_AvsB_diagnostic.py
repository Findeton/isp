"""
v6 Task 2e: A-vs-B diagnostic for the bracket-closure negative (§5.12).

Question: is the Carrollian (zero) commutator because the naive rule is STRUCTURALLY blind to the GR term
(A: no signal at any resolution), or because the GR term g^{ij}(N1 dN2 - N2 dN1) is real but SUBLEADING and
noise-swamped (B: signal/noise ~ sqrt(N), emerges with resolution)?

Method: hold the PHYSICAL deformation fixed (band scale s ∝ N, so the band keeps a fixed physical thickness
as density rises) and increase N, averaging over realizations. Signal metric = ENRICHMENT:
    enrichment = < |xi| over commutator events >  /  < |xi| over all deformation-touched events >,
where xi(x) = N1 dN2 - N2 dN1 is the GR-predicted shift profile (flat g^{xx}=1). If the commutator is GR
shift, it concentrates where |xi| is large -> enrichment > 1, rising with N (B). If it is boundary noise,
enrichment ~ 1, flat (A). Also report the histogram correlation as a cross-check.
"""
import numpy as np
rng = np.random.default_rng(1)

def sprinkle(N, Tt, X): return np.column_stack([rng.uniform(-Tt, Tt, N), rng.uniform(-X, X, N)])
def order_matrix(P):
    t, x = P[:, 0], P[:, 1]; N = len(P); R = np.zeros((N, N), dtype=np.float32)
    for i in range(N):
        dt = t - t[i]; R[i] = ((dt > 0) & (dt > np.abs(x - x[i]))).astype(np.float32)
    return R
def deform(D, R, x, lapse_fn, s):
    notD = (~D).astype(np.float32); ha = R.T @ notD
    return D | ((~D) & (ha < lapse_fn(x) * s))

k = 1.3
N1 = lambda xx: 1.0 + 0.6*np.cos(k*xx)
N2 = lambda xx: 1.0 + 0.6*np.sin(k*xx)
def grad(f, xx, h=1e-3): return (f(xx+h)-f(xx-h))/(2*h)
xi = lambda xx: N1(xx)*grad(N2, xx) - N2(xx)*grad(N1, xx)

def commutator(D0, R, x, s):
    Da = deform(deform(D0, R, x, N1, s), R, x, N2, s)
    Db = deform(deform(D0, R, x, N2, s), R, x, N1, s)
    touched = (Da | Db) & (~D0)
    return (Da ^ Db), touched

N0, s0 = 3000, 6.0
print("="*82)
print("Task 2e: A (structural blindness) vs B (subleading, noise-swamped)?  band scale s ∝ N")
print("="*82)
print(f"{'N':>6} | {'reals':>5} | {'comm/real':>9} | {'enrichment <|xi|>_c/<|xi|>_touch':>32} | {'hist corr':>9}")
trend = []
for N in [1500, 3000, 6000, 10000]:
    s = s0 * (N / N0)
    reals = max(6, int(60000 / N))            # more realizations at small N for statistics
    xc_all, xt_all, ctrl_tot, ncomm = [], [], 0, []
    for _ in range(reals):
        P = sprinkle(N, 3.0, 3.0); R = order_matrix(P); x = P[:, 1]
        D0 = P[:, 0] < 0.0
        # control N1=N2 must commute exactly
        Dca = deform(deform(D0, R, x, N1, s), R, x, N1, s)
        Dcb = deform(deform(D0, R, x, N1, s), R, x, N1, s)
        ctrl_tot += int((Dca ^ Dcb).sum())
        d, touched = commutator(D0, R, x, s)
        ncomm.append(int(d.sum()))
        xc_all.append(x[d]); xt_all.append(x[touched])
    xc = np.concatenate(xc_all); xt = np.concatenate(xt_all)
    enr = np.mean(np.abs(xi(xc))) / np.mean(np.abs(xi(xt))) if len(xc) else np.nan
    # histogram correlation
    bins = np.linspace(-3, 3, 25); ctr = 0.5*(bins[:-1]+bins[1:])
    hc, _ = np.histogram(xc, bins=bins); ht, _ = np.histogram(xt, bins=bins)
    dens = hc / np.maximum(ht, 1)             # commutator fraction per spatial bin
    pred = np.abs(xi(ctr))
    corr = np.corrcoef(dens, pred)[0, 1] if len(xc) > 20 else np.nan
    trend.append((N, enr, corr))
    print(f"{N:>6} | {reals:>5} | {np.mean(ncomm):>9.1f} | {enr:>32.3f} | {corr:>+9.3f}   (ctrl={ctrl_tot})")

print("\n" + "="*82)
print("VERDICT (Task 2e)")
print("="*82)
enrs = np.array([t[1] for t in trend]); corrs = np.array([t[2] for t in trend])
rising = (enrs[-1] - enrs[0] > 0.15) and (enrs[-1] > 1.10)
corr_rising = np.nanmax(corrs) > 0.35 and (np.nan_to_num(corrs[-1]) > np.nan_to_num(corrs[0]))
if rising or corr_rising:
    print("- (B) SUBLEADING-BUT-PRESENT: enrichment/correlation RISE with N -> the GR term g^{ij}(N1 dN2-N2 dN1)")
    print("  is there, just noise-swamped at low resolution. Path: keep scaling + the contact-term extraction;")
    print("  the directional information is implicitly captured and sharpens with N.")
else:
    print("- (A) STRUCTURAL BLINDNESS: enrichment ~ 1 and correlation ~ 0 at ALL N (no rising trend) -> the")
    print("  naive order-based rule produces only boundary NOISE, with NO GR-shift signal at any resolution.")
    print("  The naive deformation is directionally metric-blind; the c->0 (Carrollian) limit is genuine for it.")
    print("  Path: it CANNOT be fixed by scaling -- needs a directional construction (unit normal from local")
    print("  order+counts) OR a no-go theorem that k-local order+count deformations can't make the dz contact")
    print("  term. This is the honest fork the diagnostic was built to resolve.")
print(f"\n  enrichment trend: {np.array2string(enrs, precision=2)}   hist-corr trend: {np.array2string(corrs, precision=2)}")
