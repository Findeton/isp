#!/usr/bin/env python3
"""
j3_decorrelation_mechanisms.py — design note 3 phase 1: the record-native
supply process (derived, not swept) against the manifoldlike cell.

THE DERIVATION UNDER TEST (design note 3, pre-registered before this ran):
paper 1's own law decomposes supply into three factors —
  F1 commit axis: evidence clock I ~ Exp(1) with rate FIXED at lambda = 1
     (self-accounting; v6 paper 4 §71 Poisson r = 1) => homogeneous race,
     uniform committer on the live fleet (one independence posit, named);
  F2 increments: deterministic per mode (Var[content|mode] = 0); the computed
     admissible menu (p2b/p2c; C(eta) = eta*tanh(eta) - log cosh(eta)):
     1-char C = 0.156109200157, 3-char C = 0.109004107833, 7-char
     C = 0.063376134128 — THREE ATOMS (values at the TRUE roots; the first
     draft used C at paper 1's ROUNDED 7-char root 0.3680, giving 0.063388 —
     a 2e-4 transcription slip corrected at j4, no verdict impact; the 3-char
     value likewise sharpened at the full-precision root); carrier open (fork);
  F3 lineages: the odometer is per-chain BY DEFINITION, so lineage birth on a
     branching web is a chi-RESET; mean lifetime L (own-commits) is the single
     new physical quantity (unpinned); the inherit reading is the pre-registered
     refutation fork.

RE-ANALYSIS THIS TESTS (note 3 §2): j1's family A already had the derived
commit axis + exchangeable increments and failed 6.2x => the obstruction was
never increment statistics; layer O1 = common-birth co-growth (all odometers
born at b = 0, chi = 0). Churn + reset is the derived cure. Design note 2's
"exchangeable ceiling" was family A in disguise — corrected in note 3 §4.

INSTRUMENT CORRECTION (disclosed, exploration round 2): the first-draft
exploration broke exact chi ties with random jitter — that injects a fresh
uniform coordinate precisely where the deterministic-content model has none
(it scored the 3-atom corner 1.04x: an artifact, retracted). Honest treatment:
the CANONICAL realizer of the two-clock order — L1 = b-order, L2 = (chi asc,
b desc); ties embed as ANTIDIAGONALS (paper 12's relabeling lemma gives this
as the canonical point set). All atomic arms below use it; continuum arms have
measure-zero ties and reduce to the plain rank embedding.

Gates pinned from the disclosed two-round exploration (3-seed landscapes);
this receipt runs 6 seeds per arm. Conventions: paper 13's (N = 512 base,
M = 32, pooled 20-replicate faithful band, j1's interval-dispersion layer);
N in {512, 1024, 2048} for the scale trend with per-N bands/ensembles. T3
calibration disclosure: the headline verdicts use a 40-draw ensemble at
N = 2048 (early 6- and 16-draw calibrations made the per-draw z flip 1.3 <->
4.1 on the ensemble-sd draw alone). T3's convention is j1's PER-DRAW z (a
configuration's statistic vs the ensemble spread: natural families fail it at
z = 12, the atomic model at z ~ 360-450 stream-dependent, the churn corner
passes at z ~ 1); the
receipt ALSO prints the finer mean-level comparison the corpus has not used
before — the corner carries a small N-stable mean excess (~ +20%, z_mean ~
2.5, attributed to the L = 2 same-lineage pair staircase) — disclosed as the
named residual, not folded into the gate.
Float64 measurement landscape; default_rng(20260702). Synthetic mode menus
for the richness ladder are geomspace over the corpus atom range [DISCLOSED
synthetic — the corpus's own extension of the menu is the dilution chain,
whose further roots are not computed here].

T1 = |Spearman(b, chi)| < 0.1 (tie-aware average ranks)
T2 = D* within band + 2 sd (canonical embedding)
T3 = interval-dispersion within z < 3 of the same-N sprinkling ensemble
"""

import numpy as np

rng = np.random.default_rng(20260702)

PASS = 0
FAIL = 0

def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))


# ------------------------------------------------------------- instruments
ATOMS = np.array([0.156109200157240, 0.109004107833, 0.063376134128])

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

