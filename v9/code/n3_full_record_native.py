#!/usr/bin/env python3
"""
n3_full_record_native.py — v9 round 15: L3's FULL leg (note-n3-full;
gates pinned there and committed BEFORE this receipt existed).

Two substrates x six seeds under the amended composition (L2 AND n3's
own void-controls; the spectral gate stays RETIRED per the lite's
kernel-curvature attribution):
  ARM 1 (continuity anchor): the lite's lineage-segment substrate
     (N, M, L) = (2048, 32, 16), chains = lineage segments >= 8 commits.
  ARM 2 (the named design item): the certified builder's corner via
     SLOT-WORLDLINES — (N, M, L) = (2048, 64, 2), chains = fleet slots
     (each slot's full commit history; persistent at any lifetime).
GATES (note-n3-full SS2): G-1 closure >= 0.9 on >= 5/6 seeds per arm;
G-2 shuffle void > 3 null-sd every seed; G-3 confound void < 2.5
null-sd every axis-pair every seed (arm-2 confounds: slot mean-content,
lifetime count, first-commit time); G-4 the certification band: closure
floor >= 0.85 per arm; G-5 coverage printed, measured-not-gated.
Tier-A field verbatim from the lite (latent 2D, exp(-d/0.6), 5% noise);
grade [DEMONSTRATED given Tier-A input]. Seeds 20260722..27; float64.
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

def mds_xy(AFF):
    M = len(AFF)
    DIS = AFF.max() - AFF
    np.fill_diagonal(DIS, 0.0)
    J = np.eye(M) - np.ones((M, M)) / M
    B = -0.5 * J @ (DIS ** 2) @ J
    ev, V = np.linalg.eigh(B)
    return ev[::-1], V[:, -2:] * np.sqrt(np.maximum(ev[-2:], 0))

def procrustes_corr(A, Bm):
    A = A - A.mean(0); Bm = Bm - Bm.mean(0)
    U, s_, Vt = np.linalg.svd(A.T @ Bm)
    return float(np.corrcoef((A @ (U @ Vt)).ravel(), Bm.ravel())[0, 1])

def build_web(rng, N, M, L, mode):
    """mode = 'segments' (lite construction) or 'slots' (worldlines)."""
    chi_acc = np.zeros(M)
    segs = {}; gen = np.zeros(M, dtype=int); birth = {}
    for m in range(M):
        segs[(m, 0)] = []; birth[(m, 0)] = 0
    slot_hist = {m: [] for m in range(M)}
    lifec = np.zeros(M, dtype=int)
    chi_series = np.zeros(N)
    first_commit = np.full(M, -1.0)
    for t in range(N):
        c = int(rng.integers(M))
        chi_acc[c] += rng.exponential(0.109551)
        chi_series[t] = chi_acc[c]
        segs[(c, gen[c])].append(t)
        slot_hist[c].append(t)
        if first_commit[c] < 0: first_commit[c] = t
        if rng.random() < 1.0 / L:
            v = int(rng.integers(M))
            chi_acc[v] = 0.0
            gen[v] += 1; lifec[v] += 1
            segs[(v, gen[v])] = []; birth[(v, gen[v])] = t
    if mode == "segments":
        chains = [(k, v) for k, v in segs.items() if len(v) >= 8]
        confs = {
            "birth": np.array([birth[k] for k, _ in chains], dtype=float),
            "level": np.array([chi_series[v].mean() for _, v in chains]),
        }
        return [v for _, v in chains], confs
    chains = [slot_hist[m] for m in range(M) if len(slot_hist[m]) >= 8]
    keep = [m for m in range(M) if len(slot_hist[m]) >= 8]
    confs = {
        "level": np.array([chi_series[slot_hist[m]].mean() for m in keep]),
        "lives": lifec[keep].astype(float),
        "first": first_commit[keep],
    }
    return chains, confs

ARMS = (("segments (lite anchor)", 2048, 32, 16, "segments"),
        ("corner slot-worldlines", 2048, 64, 2, "slots"))
SEEDS = list(range(20260722, 20260728))
band = {}
for name, N, M, L, mode in ARMS:
    pcs = []; ok2 = True; ok3 = True; cov_rows = []
    for sd in SEEDS:
        rng = np.random.default_rng(sd)
        chains, confs = build_web(rng, N, M, L, mode)
        Mc = len(chains)
        lat = rng.random((Mc, 2)) * 2 - 1
        D_lat = np.hypot(lat[:, 0, None] - lat[None, :, 0],
                         lat[:, 1, None] - lat[None, :, 1])
        chi_AB = np.exp(-D_lat / 0.6) * (1 + 0.05 * rng.standard_normal((Mc, Mc)))
        chi_AB = np.abs((chi_AB + chi_AB.T) / 2)
        np.fill_diagonal(chi_AB, 0.0)
        ev, XY = mds_xy(chi_AB)
        pc = procrustes_corr(XY, lat)
        pcs.append(pc)
        # G-2 shuffle null
        iu = np.triu_indices(Mc, 1)
        nulls = []
        for _ in range(24):
            perm = rng.permutation(len(iu[0]))
            As = np.zeros_like(chi_AB)
            As[iu] = chi_AB[iu][perm]
            As = As + As.T
            _, XYs = mds_xy(As)
            nulls.append(procrustes_corr(XYs, lat))
        z = (pc - float(np.mean(nulls))) / float(np.std(nulls, ddof=1))
        if z <= 3: ok2 = False
        # G-3 confounds
        null_sd = 1.0 / np.sqrt(Mc - 1)
        cors = [abs(float(np.corrcoef(XY[:, d], q)[0, 1]))
                for d in (0, 1) for q in confs.values()]
        if any(c >= 2.5 * null_sd for c in cors): ok3 = False
        # G-5 coverage
        qcounts = [int(np.sum((lat[:, 0] > 0) & (lat[:, 1] > 0))),
                   int(np.sum((lat[:, 0] > 0) & (lat[:, 1] <= 0))),
                   int(np.sum((lat[:, 0] <= 0) & (lat[:, 1] > 0))),
                   int(np.sum((lat[:, 0] <= 0) & (lat[:, 1] <= 0)))]
        cov_rows.append(min(qcounts) >= Mc / 8)
        print(f"      [{name}] seed {sd}: Mc = {Mc}, closure {pc:.3f}, "
              f"shuffle-z {z:.1f}, max|conf| {max(cors):.3f} "
              f"(2.5sd = {2.5*null_sd:.3f}), quad-min {min(qcounts)}")
    band[name] = (min(pcs), max(pcs))
    n_ok = sum(1 for p in pcs if p >= 0.9)
    check(f"G-1 [{name}]: closure >= 0.9 on >= 5/6 seeds", n_ok >= 5,
          f"{n_ok}/6 (band [{min(pcs):.3f}, {max(pcs):.3f}])")
    check(f"G-2 [{name}]: shuffle void > 3 null-sd on every seed", ok2)
    check(f"G-3 [{name}]: confounds < 2.5 null-sd on every axis-pair, "
          f"every seed", ok3)
    check(f"G-4 [{name}]: the certification band floor >= 0.85",
          min(pcs) >= 0.85, f"floor = {min(pcs):.3f}")
    print(f"      G-5 [{name}] coverage (measured-not-gated): quadrant "
          f"occupancy >= Mc/8 on {sum(cov_rows)}/6 seeds")

print()
print(f"PRE-REGISTERED GATE LEDGER: "
      f"{'ALL HELD' if FAIL == 0 else 'REFUSALS PRESENT'} — G-1..G-4 x 2 "
      f"arms; G-5 measured")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
