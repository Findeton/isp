# Paper 44 (v6) - SHARD: The 3+1 Planar Lift - nu Measured, the Kernel Class-Resolved, and the BW Deficit Resolved As Currency

Preprint, not peer reviewed, version 2026-06-12 (v3, revised
under a hostile review that ran until it passed; correction
record in section 0b — including a correction to one of the
review's own earlier corrections).

Author: Felix Robles Elvira

Subtitle:

```text
The lift of the 2d closure (P43) to 3+1 at planar scope, by the
exact k_perp decomposition: a planar screen in 3+1 is a sum of
1d massive chains (m_eff^2 = 4 sin^2(kx/2) + 4 sin^2(ky/2),
exact - review-verified against a literal 3d lattice), so the
whole lift runs on the instruments of P41-43.  Six trial traps
were caught by the campaign's own cross-checks; hostile review
caught more - including, notably, that the review's own first
benchmark correction was itself wrong - and fixing them CHANGED
THE CONCLUSIONS.  All corrections visible in section 0b.
RESULT 1 - NU IS A NUMBER: the area density of record capacity,
nu_inf = 0.0242620 +- 3e-6, with the extrapolation's log
coefficient DERIVED (beta = 1/6 exactly; free fit 0.1662), the
error a conservative floor (window spread 1.6e-7; variant-form
spread 2.1e-7 across free-beta, +1/L^3, +(ln L)^2/L^2 fits).
G = 1/(4 nu_inf) = 10.304 record units at planar scope.
Finiteness per se is the lattice cutoff (BKLS; Srednicki); the
SHARD content is the ontological reading - lattice as ledger,
not regulator - plus nu as a two-route calibration target.
RESULT 2 - THE AMPLITUDE PROTOCOL: there is NO attained
linear-response regime for entropy probes on lattice vacuum
blocks - GENERIC, not a near-critical feature (m=0 block:
104/108 modes within 1e-6 of purity, g(a) drifting +0.026 ..
+0.024 per halving without converging in the receipted window
down to a = 2e-5; gapped m=0.4 control: 106/108 near-pure,
drifts +0.012/halving).  Consequence: g is DEFINED at a
reference modular amplitude, and all scale-flow statements use
MATCHED delta<K> - declared, not optional.
RESULT 3 - THE KERNEL IS CLASS-RESOLVED, not state-independent:
within a probe class the kernel passes translation consistency
(1.0000), SELF-AMPLITUDE-MATCHED two-bump superposition at
different positions AND amplitudes (0.986 - the genuine ~1.4%
cross-term, cleanly separated from the amplitude artifact), and
restoration with suppression 1656x at pinned coupling;
CROSS-CLASS prediction collapses (suppression 6-7x, kill K-A'
FIRED) and works only through the form factor g(l_eff/d),
itself an approximate collapse with a one-signed +14%
systematic.  'Rigorously state-independent' is WITHDRAWN.
RESULT 4 - THE BW DEFICIT RESOLVED AS CURRENCY (was: 'tension
with Bisognano-Wichmann'): (a) the response law with the
MEASURED weight holds (0.93) while the BOOST first law fails
(0.61): K_lattice != 2 pi sum (x-j+1/2) T00_lattice
(Eisler-Peschel) - the deficit is in the OPERATOR, not the law;
(b) the T00-carrying band of a probe is ALONE NOT EVEN A
PHYSICAL PERTURBATION (purity census: 26 modes below purity,
10 orders above the roundoff floor), and the direct two-state
receipt: a PSD tiling matched to the probe's lattice-T00
profile (shape residual 0.6%, equal energy) differs in modular
response by 4.46x - lattice T00 demonstrably UNDERDETERMINES
the response; (c) the CORRECT finite-box target (strip ->
circle doubling, BOTH Dirichlet walls) is ~1 (0.95-1.09), and
the lattice's own EXACT modular P-weight TRACKS it within a few
percent: THE BOX SATISFIES BW IN THE MODULAR CURRENCY - the
geometry component of the deficit EVAPORATES, and the measured
coherent-probe deficit is carried entirely by the amplitude
protocol and operator/sector mixing.  The scale flow at MATCHED
delta<K> is FLAT with shrinking drifts (+0.0035 -> +0.0010):
no drift toward BW, no artifact masquerading as one.  THE EP
KILL (K-W4) FIRED AT LATTICE-T00 SCOPE (2.12; amplitude-robust
to a/100 in review; equal-dE = equal boost charge across
species to 0.12%, so the kill is genuinely species-xi in that
currency) - but in the MODULAR currency the first law forces
ratio 1 at linear order, so K-W4 structurally cannot test
continuum EP there: THE CONTINUUM-EP QUESTION IS THE CURRENCY
QUESTION (the T00 -> K map), named as the successor campaign.
```

## 0. Design, trials, receipts

Receipts: `code/v6_p44_3plus1_planar_lift_campaign.py`, canonical
`/tmp/v6_p44_campaign.out`, bit-identical rerun verified, runs to
completion, and the kill-ledger lines are **generated from the
computed flags** (review hygiene: no hardcoded verdict can drift
from its receipt).  The design block carries the declared
protocols, kills, candidate list, and the trial traps:

- **t1/t6 (the channel traps):** single-bond probes and even
  smoothly-enveloped dipole *trains* are UV objects (weight ~0.06
  of boost); the IR channel requires *coherent rank-one* probes.
  Channel anatomy at matched depth and mass: coherent 0.310 /
  enveloped train 0.057 / single dipole 0.058 — review-verified
  spectrally (the coherent probe has 0% of its energy above
  $\omega = 1$; dipole objects ~99%).
- **t2:** the Williamson pairing bug (`[n:]` double-counts;
  fixed `[::2]`, receipted to $10^{-14}$).
- **t3:** ν's $k \to 0$ logarithmic tail demands the declared
  extrapolation — with the log coefficient *derived* (§1).
- **t4:** response sources must be smooth relative to lattice,
  stencil, and ξ.
- **t5 (the amplitude budget):** $\delta\langle K\rangle \sim
  2\pi d\,\delta E \ll 1$ is **necessary only** — see R-b.

## 0b. The correction record (hostile review, run to pass; all visible)

- **R-a (the broken canonical).** The first version's canonical
  receipt crashed at an undefined variable before Prologue B,
  W1–W4, and the kill ledger ever executed; the "bit-identical
  rerun" verified a deterministic traceback.  Fixed: the campaign
  runs end-to-end, the canonical is re-locked, and the ledger is
  now generated from computed flags so this failure class cannot
  recur silently.
- **R-b (no linear-response regime).** The amplitude budget (t5)
  passes by 100–3000× and yet the response coefficient drifts
  $+0.026$ per amplitude halving *without converging* in the
  receipted window ($a = 2\times10^{-3}$ to $2\times10^{-5}$).
  Cause, receipted: near-pure block modes make $S$ non-analytic
  ($-x\ln x$) — and the review sharpened this further: the
  pathology is **generic to lattice vacuum blocks**, not a
  near-critical feature (gapped $m = 0.4$ control: 106/108
  near-pure, drift $+0.012$/halving).  Consequence: $g$ is
  **protocol-defined**; all flow statements at matched
  $\delta\langle K\rangle$.  Zero-amplitude $g$: registered open.
- **R-c (state-independence was translation invariance).**  The
  original "1656× state-independence" compared the *same* probe
  translated.  Cross-class controls collapse to suppression 6–7×:
  kill **K-A′ FIRED**, the kernel is **class-resolved**, the old
  wording withdrawn.  The two-bump superposition receipt was then
  itself corrected: the tomography-calibrated version (1.0101)
  conflated a +2–3% amplitude artifact with the genuine cross
  term; the **self-amplitude-matched** receipt (joint vs directly
  measured singles) gives 0.986 — a real −1.4% cross-term, within
  the declared 5% gate.
- **R-d (the BW benchmark, corrected twice).**  Continuum $g
  \equiv 1$ was the wrong target for this geometry; the review's
  own first correction ($g_{\rm box} = 1 - d/2R$, single-image)
  was *also* wrong — it ignored the second Dirichlet wall.  The
  correct strip→circle doubling gives $g_{\rm box} \approx 1$
  (0.95–1.09 over the measured window), and the decisive
  adjudicator is the lattice itself: the **exact modular
  P-sector row-sum weight** (the P41 instrument) tracks the
  two-wall curve within a few percent.  So the *box satisfies BW
  in the modular currency*; the geometry component of the
  deficit **evaporates** (the box-size control independently
  shows this: measured $g$ is essentially $R$-independent), and
  the deficit is carried entirely by R-b plus operator mixing.
  Section 4 carries the receipts, including the review-supplied
  **matched-T00 two-state receipt** (4.46×).
- Also corrected, smaller: ν's error bar is a stated
  *conservative floor* ($3\times10^{-6}$), with window spread
  $1.6\times10^{-7}$ and variant-form spread $2.1\times10^{-7}$
  receipted under it; the zero mode is $(1/6)\ln N$-divergent
  (per-doubling diffs $0.1142/0.1149/0.1152$ vs $0.1155$) and
  measure-zero in the BZ; lattice finiteness credited to
  BKLS/Srednicki; the W4 overlay-vs-response gap (1.90 vs 2.10)
  explained as the width-class systematic (class-matched probes:
  1.898 vs 1.90 — they coincide); the declared kill set
  re-registered with the executed code.

## 1. ν — the area density of record capacity

$\nu(L_\perp) = \sum_{k_\perp \neq 0} S_{\rm bulk}(m_{\rm eff})
/ L_\perp^2$ over the exact transverse decomposition: table over
$L_\perp \in \{8, 12, 16, 24, 32, 48, 64\}$; plateau
$2\times10^{-11}$; $N$-independence $1.1\times10^{-11}$.  The
extrapolation $\nu(L) = \nu_\infty - (\alpha + \beta\ln L)/L^2$
has $\beta = 1/6$ **derived**: $S(m) = -\tfrac16\ln m + c$ as
$m \to 0$ and $m_{\rm eff} \approx |k_\perp|$ near the BZ zero,
so the missing zero cell contributes $(\tfrac16\ln L +
{\rm const})/L^2$.  Free-$\beta$ cross-check: $0.1662$.  Fit
windows $L \ge 16/24/32$ agree to $1.6\times10^{-7}$; variant
forms (free-$\beta$, added $1/L^3$, added $(\ln L)^2/L^2$) agree
to $2.1\times10^{-7}$:

$$\nu_\infty = 0.0242620 \pm 3\times10^{-6}\ \text{(conservative
floor)}, \qquad G = \tfrac{1}{4\nu_\infty} = 10.304
\;\text{(record units, planar scope)}.$$

The zero mode is $(1/6)\ln N$-divergent but measure-zero in the
BZ (excluded legitimately; would contribute 5.9% at $L = 24$).
The pre-declared nine-candidate list produced no match (nearest:
$\varepsilon_{\rm eff}$ at 27%) — as expected; the ten-digit rule
is **not in play** at this precision.  Finiteness itself is what
any lattice cutoff gives (BKLS; Srednicki); the SHARD content is
the ontological reading — the lattice is ledger, not regulator —
and ν as the two-route calibration target.

## 2. The instrument and the amplitude protocol

The time-extended Williamson machinery (GXP ≠ 0) is validated at
$1.2\times10^{-14}$ against the static route and passes a
**sanity-grade** lightcone receipt (declared as such: one
separation, ~$10^2\times$ pre/post contrast, the ramp between is
tails + lattice dispersion).

The R-b receipt is the lift's instrument discovery: **entropy
probes have no linear-response limit on lattice vacuum blocks —
generically.**  The $m = 0$ census finds 104/108 symplectic
eigenvalues within $10^{-6}$ of purity; $g(a)$ runs $0.451 \to
0.611$ from $a = 2\times10^{-3}$ to $2\times10^{-5}$ at
$+0.026$–$+0.024$/halving, not converging within the window.
The gapped control ($m = 0.4$): census 106/108, drift
$+0.012$/halving — the pathology is generic, not near-critical.
Declared consequence (the protocol): $g$ is defined at reference
$\delta\langle K\rangle$; matched-$\delta\langle K\rangle$ is the
primary protocol for every cross-scale statement; fixed-$a$ and
matched-$\delta E$ are printed as controls.

## 3. The kernel, class-resolved

Within a probe class, the measured kernel passes all three
consistency receipts: **translation** (probe moved 30 sites,
ratio 1.0000 — scoped: covariance, not state-independence);
**self-amplitude-matched two-bump superposition** (width-16
bumps at different positions with amplitudes $a$ and $a/2$,
joint $\delta S$ vs the sum of directly measured singles at
their own amplitudes: ratio 0.986 — a genuine −1.4% cross-term;
the tomography-calibrated variant 1.0101 is printed beside it
and conflates the R-b drift); **restoration** (suppression 1656×
at $\epsilon^* = 0.00$ on a 0.01 grid; width-6 class:
$5\times10^5$).  Across classes it fails exactly as the form
factor demands: cross-class restoration collapses to 6–7×
(kill **K-A′ FIRED**), and the cross-class point test through
the collapse lands at 0.893 — the collapse's own systematic.
The form-factor collapse $g(\ell_{\rm eff}/d)$ is
**approximate**: one-signed $+13.7\%$ mean deviation (max
$+14.4\%$), measured and quoted wherever it is used.

The surviving response-law statement: $\theta'(j) =
-(2\pi/\nu)\,g\,\delta T_{00}$ at measured-weight level **within
the probe class**; the pure-boost coefficient is not licensed at
this scope.

## 4. The BW deficit, resolved as currency — and the flat flow

The original registration was "$g$ vs continuum BW ($g \equiv
1$): undecided tension."  The resolution receipts, now canonical:

- **(a) The deficit is in the operator, not the law.**  At one
  config ($w16$, $m = 0$, $d = 42$): $\delta S / \sum W_{\rm
  meas}\,\delta T_{00} = 0.93$ (the measured-weight response law
  holds; the 7% is weight extrapolation below its window), while
  $\delta S / \delta\langle K_{\rm boost}\rangle = 0.61$: the
  lattice entanglement Hamiltonian is *not*
  $2\pi\sum(x{-}j{+}\tfrac12)T_{00}^{\rm latt}$ (Eisler–Peschel).
- **(b) Lattice $T_{00}$ cannot parameterize perturbations —
  structurally and directly.**  Structurally: the
  $T_{00}$-carrying band of the probe (100% of the lattice
  energy) is **alone not a physical perturbation** —
  purity-violation census 26 modes at $-6.6\times10^{-5}$, ten
  orders above the roundoff floor ($-5\times10^{-15}$, printed),
  while the full probe has zero violations.  Directly (the
  **matched-T00 two-state receipt**, review-supplied): a
  deterministic NNLS tiling of width-2 coherent probes, matched
  to the rank-one probe's lattice-$T_{00}$ profile (shape
  residual 0.6%, energy ratio 0.9985, exactly PSD), differs in
  modular response by **4.46×**.  Two physical states, same
  lattice energy profile, factor-4 different ledger response:
  $T_{00}$ demonstrably underdetermines the modular response.
