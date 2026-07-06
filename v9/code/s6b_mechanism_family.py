#!/usr/bin/env python3
"""
s6b_mechanism_family.py — v9 round 7 review repairs (both referee reports,
2026-07-05): the CORRECTION-SUPPORT receipt. No branch verdicts — this
receipt turns four review-measured facts into committed-stream receipts,
per the #45 rule (mechanism/meta claims carry receipt discipline).

Replays s5's COMMITTED stream (seed 20260712; rng call order: G-O
sprinkling -> sampled_mab2(Ctrue) -> Q1 loop) with rng-neutral
instrumentation, so every number below is measured on the exact stream
that produced LEDGER #48. Stream fidelity is PROVEN by check I1.

MEASURED (pinned in note-s6's correction addendum before this run):
  M1 mechanism decomposition, loss steps only: fraction of winners LARGER
     than truth; fraction = menu-max |D|; mean Row-A gap (truth - winner);
     mean Row-C gap; fraction of steps where |Row-C gap| > |Row-A gap|;
     prefix comparability r_t at t = 64/128/192/255 (the transient the
     Row-C target ½ punishes — ½ is the 2D box order's EQUILIBRIUM value,
     reached only at completion).
  M2 the allowance-family curve ON THE SAME MENUS (paired): truth-win rate
     under dS~ = dS - c|D| at c in {0, 0.05, 0.10, 0.15, 0.20, 0.24}
     (all < the wall bound ¼); computed arithmetically from one raw
     evaluation per candidate — no re-scoring noise.
  M3 dominance: fraction of steps carrying a decoy BOTH larger than truth
     AND raw-cheaper — at such steps truth loses at EVERY c >= 0.
  M4 the per-step oracle: fraction of steps where ANY c in [0, ¼) makes
     truth the argmin (feasibility window from the exact linear
     constraints) — the most generous member of the fixed-profile family.
  M5 chance line: 14 candidates (truth + 12 kernel decoys + the empty
     set); duplicate-empty rate printed for the 1/14..1/13 bracket;
     rep-level t vs 1/14 for the committed rates (raw, arm A, arm B).

INTEGRITY CHECKS (the receipt's PASS/FAIL — exits 0 iff all hold):
  I1 the replay reproduces s5's committed G1 rate and reps EXACTLY
     (0.039; [0.021, 0.036, 0.073, 0.026]).
  I2 the family curve's c = 0 column equals the replayed rate (paired
     arithmetic consistency).
  I3 dominated steps are infeasible steps (M3 <= 1 - M4 + tie tolerance).
Precision: float64 accumulators over the float32 Gram fast-path
(decision-invariance verified by the round-7 code review).
"""
import numpy as np

rng = np.random.default_rng(20260712)          # s5's committed seed
M0 = 8
PASS = 0
FAIL = 0

def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

def delta_S0(Ct, Ctf, D):
    if not D.any(): return 0.0
    Didx = np.nonzero(D)[0]
    Mm = (Ct[Didx, :] & D[None, :]).astype(np.float32)
    k = Mm.sum(1)
    edges = ((Mm @ Ctf) * Mm).sum(1)
    r = 2.0 * edges / np.maximum(k * (k - 1), 1.0)
    charge = np.where(k >= M0, (r - 0.5) ** 2, 0.25)
    return float(charge.sum())

def s_comp(nrel, n):
    if n < 2: return 0.0
    npair = n * (n - 1) / 2.0
    r = nrel / npair
    return npair * (r - 0.5) ** 2

def sprinkling_order(n):
    pts = rng.random((n, 2))
    order = np.argsort(pts[:, 0] + pts[:, 1])
    pts = pts[order]
    C = (pts[None, :, 0] > pts[:, None, 0]) & (pts[None, :, 1] > pts[:, None, 1])
    return pts, C

def kernel_menu(Ct, t, K=12):
    cands = [np.zeros(t, dtype=bool)]
    while len(cands) < K + 1:
        p = float(np.exp(rng.uniform(np.log(min(1.0 / t, 0.59)), np.log(0.6))))
        anc = rng.random(t) < p
        D = anc | Ct[:, anc].any(axis=1) if anc.any() else anc
    	# (verbatim s5 form)
        cands.append(D)
    return cands

def sampled_mab2_consume(C, n_samp=40):
    """Replays s5's oracle-target rng consumption (choice call) exactly;
    the value itself is not used here."""
    ii, jj = np.nonzero(C)
    f = C.astype(np.float32)
    btw = np.rint(f @ f).astype(np.int32)
    ok_idx = np.nonzero((btw[ii, jj] >= M0) & (btw[ii, jj] <= 256))[0]
    if len(ok_idx) == 0: return
    rng.choice(len(ok_idx), size=min(n_samp, len(ok_idx)), replace=False)

N = 256
print("[s6b mechanism + family receipt on s5's committed stream, n = 256]")

# --- replay s5's pre-Q1 rng consumption: G-O sprinkling + oracle targets
pts0, C0 = sprinkling_order(N)
sampled_mab2_consume(C0)

C_GRID = [0.0, 0.05, 0.10, 0.15, 0.20, 0.24]
WALL = 0.25
reps_rate = []
fam_wins = np.zeros(len(C_GRID))
n_bigger = 0; n_menu_max = 0; n_loss = 0
gapA_acc = []; gapC_acc = []; n_C_dom = 0
n_dominated = 0; n_feasible = 0; n_scored = 0
dup_empty = []
r_check = {64: [], 128: [], 192: [], 255: []}

