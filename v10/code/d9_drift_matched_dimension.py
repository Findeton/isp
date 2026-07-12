#!/usr/bin/env python3
"""Validation-gated drift-matched dimension instrument for D9.

Requires numpy and is run with the bundled workspace Python. The instrument
is validated only on synthetic latent dimensions before any frozen SCIR web is
read.
"""

from hashlib import sha256

import numpy as np


PASS = 0


def check(condition, label):
    global PASS
    if not condition:
        raise AssertionError(label)
    PASS += 1


def unit_dirs(seed, n, dim):
    rng = np.random.default_rng(seed)
    u = rng.normal(size=(n, dim))
    return u / np.linalg.norm(u, axis=1, keepdims=True)


def tau_of(t, dmat, c=0.5):
    return c * float(dmat.std()) / max(float(np.asarray(t).std()), 1e-15)


def relation_fraction(t, dmat, tau):
    ell = tau * t[:, None] + dmat
    rel = t[:, None] < t[None, :]
    for k in range(dmat.shape[1]):
        rel &= ell[:, None, k] <= ell[None, :, k]
    np.fill_diagonal(rel, False)
    n = len(t)
    return float(rel.sum() / (n * (n - 1) / 2))


def synthetic(seed, latent_d, drift_ratio=1.0, n=2048, k=24):
    rng = np.random.default_rng(seed)
    t = np.sort(rng.random(n))
    x = rng.uniform(-0.5, 0.5, (n, latent_d - 1))
    u = unit_dirs(5000 + latent_d, k, latent_d - 1)
    dmat = x @ u.T
    dmat -= dmat.mean(axis=1, keepdims=True)

    # The mean rank of the early calibration window is about 1/8 and that of
    # the measurement window about 1/2. Choose alpha so their scale ratio is
    # the declared drift_ratio.
    alpha = np.log(drift_ratio) / 0.375
    q = np.arange(n, dtype=float) / (n - 1)
    dmat *= np.exp(alpha * q)[:, None]

    didx = np.sort(rng.choice(np.arange(768, 1280), 128, replace=False))
    early = np.arange(512)
    tau_legacy = tau_of(t[early], dmat[early])
    tau_matched = tau_of(t[didx], dmat[didx])
    legacy = relation_fraction(t[didx], dmat[didx], tau_legacy)
    matched = relation_fraction(t[didx], dmat[didx], tau_matched)
    observed_ratio = float(dmat[didx].std() / dmat[early].std())
    return legacy, matched, observed_ratio


def interpolate_dimension(curve, value):
    ds = sorted(curve)
    fs = [curve[d] for d in ds]
    if value >= fs[0]:
        return float(ds[0])
    if value <= fs[-1]:
        return float(ds[-1])
    for i in range(len(ds) - 1):
        if fs[i] >= value >= fs[i + 1]:
            w = (fs[i] - value) / (fs[i] - fs[i + 1])
            return ds[i] + w * (ds[i + 1] - ds[i])
    raise AssertionError((curve, value))


# Calibration is frozen on stationary synthetic references.
cal_legacy = {}
cal_matched = {}
for d in range(2, 7):
    rows = [synthetic(20269100 + 100 * d + j, d, 1.0) for j in range(32)]
    cal_legacy[d] = float(np.mean([row[0] for row in rows]))
    cal_matched[d] = float(np.mean([row[1] for row in rows]))

check(all(cal_legacy[d] > cal_legacy[d + 1] for d in range(2, 6)),
      "legacy stationary calibration monotone")
check(all(cal_matched[d] > cal_matched[d + 1] for d in range(2, 6)),
      "matched stationary calibration monotone")


results = {}
for drift_ratio in (1.0, 1.55, 1.94):
    for d in range(2, 7):
        rows = [synthetic(20269700 + int(100 * drift_ratio) + 1000 * d + j,
                          d, drift_ratio) for j in range(24)]
        f_legacy = float(np.mean([row[0] for row in rows]))
        f_matched = float(np.mean([row[1] for row in rows]))
        ratio = float(np.mean([row[2] for row in rows]))
        d_legacy = interpolate_dimension(cal_legacy, f_legacy)
        d_matched = interpolate_dimension(cal_matched, f_matched)
        results[(drift_ratio, d)] = (d_legacy, d_matched, ratio,
                                     f_legacy, f_matched)

# The matched estimator must recover all known dimensions at both injected
# nonstationarities. Endpoint dimensions are allowed one-sided clamp error.
for drift_ratio in (1.0, 1.55, 1.94):
    for d in range(2, 7):
        d_matched = results[(drift_ratio, d)][1]
        check(abs(d_matched - d) <= 0.35,
              f"matched recovery drift={drift_ratio} d={d}")

# The old split-window estimator must visibly move on the load-bearing d=4
# controls, reproducing the diagnosed failure mode.
legacy_d4_155 = results[(1.55, 4)][0]
legacy_d4_194 = results[(1.94, 4)][0]
check(abs(legacy_d4_155 - 4) >= 0.35,
      "legacy estimator biased at 1.55 drift")
check(abs(legacy_d4_194 - 4) >= 0.35,
      "legacy estimator biased at 1.94 drift")

matched_d4_155 = results[(1.55, 4)][1]
matched_d4_194 = results[(1.94, 4)][1]
check(abs(matched_d4_155 - 4) <= 0.20,
      "matched d4 recovery at 1.55 drift")
check(abs(matched_d4_194 - 4) <= 0.20,
      "matched d4 recovery at 1.94 drift")


print("D9 DRIFT-MATCHED DIMENSION VALIDATION")
print(f"checks={PASS}")
print("stationary_curve_legacy=" + ",".join(f"d{d}:{cal_legacy[d]:.9f}" for d in range(2, 7)))
print("stationary_curve_matched=" + ",".join(f"d{d}:{cal_matched[d]:.9f}" for d in range(2, 7)))
for drift_ratio in (1.0, 1.55, 1.94):
    for d in range(2, 7):
        dl, dm, ratio, fl, fm = results[(drift_ratio, d)]
        print(f"drift={drift_ratio:.2f} latent_d={d} observed_scale={ratio:.6f} "
              f"legacy_d={dl:.6f} matched_d={dm:.6f} "
              f"f_legacy={fl:.9f} f_matched={fm:.9f}")
payload = "|".join([
    str(PASS),
    *(f"{key[0]}:{key[1]}:{':'.join(f'{v:.12f}' for v in results[key])}"
      for key in sorted(results)),
])
print(f"receipt_sha256={sha256(payload.encode('ascii')).hexdigest()}")

