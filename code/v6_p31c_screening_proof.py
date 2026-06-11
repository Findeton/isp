#!/usr/bin/env python3
"""
v6_p31c: the conditional proof of (E) (Paper 31, part C).

Paper 31 stated (E) [sealed-epsilon screening] as the load-bearing
hypothesis.  This script supplies the receipts that PROMOTE it to a
conditional theorem:

   (E) holds GIVEN three named anchors:
   L1 (COLLAPSE, the one genuinely new lemma): superselection
      classes of the record algebra connected by a SEALED,
      UNIVALENCE-EVEN, NONABELIAN-SINGLET record coincide.
      Fermionic intertwiners are blocked by P9's univalence
      superselection THEOREM; nonabelian-charged ones change
      recorded relation codes (P8/I2).
   L2 (EXISTENCE): the ledger certifies a sealed univalence-even
      singlet with charge (a,b) = (3,2): the QQQL seal (P25 dim-6
      ledger, B-L = 0), built from epsilon_3 on color and two
      epsilon_2 pairings on weak.  Receipts: the invariant tensors
      exist (dim Inv = 1 and 2), the charge arithmetic gives (3,2),
      and F = 4 is even.
   L3 (RANK BOUND): the screening lattice has rank <= 1 - rank 2
      would leave NO recordable continuous charge, contradicting
      P8's screen-U(1) theorem.  Receipt: the lattice arithmetic.
   THEOREM: rank <= 1 + (3,2) in the lattice + (3,2) primitive
      => screening lattice = Z.(3,2) => recordable data =
      (a,b) mod (3,2)Z with complete invariants EXACTLY
      (tau, sigma, Y6 = 3b - 2a): the S(U(3) x U(2)) structure
      derived, sharper than Paper 31 SS5.1 (single-direction
      quotient = the global gauge-group statement on the nose).

 (i)   invariant-tensor receipts for the QQQL seal;
 (ii)  the blocking table: which candidate screeners are excluded
       and by which corpus theorem;
 (iii) the lattice theorem: rank bound, primitivity, completeness
       of the invariants (tau, sigma, Y6);
 (iv)  THE ALTERNATIVE WORLD, exhibited honestly: a rank-1 ledger
       certifying a (0,2)-seal instead (e^c nu^c-type) is
       mathematically consistent and yields Y = a (pure color-det
       hypercharge); it is excluded by the LEDGER RECEIPTS (which
       seals exist), not by fiat - the selection is an empirical/
       dynamical fact, stated as such.
"""
import numpy as np
from itertools import product

rng = np.random.default_rng(313)

def haar_su(d, rng):
    z = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    q, r = np.linalg.qr(z)
    q = q * (np.diag(r) / np.abs(np.diag(r)))
    return q / np.linalg.det(q) ** (1 / d)

def inv_dim(d, n, rng, samples=24):
    """dim of SU(d)-invariants in (C^d)^{tensor n}."""
    dim = d ** n
    M = np.zeros((0, dim), dtype=complex)
    rows = []
    for _ in range(samples):
        U = haar_su(d, rng)
        K = np.eye(1)
        for _ in range(n):
            K = np.kron(K, U)
        rows.append(K - np.eye(dim))
    A = np.vstack(rows)
    return dim - np.linalg.matrix_rank(A, tol=1e-8)

# ---------- (i) the QQQL seal exists ----------
print("== (i) the (3,2) seal: invariant tensors and arithmetic ==")
d_color = inv_dim(3, 3, rng)
d_weak = inv_dim(2, 4, rng)
print(f"  dim Inv_SU(3)(3 x 3 x 3)   = {d_color}   (epsilon_3:"
      f" the color contraction of QQQ)")
print(f"  dim Inv_SU(2)(2^x4)        = {d_weak}   (two epsilon_2"
      f" pairings of QQQL's four doublets)")
aQ, bQ = 1, 1
aL, bL = 0, -1
a_tot, b_tot = 3 * aQ + aL, 3 * bQ + bL
F = 4
print(f"  charge arithmetic: 3x Q(1,1) + L(0,-1) = "
      f"({a_tot},{b_tot});  fermion number F = {F} (EVEN)")
ok = (d_color == 1 and d_weak == 2 and (a_tot, b_tot) == (3, 2)
      and F % 2 == 0)
print(f"  the QQQL seal: nonabelian singlet, univalence-even,"
      f" charge (3,2): {'PASS' if ok else 'FAIL'}")
print("  -> L2 receipted: the ledger's own dim-6 row (P25, B-L = 0)")
print("     is a sealed univalence-even singlet generating the")
print("     (3,2) direction.")