def rank_embed2(b, chi):
    N = len(b)
    r1 = np.argsort(np.argsort(b))
    r2 = np.argsort(np.argsort(chi))
    return np.column_stack([(r1 + 0.5) / N, (r2 + 0.5) / N])

def canon_embed(b, chi):
    # canonical realizer of the two-clock order: L1 = b, L2 = (chi asc, b desc);
    # exact chi-tie classes embed antidiagonally (the relabeling-lemma point set)
    N = len(b)
    r1 = np.argsort(np.argsort(b))
    order2 = np.lexsort((-b, chi))
    r2 = np.empty(N, dtype=float); r2[order2] = np.arange(N)
    return np.column_stack([(r1 + 0.5) / N, (r2 + 0.5) / N])

def spearman_ties(x, y):
    def avg_rank(v):
        o = np.argsort(v, kind="stable"); r = np.empty(len(v)); r[o] = np.arange(len(v))
        vals, inv = np.unique(v, return_inverse=True)
        sums = np.bincount(inv, weights=r); cnts = np.bincount(inv)
        return (sums / cnts)[inv]
    rx, ry = avg_rank(x), avg_rank(y)
    return float(np.corrcoef(rx, ry)[0, 1])

def dominance_order(pts):
    return (pts[None, :, 0] > pts[:, None, 0]) & (pts[None, :, 1] > pts[:, None, 1])

def interval_fano(b_, c_, kmin=10):
    pts_ = np.column_stack([np.asarray(b_, dtype=float), c_])
    Np = len(pts_)
    C = dominance_order(pts_)
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

# --------------------------------------------------------------- generators
def two_clock_j1(N, M, family):
    # j1's generator verbatim (anchors A/B for continuity)
    chain = rng.integers(0, M, N)
    chi = np.zeros(N); acc = np.zeros(M)
    logr = np.zeros(M) if family == "A" else np.log(10 ** rng.uniform(-1, 1, M))
    for t in range(N):
        c = chain[t]
        acc[c] += rng.exponential(np.exp(logr[c]))
        chi[t] = acc[c]
    return np.arange(N), chi

def web(N, M, L, inc, carrier, birth, atoms_arr=None):
    # the derived web-churn supply W(L, inc, carrier, birth) of design note 3 §3
    atoms_arr = ATOMS if atoms_arr is None else atoms_arr
    mean_c = float(np.mean(atoms_arr))
    chi_acc = np.zeros(M); mode = rng.integers(0, len(atoms_arr), M)
    chi = np.zeros(N); lineage = np.zeros(N, dtype=np.int64)
    lid = np.arange(M).copy(); next_id = M
    for t in range(N):
        c = int(rng.integers(M))
        m = int(mode[c]) if carrier == "lineage" else int(rng.integers(len(atoms_arr)))
        chi_acc[c] += float(atoms_arr[m]) if inc == "atoms" else rng.exponential(mean_c)
        chi[t] = chi_acc[c]; lineage[t] = lid[c]
        if rng.random() < 1.0 / L:
            if birth == "reset":
                chi_acc[c] = 0.0
            mode[c] = rng.integers(len(atoms_arr))
            lid[c] = next_id; next_id += 1
    return np.arange(N), chi, lineage

def measure(N, M, L, inc, carrier, birth, atoms_arr=None, seeds=6, fano=False):
    ds, rs, fs, ties = [], [], [], []
    for _ in range(seeds):
        b, c, _ = web(N, M, L, inc, carrier, birth, atoms_arr)
        emb = canon_embed(b, c) if inc == "atoms" else rank_embed2(b, c)
        ds.append(star_disc(emb))
        rs.append(spearman_ties(b, c))
        ties.append(1.0 - len(np.unique(c)) / N)
        if fano:
            fs.append(interval_fano(b, c))
    out = dict(D=float(np.mean(ds)), Dsd=float(np.std(ds)), rho=float(np.mean(rs)),
               tie=float(np.mean(ties)))
    if fano:
        out["fano"] = float(np.mean(fs))
        out["fano_sd"] = float(np.std(fs))
        out["fano_n"] = len(fs)
    return out

def bands(N, nD=20, nF=16):
    fb = [star_disc(rank_embed2(*(lambda p: (p[:, 0], p[:, 1]))(rng.random((N, 2)))))
          for _ in range(nD)]
    ens = [interval_fano(np.argsort(np.argsort(p[:, 0])), p[:, 1])
           for p in (rng.random((N, 2)) for _ in range(nF))]
    return (float(np.mean(fb)), float(np.std(fb)),
            float(np.mean(ens)), float(np.std(ens)))


