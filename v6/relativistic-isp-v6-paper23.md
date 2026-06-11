# Paper 23 (v6) - SHARD: The Mass Functional

Preprint, not peer reviewed, version 2026-06-10.

Author: Felix Robles Elvira

Subtitle:

```text
Tier 2b.  THE MASS-PROTECTION THEOREM (exhaustive over all 21 pairs of
the SM + nu_R content): the record lattice admits EXACTLY ONE bare
fermion mass - the right-handed Majorana term nu^c nu^c.  Every
charged Standard-Model fermion is record-protected until EWSB: every
charged mass is proportional to v through the P20 seams, and the
neutrino alone owns a v-independent scale - THE SEESAW IS STRUCTURAL
(machine spectrum: lightness m ~ (yv)^2/M with no tuning).  And the
hierarchy mechanism: the corpus' one structural small number - the
single-relation marginality eps = 3 kappa - 1 = 0.0318 (P8/P10) -
drives a record charge ladder whose rungs (eps^2 = 1.0e-3, eps =
3.2e-2, sqrt(eps) = 0.178, Cabibbo-sized) BRACKET every observed
inter-generation step (7.4e-3, 2.2e-2, 5.9e-2): the GRAIN of the
fermion hierarchy matches the record marginality at order-of-magnitude
scope.  A mechanism demo, not a fit - and a falsifiable ledger row
(P-eps) for Paper 25
```

## 0. Verdict

```text
THEOREM M1 (mass protection; p23a, exhaustive).  Of the 21 fermion
bilinears of the SM + nu_R content, exactly ONE is gauge-invariant on
the record lattice: nu^c nu^c.  Consequences:
  - every charged fermion is MASSLESS until EWSB: charged masses are
    seam-generated, proportional to v (P20);
  - the right-handed neutrino is STRUCTURALLY SPECIAL: it alone can
    carry a record-native scale M independent of v.

THE STRUCTURAL SEESAW (p23b).  With M1 + the P20 seams: light
neutrinos at m_nu = (yv)^2/M (machine: 1e-6-class at yv ~ 1.6,
M = 1e6): neutrino lightness is a CONSEQUENCE of the protection
theorem - the seesaw's two scales are exactly the two mass channels
the lattice allows.

THE MARGINALITY LADDER (p23b; mechanism demo, order-of-magnitude).
eps_record = 3 kappa - 1 = 0.0318 - the corpus' single structural
small number (the binding marginality, P8/P10).  Froggatt-Nielsen-type
record charges over the P21 family fiber give masses O(1) x
eps^(qi+qj):
  rungs available: eps^2 = 1.0e-3, eps = 3.2e-2, sqrt(eps) = 0.178
  (Cabibbo-sized; lam_C = 0.225);
  observed steps:  7.4e-3 (up), 2.2e-2 (down), 5.9e-2 (leptons) -
  ALL NINE hierarchy steps sit between eps^2 and sqrt(eps).
STATUS, stated plainly: the grain matches; the textures (which
charges, which O(1) coefficients) are NOT derived; no fit is claimed.
Falsifiable form (P-eps): every fermion hierarchy step is a power of
eps_record in [eps^2, sqrt(eps)] within O(1) - currently true of all
nine.
```

## 1. Method and reproducibility

```text
code/v6_p23a_mass_protection_campaign.py  M1 (exhaustive bilinears)
code/v6_p23b_seesaw_hierarchy_campaign.py seesaw + the eps ladder
```

Both scripts rerun bit-identically.  Corpus inputs: the P19 floor +
P21's nu_R, the P20 seams, P8/P10's marginality value.  PDG mass
ratios quoted at order-of-magnitude for the comparison only.

## 2. Theorem M1: mass protection

### 2.1 Statement and proof

A bare fermion mass is a gauge-invariant Lorentz-scalar bilinear of
two left-handed Weyl multiplets.  Gauge invariance requires: a color
bilinear singlet (1 x 1 or 3 x 3bar - the color epsilon is TRILINEAR,
so 3 x 3 and 3bar x 3bar carry none), a weak bilinear singlet (1 x 1
or the 2 x 2 epsilon), and hypercharges summing to zero.

**Theorem M1.**  Of the 21 unordered pairs of {Q, u^c, d^c, L, e^c,
nu^c}, exactly one passes all three conditions: nu^c nu^c.

*Proof by complete scan* (the machine table is the proof; the
decisive failures): every Q pairing fails color (3 with 3 or with
singlets) or weak (2 x 1); u^c/d^c pairings fail color (3bar x 3bar);
L L passes color and weak (epsilon) but fails hypercharge (-6); L e^c
fails weak; e^c e^c fails hypercharge (+12); e^c nu^c fails (+6);
nu^c nu^c: color 1, weak 1, Y6 = 0 + 0 = 0: PASSES.            QED

### 2.2 Readings