- **(c) The correct finite-box target is ≈ 1 — and the box
  meets it in the modular currency.**  The strip has Dirichlet
  walls at *both* ends; strip→circle doubling (circumference
  $2N$, interval $2R$) gives $g_{\rm box} = 0.95$–$1.09$ over
  the measured window (the earlier single-image $1 - d/2R$ is
  withdrawn — it ignored a wall).  Adjudicated by the lattice
  itself: the **exact modular P-sector row-sum weight** tracks
  the two-wall curve within a few percent ($0.953/0.968/0.950/
  0.953/1.002/1.098$ vs $0.954/0.951/0.961/0.986/1.026/1.087$).
  Regulator disclosure (review): the row-sum extraction is
  clip-sensitive on near-pure modes — an $O$(few-percent)
  systematic, receipted by a clip sweep ($0.953/0.975/0.958$ at
  $d = 22$ across clips $10^{-14}/10^{-12}/10^{-10}$); the
  ≈1-vs-measured (0.13–0.45) adjudication is **clip-robust**.
  **The box satisfies BW in the exact modular currency.**  The
  geometry component of the measured deficit evaporates.
- **(d) Box-size control:** fixed probe, $N = 256/512/1024$:
  $g = 0.4506/0.4589/0.4601$ — saturating, coherent with (c):
  geometry contributes essentially nothing to the deficit.

