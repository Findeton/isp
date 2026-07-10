#!/usr/bin/env python3
"""
stem_spectrum_receipts_b.py — v9 round 38, review pass 1 corrections:
receipt gates B (note-stem-spectrum, Round-38 amendment; pin ca924bd
committed strictly before this file ran).

rB1  the 22: all labeled 7-causets (96428, independently recounted);
     census of exact-size-3 stem signatures at n <= 7 = 22 classes,
     exactly one new at n = 7 = all five 3-orders; explicit witness
     printed and re-verified.
rB2  the extension lemma mechanized at n <= 7: every stem of size < 3
     extends to a 3-stem; exact-3 signature determines the <= 3
     signature.
rB3  the reviewer's interface state machine (adopted verbatim from the
     round-38 review's /tmp/ssrev/indep_verify.py, credited): reachable
     exact-3 sets at n <= 12 == the n = 7 brute-force census.
rB4  tower correspondence, finite shadow: #(<=3 signatures) ==
     #(exact-3 signatures) at n = 6, 7; certificates exhibited.
Exit 1 on any gate failing.
"""
import itertools
from collections import deque

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

# ---------- machinery (frozenset-of-pairs representation, as receipt A) ----------
def grow_all(n):
    levels = {1: [frozenset()]}
    for m in range(2, n + 1):
        out = set()
        for rel in levels[m - 1]:
            below = {i: {a for (a, b) in rel if b == i} for i in range(m - 1)}
            for bits in range(1 << (m - 1)):
                D = {i for i in range(m - 1) if bits >> i & 1}
                if all(below[i] <= D for i in D):
                    new = set(rel)
                    for i in D:
                        new.add((i, m - 1))
                    out.add(frozenset(new))
        levels[m] = sorted(out, key=sorted)
    return levels

PAIRS7 = [(i, j) for i in range(7) for j in range(i + 1, 7)]
def direct_count7():
    """Independent recount at m = 7: upper-triangular transitively closed
    relations, via row bitmasks (different machinery from growth)."""
    cnt = 0
    npairs = len(PAIRS7)
    for bits in range(1 << npairs):
        rows = [0] * 7
        t = bits
        while t:
            low = t & -t
            a, b = PAIRS7[low.bit_length() - 1]
            rows[a] |= 1 << b
            t ^= low
        ok = True
        for a in range(7):
            ra = rows[a]
            rb = ra
            while rb:
                low = rb & -rb
                b = low.bit_length() - 1
                if rows[b] & ~ra:
                    ok = False
                    break
                rb ^= low
            if not ok:
                break
        cnt += ok
    return cnt

def canon(rel, m):
    best = None
    for p in itertools.permutations(range(m)):
        r = tuple(sorted((p[a], p[b]) for (a, b) in rel))
        if best is None or r < best:
            best = r
    return (m, best)

# the five 3-orders by canonical form (named for the machine comparison)
NAME3 = {}
for name, edges in (("A3", []), ("C3", [(0, 1), (0, 2), (1, 2)]),
                    ("L", [(0, 1)]), ("V", [(0, 1), (0, 2)]),
                    ("Lam", [(0, 2), (1, 2)])):
    NAME3[canon(frozenset(edges), 3)] = name
ALL5 = frozenset(NAME3.values())

def downsets_le3(rel, m):
    below = {i: {a for (a, b) in rel if b == i} for i in range(m)}
    out = []
    for k in (1, 2, 3):
        for comb in itertools.combinations(range(m), k):
            S = set(comb)
            if all(below[i] <= S for i in comb):
                out.append(comb)
    return out, below

def sig_le3(rel, m):
    """(set of canonical stems size<=3, set of names of exact-3 stems,
    list of down-sets)."""
    ds, _ = downsets_le3(rel, m)
    sigs = set(); ex3 = set()
    for comb in ds:
        idx = {v: t for t, v in enumerate(comb)}
        sub = frozenset((idx[a], idx[b]) for (a, b) in rel
                        if a in comb and b in comb)
        c = canon(sub, len(comb))
        sigs.add(c)
        if len(comb) == 3:
            ex3.add(NAME3[c])
    return frozenset(sigs), frozenset(ex3), ds

print("[stem spectrum receipts B]")
levels = grow_all(7)
n7 = len(levels[7])
dc7 = direct_count7()
check("rB1a: |labeled 7-causets| = 96428 = independent recount",
      n7 == 96428 == dc7, f"growth {n7}, recount {dc7}")

# exact-3 censuses at n = 6 and n = 7; <=3 censuses; determination
census = {}
for m in (6, 7):
    ex3_to_le3 = {}
    ext_ok = True
    witness = None
    for rel in levels[m]:
        le3, ex3, ds = sig_le3(rel, m)
        ex3_to_le3.setdefault(ex3, set()).add(le3)
        # rB2: every stem of size < 3 extends to a size+1 stem
        dsets = [frozenset(c) for c in ds]
        for D in dsets:
            if len(D) < 3:
                if not any(len(E) == len(D) + 1 and D < E for E in dsets):
                    ext_ok = False
        if ex3 == ALL5 and witness is None:
            witness = rel
    census[m] = (ex3_to_le3, ext_ok, witness)

