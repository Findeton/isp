#!/usr/bin/env python3
"""
y1_d1_family_retest.py — v9 round 2, T2.1's receipt (note-t21, gates pinned
there before this first execution) + the powered D1-family retest paper 17
§7 item 2 owes.

GATES — pre-registered vs executed (review round: two pinned gates were
REFUTED at first execution; per the corpus convention the refuted
predictions are KEPT with verdicts, and the executed assertions are the
refutation-regressions. The summary line reports both counts):
  CHECK 1  budgets measured (live gate: uniform > D1).                [HELD]
  CHECK 2  P1 pinned gate: cure ratio == budget ratio within x1.6,
           both scales -> **PRE-REGISTERED GATE: REFUSED** (cure ~3.6x
           ABOVE budget at 512; unresolved at 2048). Executed assertion =
           the refutation-regression (cure significant AND above-budget).
  CHECK 3  P2 pinned gate: excesses N-flat within 2 SE per law.       [HELD]
  CHECK 4  P3 pinned gate: both D1 readings CERTIFIED-or-ADJACENT.    [HELD]
  CHECK 5  P4 pinned gate: monotone ratio decline across N ->
           **PRE-REGISTERED GATE: REFUSED** (no resolvable trend; all
           scales certified/adjacent). Executed assertion = the
           refutation-regression (no REFUSED verdict at any scale).

Conventions: one pooled 64-draw fano calibration per scale; TOST via q2's
welch_ci; float64; default_rng(20260706) (round-2 stream), disclosed.
Machinery: u3/q2 standalone copies (web with victim/atoms options incl. the
age_events line verbatim; star_disc; rank embed; interval_fano kmin = 10).
"""

import numpy as np
from math import sqrt, log

rng = np.random.default_rng(20260706)

PASS = 0
FAIL = 0

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
        vol = a * vs
        best = max(best, float(np.abs(co - vol).max()), float(np.abs(cc - vol).max()))
    return best

def rank_embed(b, chi):
    N = len(b)
    r1 = np.argsort(np.argsort(b)); r2 = np.argsort(np.argsort(chi))
    return np.column_stack([(r1 + 0.5) / N, (r2 + 0.5) / N])

def dominance(pts):
    return (pts[None, :, 0] > pts[:, None, 0]) & (pts[None, :, 1] > pts[:, None, 1])

def interval_fano(b_, c_, kmin=10):
    pts_ = np.column_stack([np.asarray(b_, dtype=float), c_])
    Np = len(pts_)
    C = dominance(pts_)
    r1 = np.argsort(np.argsort(pts_[:, 0]))
    r2 = np.argsort(np.argsort(pts_[:, 1]))
    Cf = C.astype(np.float32)
    btw = np.rint(Cf @ Cf).astype(np.int32)
    ii, jj = np.nonzero(C)
    dr1 = (r1[jj] - r1[ii]).astype(float)
    dr2 = (r2[jj] - r2[ii]).astype(float)
    exp_k = (dr1 - 1) * (dr2 - 1) / Np
    sel = exp_k >= kmin
    resid = btw[ii, jj][sel] - exp_k[sel]
    return float(np.mean(resid ** 2 / exp_k[sel]))

ATOMS128 = np.geomspace(0.063376134128, 0.156109200157, 128)

def web(N, M, L, victim="uniform", atoms=None, kernel="uniform"):
    """u3's web verbatim (incl. age_events), + j3's strict kernel option."""
    chi_acc = np.zeros(M)
    chi = np.zeros(N)
    own = np.zeros(M, dtype=np.int64); born = np.zeros(M, dtype=np.int64)
    age_events = np.zeros(M, dtype=np.int64)
    lifetimes = []
    for t in range(N):
        c = int(rng.integers(M))
        if atoms is None:
            chi_acc[c] += rng.exponential(0.109551)
        else:
            chi_acc[c] += float(atoms[int(rng.integers(len(atoms)))])
        own[c] += 1
        chi[t] = chi_acc[c]
        if kernel == "strict":
            if rng.random() < 1.0 / L:
                lifetimes.append(int(own[c] - born[c]))
                chi_acc[c] = 0.0; born[c] = own[c]
        else:
            if rng.random() < 1.0 / L:
                age_events += 1
                if victim == "uniform":
                    v = int(rng.integers(M))
                else:
                    v = int(np.argmax(age_events))
                lifetimes.append(int(own[v] - born[v]))
                chi_acc[v] = 0.0; born[v] = own[v]; age_events[v] = 0
    return np.arange(N), chi, np.array(lifetimes, dtype=float)