# ------------------------- CHECK 1: instrument, control, and the j1 anchors
print("CHECK 1: instrument + positive control + j1 anchors")
N, M = 512, 32
faith = [star_disc(rank_embed2(*(lambda p: (p[:, 0], p[:, 1]))(rng.random((N, 2)))))
         for _ in range(20)]
Df, Dsd = float(np.mean(faith)), float(np.std(faith))
print(f"      pooled faithful band D*(rank, N = {N}) = {Df:.4f} +/- {Dsd:.4f}")
pts = rng.random((N, 2))
d_ctrl = star_disc(rank_embed2(np.argsort(np.argsort(pts[:, 0])), pts[:, 1]))
ok = d_ctrl < 1.5 * Df
check("positive control (sprinkling as two-clock configuration) at the band", ok,
      f"D* = {d_ctrl:.4f}")
resA = [star_disc(rank_embed2(*two_clock_j1(N, M, "A"))) for _ in range(6)]
resB = [star_disc(rank_embed2(*two_clock_j1(N, M, "B"))) for _ in range(6)]
rA, rB = float(np.mean(resA)) / Df, float(np.mean(resB)) / Df
ok = rA > 4.5 and rB > 2.5
check("j1 anchors reproduce (A common-birth immortal >= 4.5x; B heterogeneous "
      ">= 2.5x — fresh rng stream, loose tolerance)", ok,
      f"A {rA:.1f}x, B {rB:.1f}x")

# ------------------------- CHECK 2: O1 — the interpolation and the renewal law
print("CHECK 2: layer O1 — churn interpolation W(L, cont, local, reset), N = 512")
print("      L      D*        ratio   rho")
interp = {}
for L in (1, 2, 4, 8, 16, 32):
    r = measure(N, M, L, "cont", "local", "reset")
    interp[L] = r
    print(f"      {L:<6} {r['D']:.4f}   {r['D']/Df:4.1f}x   {r['rho']:+.3f}")
ok = (interp[1]["D"] < 1.5 * Df and interp[32]["D"] > 4 * Df and
      interp[1]["D"] < interp[4]["D"] < interp[16]["D"] < interp[32]["D"])
check("D*(L) interpolates monotonically from the band (L = 1, the singleton/"
      "faithful endpoint) to the family-A wall (L = 32) — lineage turnover with "
      "odometer reset IS the decorrelation mechanism", ok,
      f"{interp[1]['D']/Df:.1f}x -> {interp[32]['D']/Df:.1f}x")
r128 = measure(N, 128, 4, "cont", "local", "reset")
ok = r128["D"] > 1.3 * interp[4]["D"]
check("the fleet-renewal law: M = 128 at L = 4 is WORSE than M = 32 (lifetime "
      "spans L*M global commits; the control parameter is L*M/N, resolving the "
      "sign flip vs paper 13's A128 lesson)", ok,
      f"M128 {r128['D']/Df:.1f}x vs M32 {interp[4]['D']/Df:.1f}x")

# ------------------------- CHECK 3: P2 — the inherit refutation fork
print("CHECK 3: P2 — inherit births leave O1 intact (the refutation arm)")
ok_all = True
for L in (2, 8, 32):
    ri = measure(N, M, L, "cont", "local", "inherit")
    rr = interp.get(L) or measure(N, M, L, "cont", "local", "reset")
    sep = ri["D"] / max(rr["D"], 1e-12)
    print(f"      L = {L:<3} inherit {ri['D']/Df:4.1f}x (rho {ri['rho']:+.2f})  "
          f"vs reset {rr['D']/Df:4.1f}x — separation {sep:.1f}x")
    # the separation gate applies only where reset has LEFT the wall (L = 2, 8);
    # at L = 32 reset is itself at the wall and the two arms converge by
    # construction (churn stops mattering as L -> inf) — wall condition only
    if not (ri["D"] > 4 * Df and ri["rho"] > 0.6 and (L == 32 or sep > 1.8)):
        ok_all = False