ex6, ext6, _ = census[6]
ex7, ext7, wit7 = census[7]
new7 = set(ex7) - set(ex6)
check("rB1b: exact-3 census = 21 (n<=6) -> 22 (n<=7); the one new class "
      "= all five 3-orders",
      len(ex6) == 21 and len(ex7) == 22 and new7 == {ALL5},
      f"n6:{len(ex6)} n7:{len(ex7)} new:{[sorted(s) for s in new7]}")

# explicit witness, re-verified element by element
ok_wit = wit7 is not None
if ok_wit:
    _, wex3, wds = sig_le3(wit7, 7)
    ok_wit = wex3 == ALL5
    print(f"      rB1c witness (7 elements, relation pairs): {sorted(wit7)}")
    print(f"      its size-3 down-sets and shapes:")
    for comb in wds:
        if len(comb) == 3:
            idx = {v: t for t, v in enumerate(comb)}
            sub = frozenset((idx[a], idx[b]) for (a, b) in wit7
                            if a in comb and b in comb)
            print(f"        {comb} -> {NAME3[canon(sub, 3)]}")
check("rB1c: explicit all-five witness at n = 7, re-verified", ok_wit)

check("rB2: extension lemma at n <= 7 (every <3-stem extends; no "
      "counterexample)", ext6 and ext7)
det6 = all(len(v) == 1 for v in ex6.values())
det7 = all(len(v) == 1 for v in ex7.values())
check("rB2b: exact-3 signature determines <=3 signature (n = 6 and 7)",
      det6 and det7, f"n6 {sum(len(v) for v in ex6.values())} le3-sigs over "
      f"{len(ex6)} classes; n7 {sum(len(v) for v in ex7.values())} over {len(ex7)}")

# ---------- rB3: the reviewer's interface state machine (adopted verbatim,
# credited: round-38 review, /tmp/ssrev/indep_verify.py) ----------
NCAP = 12
start = (1, 1, 0, frozenset(), frozenset())
seen = {start}
q = deque([start])
reach = set()
while q:
    n, c0, c1, s2, s3 = q.popleft()
    if n >= 3:
        reach.add((s2, s3))
    if n >= NCAP:
        continue
    moves = []
    ns2 = set(s2); ns3 = set(s3)
    ns2.add('ac2')
    if c1 >= 1: ns3.add('L')
    if c0 + c1 >= 2: ns3.add('A3')
    moves.append((n + 1, c0 + 1, c1, frozenset(ns2), frozenset(ns3)))
    if c0 >= 1:
        ns2 = set(s2); ns3 = set(s3)
        ns2.add('ch2')
        if c0 + c1 >= 2: ns3.add('L')
        moves.append((n + 1, c0 - 1, c1 + 1, frozenset(ns2), frozenset(ns3)))
    if c1 >= 1:
        ns2 = set(s2); ns3 = set(s3)
        ns2.add('ch2'); ns3.add('V')
        if c0 + c1 >= 2: ns3.add('L')
        moves.append((n + 1, c0, c1, frozenset(ns2), frozenset(ns3)))
    if c0 + c1 >= 2:
        ns3 = set(s3); ns3.add('Lam')
        moves.append((n + 1, c0, c1, s2, frozenset(ns3)))
    if c1 >= 1:
        ns3 = set(s3); ns3.add('C3')
        moves.append((n + 1, c0, c1, s2, frozenset(ns3)))
    for mv in moves:
        if mv not in seen:
            seen.add(mv); q.append(mv)

machine_sig3 = {s3 for (s2, s3) in reach}
brute_sig3 = set(ex7.keys())
check(f"rB3: state machine (n <= {NCAP}) exact-3 sets == n = 7 brute census",
      machine_sig3 == brute_sig3,
      f"machine {len(machine_sig3)}, brute {len(brute_sig3)}; "
      f"completeness beyond n = {NCAP} rests on the cited witness bound "
      f"(Gutzeit et al.), review-verified")

# ---------- rB4: tower correspondence, finite shadow ----------
le3_6 = {s for v in ex6.values() for s in v}
le3_7 = {s for v in ex7.values() for s in v}
check("rB4: #(<=3 signatures) == #(exact-3 signatures) at n = 6 and 7",
      len(le3_6) == len(ex6) and len(le3_7) == len(ex7),
      f"n6: {len(le3_6)}=={len(ex6)}; n7: {len(le3_7)}=={len(ex7)} — "
      f"covtree level-3 node count within these sizes: {len(ex7)}")

print()
print(f"PRE-REGISTERED GATE LEDGER B: "
      f"{'ALL HELD' if FAIL == 0 else 'REFUSALS PRESENT'} — rB1 the 22; "
      f"rB2 extension lemma + determination; rB3 machine == brute; "
      f"rB4 tower shadow")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0
      else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
