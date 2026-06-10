#!/usr/bin/env python3
"""
v6_p8a: Triangle Law at general n (Paper 8, items 1-2).

Apparatus: a ledger = a set S of distinct nontrivial parity characters on n
spins (masks in F2^n \ {0}).  Relation code K = kernel of F2^S -> F2^n.
Z / prod cosh(h_a) = W_K(t) = sum_{c in K} prod_{a in supp(c)} t_a,
t_a = tanh h_a  (exact character-expansion identity).

Theorems tested/used:
  T1 (code invariance): defect depends only on K as a subset structure.
  T2 (component decomposition): defect adds over coordinate-disjoint code
      components; free modes contribute zero.
  T3 (single relation, 1D reduction): a single weight-w relation reduces to
      the scalar fixed point  t + (1-t^2) t^{w-1}/(1+t^w) = e^{-h}.
First-order theory: per-codeword contribution theta^w (1 - w*kappa),
      kappa = eta*s/(s+theta), s = 1-theta^2.
Main test: T2 + known values PREDICT a Triangle-Law violation at n=5
      (disjoint triangle + 4-relation: +0.008438105 - 0.016839124 < 0).
"""
import numpy as np, itertools, time
from scipy.optimize import brentq

# ---------- constants ----------
eta = brentq(lambda e: np.tanh(e) - np.exp(-e), 0.1, 2.0)
theta = np.tanh(eta)
D1 = eta * theta - np.log(np.cosh(eta))
s = 1.0 - theta**2
kappa = eta * s / (s + theta)
print("== constants ==")
print(f"eta_hist = {eta:.15f}  theta_hist = {theta:.15f}")
print(f"D1 = m_hat(P1) = {D1:.15f}")
print(f"kappa = eta(1-th^2)/(1-th^2+th) = {kappa:.15f}   3*kappa = {3*kappa:.15f}")
print(f"first-order sign boundary 1/kappa = {1/kappa:.15f}  (w=3 is marginal)\n")

STATES = {n: np.array(list(itertools.product((-1, 1), repeat=n)), float)
          for n in range(2, 8)}
CHARS = {}
def char_cols(n):
    if n not in CHARS:
        st = STATES[n]
        cols = np.empty((st.shape[0], 1 << n))
        for mask in range(1 << n):
            idx = [i for i in range(n) if (mask >> i) & 1]
            cols[:, mask] = np.prod(st[:, idx], axis=1) if idx else 1.0
        CHARS[n] = cols
    return CHARS[n]

def solve_ledger(masks, n, signs=None, tol=1e-13):
    cols = char_cols(n)
    chi = cols[:, list(masks)].copy()
    if signs is not None:
        chi *= np.asarray(signs, float)[None, :]
    m = chi.shape[1]
    h = np.full(m, eta)
    for _ in range(200):
        z = chi @ h; z -= z.max()
        w = np.exp(z); p = w / w.sum()
        E = chi.T @ p
        F = E - np.exp(-h)
        r = np.abs(F).max()
        if r < tol:
            break
        Cov = (chi * p[:, None]).T @ chi - np.outer(E, E)
        J = Cov + np.diag(np.exp(-h))
        step = np.linalg.solve(J, F)
        lam = 1.0
        while lam > 1e-6:
            h2 = h - lam * step
            z2 = chi @ h2; z2 -= z2.max()
            w2 = np.exp(z2); p2 = w2 / w2.sum()
            if np.abs(chi.T @ p2 - np.exp(-h2)).max() < r:
                break
            lam *= 0.5
        h = h - lam * step
    z = chi @ h; zm = z.max()
    w = np.exp(z - zm); Z = w.sum()
    psi = zm + np.log(Z / len(w))
    E = chi.T @ (w / Z)
    D = h @ E - psi
    res = np.abs(E - np.exp(-h)).max()
    return h, D, res

def defect(masks, n, signs=None):
    h, D, res = solve_ledger(masks, n, signs)
    return len(masks) * D1 - D, D, res

# ---------- F2 code utilities ----------
def f2_rank(vecs):
    piv = {}
    r = 0
    for v in vecs:
        cur = v
        while cur:
            hb = cur.bit_length() - 1
            if hb in piv:
                cur ^= piv[hb]
            else:
                piv[hb] = cur; r += 1; break
    return r

def relation_basis(masks):
    """nullspace basis as combination-masks over S (index bitmasks)."""
    piv = {}
    null = []
    for i, vec in enumerate(masks):
        v, c = vec, 1 << i
        while v:
            hb = v.bit_length() - 1
            if hb in piv:
                pv, pc = piv[hb]; v ^= pv; c ^= pc
            else:
                piv[hb] = (v, c); break
        else:
            null.append(c)
    return null

