# Paper 36 (v6) - SHARD: The Bridge Campaign - Seven Doors to the Per-Rung Factor, and the One Left Standing

Preprint, not peer reviewed, version 2026-06-11.

Author: Felix Robles Elvira

Subtitle:

```text
The full assault on O35.1: derive the relation-to-rung bridge -
the per-rung dressing factor (1-eps) - from the corpus' own
binding theory, attacking from every standpoint we could name
(principle-first, mechanism-first, information-first, algebra-
first, RG-first, action-first, structure-first), under criteria
PRE-REGISTERED before any route was computed.  The campaign did
NOT derive the bridge.  What it produced instead: (1) a
comprehensive, receipted NO-GO MAP - every mechanical route is
excluded with exact numbers (naive one-relation identifications:
0.48-1.18 vs the needed ~0.968; frustrated-triangle action:
0.817; RG eigenvalue: 0.617; action-per-rung: sign-flips at exact
level; refinement towers: the geometry family BRACKETS the target
- single-share chains 0.987, double-share 0.921, needed 0.968 -
and no member hits it); (2) two genuine discoveries: the
CROSS-IDENTITY that P8's oriented frustrated triangle
(+0.201674235292) is exactly the lam = -1 point of the unoriented
scalar equation (match 1.8e-14) - frustration is amplitude
reversal - and the PER-LINK CHAIN LIMIT D_inf = 0.0132725, a new
exactly-computable corpus constant, obtained with new general
machinery (an exact multi-mode defect solver for arbitrary
relation codes, validated against both of P8's printed
multi-relation values); (3) the SOLE SURVIVOR, sharpened to its
final form: the coherence identification - mass as the squared
L-R seam coherence of a weight-eps recorded binary distinction,
|coherence|^2 = eps(1-eps) at purity, exact at half-rungs via the
per-half-step amplitude sqrt(eps(1-eps)) - which produces the
factor BY CONSTRUCTION and is therefore an identification, not a
derivation, carrying one precisely named tension: sealed records
are definite, while coherence lives on the unsealed side; the
bridge must make the rung PHASE silent while its MODULUS is
physical.  That tension is now the entire content of O35.1.  One
of our own blunders is kept on record as a warning: a
second-order estimate of the lam = -1 defect suggested ~eps; the
exact value is 0.2017 - the expansion has no business being
evaluated there.
```

## 0. Pre-registration (written before any route was computed)

Because this campaign hunts a known target ($g = \ln(1-
\varepsilon)$, pinned by Paper 35), it is the program's highest
numerology risk, and the criteria were fixed first — they are
printed verbatim at the top of the canonical output, before any
result.  SUCCESS requires the conjunction: a per-unit-rung
multiplicative factor in the surviving cluster, *derived not
chosen*; exactness at half-rungs; no sign flip at all-orders
level; a stated charged/neutrino story.  FAILURE rules: a route
producing an out-of-cluster factor counts *against* the dressed
base; exhausting the route list means publishing the no-go map —
which is what happened, and this paper is that publication.  The
route list (fixed in advance, with the standpoint each embodies):

```text
  R-A  product-of-poles forks       (Einstein: principle first)
  R-B  signed/frustrated relations  (Feynman: mechanism, round trips)
  R-C  variance/Fisher/coherence    (Jaynes/Shannon: information)
  R-D  exact-algebra equality scan  (Dirac: algebraic necessity)
  R-E  refinement-map eigenvalue    ('t Hooft/Wilson: RG substrate)
  R-F  action-per-rung              (Fermi: estimate the action)
  R-G  refinement towers            (this corpus: build it and
                                     measure it, exactly)
  B6   half-rung consistency        (Born/Barandes: amplitudes)
```

Receipts: `code/v6_p36_bridge_campaign.py`, canonical
`/tmp/v6_p36_campaign.out`, bit-identical rerun verified; mpmath
40 dps throughout.

## 1. The Einstein door (R-A): principle first — and why it alone is not enough

The principle candidate: *a rung step is a recorded binary
distinction, and axiom S demands both poles be sealed; a sealed
fork weighs the product of its branches*, $\varepsilon(1-
\varepsilon)$.  Beautiful — but a principle must select its own
mathematical referent, and the binding theory offers four obvious
referents for "the weight a relation contributes at the
self-consistent commitment point."  All four are computed exactly
and all four fail:

```text
   codeword amplitude ratio t^3(h*)/theta^3   0.5986
   commitment ratio e^-h*/theta               1.1211
   evidence ratio D(h*)/D(eta)                1.1781
   per-mode amplitude t(h*)/theta             0.8428
   needed (cluster)                           0.9682 - 0.9692
```

The principle survives only in the form Section 7 gives it (the
coherence identification) — where it stops being a derivation.
This is the campaign's recurring lesson: the *story* is easy; the
*referent* is the problem.

