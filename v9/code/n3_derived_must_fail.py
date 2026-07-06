#!/usr/bin/env python3
"""
n3_derived_must_fail.py — v9 round 16: THE MUST-FAIL LEG (note-n3-derived;
pins committed at 4206520 BEFORE this receipt existed). T6.4's outstanding
void, on the genuinely derived (web-functional) ml2 Hasse-GFF field.

Construction verbatim from ml2 (web (2048, 32, 16); chains = segments
>= 8; derived field = Hasse-mediated GFF exact cross-chain covariance;
target = the web's OWN two-clock chain positions). Six seeds 20260728-33.

PINNED (note-n3-derived SS2): Gn1 closure >= 0.70 on >= 5/6 (NON-BLIND:
ml2's known spread 0.743-0.919, disclosed); Gn2 THE MUST-FAIL — (a) the
supply-only surrogate (level outer product + birth affinity) falls below
shuffle-null + 3 sd on 6/6; (b) the supply-partialled residual field
retains >= 0.85x raw closure on >= 5/6; Gn3 the max-statistic confound
vs its own 24-permutation null 95th pct on >= 5/6 (firing seeds
adjudicated by Gn2b). T6.4: Gn1 AND Gn2 AND Gn3-or-benign => the void
DISCHARGED at rung-2 grade. Grade [DEMONSTRATED given the toy derived
field]. Float64. Exit 1 by design on refusal.
"""
import numpy as np

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

def mds_xy(AFF):
    Mn = len(AFF)
    DIS = AFF.max() - AFF
    np.fill_diagonal(DIS, 0.0)
    J = np.eye(Mn) - np.ones((Mn, Mn)) / Mn
    B = -0.5 * J @ (DIS ** 2) @ J
    ev, Vv = np.linalg.eigh(B)
    return Vv[:, -2:] * np.sqrt(np.maximum(ev[-2:], 0))

def procrustes_corr(A, Bm):
    A = A - A.mean(0); Bm = Bm - Bm.mean(0)
    U, s_, Vt = np.linalg.svd(A.T @ Bm)
    return float(np.corrcoef((A @ (U @ Vt)).ravel(), Bm.ravel())[0, 1])

def run_seed(sd):
    rng = np.random.default_rng(sd)
    N, M, L = 2048, 32, 16
    chi_acc = np.zeros(M)
    segs = {}; gen = np.zeros(M, dtype=int); birth = {}
    for m in range(M): segs[(m, 0)] = []; birth[(m, 0)] = 0
    chi = np.zeros(N)
    for t in range(N):
        c = int(rng.integers(M))
        chi_acc[c] += rng.exponential(0.109551)
        chi[t] = chi_acc[c]
        segs[(c, gen[c])].append(t)
        if rng.random() < 1.0 / L:
            v = int(rng.integers(M))
            chi_acc[v] = 0.0; gen[v] += 1
            segs[(v, gen[v])] = []; birth[(v, gen[v])] = t
    keys = [k for k, v in segs.items() if len(v) >= 8]
    chains = [segs[k] for k in keys]
    Mc = len(chains)
    b = np.arange(N)
    r1 = np.argsort(np.argsort(b)); r2 = np.argsort(np.argsort(chi))
    emb = np.column_stack([(r1 + 0.5) / N, (r2 + 0.5) / N])
    tpos = np.array([[emb[v, 0].mean(), emb[v, 1].mean()] for v in chains])
    C = (b[None, :] > b[:, None]) & (chi[None, :] > chi[:, None])
    Cf = C.astype(np.float32)
    btw = np.rint(Cf @ Cf).astype(np.int32)
    Hasse = C & (btw == 0)
    A_g = (Hasse | Hasse.T).astype(np.float64)
    Lg = np.diag(A_g.sum(1)) - A_g
    Cov = np.linalg.inv(Lg + 0.1 * np.eye(N))
    chi_AB = np.zeros((Mc, Mc))
    for i in range(Mc):
        for j in range(Mc):
            if i != j:
                chi_AB[i, j] = Cov[np.ix_(chains[i], chains[j])].mean()
    XY = mds_xy(chi_AB)
    pc = procrustes_corr(XY, tpos)
    # supply observables
    levels = np.array([chi[v].mean() for v in chains])
    births = np.array([birth[k] for k in keys], dtype=float)
    # the must-fail surrogate
    def norm01(Mx):
        lo, hi = Mx.min(), Mx.max()
        return (Mx - lo) / (hi - lo + 1e-30)
    sur = (norm01(np.outer(levels, levels))
           + norm01(np.exp(-np.abs(births[:, None] - births[None, :]) / (2048 / 4))))
    np.fill_diagonal(sur, 0.0)
    pc_sur = procrustes_corr(mds_xy(sur), tpos)
    # shuffle null (on the derived field)
    iu = np.triu_indices(Mc, 1)
    nulls = []
    for _ in range(24):
        perm = rng.permutation(len(iu[0]))
        As = np.zeros_like(chi_AB)
        As[iu] = chi_AB[iu][perm]
        As = As + As.T
        nulls.append(procrustes_corr(mds_xy(As), tpos))
    mu0, s0 = float(np.mean(nulls)), float(np.std(nulls, ddof=1))
    # Gn2b: supply-partialled residual field
    feats = np.column_stack([np.outer(levels, levels)[iu],
                             np.exp(-np.abs(births[:, None] - births[None, :])[iu] / 512),
                             np.ones(len(iu[0]))])
    coef, *_ = np.linalg.lstsq(feats, chi_AB[iu], rcond=None)
    resid = np.zeros_like(chi_AB)
    resid[iu] = chi_AB[iu] - feats @ coef
    resid = resid + resid.T
    pc_res = procrustes_corr(mds_xy(resid), tpos)
    # Gn3: max-statistic confound with its own permutation null
    def maxstat(XYm):
        return max(abs(float(np.corrcoef(XYm[:, d], q)[0, 1]))
                   for d in (0, 1) for q in (levels, births))
    ms = maxstat(XY)
    ms_null = []
    for _ in range(24):
        pr = rng.permutation(Mc)
        ms_null.append(maxstat(XY[pr]))
    ms95 = float(np.quantile(ms_null, 0.95))
    return dict(Mc=Mc, pc=pc, pc_sur=pc_sur, mu0=mu0, s0=s0,
                pc_res=pc_res, ms=ms, ms95=ms95)

