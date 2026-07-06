#!/usr/bin/env python3
"""
u4b_ensemble_gate.py — v9 round 11: THE CALIBRATED ENSEMBLE GATE
(note-u4b; gates pinned there pre-run; known values disclosed in-note).

All TVs exact (Fractions). G-1 separation at n = 7: TV(corner, box) <
TV(m_L-restricted-to-dim<=2, box)/3 AND < TV(atoms, box)/10. G-2 n-trend
5/6/7 (registered: mild rise, REFUSED only on a > 2x step). G-3 L-sweep
L in {2,4,8,16} at n = 6 (registered: monotone non-decreasing, L = 2 the
minimum; any strict decrease refuses). G-4 integrity (mass = 1; the
m_L-restricted mapping verified classifier-free). Exit 1 by design on
any refusal. Machinery: the u4a-validated core + the #58-repaired file.
"""
import sys, os, time
import numpy as np
from fractions import Fraction
from itertools import permutations, product

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "v8", "code"))
from pE_phase_causalset import poset_structure, is_kr_type, order_dim_le_2  # noqa

rng = np.random.default_rng(20260718)
M, L = 32, 2
ATOMS = [Fraction(156109200157240, 10**15), Fraction(109004107833, 10**12),
         Fraction(63376134128, 10**12)]
PASS = 0
FAIL = 0

def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

# ---------------- canonical forms: brute (n <= 5 gate) + refinement-fast
def canon_brute(Cm, n):
    best = None
    for perm in permutations(range(n)):
        bits = tuple(Cm[perm[i]][perm[j]] for i in range(n) for j in range(n))
        if best is None or bits < best:
            best = bits
    return best

_canon_cache = {}
def canon_fast(Cm, n):
    raw = tuple(tuple(row) for row in Cm)
    hit = _canon_cache.get(raw)
    if hit is not None:
        return hit
    inv = [(sum(Cm[i]), sum(Cm[j][i] for j in range(n))) for i in range(n)]
    for _ in range(n):
        nxt = []
        for i in range(n):
            preds = tuple(sorted(inv[j] for j in range(n) if Cm[j][i]))
            succs = tuple(sorted(inv[j] for j in range(n) if Cm[i][j]))
            nxt.append(hash((inv[i], preds, succs)))
        if nxt == inv: break
        inv = nxt
    order = sorted(range(n), key=lambda i: (inv[i], ))
    groups = []
    for i in order:
        if groups and inv[groups[-1][-1]] == inv[i]: groups[-1].append(i)
        else: groups.append([i])
    best = None
    for perm_parts in product(*[permutations(g) for g in groups]):
        perm = [v for part in perm_parts for v in part]
        bits = tuple(Cm[perm[i]][perm[j]] for i in range(n) for j in range(n))
        if best is None or bits < best:
            best = bits
    _canon_cache[raw] = best
    return best

def rel_of(bits, n):
    """Relabel by a LINEAR EXTENSION first: pE's poset_structure computes
    height by a single forward pass, valid only on natural labelings —
    feeding it canonical (hash-ordered) labels produced wrong heights/KR
    flags on 719/1956 classes at n = 7 (round-10 review MAJOR-1; the
    review's counterexample: the 7-chain flagged KR-type). This wrapper
    restores the classifier's input contract."""
    Cm = [[bits[i * n + j] for j in range(n)] for i in range(n)]
    indeg = [sum(Cm[j][i] for j in range(n)) for i in range(n)]
    order = []
    used = [False] * n
    for _ in range(n):
        v = min(i for i in range(n) if not used[i]
                and all(used[j] or not Cm[j][i] for j in range(n)))
        used[v] = True; order.append(v)
    pos = {v: k for k, v in enumerate(order)}
    return frozenset((pos[i], pos[j]) for i in range(n) for j in range(n)
                     if Cm[i][j])