def code_words(masks):
    nb = relation_basis(masks)
    words = set()
    for sel in range(1, 1 << len(nb)):
        w = 0
        for j in range(len(nb)):
            if (sel >> j) & 1:
                w ^= nb[j]
        words.add(w)
    return words  # nonzero codewords as index-bitmasks

def has_triangle(masks):
    S = set(masks)
    ml = list(masks)
    for i in range(len(ml)):
        for j in range(i + 1, len(ml)):
            x = ml[i] ^ ml[j]
            if x in S and x != ml[i] and x != ml[j]:
                return True
    return False

def components(masks):
    """indecomposable code components: partition of mode indices touched by
    codewords, joined by shared support; returns list of index-bitmasks."""
    words = code_words(masks)
    comps = []
    for w in words:
        merged = w
        keep = []
        for c in comps:
            if c & merged:
                merged |= c
            else:
                keep.append(c)
        keep.append(merged)
        comps = keep
    return comps, words

def weight_profile(words):
    from collections import Counter
    return tuple(sorted(Counter(bin(w).count('1') for w in words).items()))

# ---------- A. reproduce Paper 7 anchor values ----------
print("== A. anchor values (must match Papers 6.3-6.4) ==")
anchors = [
    ("triangle {x,y,xy}",            [1, 2, 3], 2, 0.008438105),
    ("{x,y,z,xyz} single w4",        [1, 2, 4, 7], 3, -0.016839124),
    ("3-spin pairwise (6 modes)",    [1, 2, 4, 3, 5, 6], 3, 0.060894615),
    ("3-spin full (7 modes)",        [1, 2, 4, 3, 5, 6, 7], 3, 0.120139065),
    ("{x,y,z,w,xyzw} single w5",     [1, 2, 4, 8, 15], 4, -0.023567124),
    ("plaquette {xy,yz,zw,wx}",      [3, 6, 12, 9], 4, -0.016839124),
]
for name, masks, n, ref in anchors:
    d, D, res = defect(masks, n)
    print(f"  {name:32s} defect = {d:+.12f}  (ref {ref:+.9f})  res={res:.1e}")

# ---------- B. v6.4 probe forensics + decomposition ----------
print("\n== B. decomposition theorem and v6.4 probe forensics ==")
d_tri, _, _ = defect([1, 2, 3], 2)
d_w4, _, _ = defect([1, 2, 4, 7], 3)
d_w5, _, _ = defect([1, 2, 4, 8, 15], 4)

# true 'triangle + free pair' {x,y,xy,z,w} on 4 spins
d1, _, r1 = defect([1, 2, 3, 4, 8], 4)
print(f"  {{x,y,xy,z,w}} (triangle + two FREE modes):   {d1:+.12f}"
      f"   [decomposition predicts {d_tri:+.12f}]  gap={abs(d1-d_tri):.2e}")
# two disjoint triangles on 4 spins
d2, _, r2 = defect([1, 2, 3, 4, 8, 12], 4)
print(f"  {{x,y,xy}}+{{z,w,zw}} (two disjoint triangles): {d2:+.12f}"
      f"   [2 x triangle = {2*d_tri:+.12f}]  gap={abs(d2-2*d_tri):.2e}"
      f"   [v6.4 printed +0.016876309 labeled 'triangle + free pair']")
# v6.4 'triangle + 4-relation' probe {x,y,xy,xyzw,zw}
masks_p = [1, 2, 3, 15, 12]
cw = code_words(masks_p)
print(f"  {{x,y,xy,xyzw,zw}} code weights = {sorted(bin(w).count('1') for w in cw)}"
      f"  -> contains TWO triangles ({{x,y,xy}} and {{xy,zw,xyzw}}), one w4 word;")
d3, _, _ = defect(masks_p, 4)
print(f"     defect = {d3:+.12f}   [v6.4 printed +0.020844986 labeled 'triangle + 4-relation']")

# ---------- C. THE REFUTATION TEST at n=5 ----------
print("\n== C. disjoint triangle (+) and single w4 relation (-) at n=5 ==")
masks_star = [1, 2, 3, 4, 8, 16, 28]   # {x,y,xy} on spins 0,1 ; {z,w,u,zwu} on 2,3,4
cw = code_words(masks_star)
print(f"  S* = {{x,y,xy, z,w,u,zwu}}: m=7, code weights {sorted(bin(w).count('1') for w in cw)},"
      f" contains a triangle: {has_triangle(masks_star)}")
