#!/usr/bin/env python3
"""Blind V9 geometry holdout for the Bell-frozen one-coupling SCIR packet.

Requires numpy and the bundled workspace Python. The V9 builder is SHA-256
gated and changed only at the coupling/seed tuple. The drift-matched dimension
instrument is loaded from its already validation-gated D9 source.
"""

from contextlib import redirect_stderr, redirect_stdout
from hashlib import sha256
from io import StringIO
from pathlib import Path
from runpy import run_path
from statistics import fmean, stdev

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
V9_SOURCE = ROOT / "v9" / "code" / "dimwall_diffusion_d.py"
DIM_SOURCE = ROOT / "v10" / "code" / "d9_drift_matched_dimension.py"
V9_HASH = "aff9525110f6fd209332badccf1a5353c011be9eb8461a4db50063bf0670d81a"
OLD_TUPLE = '((0.18, range(20264500, 20264510), "decision"),)'
NEW_TUPLE = '((0.5, range(20269900, 20269924), "d9-frozen"),)'


def mean_se(values):
    return fmean(values), stdev(values) / len(values) ** 0.5


raw = V9_SOURCE.read_bytes()
assert sha256(raw).hexdigest() == V9_HASH
text = raw.decode("utf-8")
assert text.count(OLD_TUPLE) == 1
text = text.replace(OLD_TUPLE, NEW_TUPLE)

ns = {"__name__": "__main__", "__file__": str(V9_SOURCE)}
with redirect_stdout(StringIO()), redirect_stderr(StringIO()):
    exec(compile(text, str(V9_SOURCE), "exec"), ns)

fd = [float(x) for x in ns["Fd"]]
fm = [float(x) for x in ns["Fm"]]
assert len(fd) == len(fm) == 24
fd_mean, fd_se = mean_se(fd)
fm_mean, fm_se = mean_se(fm)
t_dom = (fd_mean - 1.236) / fd_se
t_m4 = (fm_mean - 1.212) / fm_se
strict_shape = t_dom <= -2.33 and t_m4 <= -2.33
rf = int(ns["rf"])
s4c = int(ns["s4c"])

# Load the already validation-gated dimension curve without exposing the web
# to its construction.
with redirect_stdout(StringIO()), redirect_stderr(StringIO()):
    dim_ns = run_path(str(DIM_SOURCE))
cal_matched = dim_ns["cal_matched"]
interp_d = dim_ns["interpolate_dimension"]


