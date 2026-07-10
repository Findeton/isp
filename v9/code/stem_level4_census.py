#!/usr/bin/env python3
"""
stem_level4_census.py — v9 round 39: the level-4 covtree census
(note-stem-level4; pin committed strictly before this file ran).

Gates G1-G6 per the pin. Soundness architecture: every machine state is
reached by literal growth moves (caps only forget boundary structure),
and G5 replays every census node's path into a concrete causet whose
signature is recomputed from scratch by an independent code path.
Exit 1 on any refusal.
"""
import itertools, sys, time
from collections import deque

T0 = time.time()
def log(msg):
    print(f"  [{time.time()-T0:7.1f}s] {msg}", flush=True)

PASS = FAIL = 0
def gate(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""), flush=True)

# ---------------- stem type ids (memoized canonical forms) ----------------
_canon_memo = {}
def typeid(rel, k):
    """Canonical id of a poset on k labeled elements 0..k-1 with strict
    relation set rel (frozenset of pairs). Returns a global bit index:
    sizes 2,3,4 -> bits; size-1 ignored by callers."""
    key = (k, rel)
    v = _canon_memo.get(key)
    if v is not None:
        return v
    best = None
    for p in itertools.permutations(range(k)):
        r = tuple(sorted((p[a], p[b]) for (a, b) in rel))
        if best is None or r < best:
            best = r
    v = _register_type(k, best)
    _canon_memo[key] = v
    return v

_type_registry = {}
_type_names = {}
def _register_type(k, canon_rel):
    key = (k, canon_rel)
    if key not in _type_registry:
        if k == 2: base, cap = 0, 2
        elif k == 3: base, cap = 2, 5
        elif k == 4: base, cap = 7, 16
        else: raise ValueError(k)
        idx = base + sum(1 for (kk, _) in _type_registry if kk == k)
        assert idx < base + cap
        _type_registry[key] = idx
        _type_names[idx] = f"P{k}[" + ",".join(f"{a}<{b}" for a, b in canon_rel) + "]"
    return _type_registry[key]

def sig4_part(sig):  # bits 7..22
    return sig >> 7
def sig_split(sig):
    return sig & 0b11, (sig >> 2) & 0b11111, sig >> 7

# ---------------- shared bundle logic (concrete causets) ----------------
def downsets_le3(pasts):
    """All down-sets of size <= 3 of a causet given as tuple of past-masks.
    Returns list of (mask, size)."""
    m = len(pasts)
    out = []
    idx = list(range(m))
    small = [i for i in idx if bin(pasts[i]).count("1") <= 2]
    for r in (1, 2, 3):
        for comb in itertools.combinations(small, r):
            mask = 0
            for i in comb: mask |= 1 << i
            if all(pasts[i] & ~mask == 0 for i in comb):
                out.append((mask, r))
    return out

def stem_bits(pasts, D_mask, D_size, P_mask):
    """Bit for the stem {x} + D with x above exactly P (P subset of D,
    both down-sets). Size D_size+1 in {2,3,4}."""
    els = [i for i in range(len(pasts)) if D_mask >> i & 1]
    loc = {v: t for t, v in enumerate(els)}
    k = D_size + 1
    rel = set()
    for b in els:
        pb = pasts[b]
        for a in els:
            if pb >> a & 1:
                rel.add((loc[a], loc[b]))
    xi = k - 1
    for a in els:
        if P_mask >> a & 1:
            rel.add((loc[a], xi))
    return 1 << typeid(frozenset(rel), k)

def bundle_of(pasts, ds3, P_mask):
    """Birth bundle: all new stems of sizes 2..4 created by adding an
    element above down-set P (|P| <= 3)."""
    bits = 0
    for (D_mask, D_size) in ds3:
        if P_mask & ~D_mask == 0:
            bits |= stem_bits(pasts, D_mask, D_size, P_mask)
    return bits