for rep in range(4):
    pts, Ctrue = sprinkling_order(N)
    truth_wins = 0; total = 0
    Cw = np.zeros((N, N), dtype=bool)
    nrel = 0
    for t in range(1, N):
        Cw[:t, t] = Ctrue[:t, t]
        if t >= 64:
            if t in r_check:
                r_check[t].append(nrel / (t * (t - 1) / 2.0))
            Ct = Cw[:t, :t]
            Ctf = Ct.astype(np.float32)
            truth = Ctrue[:t, t].copy()
            menu = kernel_menu(Ct, t)
            cands = [truth] + menu
            szs = np.array([int(D.sum()) for D in cands])
            A = np.array([delta_S0(Ct, Ctf, D) for D in cands])
            Cc = np.array([s_comp(nrel + s, t + 1) - s_comp(nrel, t) for s in szs])
            dS = A + Cc
            total += 1; n_scored += 1
            dup_empty.append(int((szs[1:] == 0).sum()) - 1)
            # I1 leg: s5's exact win condition
            if dS[0] <= dS[1:].min():
                truth_wins += 1
            else:
                w = 1 + int(np.argmin(dS[1:]))
                n_loss += 1
                if szs[w] > szs[0]: n_bigger += 1
                if szs[w] == szs[1:].max(): n_menu_max += 1
                gA = A[0] - A[w]; gC = Cc[0] - Cc[w]
                gapA_acc.append(gA); gapC_acc.append(gC)
                if abs(gC) > abs(gA): n_C_dom += 1
            # M2 family curve (paired arithmetic on the same evaluation)
            for ci, c in enumerate(C_GRID):
                dSt = dS - c * szs
                if dSt[0] <= dSt[1:].min(): fam_wins[ci] += 1
            # M3 dominance / M4 feasibility window over c in [0, WALL)
            dominated = bool(np.any((szs[1:] > szs[0]) & (dS[1:] <= dS[0])))
            if dominated: n_dominated += 1
            lo, hi = 0.0, WALL
            feas = True
            for K in range(1, len(cands)):
                dsz = szs[0] - szs[K]
                gap = dS[0] - dS[K]
                if dsz == 0:
                    if gap > 0: feas = False; break
                elif dsz > 0:
                    lo = max(lo, gap / dsz)
                else:
                    hi = min(hi, gap / dsz)
            if feas and lo <= hi and lo < WALL:
                n_feasible += 1
        nrel += int(Ctrue[:t, t].sum())
    reps_rate.append(truth_wins / total)

rate = float(np.mean(reps_rate))
print(f"      replayed G1 rate: {rate:.1%} (reps {[round(r,3) for r in reps_rate]})")
check("I1: the replay reproduces s5's COMMITTED G1 result exactly — every "
      "number below is measured on the stream that produced LEDGER #48",
      abs(rate - 0.039) < 5e-4 and
      [round(r, 3) for r in reps_rate] == [0.021, 0.036, 0.073, 0.026],
      f"rate {rate:.4f}, reps {[round(r,3) for r in reps_rate]}")

print("      M1 mechanism decomposition (loss steps only):")
print(f"        winner LARGER than truth: {n_bigger/n_loss:.1%}; "
      f"winner = menu-max |D|: {n_menu_max/n_loss:.1%}")
print(f"        Row-A gap (truth - winner): mean {np.mean(gapA_acc):+.3f} "
      f"(truth Row-A-cheaper at {np.mean(np.array(gapA_acc) < 0):.1%}); "
      f"Row-C gap: mean {np.mean(gapC_acc):+.3f}")
print(f"        |Row-C| exceeds |Row-A| at {n_C_dom/n_loss:.1%} of loss steps")
for t in sorted(r_check):
    print(f"        prefix comparability r at t = {t}: {np.mean(r_check[t]):.3f}")
print("      M2 allowance-family curve (paired, same menus):")
for ci, c in enumerate(C_GRID):
    print(f"        c = {c:.2f}: truth-win rate {fam_wins[ci]/n_scored:.1%}")
check("I2: the family curve's c = 0 column equals the replayed raw rate "
      "(paired arithmetic consistency)",
      abs(fam_wins[0] / n_scored - rate) < 1e-12,
      f"{fam_wins[0]/n_scored:.4f} vs {rate:.4f}")
print(f"      M3 dominance (a decoy larger AND raw-cheaper exists): "
      f"{n_dominated/n_scored:.1%} of steps — truth loses there at EVERY c >= 0")
print(f"      M4 per-step oracle: ANY c in [0, 0.25) rescues truth at "
      f"{n_feasible/n_scored:.1%} of steps — the family's per-step-tuned "
      f"ceiling, far below the 30% rejection line")
check("I3: dominated steps are infeasible steps (M3 <= 1 - M4)",
      n_dominated / n_scored <= 1 - n_feasible / n_scored + 1e-12,
      f"{n_dominated/n_scored:.3f} <= {1 - n_feasible/n_scored:.3f}")

print("      M5 chance line:")
mean_dup = float(np.mean(dup_empty))
print(f"        candidates per step: 14 (truth + 12 kernel + empty); "
      f"duplicate-empty draws mean {mean_dup:.2f} -> effective null in "
      f"[1/14, 1/13] = [7.1%, 7.7%]")
for name, vals in (("raw (s5)", [0.021, 0.036, 0.073, 0.026]),
                   ("arm A (s6)", [0.052, 0.047, 0.068, 0.078]),
                   ("arm B (s6, edge-fixed)", [0.021, 0.021, 0.062, 0.052])):
    v = np.array(vals)
    tstat = (v.mean() - 1 / 14) / (v.std(ddof=1) / 2)
    print(f"        {name}: mean {v.mean():.3f}, rep-level t vs 1/14 = "
          f"{tstat:+.2f} (4 reps)")

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
