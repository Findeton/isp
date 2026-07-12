#!/usr/bin/env python3
"""
d26_interface_equivalence_exact.py — v10 D26: the declared interface and
the surviving equivalence class. Pin: note-d26-interface-equivalence-closure.md
(committed pre-run). Stdlib only; exact rationals. Gates E1-E6; exit 1 on failure.
"""
from fractions import Fraction as F

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

CS = {F(9,25): (F(4,5), F(3,5)), F(16,25): (F(3,5), F(4,5)),
      F(576,625): (F(7,25), F(24,25))}
PREP = (F(3,5), F(4,5))

class Web:
    def __init__(self, prep=PREP):
        c, s = prep
        self.regs = ['A']; self.psi = [c, s]
    def birth(self, parent, child, g):
        self.psi = [x for a in self.psi for x in (a, F(0))]
        self.regs.append(child)
        c, s = CS[g]
        n = len(self.regs); ctrl, targ = self.regs.index(parent), n - 1
        out = [F(0)]*(2**n)
        for i, a in enumerate(self.psi):
            if a == 0: continue
            bits = [(i >> (n-1-q)) & 1 for q in range(n)]
            if bits[ctrl] == 0:
                out[i] += a
            else:
                t = bits[targ]
                for tn in (0, 1):
                    b2 = list(bits); b2[targ] = tn
                    j = sum(bb << (n-1-q) for q, bb in enumerate(b2))
                    out[j] += a * (c if tn == t else (s if tn == 1 else -s))
        self.psi = out
    def zlaw(self, labels):
        """Exact Z-click joint law on the given registers (marginalizing the rest)."""
        n = len(self.regs); qs = [self.regs.index(l) for l in labels]
        law = {}
        for i, a in enumerate(self.psi):
            if a == 0: continue
            key = tuple((i >> (n-1-q)) & 1 for q in qs)
            law[key] = law.get(key, F(0)) + a*a
        return law
    def offdiag(self, label):
        """Exact <0|rho_label|1> (the register's coherence; real states)."""
        n = len(self.regs); q = self.regs.index(label)
        tot = F(0)
        for i, a in enumerate(self.psi):
            if a == 0 or ((i >> (n-1-q)) & 1) != 0: continue
            j = i | (1 << (n-1-q))
            tot += a * self.psi[j]
        return tot

print("[d26 interface equivalence — exact]")

# E1: two UV completions, identical probed interface, distinct heavy sector
def uv_chain(g_ah, g_hb):
    w = Web(); w.birth('A', 'H', g_ah); w.birth('H', 'B', g_hb)
    return w
u1, u2 = uv_chain(F(9,25), F(16,25)), uv_chain(F(16,25), F(9,25))
ok1 = u1.zlaw(['A','B']) == u2.zlaw(['A','B'])
h1, h2 = u1.zlaw(['H']), u2.zlaw(['H'])
ok1 &= h1 != h2
check("E1 UV equivalence: mediator completions (9/25,16/25) and (16/25,9/25) "
      "give the IDENTICAL light-sector (A,B) click law; heavy tables differ",
      ok1, f"P(H=1): {h1[(1,)]} vs {h2[(1,)]} — the future click that splits the class")

# E2: dark-interior invisibility (Z-law AND visible coherence)
def dark_web(interior):
    w = Web(); w.birth('A', 'B', F(16,25))       # visible edge
    w.birth('A', 'D', F(16,25))                  # the portal (fixed)
    for (p, ch, g) in interior:
        w.birth(p, ch, g)
    return w
INTERIORS = [ [],
              [('D','D2',F(9,25))],
              [('D','D2',F(9,25)), ('D2','D3',F(576,625))],
              [('D','D2',F(576,625))] ]
ref_z, ref_c = None, None
ok2 = True
for interior in INTERIORS:
    w = dark_web(interior)
    z, c = w.zlaw(['A','B']), w.offdiag('A')
    if ref_z is None: ref_z, ref_c = z, c
    ok2 &= (z == ref_z and c == ref_c)
check("E2 dark-interior invisibility: visible (A,B) Z-law AND A's coherence "
      "are EXACTLY invariant under every dark-interior structure (portal fixed)",
      ok2, f"{len(INTERIORS)} interiors")

# E3: portal identifiability — populations blind, coherence sees
ok3 = True
zlaws, cohs = [], []
for g_p in (F(9,25), F(16,25), F(576,625)):
    w = Web(); w.birth('A', 'B', F(16,25)); w.birth('A', 'D', g_p)
    zlaws.append(w.zlaw(['A','B'])); cohs.append(w.offdiag('A'))
