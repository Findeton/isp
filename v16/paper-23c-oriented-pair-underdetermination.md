# Paper 23c — the oriented null-realizer pair is not derivable from Γ_D

## Unit C side-gate result (mathematics only; constructed under frozen pin #324)

Date: 2026-08-22

Construction-stage status: built solely from terminal Paper 13D bytes
(`3b91766f…`) plus the target contract of Paper 15 §4.8. No code; no new
physical postulate; exact rational arithmetic throughout. Primary
disposition earned below: **`P23C-ORIENTED-PAIR-NOT-DERIVABLE`**.

## 1. Referent and question

Paper 15's conditional full-pattern rigidity theorem consumes an
*exchangeable oriented null-realizer pair*: an ordered pair $(L_1,L_2)$
of total orders on a finite carrier whose intersection realizes the
dependency relation, taken up to simultaneous presentation transport and
$L_1\leftrightarrow L_2$. Its own closing remark names the missing
bridge: either derive a covariant realizer pair from a future accepted
law, or prove the unlabeled law insufficient (#239's exact open
emergence gate). This unit settles that gate for the accepted law
$\Gamma_D$: **the pair is provably not derivable.** Three independent
obstructions are proved (§3); a potential loophole (symmetry-breaking
landmarks) is closed in §4; the positive residual — exactly how much
order content $\Gamma_D$ does derive — is recorded in §5.

Everything below is at certified-fixture scope of terminal Paper 13D.
Scope walls per pin §7: no channel odds, opportunity/activity/root,
$\Pi_{\rm phys}$, chronology, operational influence, dimension,
signature, metric, curvature, gravity, continuum, or QFT. Paper 14's
poset is a structural referent only. Paper 22 v3 consumed nowhere.

## 2. Definitions

**Definition 2.1 (presented experiment, stabilizer).** As in 13D §5.3/§9.1:
$\widehat e=(\mathcal H_S,f,K,M_{\rm int},M_{\rm land})$; its
stabilizer is $\mathcal G_{\widehat e}=\{g:g\widehat e=\widehat e\}$;
physical history cells are stabilizer orbits $[H]_{\widehat e}$ with
pushed-forward masses.

**Definition 2.2 (admissible observable).** A family
$R_{g\widehat e}:\Omega_{[g\widehat e]}\to O_{gR}$ satisfying the 13D
§9.2 equivariance law $R_{g\widehat e}([gH])=gR_{\widehat e}([H])$.
Any derivation claim must terminate in such an object: a naked
presentation coordinate is not a reader (13D §9.2), and no other
output channel exists — the declared native carrier carries no private
seed, control phase, or history identifier.

**Definition 2.3 (covariant assignment).** A rule $\mathcal A$
assigning to each presented experiment an equivalence class of ordered
pairs $(L_1,L_2)$ of total orders on its occurrence carrier, such that
for every presentation morphism $h$, $\mathcal A(h\widehat e)
=h\,\mathcal A(\widehat e)$ (naturality under the groupoid action),
and whose values factor through the physical quotient of Definition
2.1.

**Definition 2.4 (derivability).** The exchangeable oriented
null-realizer pair is *derived from $\Gamma_D$* iff there exists a
covariant assignment $\mathcal A$ (Def 2.3) whose values are admissible
observables (Def 2.2), realize the intersection condition wherever a
dependency relation is defined, and are unique in any sense claimed.
Derivability fails if any clause is provably unsatisfiable.

## 3. Three obstructions