d_star, D_star, res_star = defect(masks_star, 5)
pred = d_tri + d_w4
print(f"  defect(S*) = {d_star:+.12f}   decomposition prediction = {pred:+.12f}"
      f"   gap = {abs(d_star-pred):.2e}   res = {res_star:.1e}")
print(f"  VERDICT: contains a triangle yet defect "
      f"{'< 0  -> GLOBAL TRIANGLE LAW REFUTED' if d_star < 0 else '>= 0 -> law survives'}")
# disjoint triangle + w5 at n=6
masks_star2 = [1, 2, 3] + [4, 8, 16, 32, 60]
d_star2, _, res2 = defect(masks_star2, 6)
print(f"  triangle + disjoint w5 (n=6, m=8): defect = {d_star2:+.12f}"
      f"   [prediction {d_tri + d_w5:+.12f}]  res={res2:.1e}")

# ---------- D. single-relation exact theory (all w), mpmath ----------
print("\n== D. single-relation defect(w), 40-digit fixed point ==")
from mpmath import mp, mpf, tanh as mtanh, cosh as mcosh, log as mlog, exp as mexp, findroot
mp.dps = 40
eta_m = findroot(lambda e: mtanh(e) - mexp(-e), mpf("0.6"))
th_m = mtanh(eta_m)
D1_m = eta_m * th_m - mlog(mcosh(eta_m))
s_m = 1 - th_m**2
kap_m = eta_m * s_m / (s_m + th_m)
def defect_single(wn):
    f = lambda h: mtanh(h) + (1 - mtanh(h)**2) * mtanh(h)**(wn - 1) / (1 + mtanh(h)**wn) - mexp(-h)
    h = findroot(f, eta_m)
    t = mtanh(h)
    psi = wn * mlog(mcosh(h)) + mlog(1 + t**wn)
    D = wn * h * mexp(-h) - psi
    return wn * D1_m - D, h
print("   w   defect(w)              first-order theta^w(1-w*kappa)   ratio")
worst_ratio_dev = 0.0
for wn in list(range(3, 13)) + [16, 20, 24, 30]:
    d, h = defect_single(wn)
    fo = th_m**wn * (1 - wn * kap_m)
    ratio = float(d / fo)
    if wn >= 16:
        worst_ratio_dev = max(worst_ratio_dev, abs(ratio - 1))
    print(f"  {wn:3d}  {float(d):+.15f}   {float(fo):+.15f}   {ratio:+.6f}")
print(f"  sign(defect): w=3 POSITIVE; w>=4 NEGATIVE for all computed w;"
      f" |defect| max at w=5; asymptotic ratio->1 (dev at w>=16: {worst_ratio_dev:.3f})")
print(f"  NOTE first-order coefficient at w=3 is NEGATIVE ({float(th_m**3*(1-3*kap_m)):+.6f}):"
      f" triangle binding is a second-order effect (3*kappa-1 = {float(3*kap_m-1):+.6f}).")

# ---------- E. exhaustive n=4 ----------
print("\n== E. exhaustive scan: all 32767 statistic sets on 4 spins ==")
t0 = time.time()
all_masks = list(range(1, 16))
results = {}
counts = {"free": 0, "tri": 0, "anti": 0}
viol_tri_anti = []   # triangle present, defect < 0
viol_notri_bind = [] # relations, no triangle, defect > 0
max_free_abs = 0.0
min_tri = (1e9, None)
max_anti = (-1e9, None)
comp_gap_max = 0.0
comp_cache = {}
conn_viol_tri = {}   # frozenset -> defect (connected components violating)
conn_viol_notri = {}
profile_map = {}     # weight profile -> set of rounded CONNECTED defects
n_sets = 0
for sel in range(1, 1 << 15):
    masks = [all_masks[i] for i in range(15) if (sel >> i) & 1]
    m = len(masks)
    rank = f2_rank(masks)
    d, D, res = defect(masks, 4)
    results[sel] = d
    n_sets += 1
    if rank == m:
        counts["free"] += 1
        max_free_abs = max(max_free_abs, abs(d))
        continue
    tri = has_triangle(masks)
    if tri:
        counts["tri"] += 1
        if d < min_tri[0]:
            min_tri = (d, masks)
        if d <= -1e-9:
            viol_tri_anti.append((masks, d))
    else:
        counts["anti"] += 1
        if d > max_anti[0]:
            max_anti = (d, masks)
        if d >= 1e-9:
            viol_notri_bind.append((masks, d))
    # full component analysis
    comps, words = components(masks)
    dsum = 0.0
    for cmask in comps:
        sub = tuple(sorted(masks[i] for i in range(m) if (cmask >> i) & 1))
        if sub in comp_cache:
            dc, sub_words = comp_cache[sub]
        else:
            dc, _, _ = defect(list(sub), 4)
            sub_words = code_words(list(sub))
            comp_cache[sub] = (dc, sub_words)
            prof = weight_profile(sub_words)
            profile_map.setdefault(prof, set()).add(round(dc, 9))
            subtri = has_triangle(list(sub))
            if subtri and dc <= -1e-9:
                conn_viol_tri[sub] = dc
            if (not subtri) and dc >= 1e-9:
                conn_viol_notri[sub] = dc
        dsum += dc
    comp_gap_max = max(comp_gap_max, abs(d - dsum))
