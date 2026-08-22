# Paper 23c review — Seat Q (quantum/emergence)

Date: 2026-08-22

Disposition: **ACCEPT-WITH-FIXES** (one MAJOR, one MODERATE, one MINOR)

Blind delta review of the #325/#326 construction
(`7e90aba64c4abf5585d409f8d9696c76e0308007da3f81607e8e187cf709f126`,
235 LF) against frozen pin `d50dc41c…`, 13D `3b91766f…`. Seat lens:
emergence-gate discipline — what the result licenses downstream,
import hygiene, scope walls.

## Findings

**F-Q1 (MAJOR). Proposition F's admissibility claim is too strong and
undermines the uniqueness framing.** "Every function from history cells
to order-pairs is admissible" is false in general: 13D §9.2 requires
readers to be *equivariant families* with a defined output set $O_{gR}$
transported by the action; on a trivial-stabilizer experiment the law
is vacuous only for that experiment's self-transports, but the family
must still be declared coherently across the presentation orbit — and
arbitrary functions generally do not extend equivariantly to
$g\widehat e$ unless $O_R$ is transported along. The conclusion of Prop
F survives (with trivial stabilizer any *equivariantly extendible*
assignment is admissible; there are at least two incompatible such
extensions, e.g. an assignment and its rank swap), so the no-go stands.
*Required repair:* replace "every function … is admissible" by "every
assignment extendible to an equivariant family on the presentation
orbit is admissible; both an assignment and its $L_1\leftrightarrow
L_2$ swap qualify", and adjust the proof's first sentence accordingly.

**F-Q2 (MODERATE). §1's "settles that gate" overstates the unit's
reach.** The construction settles the gate **for the accepted present
law $\Gamma_D$**. Paper 15's dichotomy ("a future accepted law" or
unlabeled-law rigidity) remains open for future laws; §4.2/§4.3's
fixture-scoping discipline from Paper 23a v2 (#322/#323) should be
mirrored here. One sentence of scope engraving in §6 (or the primary
outcome line) is required:
`P23C-ORIENTED-PAIR-NOT-DERIVABLE` holds for terminal-$\Gamma_D$
certified fixtures and does not preclude derivation from any future
enlarged law.

**F-Q3 (MINOR). §5's second bullet imports the name "Paper 15's
$\pi_n$" without defining it in-place.** The coherence claim (exchange-
quotient match) should say "Paper 15's exchangeability quotient
(simultaneous transport and rank swap)" or cite its definition section;
as written it leans on reader memory of a contract-only document.

## What survived

The emergence reading is exactly right and well-walled: what Γ_D lacks
is not order structure but *oriented* order supply; the undirected bond
residual matches Paper 14/15's dependency-without-direction diagnosis
independently derived here. The dimension firewall is respected — no
cardinality-volume statement anywhere; the ensemble gate untouched;
Paper 15 rigidity correctly left CONDITIONAL with the bridge now proved
absent rather than unbuilt. No smoothness, aesthetic, metric, or
chronology object appears; #237 is cited where load-bearing and
respected everywhere. Import hygiene: only Def 2.4's target contract is
consumed from Paper 15 (F-Q3 cosmetic). Control rows 1–10 PASS.
Outcome `P23C-ORIENTED-PAIR-NOT-DERIVABLE` earned modulo F-Q1/F-Q2/
F-Q3; none structural.
