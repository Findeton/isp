# Paper 48 (v6) - SHARD: The Hydrodynamic Completion - the Boost Law on the Energy-Width Axis, and the EP Residue as a Cutoff Artifact

Preprint, not peer reviewed, version 2026-06-12.

Author: Felix Robles Elvira

Subtitle:

```text
The currency campaign's two registered open edges are resolved
by measurement.  THE INSTRUMENT IS REBUILT FIRST: (i) the
probe's physical scale is its ENERGY width - for the massless
chain the coherent perturbation's energy is pure gradient, so
the probe amplitude and the probe energy are different objects
(Hann^2: l_v = 0.5658 W vs l_E/W = 1.064-1.071; receipted
identities) - and the window is quoted on the measured l_E/d;
(ii) enclosure is a PER-ANCHOR RECEIPT (computed leakage, kill
K-LEAK at exactly 0.0) - exactly-enclosed Hann^2 probes cap at
l_v/d <= 0.566, i.e. l_E/d ~ 1.07, and a SECOND compact family
(flat-top plateau probes, energy in the taper bands) extends
the exactly-enclosed window to l_E/d = 1.26; (iii) the float
regulator droop is receipted PER ANCHOR at identical geometry,
not inferred; (iv) anchors are ADMISSIBLE only through floor
gates (1e-2), with fragile anchors excluded by declared rule -
band-concentrated energy is floor-fragile (the near-cut
regime): one plateau anchor is excluded and listed; (v) a
DIFFERENTIAL RECEIPT - matched-depth anchor pairs difference
out the boost-offset convention - sees below the offset
systematic; (vi) a BOX RECEIPT - the same anchors at N = 240,
far wall receding - tests what the differential finds.
RESULT 1 - COMPLETION, ON BOTH FAMILIES, STRICT ON CENTRALS,
AND THE PERCENT-LEVEL DRIFT RESOLVED AS A BOX RESIDUAL: exact
floor-swept anchors give r_exact/g_box =
0.995/0.996/0.991/0.989 (Hann^2, l_E/d = 0.31-1.01) and
0.985/0.981 (plateau, to l_E/d = 1.26): every admissible
anchor sits within 0.03 of 1 on CENTRAL VALUES at the declared
+1/2 offset (gaps 0.0044-0.0192; the criterion is anchored to
that declared convention - stated).  The float 0.93-0.95
plateau is regulator droop, receipted at identical geometry
per anchor (float r/g_box 0.57-0.95 vs exact 0.98-1.00).  THE
SHAPE FORK RESOLVES ROBUST: the resolvable pair (l_E/d 0.95 vs
0.88) agrees - 0.9907 vs 0.9853, |delta| = 0.0055 vs combined
systematic 0.094 (a coarse yardstick; power note printed).
THEN THE INSTRUMENT SEES BELOW ITS OWN SYSTEMATIC: the
differential receipt finds a convention-robust 1.4-1.6%
downward drift across the top half of the window (h12 - p21:
+0.0140..+0.0154 at every offset) - and THE BOX RECEIPT
RESOLVES IT: at N = 240 (identical probes, x0, d; far wall
receding) the differential LOSES ITS SIGN (-0.0043..-0.0021)
and the matched anchors sit within 0.5% of the target
(r/g_box = 1.0011/1.0044/1.0043).  THE BEND was a finite-box
residual, not saturation: raised by one receipt, resolved by
the next.
RESULT 2 - THE EP RESIDUE IS A CUTOFF ARTIFACT (RECEIPTED ON
THE GAUSSIAN FAMILY): the registered hydrodynamic reading
comes back NO (EP_exact(d) = 1.0280/1.0277/1.0142 at
d = 13/16/20, monotone - the residue does NOT dissolve with
l_E/d; adverse answer stated), and the residue is probe-shape
dependent at half scale (plateau pair 1.0014 vs Hann^2
1.0280).  What moves it is the CUTOFF: the three-rung ladder
at fixed dimensionless geometry (N = 64/128/256, dps 90,
floors to 1e-75; the tail-model conservativeness q23 < q12 is
a computed flag - the bracket is conservative) reads
EP_exact = 1.0938 [1.0938-1.0945] -> 1.0270 [1.0270-1.0288]
-> 1.0061 [1.0061-1.0085]: |EP - 1| = 9.4% -> 2.7% -> 0.6% on
extrapolated centrals, MONOTONE TOWARD 1 ACROSS THE BRACKETS
(robust: true for any value inside them).  THE SPECIES
STRUCTURE IS THE RECEIPT BEHIND THE READING: both species
individually approach the boost law as 1 - r ~ C (m a)^2,
with deviation ratios (1-r_h)/(1-r_l) = 3.24/3.66/3.43 vs
(m_h/m_l)^2 = 4 - the m^2 a^2 artifact signature; EP -> 1 is
its corollary.  Step shrink factors [3.2, 3.5] / [3.1, 4.8]
across brackets - same order as the O(a^2) factor 4 (an
observation; the quarter rung is deep-lattice, heavy
xi = 0.625 a).  The half rung is consistent with the currency
campaign's 1.027 [1.025-1.029] (computed overlap flag); the
half -> full brackets are DISJOINT (computed flag): the registered
transfer assumption is corrected by receipt, and the 'genuine
species residue' reading with it - a lattice artifact of the
coarse heavy species (xi = 1.25 a at half scale), dissolving
toward the continuum.  No scale-invariant zero-amplitude EP
violation survives at planar scope (receipted on the Gaussian
family; compact-probe continuum EP registered).
NET, for the gravitational ledger: at planar scope, at
first-law scope, in the modular currency, the response to
coherent energy COMPLETES to the finite-box BW target across
the exactly-enclosed hydrodynamic window (l_E/d to 1.26, two
probe families, strict on centrals, the percent-level drift
resolved as a box residual), and the species residue
dissolves toward the continuum.  NOT claimed: continuum
beyond the box; spheres, tensor components, Lorentzian
dynamics; compact-probe continuum EP; anything beyond the
quoted per-anchor systematics and brackets.
```