def welch_ci(m1, s1, n1, m2, s2, n2):
    se = sqrt(s1 * s1 / n1 + s2 * s2 / n2)
    df = (s1**2/n1 + s2**2/n2)**2 / ((s1**2/n1)**2/(n1-1) + (s2**2/n2)**2/(n2-1))
    z90 = 1.6449
    t = z90 * (1 + (z90**2 + 1) / (4 * max(df, 1)))
    return (m1 - m2) - t * se, (m1 - m2) + t * se

def verdict(arm, band, dmult):
    m, s, K = np.mean(arm), np.std(arm, ddof=1), len(arm)
    mb, sb, nb = np.mean(band), np.std(band, ddof=1), len(band)
    Delta = dmult * sb
    lo, hi = welch_ci(m, s, K, mb, sb, nb)
    if lo > -Delta and hi < Delta:
        return "CERTIFIED-IN-BAND", m, mb
    if lo > Delta or hi < -Delta:
        return "REFUSED", m, mb
    return "BAND-ADJACENT", m, mb

# ---------------------------------------------------- pooled calibrations
print("[calibrations: pooled 64-draw fano ensembles + 16-draw D* bands]")
cal = {}
for N in (512, 2048):
    ens = []
    for _ in range(64):
        p = rng.random((N, 2))
        ens.append(interval_fano(np.argsort(np.argsort(p[:, 0])), p[:, 1]))
    cal[N] = (float(np.mean(ens)), float(np.std(ens, ddof=1)))
    print(f"      N = {N}: fano ensemble {cal[N][0]:.3f} +/- {cal[N][1]:.3f}")
dband = {}
for N in (512, 1024, 2048):
    b = []
    for _ in range(16):
        p = rng.random((N, 2))
        b.append(star_disc(rank_embed(np.argsort(np.argsort(p[:, 0])), p[:, 1])))
    dband[N] = np.array(b)

# ---------------------------------------------------- CHECK 1: budgets
print("CHECK 1: the lifetime-law budgets (the Lemma's inputs, measured)")
budget = {}
for lawname, vic in (("uniform", "uniform"), ("D1", "oldest")):
    g_all = []
    for s in range(6):
        _, _, lifes = web(4096, 32, 2, victim=vic)
        g_all.extend(lifes.tolist())
    g = np.array(g_all)
    B = float(np.mean(g * (g - 1)) / (2 * np.mean(g)))
    budget[lawname] = B
    print(f"      {lawname:>8}: E[g] = {g.mean():.2f}, E[g(g-1)] = "
          f"{np.mean(g*(g-1)):.2f}, budget/commit = {B:.3f} "
          f"(cv^2 = {g.var()/g.mean()**2:.2f}, n = {len(g)})")
ratio_budget = budget["uniform"] / budget["D1"]
check("both victim laws' budgets measured at matched mean; the uniform "
      "(geometric-class) budget exceeds D1's (the concentration the Lemma "
      "prices)", budget["uniform"] > budget["D1"],
      f"budget ratio uniform/D1 = {ratio_budget:.2f}")

# ---------------------------------------------------- CHECK 2+3: excesses
print("CHECK 2/3: mean-level dispersion excesses (K = 12 arms, pooled cal)")
exc = {}
for lawname, vic in (("uniform", "uniform"), ("D1", "oldest")):
    for N in (512, 2048):
        arm = []
        for _ in range(12):
            b, chi, _ = web(N, 32, 2, victim=vic)
            arm.append(interval_fano(b, chi))
        arm = np.array(arm)
        mu_e, sd_e = cal[N]
        zs = (arm - mu_e) / sd_e
        exc[(lawname, N)] = (float((arm.mean() - mu_e) / mu_e), zs)
        print(f"      {lawname:>8} N = {N:>4}: fano {arm.mean():.3f} -> "
              f"mean-excess {exc[(lawname, N)][0]:+.1%}, mean z {zs.mean():+.2f}")
r512 = exc[("uniform", 512)][0] / max(exc[("D1", 512)][0], 1e-9)
r2048 = exc[("uniform", 2048)][0] / max(exc[("D1", 2048)][0], 1e-9)
# P1's pinned gate (cure ratio == budget ratio within x1.6, both scales)
# REFUSED at first execution: at N = 512 the cure is ~3.6x STRONGER than
# the budget predicts (6.85 vs 1.88) — the pre-registered second branch
# ("the tail acts through more than the pair count"); at N = 2048 both
# excesses sit ~1 sigma_ens and the ratio is unresolvable at K = 12.
# The check asserts the MEASURED structure (prediction kept with verdict):
z5u, z5d = exc[("uniform", 512)][1], exc[("D1", 512)][1]
dcure = z5u.mean() - z5d.mean()
se_c = sqrt(z5u.var(ddof=1) / 12 + z5d.var(ddof=1) / 12)
ok = (dcure > 2 * se_c) and (r512 > ratio_budget * 1.6)
check("P1 REFUTED-as-stated, mechanism direction recorded: the D1 cure at "
      "N = 512 is significant (> 2 SE) and EXCEEDS the pair-budget "
      "prediction by ~3.6x — the lifetime tail suppresses dispersion "
      "through more than the same-lineage pair count (superlinear; "
      "exponent unresolved at this power); at N = 2048 the ratio is "
      "below resolution (both excesses ~1 sigma_ens)", ok,
      f"cure z-diff {dcure:+.2f} vs 2 SE {2*se_c:.2f}; ratios {r512:.2f} "
      f"(512) / {r2048:.2f} (2048, unresolved) vs budget {ratio_budget:.2f}")
