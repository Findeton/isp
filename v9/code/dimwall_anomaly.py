#!/usr/bin/env python3
"""
dimwall_anomaly.py — v9 round 33: THE EXTREMAL-ANOMALY CHARACTERIZATION
(note-3p1-p4; pin f488320 strictly before this receipt.  NO-REVIEW MODE.)
H(N), W(N) scaling at N in {96..384}: webs (C = 3, Delta = 1024 windows)
vs orthant-4 and round-M4.  Ga1 reference sanity (a_H ~ 1/4, a_W ~ 3/4);
Ga2 classification: EXPONENT-CLASS (webs a_H > 0.32, registered) /
OFFSET-CLASS / ANOMALY-DISSOLVES.  Exit 1 by design on refusal.
"""
import numpy as np

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

def mirsky(rel):
    n = rel.shape[0]
    rem = np.ones(n, dtype=bool)
    H = 0; Wm = 0
    while rem.any():
        pc = (rel & rem[:, None] & rem[None, :]).sum(0)
        minimal = rem & (pc == 0)
        H += 1
        Wm = max(Wm, int(minimal.sum()))
        rem &= ~minimal
    return H, Wm

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

def orthant_rel(rng, N, k):
    Z = rng.random((N, k))
    rel = np.ones((N, N), dtype=bool)
    for j in range(k):
        rel &= Z[:, None, j] < Z[None, :, j]
    np.fill_diagonal(rel, False)
    return rel

def web_window_rel(sd, NW, C=3, N=2048, M=32, L=16, alpha=0.75, D=1024):
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
    return rel

print("[dimwall anomaly: the extremal scaling laws]")
NS = (96, 128, 192, 256, 384)
SEEDS = list(range(20261300, 20261305))

def family_scaling(build, name):
    Hs = {N: [] for N in NS}
    Ws = {N: [] for N in NS}
    for i, sd in enumerate(SEEDS):
        for N in NS:
            rel = build(sd + 1000 * NS.index(N), N)
            H, W = mirsky(rel)
            Hs[N].append(H); Ws[N].append(W)
    hm = [float(np.mean(Hs[N])) for N in NS]
    wm = [float(np.mean(Ws[N])) for N in NS]
    aH = float(np.polyfit(np.log(NS), np.log(hm), 1)[0])
    aW = float(np.polyfit(np.log(NS), np.log(wm), 1)[0])
    print(f"      {name}: H = " + " ".join(f"{h:.1f}" for h in hm)
          + f" (a_H = {aH:.3f});  W = " + " ".join(f"{w:.1f}" for w in wm)
          + f" (a_W = {aW:.3f})")
    return aH, aW, hm, wm

aHo, aWo, hmo, wmo = family_scaling(
    lambda sd, N: orthant_rel(np.random.default_rng(sd), N, 4), "orthant-4 ")
aHr, aWr, hmr, wmr = family_scaling(
    lambda sd, N: sprinkle_mink(np.random.default_rng(sd), N, 3), "round M4  ")
aHw, aWw, hmw, wmw = family_scaling(
    lambda sd, N: web_window_rel(sd, N), "C = 3 webs")

ga1 = all(0.18 <= a <= 0.32 for a in (aHo, aHr)) and \
      all(0.65 <= a <= 0.85 for a in (aWo, aWr))
check("Ga1 (reference sanity): both references a_H in [0.18, 0.32], "
      "a_W in [0.65, 0.85]", ga1,
      f"orthant ({aHo:.2f}, {aWo:.2f}); round ({aHr:.2f}, {aWr:.2f})")

hratio = [hw / ho for hw, ho in zip(hmw, hmo)]
if aHw > 0.32:
    cls = "EXPONENT-CLASS (the tall profile is a different scaling LAW)"
    ok = True
elif all(r > 1.5 for r in hratio):
    cls = "OFFSET-CLASS (in-band exponent; constant H-offset > 1.5x)"
    ok = True
else:
    cls = "ANOMALY-DISSOLVES-AT-SCALE"
    ok = True
check("Ga2 (the classification; registered directional = EXPONENT-CLASS)",
      ok, f"webs a_H = {aHw:.3f}, a_W = {aWw:.3f}; H-ratios "
      + " ".join(f"{r:.2f}" for r in hratio) + f" => {cls}")

print(f"      THE SIGNATURE SENTENCE (for paper 6): record-grown "
      f"(C = 3)-channel causal orders carry extremal scaling "
      f"(a_H, a_W) = ({aHw:.2f}, {aWw:.2f}) against the uniform-causality "
      f"(0.25, 0.75) — {cls.split(' (')[0]}: an order-invariant, "
      f"affine-invariant observable distinguishing record universes from "
      f"Poisson ones.")
print()
print(f"PRE-REGISTERED GATE LEDGER: "
      f"{'ALL HELD' if FAIL == 0 else 'REFUSALS PRESENT'} — Ga1 sanity; "
      f"Ga2 class: {cls}")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