print(f"  scanned {n_sets} sets in {time.time()-t0:.1f}s")
print(f"  relation-free: {counts['free']}  (max |defect| = {max_free_abs:.2e}; theorem: 0)")
print(f"  triangle-bearing: {counts['tri']}   min defect = {min_tri[0]:+.12f}  at masks {min_tri[1]}")
print(f"  relations-no-triangle: {counts['anti']}   max defect = {max_anti[0]:+.12f}  at masks {max_anti[1]}")
print(f"  GLOBAL law violations: triangle-but-antibinds = {len(viol_tri_anti)},"
      f" no-triangle-but-binds = {len(viol_notri_bind)}")
print(f"  component-additivity max gap (ALL sets): {comp_gap_max:.2e}")
print(f"  CONNECTED (indecomposable) violating codes: triangle-anti = {len(conn_viol_tri)},"
      f" no-tri-bind = {len(conn_viol_notri)}")
def smallest(d):
    return min(d.items(), key=lambda kv: (len(kv[0]), kv[0]))
if conn_viol_tri:
    sub, dc = smallest(conn_viol_tri)
    ws = sorted(bin(w).count('1') for w in code_words(list(sub)))
    print(f"    minimal connected triangle-anti example: masks {list(sub)} m={len(sub)}"
          f" code weights {ws} defect = {dc:+.12f}")
if conn_viol_notri:
    sub, dc = smallest(conn_viol_notri)
    ws = sorted(bin(w).count('1') for w in code_words(list(sub)))
    print(f"    minimal connected no-tri-bind example:   masks {list(sub)} m={len(sub)}"
          f" code weights {ws} defect = {dc:+.12f}")

# is defect a function of the code weight enumerator?
multi = {p: v for p, v in profile_map.items() if len(v) > 1}
print(f"\n  distinct connected codes solved: {len(comp_cache)}")
print(f"  weight-enumerator classes among connected components: {len(profile_map)};"
      f" classes with MULTIPLE defect values: {len(multi)}")
print("  connected-class table (enumerator -> defect):")
rows = sorted(((p, sorted(v)[0]) for p, v in profile_map.items()),
              key=lambda r: (sum(c for _, c in r[0]), r[0]))
for p, dval in rows:
    pe = ",".join(f"{w}^{c}" if c > 1 else f"{w}" for w, c in p)
    print(f"    [{pe:30s}]  defect = {dval:+.9f}")
if multi:
    p, v = min(multi.items(), key=lambda kv: sum(w * c for w, c in kv[0]))
    sv = sorted(v)
    sign_split = sum(1 for p2, v2 in multi.items()
                     if min(v2) < -1e-9 and max(v2) > 1e-9)
    print(f"    example: profile {p} -> defect values {sv[:4]}{'...' if len(sv)>4 else ''}")
    print(f"    enumerator classes containing BOTH signs: {sign_split}")
    print("    => the defect is a CODE-GEOMETRY invariant, strictly finer than the weight enumerator")

# monotone-above-triangle test using stored exhaustive defects
print("\n  monotonicity of defect under adding one mode to a triangle-bearing set:")
inc_min_tri = 1e9; dec_cases = 0; tested = 0
for sel in range(1, 1 << 15):
    masks = [all_masks[i] for i in range(15) if (sel >> i) & 1]
    if not has_triangle(masks):
        continue
    d0 = results[sel]
    for i in range(15):
        if (sel >> i) & 1:
            continue
        d1x = results[sel | (1 << i)]
        tested += 1
        if d1x - d0 < inc_min_tri:
            inc_min_tri = d1x - d0
        if d1x < d0 - 1e-9:
            dec_cases += 1