> **Proposition A (fixed-point obstruction).** For any presented
> experiment with $|{\mathcal G}_{\widehat e}|$ acting transitively-
> containing a transposition of two occurrences ($|I|\ge2$, unmarked
> or mark-symmetric), no admissible observable outputs an ordered pair
> of total orders on $I$.
>
> **Proof.** Let $g\in{\mathcal G}_{\widehat e}$. By Definition 2.1 the
> cell map $[H]\mapsto[gH]$ is the identity on orbit cells, so the
> equivariance law gives $R_{\widehat e}([H])=gR_{\widehat e}([H])$:
> every emitted value is fixed by $g$. The unmarked grand experiment at
> size $n$ has stabilizer containing the full symmetric group (13D §12:
> exchangeable source and seed laws; "no canonical order on $I$ is
> used"), and likewise every experiment whose marks are invariant under
> some transposition $(i\ j)$ admits one. But no ordered pair of total
> orders on a set of size $\ge2$ is fixed by a transposition acting on
> coordinates: a fixed order would need $x<_{L_i}y$ and $y<_{L_i}x$
> simultaneously. Verified exhaustively for $n=2,\dots,5$ over all
> $(n!)^2$ pairs. ∎

*(Citation anchor for the stabilizer claim: 13D §14 — unmarked
$U_\varnothing$ grand experiment, "no canonical order on $I$ is used"
— with Theorem 2's exchangeability argument (§10 of file) and the
port-swap groupoid of §3.1.)*

> **Proposition B (no covariant single order).** Even before
> quotienting: there is no assignment associating to *every* finite set
> $I$ a total order $<_I$, natural under all bijections. Hence no
> covariant assignment (Definition 2.3) exists at any level — reader or
> raw construction — on free carriers.
>
> **Proof.** Naturality under a transposition $\tau$ of $I$ gives
> $\tau(<_I)=<_I$, i.e. a $\tau$-fixed total order: impossible for
> $|I|\ge2$ (Proposition A's counting argument applies verbatim). This
> is the classical fact that finite sets carry no distinguished
> enumeration; Paper 13D honors it structurally ("serialization order…
> occurs in none of these boundary sets", §3.4). ∎

> **Lemma C (bond-law rank blindness).** On the unmarked primitive
> $U_\varnothing(I)$: the joint law of all physical fields — packets,
> colors $d_i=e'_i$, records, and endpoint bonds $\ell_{ij}$ — is
> invariant under any relabeling or independent reversal of the two
> hypothetical ranks. Every field is a function of fair bits, uniforms,
> and the fresh pair seeds $v_{ij}$; the bond law (13D §6.3) depends
> only on color equality and $v_{ij}$. In particular the law contains
> no rank-correlated object whose orientation could be read off.
>
> **Proof.** Each packet coordinate is a bitwise function (13D §6.2) of
> exchangeable inputs; $\ell_{ij}=\mathbb 1[v_{ij}<16\text{ or }9]$
> conditioned on $d_i,d_j$ only. Reversing a hypothetical rank changes
> no input distribution and no kernel. ∎

> **Proposition D (informational obstruction).** There exist two rank
> couplings with identical complete $\Gamma_D$ law but different
> oriented permutation-pattern densities. Hence the oriented pair is
> not a functional of the accepted law, even up to the physical
> quotient.
>
> **Proof.** Fix three occurrences. Coupling A draws $L$ uniformly and
> sets $(L_1,L_2)=(L,\mathrm{rev}\circ L)$; coupling B draws $L$
> uniformly twice independently… specialize B to $(L,L)$. Under both
> couplings the induced joint law of $(d_i)_{i},(\ell_{ij})_{ij}$ is
> identical by Lemma C (colors and bonds do not see ranks), so the
> physical quotient cells and masses coincide — $\Gamma_D$ assigns the
> same law to both worlds. Yet the oriented increasing–increasing
> pattern density is $0$ under A (both ranks increase simultaneously is
> impossible for a list and its reverse) and $\frac16$ under B. Two
> different oriented-pattern laws over one $\Gamma_D$ law: the pair is
> underdetermined. ∎

> **Theorem E (main no-go).** The exchangeable oriented null-realizer
> pair is not derivable from terminal $\Gamma_D$: Definition 2.4 fails
> at every clause. Propositions A/B kill existence of a covariant
> admissible assignment on symmetric experiments and on free carriers;
> Proposition D kills determination by the law even where bookkeeping
> might permit a decoration; and where the obstructions momentarily
> lapse (§4), uniqueness fails instead.
>
> **Proof.** Immediate composition of Propositions A, B, D and §4. ∎

Outcome: **`P23C-ORIENTED-PAIR-NOT-DERIVABLE`.**

## 4. The landmark loophole, closed

A reader-free experiment may declare landmarks $M_{\rm land}$
(13D §5.3/§9.2), shrinking the stabilizer; a fully landmark-rigid
experiment has trivial stabilizer, where Proposition A's fixed-point
demand is empty. This does not reopen derivability:

> **Proposition F (rigid-experiment uniqueness failure).** On any
> trivial-stabilizer experiment, every function from history cells to
> order-pairs is admissible (equivariance is vacuous). Given any two
> candidates producing different oriented-pattern laws — they exist,
> since both constant-on-cells assignments and their swaps are
> admissible and differ — $\Gamma_D$ provides no datum selecting
> between them. Choosing one would require smoothness, aesthetics, or
> apparatus preference, all forbidden (#237 decoder-nonselection wall,
> pin control 1). Derivability therefore fails on uniqueness, exactly
> where it fails on existence elsewhere.
>
> **Proof.** Vacuous equivariance makes all assignments admissible;
> Lemma C shows the law is blind to the distinction any choice would
> encode; the pin forbids extra-legal selection principles. ∎

The landmarks are apparatus presentation, not law content (13D §5.3:
"It orients an apparatus but does not choose a reader function");
importing them as an order source would smuggle orientation in through
declaration (pin control 4).

## 5. Positive residual — what Γ_D does derive

Exactly this much order content descends covariantly:

- the **undirected endpoint-bond graph** $\{i,j\}\mapsto\ell_{ij}$:
  equivariant by Lemma C's proof, defined at every size, the unique
  maximal $\Gamma_D$-native binary relation (`P23C-UNORIENTED-BOND-
  STRUCTURE-DERIVED`);
- the **exchangeability class** of any externally supplied pair:
  Paper 15's $\pi_n$ invariances (simultaneous transport, rank swap)
  match $\Gamma_D$'s groupoid action, so the contract's quotient is
  coherent — but coherence is not supply.

This residual is precisely Paper 14/Paper 15's unlabeled structural
poset situation: dependency-without-direction. The gate closes the way
Paper 15 anticipated: the accepted law sits on the *insufficient* side
of its dichotomy.

## 6. Outcomes earned

```text
P23C-ORIENTED-PAIR-NOT-DERIVABLE              (primary, pin §5)
P23C-EQUIVARIANT-FIXED-POINT-OBSTRUCTION      (Prop A)
P23C-NO-COVARIANT-SINGLE-ORDER                (Prop B)
P23C-LAW-RANK-INVARIANCE                      (Lemma C + Prop D)
P23C-RIGID-EXPERIMENT-UNIQUENESS-FAILURE      (Prop F)
P23C-UNORIENTED-BOND-STRUCTURE-DERIVED        (§5 residual)
```

Not earned (correctly absent):
`P23C-ORIENTED-PAIR-DERIVED-COVARIANTLY`,
`P23C-ORIENTED-PAIR-GATE-BLOCKED`.

**Dimension firewall:** no dimension, cardinality-volume, or ensemble
statement is made anywhere above; the Unit D ensemble gate remains
closed; Paper 15's rigidity theorem remains CONDITIONAL, now with its
missing bridge proved missing for the present law rather than merely
unbuilt.

## 7. Hostile-control matrix (pin §6)

| # | control | disposition |
|---|---|---|
| 1 | smuggled smoothness | no regularity axiom anywhere; Prop F refuses aesthetic selection |
| 2 | smuggled metric | no distance/volume/conformal object appears |
| 3 | representative choice | Props A/D stated and proved on orbit cells and pushed-forward masses |
| 4 | naked-coordinate reader | Def 2.2 restricts to §9.2 observables; §4 refuses landmark smuggling |
| 5 | chronology leakage | derived structures called structural throughout; no causal claim |
| 6 | local-X/Y swap blindness | port swaps are stabilizer elements whenever marks are swap-invariant; Prop A covers them |
| 7 | Paper 15 import drift | only Def 2.4's target contract used; §1 enumerates the forbidden imports |
| 8 | vacuous derivation | intersection condition required wherever a dependency relation exists; residual §5 is non-vacuous |
| 9 | uniqueness assumed | uniqueness nowhere claimed; its FAILURE is Prop F |
| 10 | dimension creep | firewall §6 |

## 8. Comparators

Terminal Paper 13D bytes (sole scientific source); Paper 15 §§4.8/5
(target contract and its own statement of the open gate); the #237
decoder-nonselection theorem; the classical no-natural-ordering fact
underlying Proposition B; Janson-style exchangeable-poset limits as
named by Paper 15 (context only — no theorem imported). No comparator
supplies probability, orientation, or geometry.