## 2. The Feynman door (R-B): mass as a round trip — and a discovery that is not the one we wanted

Mechanism reading: a Dirac mass is a left-right round trip;
if the forward hop is the committed pole and the return the
declined pole, the round-trip weight is $\varepsilon(1-
\varepsilon)$.  The corpus object that implements "the reversed
hop" is the sign-reversed relation: the scalar fixed-point
equation at $\lambda = -1$.  Computing it exactly:

```text
   defect(w = 3, lam = -1) = 0.2016742352919823
   P8's oriented FRUSTRATED triangle (chirality campaign,
   printed): +0.201674235292      match: 1.8e-14
```

**Cross-identity (new receipt for the corpus).**  The oriented
frustrated triangle of P8's chirality campaign *is* the
$\lambda = -1$ point of the unoriented scalar theory: frustration
is exactly amplitude reversal.  P8's "frustrated triangles bind
$24\times$ harder" becomes a one-line statement about the scalar
equation.  This connects the chirality campaign to the
single-relation theorem with no new machinery — found because the
Feynman door demanded the object be computed.

As a *dressing* candidate it is excluded: $e^{-0.2017} = 0.817$,
far outside the cluster.  **A trap, kept on record**: our own
second-order estimate ($d_1\lambda + d_2\lambda^2$ at $\lambda =
-1$) gave $\approx 0.0317 \approx \varepsilon$ — tantalizing and
*wrong by a factor of six*; the perturbation series (built at
$\lambda = 0$ with the P35 toolkit) has no business being
evaluated at $\lambda = -1$.  Had we trusted the estimate, this
paper would contain a fake derivation of the target.  The exact
computation is what killed it; this is why the campaign computes
everything exactly.

## 3. The Jaynes door (R-C): information — the factor for free, which is exactly the problem

$\varepsilon(1-\varepsilon)$ is the Bernoulli variance — the
discriminating power a weight-$\varepsilon$ binary record
carries; its inverse is the Fisher information.  "Each rung costs
one bit of generation-distinction, weighted by the evidence the
record carries" produces the factor *exactly, by construction* —
and that is its weakness: it is an identification wearing a
derivation's clothes.  It earns one real credit (Section 7's
half-rung exactness) and one real debt: it must say why the
*binding marginality* $\varepsilon$ — a fixed-point quantity, not
a probability — is the Bernoulli parameter of anything.  Graded:
identification, the only survivor, final form in Section 7.

## 4. The Dirac door (R-D): is the factor already hiding in the exact algebra?

Equality scan of every exact binding quantity the campaign
touched (frustrated defects at $w = 3..6$, the exact triangle
defect, the anti-binding sum $\sum_{w\ge4}$, tower increments,
the map eigenvalue) against the targets $\{\varepsilon,
\varepsilon(1-\varepsilon), -\ln(1-\varepsilon)\}$ at 40 digits:
**no nontrivial identity**.  The only match is the defining one
($-d_1(3)/\theta^3 = \varepsilon$, exact, as it must be).  The
factor is not hiding in plain sight; cheap numerological
"derivations" from the binding constants are closed off in
advance, by receipt.

## 5. The 't Hooft door (R-E) and the Fermi door (R-F): the substrate and the action say no