print(f"    extensions tested: {tested}; min increment = {inc_min_tri:+.3e};"
      f" strict decreases: {dec_cases}  -> monotone-above-triangle conjecture"
      f" {'REFUTED' if dec_cases else 'holds'}")

# ---------- F. n=5 structured + random ----------
print("\n== F. n=5 structured probes and random sample ==")
rng = np.random.default_rng(7)
viol5_global = 0; viol5_conn = 0; checked5 = 0; comp_gap5 = 0.0
t0 = time.time()
for trial in range(1200):
    m = rng.integers(3, 11)
    masks = list(rng.choice(np.arange(1, 32), size=m, replace=False))
    masks = [int(x) for x in masks]
    if f2_rank(masks) == len(masks):
        continue
    d, D, res = defect(masks, 5)
    comps, words = components(masks)
    dsum = 0.0
    ok = True
    for cmask in comps:
        sub = [masks[i] for i in range(len(masks)) if (cmask >> i) & 1]
        dc, _, _ = defect(sub, 5)
        dsum += dc
        subtri = has_triangle(sub)
        if subtri and dc <= -1e-9:
            viol5_conn += 1; ok = False
        if (not subtri) and dc >= 1e-9:
            viol5_conn += 1; ok = False
    comp_gap5 = max(comp_gap5, abs(d - dsum))
    tri = has_triangle(masks)
    if (tri and d <= -1e-9) or ((not tri) and len(words) > 0 and d >= 1e-9):
        viol5_global += 1
    checked5 += 1
print(f"  random relation-carrying sets checked: {checked5} ({time.time()-t0:.1f}s)")
print(f"  component-additivity max gap: {comp_gap5:.2e}")
print(f"  GLOBAL-law violations: {viol5_global}   CONNECTED-law violations: {viol5_conn}")

# ---------- F2. classification robustness and near-cancellation ----------
print("\n== F2. sign-classification robustness ==")
nonzero_cls = [abs(sorted(v)[0]) for p, v in profile_map.items()
               if abs(sorted(v)[0]) > 1e-9]
print(f"  min |defect| over relation-carrying CONNECTED classes at n<=4: "
      f"{min(nonzero_cls):.12f}")
print(f"  (six orders above the 1e-9 classification threshold and the 1e-13")
print(f"   solver residual: the n=4 exhaustive classification is robust.)")
# but TOTAL defects of decomposable sets can nearly cancel: smallest such
# composite is two disjoint triangles + one disjoint w4 relation (n=7):
masks7 = [1, 2, 3, 4, 8, 12, 16, 32, 64, 112]
d7, D7, r7 = defect(masks7, 7)
pred7 = 2 * d_tri + d_w4
print(f"  near-cancellation composite (2 triangles + w4, n=7, m=10):")
print(f"    defect = {d7:+.12f}   prediction 2*tri + w4 = {pred7:+.12f}"
      f"   gap = {abs(d7-pred7):.1e}   res = {r7:.1e}")
print(f"  -> TOTAL defects of decomposable ledgers approach zero (here +3.7e-5);")
print(f"     sign classification is only meaningful PER COMPONENT - one more")
print(f"     reason the component law, not any global sign rule, is the physics.")

# ---------- G. triangle-rich families: binding density ----------
print("\n== G. families: binding density (item 2 / stable species) ==")
fams = []
for n in (3, 4, 5):
    masks = list(range(1, 1 << n))
    d, D, res = defect(masks, n)
    fams.append((f"full set n={n} (m={len(masks)})", d, len(masks), res))
for n in (3, 4, 5):
    singles = [1 << i for i in range(n)]
    pairs = [(1 << i) | (1 << j) for i in range(n) for j in range(i + 1, n)]
    masks = singles + pairs
    d, D, res = defect(masks, n)
    fams.append((f"singles+pairs n={n} (m={len(masks)})", d, len(masks), res))
for n in (4, 5):
    pairs = [(1 << i) | (1 << j) for i in range(n) for j in range(i + 1, n)]
    d, D, res = defect(pairs, n)
    fams.append((f"pairs-only (Curie-Weiss-type) n={n} (m={len(pairs)})", d, len(pairs), res))
print(f"  {'family':44s} {'defect':>14s} {'defect/mode':>13s}")
for name, d, m, res in fams:
    print(f"  {name:44s} {d:+13.9f} {d/m:+12.9f}   res={res:.0e}")
print("\n== p8a done ==")