**The protocol-controlled scale flow (t8).**  Three $\ell/d$
classes, scales ×1/×2/×4 (×8 for the 0.27 class), geometry
receipted fixed ($x_0/N = 0.6641$ at every scale):

```text
              x1        x2        x4        x8     drifts
  fixed-a   0.4506 -> 0.4803 -> 0.5082 -> 0.5345  (+0.03/dbl: ARTIFACT)
  match-dE  0.4506 -> 0.4271 -> 0.4013            (reverses sign)
  MATCH-dK  0.4506 -> 0.4540 -> 0.4559 -> 0.4569  (+0.0035,+0.0019,+0.0010)
  (l/d ~ 0.18 and 0.13 classes: match-dK drifts +0.0016,+0.0009
   and +0.0008,+0.0005 - same pattern, shrinking)
```

Protocol-uniqueness caveat (review): in the family $a_s \propto
s^{-p}$ the protocols differ by the R-b log slope, so "flat" is
specific to matched-$\delta\langle K\rangle$ ($p = 1$) — the
principled member (it fixes the first-law charge $2\pi d\,\delta
E$; matching the *box* charge gives identical numbers since
$d/R$ is scale-fixed) — and the **shrinking** drifts are a
convergence signature a constant-log artifact cannot mimic.

Verdict: the benchmark was wrong twice; corrected, the box obeys
BW in the modular currency, and the measured coherent-probe
deficit is carried entirely by two receipted non-gravitational
mechanisms — the amplitude protocol and operator/sector mixing.
**No residual record-law anomaly is demonstrated**; zero-
amplitude X-sector BW is *not* demonstrated either — re-
registered open with the Eisler–Peschel exact-kernel route named
(**the currency campaign**).