def sig_from_scratch(pasts):
    """Full signature (sizes 2..4) of a concrete causet — the independent
    verification path for G5: enumerate ALL down-sets of size 2..4."""
    m = len(pasts)
    sig = 0
    for r in (2, 3, 4):
        for comb in itertools.combinations(range(m), r):
            mask = 0
            for i in comb: mask |= 1 << i
            if all(pasts[i] & ~mask == 0 for i in comb):
                loc = {v: t for t, v in enumerate(comb)}
                rel = frozenset((loc[a], loc[b]) for b in comb for a in comb
                                if pasts[b] >> a & 1)
                sig |= 1 << typeid(rel, r)
    return sig

# ---------------- G1: brute anchor to n = 8 (incremental sigs) ----------------
EXPECT_COUNTS = {1: 1, 2: 2, 3: 3+4, 4: 40, 5: 357, 6: 4824, 7: 96428, 8: 2800472}
EXPECT_COUNTS[3] = 7
NB = 8
log("G1: brute stream to n = 8 begins")
brute_cum = {}      # n -> set of full sigs over causets of size <= n
cur = [((0,), 0)]   # (pasts, sig)
brute_cum[1] = set()
counts = {1: 1}
all_sigs_by_n = {1: {0}}
for n in range(2, NB + 1):
    nxt = []
    sigs_here = set()
    cnt = 0
    store = n < NB
    for (pasts, psig) in cur:
        m = len(pasts)
        ds3 = downsets_le3(pasts)
        # bundle cache for this parent, keyed by P_mask
        bcache = {}
        for Pm in range(1 << m):
            ok = True
            t = Pm
            while t:
                low = t & -t
                i = low.bit_length() - 1
                if pasts[i] & ~Pm:
                    ok = False; break
                t ^= low
            if not ok:
                continue
            pc = bin(Pm).count("1")
            if pc <= 3:
                b = bcache.get(Pm)
                if b is None:
                    b = bundle_of(pasts, ds3, Pm)
                    bcache[Pm] = b
                csig = psig | b
            else:
                csig = psig
            cnt += 1
            sigs_here.add(csig)
            if store:
                nxt.append((pasts + (Pm,), csig))
    counts[n] = cnt
    all_sigs_by_n[n] = sigs_here
    cur = nxt
    log(f"G1: n={n}: {cnt} labeled causets, {len(sigs_here)} distinct sigs at this size")
cum = set()
brute_cum_sets = {}
for n in range(1, NB + 1):
    cum |= all_sigs_by_n[n]
    brute_cum_sets[n] = set(cum)
ok_counts = all(counts[n] == EXPECT_COUNTS[n] for n in range(1, NB + 1))
gate("G1a: labeled counts 1/2/7/40/357/4824/96428/2800472 (A006455)",
     ok_counts, " ".join(f"n{n}:{counts[n]}" for n in range(1, NB + 1)))
cens4 = {n: {sig4_part(s) for s in brute_cum_sets[n] if sig4_part(s)} for n in range(1, NB + 1)}
mono = all(cens4[n] <= cens4[n + 1] for n in range(1, NB))
gate("G1b: cumulative exact-4 censuses printed, monotone", mono,
     "sizes " + " ".join(f"n{n}:{len(cens4[n])}" for n in range(4, NB + 1)))
cens3 = {n: set() for n in range(1, NB + 1)}
for n in range(1, NB + 1):
    cens3[n] = {sig_split(s)[1] for s in brute_cum_sets[n] if sig_split(s)[1]}
print(f"      brute exact-3 cumulative census sizes: "
      + " ".join(f"n{n}:{len(cens3[n])}" for n in range(3, NB + 1)))

# ---------------- the abstract interface machine ----------------
# Bstruct = (minimals, joins):
#   minimals: tuple of descs; desc = sorted tuple of child gcounts
#   joins: sorted tuple of (i, j) minimal-index pairs, i < j
def canon_B(minimals, joins, return_perm=False):
    k = len(minimals)
    best = None; bestp = None
    for p in itertools.permutations(range(k)):
        inv = [0] * k
        for a, b in enumerate(p): inv[b] = a
        ms = tuple(minimals[inv[t]] for t in range(k))
        js = tuple(sorted(tuple(sorted((p[a], p[b]))) for (a, b) in joins))
        cand = (ms, js)
        if best is None or cand < best:
            best = cand; bestp = p
    return (best, bestp) if return_perm else best