The commitment law rewrites as the one-step map $x \mapsto
1/(1+x+x^2)$ with the corpus cubic as fixed point (a rewriting,
not asserted to be P7's dynamical refinement map); its eigenvalue
is exactly $\theta^2(1+2\theta) = 2-2\theta-\theta^2 =
0.617024\ldots$ — excluded as a dressing, recorded as a corpus
constant (curiously near, but provably not equal to, $\eta$;
difference $7.6\times 10^{-3}$).  The action-per-rung reading was
already killed at exact level by Paper 35 (the marginality is a
first-order object; the exact $w = 3$ defect flips sign), and its
scale is wrong besides.

## 6. The structural door (R-G): build the towers and measure them — new machinery, a new constant, and a bracketing no-go

The corpus picture of a generation step is a refinement: a mode
of a triangle re-expressed through a further triangle.  Chains
$T_k$ of $k$ single-share triangles are exactly computable with
this campaign's new tool — a general multi-mode defect solver for
*arbitrary* relation codes (fixed point $\langle s_a\rangle =
e^{-h_a}$ for every mode; defect $= \ln W_K - \sum_a [D(h_a) -
D(\eta)]$), validated against both multi-relation values P8 ever
printed ($T_2 = +0.020844970391$: match; disjoint additivity:
match).  It also caught and corrected a hand-assembly error in
our own first $T_3$ — machine-generated codes only, from here on.

```text
   per-link increments:  D2 = 0.0124069   D5 = 0.0132686
                         D3 = 0.0131168   D6 = 0.0132725
                         D4 = 0.0132459
   PER-LINK LIMIT  D_inf = 0.0132725 (converged to 4e-6 by k = 6)
   needed g = 0.0322842;  single-share delivers 0.41 x g
   star (common mode):       0.0125 per triangle
   double-share pair:        0.0819 per link  (2.5 x g)
```

The tower-geometry family **brackets the target and no member
hits it**.  The pre-registration forbids the obvious next move —
hunting intermediate geometries until one fits — so R-G is
excluded at the named family, and $D_\infty = 0.0132725$ enters
the corpus as a new exactly-computable constant (the asymptotic
defect cost of one refinement link).

## 7. The Born door (B6) and the survivor, in final form

Half-integer rungs are the quiet discriminator: a dressing law
must be exact at $x = \tfrac12$.  Only the multiplicative class
survives, and it does so naturally in amplitude language: *the
rung index counts amplitude powers*, with per-half-step amplitude
$\sqrt{\varepsilon(1-\varepsilon)}$ — which is precisely the
maximal off-diagonal coherence of a two-outcome record of weight
$\varepsilon$.  Assembling the survivor:

> **The coherence identification (sole survivor, stated fully).**
> A mass term is a left-right transition: its rung weight is the
> squared coherence of the L-R seam record.  If the seam is a
> recorded binary distinction of weight $\varepsilon$ and the
> seam state is pure, $|\text{coherence}|^2 = \varepsilon(1-
> \varepsilon)$ exactly — the dressed base — and the half-rung
> structure is automatic (amplitudes, not weights, count rungs).
> Charged seams pass through EWSB and need not be pure; the
> seesaw seal is pre-EWSB.

What it is *not*: a derivation.  It produces the factor by
construction, and it carries one precisely named tension, which
is the campaign's distilled output: **sealed records are
definite — decohered — while coherence lives on the unsealed side
of a distinction.  The bridge must make the rung phase *silent*
(axiom-S gauge) while keeping its modulus *physical*.**  Whether
the record calculus permits an object that is sealed in modulus
and silent in phase is a well-posed question about the corpus'
own axioms — and it is now the entire remaining content of
O35.1.  (The corpus is not without precedent here: superselection
sectors in Part II are exactly moduli-without-relative-phase
structures; whether the rung ladder is such a sector is the
sharpest form of the question.)

## 8. Verdict, and the honest scoreboard

```text
   route                       factor       status
   R-A naive identifications   0.48-1.18    EXCLUDED (exact)
   R-B frustrated triangle     0.817        EXCLUDED (+ the
                                            cross-identity found)
   R-C coherence/variance      0.9682 exact IDENTIFICATION - the
                                            sole survivor
   R-E map eigenvalue          0.617        EXCLUDED (exact)
   R-F action-per-rung         sign flips   EXCLUDED (P35)
   R-G refinement towers       0.987/0.921  EXCLUDED (brackets,
                                            misses; D_inf new)
```

The campaign did not derive the bridge.  It closed every
mechanical door at the named families with exact receipts, found
two structural results worth keeping regardless (the
frustration-as-amplitude-reversal identity; the multi-mode solver
and $D_\infty$), preserved one of its own blunders as a warning
about perturbative wishful thinking, and reduced O35.1 from "find
a derivation" to one sharp question: **can a record be sealed in
modulus and silent in phase?**  If yes, the dressed base has its
derivation and the registered prediction's expected failure
becomes the program's confirmation.  If no — if axiom S forbids
exactly this — then the dressed base is dead *by the program's
own axioms*, which would be the strongest possible form of the
withdrawal O35.1 pre-commits to.  Either resolution is now a
single, well-posed theory question rather than an open hunt.
*[Resolved by Paper 37: the object exists constructively, and the
forcing is STATIONARITY (Lemma B: a misaligned sealed seam cannot
host a stationary state).  O35.1 splits: O35.1a (the per-seam
factor) = THEOREM, given the named premises; O35.1b (rung = seam
count) remains open.  The mechanism's untuned consequence set is
registered there, including one claim currently 3.1 sigma against
us.]*

## Receipts

```text
code/v6_p36_bridge_campaign.py   the whole campaign
/tmp/v6_p36_campaign.out         canonical (BIT-IDENTICAL rerun)
Pre-registration printed before all results; B1 exclusions (4
referents, exact); B2 frustrated cross-identity (1.8e-14) +
exclusion + the recorded trap; B3 towers (solver validated on
both P8 multi-relation values; chains k = 1..6; D_inf converged
4e-6; star; double-share); B4 eigenvalue exclusion; B5 equality
scan (no nontrivial identity at 40 digits); B6 half-rung
consistency; B7 verdict.
```
