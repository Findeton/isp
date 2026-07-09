#!/usr/bin/env python3
"""
dimwall_finder.py — v9 round 32: THE FIRST RECONSTRUCTION ON A GROWN WEB
(note-3p1-p3; pin committed at a8d4023 strictly before this receipt.
NO-REVIEW MODE.)  Order-only 2+1 pipeline: t-hat = |past|^(1/3) -
|future|^(1/3); transverse = 2-comp MDS on past-overlap dissimilarity;
certificate = cone-fit balanced accuracy (rho fit in-sample, identical
per family).  Gates: Gp1 M3 control >= 0.85; Gp2 the chi-permuted null
>= 0.10 below the web (else VOID); Gp3 the measurement [directional:
null + 0.10 <= web <= M3; >= M3 - 0.03 flags MANIFOLDLIKE-GRADE].
Exit 1 by design on refusal.
"""
import numpy as np

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

def sprinkle_mink(rng, N, dspace):
    T = np.empty(0); X = np.empty((0, dspace))
    while len(T) < N:
        t = rng.random(6 * N)
        x = rng.uniform(-0.5, 0.5, (6 * N, dspace))
        r = np.linalg.norm(x, axis=1)
        keep = (r <= t) & (r <= 1 - t)
        T = np.concatenate([T, t[keep]]); X = np.vstack([X, x[keep]])
    T = T[:N]; X = X[:N]
    dt = T[None, :] - T[:, None]
    dx = np.linalg.norm(X[None, :, :] - X[:, None, :], axis=2)
    rel = (dt > 0) & (dt >= dx)
    np.fill_diagonal(rel, False)
    return rel

def web_window(sd, C=2, N=2048, M=32, L=16, alpha=0.75, D=512, NW=128):
    rng = np.random.default_rng(sd)
    acc = np.zeros((M, C))
    pref = np.arange(M) % C
    chiV = np.zeros((N, C))
    for t in range(N):
        c = int(rng.integers(M))
        if rng.random() < alpha:
            k = int(pref[c])
        else:
            k = int(rng.integers(C))
        acc[c, k] += rng.exponential(0.109551)
        chiV[t] = acc[c]
        for kk in range(C):
            if rng.random() < 1.0 / L:
                acc[int(rng.integers(M)), kk] = 0.0
    start = (N - D) // 2
    idx = np.sort(rng.choice(np.arange(start, start + D), NW, replace=False))
    b = idx
    rel = b[:, None] < b[None, :]
    for k in range(C):
        rel &= chiV[idx][:, None, k] <= chiV[idx][None, :, k]
    np.fill_diagonal(rel, False)
    return rel, chiV[idx], idx

def permuted_null(rel_src_web):
    """chi-permuted null: rebuild the window order with each channel
    column independently permuted across events (b kept)."""
    rel, chiW, idx = rel_src_web
    rng = np.random.default_rng(int(idx[0]) * 7 + 13)
    chiP = chiW.copy()
    for k in range(chiP.shape[1]):
        chiP[:, k] = rng.permutation(chiP[:, k])
    b = idx
    r2 = b[:, None] < b[None, :]
    for k in range(chiP.shape[1]):
        r2 &= chiP[:, None, k] <= chiP[None, :, k]
    np.fill_diagonal(r2, False)
    return r2

