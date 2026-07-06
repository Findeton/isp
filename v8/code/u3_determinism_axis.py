#!/usr/bin/env python3
"""
u3_determinism_axis.py — design note 8 gate G2 (pilot): where does
determinism in the click law become geometrically visible?

THE QUESTION (note 8 §2/§4): the beta-family has two deterministic limits —
D1 (deterministic PLACEMENT: the web-building move is argmax-Phi of the
history; the committer race and the content stay random — corpus-
conservative) and D2 (fully deterministic SEQUENCING: the committer itself is
a history functional — a posit swap replacing the independence refinement of
paper 13's posit 1). The note's G2 conjecture: irreducible randomness in the
click law is necessary for the statistical layer (Poisson-typicality); the
lattice precedent (paper 12: volume-pass, statistical-fail z = 5.2
SUB-Poisson) says regularity is what dispersion catches.

PRE-REGISTERED PREDICTIONS, RECORDED BEFORE FIRST RUN (P1's fate recorded
after it — the corpus convention: predictions stand in the text with their
measured verdicts, not silently rewritten):
  (P1) D2b — the evidence-balancing committer (argmin chi_acc commits) —
       REBUILDS the clock correlation that churn cured: water-filling makes
       the fleet rise in lockstep, chi(t) tracks the rising minimum level,
       so T1 fails toward rho ~ +1. *** REFUTED at the exploration pass:
       rho = +0.06 at the churn corner. The mechanism control (CHECK 4)
       localizes why: a freshly reset slot IS the argmin and monopolizes
       commits during catch-up, sweeping chi across [0, level] — CHURN
       LAUNDERS THE LOCKSTEP. Remove churn and the prediction's mechanism
       is real (rho = +0.98 at L = inf; +0.42 at L = 8): the visibility
       axis is L, not determinism per se. ***
  (P2) D2a — round-robin committer — trivially deviates from the race's
       sequencing marginal (per-slot gap = M exactly vs Geometric(1/M)).
       HELD.
  (P3) D1 — kill-the-oldest victim (deterministic placement at fixed event
       rate) — concentrates the lifetime law (sd << geometric's). HELD.
       Its dispersion-layer effect was NOT confidently predicted (two-sided
       measurement, disclosed): the run resolved it to the BENEFICIAL side
       — D1 REDUCES the corner's dispersion excess (the paper-16 staircase
       residual is lifetime-tail-driven; see CHECK 1).

SCOPE, stated in advance: this is the G2 PILOT. Full placement+content
determinism (w = 0 atoms + deterministic mode + D1) is confounded at the
3-atom corner by the content-degeneracy wall (j3: z ~ 400 for reasons that
have nothing to do with placement); the rich-menu arm (128 geomspace atoms,
j3's disclosed synthetic ladder convention, statically in-cell) isolates the
placement axis. The D2 rows measure the SEQUENCING-MARGINAL deviation (the
observable face of the posit swap) — deviation is not illegality: the swap
is licensed by the note, and its price is what is being measured. The
corpus-legality question proper (can ANY deterministic committer preserve
the per-lineage Exp(1) evidence marginals C1 derives?) is the note's named
proof target, not settled here.

Gate discipline as in u2: gates marked [pinned-post-exploration] were set
from the disclosed same-date single exploration pass on this stream.
Conventions: default_rng(20260703); float64; canonical tie treatment
(paper 12's relabeling-lemma point set) on atomic arms; j1's dispersion
statistic with SIGNED z reported (sub- vs super-Poisson disclosed).
"""

import numpy as np

rng = np.random.default_rng(20260703)

PASS = 0
FAIL = 0

def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))


# ------------------------------------------------------------- instruments
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
    r1 = np.argsort(np.argsort(b)); r2 = np.argsort(np.argsort(chi))
    return np.column_stack([(r1 + 0.5) / N, (r2 + 0.5) / N])

def canon_embed(b, chi):
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
    return float(np.corrcoef(avg_rank(x), avg_rank(y))[0, 1])

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
ATOM_LO, ATOM_HI = 0.063376134128, 0.156109200157