check("inherit-chi births stay at the wall (> 4x, rho > 0.6) at EVERY L, and "
      "where reset has left the wall (L = 2, 8) the separation is > 1.8x — the "
      "O1 mechanism attribution is confirmed both ways", ok_all)

# ------------------------- CHECK 4: THE HEADLINE — the churn corner enters the cell
print("CHECK 4: the churn corner W(L = 2, cont, reset) vs N — cell membership")
trend = {}
for NN in (512, 1024, 2048):
    Dfn, Dsn, mun, sdn = bands(NN)
    r = measure(NN, 32, 2, "cont", "local", "reset", seeds=10, fano=True)
    z = abs(r["fano"] - mun) / max(sdn, 1e-12)
    trend[NN] = (r, Dfn, Dsn, z, mun, sdn)
    print(f"      N = {NN:<5} D* {r['D']:.4f} ({r['D']/Dfn:4.2f}x of {Dfn:.4f}+/-{Dsn:.4f})  "
          f"rho {r['rho']:+.3f}  fano z {z:4.1f}")
r2048, Df2048, Ds2048, z2048, mun2048, sdn2048 = trend[2048]
# headline T3 calibration: 40-draw ensemble at N = 2048 (see docstring)
ens40 = [interval_fano(np.argsort(np.argsort(p[:, 0])), p[:, 1])
         for p in (rng.random((2048, 2)) for _ in range(40))]
mun40, sdn40 = float(np.mean(ens40)), float(np.std(ens40))
z2048d = abs(r2048["fano"] - mun40) / max(sdn40, 1e-12)
# what is and is not claimed here: across repeated runs the per-N ratio
# fluctuates by ~+/-0.2 (seed spread x band spread) while the L*M/N transient
# step predicted between N = 512 and 2048 is smaller than that — so NO
# directional trend is claimed or gated; the robust fact is band-ADJACENCY at
# every scale (~1.1-1.4x, against the 5-6x common-birth wall), with the full
# three-layer cell test carried at N = 2048 below
ratios = [trend[NN][0]["D"] / trend[NN][1] for NN in (512, 1024, 2048)]
ok = max(ratios) < 1.6
check("the churn corner is band-ADJACENT at every scale (< 1.6x vs the 5-6x "
      "wall; per-run ratio noise ~+/-0.2 disclosed; the directional trend is "
      "below current resolution and NOT claimed)", ok,
      " -> ".join(f"{x:.2f}x" for x in ratios))
ok = (r2048["D"] <= Df2048 + 2 * Ds2048 and abs(r2048["rho"]) < 0.1 and z2048d < 3)
check("AT N = 2048 ALL THREE LAYERS PASS — T1 rho < 0.1, T2 D* within band + 2sd, "
      "T3 per-draw dispersion z < 3 (40-draw ensemble): a cumulative, churn-born, "
      "record-shaped supply IS in the manifoldlike cell (quasi-continuous content "
      "spread; L = 2)", ok,
      f"D* {r2048['D']:.4f} vs gate {Df2048 + 2*Ds2048:.4f}; rho {r2048['rho']:+.3f}; "
      f"z_draw {z2048d:.1f}")
# combined-uncertainty significance of the mean-level excess (ensemble-mean
# error + corner seed-mean error) — printed, so the paper can quote it:
z_comb = (r2048["fano"] - mun40) / np.sqrt(sdn40**2 / 40 +
                                           r2048["fano_sd"]**2 / r2048["fano_n"])
print(f"      [disclosed residual] mean-level dispersion excess "
      f"{r2048['fano'] - mun40:+.4f} ({100*(r2048['fano']-mun40)/mun40:+.0f}% of "
      f"{mun40:.4f}; ensemble sd {sdn40:.4f}; corner seed sd "
      f"{r2048['fano_sd']:.4f}, n = {r2048['fano_n']}) — combined significance "
      f"z_comb = {z_comb:+.1f}; probe record spans +17% to +30% across runs "
      f"and scales (off-receipt probes, disclosed as such); candidate cause: "
      f"the L = 2 same-lineage pair staircase — a finer-grained open, below "
      f"the T3 instrument's per-draw resolution")