def reconstruct_score(rel):
    """The order-only pipeline + the cone-fit balanced accuracy."""
    n = rel.shape[0]
    past = rel.sum(0).astype(float)     # |past(x)| = column sums
    fut = rel.sum(1).astype(float)
    that = past ** (1 / 3) - fut ** (1 / 3)
    # past-overlap dissimilarity
    R = rel.astype(float)
    ov = R.T @ R                        # |past_i ∩ past_j|
    denom = np.sqrt(np.outer(past, past))
    S = np.where(denom > 0, ov / np.maximum(denom, 1e-12), 0.0)
    Dm = 1.0 - np.clip(S, 0, 1)
    np.fill_diagonal(Dm, 0.0)
    # classical MDS, 2 components
    J = np.eye(n) - np.ones((n, n)) / n
    B = -0.5 * J @ (Dm ** 2) @ J
    ev, V = np.linalg.eigh(B)
    XY = V[:, -2:] * np.sqrt(np.maximum(ev[-2:], 0))
    # cone fit: related iff dt > rho * r
    dt = that[None, :] - that[:, None]
    r = np.linalg.norm(XY[None, :, :] - XY[:, None, :], axis=2)
    iu = np.triu_indices(n, 1)
    rel_sym = rel | rel.T
    y = rel_sym[iu]
    # candidate rho grid from data quantiles
    with np.errstate(divide="ignore", invalid="ignore"):
        ratio = np.abs(dt[iu]) / np.maximum(r[iu], 1e-12)
    best = (0.5, 0.0)
    for q in np.quantile(ratio, np.linspace(0.05, 0.95, 19)):
        pred = np.abs(dt[iu]) > q * r[iu]
        tp = (pred & y).sum() / max(y.sum(), 1)
        tn = (~pred & ~y).sum() / max((~y).sum(), 1)
        bal = 0.5 * (tp + tn)
        if bal > best[0]:
            best = (bal, q)
    tb = float(np.corrcoef(that, np.arange(n))[0, 1])
    return best[0], best[1], tb

print("[dimwall finder: the first reconstruction on a grown web]")
SEEDS = list(range(20261200, 20261205))

m3 = []
for sd in SEEDS:
    r = np.random.default_rng(sd)
    acc, rho, tb = reconstruct_score(sprinkle_mink(r, 128, 2))
    m3.append(acc)
print("      M3 controls: " + "  ".join(f"{a:.3f}" for a in m3))
check("Gp1 (positive control): M3 mean balanced accuracy >= 0.85",
      float(np.mean(m3)) >= 0.85, f"mean {np.mean(m3):.3f}")

webs, nulls, tbs = [], [], []
for sd in SEEDS:
    pack = web_window(sd)
    acc, rho, tb = reconstruct_score(pack[0])
    webs.append(acc); tbs.append(tb)
    accN, _, _ = reconstruct_score(permuted_null(pack))
    nulls.append(accN)
print("      C = 2 webs:  " + "  ".join(f"{a:.3f}" for a in webs))
print("      chi-nulls:   " + "  ".join(f"{a:.3f}" for a in nulls))
wm, nm, mm = float(np.mean(webs)), float(np.mean(nulls)), float(np.mean(m3))
check("Gp2 (discrimination): the null sits >= 0.10 below the web",
      wm - nm >= 0.10, f"web {wm:.3f} vs null {nm:.3f} (gap {wm-nm:.3f})")
flag = wm >= mm - 0.03
check("Gp3 (THE MEASUREMENT) [directional]: null + 0.10 <= web <= M3",
      nm + 0.10 <= wm <= mm,
      f"web {wm:.3f} in [{nm+0.10:.3f}, {mm:.3f}]"
      + ("; >= M3 - 0.03 => MANIFOLDLIKE-GRADE FLAG" if flag else ""))
print(f"      INFO: t-hat/b rank correlation {np.mean(tbs):+.3f}; "
      f"score gap to M3 = {mm - wm:+.3f} (the measured manifoldlikeness "
      f"deficit of grown C = 2 webs)")

verdict = ("MANIFOLDLIKE-GRADE FLAG" if flag and FAIL == 0 else
           "RECONSTRUCTION-SCORED (sub-sprinkling, as registered)" if FAIL == 0
           else "SEE REFUSALS")
print(f"      VERDICT: {verdict}")
print()
print(f"PRE-REGISTERED GATE LEDGER: "
      f"{'ALL HELD' if FAIL == 0 else 'REFUSALS PRESENT'} — Gp1 control; "
      f"Gp2 discrimination; Gp3 measurement; verdict: {verdict}")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