def web(N, M, L, victim="uniform", committer="race", atoms=None):
    """The churn web with pluggable sequencing (committer) and placement
    (victim) laws. committer in {race, roundrobin, argmin_chi};
    victim in {uniform, oldest}; atoms None => continuous exponential
    increments (route B), else the given menu with uniform mode choice."""
    chi_acc = np.zeros(M)
    chi = np.zeros(N)
    own = np.zeros(M, dtype=np.int64); born = np.zeros(M, dtype=np.int64)
    age_events = np.zeros(M, dtype=np.int64)   # churn events survived
    lifetimes = []
    gaps = {m: [] for m in range(M)}
    last_commit = np.full(M, -1, dtype=np.int64)
    for t in range(N):
        if committer == "race":
            c = int(rng.integers(M))
        elif committer == "roundrobin":
            c = t % M
        elif committer == "argmin_chi":
            c = int(np.argmin(chi_acc))
        if last_commit[c] >= 0:
            gaps[c].append(int(t - last_commit[c]))
        last_commit[c] = t
        if atoms is None:
            chi_acc[c] += rng.exponential(0.109551)
        else:
            chi_acc[c] += float(atoms[int(rng.integers(len(atoms)))])
        own[c] += 1
        chi[t] = chi_acc[c]
        if rng.random() < 1.0 / L:
            age_events += 1
            if victim == "uniform":
                v = int(rng.integers(M))
            elif victim == "oldest":
                v = int(np.argmax(age_events))
            lifetimes.append(int(own[v] - born[v]))
            chi_acc[v] = 0.0; born[v] = own[v]; age_events[v] = 0
    allgaps = np.array([g for m in range(M) for g in gaps[m]], dtype=float)
    return np.arange(N), chi, np.array(lifetimes, dtype=float), allgaps

def bands(N, nD=16, nF=16):
    fb = [star_disc(rank_embed2(*(lambda p: (p[:, 0], p[:, 1]))(rng.random((N, 2)))))
          for _ in range(nD)]
    ens = [interval_fano(np.argsort(np.argsort(p[:, 0])), p[:, 1])
           for p in (rng.random((N, 2)) for _ in range(nF))]
    return (float(np.mean(fb)), float(np.std(fb)),
            float(np.mean(ens)), float(np.std(ens)))

def geom_cdf_dist(gaps, p):
    """sup-distance between the empirical gap CDF and Geometric(p) on
    {1, 2, ...} (the uniform race's per-slot sequencing marginal)."""
    if len(gaps) == 0:
        return float("nan")
    ks = np.arange(1, int(gaps.max()) + 2)
    F_geom = 1.0 - (1.0 - p) ** ks
    F_emp = np.searchsorted(np.sort(gaps), ks, side="right") / len(gaps)
    return float(np.abs(F_emp - F_geom).max())


# =========================== CHECK 1: D1 — deterministic placement, N = 512
print("CHECK 1: D1 (kill-the-oldest victim) vs uniform, continuous content, "
      "N = 512")
N, M, L = 512, 32, 2
Df, Dsd, mu_f, sd_f = bands(N)
print(f"      band {Df:.4f} +/- {Dsd:.4f}; fano ensemble {mu_f:.3f} +/- {sd_f:.3f}")
print("      law            D*      ratio   |rho|   fano    z(signed)  "
      "lifetime mean/sd")
rows = {}
for tag, vic in (("uniform", "uniform"), ("D1 oldest", "oldest")):
    ds, rs, fs, lt_m, lt_s = [], [], [], [], []
    for _ in range(6):
        b, c, lts, _ = web(N, M, L, victim=vic)
        ds.append(star_disc(rank_embed2(b, c)))
        rs.append(spearman_ties(b, c))
        fs.append(interval_fano(b, c))
        lt_m.append(lts.mean()); lt_s.append(lts.std())
    D_, rho_, f_ = float(np.mean(ds)), float(np.mean(np.abs(rs))), float(np.mean(fs))
    z_ = (f_ - mu_f) / max(sd_f, 1e-12)
    rows[tag] = (D_, rho_, f_, z_, float(np.mean(lt_m)), float(np.mean(lt_s)))
    print(f"      {tag:<12} {D_:.4f}  {D_/Df:5.2f}x  {rho_:.3f}  {f_:.3f}  "
          f"{z_:+6.1f}     {rows[tag][4]:.2f}/{rows[tag][5]:.2f}")
