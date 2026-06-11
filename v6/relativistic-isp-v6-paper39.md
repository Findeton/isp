# Paper 39 (v6) - SHARD: The Gauge Tower - Lattice Yang-Mills as a Record Tower, Axiom C on Refinement, and the Self-Consistency Defect at the Wall

Preprint, not peer reviewed, version 2026-06-11.

Author: Felix Robles Elvira

Subtitle:

```text
The first campaign where the program's two lines physically join.
Lattice gauge theory at finite level ALREADY IS a record tower:
the plaquette chain has positive-definite letter kernels (character
coefficients >= 0, receipted for U(1) and SU(2)) and PSD transfer
spectra, with Osterwalder-Seiler reflection positivity as the d>2
import - the alphabet is a compact group, a continuous-alphabet
EXTENSION of the batch's tame class, flagged as such.  On this
tower, axiom C (couplings fixed by self-consistency under
refinement) becomes a functional equation on the plaquette action,
and in 2d it is EXACTLY SOLVABLE: refinement is plaquette
convolution, the heat-kernel family is closed (K_t -> K_4t,
receipt 4.7e-15 through the full pipeline), and the class of all
axiom-C towers is the Levy/Hunt class of convolution semigroups.
The honest sharpening the receipts forced: axiom C ALONE does not
select Yang-Mills - the Wilson action's downward roots stay
positive to probe depth 4, with minimum scaling exactly like
t = 4^-k: Wilson is (as far as probed) a perfectly good NON-LOCAL
axiom-C tower whose Levy JUMP density we measure (4^k min_w ->
0.0385 [U(1), converged], -> ~0.019 [SU(2), drifting 2%/depth]).
What selects Yang-Mills is axiom C + LOCALITY (continuous, no-jump
generator), uniquely, by Hunt's theorem - and then the 2d
continuum action is DERIVED (credit: Migdal 1975 for heat-kernel
self-reproduction; this paper adds the record-class framing, the
selection grading, and the jump-density receipt).  In d>2
(hierarchical/Migdal recursion, exact for that model) the local
family is NOT closed, and the self-consistency defect D1 becomes
the wall's shadow: it VANISHES AT BOTH FIXED ENDS (1.4e-5 weak,
5e-15 strong), PEAKS at intermediate coupling (0.0595 one-step at
t~1.0; 0.062 pooled along flows at u~1.5; d=3 peak 0.033 -
shallower wall; d=2 identically 0), and the pooled flow data from
twelve starting couplings COLLAPSE onto one curve in the flow
coordinate u = -log r_F - the wall sits at FIXED effective
coupling, exactly the v4 picture (the traversal window, papers
40-45), now in record coordinates.  Sharpest single statement:
d=4 is MARGINAL on the local family (one-step u: 0.0375 -> 0.0385
at weak coupling), so the flow through the window is DRIVEN by
the defect - corr(log du, log D1) = 0.65-0.79 along all probed
flows.  The asymptotic-freedom-side slowness and the wall are one
object: departure from refinement self-consistency.  Registered
open core, named and not claimed: the UNIFORM TOWER GAP, which is
simultaneously the tame-class axis-5 wall (SHARD side) and the
intermediate-window crossing (v4 side).  Not claimed: 4d
continuum existence, mass gap, confinement beyond the
hierarchical model (Ito 1985 calibrates there).
```

## 0. Pre-registration, receipts, and what this campaign is

The targets, admissible outcomes, declared metrics, and numerical
conventions were fixed before computation and are printed verbatim
at the top of the canonical output.  Receipts:
`code/v6_p39_ym_bridge_campaign.py`, canonical
`/tmp/v6_p39_campaign.out`, bit-identical rerun verified.

This campaign is the bridge between the SHARD record program and
the Yang-Mills line (v4 papers 40-45).  Its claims are
deliberately finite-level: the finite objects exist and are
rigorous already (Wilson lattice gauge theory); what is new is
*whose* objects they turn out to be, what axiom C says on them,
and where the wall appears in record coordinates.  Guardrails
honored throughout: the d>2 computations are the hierarchical
(Migdal) recursion, for which the recursion is *exact* - no
uniform-truncation claim is made for real 4d (v4 paper 44, Secs.
10-11, closed that route; the Tomboulis-decimation critiques,
arXiv:0711.4930 and 0803.3019, bind here).

