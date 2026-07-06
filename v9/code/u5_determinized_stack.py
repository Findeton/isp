#!/usr/bin/env python3
"""
u5_determinized_stack.py — v9 round 3: G2-strict's first real test (the
memo's queue item 3, run AFTER the theorem per note 8 §2's directive, with
note-t31's redesigned gate pair and its stated boundary).

THE STACK (fully determinized, w = 0): periodic churn events (every L-th
commit), deterministic 3-atom content cycling, D1 kill-the-oldest victim,
D2 round-robin committer. Zero randomness anywhere.

PRE-REGISTERED (both directions live; note-t31's legs predict the first
three, G2-strict predicts the fourth):
  P1 the per-lineage inter-commit content-gap marginal fails KS vs Exp(1)
     at-or-above the finite-alphabet floor (leg ii; support size counted).
  P2 the two-time gate flags the deterministic cycling (gap-autonomous
     class — within the battery's stated boundary).
  P3 the WEB's volume layer: D* vs the same-N band (verdict recorded).
  P4 G2-STRICT'S FACE: the web's dispersion layer REFUSES (fano z >> 3 vs
     a 64-draw sprinkling ensemble) — full determinism => statistically
     dead web (the lattice precedent). A PASS here would REFUTE G2-strict.
Boundary disclosure (note-t31 §4): these gates decide THIS named stack,
not the zero-randomness class. Seed 20260707 (calibrations only — the
stack itself is deterministic); float64.
"""
import numpy as np
from math import sqrt

rng = np.random.default_rng(20260707)
PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

def star_disc(pts):
    N = len(pts)
    us = np.unique(np.concatenate([pts[:, 0], [1.0]]))
    vs = np.unique(np.concatenate([pts[:, 1], [1.0]]))
    order = np.argsort(pts[:, 0], kind="stable")
    pu = pts[order, 0]; pv = pts[order, 1]
    best = 0.0
    for a in us:
        ko = np.searchsorted(pu, a, "left"); kc = np.searchsorted(pu, a, "right")
        so = np.sort(pv[:ko]); sc = np.sort(pv[:kc])
        co = np.searchsorted(so, vs, "left") / N
        cc = np.searchsorted(sc, vs, "right") / N
        best = max(best, float(np.abs(co - a * vs).max()), float(np.abs(cc - a * vs).max()))
    return best

def canon_embed_pts(b, chi):
    N = len(b)
    r1 = np.argsort(np.argsort(b)).astype(int)
    order2 = np.lexsort((-np.asarray(b, dtype=float), chi))
    r2 = np.empty(N, dtype=int); r2[order2] = np.arange(N)
    return np.column_stack([(r1 + 0.5) / N, (r2 + 0.5) / N])

def interval_fano(b_, c_, kmin=10):
    pts_ = np.column_stack([np.asarray(b_, dtype=float), c_])
    Np = len(pts_)
    C = (pts_[None, :, 0] > pts_[:, None, 0]) & (pts_[None, :, 1] > pts_[:, None, 1])
    r1 = np.argsort(np.argsort(pts_[:, 0])); r2 = np.argsort(np.argsort(pts_[:, 1]))
    Cf = C.astype(np.float32)
    btw = np.rint(Cf @ Cf).astype(np.int32)
    ii, jj = np.nonzero(C)
    exp_k = ((r1[jj] - r1[ii]).astype(float) - 1) * ((r2[jj] - r2[ii]).astype(float) - 1) / Np
    sel = exp_k >= kmin
    resid = btw[ii, jj][sel] - exp_k[sel]
    return float(np.mean(resid ** 2 / exp_k[sel]))

ATOMS = [0.156109200157, 0.109004107833, 0.063376134128]
N, M, L = 2048, 32, 2

# ---- the determinized stack
chi_acc = np.zeros(M); chi = np.zeros(N)
age = np.zeros(M, dtype=int); own = np.zeros(M, dtype=int); born = np.zeros(M, dtype=int)
gaps_content = {m: [] for m in range(M)}
last_chi = {m: 0.0 for m in range(M)}
atom_idx = 0
for t in range(N):
    c = t % M                              # D2 round-robin
    chi_acc[c] += ATOMS[atom_idx]          # deterministic content cycling
    atom_idx = (atom_idx + 1) % 3
    own[c] += 1
    chi[t] = chi_acc[c]
    gaps_content[c].append(chi_acc[c] - last_chi[c])
    last_chi[c] = chi_acc[c]
    if (t + 1) % L == 0:                   # periodic churn event
        age += 1
        v = int(np.argmax(age))            # D1 kill-the-oldest
        chi_acc[v] = 0.0; born[v] = own[v]; age[v] = 0
        last_chi[v] = 0.0

g = np.array([x for m in range(M) for x in gaps_content[m]])
g = g / g.mean()                           # unit-mean normalization (scale-free)

print("P1: the content-gap marginal vs Exp(1)")
supp = len(np.unique(np.round(g, 12)))
gs = np.sort(g)
F = 1.0 - np.exp(-gs)
n_ = len(gs)
ks = max(np.max(np.abs(F - np.arange(1, n_ + 1) / n_)), np.max(np.abs(F - np.arange(n_) / n_)))
floor = 1.0 / (2 * supp)
check("marginal KS at-or-above the finite-alphabet floor (leg ii): full "
      "determinism yields a finitely-supported gap law", ks >= floor - 0.01,
      f"KS = {ks:.3f}, support = {supp}, floor = {floor:.4f}")

print("P2: the two-time gate (the serial-rank half; note-t31's binned pair-chi2")
print("    half omitted here — disclosed; rho fires decisively alone)")
a, b2 = g[:-1], g[1:]
ra = np.argsort(np.argsort(a)); rb = np.argsort(np.argsort(b2))
rho = float(np.corrcoef(ra, rb)[0, 1])
check("serial structure flags the deterministic cycling (|rho| > 0.2 — "
      "gap-autonomous class, inside the battery's stated boundary)",
      abs(rho) > 0.2, f"serial rho = {rho:+.3f}")

print("P3/P4: the web's layers (vs 16-draw D* band / 64-draw fano ensemble)")
emb = canon_embed_pts(np.arange(N), chi)
d_web = star_disc(emb)
band = [star_disc(canon_embed_pts(np.argsort(np.argsort(p[:, 0])), p[:, 1]))
        for p in (rng.random((N, 2)) for _ in range(16))]
mb, sb = float(np.mean(band)), float(np.std(band, ddof=1))
ens = [interval_fano(np.argsort(np.argsort(p[:, 0])), p[:, 1])
       for p in (rng.random((N, 2)) for _ in range(64))]
mu_e, sd_e = float(np.mean(ens)), float(np.std(ens, ddof=1))
f_web = interval_fano(np.arange(N), chi)
z_disp = (f_web - mu_e) / sd_e
print(f"      D* = {d_web:.4f} vs band {mb:.4f} +/- {sb:.4f} ({d_web/mb:.2f}x); "
      f"fano = {f_web:.3f} vs {mu_e:.3f} +/- {sd_e:.3f} (z = {z_disp:+.1f})")
print(f"  [INFO] volume-layer verdict recorded (print-not-count per "
      f"#36/#45): {d_web/mb:.2f}x band")
check("G2-STRICT's first real test: the dispersion layer REFUSES at z >> 3 "
      "— the fully determinized stack's web is statistically dead (a pass "
      "would have REFUTED G2-strict; both directions were live)",
      abs(z_disp) > 3, f"z = {z_disp:+.1f}")

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