# [pinned-post-exploration] measured: D1 concentrates the lifetime law
# (sd 2.13 -> 1.41 at mean ~ 1.8) — P3's distribution prediction held — and
# IMPROVES every geometric layer: D* 1.72x -> 1.15x, |rho| 0.132 -> 0.048,
# and the dispersion excess z +5.0 -> +1.3. Two disclosures: (i) the uniform
# kernel's z = +5.0 at N = 512 (vs +2.4 at N = 2048 in u1) says the corner's
# dispersion excess — paper 16's L = 2 same-lineage staircase residual — is
# LARGER at small N, consistent with a finite-N staircase; (ii) that D1
# CURES most of it identifies the residual as LIFETIME-TAIL-DRIVEN: the
# geometric lifetime law's long tail, not churn per se, carries the excess.
# A named fix candidate for the paper-16 residual, at directional grade.
ok = rows["D1 oldest"][5] < 0.8 * rows["uniform"][5]
check("P3 (distribution level): the deterministic victim concentrates the "
      "lifetime law (sd < 0.8x the uniform kernel's)", ok,
      f"sd {rows['uniform'][5]:.2f} -> {rows['D1 oldest'][5]:.2f}")
ok = rows["D1 oldest"][0] < 2.0 * Df and abs(rows["D1 oldest"][3]) < 3.5
check("D1 stays in the corner's range on all layers — placement determinism "
      "at fixed event rate is geometrically INVISIBLE at N = 512 (the G2 "
      "conjecture does NOT bite at the placement layer here; the randomness "
      "the statistical layer needs is supplied by the race + content)", ok,
      f"D* {rows['D1 oldest'][0]/Df:.2f}x, z {rows['D1 oldest'][3]:+.1f}")
ok = rows["D1 oldest"][2] < rows["uniform"][2] and \
     abs(rows["D1 oldest"][3]) < abs(rows["uniform"][3])
check("BEYOND invisibility: D1 REDUCES the corner's dispersion excess "
      "(z +5.0 -> +1.3) — the paper-16 staircase residual is identified as "
      "lifetime-tail-driven (concentrating the lifetime law cures most of "
      "it); directional grade, single stream", ok,
      f"fano {rows['uniform'][2]:.3f} -> {rows['D1 oldest'][2]:.3f}")

# =========================== CHECK 2: D1 + rich atoms, N = 1024
print("CHECK 2: D1 on the rich-atom menu (128 geomspace atoms, canonical "
      "ties), N = 1024")
N2 = 1024
Df2, Dsd2, mu2, sd2 = bands(N2, nD=12, nF=16)
atoms128 = np.geomspace(ATOM_LO, ATOM_HI, 128)
print(f"      band {Df2:.4f} +/- {Dsd2:.4f}; fano ensemble {mu2:.3f} +/- {sd2:.3f}")
rows2 = {}
for tag, vic in (("uniform+atoms", "uniform"), ("D1 oldest+atoms", "oldest")):
    ds, rs, fs = [], [], []
    for _ in range(4):
        b, c, _, _ = web(N2, M, L, victim=vic, atoms=atoms128)
        ds.append(star_disc(canon_embed(b, c)))
        rs.append(spearman_ties(b, c))
        fs.append(interval_fano(b, c))
    D_, rho_, f_ = float(np.mean(ds)), float(np.mean(np.abs(rs))), float(np.mean(fs))
    z_ = (f_ - mu2) / max(sd2, 1e-12)
    rows2[tag] = (D_, rho_, f_, z_)
    print(f"      {tag:<16} D* {D_:.4f} ({D_/Df2:.2f}x)  |rho| {rho_:.3f}  "
          f"fano {f_:.3f}  z {z_:+.1f}")
# [pinned-post-exploration] measured: uniform+atoms 1.33x (z +1.1); D1+atoms
# lands AT THE BAND — 0.96x, z -1.3 — the first arm in the u-line to reach
# ratio ~ 1.0. Directional grade (4 seeds, single stream): a certification
# claim needs the N = 2048 / more-seed retest, named as the u-line's top
# follow-up. The invisibility finding is thereby STRENGTHENED to a mild
# benefit on the quasi-continuous menu as well.
ok = all(v[0] < 2.0 * Df2 and abs(v[3]) < 3.5 for v in rows2.values())
check("no confound-free dispersion break on the rich menu at N = 1024 for "
      "either arm — placement-determinism invisibility persists", ok)
ok = rows2["D1 oldest+atoms"][0] < 1.15 * Df2
check("D1+atoms reaches the faithful band itself (ratio < 1.15x) — the "
      "closest approach to ratio 1.0 measured in the corner family so far "
      "(directional grade; certification retest named)", ok,
      f"{rows2['D1 oldest+atoms'][0]/Df2:.2f}x")