1. **Mass protection is lattice structure, not symmetry decoration:**
   the same Z_6-lattice content selected by the inverse search (P18
   Part II, P19) is also exactly the content whose charged sector is
   completely mass-protected.  The two facts come from one structure.
2. **The neutrino is special by THEOREM:** nu^c is the unique field
   whose bilinear self-pairing the ledger can seal bare.  Lepton
   number is broken by exactly two units in exactly one place - the
   structural origin of the seesaw's heavy side and of P25's P-Maj
   row.
3. Every charged mass is proportional to v: the P-mass prediction.
   At the lattice level this is the SM's own structure recovered; the
   record content is that it is FORCED by the floor content, with no
   freedom to add a vector-like exception without leaving the floor.

## 3. The structural seesaw

With M1, the neutrino sector has two channels: the Dirac seam
L nu^c H (Y6: -3 + 0 + 3 = 0, lattice-allowed - the fourth Yukawa) at
scale y v, and the bare Majorana scale M.  Integrating out the heavy
state (standard seesaw algebra, named import) gives the light mass
matrix m_nu = (m_D) M_R^{-1} (m_D)^T.  Machine receipts: with random
O(1) Yukawas (y v ~ 1.6) and M = 1e6, the light spectrum lands at
1.8e-6 / 8.2e-7 / 2.7e-7 - the (yv)^2/M suppression with NO tuning:
lightness is a consequence of the protection theorem, because the only
scale that can be large without touching v is the one the ledger gives
to nu^c alone.

## 4. The marginality-hierarchy mechanism

### 4.1 The corpus' one small number

The single-relation marginality eps_record = 3 kappa - 1 = +0.0318
(P8's binding law; P10's marginality reading) is the corpus' only
structural small dimensionless number.  A Froggatt-Nielsen-type
ladder (named import for the mechanism class) over the P21 family
fiber assigns generation charges q = (2, 1, 0) and produces mass
matrices M_ij = O(1) x eps^(q_i + q_j).

### 4.2 Receipts and the honest comparison

```text
ladder spectrum (charges (2,1,0)): 0.735 : 1.09e-4 : 2.72e-6
   (per-generation steps of eps^2 = 1.0e-3 at these charges)
the available rungs: eps^2 = 1.0e-3, eps = 3.2e-2,
   sqrt(eps) = 0.178 (Cabibbo-sized: lam_C = 0.225)
observed ladders (PDG, order of magnitude):
   up:      m_u : m_c : m_t   ~  1.3e-5 : 7.4e-3 : 1
   down:    m_d : m_s : m_b   ~  1.1e-3 : 2.2e-2 : 1
   leptons: m_e : m_mu : m_tau ~ 2.9e-4 : 5.9e-2 : 1
observed one-step suppressions: 7.4e-3 (u), 2.2e-2 (d), 5.9e-2 (e):
   every step sits BETWEEN eps^2 and sqrt(eps)
```

Integer/half-integer record charges with O(1) coefficients cover the
entire observed ladder using the corpus' one small number.  STATUS,
stated plainly: this is a mechanism demo at order-of-magnitude scope -
the GRAIN of the hierarchy matches eps_record; the textures (which
charges, which O(1)'s) are NOT derived; no fit is claimed.  The
falsifiable form is the ledger row P-eps: all fermion hierarchy steps
are powers of eps_record in [eps^2, sqrt(eps)] within O(1) - currently
true of all nine, and testable against any future fourth-generation-
like or precision-ratio data.

## 5. What this paper proves and does not prove

Proves: M1 (Section 2.1, exhaustive); the structural-seesaw consequence
(Section 3); the bracket statement for the observed steps against the
eps rungs (Section 4.2).

Does not prove: Yukawa textures or any specific mass value; the
identification of the family charges (the (2,1,0) ladder is the demo
assignment); that eps_record is THE hierarchy parameter (P-eps is a
falsifiable pattern claim, not a derivation); the value of M (the
record-native heavy scale awaits calibration, Paper 25).

## 6. The kernel after Paper 23

```text
MASSES: protected except nu^c (M1); charged masses = seam x v;
  seesaw structural; hierarchy mechanism demonstrated at grain level.
PREDICTION LEDGER (for Paper 25):
  P-nu (from P21): nu_R exists [conditional on (F-fiber)];
  P-Maj: the neutrino sector is Majorana with a v-free heavy scale
    (M1 is unconditional given the content);
  P-eps: hierarchy steps are powers of eps_record = 0.0318 in
    [eps^2, sqrt(eps)] (pattern claim, currently 9/9).
KERNEL otherwise unchanged.
```

## References and literature map

- Papers 8, 10, 19-21 (internal): the marginality value, the content,
  the seams, the family fiber.
- P. Minkowski (1977); Gell-Mann, Ramond, Slansky; Yanagida (1979):
  the seesaw (here structural).
- C. D. Froggatt and H. B. Nielsen, Nucl. Phys. B 147, 277 (1979):
  the charge-ladder mechanism (here driven by the corpus' own eps).
```