def layout(B):
    """Deterministic concrete element list for a canonical Bstruct.
    Elements: ('m',i) ; ('c',i,ci) ; ('g',i,ci,gi) ; ('j',t).
    Returns (elements, pastsets dict el -> frozenset of elements)."""
    minimals, joins = B
    els = []
    past = {}
    for i, desc in enumerate(minimals):
        e = ('m', i); els.append(e); past[e] = frozenset()
    for i, desc in enumerate(minimals):
        for ci, g in enumerate(desc):
            e = ('c', i, ci); els.append(e); past[e] = frozenset({('m', i)})
    for i, desc in enumerate(minimals):
        for ci, g in enumerate(desc):
            for gi in range(g):
                e = ('g', i, ci, gi); els.append(e)
                past[e] = frozenset({('m', i), ('c', i, ci)})
    for t, (a, b) in enumerate(joins):
        e = ('j', t); els.append(e)
        past[e] = frozenset({('m', a), ('m', b)})
    return els, past

def b_downsets_le3(els, past):
    """Structural enumeration (the nine kinds) — equivalent to filtering
    all <=3-subsets for down-closure, but linear in the structure."""
    mins = [e for e in els if e[0] == 'm']
    chs = {}
    for e in els:
        if e[0] == 'c':
            chs.setdefault(e[1], []).append(e)
    grs = {}
    for e in els:
        if e[0] == 'g':
            grs.setdefault((e[1], e[2]), []).append(e)
    jns = [e for e in els if e[0] == 'j']
    out = []
    # size 1
    for m in mins:
        out.append(frozenset({m}))
    # size 2
    for a, b in itertools.combinations(mins, 2):
        out.append(frozenset({a, b}))
    for i, cl in chs.items():
        for c in cl:
            out.append(frozenset({('m', i), c}))
    # size 3
    for tri in itertools.combinations(mins, 3):
        out.append(frozenset(tri))
    for i, cl in chs.items():
        for c in cl:
            for m2 in mins:
                if m2 != ('m', i):
                    out.append(frozenset({('m', i), c, m2}))     # L
        for c, c2 in itertools.combinations(cl, 2):
            out.append(frozenset({('m', i), c, c2}))             # V
    for (i, ci), gl in grs.items():
        for g in gl:
            out.append(frozenset({('m', i), ('c', i, ci), g}))   # 3-chain
    for j in jns:
        a, b = sorted(past[j])
        out.append(frozenset({a, b, j}))                          # Lambda
    return out

def b_bundle(past, ds3, P):
    bits = 0
    for D in ds3:
        if P <= D:
            els = sorted(D)
            loc = {v: t for t, v in enumerate(els)}
            k = len(D) + 1
            rel = set()
            for b in els:
                for a in past[b]:
                    if a in D:
                        rel.add((loc[a], loc[b]))
            xi = k - 1
            for a in P:
                rel.add((loc[a], xi))
            bits |= 1 << typeid(frozenset(rel), k)
    return bits