## 5. The equivalence principle at lattice-T00 scope

Equal-lattice-energy sources on species $\xi = 5$ vs $\xi = 2.5$
produce geometry responses in ratio $2.12$–$2.08$ across screens,
amplitude-robust ($2.085$ at $a/10$; ~$2.0$ at $a/100$ in
review): kill **K-W4 FIRED** at lattice-$T_{00}$ scope.  The
review's confound checks sharpen it: $\delta\langle K_{\rm
boost}\rangle$ per unit $\delta E$ is equal across species to
$0.12\%$ — equal-$\delta E$ *is* equal boost charge, so the kill
is genuinely species-ξ in that currency, not vacuum
normalization; and with class-matched ($w = 6$) probes the
response ratio is $1.898$ vs the $w6$ tomography overlay $1.90$
— overlay and response coincide; the earlier 1.90-vs-2.10 gap
was the width-class systematic.  The per-species receipts
($\delta S/\delta\langle K_{\rm boost}\rangle = 0.257$ vs
$0.122$; band census 27/27) show the comparison currency is not
the modular charge — and in the **modular** currency the first
law forces ratio 1 at linear order ($\delta S = \delta\langle
K_{\rm exact}\rangle$ for any perturbation), so K-W4
*structurally cannot* test continuum EP there.  **The
continuum-EP question is the currency question** — the
$T_{00} \to K$ map — scoped by §4 and named as the successor
campaign.

## 6. Kill ledger

```text
  K-A  within-class translation (0.00%)      -> did not fire
  K-A' cross-class universality              -> FIRED (kernel is
       CLASS-RESOLVED; 'state-independent' withdrawn, R-c)
  K-B  lightcone/causality (sanity-grade)    -> did not fire
  K-W1 nu fit-window stability (1.6e-7)      -> did not fire
       (beta = 1/6 derived, free fit 0.1662; variant spread
       2.1e-7)
  K-W3 within-class restoration + pinning    -> did not fire
       (1656x, eps* = 0.00 on a 0.01 grid)
  K-W4 EP at lattice-T00 scope               -> FIRED (direction
       amplitude-robust; equal-dE = equal boost charge to
       0.12%); in the modular currency the first law forces
       ratio 1 at linear order - continuum EP = the currency
       question
  candidates                                 -> no match (expected)
  t7: RESOLVED-AS-SCOPED: corrected box target ~1; exact modular
      P-weight tracks it (lattice BW in the modular currency);
      coherent-probe deficit = amplitude protocol + operator/
      sector mixing (matched-T00 underdetermination 4.5x); no
      residual anomaly demonstrated; X-sector zero-amplitude BW
      not demonstrated; Eisler-Peschel route re-registered
  t8: flat at matched delta<K> (drifts +0.0035 -> +0.0010,
      shrinking); fixed-a drift withdrawn as amplitude artifact;
      'flat' is protocol-specific to the declared primary
  t1-t6 documented; zero-amplitude g = open instrument item
  (ledger lines generated from computed flags in the canonical)
```