## 0. Questions, instruments, forks

The currency campaign (P45) ended with two quantitative edges.
*Completion*: the coherent kernel ratio $r = \delta\langle K
\rangle/\delta\langle K_{\rm boost}\rangle$ reached $r/g_{\rm
box} = 0.980$ at its single exact anchor, with the window
capped by Gaussian probe tails - does the map complete to the
finite-box BW target at the hydrodynamic end, or saturate?
*EP*: the half-scale species anchor gave ${\rm EP}_{\rm exact}
= 1.027\,[1.025\!-\!1.029]$, with transfer to the full
configuration registered, not receipted - is the residue a
property of the map, or a cutoff artifact of the coarse heavy
species ($\xi = 1.25$ lattice units at half scale)?

**The energy-width axis.**  For the massless chain a coherent
perturbation $\delta G_X = \varepsilon\, vv^\top$ carries pure
*gradient* energy: $\delta T_{00} \sim (\nabla v)^2$.  The
probe's amplitude width and its energy width are different
objects - receipted as lattice identities: for Hann$^2$
($v = \cos^2$ on support $W$), $\ell_v = 2\sigma(v^2) =
0.5658\,W$ at every $W$, while $\ell_E = 2\sigma(\delta T_{00})
= 1.064$-$1.071\,W$ (the energy lives in a ring).  The window
is therefore quoted on the *measured* $\ell_E/d$.  Enclosure
is exact only for $d \ge W$, so exactly-enclosed Hann$^2$
probes cap at $\ell_v/d \le 0.566$ - i.e. $\ell_E/d \approx
1.07$.  One stated limit: for the plateau family the energy is
two disjoint bands, so its $\ell_E$ measures band *separation*
(it is nearly constant across that family's depth sweep) -
cross-family "matched $\ell_E/d$" matches a statistic that
weighs the families differently; the matched-depth
differential below is the finer cross-family instrument.

**Two probe families.**  Because $\ell_E$ alone need not be a
sufficient statistic, a second compact family is run: flat-top
*plateau* probes ($v = 1$ on $|x-x_0| \le P$, $\cos^2$ taper of
width $T$; same $C^1$ class), whose energy concentrates in the
taper bands - by design a different energy profile.  Band
width is the floor-stability scale: the family is validated at
taper $T = 14$ (floor growth $+9.8\times10^{-4}$, K-PROBE2;
the Hann$^2$ gate reads $+6.2\times10^{-4}$, K-PROBE), and
band-concentrated energy sits toward the near-cut regime, so
every anchor passes its own 1e-2 floor gate or is excluded by
declared rule.

**Per-anchor receipts.**  Every compact anchor prints its
computed leakage (kill K-LEAK fires unless exactly $0.0$ at
every anchor), its mpmath floor sweep (dps 80, floors
$10^{-30}/10^{-45}/10^{-60}$; kill K-FLOOR on the Hann$^2$
headline family at 1e-2), its boost-offset spread (offsets
$0/\tfrac12/1$; the P44 $+\tfrac12$ convention declared), and
its float clip-14 ratio at *identical geometry* - the
regulator droop is receipted, not inferred.  The float trend
map is context only, with no verdict weight (declared).

**The differential and box receipts.**  Matched-depth anchor
pairs (h12/h20/p21 at $d = 22/21/21$) difference out the
boost-offset convention almost exactly - the instrument that
sees *below* the offset systematic; the flag is defined on the
h12-p21 endpoint pair (declared), and the sub-pairs decompose
any drift into an intra-family and a cross-family leg.  What
the differential finds, the BOX RECEIPT tests: the same three
anchors - identical probes, $x_0$, $d$ - recomputed exactly at
$N = 240$, the far wall receding.  Box-stable, box-sensitive,
and sign-loss branches all declared in advance; no directional
kill on either receipt.

**The forks, pre-registered.**  COMPLETION (per family): the
family's top-of-window $r_{\rm exact}/g_{\rm box}$ sits within
$0.03$ of 1 *on central values* (strict proximity) AND 1 lies
within the per-anchor systematic (consistency) - both printed.
The strict criterion is anchored to the declared $+\tfrac12$
convention (stated; convention-robust statements live in the
differential receipt).  SATURATION: the top central sits below
1 beyond the stacked systematic; the zone between is
UNRESOLVED and says so.  SHAPE: matched $\ell_E/d$ pairs
across the families agree within combined systematics (ROBUST)
or not; pairs resolve only on admissible anchors.

Receipts: `code/v6_p48_hydrodynamic_completion_campaign.py`,
canonical `/tmp/v6_p48_campaign.out`, bit-identical rerun
verified; ledger generated from computed flags.

## 1. The completion curve

Exact anchors at $N = 192$, all leakages exactly $0.0$
(K-LEAK), float-droop receipts at identical geometry beside
each:

```text
  Hann^2 family (K-FLOOR did not fire):
  l_E/d = 0.306 (W=8,  d=28): float 0.5757 | r_exact = 1.0129
    [floor +8.5e-3; offsets 3.5%]  g_box = 1.0179
    r/g_box = 0.9952 +- 0.044   excludes plateaus below 0.952
  l_E/d = 0.582 (W=12, d=22): float 0.8588 | r_exact = 0.9976
    [floor +1.5e-3; offsets 4.4%]  g_box = 1.0020
    r/g_box = 0.9956 +- 0.046   excludes plateaus below 0.950
  l_E/d = 0.947 (W=16, d=18): float 0.9387 | r_exact = 0.9812
    [floor +5.9e-4; offsets 5.4%]  g_box = 0.9904
    r/g_box = 0.9907 +- 0.055   excludes plateaus below 0.936
  l_E/d = 1.014 (W=20, d=21 - the enclosure cap):
    float 0.9436 | r_exact = 0.9893
    [floor +5.7e-4; offsets 4.7%]  g_box = 1.0000
    r/g_box = 0.9893 +- 0.047   excludes plateaus below 0.942

  plateau family (P=6, T=14; admissibility by declared rule):
  l_E/d = 0.564 (d=47): EXCLUDED (floor growth +3.2e-2 > 1e-2;
    exploratory row, no exclusion claimed: 0.9786 +- 0.053)
  l_E/d = 0.884 (d=30): float 0.8022 | r_exact = 1.0014
    [floor +6.8e-3; offsets 3.3%]  g_box = 1.0164
    r/g_box = 0.9853 +- 0.040   excludes plateaus below 0.946
  l_E/d = 1.262 (d=21 - past the Hann^2 cap):
    float 0.8337 | r_exact = 0.9753
    [floor +1.7e-3; offsets 4.7%]  g_box = 0.9944
    r/g_box = 0.9808 +- 0.048   excludes plateaus below 0.933
```

**The fork resolves: COMPLETION, on both families, strict on
centrals.**  Every admissible anchor sits within $0.03$ of 1
on central values at the declared $+\tfrac12$ offset - the
registered strict criterion passes with no systematics slack
(gaps $0.0044$-$0.0192$; Hann$^2$ top: $0.9893$ at $\ell_E/d =
1.01$, gap $0.0107$; plateau top: $0.9808$ at $\ell_E/d =
1.26$, gap $0.0192$).  The criterion is anchored to the
declared convention - at other offsets the centrals shift
coherently within the printed spreads, and only the
differential receipt below is convention-robust (stated).
The float map's $0.93$-$0.95$ plateau is regulator droop at
these anchors' own geometries - the per-anchor receipts read
float $0.58/0.86/0.94/0.94$ (Hann$^2$) and $0.80/0.83$
(plateau) against exact $r/g_{\rm box} = 0.98$-$1.00$.
Saturation is excluded below the per-anchor floors
($0.93$-$0.95$).

**The shape fork resolves: ROBUST - with low power, stated.**
The resolvable pair sits at $\ell_E/d = 0.95$ vs $0.88$ (both
printed): $0.9907$ vs $0.9853$, $|\Delta| = 0.0055$ against a
combined systematic of $0.094$ - a coarse yardstick that only
a gross shape effect could fail.  The second pair is not
resolvable (its plateau anchor is the excluded one) and says
so.  Within that power, the completion diagnostic is a
property of the energy distribution, not the probe shape - and
the plateau family carries the exactly-enclosed window past
the Hann$^2$ cap to $\ell_E/d = 1.26$, still completing.

**The differential receipt - and the box receipt that answers
it.**  Matched-depth differences cancel the offset convention
almost exactly:

```text
  h12 (d = 22) - h20 (d = 21): +0.0054 .. +0.0072  (all offsets)
  h20 (d = 21) - p21 (d = 21): +0.0083 .. +0.0087
  h12 (d = 22) - p21 (d = 21): +0.0140 .. +0.0154
```

A convention-robust downward drift of $1.4$-$1.6\%$ from
mid-window to the top survives every offset choice - finer
than the shape fork's yardstick, invisible to the per-anchor
systematics, and in the data (THE BEND; linear continuation
would have breached the $0.03$ criterion near $\ell_E/d \sim
1.74$-$1.79$).  The declared hypothesis set - residual form
factor, saturation onset, finite-box residual beyond $g_{\rm
box}$, probe-sampling discreteness - is then cut by the box
receipt:

```text
  N = 240 (identical probes, x0, d; far wall recedes):
  [h12] leakage 0.0; floor +2.0e-3; r/g_box = 1.0011
  [h20] leakage 0.0; floor +8.1e-4; r/g_box = 1.0044
  [p21] leakage 0.0; floor +2.7e-3; r/g_box = 1.0043
  h12 - p21 at N = 240: -0.0043 .. -0.0021
                (N = 192: +0.0140 .. +0.0154)
```

**THE BEND resolves: a finite-box residual.**  The
differential *loses its sign* as the far wall recedes, and at
$N = 240$ the matched anchors sit within $0.5\%$ of the
target.  The percent-level drift was the box, not saturation -
raised by one receipt, resolved by the next, both declared in
advance.  What remains beyond the box is the generic
continuum scope, NOT claimed.

## 2. EP - the species question

**The registered hydrodynamic reading comes back NO.**  At
half scale (enclosed Hann$^2$ $W = 12$ anchors, leakage $0.0$):

```text
  d = 13: r(0.4) = 0.9902, r(0.8) = 0.9632 -> EP = 1.0280
  d = 16: r(0.4) = 0.9902, r(0.8) = 0.9635 -> EP = 1.0277
  d = 20: r(0.4) = 0.9901, r(0.8) = 0.9763 -> EP = 1.0142
  (monotone: True; toward 1 at the hydrodynamic end: NO)
```

The residue does *not* dissolve with $\ell_E/d$ - it is
largest at the most hydrodynamic depths.  And it is
probe-shape dependent: the plateau pair at matched $\ell_E/d$
reads ${\rm EP} = 1.0014$ against the Hann$^2$ row's $1.0280$
(shape spread $2.7\%$).  A *scale-invariant* violation is
excluded by what follows; probe-dependent structure is not -
the continuum reading below is receipted for the Gaussian
family and registered for compact probes.

**What moves the residue is the cutoff.**  The three-rung
ladder holds the dimensionless geometry fixed (the P44/P45
Gaussian configuration: $x_0/N = 0.508$, $w/N = 3/32$, $j/N =
13/32$, $mN = 51.2/102.4$) and refines the lattice through it
(dps 90, floors to $10^{-75}$; the Gaussian tails cross the
cut at the percent level at every rung - printed; the ladder's
receipt is the *trend* at fixed dimensionless geometry, under
the tail-bracket discipline).  The tail model's
conservativeness is a computed flag: $q_{23} < q_{12}$ at
every ladder species and rung, so the geometric extrapolation
overshoots and the bracket $[\text{no-tail},
\text{extrapolated}]$ is conservative; all tails $\le 0.2\%$
against the $10\%$ kill threshold (K-EPFLOOR).

```text
  quarter (N =  64, m = 0.8/1.6): EP = 1.0938 [1.0938-1.0945]
                       deviation ratio (1-r_h)/(1-r_l) = 3.24
  half    (N = 128, m = 0.4/0.8): EP = 1.0270 [1.0270-1.0288]
                       deviation ratio                  = 3.66
  full    (N = 256, m = 0.2/0.4): EP = 1.0061 [1.0061-1.0085]
                       deviation ratio                  = 3.43
  |EP - 1| (extrapolated centrals): 9.4% -> 2.7% -> 0.6%
  monotone toward 1 across the brackets (robust): YES
  step shrink factors across brackets: [3.2, 3.5] / [3.1, 4.8]
```

The monotone collapse is *bracket-robust* - true for any
values inside the brackets.  **The species structure is the
receipt behind the reading**: both species individually
approach the boost law as $1 - r \sim C\,(ma)^2$, and the
deviation ratio sits near $(m_h/m_l)^2 = 4$ at every rung -
the $m^2a^2$ artifact signature, with ${\rm EP} \to 1$ as its
corollary.  The step factors are the same order as the
$O(a^2)$ factor 4 - an observation, not a receipt (the
quarter rung is deep-lattice, heavy $\xi = 0.625\,a$: a trend
point, not a scaling-window rung).  The half rung is
consistent with the currency campaign's receipt
($1.027\,[1.025\!-\!1.029]$; computed overlap flag), and the
half $\to$ full brackets are **disjoint (computed flag)**: the currency
campaign's registered transfer assumption is corrected by
receipt, and its "genuine species residue" reading with it.
The residue is a lattice artifact of the coarse heavy species,
dissolving toward the continuum: **no scale-invariant
zero-amplitude EP violation survives at planar scope**
(receipted on the Gaussian family; compact-probe continuum EP
registered).

## 3. Ledger

```text
  K-PROBE   Hann^2 floor-stable (+6e-4)        -> did not fire
  K-PROBE2  plateau floor-stable (+1e-3)       -> did not fire
  K-LEAK    every compact anchor leakage 0.0   -> did not fire
  K-FLOOR   every Hann^2 anchor growth <= 1e-2 -> did not fire
  K-EPFLOOR all species tails <= 10%           -> did not fire
  COMPLETION CURVE (l_E/d axis):
    hann 0.995/0.996/0.991/0.989 at 0.31/0.58/0.95/1.01;
    plat 0.985/0.981 at 0.88/1.26 (one anchor excluded by the
    floor gate, listed) -> fork: COMPLETION on both families
    (strict + consistent); shape fork: ROBUST (low power,
    stated); differential receipt: +0.0140..+0.0154 (h12-p21,
    all offsets) -> box receipt at N = 240: sign LOST
    (-0.0043..-0.0021), anchors within 0.5% of target
    -> THE BEND RESOLVED as a finite-box residual
  EP: d-sweep 1.0280/1.0277/1.0142 - toward-1 reading NO
    (registered adverse answer); shape pair 1.0014;
    CUTOFF LADDER 1.0938 -> 1.0270 -> 1.0061 (brackets above),
    monotone toward 1 YES (bracket-robust YES); deviation
    ratios 3.24/3.66/3.43 vs 4; half-full transfer: DISJOINT
    (computed) - the currency campaign's transfer CORRECTED
  REGISTERED: compact-probe continuum EP (the ladder is
    Gaussian-family); the continuum (beyond-box) fate;
    spherical/tensor/Lorentzian scopes
  (ledger generated from computed flags in the canonical)
```

## 4. Verdict

Resolved by measurement, with the instrument rebuilt to carry
its own receipts.  *Completion*: on the energy-width axis the
coherent currency map completes to the finite-box BW target -
within $0.03$ of 1 on central values at every admissible
anchor, across two probe families, out to the exactly-enclosed
$\ell_E/d = 1.26$ - with the float plateau receipted as
regulator droop at identical geometry and saturation excluded
below the printed floors.  The differential receipt then sees
below the offset systematic and finds a convention-robust
$1.4$-$1.6\%$ drift - and the box receipt resolves it: **THE
BEND was a finite-box residual** (sign lost at $N = 240$,
matched anchors within $0.5\%$ of the target), not saturation.
The instrument saw its own edge and then measured it away.
*EP*: the residue does not dissolve hydrodynamically (adverse
answer stated), is probe-shape dependent at fixed scale, and
collapses monotonically - bracket-robustly - under cutoff
refinement at fixed dimensionless geometry, with the species
deviation ratio pinned near the $m^2a^2$ value 4 at every
rung: a lattice artifact of the coarse heavy species,
correcting the currency campaign's registered transfer
assumption by computed receipt; no scale-invariant
zero-amplitude EP violation survives at planar scope
(receipted on the Gaussian family; compact-probe continuum EP
registered).  For the gravitational ledger: *at planar scope,
at first-law scope, in the modular currency, the response to
coherent energy is the boost law with capacity coupling
$1/(4\nu)$, completing to the BW target at the hydrodynamic
end - universal across species up to a receipted, dissolving
cutoff artifact (Gaussian-family receipted, compact-probe
continuum registered).*  The planar 00-chapter that opened
with P44's form factor closes here at first-law scope; its
remaining registered threads are compact-probe continuum EP
and the generic beyond-box scope.  NOT claimed: continuum
beyond the box; spheres, tensor components, Lorentzian
dynamics; compact-probe continuum EP; anything beyond the
quoted per-anchor systematics and brackets.

## Receipts

```text
code/v6_p48_hydrodynamic_completion_campaign.py  the campaign
/tmp/v6_p48_campaign.out                         canonical
                       (BIT-IDENTICAL, ledger from flags)
W0: Hann^2 identities l_v/W = 0.5658 (W = 8..20), l_E/W =
1.0708/1.0666/1.0652/1.0645; Hann^2 sweep 1.127798/1.131601/
1.132304 (+6.2e-4), Gaussian control +7.2e-7; plateau (6,14)
l_v = 13.93, l_E = 26.51, sweep 0.490636/0.496518/0.497005
(+9.8e-4); leakage 0.0e+0 at both gates.
W1: float context map (l_E/d, r14/g_box): 0.356 -> 0.6565 ...
0.997 -> 0.9431 (context only, declared).
W2: the completion table as printed (7 anchors, one excluded);
admissibility h8/h12/h16/h20/p30/p21 ok, p47 EXCLUDED;
differential receipt +0.0054..+0.0072 / +0.0083..+0.0087 /
+0.0140..+0.0154; box receipt at N = 240: 1.0011/1.0044/
1.0043, differential -0.0043..-0.0021 (sign lost).
W3: d-sweep and ladder as printed; ladder sweeps e.g. full
m=0.4: 10.3948/12.6143/13.3326/13.4685 (tail 0.2%, q12/q23 =
0.324/0.189); cut-crossings printed per rung; half-rung vs
P45: consistent (computed overlap flag); step factors
[3.2, 3.5]/[3.1, 4.8]; deviation ratios 3.24/3.66/3.43.
Reproduction note: the floor clamp nu = 1/2 + floor needs
working precision beyond the floor's digits (this campaign:
dps 80/90 over floors to 1e-60/1e-75); at dps <= 60 the
1e-60 clamp underflows to exactly 1/2.
Literature: Bisognano-Wichmann; Cardy-Tonni; Eisler-Peschel;
Symanzik (lattice artifacts); the currency campaign (P45) and
its instrument lineage; P44 (the form factor and the box
target); Blanco-Casini-Hung-Myers; Jacobson (equation of
state).
```