def apply_move(B, P, caps):
    """Return newBstruct (uncanonicalized, with an element-name map
    old-name -> new-name) after adding x above P (concrete names)."""
    MCAP, CCAP, GCAP, JCAP = caps
    minimals, joins = B
    minimals = [list(d) for d in minimals]
    joins = list(joins)
    kinds = sorted(e[0] for e in P)
    namemap = {}
    if len(P) == 0:
        if len(minimals) < MCAP:
            minimals.append([])
    elif len(P) == 1 and kinds == ['m']:
        (_, i), = P
        if len(minimals[i]) < CCAP:
            minimals[i].append(0)
    elif len(P) == 2 and kinds == ['m', 'm']:
        pair = tuple(sorted(e[1] for e in P))
        if joins.count(pair) < JCAP:
            joins.append(pair)
    elif len(P) == 2 and kinds == ['c', 'm']:
        c = next(e for e in P if e[0] == 'c')
        _, i, ci = c
        if minimals[i][ci] < GCAP:
            minimals[i][ci] += 1
    # |P| == 3, or capped: B unchanged
    # normalize: sort each minimal's children; build name map old->new
    newmin = []
    childmap = {}
    for i, ch in enumerate(minimals):
        order = sorted(range(len(ch)), key=lambda t: ch[t])
        newmin.append(tuple(ch[t] for t in order))
        for newci, oldci in enumerate(order):
            childmap[(i, oldci)] = newci
    joins_sorted = sorted(joins)
    newB = (tuple(newmin), tuple(joins_sorted))
    canonB, perm = canon_B(newB[0], newB[1], return_perm=True)
    # element name map old-name -> canonical new-name
    def mapname(e):
        if e[0] == 'm':
            return ('m', perm[e[1]])
        if e[0] == 'c':
            i, ci = e[1], e[2]
            if (i, ci) not in childmap:  # child index within old B
                return None
            nci = childmap[(i, ci)]
            # after perm, minimal i -> perm[i]; children order: desc is
            # sorted tuple, identical multiset -> same sorted order; but
            # perm reindexes minimals, children keep their sorted slot
            return ('c', perm[i], nci)
        if e[0] == 'g':
            i, ci, gi = e[1], e[2], e[3]
            if (i, ci) not in childmap:
                return None
            return ('g', perm[i], childmap[(i, ci)], gi)
        if e[0] == 'j':
            a, b = joins[e[1]] if e[1] < len(joins) else (None, None)
            pr = tuple(sorted((perm[a], perm[b])))
            return ('j', tuple(sorted(tuple(sorted((perm[x], perm[y])))
                                      for (x, y) in joins)).index(pr))
        return None
    return canonB, mapname

# note on mapname for 'c'/'g': a canonical perm relabels minimals; a
# minimal's desc tuple is invariant, and children slots are by sorted
# gcount — twins are automorphic, so slot-stable mapping is valid.

def transitions(Bcanon, caps):
    """List of (P_names_frozenset, bundlebits, newBcanon, mapname_fn)."""
    els, past = layout(Bcanon)
    ds3 = b_downsets_le3(els, past)
    out = []
    Pcands = [frozenset()] + ds3
    for P in Pcands:
        if len(P) > 3:
            continue
        bits = b_bundle(past, ds3, P)
        newB, mapname = apply_move(Bcanon, P, caps)
        out.append((P, bits, newB, mapname))
    return out

def machine_bfs(caps, ncap=None, want_pred=False, state_limit=6_000_000):
    """BFS over (Bcanon, sig). Returns (census set of sigs with sig4!=0,
    per-depth cumulative sig sets (if ncap), pred dict, minsize dict)."""
    trans_cache = {}
    B0 = ((), ())
    start = (B0, 0)
    visited = {start: 0}
    pred = {start: None} if want_pred else None
    frontier = deque([start])
    depth_sets = {}
    minsize = {}
    census = set()
    depth = {start: 0}
    while frontier:
        st = frontier.popleft()
        B, sig = st
        d = depth[st]
        n = d + 1  # elements = moves + ... first move creates element 1
        if ncap is not None and n >= ncap + 1:
            continue
        tr = trans_cache.get(B)
        if tr is None:
            tr = transitions(B, caps)
            trans_cache[B] = tr
        for (P, bits, newB, mapname) in tr:
            nsig = sig | bits
            nst = (newB, nsig)
            if nst not in visited:
                if len(visited) >= state_limit:
                    print("  [ABORT] state limit reached — SCALE REFUSAL", flush=True)
                    return None
                visited[nst] = 1
                depth[nst] = d + 1
                if want_pred:
                    pred[nst] = (st, P, mapname)
                frontier.append(nst)
                if sig4_part(nsig):
                    if nsig in census:
                        pass
                    census.add(nsig)
                    p4 = sig4_part(nsig)
                    if p4 not in minsize:
                        minsize[p4] = d + 2  # n = moves+1... see below
                nn = d + 2
                depth_sets.setdefault(nn, set()).add(nsig)
    return census, depth_sets, pred, minsize, len(visited), len(trans_cache)

