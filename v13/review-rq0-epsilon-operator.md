# R1 — OPERATOR-LENS HOSTILE REVIEW

## ε-Admissibility and the Mixed-Law Arena (RQ0-L3, stage 5)

**Reviewer:** R1, operator lens. **Protocol:**
`v13/note-rq0-epsilon-hostile-protocol.md` (frozen, d670892). **Object:**
`v13/paper-rq0-epsilon-admissibility.md` + `v13/code/rq0_l3_epsilon_*`
(d5eca4e). **Pin:** 6e1aa82. **Primary kill-shot:** K1 (the inversion's
state-robustness), plus the closed form re-proved and the spectrum/tower
welds re-verified.

**Method.** Everything below was recomputed on code written for this review
alone — own partition generator, own law constructors (DET, REV, FUNNEL,
FUNNEL's composition closure, the counter-law by its own saturation from the
block-minimum idempotents, and the left-total relation family ALL), own
`Pres`, own per-task defect, own ε, ω and reachability. Nothing is imported
from the unit; exact `Fraction` arithmetic throughout; no float appears in any
path. 28 quantities were recomputed independently, plus an exhaustive
4845-state sweep of the state simplex.

---

# VERDICT

$$\boxed{\texttt{ACCEPT-WITH-FIXES}}$$

**No false number was found.** Every substantive number in the paper — the
spectrum with its counts, the closed form, the four named boundaries and their
closure sizes, the whole cost tower with every graded-cost cell, the residues,
the tolerance-admission counts, the monotonicity sweep, the (i-b′) family
sizes, the sub-law control, ω's four rows — reproduces exactly on independent
code. The `EPSILON-BLIND` headline is correct.

It is also **weaker than the unit's own materials support**, and that is the
substance of this review. K1's question — *is there an admitted state where ε
DOES separate?* — is answered **no, at every state in the simplex and not
merely at the committed one**, and it is answered by a theorem the unit has
both halves of and never assembles. The headline needs no state-quantifier
rescope; it needs strengthening. Alongside that, one theorem ships without the
hypothesis its own proof requires (no number moves), one scope tag claims a
sweep that was not run, and one declared component — the state — carries the
same escape as the declared law with none of §8's closure machinery and no
registration.

---

# 1. FINDINGS, RANKED

## F1 — MAJOR. The inversion is a theorem, not a measurement, and it holds at every state. K1 answered.

The paper measures the inverted ordering at the committed state and discloses
(§3.1) that ε is state-relative. Placed as it is, the disclosure invites the
reading that a differently declared state might rescue the separation. **It
cannot, and this is provable from two things the unit already owns.**

**(i) The committed boundaries form a single refinement chain.** Verified:

$$\{0\mid1\mid2\mid3\mid4\}\ \prec\ \underbrace{\{01\mid2\mid3\mid4\}}_{\textbf{FORGED}}\ \prec\ \underbrace{\{01\mid23\mid4\}}_{\textbf{FORGED}}\ \prec\ \underbrace{\{0123\mid4\}}_{\textbf{LEGITIMATE}}\ \prec\ \{01234\}$$

Both forgeries are **refinements** of the legitimate coarse chart.