# =========================== CHECK 3: D2 — the sequencing-marginal price
print("CHECK 3: D2 candidates — deviation from the race's sequencing marginal")
N3 = 10_000
_, _, _, gaps_race = web(N3, M, L, committer="race")
_, _, _, gaps_rr = web(N3, M, L, committer="roundrobin")
_, _, _, gaps_am = web(N3, M, L, committer="argmin_chi")
p = 1.0 / M
d_race = geom_cdf_dist(gaps_race, p)
d_rr = geom_cdf_dist(gaps_rr, p)
d_am = geom_cdf_dist(gaps_am, p)
print(f"      sup-CDF distance to Geometric(1/M): race (calibration) "
      f"{d_race:.4f}; round-robin {d_rr:.4f}; argmin-chi {d_am:.4f}")
# power note: at ~1e4 gaps the calibration distance is O(1e-2); the
# deterministic candidates' deviations are O(1e-1)-O(1) — the gate below is
# powered by two orders of magnitude against the tested alternatives (the
# #36 M1 lesson: the power against the SPECIFIC alternative is stated, not
# assumed).
ok = d_race < 0.03 and d_rr > 5 * d_race and d_am > 5 * d_race
check("P2 + the argmin row: BOTH tested deterministic committers deviate "
      "from the race's Geometric(1/M) sequencing marginal by > 5x the "
      "calibration distance — the posit swap is OBSERVABLE at the "
      "sequencing layer for every tested candidate (enumerative grade; "
      "the can-any-D2-hide question is the note's named proof target)", ok,
      f"race {d_race:.3f}, RR {d_rr:.3f}, argmin {d_am:.3f}")

# =========================== CHECK 4: P1 — refuted, and the mechanism found
print("CHECK 4: P1 refuted — churn launders deterministic sequencing; the "
      "mechanism control")
ds, rs = [], []
for _ in range(4):
    b, c, _, _ = web(512, M, L, committer="argmin_chi")
    ds.append(star_disc(rank_embed2(b, c)))
    rs.append(spearman_ties(b, c))
rho_am = float(np.mean(rs)); D_am = float(np.mean(ds))
print(f"      argmin-chi web at L = 2: rho = {rho_am:+.3f}, D* = {D_am:.4f} "
      f"({D_am/Df:.2f}x)")
ok = rho_am < 0.2
check("P1 REFUTED (the pre-registered prediction was WRONG, recorded): at "
      "the churn corner the evidence-balancing committer does NOT rebuild "
      "the clock correlation — a freshly reset slot is the argmin and "
      "monopolizes commits during catch-up, sweeping chi across [0, level]: "
      "CHURN LAUNDERS THE LOCKSTEP, and the web stays band-adjacent", ok,
      f"rho = {rho_am:+.3f}, D* = {D_am/Df:.2f}x")
# the mechanism control: the predicted lockstep is real WITHOUT churn —
# rho must rise monotonically in L toward ~ +1 as the laundering is removed
rho_by_L = {}
for Lc in (2, 8, 10 ** 9):
    rs = []
    for _ in range(4):
        b, c, _, _ = web(512, M, Lc, committer="argmin_chi")
        rs.append(spearman_ties(b, c))
    rho_by_L[Lc] = float(np.mean(rs))
print(f"      laundering axis: rho(L = 2) = {rho_by_L[2]:+.3f}, "
      f"rho(L = 8) = {rho_by_L[8]:+.3f}, rho(no churn) = "
      f"{rho_by_L[10**9]:+.3f}")
ok = rho_by_L[2] < rho_by_L[8] < rho_by_L[10 ** 9] and rho_by_L[10 ** 9] > 0.9
check("the mechanism is localized: WITHOUT churn the water-filling lockstep "
      "is real (rho > +0.9, the O1 obstruction reborn exactly as P1 "
      "reasoned) and rho rises monotonically in L — the geometric "
      "VISIBILITY of sequencing determinism is controlled by the churn "
      "rate, not by determinism per se; the same churn that cures O1 "
      "(paper 16) also launders a determinized committer", ok,
      f"{rho_by_L[2]:+.2f} < {rho_by_L[8]:+.2f} < {rho_by_L[10**9]:+.2f}")

# ------------------------- verdict
print()
total = PASS + FAIL
if FAIL == 0:
    print(f"ALL CHECKS PASS ({PASS}/{total})")
else:
    print(f"FAILURES: {FAIL}/{total}")
    raise SystemExit(1)