# depth bookkeeping: the start state is the empty causet (0 elements);
# each move adds one element, so a state at BFS depth d is a causet with
# d elements. minsize/depth_sets use n = d (fixed below by calibration
# against the brute per-n sets in G3 — the calibration is part of the gate).

log("machine: validation run (n-tracked to 8, production caps)")
CAPS_BIG = (5, 3, 2, 1)
CAPS_SMALL = (4, 2, 1, 1)

def machine_bfs_ntracked(caps, ncap):
    trans_cache = {}
    B0 = ((), ())
    start = (0, B0, 0)  # (n, B, sig): n = number of elements
    visited = {start}
    frontier = deque([start])
    per_n = {}
    while frontier:
        n, B, sig = frontier.popleft()
        per_n.setdefault(n, set()).add(sig)
        if n >= ncap:
            continue
        tr = trans_cache.get(B)
        if tr is None:
            tr = transitions(B, caps)
            trans_cache[B] = tr
        for (P, bits, newB, mapname) in tr:
            nst = (n + 1, newB, sig | bits)
            if nst not in visited:
                visited.add(nst)
                frontier.append(nst)
    cum = {}
    acc = set()
    for n in range(0, ncap + 1):
        acc |= per_n.get(n, set())
        cum[n] = set(acc)
    return cum, len(visited)

mcum, nstates_v = machine_bfs_ntracked(CAPS_BIG, NB)
log(f"machine validation: {nstates_v} (n,B,sig) states")
ok3 = all(mcum[n] == brute_cum_sets[n] for n in range(1, NB + 1))
gate("G3: machine (n-tracked, caps {}) == brute cumulative census at every n <= {}".format(CAPS_BIG, NB),
     ok3, " ".join(f"n{n}:{len(mcum[n])}/{len(brute_cum_sets[n])}" for n in range(4, NB + 1)))
if not ok3:
    for n in range(1, NB + 1):
        miss = brute_cum_sets[n] - mcum[n]
        extra = mcum[n] - brute_cum_sets[n]
        if miss or extra:
            print(f"      n={n}: machine missing {len(miss)}, extra {len(extra)}")
    print("REFUSAL: exiting before production run")
    sys.exit(1)

# level-3 back-check from the machine
m3 = {sig_split(s)[1] for s in mcum[NB] if sig_split(s)[1]}
gate("G2: machine exact-3 census = 22 (round-38 anchor; within n <= 8: "
     "expect 22 since the 22nd appears at n = 7)", len(m3) == 22, f"{len(m3)}")

# ---------------- production runs ----------------
log(f"production BFS, caps {CAPS_SMALL}")
res_small = machine_bfs(CAPS_SMALL, want_pred=False)
if res_small is None: sys.exit(1)
cen_s, _, _, mins_s, nvis_s, nB_s = res_small
lvl4_small = {sig4_part(s) for s in cen_s}
log(f"caps {CAPS_SMALL}: {nvis_s} states, {nB_s} B-canons, level-4 census {len(lvl4_small)}")

log(f"production BFS, caps {CAPS_BIG} (with predecessor tracking for G5)")
res_big = machine_bfs(CAPS_BIG, want_pred=True)
if res_big is None: sys.exit(1)
cen_b, _, pred, mins_b, nvis_b, nB_b = res_big
lvl4_big = {sig4_part(s) for s in cen_b}
log(f"caps {CAPS_BIG}: {nvis_b} states, {nB_b} B-canons, level-4 census {len(lvl4_big)}")

gate(f"G4: cap-stability — census identical at {CAPS_SMALL} and {CAPS_BIG}",
     lvl4_small == lvl4_big,
     f"{len(lvl4_small)} vs {len(lvl4_big)}")

# G6: determination shadow
full_by_4 = {}
for s in cen_b:
    full_by_4.setdefault(sig4_part(s), set()).add(s)
