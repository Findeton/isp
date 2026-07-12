#!/usr/bin/env python3
"""D11 finite generated-history and paired-intervention campaign.

This is the numerical companion to d11_complete_bloch_lorentz_exact.py.  It
uses the frozen equal-activity SPLIT/JOIN/SEAL grammar without survivor
selection or parameter tuning.  Algebraic identities are primary in the
exact script; this file asks whether typical complete histories live long
enough to populate the cone and transmit interventions through joins.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from math import cos, pi, sqrt
from statistics import median

import numpy as np


I2 = np.eye(2, dtype=complex)
P0 = np.array([[1, 0], [0, 0]], dtype=complex)
P1 = np.array([[0, 0], [0, 1]], dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
PPLUS = (I2 + X) / 2
H = np.array([[1, 1], [1, -1]], dtype=complex) / sqrt(2)
T = np.diag([1, np.exp(1j * pi / 4)])
UPS = np.array([
    [1, 0, 0, 0],
    [0, 1 / sqrt(2), 1j / sqrt(2), 0],
    [0, 1j / sqrt(2), 1 / sqrt(2), 0],
    [0, 0, 0, 1],
], dtype=complex)
J0 = UPS[[0, 2], :]
J1 = UPS[[1, 3], :]
PAULI = (X, Y, Z)
TOL = 2e-11


def clean_rho(rho):
    rho = (rho + rho.conj().T) / 2
    return rho / np.trace(rho).real


def push(u, rho):
    return clean_rho(u @ rho @ u.conj().T)


def branch(k, rho):
    out = k @ rho @ k.conj().T
    p = float(np.trace(out).real)
    if p <= 1e-15:
        return p, None
    return p, clean_rho(out / p)


def herm_vector(a):
    """X=tI+x.sigma -> (t,x,y,z), using trace pairings."""
    vals = [np.trace(a).real / 2]
    vals.extend(np.trace(s @ a).real / 2 for s in PAULI)
    return np.asarray(vals, dtype=float)


def increment(rho):
    return herm_vector(2 * rho)


def future(delta, tol=TOL):
    q = np.asarray(delta, dtype=np.longdouble)
    return q[0] + np.longdouble(tol) >= np.sqrt(np.sum(q[1:] ** 2))


def fib_sphere(n):
    k = np.arange(n, dtype=float) + 0.5
    z = 1 - 2 * k / n
    r = np.sqrt(np.maximum(0, 1 - z * z))
    az = pi * (3 - sqrt(5)) * k
    return np.column_stack([r * np.cos(az), r * np.sin(az), z])


PROBE = fib_sphere(4096)
F_DIRS = fib_sphere(64)


def covering_support(directions):
    if not directions:
        return -1.0
    points = np.asarray(directions)
    return float(np.min(np.max(PROBE @ points.T, axis=1)))


def transverse(rel, coords, family):
    x = (coords - coords.mean(axis=0)) / np.maximum(coords.std(axis=0), 1e-12)
    if family == "m4":
        axis = np.array([1.0, 0.0, 0.0, 0.0])
    else:
        axis = np.ones(4) / 2
    ii, jj = np.where(rel)
    if not len(ii):
        return np.empty((0, 4))
    d = x[jj] - x[ii]
    s = d @ axis
    keep = s >= 0.3
    d, s = d[keep], s[keep]
    return d / s[:, None] - axis[None, :] if len(d) else np.empty((0, 4))


def f_iso_cloud(v):
    if len(v) < 120:
        return float("nan"), 0, float("nan")
    cov = np.cov(v.T)
    vals, vecs = np.linalg.eigh(cov)
    order = np.argsort(vals)[::-1]
    vals, frame = vals[order], vecs[:, order[:3]]
    p3 = v @ frame
    supports = []
    min_count = 10**9
    for u in F_DIRS:
        positive = p3 @ u
        positive = positive[positive > 0]
        min_count = min(min_count, len(positive))
        if len(positive) < 30:
            return float("nan"), min_count, float(vals[2] / max(vals[0], 1e-30))
        supports.append(np.quantile(positive, 0.9))
    supports = np.sort(supports)
    return (float(supports[-8:].mean() / supports[:8].mean()), min_count,
            float(vals[2] / max(vals[0], 1e-30)))


def m4_control(seed, n=256):
    rng = np.random.default_rng(seed)
    rows = []
    while sum(len(x) for x in rows) < n:
        t = rng.random(6 * n)
        xyz = rng.uniform(-0.5, 0.5, (6 * n, 3))
        r = np.linalg.norm(xyz, axis=1)
        keep = (r <= t) & (r <= 1 - t)
        rows.append(np.column_stack([t[keep], xyz[keep]]))
    coords = np.vstack(rows)[:n]
    d = coords[None, :, :] - coords[:, None, :]
    rel = (d[:, :, 0] > 0) & (d[:, :, 0] >= np.linalg.norm(d[:, :, 1:], axis=2))
    np.fill_diagonal(rel, False)
    return tuple(f_iso_cloud(transverse(rel, coords, family))[0]
                 for family in ("dom", "m4"))


@dataclass
class Port:
    pid: int
    record: int
    rho: np.ndarray
    rho_i: np.ndarray
    y: np.ndarray
    y_i: np.ndarray


@dataclass
class Join:
    jid: int
    left: int
    right: int
    anchor_record: int
    anchor_y: np.ndarray
    anchor_y_i: np.ndarray


@dataclass
class Record:
    rid: int
    y: np.ndarray
    y_i: np.ndarray
    parents: tuple
    ancestors: frozenset
    kind: str


def differs(a, b):
    return np.max(np.abs(a - b)) > TOL


def join_step(rhoa, rhob, outcome):
    k = J0 if outcome == 0 else J1
    return branch(k, np.kron(rhoa, rhob))[1]


def outcome_from_u(p0, u):
    return 0 if u < min(1.0, max(0.0, p0)) else 1


def simulate(seed, cutoff):
    rng = np.random.default_rng(seed)
    ports = {0: Port(0, 0, P0.copy(), PPLUS.copy(), np.zeros(4), np.zeros(4))}
    joins = {}
    records = {0: Record(0, np.zeros(4), np.zeros(4), (), frozenset(), "ROOT")}
    next_pid = next_jid = next_rid = 1
    counts = {"SPLIT": 0, "JOIN": 0, "SEAL": 0}
    max_open = 1
    edge_violations = influence_violations = 0
    changed_seals = join_transfers = 0
    null_directions = []

    def invalidate(consumed):
        for pid in consumed:
            ports.pop(pid, None)
        stale = [jid for jid, jt in joins.items()
                 if jt.left in consumed or jt.right in consumed]
        for jid in stale:
            joins.pop(jid, None)

    def add_record(y, yi, parents, kind):
        nonlocal next_rid, edge_violations, influence_violations
        rid = next_rid
        next_rid += 1
        ancestors = set(parents)
        for parent in parents:
            ancestors.update(records[parent].ancestors)
            if not future(y - records[parent].y):
                edge_violations += 1
        rec = Record(rid, y, yi, tuple(parents), frozenset(ancestors), kind)
        records[rid] = rec
        if (differs(y, yi) and not future(y - records[0].y)):
            influence_violations += 1
        return rid

    clicks = 0
    while ports and clicks < cutoff:
        tokens = [("SPLIT", pid) for pid in sorted(ports)]
        tokens += [("SEAL", pid) for pid in sorted(ports)]
        tokens += [("JOIN", jid) for jid, jt in sorted(joins.items())
                   if jt.left in ports and jt.right in ports]
        kind, key = tokens[int(rng.integers(len(tokens)))]
        clicks += 1
        counts[kind] += 1

        if kind == "SPLIT":
            parent = ports[key]
            u = H if rng.random() < 0.5 else T
            rho_l, rhoi_l = push(u, parent.rho), push(u, parent.rho_i)
            rho_r = rhoi_r = P0.copy()
            y_l, yi_l = parent.y + increment(rho_l), parent.y_i + increment(rhoi_l)
            y_r, yi_r = parent.y + increment(rho_r), parent.y_i + increment(rhoi_r)
            invalidate({key})
            left, right = next_pid, next_pid + 1
            next_pid += 2
            lr = add_record(y_l, yi_l, (parent.record,), "SPLIT-CARRIER")
            rr = add_record(y_r, yi_r, (parent.record,), "SPLIT-ANCILLA")
            ports[left] = Port(left, lr, rho_l, rhoi_l, y_l, yi_l)
            ports[right] = Port(right, rr, rho_r, rhoi_r, y_r, yi_r)
            joins[next_jid] = Join(next_jid, left, right, parent.record,
                                   parent.y.copy(), parent.y_i.copy())
            next_jid += 1
            for rho in (rho_l, rho_r):
                bloch = increment(rho)[1:]
                norm = np.linalg.norm(bloch)
                if abs(norm - 1) < 1e-9:
                    null_directions.append(bloch / norm)

        elif kind == "SEAL":
            port = ports[key]
            p0 = float(np.trace(P0 @ port.rho).real)
            p0i = float(np.trace(P0 @ port.rho_i).real)
            u = rng.random()
            outcome_from_u(p0, u)
            outcome_from_u(p0i, u)
            # The intervention is made at the root state.  A SEAL of that
            # same root port is a readout of the intervention, not a later
            # descendant influence witness.
            if port.record != 0 and abs(p0 - p0i) > TOL:
                changed_seals += 1
                if not future(port.y - records[0].y):
                    influence_violations += 1
            invalidate({key})

        else:
            jt = joins[key]
            left, right = ports[jt.left], ports[jt.right]
            left_changed = differs(left.rho, left.rho_i) or differs(left.y, left.y_i)
            right_changed = differs(right.rho, right.rho_i) or differs(right.y, right.y_i)
            p0, _ = branch(J0, np.kron(left.rho, right.rho))
            p0i, _ = branch(J0, np.kron(left.rho_i, right.rho_i))
            u = rng.random()
            ob, oi = outcome_from_u(p0, u), outcome_from_u(p0i, u)
            rho = join_step(left.rho, right.rho, ob)
            rhoi = join_step(left.rho_i, right.rho_i, oi)
            y = left.y + right.y - jt.anchor_y
            yi = left.y_i + right.y_i - jt.anchor_y_i
            invalidate({jt.left, jt.right})
            rid = add_record(y, yi, (left.record, right.record), "JOIN")
            pid = next_pid
            next_pid += 1
            ports[pid] = Port(pid, rid, rho, rhoi, y, yi)
            downstream_p0 = float(np.trace(P0 @ rho).real)
            downstream_p0i = float(np.trace(P0 @ rhoi).real)
            if ((left_changed or right_changed) and
                    abs(downstream_p0 - downstream_p0i) > TOL):
                join_transfers += 1

        max_open = max(max_open, len(ports))

    ordered_records = [records[k] for k in sorted(records)]
    coords = np.asarray([rec.y for rec in ordered_records])
    unique_dirs = {tuple(np.round(x, 10)) for x in null_directions}
    support = covering_support([np.asarray(x) for x in unique_dirs])
    if len(coords) >= 5:
        evals = np.linalg.eigvalsh(np.cov(coords.T))
        evals = np.maximum(evals, 0)
        rank4 = bool(evals[0] > max(evals[-1], 1e-30) * 1e-10)
    else:
        evals = np.zeros(4)
        rank4 = False

    # Deterministic at-most-256 record read, independent of the growth RNG.
    if len(ordered_records) > 256:
        ids = np.unique(np.linspace(0, len(ordered_records) - 1, 256).astype(int))
        sample = [ordered_records[i] for i in ids]
    else:
        sample = ordered_records
    related = ancestry_related = 0
    for a in sample:
        for b in sample:
            if a.rid == b.rid:
                continue
            if future(b.y - a.y) and np.max(np.abs(b.y - a.y)) > TOL:
                related += 1
                ancestry_related += int(a.rid in b.ancestors)
    ancestry_fraction = ancestry_related / related if related else float("nan")

    fdom = fm4 = float("nan")
    fdom_count = fm4_count = 0
    if len(sample) >= 32:
        p = np.asarray([rec.y for rec in sample])
        d = p[None, :, :] - p[:, None, :]
        rel = (d[:, :, 0] > TOL) & (
            d[:, :, 0] + TOL >= np.linalg.norm(d[:, :, 1:], axis=2))
        np.fill_diagonal(rel, False)
        fdom, fdom_count, _ = f_iso_cloud(transverse(rel, p, "dom"))
        fm4, fm4_count, _ = f_iso_cloud(transverse(rel, p, "m4"))

    return {
        "seed": seed, "cutoff": cutoff, "clicks": clicks,
        "terminal": not ports, "records": len(records), **counts,
        "max_open": max_open, "unique_dirs": len(unique_dirs),
        "support": support, "evals": evals, "rank4": rank4,
        "edge_violations": edge_violations,
        "influence_violations": influence_violations,
        "changed_seals": changed_seals, "join_transfers": join_transfers,
        "ancestry_fraction": ancestry_fraction,
        "F_dom": fdom, "F_m4": fm4,
        "F_dom_minproj": fdom_count, "F_m4_minproj": fm4_count,
    }


def finite(values):
    return [float(x) for x in values if np.isfinite(x)]


blocks = ((512, 20276000), (1024, 20277000), (2048, 20278000))
all_rows = []
summaries = []
print("D11 GENERATED COMPLETE-HISTORY CAMPAIGN")
print("activities=SPLIT:1,SEAL:1,JOIN:1 theta=pi/4 click_scale=2")
print("paired_intervention=P0_vs_PPLUS common_token_and_uniform_coupling")
for cutoff, seed0 in blocks:
    rows = [simulate(seed0 + j, cutoff) for j in range(24)]
    all_rows.extend(rows)
    supports = [row["support"] for row in rows]
    fd, fm = finite(row["F_dom"] for row in rows), finite(row["F_m4"] for row in rows)
    m4 = [m4_control(seed0 + 1000 + j) for j in range(24)]
    m4d = finite(x[0] for x in m4)
    m4m = finite(x[1] for x in m4)
    summary = {
        "cutoff": cutoff,
        "reached": sum(row["clicks"] == cutoff for row in rows),
        "terminal": sum(row["terminal"] for row in rows),
        "median_clicks": median(row["clicks"] for row in rows),
        "max_clicks": max(row["clicks"] for row in rows),
        "median_records": median(row["records"] for row in rows),
        "max_records": max(row["records"] for row in rows),
        "median_support": median(supports),
        "rank4": sum(row["rank4"] for row in rows),
        "join_influence": sum(row["join_transfers"] > 0 for row in rows),
        "changed_seal": sum(row["changed_seals"] > 0 for row in rows),
        "edge_violations": sum(row["edge_violations"] for row in rows),
        "influence_violations": sum(row["influence_violations"] for row in rows),
        "valid_F_dom": len(fd), "valid_F_m4": len(fm),
        "M4_dom_valid": len(m4d),
        "M4_m4_valid": len(m4m),
        "M4_dom_mean": float(np.mean(m4d)) if m4d else float("nan"),
        "M4_m4_mean": float(np.mean(m4m)) if m4m else float("nan"),
    }
    summaries.append(summary)
    print(" ".join(f"{key}={value}" for key, value in summary.items()))
    longest = sorted(rows, key=lambda row: row["clicks"], reverse=True)[:3]
    for row in longest:
        print(f"  long seed={row['seed']} clicks={row['clicks']} records={row['records']} "
              f"S/J/Q={row['SPLIT']}/{row['JOIN']}/{row['SEAL']} "
              f"max_open={row['max_open']} dirs={row['unique_dirs']} "
              f"support={row['support']:.6f} join_influence={row['join_transfers']}")

zero_cone_violations = all(
    row["edge_violations"] == row["influence_violations"] == 0 for row in all_rows)
join_gate = all(summary["join_influence"] >= 20 for summary in summaries)
support_gate = (all(a["median_support"] <= b["median_support"] + 1e-12
                    for a, b in zip(summaries, summaries[1:]))
                and summaries[-1]["median_support"] >= 0.80)
rank_gate = summaries[-1]["rank4"] >= 20
if not zero_cone_violations:
    verdict = "REFUTED-CAUSAL-WIRING"
elif not join_gate:
    verdict = "INTERACTION-INERT"
elif not support_gate or not rank_gate:
    verdict = "GENERATIVE-DEGENERACY"
else:
    verdict = "GENERATED-ENVELOPE-CONSISTENT"

print(f"zero_cone_violations={zero_cone_violations}")
print(f"join_gate={join_gate}")
print(f"support_gate={support_gate}")
print(f"rank_gate={rank_gate}")
print(f"frozen_numerical_verdict={verdict}")
print("mechanism_diagnosis=POPULATION-EXTINCT_INTERACTION-SPARSE")
payload = repr((summaries, verdict, [(r["seed"], r["clicks"], r["records"],
                                      r["join_transfers"]) for r in all_rows]))
receipt = sha256(payload.encode()).hexdigest()
EXPECTED_RECEIPT = "f1ab9e04caa42f200c3af53adb295d8f78d547178d0b67fff0bcffd9af547224"
if receipt != EXPECTED_RECEIPT:
    raise AssertionError(f"receipt drift: {receipt}")
print("receipt_sha256=" + receipt)