# ------------------------- CHECK 5: the wall relocated — content degeneracy
print("CHECK 5: the STRICT derived model (3 exact atoms) at N = 2048, canonical ties")
mun, sdn = mun40, sdn40
ok_all = True
worst = {}
for car in ("lineage", "local"):
    r = measure(2048, 32, 2, "atoms", car, "reset", fano=True)
    z = abs(r["fano"] - mun) / max(sdn, 1e-12)
    print(f"      atoms3/{car:<8} D*canon {r['D']/Df2048:4.2f}x  rho {r['rho']:+.3f}  "
          f"tie-mass {r['tie']:.2f}  fano z {z:6.1f}")
    worst[car] = (r, z)
    if not (abs(r["rho"]) < 0.1 and r["tie"] > 0.8 and z > 100 and r["D"] > 1.5 * Df2048):
        ok_all = False
check("the 3-atom model DECORRELATES (T1 passes — O1 is cured) yet FAILS the "
      "cell by CONTENT DEGENERACY: > 80% exact chi-ties (Var[content|mode] = 0 "
      "with a 3-atom menu), antidiagonal-module D* > 1.5x, dispersion z > 100 — "
      "the obstruction has MOVED from clock correlation to mode poverty", ok_all)

# ------------------------- CHECK 6: the mode-richness ladder
print("CHECK 6: the richness requirement — menu size vs the statistical layer "
      "(L = 2, lineage, N = 2048; synthetic geomspace menus, disclosed)")
ladder = []
for k, arr in [(3, ATOMS), (8, np.geomspace(ATOMS[2], ATOMS[0], 8)),
               (32, np.geomspace(ATOMS[2], ATOMS[0], 32)),
               (128, np.geomspace(ATOMS[2], ATOMS[0], 128))]:
    r = measure(2048, 32, 2, "atoms", "lineage", "reset", atoms_arr=arr, fano=True)
    z = abs(r["fano"] - mun) / max(sdn, 1e-12)
    ladder.append((k, z, r["tie"]))
    print(f"      atoms = {k:<4} fano z {z:7.1f}  tie-mass {r['tie']:.3f}")
zc = abs(trend[2048][0]["fano"] - mun40) / max(sdn40, 1e-12)
print(f"      continuum   fano z {zc:7.1f}  tie-mass 0.000")
zs = [z for _, z, _ in ladder] + [zc]
ts = [t for _, _, t in ladder]
zat = [z for _, z, _ in ladder]
ok = all(zat[i] > zat[i + 1] for i in range(len(zat) - 1)) and \
     all(ts[i] > ts[i + 1] for i in range(len(ts) - 1)) and \
     zat[0] > 100 and ladder[3][1] < 10 and zc < 3
check("dispersion z falls MONOTONICALLY down the atom ladder (3 -> 8 -> 32 -> "
      "128) and reaches the continuum's own level (z < 3) by ~10^2 atoms at "
      "this scale — records need quasi-continuous content spread to be "
      "spacetime (the new named requirement, hooked to paper 1 §4.4's mode "
      "non-canonicity)", ok,
      f"z: {' > '.join(f'{z:.0f}' for z in zat)}; continuum {zc:.1f}")

# ------------------------- CHECK 7: structure — odometer + canonical realizer
print("CHECK 7: structural sanity")
b7, c7, lin7 = web(512, 32, 4, "atoms", "lineage", "reset")
ok = True
for l in np.unique(lin7):
    mem = np.nonzero(lin7 == l)[0]
    if len(mem) > 1 and not (np.all(np.diff(b7[mem]) > 0) and np.all(np.diff(c7[mem]) > 0)):
        ok = False
check("same-lineage seals strictly increase in both clocks (the odometer is "
      "monotone along its own lineage; resets only ever start NEW lineages)", ok)
bs, cs, _ = web(256, 16, 2, "atoms", "lineage", "reset")
emb = canon_embed(bs, cs)
ok = np.array_equal(dominance_order(emb),
                    dominance_order(np.column_stack([bs.astype(float), cs])))
check("the canonical embedding REALIZES the two-clock order exactly (tie "
      "classes antidiagonal; intersection identity verified bit-level at "
      "N = 256)", ok)

# ------------------------------------------------------------------- verdict
print()
total = PASS + FAIL
if FAIL == 0:
    print(f"ALL CHECKS PASS ({PASS}/{total})")
else:
    print(f"FAILURES: {FAIL}/{total}")
    raise SystemExit(1)