## 1. The embedding: lattice gauge theory is a record tower

**Statement (finite level).**  The plaquette/holonomy chain of 2d
lattice gauge theory with Wilson action is a stationary record
process in the sense of the program's RP form: the transfer kernel
$w(h^{-1}h')$ is a positive-definite class function — its character
coefficients are the letter spectrum, and they are nonnegative:

- $U(1)$: $\lambda_n = I_n(\beta) > 0$ (receipted $n \le 30$,
  $\beta \in \{0.5, 2, 8, 32\}$);
- $SU(2)$: $\lambda_j = 2(2j{+}1) I_{2j+1}(\beta)/\beta > 0$
  (the closed form receipted against quadrature, worst relative
  deviation $4.6\times 10^{-7}$).

Link-reflection Gram receipt (U(1) chain, six random functions):
minimum eigenvalue $+7.2\times 10^{-4} \ge 0$; transfer spectrum
nonnegative at machine floor ($-1.7\times 10^{-17}$).  For $d > 2$
Wilson LGT, reflection positivity is an **import**
(Osterwalder–Seiler 1978), credited and not re-proved; the
structural mapping (letters = time-slice kernels on the
gauge-invariant Hilbert space) is the same.

**The tame-class flag.**  The alphabet is a compact group: this
embedding lands in a *continuous-alphabet extension* of the
publishable batch's tame class.  Nothing in this paper claims that
extension closed; the embedding is exactly the kind of concrete
target the extension program needs (axis 5 of the tame-frontier
analysis: the constructive-QFT direction).

## 2. Axiom C on the 2d gauge tower: solvable, and honestly selective

Refinement of a 2d gauge tower is plaquette composition =
**convolution** of the plaquette weight with itself (4 sub-plaquettes
per plaquette at scale 2): in character coefficients
$\lambda_j \mapsto \lambda_j^4/d_j^3$.  Axiom C — the tower exists
with the same form at every level — is then exactly analyzable:

**(a) The heat-kernel family is closed.**  $K_t * K_t * K_t * K_t =
K_{4t}$ (the convolution semigroup property); receipted through
the full numerical pipeline at max coefficient residual
$4.7\times 10^{-15}$.  Credit where it is due: this
self-reproduction is Migdal's (1975), and the heat-kernel action
is the known 2d Yang–Mills continuum action.

**(b) The Wilson action is off the family.**  Distance (declared
metric D1) $0.101 / 0.080 / 0.041$ at $\beta = 1/2/4$ — nonzero,
shrinking like $\sim 1/\beta$ toward the family at weak coupling.

**(c) The sharpening the receipts forced.**  Within the record
class the downward root at each level is *unique* (positive
coefficients forced), so a complete axiom-C tower through Wilson
is decided by pointwise positivity of iterated convolution roots.
Probed to depth 4 with converged cutoffs and printed tail bounds:
**the roots stay positive** — minima $1.05\times 10^{-2} \to
1.5\times 10^{-4}$ (U(1)), $6.9\times 10^{-3} \to 7.5\times
10^{-5}$ (SU(2)), all at $\theta = \pi$.  And the minima scale
*exactly* like $t = 4^{-k}$: the rescaled sequence $4^k\,
\mathrm{min}\,w$ converges to $0.0385$ (U(1); to three digits) and
drifts at $\sim 2\%$/depth toward $\approx 0.019$ (SU(2)).  Linear
scaling of the small-$t$ density is the signature of a **Lévy jump
component**: as far as probed, Wilson generates a perfectly good
*non-local* axiom-C tower, and the limit of $4^k \mathrm{min}\,w$
is a measurement of its jump density at the antipode.

**(d) Selection, graded.**  So axiom C alone does **not** select
Yang–Mills, even in 2d — the axiom-C class is the full Lévy/Hunt
class of convolution semigroups (import: Hunt 1956).  The named
premise that selects is **locality** — a continuous, no-jump
generator — under which Hunt's theorem forces the bi-invariant
diffusion, i.e. the Casimir heat kernel, uniquely up to scale.
Ledger form:

```text
  DERIVED    2d YM continuum action = the unique axiom-C tower
             with local generator        (Hunt import + receipts)
  MEASURED   Wilson's non-locality: jump density 0.0385 (U(1)),
             ~0.019 (SU(2)) at theta = pi
  NAMED      locality premise (no-jump generator)
  CREDIT     Migdal 1975 (self-reproduction); Hunt 1956
```

## 3. d > 2: the defect is the wall's shadow

In $d > 2$ the hierarchical (Migdal) step is convolution **plus
bond-moving** (pointwise power $2^{d-2}$), and the local family is
no longer closed.  Define the **self-consistency defect** D1 =
relative $L^2(G)$ distance to the heat-kernel family (declared
metric).  Findings, all receipted:

**(a) Both ends vanish; the middle peaks.**  One step from a
heat-kernel start: defect $1.4\times 10^{-5}$ at $t = 0.03$ (weak
end), $5\times 10^{-15}$ at $t = 8$ (strong end), peak $0.0595$ at
$t \approx 1.0$ for $d = 4$; $d = 3$ peaks at $0.0333$ (shallower
wall); $d = 2$ is $10^{-15}$ everywhere (control).  The wall is
*the transient departure from the refinement-consistent manifold*,
and it lives exactly where v4 located the traversal window —
neither expansion's territory.

**(b) Fixed placement (the collapse).**  Twelve flows from Wilson
$\beta_0 = 3$ to $40$, pooled in the flow coordinate $u = -\log
r_F$: mean defect rises $0.0015 \to 0.061$ across $u \in [0, 2)$,
peaks at $0.062$ near $u \approx 1.5$, falls to $0.001$ by $u \in
[6, 8)$, with per-bin spreads $0.003$–$0.025$ — one curve, all
starts.  The transient (a Wilson-shaped start relaxing onto the
flow) is visible and dies in $\sim 2$ steps (receipt (d)).  The
window does not move with the cutoff: *fixed effective coupling*,
the record-coordinate version of v4's uniform-placement question.

**(c) Marginality: the defect drives the traversal.**  In $d = 4$
the local family is nearly stationary at weak coupling (one-step
$u: 0.0375 \to 0.0385$) — the record-language face of asymptotic
freedom's marginality.  The flow therefore moves only as fast as
its non-locality: $\mathrm{corr}(\log du_k, \log \mathrm{D1}_k) =
0.65 / 0.75 / 0.79$ for $\beta_0 = 12/24/40$.  The
asymptotic-freedom slowness and the wall are one object measured
two ways.

**(d) Transient decay (matched starts).**  Wilson($\beta = 12$) vs
heat-kernel start at matched $u$: log-ratio shape distance
$0.042 \to 0.003 \to 0.0002$ in two steps, staying $\le 0.004$
through the window — the flow forgets its start (receipt only; no
uniqueness theorem claimed).

**(e) Instrument honesty.**  A scale-$\sqrt 2$ Kadanoff
interpolation (declared fine instrument) reproduces the same
window at $u \approx 1.9$ with per-step peak $0.043$: the defect
is a *per-step* quantity, so its magnitude is
instrument-dependent; the location and both-ends-vanishing are
not.  Two $\sqrt 2$-steps vs one $2$-step differ ($u$ $0.1355$ vs
$0.1413$): the interpolation is an instrument, exact only at
integer scale, and is used only for resolution.

**(f) Known-artifact flag.**  The Migdal recursion confines U(1)
in $d = 4$ too (no Coulomb phase) — a known artifact; SU(2) is the
headline and nothing here distinguishes U(1) phase structure.

## 4. The port, and the registered open core

The 2d area law is exact in characters ($W(A) = d_F r_F^A$;
$\sigma a^2 = 0.8367$ at $\beta = 2$; known — Migdal): with the
embedding of Section 1, the corpus P8 area/perimeter dichotomy
becomes a statement *about gauge towers*, landing area-side on
every 2d tower.

**Registered open core (named, not claimed).**

```text
  UNIFORM TOWER GAP: along any axiom-C-consistent gauge tower in
  d > 2, the normalized transfer gap admits a positive uniform
  lower bound in physical units.
```

This single statement is (i) the tame-class axis-5 wall on the
SHARD side (uniform control of the infinite-refinement limit) and
(ii) the v4 traversal window on the Yang–Mills side (the certified
crossing's missing uniformity).  Both lines now pay into one
account; neither this paper nor any companion claims it.

## 5. Numerical traps, documented

Two first-run artifacts were caught and fixed in review of the
receipts, and are recorded because each could have flipped a
conclusion: (1) a truncated root probe produced a *spurious
negative* minimum (Gibbs oscillation from cutting coefficients of
size $\sim 0.05$) — a first run wrongly suggested the Wilson tower
terminates at depth 3; the converged-cutoff rerun with printed
tail bounds shows positivity and the $4^{-k}$ jump scaling
instead.  (2) A bare golden-section fit of the heat-kernel
distance silently converged to the search boundary whenever the
objective's large-$t$ plateau produced float ties (defect
misreported as $1.0$); fixed by a 161-point log-grid pre-scan.
Both traps are exactly the class the corpus discipline
(converged cutoffs, printed tails, control rows) exists to catch.

## 6. What would kill what (pre-committed)

```text
  K1  a Wilson root found negative at any depth (robust above
      tail bound)           -> the non-locality reading dies; the
                               termination branch replaces it
  K2  defect peak moves with beta0 (no collapse)   -> fixed-window
                               claim dies
  K3  defect fails to vanish at either fixed end   -> "wall =
                               departure from self-consistency"
                               dies
  K4  corr(du, D1) ~ 0 at d=4                      -> defect-driven
                               traversal dies
  K5  a local (no-jump) non-heat-kernel axiom-C tower in 2d
                            -> the Hunt selection grading dies
```

None fired at probed scope.

## 7. Verdict

The two program lines meet on one object.  Lattice Yang–Mills is a
record tower (finite level, receipted; OS import above 2d); axiom
C on that tower is exactly solvable in 2d and *honestly
non-selective* — the receipts forced the sharpening that locality,
not self-consistency alone, is what singles out Yang–Mills, and
they measured the excluded alternative's jump density.  Above 2d
the wall appears in record coordinates as the self-consistency
defect: zero at both fixed ends, peaked at fixed effective
coupling, driving the traversal it obstructs.  The campaign
changes where the program stands relative to the Clay-problem
wall — both faces now share one observable and one registered open
core — while claiming nothing across it.

## Receipts

```text
code/v6_p39_ym_bridge_campaign.py   the whole campaign
/tmp/v6_p39_campaign.out            canonical (BIT-IDENTICAL rerun)
A  letter positivity U(1)/SU(2); analytic-coefficient identity
   4.6e-7; RP Gram min eig +7.2e-4; OS import stated
B  heat-kernel closure 4.7e-15; Wilson D1 0.101/0.080/0.041 at
   beta 1/2/4; root minima positive to depth 4, 4^k min_w ->
   0.0385 (U(1)) / ~0.019 (SU(2), drifting, reported as such)
C  one-step defect: d=4 peak 0.0595 at t~1.0, ends 1.4e-5/5e-15;
   d=3 peak 0.0333; d=2 ~1e-15 control; pooled flows (12 starts)
   peak 0.062 at u~1.5, bin spreads 0.003-0.025; marginality
   0.0375->0.0385; corr(log du, log D1) 0.65/0.75/0.79;
   transient decay 0.042->0.0002 in two steps; sqrt(2)-instrument
   window at u~1.9
D  2d area law sigma a^2 = 0.8367 (beta=2); uniform-tower-gap
   registration printed
```
