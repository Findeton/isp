# Paper 23d adjudication correction — terminal withdrawn; scalar-reweighting scope restored

Date: 2026-08-22

Disposition: **FORWARD-ONLY ADJUDICATION CORRECTION TO #335/#336 —
`P23D-ORIENTATION-FIBER-INERT` AND TERMINAL ACCEPTANCE WITHDRAWN;
CORRECTED COORDINATES `P23D-SCALAR-REWEIGHTING-INERT`,
`P23D-STATE-EXTENSION-UNTESTED`; SUCCESSOR MAP CORRECTED**

User-ordered semantic correction after the user identified three
structural defects. Frozen bytes are untouched: the candidate remains
at `2501d316fb9071062a7e50d32ec8fd64af2fdf660f6ca037a1a8a837fc34408a`;
this note and the ledger carry the corrected state. #336 is **not**
terminal as of this entry.

## 1. Bound corpus

| object | ordinary SHA-256 |
|---|---|
| Paper 13D | `3b91766fe269e8145766f4622f99e9009c3270530670119735e6045a473de5c9` |
| P23d pin (#332) | `112684d6eaf4f68489742fc1e046ca9b5af6fafb41f9f6e8e908425431b965ba` |
| P23d candidate pre-repair (#333) | `699fe5b72037f47a6ef93b51af548a7b476a400a94230eb3d3c606bdf95a52e8` |
| P23d candidate post-repair (#336, unchanged) | `2501d316fb9071062a7e50d32ec8fd64af2fdf660f6ca037a1a8a837fc34408a` |
| Seats (#334) | `5dcff03a…`, `e5670376…`, `9005f0e9…` |
| Adjudication (#335) | `cc2857134abacaa72f7bf9ef817da5b86ac03dabab184637ef50e1ce81a70d37` |
| #330 correction (binding precedent) | `a462a10d1f590c7581951db609fdaa66ea1aced17f1f92889540c9f6bd4b503e` |

## 2. The three defects, confirmed

**D1 — Q1 misapplied a #330-refuted implication.** Q1 argued: a
covariant extractor $\mathsf{Cpx}\to$ exchangeable *classes* would
restrict to an order-valued covariant assignment on free carriers,
hence impossible by `P23C-NO-COVARIANT-SINGLE-ORDER`. But #330
explicitly established the opposite direction: ordered-pair fixed-point
arguments do NOT transfer to quotient-valued targets — class-valued
covariant existence was left open there, and this unit was supposed to
test it. The restriction argument proves only that no *order-valued*
extractor exists; it says nothing about class-valued ones. Q1's "NO"
verdict is unproven as printed.

**D2 — Lemma A ignored the realizer intersection condition.** The
target type requires the pair to *realize* the dependency relation:
$x\prec y\iff x<_{L_1}y\wedge x<_{L_2}y$. Parallel and antiparallel
pairs do not realize the same relation — verified directly at $n=3$:
parallel $(L,L)$ yields the chain $0<1<2$; antiparallel
$(L,\mathrm{rev}\circ L)$ yields the antichain. Lemma A's claim that
both "realize over every complex" is false for any complex with a
nontrivial fixed dependency, and its fiber counts (2/5/17) counted all
decorations regardless of realizability. The within-fiber multiplicity
lemma fails as stated.

**D3 — Lemma B assigned probabilities outside the pinned space.** The
external decorations of Def 1.1 are not points of the pinned
probability space; the joint law assigns them *no* probability at all.
"Equal mass to every event containing them" conflated an omitted
latent variable (underdetermined) with a uniformly weighted one
(determined). What actually follows from pin §§2–4 is only: the joint
law, being fiber-blind by construction, cannot distinguish
decorations it never measured — underdetermination, not inertness of
all weights.

Additionally recorded: **the pin itself pre-excluded every
orientation-bearing root variable** (pin §3 barred orders/ranks at
input), so the gate never tested the full state/root symmetry-breaking
door of synthesis §3(b) — it tested scalar reweighting of an
orientation-forgetting measurable space.

## 3. Withdrawn

```text
P23D-ORIENTATION-FIBER-INERT     (withdrawn: rests on D1–D3)
TERMINAL ACCEPT-WITH-SCOPE #336  (withdrawn)
```

Theorem C, Lemmas A/B in their printed forms, and the Q1 verdict are
withdrawn with them. The three seats' approvals and #335's
confirmations are voided insofar as they endorsed these objects; the
seats did flag adjacent weaknesses (F-P1's near-vacuous Lemma B,
F-C2's ambiguous Def 1.1) whose full implications were not drawn at
adjudication.

## 4. Preserved

Two results stand, both independently supported:

1. **Γ_D does not determine the realizer class** — #330, unchanged.
2. **Scalar reweighting of the unchanged orientation-forgetting
   measurable space cannot create a missing measurable variable** —
   the corrected residue of Lemma B/Q3(ii): if the σ-algebra carries
   no orientation copy, multiplying by a weight on the same space adds
   none. This is now recorded as:

```text
P23D-SCALAR-REWEIGHTING-INERT        (earned, corrected scope)
P23D-STATE-EXTENSION-UNTESTED        (earned: the door was never opened)
```

Not earned: `-ORIENTATION-FIBER-INERT`, `-CHI-MEASURABLE`,
`-SUPPORT-SELECTED`, `-NOT-SELECTED`, and no positive
state-induced-orientation coordinate.

## 5. Corrected successor map

The state/root door remains genuinely open, and is **distinct** from
three other routes it must not be conflated with:

| route | status |
|---|---|
| change Γ_D's primitives | new physical postulate; separate door |
| change what a history is | new physical postulate; separate door |
| retune the accepted conditional (H-dependent terms) | forbidden by exogeneity (Paper 17 note §3) |
| **latent state-space extension below the joint law** | **OPEN — the genuine next gate** |

Formally: an extension probability space $\widetilde{\mathsf{Cpx}}$
with projection

$$p:\widetilde{\mathsf{Cpx}}\to\mathsf{Cpx},\qquad
(p,\mathrm{id})_*\widetilde\Gamma=\Pi(d\chi)\,\Gamma_D(dH\mid\chi),$$

which preserves every accepted old prediction while carrying an
additional covariant state variable on which orientation may live.
Such extensions exist in abundance mathematically; nothing above bars
them. The genuine next gate asks whether a candidate extension's state
variable is (i) physically selected under declared rules, (ii)
realizes the dependency relation, and (iii) has an operational readout
— each a theorem/no-go of its own.

**Admissibility wall (binding):** containing an order does not make an
extension physical. Label-based orientations, idle variables that
never interact, post-hoc constructions chosen after seeing outputs,
and dimension-selected orientations are rejected in advance. Any
future pin must encode these rejections as controls before
construction.

One-strike rule: not triggered (user-ordered correction; no new
candidate). No automatic successor; Unit D and every route above need
explicit user authorization and a fresh freeze.