# ---------------- the u4a-validated race-model core
def rgs_patterns(n):
    out = []
    def rec(seq, u, p):
        if len(seq) == n:
            out.append((tuple(seq), p)); return
        for s in range(u):
            rec(seq + [s], u, p * Fraction(1, M))
        rec(seq + [u], u + 1, p * Fraction(M - u, M))
    rec([], 0, Fraction(1))
    return out

def life_partition(slots, resets):
    n = len(slots); life_of = [None] * n; cur = {}; nxt = 0
    for t in range(n):
        s = slots[t]
        if s not in cur: cur[s] = nxt; nxt += 1
        life_of[t] = cur[s]
        if resets[t]: del cur[s]
    return tuple(life_of)

def lp_law(n, Lval):
    pr = Fraction(1, Lval); qr = 1 - pr
    acc = {}
    for slots, ps in rgs_patterns(n):
        for resets in product((0, 1), repeat=n):
            p = ps
            for r in resets: p *= pr if r else qr
            lp = life_partition(slots, resets)
            acc[lp] = acc.get(lp, Fraction(0)) + p
    return acc

def interleavings(life_of):
    n = len(life_of); lives = {}
    for t, l in enumerate(life_of): lives.setdefault(l, []).append(t)
    out = []
    def rec(pos, ranks, pending, p):
        live = [l for l in pending if pending[l]]
        if pos == n: out.append((tuple(ranks), p)); return
        k = len(live)
        for l in live:
            t = pending[l][0]
            r2 = list(ranks); r2[t] = pos
            p2 = dict(pending); p2[l] = pending[l][1:]
            rec(pos + 1, r2, p2, p * Fraction(1, k))
    rec(0, [None] * n, {l: v[:] for l, v in lives.items()}, Fraction(1))
    return out

def order_from_ranks(ranks):
    n = len(ranks)
    return [[1 if (i < j and ranks[i] < ranks[j]) else 0 for j in range(n)]
            for i in range(n)]

def corner_measure(n, Lval, canon):
    meas = {}
    for lp, plp in lp_law(n, Lval).items():
        for ranks, pi in interleavings(lp):
            key = canon(order_from_ranks(ranks), n)
            meas[key] = meas.get(key, Fraction(0)) + plp * pi
    return meas

def atoms_measure(n, Lval):
    meas = {}
    third = Fraction(1, 3)
    for lp, plp in lp_law(n, Lval).items():
        lives = {}
        for t, l in enumerate(lp): lives.setdefault(l, []).append(t)
        for seq in product((0, 1, 2), repeat=n):
            chi = [None] * n
            for l, ts in lives.items():
                s = Fraction(0)
                for t in ts:
                    s += ATOMS[seq[t]]; chi[t] = s
            Cm = [[1 if (i < j and chi[i] < chi[j]) else 0 for j in range(n)]
                  for i in range(n)]
            key = canon_fast(Cm, n)
            meas[key] = meas.get(key, Fraction(0)) + plp * third ** n
    return meas


from pE_phase_causalset import process_n  # noqa  (classifier-free use: lab_mult only)

def tv(a, b):
    keys = set(a) | set(b)
    return sum(abs(a.get(k, Fraction(0)) - b.get(k, Fraction(0))) for k in keys) / 2

def kr_free_box(n):
    return corner_measure(n, 1, canon_fast)

print("[u4b calibrated ensemble gate — exact TVs on the validated core]")
t0 = time.time()

# measures
CORNER = {n: corner_measure(n, L, canon_fast) for n in (5, 6, 7)}
BOX = {n: kr_free_box(n) for n in (5, 6, 7)}
for n in (5, 6, 7):
    check(f"G-4 (mass, n = {n}): corner and box measures sum to exactly 1",
          sum(CORNER[n].values()) == 1 and sum(BOX[n].values()) == 1)

# m_L restricted to dim <= 2 (classifier-free: lab_mult through canon_fast keys)
classes7 = process_n(7, want_aut=True)
A001035_7 = 6129859
wL = {}
for c in classes7:
    Cm = [[0] * 7 for _ in range(7)]
    for (i, j) in c.rel: Cm[i][j] = 1
    key = canon_fast(Cm, 7)
    wL[key] = wL.get(key, Fraction(0)) + Fraction(c.lab_mult)