**(ii) ε is monotone under refinement at every law and every state** — which
Prop 6.1 *measures* (1790 instances) but never *proves*. The proof is two
lines: if $\pi\preceq\pi'$ then $\operatorname{Pres}_L(\pi)\subseteq
\operatorname{Pres}_L(\pi')$, and for each $F$ in the smaller set
$d(F,\pi,\rho)\le d(F,\pi',\rho)$ because each block of $\pi'$ is a union of
blocks of $\pi$ and $\max$ over a union is at most the sum of the maxima.
Both facts are law-free and state-free.

**Corollary (the one the paper should be stating).** For every law and every
declared state,
$$\varepsilon(\text{forged }2{+}1{+}1)\ \le\ \varepsilon(\text{forged }2{+}2)\ \le\ \varepsilon(\text{legitimate}),$$
hence a threshold admitting the legitimate coarse patch while rejecting either
forgery would need $\varepsilon(\text{legit})<\varepsilon(\text{forged})\le
\varepsilon(\text{legit})$. **The forward separating set is empty at every
state in the simplex**, not at the committed one only.

**The closed-form state map** (my derivation, verified on all 4845 grid states
and by max-over-`Pres` on 13 named states × 5 laws):

| boundary | ε as a function of the declared state |
|---|---|
| forged $2{+}1{+}1$ | $\min(\rho_0,\rho_1)$ |
| forged $2{+}2$ | $\min(\rho_0,\rho_1)+\min(\rho_2,\rho_3)$ |
| legitimate $\{0123\mid4\}$ | $\min(\rho_0,\rho_1)+\min(\rho_2,\rho_3)+\min\bigl(\max(\rho_0,\rho_1),\max(\rho_2,\rho_3)\bigr)$ |

The two gaps are $\min(\rho_2,\rho_3)\ge0$ and
$\min(\max(\rho_0,\rho_1),\max(\rho_2,\rho_3))\ge0$: **non-negative at every
state, and strictly positive at every full-support state.** So under the
reduction theorem's own hypothesis the inversion is not merely present, it is
*strict*, everywhere.

Measured (exhaustive grid, all $\binom{20}{4}=4845$ states with denominator
16): weak inversion **4845/4845**; strict inversion at **1365/1365**
full-support states; forward separating set empty at **4845/4845**;
monotonicity violations **0** over $306\times4845=1{,}482{,}570$ pair-state
instances.

**Consequence for the registration.** `RQ0-L3-EPSILON-BLIND` does **not** need
a state-quantifier rescope. It should be re-scoped *upward*: from "measured at
the committed state" to "proved at every declared state, strictly at every
full-support one". The structural proof (Thm 5.3) gains the measured companion
K1 asked for — and more, a proved one.

## F2 — MAJOR. The amnesty is selective, not uniform, and the reverse separation is non-empty.

The paper reports that the forward separating set is empty. The sharper true
statement, absent from the paper: **the reverse separating set is not.**

- At the committed state, $\tau=1/8$ admits **both** forgeries ($1/16$, $1/8$)
  and **rejects** the legitimate coarse chart ($3/16$). Over the 4845-state
  grid, a threshold admitting both forgeries while rejecting the legitimate
  chart exists at **4540 of 4845 states**.
- At the state $\rho=(1/2,0,1/2,0,0)$ both forgeries have $\varepsilon=
  \mathbf{0}$ while the legitimate coarse chart has $\varepsilon=1/2$. **At
  tolerance zero — the terminal axiom's own tolerance — the ε-form certifies
  both forgeries and rejects the legitimate coarse chart.**

This strictly strengthens §3.1's degenerate control. At the sink-degenerate
state *every* boundary has $\varepsilon=0$ (I reproduced this: the whole
spectrum collapses), which reads as a corner case of a uniform amnesty. At
$(1/2,0,1/2,0,0)$ the amnesty **discriminates in the adversary's favour**. The
escalation the paper registers is real; it is also worse than registered.

## F3 — MAJOR. The declared state is a fifth declaration with the same escape and no closure route. Unregistered.

§8 formalizes the mixed-law arena and closes it twice, pricing both routes.
The declared **state** is declared per patch exactly as the law is — §3.1 says
so in terms ("whoever declares the state moves the number") — and there is no
mixed-state arena anywhere in the unit.

The asymmetry is structural, not an oversight of effort: route (i) needs a
*least law containing both* and route (ii) needs a *descent filter over
admissible boundaries*. **Neither construction has a state analogue.** There
is no least state containing two declared states and no state-relative
descent. Combined with F2, an adversary who declares the state of his own
patch holds a $\tau=0$-admissible forgery against a rejected legitimate chart
— an escape strictly cheaper than the mixed-law one, and one the unit closes
zero times rather than twice.

What holds it back is a single sentence — "The committed state is laboratory
data here, so the measurements below stand" (§3.1) — asserted, not gated,
while the exactly parallel doctrinal question for the law (*admission is
measured per law and never inferred from algebraic existence*) is inherited,
cited and enforced against route (i). Either the state's laboratory-datum
status gets the same explicit doctrinal citation, or a `RQ0-L3-MIXED-STATE-…`
rung (open, or priced) belongs in the verdict box.

## F4 — MODERATE. Theorem 4.2 ships without the hypothesis its own proof needs. No number moves.

Theorem 4.2 is stated "**Let $L$ contain the identity.** Then for every
carrier-typed boundary, $\varepsilon(\pi)=\sum_r[\Pr(r)-\max_{j\in r}\rho_j]$"
and its proof turns on $\max_s\Pr(r,s)\ge\max_{j\in r}\rho_j$ — "the mass of a
single configuration is a lower bound on the mass reaching whichever later
configuration it reaches".

**That inequality is false as soon as an admitted operation has a multivalued
support**, which Definition 2.1's own $\rho_j/\lvert\operatorname{sup}_F(j)
\rvert$ construction is written to accommodate and which this corpus's `ALL`
family instantiates. Counterexample, exact and inside the corpus's own law
list: at $\mathrm{ALL}(2)$ — 9 relations, composition-closed, identity-
containing, all three verified by me — with $\rho=(3/4,1/4)$ and the boundary
$\{01\}$, the closed form gives $1/4$ while $\varepsilon=\mathbf{1/2}$,
attained at $\operatorname{sup}(0)=\operatorname{sup}(1)=\{0,1\}$. At the
committed carrier and the committed state, the single admitted operation
$\operatorname{sup}(j)=\{4\}\,(j\le3),\ \operatorname{sup}(4)=\{0,1\}$ lies in
$\operatorname{Pres}$ of the one-atom boundary and has $d=\mathbf{5/8}$ —
outside the five-value spectrum entirely, so **Theorem 4.1's "the same five
under every committed law" is determinism-dependent too**.

**Severity is contained and I checked it four ways.** (1) All five committed
laws at five configurations are single-valued — 3125, 21, 120, 3006 and 120
operations, every support a singleton, verified. (2) `ALL` enters this unit
only at $n\le4$ (its presence is what makes the reduction sweep's 368 come
out: $4\cdot2+5\cdot5+5\cdot15+5\cdot52$). (3) At the uniform states the unit
uses there, the closed form still holds under `ALL` — 22 records at 2, 3 and 4
configurations, **0 mismatches** (I ran it; the unit did not). (4) The code
*knew*: the source comment above gate L3-24 reads "**for deterministic F**,
max_s Pr(r,s) >= max_{j in r} rho_j". The hypothesis was dropped on the way
into the paper. Fix = one clause in the statement and one in the proof.

## F5 — MODERATE. Theorem 4.2's `[EXH-5]` tag claims a sweep that was not run.

The Scope box defines `[EXH-5]` as "additionally verified exhaustively over
all records at two to five configurations against every committed law". Gate
L3-24 measured **260 instances at five configurations only** (52 records × the
five identity-containing $n=5$ laws) — the receipt says so in its own value
field. The claim happens to be true at $n\le4$ as well (F4(3): I ran it), but
it was true *unmeasured*. Either re-tag Theorem 4.2 `[FIN]` or run the sweep.

## F6 — MINOR. One gate citation is over-scoped.

§4, immediately under the five-row spectrum table: "The three named coarse
boundaries carry strictly positive defect under every one of these laws (gate
`L3-05`)". `L3-05` runs **four** laws — DET, REV, FUNNEL-CLOSURE, COUNTER-LAW
(12 rows, as the receipt records) — while "these laws" is the five-row table
*including FUNNEL*. The claim is true for FUNNEL (I measured $1/16$, $1/8$,
$3/16$ there), but the covering gate is `L3-24`, not `L3-05`.

## F7 — MINOR. "1790 pairs" is 1790 (pair, law) instances.

Prop 6.1 and the receipt field `comparable_pairs_checked` both read as 1790
distinct pairs. There are **358** distinct strictly comparable pairs at three,
four and five configurations ($7+45+306$); swept against five laws at each
arity they give $35+225+1530=1790$ instances. My sweep reproduces both numbers
and 0 violations.

## F8 — MINOR. The common gate "state-relativity named at every ε claim" is not met.

Theorem 5.2's table, Theorem 6.2's tower table, §6.1's two amnesty paragraphs
and Theorem 9.3's ω table all carry state-dependent exact numbers with no
state named in the local context. (Theorem 4.1 does name it; Theorem 5.1's own
headline, per F1, needs the universal statement rather than a tag.)

## F9 — MINOR. Theorem 5.3's exhibit does no work.

Gate `L3-09` exhibits two declarations with identical defects — but both
defects are **0**, at the carrier's own configuration algebra, the one
boundary where ε is trivially zero and the terminal axiom already admits. As
an exhibit of blindness *at a coarse patch* it is empty; the paper calls it
"Exhibited rather than asserted". The working exhibit is F1's inverted chain.

## F10 — OBSERVATION. The successor constraint is sharper than BLOCKED-AT-PROVENANCE.

The mechanism is not just "coarseness and provenance are orthogonal". It is
that **the committed forgeries sit below the legitimate chart in the
refinement order**. Therefore *no refinement-monotone statistic whatever* —
not merely no function of the quadruple, and not even one that reads
provenance — can separate them by a threshold. Any successor must be
non-monotone in the refinement order, or must be a cross-patch condition. This
is strictly stronger than `RQ0-L3-BLOCKED-AT-PROVENANCE` as a constraint on
the next stage, and it is derivable from the unit's own §6.1 aside ("a grading
monotone in coarseness is a measure of coarseness"), which the paper leaves as
a remark rather than promoting to the finding it is.

---

# 2. THE K1 STATE MAP

The inverted ordering, attacked with every state the unit admits and then with
the whole simplex. `fwd` = some threshold admits the legitimate coarse patch
and rejects both forgeries. `rev` = some threshold admits both forgeries and
rejects the legitimate patch. Both ε routes (max over `Pres_DET`, and the
closed form) agree on every row.

| declared state | ε forged 2+1+1 | ε forged 2+2 | ε legitimate | fwd | rev | strict inversion |
|---|---|---|---|---|---|---|
| committed $(1,1,1,1,12)/16$ | 1/16 | 1/8 | 3/16 | **no** | yes | yes |
| uniform at five | 1/5 | 2/5 | 3/5 | **no** | yes | yes |
| degenerate on the sink (the unit's control) | 0 | 0 | 0 | **no** | no | no (all tie) |
| sink mass moved to address 0 | 1/16 | 1/8 | 3/16 | **no** | yes | yes |
| sink mass moved to address 1 | 1/16 | 1/8 | 3/16 | **no** | yes | yes |
| sink mass moved to address 2 | 1/16 | 1/8 | 3/16 | **no** | yes | yes |
| sink mass moved to address 3 | 1/16 | 1/8 | 3/16 | **no** | yes | yes |
| near-degenerate $(1,1,1,1,996)/1000$ | 1/1000 | 1/500 | 3/1000 | **no** | yes | yes |
| colluding pair starved $(0,1,1,1,13)/16$ | 0 | 1/16 | 1/8 | **no** | yes | yes |
| asymmetric full support $(1,2,3,4,6)/16$ | 1/16 | 1/4 | 3/8 | **no** | yes | yes |
| legitimate-favouring attempt $(7,1,1,1,6)/16$ | 1/16 | 1/8 | 3/16 | **no** | yes | yes |
| flat on the four addresses $(4,4,4,4,0)/16$ | 1/4 | 1/2 | 3/4 | **no** | yes | yes |
| **adversarial $(1/2,0,1/2,0,0)$** | **0** | **0** | **1/2** | **no** | **yes, at $\tau=0$** | no |

Exhaustive grid, all 4845 states of denominator 16:

| quantity | value |
|---|---|
| states where a threshold admits the legitimate patch and rejects both forgeries | **0 / 4845** |
| states where a threshold admits both forgeries and rejects the legitimate patch | **4540 / 4845** |
| states with weak inversion $\varepsilon(f_1)\le\varepsilon(f_2)\le\varepsilon(\text{legit})$ | **4845 / 4845** |
| full-support states in the grid / of them strictly inverted | **1365 / 1365** |
| monotonicity violations, 306 comparable pairs × 4845 states | **0** of 1,482,570 |
| max-over-`Pres` vs closed form, 50 sampled states × 5 laws × 5 boundaries | **0** mismatches of 1250 |
| identity-free laws: monotonicity violations (2 arities, 2 states each) | **0** of 222 |

**Answer to K1.** There is no admitted state at which ε separates; there is no
state at all. The blindness headline does not need a state-quantifier rescope
— it needs to be stated for all states, with the two-line proof. What the
declared state *can* do is lower every defect together (§3.1's real content)
and, per F2, make the amnesty selective in the adversary's favour. It can
never reorder.

---

# 3. NUMBERS — 28 INDEPENDENT RECOMPUTATIONS

All recomputed on own code, exact rationals. "Committed" = the paper/receipt.

| # | quantity | committed | recomputed | ✓ |
|---|---|---|---|---|
| 1 | record-lattice sizes at 1–5 configurations | 1, 2, 5, 15, 52 | 1, 2, 5, 15, 52 | ✓ |
| 2 | law sizes DET / FUNNEL / REV / FUNNEL-CLOSURE / COUNTER-LAW | 3125, 21, 120, 3006, 120 | same | ✓ |
| 3 | all five contain a reversible operation and the identity | yes | yes | ✓ |
| 4 | FUNNEL composition-closed at five configurations | no (task family) | no | ✓ |
| 5 | permutations in the counter-law | (identity only) | 1 | ✓ |
| 6 | $\lvert\operatorname{Pres}_{\rm DET}\rvert$: forged 2+1+1 / 2+2 / legit / carrier algebra | 240, 420, 1280, 120 | same | ✓ |
| 7 | ε of the four named boundaries, committed state | 1/16, 1/8, 3/16, 0 | same | ✓ |
| 8 | …under all five committed laws (20 cells) | identical | identical | ✓ |
| 9 | spectrum values over all 52 records | 0, 1/16, 1/8, 3/16, 1/4 | same | ✓ |
| 10 | spectrum counts | 1, 10, 25, 15, 1 | same | ✓ |
| 11 | five spectra identical across law sizes 21…3125 | yes | yes | ✓ |
| 12 | closed form vs ε, committed carrier | 260 instances, 0 mismatch | 260, 0 | ✓ |
| 13 | independent analytic form $\varepsilon=1/4-k/16$, $k$ = atoms missing the sink | — | holds; counts 1,15,25,10,1 by $k$ | ✓ |
| 14 | admitted records at $\tau=0$ / $1/16$ / $3/16$ | 1, 11, 51 | 1, 11, 51 | ✓ |
| 15 | …and at $1/8$ and $1/4$ (not in the paper) | — | 36, 52 | — |
| 16 | full ε-admissibility (with ω and clause (d)) vs ε alone | (paper reads ε) | identical at all five tolerances | ✓ |
| 17 | ten boundaries attain 1/16; all single-pair merges; forgery among them | yes | yes | ✓ |
| 18 | cost tower $\lvert\operatorname{Obs}_0\rvert$ | 120, 360, 1260, 3120 | same | ✓ |
| 19 | tower residues $3125-\lvert\operatorname{Obs}_0\rvert$ | 3005, 2765, 1865, 5 | same | ✓ |
| 20 | graded costs, record level | $0\!\to\!120$; $1/16\!\to\!0$ | same | ✓ |
| 21 | graded costs, boundary level | $360$; $120$; $0$ | same | ✓ |
| 22 | graded costs, coarser level | $1260$; $1020$; $120$; $0$ | same | ✓ |
| 23 | graded costs, the limit | $3120$; $3040$; $2560$; $1280$; $0$ | same | ✓ |
| 24 | tasks attaining the maximum at the record level | 120 of 240 | 120 of 240 | ✓ |
| 25 | monotonicity sweep | 1790, 0 violations | 1790 (= 358 pairs × 5 laws), 0 | ✓ (label, F7) |
| 26 | (i-b′) family sizes; boundaries admitted | 120, 60, 20; 52 of 52 | same | ✓ |
| 27 | sub-law control at $\{(0,0,2,3,4)\}$: closed, identity-free, $\lvert\mathfrak F\rvert$, ε | yes, yes, 1, 0 | same | ✓ |
| 28 | ω: W1 / W3 / carrier full prep / carrier prep $\{0\}$ | 0, 2/3, 0, 15/16 | same (reach $=\{0\}$, $\lvert\mathfrak F\rvert=1$) | ✓ |

Additional (this review's own, not in the unit): the reduction sweep's 368 =
$4\cdot2+5\cdot5+5\cdot15+5\cdot52$ reconstructed, confirming `ALL` is a
committed law at $n\le4$; the closed form under `ALL` at 2, 3, 4 configurations
(22 records, 0 mismatches); the `ALL(2)` counterexample $\varepsilon=1/2$ vs
closed form $1/4$; the multivalued witness at the committed carrier, $d=5/8$;
δ $=0$ at the carrier algebra under both preparations (σ/δ blindness);
the refinement chain of all five committed boundaries.

Receipt-vs-paper sweep: **25/25 gates pass, 19/19 anchors pass**; every gate
value I checked matches the paper's prose (368/3435/0; 745/745; 1/11/51; the
nine thresholds tried $0,1/32,1/16,3/32,1/8,5/32,3/16,7/32,1/4$; 1790/0;
120/360/1260/3120; 120/60/20; 14 of 15; 51 → 1; 3125; 240 vs 1; 0, 2/3, 0,
15/16). `L3-00` reports no float literal; no wall-clock string appears in the
rendered output. Forbidden vocabulary: clean — "spacetime", "locality",
"manifold", "QFT", "gravity", "causal" occur only inside the scope box and the
non-claims.

---

# 4. PER-RUNG CONFIRMATIONS

**(a) `EPSILON-BLIND`, the inverted ordering, the structural proof —
CONFIRMED and STRENGTHENED.** Ordering $1/16<1/8<3/16$ reproduced by both
routes under all five committed laws; separating set empty at all nine
thresholds, at all 4845 grid states, and provably at every state (F1). The
structural proof of Thm 5.3 is valid as stated; its exhibit is weak (F9) and
it is not the strongest argument available (F10).

**(b) The ε = 0 reduction, both directions — CONFIRMED at operator scope.**
The instance arithmetic reconstructs (368; 3435 census; 745/745 receipt-
consistent), and my own $\tau=0$ sweep gives exactly 1 admissible record of 52
under DET at the committed state, with full ε-admissibility agreeing with
ε-only at every tolerance tested. Full re-derivation of the census is R2's.

**(c) The closed form — CONFIRMED at the committed scope, with a missing
hypothesis and a bad tag.** Re-proved independently; agrees on 260/260
instances and on a further 1250 instances over sampled states × 5 laws × 5
boundaries. Fixes: F4 (determinism hypothesis), F5 (`[EXH-5]`).

**(d) Mixed-law closures + the law-free-descent finding — NOT MY PRIMARY; no
objection.** Receipt-consistent throughout (3125; 240 vs 1; 14 → 0; 51 → 1).
The operator lens adds F3: the same escape via the declared *state* has no
closure route at all and is unregistered.

**(e) ω's separations — CONFIRMED independently.** $0$ vs $2/3$ at three
configurations and $0$ vs $15/16$ at the committed carrier, with δ $=0$ in all
four rows; in both prep-$\{0\}$ rows the declared family is the identity alone
and the reachable subprocess is $\{0\}$, which is exactly why ω moves and δ
does not.

**(f) The rung set, including the combined `MIXED-LAW-CLOSED` +
`PLURALISM-PRICED` registration — HONEST BUT INCOMPLETE.** No
having-it-both-ways from the operator side: at the measured scope the escape
does close by both routes and the price is the finding, and the paper states
both. Incomplete because the declared state is a fifth declaration with the
same escape structure and no closure (F3), and because `EPSILON-BLIND` is
registered at a scope narrower than the truth (F1).

---

# 5. SENTENCES TO REWRITE

1. **§5, Theorem 5.1** — replace the measured framing with the theorem.
   Currently: "*Every value of the spectrum and every midpoint between
   consecutive values is tried … and the separating set is empty … Worse than
   empty: the ordering is inverted. At the committed state …*". Should read,
   in substance: *the two forged boundaries are refinements of the legitimate
   coarse boundary, and ε is monotone under refinement at every law and every
   state; hence $\varepsilon(\text{forged})\le\varepsilon(\text{legitimate})$
   at every declared state and the separating set is empty at every state,
   strictly so at every full-support state. At the committed state the values
   are $1/16$, $1/8$ and $3/16$.* The threshold sweep then corroborates a
   theorem instead of standing in for one.

2. **§6, Proposition 6.1** — "Measured exhaustively over every strictly
   comparable pair … 1790 pairs, zero violations" → state the two-line proof
   first and keep the sweep as corroboration, and correct the count to *358
   distinct comparable pairs, 1790 (pair, law) instances*.

3. **§4, Theorem 4.2** — add the hypothesis the proof uses: "Let $L$ contain
   the identity **and let every admitted operation be single-valued (verified
   for all five committed laws)**". In the proof, the sentence "For any
   admitted future, $\max_s\Pr(r,s)\geq\max_{j\in r}\rho_j$" needs "for any
   admitted **deterministic** future", with a footnote that the inequality
   fails for multivalued supports (witness: $\mathrm{ALL}(2)$,
   $\rho=(3/4,1/4)$, $\varepsilon=1/2$ against the closed form's $1/4$).
   Theorem 4.1's "the same five under every committed law" needs the same
   qualifier.

4. **§4, Theorem 4.2's scope tags** — drop `[EXH-5]` or run the $n\le4$
   sweep; gate `L3-24` measured five configurations only.

5. **§4, under the spectrum table** — "under every one of these laws (gate
   `L3-05`)" → cite `L3-24` (which covers all five) or say "under DET, REV,
   the funnel closure and the counter-law (gate `L3-05`); under FUNNEL by the
   spectrum table and `L3-24`".

6. **§3.1, the state-relativity paragraph** — after "an adversary who declares
   the state can drive any coarse boundary's defect as close to zero as the
   state's support allows", add the countervailing fact, which is the whole
   K1 result: *what the declared state cannot do is reorder the three
   boundaries — the inversion holds at every state — so the exposure is
   uniform lowering, never rescue.* And add F2's sharper control: at
   $\rho=(1/2,0,1/2,0,0)$ both forgeries carry defect 0 while the legitimate
   coarse chart carries $1/2$, so tolerance zero certifies the forgeries and
   rejects the legitimate chart. The present degenerate-state control
   understates the exposure because there *everything* collapses to 0.

7. **§5.2 / §6.2 / §6.1 / §9.3** — name the declared state locally in the
   tolerance table, the tower table, the two amnesty paragraphs and the ω
   table; every number in them is state-dependent.

8. **§8 or §11** — register the state. Either add to the non-claims that *the
   declared state is treated as laboratory data at this scope, and the
   mixed-state arena — two patches declaring different states — is not
   formalized and has no closure route analogous to shared refinement or
   inter-law descent*, or open the rung. As it stands §8 prices pluralism in
   the law while the same pluralism in the state is unpriced and unnamed.

9. **§5.3 / §10** — promote the mechanism. "Forgery is a property of how a
   declaration came to be made; coarseness is a property of the declaration"
   is right but weaker than what is proved: *the committed forgeries are
   refinements of the legitimate chart, so no refinement-monotone statistic —
   not merely no function of the quadruple — can separate them by a
   threshold. The successor must be non-monotone in the refinement order or
   must live on the atlas rather than on the patch.* This sharpens "The next
   obstruction, named" into an actual constraint on the successor.

---

# 6. WHAT SURVIVED THE ATTACK

Stated plainly, because most of the unit did survive it: the ε-form's
construction, its reduction, its spectrum, its closed form at the committed
scope, its monotonicity, its weld to the cost tower and every one of its
graded-cost cells, the two negative controls, ω's four rows and the honesty of
reporting the pin's required outcome as refuted — all reproduce exactly on
independent code. The headline finding is not merely intact but understated.
The fixes above move no number in the paper.

**Verdict: `ACCEPT-WITH-FIXES`.**

*R1, operator lens. Frozen on delivery.*