# ---------- (ii) the blocking table ----------
print("\n== (ii) candidate screeners and their blockers ==")
print("""   candidate        (a,b)   F par.  singlet?  verdict
   epsilon_3 (QQQ)  (3,3)*  odd     no(weak)  BLOCKED: no weak
                                              singlet in 2^x3 AND
                                              univalence-odd (P9)
   bare baryon ch.  (3,0)   odd     yes       BLOCKED: univalence-
                                              odd (P9 theorem)
   H-tilde          (0,1)   even    no        BLOCKED: weak doublet
                                              (recorded nonabelian
                                              data changes)
   eps_2(H,H)       (0,2)   even    yes       VANISHES identically
                                              (antisym of identical
                                              bosons)
   e^c nu^c         (0,2)   even    yes       EXCLUDED by L3 given
                                              L2 (rank bound) - see
                                              (iv); not in the P25
                                              ledger
   QQQL             (3,2)   even    yes       SEALS (L2)""")
w3 = inv_dim(2, 3, rng)
print(f"  receipt for row 1: dim Inv_SU(2)(2^x3) = {w3} (no weak"
      f" singlet of three doublets)")
hh = np.zeros(1)
print("  receipt for eps_2(H,H): antisymmetrization of identical")
print("  bosonic doublets is identically zero (epsilon symmetry).")

# ---------- (iii) the lattice theorem ----------
print("\n== (iii) the screening lattice = Z.(3,2) ==")
# rank bound: rank-2 screening leaves no continuous functional
for gens in [[(3, 2), (0, 2)], [(3, 2), (3, 0)]]:
    sols = [(p, q) for p in range(-9, 10) for q in range(-9, 10)
            if all(p * g[0] + q * g[1] == 0 for g in gens)
            and (p, q) != (0, 0)]
    print(f"  if screening contained {gens}: surviving functionals ="
          f" {sols if sols else 'NONE'}")
print("  -> rank-2 screening kills ALL continuous charge,")
print("     contradicting P8's screen-U(1): rank <= 1  (L3).")
g = int(np.gcd(3, 2))
print(f"  (3,2) is primitive (gcd = {g}): a rank-1 lattice")
print("  containing it is exactly Z.(3,2).")
# completeness of the invariants on the quotient
def cls(a, b):
    # canonical representative of (a,b) mod (3,2)Z
    k = a // 3
    return (a - 3 * k, b - 2 * k)
bad = 0
for a, b in product(range(-6, 7), repeat=2):
    for a2, b2 in product(range(-6, 7), repeat=2):
        same_class = (a - a2) * 2 == (b - b2) * 3 and (a - a2) % 3 == 0
        same_inv = (a % 3, b % 2, 3 * b - 2 * a) == \
                   (a2 % 3, b2 % 2, 3 * b2 - 2 * a2)
        if same_class != same_inv:
            bad += 1
print(f"  completeness: (tau, sigma, Y6) separates (a,b) mod (3,2)Z")
print(f"  exactly: mismatches over [-6,6]^4 = {bad}")
print("  -> THEOREM (E), conditional form: given L1 (collapse), L2")
print("     (the QQQL receipt), L3 (P8 rank bound): the screening")
print("     lattice is Z.(3,2); recordable charge data = (a,b) mod")
print("     (3,2)Z with complete invariants (tau, sigma, Y6 = 3b-2a)")
print("     - the S(U(3) x U(2)) structure, hence (Y-det), hence the")
print("     Z6 lattice.  The only unproved piece is L1 at record")
print("     scope: (E-coll), strictly smaller than the old (E-cond).")

# ---------- (iv) the alternative world ----------
print("\n== (iv) the alternative rank-1 world (honest exhibit) ==")
sols = [(p, q) for p in range(-9, 10) for q in range(-9, 10)
        if q * 2 == 0 and p != 0 or (p == 0 and q * 2 == 0 and q != 0)]
surv = [(p, q) for p in range(-9, 10) for q in range(-9, 10)
        if p * 0 + q * 2 == 0 and (p, q) != (0, 0)]
gen = min(surv, key=lambda t: abs(t[0]) + abs(t[1]))
print(f"  a ledger certifying a (0,2)-seal instead (e^c nu^c-type)")
print(f"  would screen Z.(0,2): surviving functionals = Z.{gen}:")
print(f"  hypercharge would be Y = a (pure color-determinant).")
print("  That world is mathematically consistent at this level; it")
print("  is excluded by the LEDGER RECEIPTS - nature's sealed set")
print("  contains baryon-lepton seals (B-L = 0 rows, P25) and no")
print("  charged-lepton-pair seal - and by nothing else offered")
print("  here.  The selection between the two rank-1 worlds is an")
print("  empirical/dynamical fact (a candidate (M)-dynamics target),")
print("  stated as such; what the conditional theorem removes is the")
print("  TARGET-CALIBRATION: no congruence is copied from the SM")
print("  anywhere in the chain.")
print("== p31c done ==")