## 7. Verdict

What the lift delivers, after its own traps and a hostile review
run until it passed — twice correcting even its own corrections:
**ν as a measured number with a derived extrapolation** and a
floor-honest error; **the amplitude protocol** — a real
instrument discovery: entropy probes on lattice vacuum blocks
generically have no linear-response limit, so modular-response
quantities are protocol-defined; **a class-resolved kernel**
with translation, self-matched superposition, and restoration
receipts inside the class and a fired kill outside it; and **the
BW deficit resolved as currency**: the correct finite-box target
is ≈ 1, the lattice's own exact modular weight meets it within a
few percent — the box obeys BW in the modular currency — and the
measured deficit is carried entirely by the amplitude protocol
and operator/sector mixing, with lattice $T_{00}$ directly shown
to underdetermine the modular response by 4.46× at matched
profile.  No residual record-law anomaly demonstrated; no
recovery claimed beyond its receipts; the EP kill standing at
exactly the scope its currency supports, with continuum EP
identified as the currency question itself.  The program's
gravitational ledger after P41–44: matter side receipted (P42),
2d response law with curvature term receipted (P43), 3+1 planar
response at measured-weight level receipted within probe class,
ν and G as numbers, lattice BW receipted in the modular currency
— and the named successor: **the currency campaign** (the exact
$T_{00} \to K$ map), with zero-amplitude $g$ and ν's closed form
as the open instrument and calibration items.

## Receipts

```text
code/v6_p44_3plus1_planar_lift_campaign.py    the campaign
/tmp/v6_p44_campaign.out             canonical (BIT-IDENTICAL,
                                     runs to completion, ledger
                                     generated from flags)
nu table L=8..64 + beta=1/6 fit (window spread 1.6e-7; variant
spread 2.1e-7); nu_inf = 0.0242620 +- 3e-6 (floor); candidates
(9, declared): no match; channel anatomy 0.310/0.057/0.058;
near-purity census 104/108 (m=0), 106/108 (m=0.4 control);
g(a) 0.451->0.611 (+0.026..+0.024/halving); gapped drift
+0.012/halving; form-factor collapse deviation +13.7% mean,
one-signed; Williamson 1.2e-14; lightcone 5.1e-5/7.5e-3
(sanity-grade); T7: response 0.93 vs boost 0.61; purity census
0/0/26/49 (roundoff floor 5e-15); matched-T00 two-state
receipt: residual 0.006, dE 0.9985, ratio 4.46; corrected box
target (two-wall) 0.954..1.087 vs exact modular P-weight
0.953..1.098 vs measured 0.451..0.134 (clip-sweep regulator
disclosure: O(few %) systematic, adjudication clip-robust);
candidates ledger line generated (nearest 27%); box control
0.4506/0.4589/0.4601; t8 three protocols, matched-dK drifts
+0.0035/+0.0019/+0.0010; W2: translation 1.0000, two-bump
self-matched 0.9860 (tomography-calibrated 1.0101 conflates
drift), cross-class 0.893; W3: within 1656.5 (w6: 5e5), cross
6.2/7.2 -> K-A' FIRED; W4: 2.124..2.079, a/10: 2.085,
boost-charge equality 1.0012, class-matched overlay 1.898 vs
1.90; per-species dS/dK_boost 0.257/0.122.
Literature: Bisognano-Wichmann; Eisler-Peschel; Casini-Huerta;
Cardy-Tonni (BCFT modular weight); Bombelli-Koul-Lee-Sorkin;
Srednicki; Callan-Wilczek; Jacobson (1995, 2015); Faulkner et
al.; Wall; Bousso et al.; Eotvos/MICROSCOPE; Peschel
(correlation-matrix method); Williamson;
Audenaert-Eisert-Plenio-Werner (harmonic chains).
```