sup7 = set(CORNER[7])
wL_res = {k: v for k, v in wL.items() if k in sup7}
tot_res = sum(wL_res.values())
mL7 = {k: v / tot_res for k, v in wL_res.items()}
check("G-4 (the m_L-restricted mapping, classifier-free): pE classes map "
      "1-1 onto canon keys; the restricted support = the corner's 1956 "
      "(asserted, round-11 review NIT-10); total m_L mass = A001035(7); "
      "the restricted share EQUALS paper 7's geo share as an exact "
      "Fraction (5844259/6129859 — asserted, not just printed)",
      len(wL) == 2045 and len(wL_res) == 1956 and len(sup7) == 1956
      and sum(wL.values()) == A001035_7 and sum(mL7.values()) == 1
      and tot_res == Fraction(5844259, 6129859) * A001035_7,
      f"restricted share of labeled mass = {float(tot_res)/A001035_7:.4f}")

tv_cb7 = tv(CORNER[7], BOX[7])
tv_mb7 = tv(mL7, BOX[7])
ATOMS_M = {7: atoms_measure(7, L)}
tv_ab7 = tv(ATOMS_M[7], BOX[7])
print(f"      n = 7 exact TVs: corner-box {float(tv_cb7):.4f}; "
      f"counting(m_L, dim<=2)-box {float(tv_mb7):.4f}; atoms-box {float(tv_ab7):.4f}")
check("G-1 (separation, the headline): TV(corner, box) < TV(m_L-restricted, "
      "box)/3 AND < TV(atoms, box)/10 — the builder is history-weighted "
      "toward the target, not merely legal-shaped",
      tv_cb7 < tv_mb7 / 3 and tv_cb7 < tv_ab7 / 10,
      f"{float(tv_cb7):.4f} vs {float(tv_mb7)/3:.4f} and {float(tv_ab7)/10:.4f}")

tvs = {n: tv(CORNER[n], BOX[n]) for n in (5, 6, 7)}
print(f"      G-2 n-trend (exact): TV(5) = {float(tvs[5]):.4f}, "
      f"TV(6) = {float(tvs[6]):.4f}, TV(7) = {float(tvs[7]):.4f}")
runaway = (tvs[6] > 2 * tvs[5]) or (tvs[7] > 2 * tvs[6])
check("G-2 (the n-trend): mild rise registered (pre-washout regime "
      "n << L*M = 64); REFUSED only on a > 2x step (runaway)",
      not runaway,
      "held-as-expected" if tvs[5] <= tvs[6] <= tvs[7] else "non-monotone, within band")

lsweep = {}
for Lv in (2, 4, 8, 16):
    lsweep[Lv] = tv(corner_measure(6, Lv, canon_fast), BOX[6])
print("      G-3 L-sweep at n = 6 (exact): " +
      "  ".join(f"L={Lv}: {float(t):.4f}" for Lv, t in sorted(lsweep.items())))
mono = all(lsweep[a] <= lsweep[b] for a, b in ((2, 4), (4, 8), (8, 16)))
lmin = all(lsweep[2] <= lsweep[Lv] for Lv in (4, 8, 16))
check("G-3 (the L-sweep): TV monotone non-decreasing in L with L = 2 the "
      "minimum (paper 16's renewal law at census scale; registered "
      "prediction)", mono and lmin,
      "monotone" if mono else "NON-monotone")

print()
print(f"PRE-REGISTERED GATE LEDGER: G-1 {'HELD' if tv_cb7 < tv_mb7/3 and tv_cb7 < tv_ab7/10 else 'REFUSED'}; "
      f"G-2 {'REFUSED (runaway)' if runaway else 'HELD'}; "
      f"G-3 {'HELD' if mono and lmin else 'REFUSED'}; "
      f"G-4 {'HELD' if FAIL == 0 else 'see check lines'}  "
      f"[{time.time()-t0:.0f}s]")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