ok6 = all(len(v) == 1 for v in full_by_4.values())
gate("G6: each exact-4 set carries exactly one full signature", ok6,
     f"{sum(len(v) for v in full_by_4.values())} sigs over {len(full_by_4)} nodes")

# ---------------- G5: witness replay for EVERY node ----------------
log("G5: replaying witness paths for every census node")
# first-reaching state per node
first_state = {}
for st in pred:
    B, sig = st
    p4 = sig4_part(sig)
    if p4 and p4 not in first_state:
        first_state[p4] = st
# ensure we use a state whose sig is THE unique full sig (G6) — any works
node_state = {}
for st in pred:
    B, sig = st
    p4 = sig4_part(sig)
    if p4 and p4 not in node_state:
        node_state[p4] = st

def replay2(st):
    chain = []
    cur = st
    while pred[cur] is not None:
        prev, P, mapname = pred[cur]
        chain.append((prev, P, mapname, cur))
        cur = prev
    chain.reverse()
    pasts = []
    name2idx = {}
    for (prev, P, mapname, nxt) in chain:
        mask = 0
        for e in P:
            i = name2idx[e]
            mask |= (1 << i) | pasts[i]
        pasts.append(mask)
        newidx = len(pasts) - 1
        new_map = {}
        for name, idx in name2idx.items():
            nn = mapname(name)
            if nn is not None:
                new_map[nn] = idx
        els_new, _ = layout(nxt[0])
        missing = [e for e in els_new if e not in new_map]
        if len(missing) == 1:
            new_map[missing[0]] = newidx
        elif len(missing) > 1:
            raise RuntimeError(f"ambiguous mapping: {missing}")
        name2idx = new_map
    return tuple(pasts)

ok5 = True
bad = []
witness_sizes = {}
for p4, st in sorted(node_state.items()):
    try:
        pasts = replay2(st)
        s = sig_from_scratch(pasts)
        expect = full_by_4[p4]
        okone = (s in expect) and sig4_part(s) == p4
        witness_sizes[p4] = len(pasts)
    except Exception as ex:
        okone = False
        bad.append((p4, repr(ex)))
    if not okone:
        ok5 = False
        bad.append((p4, "sig mismatch"))
gate("G5: every census node's path replayed to a concrete causet; "
     "signature recomputed from scratch matches", ok5,
     f"{len(node_state)} nodes replayed" + (f"; failures {bad[:3]}" if bad else ""))

# ---------------- outputs ----------------
print()
print(f"THE LEVEL-4 COVTREE CENSUS: {len(lvl4_big)} nodes "
      f"(of {2**16-1} candidate subsets of the 16 four-element posets)")
newly = {}
prev = set()
for n in range(4, NB + 1):
    newly[n] = len(cens4[n] - prev)
    prev = set(cens4[n])
beyond = lvl4_big - cens4[NB]
print(f"  new nodes by witness size (brute, exact): "
      + " ".join(f"n={n}:+{newly[n]}" for n in range(4, NB + 1))
      + f"; first reached beyond n = 8 (machine): +{len(beyond)}")
if beyond:
    sizes = sorted(witness_sizes[p] for p in beyond)
    print(f"  machine witness sizes beyond 8: {sizes}")
hist = {}
for p4 in lvl4_big:
    hist[bin(p4).count('1')] = hist.get(bin(p4).count('1'), 0) + 1
print(f"  nodes by |Q| (number of 4-poset types in the node): "
      + " ".join(f"|Q|={k}:{hist[k]}" for k in sorted(hist)))
print(f"  type table (bit -> poset, strict relations on a<b<c<d labels):")
for idx in sorted(_type_names):
    if idx >= 7:
        print(f"    bit{idx-7:2d}: {_type_names[idx]}")
print()
print(f"PRE-REGISTERED GATE LEDGER: "
      f"{'ALL HELD' if FAIL == 0 else 'REFUSALS PRESENT'} — "
      f"G1 brute anchor; G2 level-3 back-check; G3 exhaustive cross-validation; "
      f"G4 cap-stability; G5 witness soundness; G6 determination")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: sys.exit(1)
