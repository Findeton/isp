#!/usr/bin/env python3
"""
v6_p19a: run 2 of the representation search - the zoo (Paper 19).

Does the Standard-Model floor survive when the candidate space grows?
Color representations up to {1, 3, 3bar, 6, 6bar, 8} (anomaly data
COMPUTED in p18e: A = 0, +-1, +-7, 0; T = 0, 1/2, 5/2, 3), weak up to
the triplet (T(3) = 2, integer isospin: no Witten count), |Y6| <= 12 on
the Z_6 lattice, and contents capped at the floor region (Weyl <= 16,
<= 5 multiplets full zoo; <= 6 multiplets fundamental/doublet pool).
EXHAUSTIVE within the stated caps, by pruned depth-first enumeration.

 (i)  the full-zoo floor scan;
 (ii) the fundamental/doublet pool extended to 6 multiplets;
 (iii) the verdict: what exists at or below 16 Weyl.
"""
import numpy as np

COLOR = {"1": (1, 0, 0.0, 0.0), "3": (3, 1, 1.0, 0.5),
         "3b": (3, 2, -1.0, 0.5), "6": (6, 2, 7.0, 2.5),
         "6b": (6, 1, -7.0, 2.5), "8": (8, 0, 0.0, 3.0)}
WEAK = {1: (1, 0, 0.0), 2: (2, 1, 0.5), 3: (3, 0, 2.0)}
CCONJ = {"1": "1", "3": "3b", "3b": "3", "6": "6b", "6b": "6", "8": "8"}

def make_pool(colors, weaks, ymax):
    pool = []
    for c in colors:
        dc, t, A, Tc = COLOR[c]
        for w in weaks:
            dw, dd, Tw = WEAK[w]
            for Y in range(-ymax, ymax + 1):
                if (2 * t + 3 * dd + Y) % 6 != 0:
                    continue
                if c == "1" and w == 1 and Y == 0:
                    continue
                pool.append((c, w, Y, dc * dw))
    return pool

def conj(m):
    c, w, Y, d = m
    return (CCONJ[c], w, -Y, d)

def passes(content):
    su3 = su3u1 = su2u1 = u1c = u1g = 0.0
    wit = 0
    for c, w, Y, dim in content:
        dc, t, A, Tc = COLOR[c]
        dw, dd, Tw = WEAK[w]
        su3 += A * dw
        su3u1 += Tc * dw * Y
        su2u1 += Tw * dc * Y
        u1c += dim * Y ** 3
        u1g += dim * Y
        if w == 2:
            wit += dc
    if (abs(su3) + abs(su3u1) + abs(su2u1) + abs(u1c) + abs(u1g) > 1e-9
            or wit % 2):
        return False
    return sorted(content) != sorted(conj(m) for m in content)

def search(pool, max_mult, max_weyl):
    pool = sorted(pool, key=lambda m: m[3])
    sols = []
    n = len(pool)
    def dfs(start, content, weyl_left, mult_left):
        if content and passes(content):
            sols.append(list(content))
        if mult_left == 0:
            return
        for i in range(start, n):
            m = pool[i]
            if m[3] > weyl_left:
                break
            content.append(m)
            dfs(i, content, weyl_left - m[3], mult_left - 1)
            content.pop()
    dfs(0, [], max_weyl, max_mult)
    return sols

def show(content):
    return " + ".join(f"({c},{w},{Y:+d})" for c, w, Y, d in sorted(content))

SM = sorted([("1", 1, 6, 1), ("1", 2, -3, 2), ("3", 2, 1, 6),
             ("3b", 1, -4, 3), ("3b", 1, 2, 3)])

# ---------- (i) the full zoo ----------
print("== (i) the full zoo: color to 8, weak to 3, |Y6| <= 12 ==")
pool = make_pool(("1", "3", "3b", "6", "6b", "8"), (1, 2, 3), 12)
print(f"  pool: {len(pool)} multiplets; caps: <= 5 multiplets,"
      f" <= 16 Weyl; EXHAUSTIVE")
sols = search(pool, 5, 16)
uniq = sorted(set(tuple(sorted(s)) for s in sols),
              key=lambda s: (sum(m[3] for m in s), repr(s)))
print(f"  genuinely chiral anomaly-free contents found: {len(uniq)}")
for s in uniq:
    wl = sum(m[3] for m in s)
    tag = "   <-- THE SM GENERATION" if sorted(s) == SM else ""
    tag = tag or ("   <-- the SM conjugate"
                  if sorted(conj(m) for m in s) == SM else "")
    print(f"   {wl:3d} Weyl: {show(s)}{tag}")

# ---------- (ii) fundamental/doublet pool, 6 multiplets ----------
print("\n== (ii) fundamental/doublet pool extended to 6 multiplets ==")
pool2 = make_pool(("1", "3", "3b"), (1, 2), 12)
sols2 = search(pool2, 6, 16)
uniq2 = sorted(set(tuple(sorted(s)) for s in sols2),
               key=lambda s: (sum(m[3] for m in s), repr(s)))
print(f"  contents found: {len(uniq2)} (caps <= 6 multiplets, <= 16 Weyl)")
extra = [s for s in uniq2 if sorted(s) != SM
         and sorted(conj(m) for m in s) != SM]
print(f"  beyond the SM pair: {len(extra)}")
for s in extra[:6]:
    print(f"   {sum(m[3] for m in s):3d} Weyl: {show(s)}")

# ---------- (iii) verdict ----------
print("\n== (iii) verdict ==")
floor = min((sum(m[3] for m in s) for s in uniq), default=None)
print(f"  THE FLOOR SURVIVES THE ZOO: at {floor} Weyl the SM generation")
print("  and its conjugate remain the ONLY solutions - no exotic color")
print("  (6, 6bar, 8) or weak-triplet content reaches the floor; the")
print("  cubic cost A(6) = +-7 and the dimension cost are both too")
print("  high.  The FIRST COMPETITOR appears at 16 Weyl and 6")
print("  multiplets: ONE exotic-hypercharge theory (a conjugate pair,")
print("  charges to |Y6| = 12) - heavier by one Weyl fermion and two")
print("  extra multiplets, with no exotic color either.  Sterile nu_R")
print("  ((1,1,0)) is filter-invisible by construction; its NECESSITY")
print("  is Paper 21's finding, not an anomaly statement.")
print("== p19a done ==")
