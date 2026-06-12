# Paper 45 (v6) - SHARD: The Currency Campaign - Energy, Modular Charge, and Where Universality Lives

Preprint, not peer reviewed, version 2026-06-12 (v5, revised
under hostile review run until pass; correction record in
section 0b — five trial rows fired, withdrawn, or corrected,
all kept visible, twice including corrections of the review
process's own earlier fixes).

Author: Felix Robles Elvira

Subtitle:

```text
The successor campaign named by P44: compute the exact T00 -> K
map (the entanglement Hamiltonian of the block, Williamson
route) and ask whether the gravitational response is UNIVERSAL
IN MODULAR CHARGE.  The float wall is real: the block has modes
pure beyond double precision, so every exact statement is
anchored in 80/90-digit arithmetic with declared floors,
per-anchor floor sweeps, censuses, and conventions - and five
trial rows died on the way, all kept visible.
RESULT 1 - THE GRADING: charge convergence is an OVERLAP-vs-
MODULAR-SPECTRUM RACE, receipted on three axes and QUANTIFIED
(clipped-set overlap mass 1.4e-7 coherent vs 3.36 bulk
dipole): width-graded (w6/w3/w2/w1 floor growths +0.0000/
+0.0010/+0.0190/+0.1575), position-graded (near-cut dipoles at
70/72/75 CONVERGE - +0.0000/+0.0000/+0.0063, all printed -
while bulk dipoles ride a linear staircase, block total
FINITE, span 252-349 under bottom-position uncertainty), and
SPECTRUM-graded (gapped blocks tighten the race - the W4 floor
sweep is the receipt; 'smooth probes converge' is scoped to
the massless block).  'Divergent modular price' is the
continuum limit: conjectured, registered, not computed.
RESULT 2 - THE EXACT FIRST-LAW LADDER (eight rungs, no
regulator anywhere): dS/(a d<K_exact>) = 0.7453 -> 0.8566 ->
0.9168 -> 0.9510 -> 0.9768 -> 0.9901 -> 0.9946 -> 0.9974 for
a = 1e-6 .. 1e-20, monotone, every ratio < 1 (exact
relative-entropy positivity).  HONEST LOGIC (T5): the
MODEL-INDEPENDENT statement is the last-rung bound, FLOOR-
rounded (bounds round in the safe direction - a review
correction): the limit is >= 0.9973, sub-unity saturation
confined below 0.0027; completion to 1 is consistent, not
excluded beyond that bound.  The first law itself is the imported structural
identity (Blanco-Casini-Hung-Myers): the campaign's content
is that the CHARGE EXISTS (graded) and the approach structure
is MEASURED to 1e-20.
RESULT 3 - THE CURRENCY MAP, ZERO-AMPLITUDE LIMIT IDENTIFIED:
the kernel ratio r(d) is amplitude-free; the measured response
approaches it from below at every depth; the float ladder
lands on the exact ladder (0.7895 vs 0.7842 - a float-
validation receipt, corollary of Result 2).  r_exact = 0.9072
at the anchor (offset spread 0.040 disclosed; float clip-12
low by 9.2%).  The channel HIERARCHY (coherent >> UV) is
clip-robust; the channel VALUES are clip-referenced and
clip-swept on the gapped block (coherent row 0.741/0.852/0.926
across clips - no exact anchor there, registered).
RESULT 4 - FAMILY-RESOLVED TREND + FLAT FLOW: families do NOT
collapse (max deviation 7.7%, computed); the w6 family RISES
through its window; BW-normalized, the exact anchor reaches
r/g_box = 0.980 (offset spread 0.958-1.002, printed):
completion to the box target is FAVORED only as this receipted
rising trend - the registered open edge.  The amplitude-free
flow at fixed l/d is flat (drifts +0.0024 -> +0.0008,
clip-robust): the clean t8.
RESULT 5 - EP, THE HONEST DECOMPOSITION (T4 + T5): P44's
measured kill (2.12) factors into (i) a FINITE-AMPLITUDE
S_rel factor - dominant, present in EITHER currency, receipted
in direction only (measured series stuck near 2.03-2.04 at
a_ref/64) - and (ii) the ZERO-AMPLITUDE currency-map species
dependence: EP_exact = 1.027 [1.025-1.029 tail-model bracket],
from the floor-swept exact anchor (per-species sweeps printed;
the single-floor 1.092 of an earlier pass was itself
floor-dominated, kept as T4).  Equal lattice-T00 sources of
the two species differ in modular response by 2.7% of the
response (2.4% of the kill magnitude; denominators stated) at
zero amplitude - the genuine currency residue, hydrodynamic
fate open.  The earlier '98% currency artifact' conflated (i)
with (ii) and is withdrawn (T5).
NET: where the modular charge converges - graded as receipted
- the first law holds with its approach measured to 1e-20 and
its limit bounded within 0.27% of universality.  The 3+1
planar FIRST LAW AT SCREENS: capacity responds to modular
charge at rate 1/(4 nu) on the coherent sector; the
geometry-field (response-law) form remains at its P43/P44
receipted scope.
```

## 0. Design, trial record, receipts

Receipts: `code/v6_p45_currency_campaign.py`, canonical
`/tmp/v6_p45_campaign.out`, bit-identical rerun verified,
kill-ledger lines generated from computed flags, no hardcoded
constants (all formerly-prose numbers computed and printed).
Instrument: $K = \tfrac12(x K_x x + p K_p p)$, $K_x =
M^{-1}W\,\mathrm{diag}(F\nu)W^{T}M^{-1}$, $K_p =
MW\,\mathrm{diag}(F/\nu)W^{T}M$, $M = G_X^{1/2}$, $F(\nu) =
\log\frac{\nu+1/2}{\nu-1/2}$; $\delta\langle K\rangle =
\tfrac12\mathrm{Tr}(K_x\delta G_X)$, exactly linear.  Pairing
receipt $10^{-14}$.  Exact statements at dps 80 (dps 90 at the
W4 anchor) with declared floors and per-anchor floor sweeps.

## 0b. The correction record (hostile review, run to pass)

- **T1 (fired, kept).**  Naive first-order kill at $a = 10^{-7}$:
  fired at $1.2\times10^{-1}$ — the gap is the relative-entropy
  mode-staircase plus clip mismatch; superseded by the ladder.
- **T2 (fired, kept).**  v1 EP comparison vs P44's 2.12 at
  $a_{\rm ref}$: fired at 15.2% — amplitude-mismatched.
- **T3 (withdrawn).**  Float clip-12 EP "prediction" 1.802:
  regulator-dominated (sweep 1.848/1.802/1.749; per-species
  float deficits 35%/63%, printed).
- **T4 (corrected).**  The first exact EP anchor (1.092 at one
  floor) was itself floor-dominated ($m = 0.8$ is spectrally
  UV).  Per-species floor sweeps now run at every exact anchor;
  floor-converged EP$_{\rm exact}$ = 1.027 [1.025–1.029].
  Lesson: *every exact anchor carries its own floor sweep.*
- **T5 (withdrawn/corrected).**  (a) "Saturation excluded above
  ~0.99" was **unsound**: a saturating gap $g_0$ + falling tail
  reproduces falling gap ratios for any $g_0$ below the last
  gap.  Only the model-independent last-rung bound stands; the
  ladder was extended to $a = 10^{-20}$ (bound $\ge 0.9973$,
  floor-rounded — bounds round in the safe direction, a
  further review correction) and the falling-ratio kill
  clause retired as post-hoc.
  (b) "~98% currency artifact" **conflated** the
  finite-amplitude $S_{\rm rel}$ factor (present in any
  currency) with the currency map's species dependence; the
  decomposition is now stated with denominators.  (c) The
  channel-anatomy coherent row is regulator-spread on the
  gapped block (~20%, spread/max basis) — all rows now clip-swept
  and clip-referenced; T4's lesson applied to its own paper.
- **R-1..R-6 (earlier waves, kept):** finite-block staircase
  (span printed); grading not dichotomy (near-cut dipoles
  converge — now printed for 70/72/75); window-edge crossing
  computed ($0.9312/0.9750/1.0058$); family conflation
  withdrawn (max deviation 7.7% computed); offset conventions
  disclosed ($0.9278/0.9072/0.8875$); the float-degeneracy
  trap (set sums only); the matched-screen comparator (P44's
  $j = 104$: 2.106, not the adjacent 2.124).

## 1. The grading — where the currency exists

At the exact anchor (dps 80; 39/60 modes below the $10^{-45}$
floor, max unclipped $F = 102.5$):

```text
                        dK/a (f45)   30->45     45->60
  Gaussian w6@90           0.8876    +0.0002    +0.0000
  Gaussian w3@90           3.5634    +0.0261    +0.0010
  Gaussian w2@90           7.7556    +0.1204    +0.0190
  Gaussian w1@90          22.8423    +0.3433    +0.1575
  dipole @70 (near cut)   28.1534    +0.0000    +0.0000
  dipole @72 (near cut)   46.7695    +0.0069    +0.0000
  dipole @75 (near cut)   73.9320    +0.2895    +0.0063
  dipole @90 (bulk)       87.7944    +0.4978    +0.3280
  dipole @110 (bulk)      87.9267    +0.4996    +0.3325
```

Coherent anchor: floor-stable $+2.5\times10^{-7}$, unclipped
share 0.9999960 (K-IR ok).  Bulk dipole: linear staircase
$1.93$/decade — block total finite (~291 for a bottom at
$\eta \sim 10^{-150}$; span 252–349 printed; finiteness is the
receipt, the total illustrative).  **The race, quantified:**
clipped-set overlap mass $1.4\times10^{-7}$ (coherent) vs 3.36
(bulk dipole, both unit-norm).  Three axes: width, position
(the near-cut crossover now printed at 70/72/75), and spectrum
(gapped blocks tighten the race — the W4 sweep; "smooth probes
converge" is massless-block-scoped, T4).

## 2. The exact first-law ladder — measured to 1e-20

$$\frac{\delta S}{a\,\delta\langle K\rangle_{\rm exact}}:
0.7453,\ 0.8566,\ 0.9168,\ 0.9510,\ 0.9768,\ 0.9901,\ 0.9946,\
0.9974 \;\;(a = 10^{-6}..10^{-20})$$

— monotone; every ratio $< 1$ (exact $S_{\rm rel}$ positivity);
gap ratios per 100×: $0.56/0.58/0.59/0.47/0.43/0.54/0.49$.
**Honest logic (T5):** the model-independent statement is the
last-rung bound — the limit is $\ge 0.9973$ (last rung $0.9973602$,
floor-rounded; bounds round in the safe direction — a review
correction), sub-unity saturation confined below $0.0027$
(ceil-rounded); completion to 1 is consistent (deep-rung
geometric fits compatible with $g_0 = 0$) but *not excluded
from below* beyond that bound.  The
first law itself is the imported structural identity
(Blanco–Casini–Hung–Myers); the campaign's content is that
**the charge exists** (§1) and **the approach structure is
measured** — plus the float window scoping: the clip-12 tables
are corroboration with a computed window edge (the clipped
ratio crosses 1 between $a = 10^{-9}$ and $10^{-10}$:
$0.9312/0.9750/1.0058$).

## 3. The currency map — zero-amplitude limit identified

The kernel ratio $r(d)$ is amplitude-free; measured responses
approach it from below at every P44 depth (K-G, +0.02 declared
tolerance).  The float ladder lands on the exact ladder
($0.7895$ vs $0.7842$) — a **float-validation receipt**
(corollary of §2, not independent evidence).  At the anchor:

$$r_{\rm exact} = 0.9072 \quad (\text{offsets } 0/\tfrac12/1:\
0.9278/0.9072/0.8875;\ \text{float clip-12 low by } 9.2\%).$$

Channel anatomy ($m = 0.2$, $d \sim 20$), all rows clip-swept
(clips $10^{-10}/10^{-12}/10^{-14}$): coherent w6
$0.741/0.852/0.926$; dipole train $0.096/0.115/0.134$; single
dipole $0.098/0.118/0.137$.  **The hierarchy (coherent ≫ UV)
is clip-robust; the values are regulator-spread on this gapped
block** (no exact anchor at this config — registered; T4's
lesson applied).

## 4. Family-resolved trend, flat flow — and the open edge

```text
  w6:  (0.273: 0.885|0.928) (0.176: 0.767|0.806) (0.130: 0.637|0.663)
       (0.103: 0.541|0.549) (0.086: 0.466|0.454) (0.073: 0.405|0.373)
  w10: (0.312: 0.902|0.949) (0.227: 0.845|0.881) (0.179: 0.778|0.793)
  w16: (0.381: 0.907|0.949) (0.296: 0.907|0.930) (0.242: 0.901|0.892)
       (0.205: 0.864|0.812) (0.178: 0.809|0.709) (0.157: 0.766|0.610)
  exact anchor: r = 0.9072, r/g_box = 0.9795
               (offset spread 1.002 / 0.980 / 0.958)
```

Computed: max family deviation 7.7%; droop ($N128 \to 256$,
clip-12) 2.6%.  The w6 family rises through its window;
**completion to the box target is favored only as this
receipted rising trend**; the offset, droop, and family spreads
stack into the registered open edge (wider-window exact anchors
named).  The amplitude-free flow at fixed $\ell/d$: flat,
drifts $+0.0024 \to +0.0008$ over ×8, clip-robust (clean t8).

## 5. First law per class (float window)

All 8 class × species rows rise monotonically in-window (K-UNIV
ok); window positivity $7\times10^{-2}$; window edge computed
(§2).  Clip-referenced corroboration of §2; the window limits
are config-dependent (the $\sim 1.08$ figure is the $m = 0$
anchor's; gapped configs differ — scoped).

## 6. EP — the honest decomposition

At the half-scale analog of P44's W4 config (dimensionless
ratios matched; comparator: P44's **matched screen** $j = 104$ reads 2.106;
the half-scale match quality is ~1% (2.123 vs 2.106, the
honest cross-scale receipt), while the full-config 2.104 vs
2.106 agreement is currency-trivial (boost-per-dE 1.0012, a
P44 canonical receipt);
the adjacent-screen 2.124 used earlier is retired), with
per-species floor sweeps at dps 90:

```text
  m = 0.4: 0.9793 -> 0.9902 -> 0.9902 -> 0.9902 (conv 0.9902)
  m = 0.8: 0.7503 -> 0.9065 -> 0.9543 -> 0.9625 (conv 0.9642)
  EP at the floors: 1.305 -> 1.092 -> 1.038 -> 1.029
  EP_EXACT (floor-converged) = 1.027  [1.025 - 1.029]
```

(float clip-12 low by 35%/63% — the mass-asymmetric clip error
that manufactured the withdrawn 1.802; T4's single-floor 1.092
kept visible.)  Measured series: half-scale $2.123 \to 2.065
\to 2.042$; full-config $2.104 \to 2.051 \to 2.030$ — above
EP$_{\rm exact}$, decreasing (K-EP-X ok), $S_{\rm rel}$-
dominated throughout.

**The decomposition (T5):** P44's measured kill factors into
(i) a **finite-amplitude $S_{\rm rel}$ factor** — dominant,
present in *either* currency, receipted in direction only (the
series are stuck near 2.03–2.04 at $a_{\rm ref}/64$); and (ii)
the **zero-amplitude currency-map species dependence**,
EP$_{\rm exact}$ = 1.027 [1.025–1.029]: equal lattice-$T_{00}$
sources of the two species differ in modular response by
**2.7% of the response** (2.4% of the 2.12-vs-1 kill magnitude;
denominators stated) at zero amplitude.  The earlier "98%
currency artifact" conflated (i) with (ii) — withdrawn.  In the
exact modular currency EP is the first-law identity (§2) —
machinery.  Scale transfer to P44's full config: registered
(dimensionless match; full-config exact anchor named).

## 7. Kill ledger

```text
  K-INST-i   frequency pairing (1e-14)        -> did not fire
  T1 (v1)    first-order at 1e-7 (1.2e-1)     -> FIRED (kept)
  K-IR       coherent floor-stable + share    -> did not fire
  K-STAIR    bulk-dipole staircase            -> did not fire
             (finite block total, span printed)
  GRADING    near-cut dipoles converge (70/72/75 printed);
             race quantified (1.4e-7 vs 3.36); spectrum-scoped
  K-UNIV     per-class monotone (float window) -> did not fire
  K-EXACT-FL ladder: monotone, all < 1, the
             a=1e-20 rung >= 0.99 (named rung;
             bound L >= 0.9973, floor-rounded)  -> did not fire
             (v4 falling-ratio clause RETIRED as post-hoc, T5)
  K-REL'     exact-currency S_rel > 0          -> did not fire
  W1c        window edge computed (1e-9..1e-10) -> receipted
  K-G        measured approaches kernel ratio
             (+0.02 declared tolerance)        -> did not fire
  T2 (v1)    EP vs 2.12 at a_ref (15.2%)       -> FIRED (kept)
  T3 (v2)    quantitative float EP pass        -> WITHDRAWN
  T4 (v3)    EP anchor at single floor (1.092) -> CORRECTED
             (floor sweep -> 1.027 [1.025-1.029])
  T5 (v4)    'saturation excluded above 0.99'  -> WITHDRAWN
             (only the last-rung bound stands); '98% currency
             artifact' -> CORRECTED (decomposition stated)
  K-EP-X     measured > EP_exact, decreasing   -> did not fire
  W2b: families do not collapse (7.7% computed); anchor
       r/g_box 0.980 (offset spread printed); completion
       FAVORED as the rising trend only - open edge
  W3:  flow flat, drifts shrinking, clip-robust
  boost-offset convention spread 0.040 (declared +1/2)
  (W1c is a receipt row, printed in the canonical's W1b
   section; ledger generated from computed flags)
```

## 8. Verdict — what the currency buys the gravitational program

Where the modular charge converges — graded by the quantified
overlap-vs-spectrum race, on three receipted axes — the first
law $\delta S = \delta\langle K\rangle$ (the imported
structural identity) holds with its approach **measured to
$a = 10^{-20}$ and its limit bounded within 0.27% of
universality** (§2, floor-rounded bound).  The campaign's deliverables: the charge
*exists* on the coherent sector (the nontrivial part); the
currency map converting lattice energy to modular charge is
measured, with P44's form factor, channel hierarchy, and
amplitude drift as its structure and the zero-amplitude limit
identified at the exact anchor (§3); the EP kill honestly
decomposed — amplitude physics dominant, a genuine **2.7%
zero-amplitude currency residue** at finite $\ell/\xi$
(bracketed, floor-swept; §6); and the hydrodynamic trend rising
toward the finite-box BW target with completion favored as a
trend and an honestly stacked uncertainty budget (§4).  For
the program's ledger: the 3+1 planar **first law at screens**
is universal in modular charge on the coherent sector within
the stated bounds; the *response-law/geometry-field* form
remains at its P43 (2d, receipted) and P44 (within-class,
scoped) status.  Named follow-ups: wider-window exact anchors;
the full-config exact EP anchor; spherical screens; tensor
structure; Lorentzian dynamics.  NOT claimed: any of those;
ν's closed form; the continuum limit; the continuum fate of
the UV charge; the last 0.27% of the ladder; the last few
percent of the hydrodynamic trend.

## Receipts

```text
code/v6_p45_currency_campaign.py     the campaign
/tmp/v6_p45_campaign.out             canonical (BIT-IDENTICAL,
                                     ledger from computed flags)
instrument: pairing 1e-14; clip sweep 0.6922..0.8851; T1 1.2e-1.
anchor (dps 80): 39/60 below floor 1e-45; max unclipped F =
102.5; grading table incl. dipoles @70/72/75/90/110
(28.15/46.77/73.93/87.79/87.93; growths printed); staircase
58.6/87.8/116.6 (1.93/decade, total ~291, span 252-349); race
1.4e-7 vs 3.36; dipole floor-set share 99.2%; coherent dK/a
0.887561, +2.5e-7, share 0.9999960, tail 5.3e-8; r_exact
0.9072 (offsets 0.9278/0.9072/0.8875); float low by 9.2%/5.8%.
exact ladder (8 rungs): 0.7453/0.8566/0.9168/0.9510/0.9768/
0.9901/0.9946/0.9974; gap ratios 0.56/0.58/0.59/0.47/0.43/
0.54/0.49; bound L >= 0.9973 (floor-rounded, T5).  window edge 0.9312/0.9750/
1.0058.  float ladder 0.4511 -> 0.7162; overlap 0.7895 vs
0.7842.  W1 8 rows monotone; positivity 7e-2.  W2 r(d) ok;
channel sweep: 0.741/0.852/0.926, 0.096/0.115/0.134,
0.098/0.118/0.137.  W2b tables; anchor r/g_box 0.9795 (spread
1.002/0.980/0.958); family dev 7.7%; droop 2.6%.  W3 flow
+0.0024 -> +0.0008.  W4 floor sweeps: 0.9793..0.9902 (conv
0.9902), 0.7503..0.9625 (conv 0.9642); EP floors 1.305/1.092/
1.038/1.029, converged 1.027 [1.025-1.029]; float deficits
35%/63%; T3 sweep 1.848/1.802/1.749; measured half 2.123/
2.065/2.042, full 2.104/2.051/2.030; comparator: P44 matched
screen j=104 = 2.106.
Literature: Bisognano-Wichmann; Eisler-Peschel; Peschel;
Casini-Huerta; Cardy-Tonni; Williamson; Audenaert-Eisert-
Plenio-Werner; Araki / Lindblad; Blanco-Casini-Hung-Myers;
Faulkner et al.; Jacobson (1995, 2015); Wall; BKLS; Srednicki.
```