rows = [run_seed(sd) for sd in range(20260728, 20260734)]
for sd, r in zip(range(20260728, 20260734), rows):
    print(f"      seed {sd}: Mc = {r['Mc']}, closure {r['pc']:.3f}, "
          f"surrogate {r['pc_sur']:.3f} vs null {r['mu0']:.3f}+-{r['s0']:.3f}, "
          f"residual {r['pc_res']:.3f} ({r['pc_res']/max(r['pc'],1e-9):.2f}x), "
          f"maxstat {r['ms']:.3f} vs 95th {r['ms95']:.3f}")

n1 = sum(1 for r in rows if r['pc'] >= 0.70)
check("Gn1 (closure, derived field; NON-BLIND band per ml2's known "
      "spread): >= 0.70 on >= 5/6 seeds", n1 >= 5,
      f"{n1}/6 (band [{min(r['pc'] for r in rows):.3f}, "
      f"{max(r['pc'] for r in rows):.3f}])")
g2a = all(r['pc_sur'] < r['mu0'] + 3 * r['s0'] for r in rows)
check("Gn2a (THE MUST-FAIL): the supply-only surrogate falls below "
      "shuffle-null + 3 sd on 6/6 seeds — the pipeline rejects "
      "bookkeeping-only fields", g2a)
n2b = sum(1 for r in rows if r['pc_res'] >= 0.85 * r['pc'])
check("Gn2b: the supply-partialled residual field retains >= 0.85x the "
      "raw closure on >= 5/6 — the geometry does not ride the supply "
      "channel", n2b >= 5, f"{n2b}/6")
n3ok = sum(1 for r in rows if r['ms'] <= r['ms95'])
fired_benign = all(r['pc_res'] >= 0.85 * r['pc'] for r in rows if r['ms'] > r['ms95'])
check("Gn3 (max-statistic confound, family-calibrated): below the "
      "permutation-null 95th on >= 5/6; firing seeds adjudicated by "
      "Gn2b (benign if residual retained)",
      n3ok >= 5 or fired_benign, f"{n3ok}/6 below; fired-benign: {fired_benign}")
t64 = (n1 >= 5) and g2a and (n2b >= 5) and (n3ok >= 5 or fired_benign)
check("T6.4 (pinned semantics): Gn1 AND Gn2(a, b) AND Gn3-or-benign — "
      "the must-fail void DISCHARGED; T6.4 fully met at rung-2 grade "
      "[DEMONSTRATED given the toy derived field]", t64)

print()
print(f"PRE-REGISTERED GATE LEDGER: "
      f"{'ALL HELD' if FAIL == 0 else 'REFUSALS PRESENT'} — Gn1; Gn2a "
      f"must-fail; Gn2b residual; Gn3 calibrated; T6.4")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