def raw_web_metrics(seed, n=2048):
    ns["G_LEAK"] = 0.5
    chi, commit_slot, rng = ns["build_web"](seed, N=n)
    dmat = chi - chi.mean(axis=1, keepdims=True)
    b = np.arange(n, dtype=float)

    # Frozen shape pipeline: early split-sample tau, central scale-covariant
    # window, 256 points.
    tau_shape = ns["tau_of"](b[: n // 4], dmat[: n // 4], 0.5)
    widx = np.sort(rng.choice(np.arange(n // 4, 3 * n // 4), 256,
                              replace=False))
    rel = ns["ballistic_rel_split"](b[widx], dmat[widx], tau_shape)
    coords = np.column_stack([b[widx], dmat[widx]])
    fdom = ns["F_iso_cloud"](ns["transverse"](rel, coords, "dom"))[0]
    fm4 = ns["F_iso_cloud"](ns["transverse"](rel, coords, "m4"))[0]

    # Validated repair: local tau on the same dimension window used to form
    # the relation fraction.
    lo, hi = 3 * n // 8, 5 * n // 8
    didx = np.sort(rng.choice(np.arange(lo, hi), 128, replace=False))
    tau_local = ns["tau_of"](b[didx], dmat[didx], 0.5)
    drel = ns["ballistic_rel_split"](b[didx], dmat[didx], tau_local)
    frac = float(drel.sum() / (128 * 127 / 2))
    drift = float(dmat[lo:hi].std() / max(dmat[: n // 4].std(), 1e-15))
    return fdom, fm4, frac, drift, commit_slot


holdout_seeds = list(range(20269900, 20269924))
raw_metrics = [raw_web_metrics(seed) for seed in holdout_seeds]
corrected_fraction = fmean(row[2] for row in raw_metrics)
corrected_dimension = interp_d(cal_matched, corrected_fraction)
observed_drift = fmean(row[3] for row in raw_metrics)

# Influence support on three paired worlds at the frozen coupling.
influence_counts = []
for seed in (20270501, 20270502, 20270503):
    ns["G_LEAK"] = 0.5
    base, slots, _ = ns["build_web"](seed, N=2048)
    marked, marked_slots, _ = ns["build_web"](
        seed, N=2048,
        mark=(1024, 7, 1.0, np.array([0.0, 0.0, 1.0])))
    assert np.array_equal(slots, marked_slots)
    changed = np.abs(marked - base).max(axis=1) > 1e-12
    rows = np.where(changed & (np.arange(2048) > 1024))[0]
    influence_counts.append(len(set(int(slots[i]) for i in rows)))

# Scale holdout: no parameter changes, scale-covariant windows, 12 fresh seeds
# per rung. Shape is reported; corrected dimension uses the validated local
# ruler. This is intentionally a smaller scale diagnostic than the 24-seed
# primary holdout.
scale = {}
for n, seed0 in ((2048, 20271000), (4096, 20272000), (8192, 20273000)):
    rows = [raw_web_metrics(seed0 + j, n=n) for j in range(12)]
    md, sed = mean_se([row[0] for row in rows])
    mm, sem = mean_se([row[1] for row in rows])
    frac = fmean(row[2] for row in rows)
    dhat = interp_d(cal_matched, frac)
    drift = fmean(row[3] for row in rows)
    scale[n] = (md, sed, mm, sem, dhat, drift)

dom_worsen = (scale[8192][0] - scale[2048][0]) / (
    scale[8192][1] ** 2 + scale[2048][1] ** 2) ** 0.5
m4_worsen = (scale[8192][2] - scale[2048][2]) / (
    scale[8192][3] ** 2 + scale[2048][3] ** 2) ** 0.5
scale_reversal = dom_worsen >= 2.33 or m4_worsen >= 2.33

dim_pass = 3.5 <= corrected_dimension <= 4.5
witness_pass = rf >= 20 and s4c >= 8
decisive_shape_bad = t_dom >= 2.33 or t_m4 >= 2.33
if strict_shape and dim_pass and witness_pass and not scale_reversal:
    verdict = "SUPPORTED"
elif (not dim_pass) or decisive_shape_bad or scale_reversal:
    verdict = "REFUTED-ONE-COUPLING"
else:
    verdict = "MIXED"

print("D9 BELL-FROZEN PACKET GEOMETRY HOLDOUT")
print(f"v9_source_sha256={V9_HASH}")
print("frozen_theta=pi/4")
print("frozen_g=1/2")
print(f"primary_seeds={holdout_seeds[0]}..{holdout_seeds[-1]}")
print(f"F_dom={fd_mean:.12f} se={fd_se:.12f} t={t_dom:+.6f}")
print(f"F_m4={fm_mean:.12f} se={fm_se:.12f} t={t_m4:+.6f}")
print(f"strict_shape_pass={strict_shape}")
print(f"corrected_relation_fraction={corrected_fraction:.12f}")
print(f"corrected_dimension={corrected_dimension:.12f}")
print(f"observed_scale_drift={observed_drift:.12f}")
print(f"dimension_refusals={rf}/24")
print(f"S4_witnesses={s4c}/24")
print("influence_slots=" + ",".join(str(x) for x in influence_counts))
for n in sorted(scale):
    md, sed, mm, sem, dhat, drift = scale[n]
    print(f"scale_N={n} F_dom={md:.12f} se_dom={sed:.12f} "
          f"F_m4={mm:.12f} se_m4={sem:.12f} "
          f"corrected_d={dhat:.12f} drift={drift:.12f}")
print(f"dom_worsening_z={dom_worsen:+.6f}")
print(f"m4_worsening_z={m4_worsen:+.6f}")
print(f"scale_reversal={scale_reversal}")
print(f"verdict={verdict}")
payload = "|".join([
    V9_HASH, str(fd_mean), str(fm_mean), str(corrected_dimension),
    str(observed_drift), str(rf), str(s4c), str(influence_counts),
    str(scale), str(verdict),
])
print(f"receipt_sha256={sha256(payload.encode('ascii')).hexdigest()}")

