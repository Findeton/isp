#!/usr/bin/env python3
"""
v6_p23a: the mass-protection theorem (Paper 23).

Which fermion masses can the record ledger seal WITHOUT the scalar?
A bare mass is a gauge-invariant fermion bilinear.  Exhaustive scan of
all 21 pairs of the SM + nu_R content:

  color singlet:  1x1 or 3x3bar only (3x3 and 3barx3bar have no
                  bilinear singlet - the epsilon is trilinear);
  weak singlet:   1x1 or 2x2 (epsilon);
  hypercharge:    Y6 sum = 0.

THE THEOREM: exactly ONE gauge-invariant bilinear exists -
nu^c nu^c (the right-handed Majorana mass).  Every charged fermion of
the Standard Model is RECORD-PROTECTED until EWSB: mass requires the
seam through H (P20), so every charged mass is proportional to v -
and the neutrino is structurally special, exactly as observed.
"""
fields = [("Q", "3", 2, 1), ("u^c", "3b", 1, -4), ("d^c", "3b", 1, 2),
          ("L", "1", 2, -3), ("e^c", "1", 1, 6), ("nu^c", "1", 1, 0)]

def color_ok(c1, c2):
    return (c1, c2) in (("1", "1"), ("3", "3b"), ("3b", "3"))

def weak_ok(w1, w2):
    return (w1, w2) in ((1, 1), (2, 2))

print("== the bilinear scan: all 21 pairs of the SM + nu_R content ==")
print("   pair          color   weak    Y6 sum   bare mass?")
count = 0
for i in range(len(fields)):
    for j in range(i, len(fields)):
        n1, c1, w1, y1 = fields[i]
        n2, c2, w2, y2 = fields[j]
        ok_c = color_ok(c1, c2)
        ok_w = weak_ok(w1, w2)
        ok_y = (y1 + y2 == 0)
        ok = ok_c and ok_w and ok_y
        if ok:
            count += 1
        mark = "  <-- ALLOWED" if ok else ""
        print(f"   {n1:5s}{n2:6s}   {'ok' if ok_c else '--':4s}"
              f"   {'ok' if ok_w else '--':4s}   {y1 + y2:+3d}     "
              f"{'YES' if ok else 'no'}{mark}")
print(f"\n  gauge-invariant bare masses: {count} of 21")
print("  -> THE MASS-PROTECTION THEOREM (exhaustive): the ONLY bare")
print("     fermion mass the record lattice admits is nu^c nu^c - the")
print("     right-handed Majorana mass.  Every charged Standard-Model")
print("     fermion is massless until EWSB; every charged mass is")
print("     proportional to v through the P20 seams.  The neutrino is")
print("     STRUCTURALLY SPECIAL: it alone owns a v-independent scale -")
print("     the seesaw's heavy side is record-native, not engineered.")
print("== p23a done ==")