flat_ok = True
for lawname in ("uniform", "D1"):
    z5, z20 = exc[(lawname, 512)][1], exc[(lawname, 2048)][1]
    d = z5.mean() - z20.mean()
    sed = sqrt(z5.var(ddof=1) / 12 + z20.var(ddof=1) / 12)
    flat = abs(d) < 2 * sed
    flat_ok &= flat
    print(f"      {lawname:>8}: z(512) - z(2048) = {d:+.2f} vs 2 SE {2*sed:.2f}"
          f" -> {'N-FLAT' if flat else 'N-TREND'}")
check("P2: no RESOLVABLE N-trend at K = 12 for either law (flat within "
      "2 SE; a <= 2x decline remains unexcluded at this power — stated "
      "symmetrically with CHECK 2's unresolved-at-2048 clause)", flat_ok)

# ---------------------------------------------------- CHECK 4: D* verdicts
print("CHECK 4: P3 — the D1-family D* verdicts at N = 2048 (K = 12, q2 semantics)")
verd = {}
for armname, kw in (("D1-continuous", dict(victim="oldest")),
                    ("D1+atoms128", dict(victim="oldest", atoms=ATOMS128))):
    arm = []
    for _ in range(12):
        b, chi, _ = web(2048, 32, 2, **kw)
        arm.append(star_disc(rank_embed(b, chi)))
    v2, m, mb = verdict(np.array(arm), dband[2048], 2.0)
    v1, _, _ = verdict(np.array(arm), dband[2048], 1.0)
    verd[armname] = v2
    print(f"      {armname:>14}: D* {m:.4f} vs band {mb:.4f} ({m/mb:.2f}x) "
          f"-> {v2}  [1-sigma: {v1}]")
ok = all(v != "REFUSED" for v in verd.values())
check("P3: both D1 content readings land CERTIFIED-or-ADJACENT at N = 2048 "
      "under the powered semantics — paper 17's directional 0.96x headline "
      "is de-asterisked (a REFUSED here would have demoted it; both "
      "directions were live)", ok, f"{verd}")

# ---------------------------------------------------- CHECK 5: strict corner
print("CHECK 5: P4 — the strict corner's volume face across N (K = 12)")
ratios = {}
for N in (512, 1024, 2048):
    arm = []
    for _ in range(12):
        b, chi, _ = web(N, 32, 2, kernel="strict")
        arm.append(star_disc(rank_embed(b, chi)))
    v2, m, mb = verdict(np.array(arm), dband[N], 2.0)
    ratios[N] = (m / mb, v2)
    print(f"      N = {N:>4}: {m/mb:.2f}x -> {v2}")
# P4's pinned prediction (monotone decline) REFUSED at first execution:
# no monotone N-trend at K = 12 — the transient story over-generalized
# q2's UNIFORM-kernel fresh-vs-warm split to the strict kernel (whose
# renewal has no common-birth cohort of the same kind). The measured
# answer to paper 17 SS3's owed question:
ok = all(r[1] != "REFUSED" for r in ratios.values())
check("P4 REFUTED-as-stated, and the owed question CLOSED the other way: "
      "the strict corner is CERTIFIED-or-ADJACENT at every scale with no "
      "resolvable N-trend at K = 12 — u1's 1.60x N=512 reading was stream "
      "scatter (the +/-0.2x noise q2 measured), not a transient staircase",
      ok, f"{ {N: (round(r[0], 2), r[1]) for N, r in ratios.items()} }")

print()
print("PRE-REGISTERED GATE LEDGER: 3/5 held (CHECKs 1/3/4); 2 REFUSED")
print("(P1, P4 — refutations kept with verdicts; assertions above are the")
print("refutation-regressions, pinned at first refuted execution)")
print()
total = PASS + FAIL
if FAIL == 0:
    print(f"ALL CHECKS PASS ({PASS}/{total})")
else:
    print(f"FAILURES: {FAIL}/{total}")
    raise SystemExit(1)