ok3 &= all(z == zlaws[0] for z in zlaws)          # Z-populations portal-blind
ok3 &= len(set(cohs)) == len(cohs)                # coherence pins the portal
print("      E3 honesty: visible Z-POPULATION clicks are portal-blind (dispersal")
print("      does not move populations); the portal is pinned by COHERENCE clicks")
print(f"      (X-visibility): A-coherence = {cohs[0]}, {cohs[1]}, {cohs[2]} — injective.")
check("E3 portal identifiability: Z-law invariant, coherence law injective in "
      "the portal coupling — what is probed is pinned", ok3)

# E4: the birth-decoherence bridge — per-birth visibility factor sqrt(1-g), exact
ok4 = True
c0 = PREP[0]*PREP[1]                              # root coherence cs
for g1 in CS:
    w = Web(); w.birth('A', 'X1', g1)
    ok4 &= w.offdiag('A') == c0 * CS[g1][0]       # x cos(theta) = sqrt(1-g)
    for g2 in CS:
        w2 = Web(); w2.birth('A', 'X1', g1); w2.birth('A', 'X2', g2)
        ok4 &= w2.offdiag('A') == c0 * CS[g1][0] * CS[g2][0]   # multiplicative
check("E4 birth-decoherence bridge: each birth contracts the parent's coherence "
      "by exactly sqrt(1-g), multiplicatively — births are NSE-compliant "
      "dispersal-decoherence events (D25-admitted isometries)", ok4)
print("      E4 consequence [LITERATURE, consistency only]: the kernel's")
print("      laboratory shadow is an anomalous-decoherence channel; current")
print("      coherence records (matter-wave interferometry >1.7e5 Da; the D21")
print("      ladder discipline) bound (rate x coupling) onto probed systems.")
print("      Current nulls are CONSISTENT with any admissible kernel below the")
print("      bound; no quantitative rate is claimed (grounding rule).")

# E5: tested-domain consistency — zero-birth window == the identified law.
# The grown-vs-independent-static wiring leg is receipt-carried at D24 G4;
# here the frozen law is gated against the hand closed forms, all 8 outcomes.
pA, g1, g2 = F(16,25), F(9,25), F(16,25)
w_grown = Web(); w_grown.birth('A', 'B', g1); w_grown.birth('B', 'C', g2)
law = w_grown.zlaw(['A','B','C'])
closed = {(0,0,0): 1 - pA,
          (1,0,0): pA*(1-g1),
          (1,1,0): pA*g1*(1-g2),
          (1,1,1): pA*g1*g2}
ok5 = all(law.get(k, F(0)) == v for k, v in closed.items())
ok5 &= all(law[k] == 0 for k in law if k not in closed)
ok5 &= sum(law.values()) == 1
check("E5 tested-domain consistency: the zero-birth-window law equals the "
      "fixed-carrier conditional measure — full 8-outcome chain table gated "
      "against hand closed forms (wiring leg: D24 G4)", ok5)

# E6: the surviving class + measured inputs (prints)
print("      E6 THE SURVIVING CLASS AT THE DECLARED INTERFACE (current lab/")
print("      collider/solar-system + current cosmological/coherence records):")
print("        { D15 tested-domain restriction (identified, paper 18) }")
print("        x { dim-5 neutrino operator at measured inputs [LITERATURE]:")
print("            dm2_21 ~ 7.5e-5 eV^2, |dm2_32| ~ 2.4e-3 eV^2,")
print("            sin2th12 ~ 0.31, sin2th23 ~ 0.55, sin2th13 ~ 0.022;")
print("            ordering + Dirac/Majorana OPEN = class-internal }")
print("        x { any dark sector entering only via its pinned portal (E2/E3) }")
print("        x { any UV completion with the D15 low-energy shadow (E1) }")
print("        x { any admissible birth kernel below coherence bounds (E4/E5) }")
print("      SPLITTERS (future clicks that break each freedom): heavy-sector")
print("      clicks (E1); portal-coherence precision + direct detection (E2/E3);")
print("      ladder residuals / interferometric visibility (E4); 0nubb and")
print("      ordering data (neutrino); cosmological record-count precision (birth")
print("      kernel rate) [CONSISTENT today, not identified].")
check("E6 class statement + splitters printed", True)

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total}: 5 substantive gates + 1 print gate)"
      if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
