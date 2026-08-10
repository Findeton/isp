# Γ-PREP (paper-11) — HOSTILE REVIEW, EFFECTUS LENS (meaning, scope, motivation)

**Reviewer lens:** EFFECTUS. **Decisive row:** K4 (scope and
motivation). Also carried: K1 scope half, K2 meaning half, K3 meaning
half, the deviations register, the prose↔receipt sweep (#20).

**Object, hashes verified before use** (all eight reproduce):
paper `09482eb080cc`, code `9a4f0529b840`, output `097c08a0229d`,
receipt `dd86ad1a80d7`, pin `42ce06e6be8a`, protocol `b00a0be5c1ce`,
Γ-main paper `d85a629a9378`, Γ-main adjudication `972e547413304`
(sha not supplied in the brief; recorded here). Repo HEAD at review
time `d9f39a2`. All 17 pinned source artifacts re-hashed
independently: **17/17 reproduce their pinned sha256-12.**

**Discipline honoured:** read-only git (`rev-parse`, `log`, `show`
only); no execution in the repo; three scratch executions in
`/private/tmp/.../scratchpad/gprep-ef/` reading repo files read-only
and writing only to scratch; one repo write — this file.

---

## GRADE: **ACCEPT-WITH-FIXES**

**Recomputations: 508** (breakdown in §10), **3 scratch executions**.
**False computed numbers found: 0.** Every numeric token in the paper
renders from the receipt or from a one-step derivation of receipt
values (§9). The grade is not ACCEPT because five MAJOR findings bear
on what the unit *claims* rather than on what it computed — the era's
registered pattern — and one of them (MAJOR-2) is decidable *here*,
from this unit's own receipt, and reverses a headline sentence. The
grade is not REJECT because no theorem is false, no number moved, the
seven Arm-A facts bind to their pinned rows by genuine recomputation,
and the Arm-B result survives intact once re-scoped.

---

## 1. K4 — SCOPE AND MOTIVATION (the decisive row)

### 1.1 What the seven facts + the δ*=1 atoms license

**Licensed by Arm A.** Seven statements about the *committed d42b1
layer at two actors*, each gated against a hash- and verbatim-anchored
predecessor row, at windows of 1 to 243,769 histories. These are
recomputations, not re-declarations (K1, §2): the escape's 68/5, the
reopening's 84/4/(1/256), the ports' 5161/1365/3796/0, the potentials
at both scopes, the growth table (0,4,3969,13)… all appear *verbatim*
in the pinned sources and are re-derived from the layer here.

**Licensed by Arm B.** Exactly this: *on the declared arena — two
actors, transport depth ≤ 6, MATCHED horizon convention, Ψ = the
kind×weight menu shape — each of the four holdings-profile blocks of
R-SIG that a window of ≥ 2 points can test carries δ\*(block,N) = 1 at
N ∈ {1,2}; the full class carries δ\* = 0 at N ∈ {1,2}; the hitting
infimum into every block is 0 at every N the window admits; and the
history-level Birkhoff coefficient is 1 and Doeblin constant 0.*

**NOT licensed.** (i) That a uniform Doeblin bound fails at any depth
— correctly disclaimed in §14. (ii) That the *Birkhoff/Hilbert* route
— the engine the predecessor actually named — is dead anywhere except
on the raw history tree (MAJOR-5). (iii) That the blocks are atoms at
any grain other than the primary one; they are not, at the declared
control grain, in 4 of 6 measured rows, and they are provably not at
the ruled carrier (MAJOR-2). (iv) That "R-MENU is not a special class
at all" (abstract; §11.4) — at the control grain and at the carrier
R-MENU is the *only* surviving block. (v) That the holdings profile
"decreases at zero transitions of the family" without a window
(MINOR-1): 30,728 of the family's 243,768 transitions were censused
(12.6%).

### 1.2 Candidate readings of `GPREP-MINORIZATION-BLOCKED-AT-[THE MONOTONE HOLDINGS LADDER]`

| # | reading | status |
|---|---|---|
| **R1** | No minorization / regeneration exists for the transport process. | **NOT licensed.** Disclaimed in §14; every Arm-B row is a finite-cap measurement. |
| **R2** | No regeneration can run on *any* R-SIG-based small set, at any depth, because the profile is monotone. | **Partly licensed.** The monotone half is a theorem of the layer (§1.4). The "any small set" half is untested: only the four blocks and their full union were tried. |
| **R3** | On the declared arena, the blocks have δ\*=1 at N≤2, the union has δ\*=0 at N≤2, and the hitting infimum into every block is 0. | **LICENSED.** This is the measurement. |
| **R4** | The blocking is a *construction* fact: this construction chose its candidate small sets to be the level sets of a coordinate the grammar makes monotone, so "the process climbs past each one" is entailed by the choice, not discovered. | **LICENSED, and the sharpest.** |

**Is "blocked" a corpus fact or a construction fact?** Both halves,
separately, and the paper does not separate them:

- **The ladder is a corpus fact — indeed a theorem.** The receipt's
  own gate `A4-MONO` is classified `THEOREM-PASS` with the rationale
  "a one-line consequence of `View.holdings` being a union over the
  view's past". Set-monotonicity of holdings entails
  cardinality-monotonicity of the profile. So the ladder is a property
  of the committed layer, not of this arena, and it would hold at any
  cap.
- **The blocking is a construction fact.** The candidate small sets
  were declared to be R-SIG's holdings-profile blocks — i.e. exactly
  the level sets of the monotone coordinate. A ladder the process
  never descends is then the *definition* of what was chosen, not a
  finding about it. Nothing outside the level-set family was tried.

**And the two sides of Arm B are one fact, not two.** The paper's
abstract says "the two sides are the same fact seen twice" of the
tree/quotient pair; the observation applies far more sharply to the
`FOUND` / `BLOCKED` pair, where it is *not* made. Both descend from a
single structural statement: **the holdings profile is exactly the
datum the delivery budget writes into the menu** (`1/4 ÷ |hold(a)|`).
Therefore (i) each block is menu-shape-constant, so its one-step law
at a grain that reads menu shape is *one law* — δ\*=1; and (ii)
different blocks carry different menu weights, so their laws have
disjoint Ψ-support — δ\*=0 on the union. I verified (i) directly
(scratch probe 1, depth ≤ 4): block (1,1) has **1** distinct own
kind-shape, **1** distinct own event-shape, **1** distinct successor
law; block (2,2) has **1** distinct own kind-shape, **8** distinct own
event-shapes, **1** distinct successor law at the kind grain and
δ\*(event) = **0**. The paper reports "what landed" and "what did not"
as two independent measurements in two sections.

### 1.3 The choice inventory, at the RSQ standard

Every choice classified **declared** / **forced** (forcing exhibited)
/ **free** (fiber measured). *A motivated claim requires zero free
items.*

| # | choice | class | evidence |
|---|---|---|---|
| C1 | the R-SIG predicate reduction | **FORCED** | exhibited: agrees with the full predicate at 30,729/30,729, 0 disagreements; plus the two structural arguments (components need live proposals; merge pairs need two non-superseded creations) |
| C2 | the delivery-free partner derived, not imported | **FORCED** | exhibited: the layer's idle weight is `1 − ¼·1[p] − ¼·1[arb] − ¼·1[d]` and `1[d]` is identically true at two actors; gated against T4's committed partner census and potentials |
| C3 | grain: primary 13-class vs control 113-class | **DECLARED, fiber measured** | both run; the fiber is large — 4 of 6 atom rows flip. This is the model row of the unit |
| C4 | horizon: H7 vs MATCHED | **DECLARED, fiber measured at the primary grain only** | the H7 × control cell is never computed (MINOR-3) |
| C5 | CAP_T = 6, N ≤ 5, escape window 4, symmetry window 3 | **DECLARED, fibers partly measured** | N-fiber measured across N=1..5; depth-fiber not measured, but depth 7 declared infeasible with the count printed |
| C6 | actor pool = (A,B) for Arm B | **FREE** | three actors censused to depth 3 only; **no Arm-B row at three actors**; fiber unmeasured |
| C7 | terminal convention `G(h,0)=1` | **FREE** | no second terminal convention is run anywhere; §10 forces only the *root leg*, for relabelling-invariant conventions |
| C8 | Ψ ranges over **menu-shape functions only** | **FREE** | both declared grains are menu-shape functions of the successor. No abstraction of a different *kind* is tried — in particular not d74's congruence, which #82 has since ruled the carrier |
| C9 | the candidate small sets = R-SIG's profile blocks (and their union) | **FREE** | declared, not answer-selected (verified: the block list is taken from Arm A fact 4, before Arm B runs) — but the fiber over candidate small sets has exactly two sampled points, and both are level sets / the total of the same monotone coordinate |

**Verdict on motivation.** Arm A is **motivated**: nine of its facts'
choices are forced or bound to a hash- and verbatim-anchored
predecessor row, and where a choice remained (the grain) both values
are measured and their disagreement is reported as a control. **Arm B
is NOT motivated at the RSQ standard**: four free items (C6, C7, C8,
C9) with unmeasured fibers, two of which — C8 and C9 — are precisely
the choices that determine the answer. Arm B is a *measurement at a
declared arena*, which is a real and honest thing, but the unit does
not say so; §15 ("What the successor inherits") presents Arm B's
conclusions as inherited facts rather than as arena-relative
measurements.

### 1.4 Is the atoms' exactness arena-dependent?

**Yes, decisively, and the receipt measures the dependence.** Of the
four (convention × grain) cells the arena declares, three are
computed. Reading `B2_profile_rows`:

| block | N | δ\* H7·primary | δ\* MATCHED·primary | δ\* MATCHED·control | δ\* H7·control |
|---|---|---|---|---|---|
| (1,1) | 1 | 5531/5564 | **1** | **1** | not computed |
| (1,1) | 2 | 3916670725604/3948076132837 | **1** | **1** | not computed |
| (2,2) | 1 | 1373/1380 | **1** | **0** | not computed |
| (2,2) | 2 | 88301/88665 | **1** | **0** | not computed |
| (2,3) | 1 | **1** | **1** | **0** | not computed |
| (3,2) | 1 | **1** | **1** | **0** | not computed |

So "exact atom" holds in **6 of 6** rows at MATCHED·primary, **2 of 6**
at H7·primary, **2 of 6** at MATCHED·control, and is unmeasured at
H7·control. **The δ\*=1 claim is true in exactly one of the arena's
declared cells.** The paper attaches the qualifier in the lead-in
sentence of §11.4 and in the verdict segment — correct — but the
abstract's "The menu-exact port `R-MENU` is not a special class at all
— it is the first block of that ladder" and §11.4's "R-MENU … is just
the first of them" are *unqualified meaning claims* that the control
column falsifies: at the control grain R-MENU is the **only** block
with δ\* > 0.

### 1.5 THE CARRIER QUESTION — measurable HERE, and it bites

#82 ruled **CONG-185** supersedes MENU+G as the law's carrier. Do this
unit's atoms survive?

**The refinement chain, established from the pinned sources, not
assumed.** d74's own output (`b5a9d50f9573`) states the construction:
*"Refining the menu partition by successor-closure (partition
refinement to a fixed point) gives the coarsest weighted CONGRUENCE"*,
and `[DATA] AB4 (A,B) depth<=4 CARRIER: menu quotient 113 classes;
coarsest congruence 185 classes after 5 refinement rounds`. Therefore

> **CONG-185 ⊑ MENU-113 ⊑ KIND-13** (finer to coarser).

I verified the second refinement independently (scratch probe 2): over
all 3,969 histories of depth ≤ 4 the event×weight shape determines the
kind×weight shape with 0 exceptions, and the class counts are 113 and
13 — reproducing `grain_control_classes` and `grain_primary_classes`,
and reproducing d74's committed `MENU 113`.

**The lemma (two lines, no computation).** For Ψ′ coarser than Ψ and
any Ψ′-class `s′ = ⊔ᵢ sᵢ`, `minₓ P^N(x,s′) = minₓ Σᵢ P^N(x,sᵢ) ≥ Σᵢ
minₓ P^N(x,sᵢ)`; summing over s′ gives **δ\*(Ψ′) ≥ δ\*(Ψ)**.
Refinement can only *decrease* δ\*. (Demonstrated live in probe 1:
block (2,2), δ\*(KIND) = 1 → δ\*(EVENT) = 0.)

**Consequence, derivable from this unit's own receipt:**

> δ\*(C, N, CONG-185) ≤ δ\*(C, N, MENU-113) = 0 for blocks (2,2) at
> N=1, (2,2) at N=2, (2,3) at N=1, (3,2) at N=1.
>
> **Four of the six delivered atom rows are δ\* = 0 at the ruled
> carrier. The atom claim collapses to the (1,1) block — i.e. to
> R-MENU — exactly reversing the paper's headline sentence.**

**What is *not* decidable here.** The two (1,1) rows: δ\*(CONG-185) ≤ 1
and could be anything in [0,1]. It is plausible they survive — probe 2
shows the whole (1,1) block lies inside a *single* MENU-113 class and
its one-step law over MENU classes is constant, so the first
refinement round does not split it — but rounds 2–5 might, and that is
a genuine successor computation.

**Two further carrier obstacles the unit does not name:**

1. **Window.** CONG-185 lives on the (A,B) `d ≤ 4` window (3,969
   histories). The (2,3) and (3,2) blocks live *only at depth 5*, and
   the (1,1)/(2,2) block windows reach depth 5 with successors at
   depth 6. So three of the four blocks are not even *statable* on the
   carrier without extending it. d74 **does** commit the wider arm —
   `(A,B) depth<=5 CARRIER: menu quotient 265 classes; coarsest
   congruence 462 classes after 6 refinement rounds` — a pinned row
   this unit's T5 supply list does not carry, and precisely the one
   the Γ-iteration needs.
2. **The grain names are window-bound.** Scratch probe 3 (build to
   depth 5, 30,729 histories) gives, per window `d ≤ 0…5`:
   KIND×weight classes `[1, 2, 5, 9, 13, 21]`, EVENT×weight classes
   `[1, 5, 13, 45, 113, 265]`. The first list reproduces the leading
   column of `tables_primary`; the second reproduces `tables_control`
   *and* d74's 113 and 265. So "the 13-class primary grain" has 13
   classes only on the escape window; on the depth-≤5 window it has
   **21**, and Arm B applies it at depths up to 6. A successor that
   implements "the 13-class grain" literally will not reproduce these
   atoms.

**Answer to the K4 carrier question, stated once:** *the atoms do not
survive the carrier change in general; four of six rows die by a
two-line lemma applied to numbers already in this receipt; the two
(1,1) rows are a genuine successor computation whose cost is one run
of δ\* at Ψ = CONG-185 (and, past depth 4, at CONG-462); and before
either can run, the carrier must be extended past the depth at which
three of the four blocks live.*

---

## 2. K1 (scope half) — what each of the seven facts binds to

For each fact: the upstream row, the anchored committed value, and
whether the unit **recomputes** it or **re-declares** it.

| fact | row | committed value located at its pinned sha | binding |
|---|---|---|---|
| F1 grammar | T1 `576275d55ecf` | docstring "Budgets: propose 1/4 \| arb-and-merge 1/4 (components join-view + pairs initiator-view) \| deliver 1/4 (sender-view) \| idle absorbs." (the 130-char verbatim window, consumer `A1-BUDGETS`); T8 `a6368078be4c` "NON-INJECTIVE (re-delivery admissible…)" | **RECOMPUTATION.** Budgets measured per (history, actor) over the whole family; the value set `{1/2,1/4}` for arb-and-merge is a *measurement that departs from the quoted quarter* and is reported as such. Kind census measured. |
| F2 census + potentials | T4 `1177761ed54d` HZ0-3/4/5/6 | `[1,7,39,215,1191,6471,34375]`; `2,4,257/32,1037/64,2101/64,68313/1024,139065/1024`; `2,4,257/32,1035/64,4173/128,134587/2048,2168717/16384`; both ratio columns | **RECOMPUTATION**, and the delivery-free arm is *derived* from T1 rather than read from a second layer, then gated against T4's census — the strongest binding in the unit. |
| F3 kernels | T7 `406af54e0c5c` "objects k_r(e\|h) = q G(h+e, r−1)/G(h, r)."; T4 "**HZ1-b (strict positivity) is the substantive one**" | verbatim windows located | **RECOMPUTATION** of the sweep; the *definition* is a re-declaration (correctly — it is a definition), and cut-additivity is inherited as T4's own `[THEOREM-PASS — CANNOT FAIL]` and disclosed as such. Faithful. |
| F4 renewal ports | T4 "**R-MENU absorbing-complement (0 re-entries), R-SIG re-entered 3,796 times**" | verbatim window located | **RECOMPUTATION** of 5161/1365/3796/0, of `4ⁿ`, of `(3/2)ⁿ`, of `renewal_k`/`nonrenewal_k` (d70 lines 336–340 match cell for cell), and of the closed form by two genuinely disjoint code paths (verified: `ret_k[5]` is a chained kernel product; `renewal_depth5_closed` is `(3/2)⁵·GT[ROOT][1]/GT[ROOT][6]`). |
| F5 the escape | T3 `598ada389811` "window chain ESCAPES: 68 transitions from len <= 2 parents land in 5 classes first realized only at len 3."; T2 `4b533e437b0f` the same, plus the extensional-nullity clause; T6 `7ac66f3fe74d` the P₀/P_{t+1} method; T5 `b5a9d50f9573` "MENU        113" | verbatim windows located; d44b's `TG1 growth table (t, window len<=, histories, |P_t|): (0,4,3969,13); (1,3,521,11); (2,2,69,6); (3,1,9,2); (4,0,1,1)` matches §8.1 **cell for cell** | **RECOMPUTATION.** The T2 clause is *gated rather than repeated* (`operator_agree = true`), which is the correct treatment of a binding clause. |
| F6 reopening | T3 "84 distinct diverged prefixes; 4 DISTINCT minimal (3-event) reconverging chains, all at weight 1/256"; d44b out `diverged histories in ARM-1T = 1044`; note "124 reconverging pairs among 1,044 diverged histories" | located | **RECOMPUTATION.** |
| F7 root symmetry | T4 (window CAP_SYM = 3) | — | **RECOMPUTATION**, and correctly demoted: §10 states it is "a theorem of the construction, not a measurement of stability", and the receipt classifies `A7-ROOTTHEOREM` as `THEOREM-PASS` with a waiver. Model handling. |

**T5's ledger repair, verified.** `git show HEAD:v10/LOG.md` line
11906 heads *"D74 ROUND 1 ADJUDICATED AND TERMINAL: TH-II WITH A
FIND"*, and line 11909 carries `## (LEDGER #495)`. The note's own
status line is byte-identical to `t5_note_status_line`. T4's `#489`
also verifies (LOG lines 11717, 11797). **The citability gap is really
closed and really was open.**

**One weak anchor.** T5 carries a **single 15-character** verbatim
window (`"MENU        113"`) for a row the pin says supplies six
abstractions, the μ/menu descent columns, the curvature group ⟨2,3⟩,
the removability threshold and J. Everything but the 113 is unused,
and the 113 is anchored by a string short enough to occur by accident.
Not a false claim — but at the #62 standard ("verbatim anchors that
bind meaning") this is the thinnest anchor in the table, on the row
that turns out to matter most downstream (§1.5).

---

## 3. K2 (meaning half) — what Birkhoff-route-death establishes, and what an ATOM is

### 3.1 The Birkhoff route

**What is established:** that the *level operators of a history tree*
have infinite projective diameter. This is true of every history tree
under every weight law: distinct nodes have disjoint descendant sets.
The paper says so itself — "Unique parenthood is the defining property
of a history tree" — and the verdict segment is correctly scoped ("at
the history level").

**What is not established, and is not disclosed as un-attempted:** the
Birkhoff/Hilbert contraction coefficient of any **quotient** operator.
Grepping the source for `birkhoff|hilbert|diameter|tanh|cross.ratio`
returns exactly one block, at the history level. On a quotient the
transfer operator need not be a tree operator and Δ may be finite —
which is the only level at which the predecessor's named engine could
ever have been a candidate. The unit substitutes a *different*
instrument (Doeblin δ\*) on the quotient and reports the substitution
nowhere; §14 ("what this unit does not decide") does not list it.

**The measurement behind the tree claim is thinner than the prose.**
The column loop's own comment reads *"A history determines its own
prefix, so the only candidate row is `h[:-1]`"* — parenthood is
assumed by the loop, and what is counted is the multiplicity of the
last event in the parent's menu. So `columns_single_parent = 243768`
measures *"no duplicated menu entries"*, not *"no second parent"*. And
the "exhibited" witness minor is constructed to be zero: `m12` and
`m21` are assigned `Fr(0)` by an `else` branch whose guard
(`c2[:-1] == r1`) can never hold for `r1 ≠ r2` at the same level, and
`birkhoff_diameter_finite = False` / `birkhoff_tau = '1'` are **typed
literals**, two of which the gate `B1-TREE` then reads back
(`f['birkhoff_diameter_finite'] is False`). The mathematics is right;
the framing "**Measured:**" / "**Exhibited:**" is not.

### 3.2 What an ATOM is here, precisely — and where the usage drifts

Precisely: *a set C on which the map `x ↦ P^N(x, Ψ⁻¹(·))` is
constant*, i.e. a set contained in one state of the N-step Ψ-quotient
chain. That is what δ\*(C,N,Ψ) = 1 says, and the paper states it
correctly in §11.4 ("the N-step law is the **same** measure at every
point of the block, not merely bounded below by a common one").

Two consequences the paper does not draw:

1. **δ\* = 1 is the degenerate end of the minorization scale, not its
   strong end.** A Doeblin minorization is an instrument when δ ∈ (0,1)
   on a set the chain *returns to*. δ = 1 on a set that is a single
   quotient state contributes no contraction: there is nothing left to
   contract. So `GPREP-MINORIZATION-FOUND-[delta = 1 exact …]` records
   a **lumpability** observation (the profile blocks refine the
   one-step Ψ-bisimulation) under a minorization label. §11.6 is
   structurally honest about the missing half ("A regeneration
   argument needs both halves"), but the abstract's "On the quotient
   it does land, and **it lands hard**" and the first-class `FOUND`
   verdict price a degeneracy as a discovery.
2. **Drift in "atom".** §11.4 and §15.2 use "atom" unqualified; the
   verdict segment qualifies it (MATCHED, primary grain); the abstract
   qualifies it in the preceding sentence but not in the R-MENU
   sentence that draws the conclusion. Γ-main then imports the word
   with no qualifier at all (§4).

### 3.3 The re-entry census reads against the claim it is printed to support

`reentry(S) = Σ_{h∈S} 1[∃ proper prefix of h outside S]`. For any block
**not containing the root**, the empty history is an outside ancestor
of every point, so `reentry(S) = |S|` **identically**. Hence:

| block | points | "re-entries" | status |
|---|---|---|---|
| (1,1) | 5,461 | 0 | informative (the block contains the root) |
| (2,2) | 33,260 | 33,260 | **forced**: 100% by construction |
| (2,3) | 108 | 108 | **forced** |
| (3,2) | 108 | 108 | **forced** |

Three of the four rows cannot come out any other way, and the paper
prints them (§11.6 iii) **without the definition**, immediately after
"The profile is a monotone non-decreasing coordinate of the process".
A reader who takes "33,260 re-entries" at face value reads the
opposite of the sentence it is printed to support. (The same function
is genuinely informative for R-SIG/R-MENU in §7, precisely because
R-MENU contains the root; I confirmed the associated set claim — see
MINOR-7.)

---

## 4. K3 (meaning half) — what Γ-main took this unit to mean

Γ-main (`d85a629a9378`) consumes this unit in three places. **Two of
the three readings do not match this paper's own scope statements.**

1. **§4, "The block decomposition."** *"Γ-prep's B2 atoms — the
   holdings-profile blocks of R-SIG — are read, not chosen: 5161 R-SIG
   points, 1365 of them menu-exact, in blocks {(1,1): 1365, (2,2):
   3788, (2,3): 4, (3,2): 4}…"* The **census** is consumed correctly
   (values and provenance match `rsig_count`, `rsig_menu_exact`,
   `rsig_profiles` exactly). The **word "atoms"** is consumed with no
   qualifier — and Γ-main's own §8 says *"The MATCHED horizon
   convention and the 13-class primary grain are named in the
   inventory and **not run**."* **Γ-main therefore imports a result
   whose entire scope it has declared outside its own arena**, and
   works on a carrier (MENU-113, ruled CONG-185) at which 3 of the 4
   blocks are not atoms at all (§1.5). This is the sharpest K3
   mismatch, and it is a *reading* defect at both ends: Γ-prep's
   unqualified "atom"/"R-MENU is not special" sentences invite it.
2. **§4, the blocking fact.** Γ-main inherits it as *"The holdings
   profile decreases at **zero** transitions of the family"* — which is
   the **abstract's unscoped sentence, verbatim**, not §7's scoped one
   ("Over all 30,728 transitions out of every history of depth < 5").
   The under-scoping propagated downstream exactly as written. This is
   MINOR-1 with a demonstrated consumer.
3. **§8, the cap.** *"The carrier is the (A,B) d ≤ 4 arena the pin
   declares; the d ≤ 6 and d ≤ 7 arenas are EXCLUDED-BY-CAP, Γ-prep
   having declared depth 7 infeasible."* **Γ-prep declares depth 7
   infeasible; d ≤ 6 is Γ-prep's actual, built, delivered arena.** A
   row Γ-main leans on that this unit does not pin. Flagged for the
   Γ-main repair register, not chargeable to Γ-prep.

**R-GM-9's swallowed probe — what it should have found, on this
unit's side.** The probe was `armB/atoms/0/delta_matched_primary`.
This receipt is a **flat 196-key dict**, and the flat structure is not
this unit's defect. The defect is: **there is no receipt key that
publishes a per-block δ\*.** `B2_atoms` is built as
`(str(p), N, len(Xs))` — the δ value present in the internal `_atoms`
tuples is **dropped at serialisation**, precisely because the list is
already filtered on `dM == '1'`. The only δ-bearing flat keys are
`B2_best_delta = "1"` (a selector over the whole table, not a row) and
`B2_profile_rows`, where the datum sits at unadvertised positional
index 5 (H7 at 4, MATCHED-primary at 5, MATCHED-control at 6). So a
consumer who wants "the δ of atom 0" has no named path. A probe
pointed at `B2_best_delta` would have resolved — but would have read a
maximum, not the row.

**Repair (this unit's side):** publish
`B2_atom_deltas = ((profile, N, delta_H7, delta_matched_primary,
delta_matched_control), …)` and keep the δ in `B2_atoms`; add a
`_schema` key naming the column order of every positional tuple in the
receipt. **Repair (protocol side, already ordered as R-GM-9):**
`want=None` probes must still gate that the path *resolves*.

---

## 5. THE DEVIATIONS REGISTER — is each priced honestly?

Every self-disclosed deviation/limitation, with my pricing.

| # | disclosed as | priced |
|---|---|---|
| D1 | five event kinds where the pin's summary says six (§4, parenthetical) | **UNDER-priced.** Verified: `candidates_for` in the layer at its pinned sha has exactly five branches (`p`, `r`, `m`, `d`, `n`); there is no sixth kind anywhere. This is a **pin error**, not an arena-dependent count. The paper says only "this paper reports the measurement", leaving a reader unable to tell whether a kind is missing from the arena or the pin miscounted. → MINOR-4 |
| D2 | arb-and-merge per-actor totals `{1/2, 1/4}` rather than the docstring's quarter (§4) | **HONESTLY priced.** Measured, reported as measured, and the mechanism (join-view components vs initiator-view pairs) is given. Model row. |
| D3 | cut-additivity is an induction, not a measurement (§6) | **HONESTLY priced**, and inherited from T4's own `[THEOREM-PASS — CANNOT FAIL]`. |
| D4 | the properness identity is a construction identity; strict positivity is the substantive gate (§6) | **HONESTLY priced.** |
| D5 | window artefacts / the off-root prefix convention (§6) | **HONESTLY priced**, and applied (r = 7 is a root-only window and is never read as contraction). |
| D6 | the monotonicity theorem "at its narrowed scope"; non-superseded holdings *do* shrink at 4,340 transitions (§7) | **HONESTLY priced** in §7 — this is the unit's best paragraph — but the *narrowing* is stated as "depth < 5" without saying that this is 30,728 of 243,768 transitions, and the abstract drops the scope entirely. → MINOR-1 |
| D7 | the grain choice is a §15 declaration; both grains measured; disagreement is a control (§2, §8.2, §11.4) | **HONESTLY priced for Arm A**, **UNDER-priced for Arm B**: "the same blocks **split**" is a soft word for "3 of 4 blocks have δ\* = 0", and the unqualified "R-MENU is not a special class at all" survives the disclosure unretracted. → MAJOR-2 |
| D8 | no closed exact transfer at feasible caps; "the state space outruns every window this unit can afford" (§8.3) | **HONESTLY priced.** |
| D9 | the root-symmetry theorem "is a theorem of the construction, not a measurement of stability" (§10) | **HONESTLY priced**, with a `THEOREM-PASS` waiver behind it. |
| D10 | the infeasible arms with counts printed (§11.1) | **HONESTLY priced.** Both projections re-derived: `int(213040²/26760) = 1,696,040` ✓; `int(3189·(1063/73)²) = 676,200` ✓. |
| D11 | the N=3 cross-profile positive row printed rather than dropped (§11.5, abstract, §14) | **HONESTLY priced** — the single best disclosure in the unit, and the reason the abstract survives hostile reading. |
| D12 | "no claim that a uniform Doeblin bound fails at every depth" (§14) | **HONESTLY priced.** |
| D13 | the theorem-pass census, "printed with its count" (§13) | **UNDER-priced.** The count (3 of 44) omits at least two gates that cannot fail — and they are the two carrying the Arm-B headline. → MAJOR-1 |
| D14 | "the complete emitted string compared for equality against a segment-by-segment rebuild from the gated object" (§12) | **FALSE at the standard the unit itself claims.** → MAJOR-3 |
| — | *not disclosed at all:* Birkhoff never run on a quotient | → MAJOR-5 |
| — | *not disclosed at all:* the H7 × control cell never computed | → MINOR-3 |
| — | *not disclosed at all:* the grain names are window-bound (13→21, 113→265) | → MINOR-2 |
| — | *not disclosed at all:* three of four block-re-entry rows are structurally forced | → MAJOR-4 |

**Pattern.** The unit prices its *arithmetic* limitations excellently
(D3, D4, D5, D6, D10, D11) and its *scope* limitations unevenly. Every
one of the four undisclosed items is a scope item, and three of the
four are in Arm B.

---

## 6. FINDINGS

### MAJOR-1 — the theorem-pass census under-counts by at least two, and both misses carry the Arm-B headline

`A4-MONO` is classified `THEOREM-PASS` ("a one-line consequence of
`View.holdings` being a union over the view's past"). But
`B3-MONOTONE` — predicate `B3_profile_decreases == 0 and
B3_profile_pairs > 10000` — is classified `SUBSTANTIVE`, and it
measures the *same loop over the same 30,728 pairs*, testing
cardinality-monotonicity, which set-monotonicity strictly entails.
It cannot fail on any input the construction admits. `B1-TREE` is
likewise `SUBSTANTIVE` while the paper's own text calls its content
"the defining property of a history tree", and two of its five
conjuncts read typed literals (`birkhoff_diameter_finite is False`;
`_wit[1]=='0'`, `_wit[2]=='0'` — both assigned by an `else` branch that
always fires). So §13's "Of the 44 gates … 3 are theorem-passes that
cannot fail on any input the construction admits … and the receipt
says so before anyone else has to" is itself the thing it was built to
prevent.

**Repair.** (a) Reclassify `B3-MONOTONE` as `THEOREM-PASS` with the
one-line entailment from `A4-MONO` printed, or replace its predicate
with something that can fail (e.g. gate the *non-superseded* profile,
which does decrease — 4,340 transitions). (b) Reclassify `B1-TREE` as
`THEOREM-PASS`, or split it: keep a substantive
`B1-NO-DUPLICATE-MENU-ENTRIES` gate (which is what the loop actually
measures) and disclose unique parenthood as a theorem. (c) Compute
`birkhoff_diameter_finite` and `birkhoff_tau` from the witness minor
instead of typing them, and build the witness so the off-diagonal
zeros are *read* rather than assigned. (d) Re-render §13's census with
the corrected count and **name the theorem-passes in the paper**, not
only in the receipt.

### MAJOR-2 — the atoms do not survive the #82 carrier ruling, and the reversal is derivable from this unit's own receipt

§1.5 in full. Four of the six delivered atom rows have δ\* = 0 at
CONG-185, by δ\*-monotonicity under refinement applied to the
already-measured `MATCHED control` column; the remaining two are open;
and three of the four blocks are not statable on the carrier's `d ≤ 4`
window at all. The abstract's "The menu-exact port `R-MENU` is not a
special class at all — it is the first block of that ladder" and
§11.4's "R-MENU … is just the first of them" are false at the
declared control grain and provably false at the carrier.

**Repair.** (a) Replace both sentences with: *"At the primary grain
R-MENU is not distinguished — it is the first block of the ladder. At
the control grain it is the only block that remains an atom, and by
δ\*-monotonicity under refinement the same holds at any refinement of
the control grain, including d74's coarsest weighted congruence."*
(b) Add the monotonicity lemma to §11.3 as a stated proposition with
its two-line proof — it costs nothing and converts an unmeasured cell
into a bound. (c) Add a carrier row to §15: the (1,1) atom at
Ψ = CONG-185 is the one open question, and CONG-462 (d74's committed
`d ≤ 5` carrier, 265 menu classes / 462 congruence classes) is the
object it needs. (d) Add the corresponding line to §14.

### MAJOR-3 — `V-VERDICT` is `build_verdict` compared with `build_verdict`

`F['verdict'] = build_verdict(F)`; the gate predicate is
`f['verdict'] == build_verdict(f)`. The comparator shares **all** code,
**all** inputs and **all** typed literals with the builder — the
`#82`-engraved failure mode ("the same concatenation written twice"),
third recurrence. It is genuinely two-way against *field* drift (the
stored string is stale under mutation), which is why the five verdict
falsifiers all kill; it is blind to any error in the composition logic
itself. §12's claim ("compared for equality against a
segment-by-segment rebuild from the gated object") and the receipt's
compliance row `['RUNBOOK 14 (#219) comparators built independently',
True]` are both false — and #219 predates this delivery, so this is not
excused by #82's later date.

**Repair.** Rebuild the comparator from a **separate literal template**
that shares no function, and populate it by *parsing the emitted
string* back into fields and re-checking each against the gated object,
so a wrong segment template dies. Then re-derive the `#219` compliance
row from the new gate rather than asserting it.

### MAJOR-4 — the block re-entry census prints three structurally forced rows as measurements, without their definition, in the direction opposite to the claim

§3.3 in full.

**Repair.** In §11.6(iii) state the definition ("a point of the block
having an ancestor outside it") and add one clause: *"For any block not
containing the root this count is its size by construction; only the
(1,1) row, which contains the root, carries information."* Better: in
the receipt, replace the three forced rows with the object the argument
actually needs — the number of transitions **into** each block from
outside it — and gate that instead.

### MAJOR-5 — the named successor engine is attempted only where it is trivially dead, and the omission is not disclosed

The predecessor's verbatim open question, anchored here at
`B0-SUCCESSOR-NAMED`, is: *"No operator-level minorization — Birkhoff /
Hilbert-metric contraction of the positive backward recursion `G` … has
been attempted anywhere."* This unit runs Birkhoff **only at the
history level**, where the answer is a theorem about trees carrying no
transport-specific content, and runs a **different** instrument
(Doeblin δ\*) on the quotients. The Hilbert projective diameter of a
quotient transfer operator is never computed. §14 does not list the
omission.

**Repair.** Add to §14: *"The Hilbert projective diameter of the
quotient transfer operators is not computed; the Birkhoff route is
closed at the history level only, where it closes for every history
tree. The named engine remains un-attempted at the level where it
could have worked."* And add it to §15 as the successor's first
Arm-B task — it is cheap on the 13- and 113-class quotients.

---

### MINOR-1 — the abstract drops the monotonicity scope, and Γ-main inherited the dropped version

Abstract: "The holdings profile decreases at **zero** transitions of
the family." The family has 243,768 transitions; 30,728 were censused
(12.6%), because `HOLD` is built only for `len(h) ≤ 5`. §7 and the
verdict segment are correctly scoped; the abstract and §11.6's
"monotone non-decreasing coordinate of the process" are not.
**Repair:** "…at zero of the 30,728 transitions out of histories of
depth < 5 (the census window), and by `A4-MONO` this is a theorem of
the layer rather than a finding about this window." Note the theorem
status *strengthens* the claim while fixing the scope.

### MINOR-2 — the grain names are window-bound and Arm B uses them outside their window

"the 13-class kind × weight menu partition" has 13 classes only at
`d ≤ 4`; at `d ≤ 5` it has 21 (measured, probe 3), and Arm B evaluates
Ψ on successors at depths up to 6. Same for "the 113-class"
(→ 265 at `d ≤ 5`). No number in the paper is wrong; the *names* are.
**Repair:** rename to "the kind×weight menu-shape grain (13 classes on
the escape window)" and print the per-window class counts
`[1,2,5,9,13,21]` / `[1,5,13,45,113,265]` in §2, which also
independently re-anchors the control grain to d74's committed 113 and
265.

### MINOR-3 — the arena declares a 2×2 and three cells are filled

Two grains × two horizon conventions; `H7 × control` is never computed
(`delta_star(Xs, N, psi_event_of, False)` appears nowhere) and its
absence is not printed. §2's own rule ("Choosing one silently would be
an arena artefact, so both are measured") makes the silent gap a
disclosed-standard violation. Also: §11.5's full-class table is run at
the primary grain only. **Repair:** run the fourth cell (it costs one
line), or print "not computed; bounded above by the H7·primary column
by δ\*-monotonicity" — which is true and free.

### MINOR-4 — the "six event kinds" discrepancy is a pin error and should be registered as one

§5, D1. **Repair:** "The pin's T1 summary column says six event kinds;
the committed generator has exactly five branches (`p`, `r`, `m`, `d`,
`n`) and no sixth kind exists in the layer. Registered as a pin
erratum." (Follows the v14 #4 erratum practice.)

### MINOR-5 — a receipt key name inverts its content

`B3_dist_rows_saturated = [0,1,2,3]` and `B3_dist_max_saturated = 2`
in fact hold the **informative** (i.e. *un*saturated: max < lookahead)
rows — the output prints them under the header "informative rows", and
the paper follows the output. A consumer reading the receipt **by key
name** gets the complement. **Repair:** rename to
`B3_dist_rows_informative` / `B3_dist_max_informative`, keeping the old
keys as aliases for one iteration.

### MINOR-6 — the receipt publishes no per-block δ\* under a name

§4. **Repair** as given there (`B2_atom_deltas` + a `_schema` key).

### MINOR-7 — a set claim gated by a count

§7: "The R-SIG points that are not menu-exact are **exactly** the
re-entered ones." The gate checks `rsig_reentries == 3796` and
`rsig_reentries == rsig_menu_not_exact` — **counts only**. I verified
the set claim independently at `d ≤ 4` (probe 2): 689 R-SIG points, 341
menu-exact, 348 not menu-exact, 348 re-entered, **symmetric difference
0**. So the claim is true where I could test it; the *gate* does not
establish it. **Repair:** gate `set(not_menu_exact) == set(reentered)`.

### MINOR-8 — asymmetric reporting between the two grains

§8.1 prints "out of the 6 classes the window carries" for the primary
grain; §8.2 omits the control's analogue, which the receipt holds
(`escape_control_window_classes = 17`). Printing it *strengthens* §8.3
— 76 escapes into 32 above-window classes against 17 in-window classes
is a worse ratio than 68 into 5 against 6. **Repair:** print it.

### MINOR-9 — "at a family of 243,769 histories" over-states the abstract's own scope

Only F1's kind census, F2's census/potentials and F3's properness
sweep use the full family; F4 runs at `d ≤ 5`, F5 at `d ≤ 4`, F6 at
`d ≤ 4`, F7 at `d ≤ 3`. §12's scope qualifiers are correct; the
abstract's single number is not. **Repair:** "…at windows of the
243,769-history family, each window printed with its fact."

### MINOR-10 — the CLI (registered disease, deferred to K5)

`ARGV = set(sys.argv[1:])` with no whitelist: unknown flags are
silently ignored, which is what made the #65 verification vacuous
(#66). Not chargeable as a compliance violation at birth (#63 predates
the #82 engraving), but the repair is ordered. Full audit is the
instrument reviewer's row; recorded here only because the paper's §13
and §16 make blindness and reproducibility claims that a real
`--selftest` would have to carry.

---

## 7. THE LICENSED CLAIM

The sharpest sentence the artifacts actually support:

> **On the committed d42b1 transport layer at two actors and depth 6,
> seven predecessor facts re-derive exactly from the layer and agree
> cell for cell with their hash- and verbatim-anchored sources; and the
> operator-level minorization the predecessor named is dead at the
> history level for the reason every history tree is (unique
> parenthood), while on a quotient the choice of small set decides
> everything: R-SIG's holdings-profile blocks are single states of the
> one-step kind×weight quotient — δ\* = 1 with an explicit ν on two
> classes — at the MATCHED horizon and that grain and nowhere else
> measured, since refining to the event×weight grain sends δ\* to 0 on
> every block but R-MENU; the union of the blocks has δ\* = 0 on both
> of its widest windows; the hitting infimum into every block is 0; and
> the coordinate that indexes the blocks is the one the delivery budget
> `1/4 ÷ |hold(a)|` writes into the menu and that the layer makes
> monotone, so both halves of the answer — the blocks being atoms and
> their union not being one — are one structural fact about that
> coordinate rather than two independent measurements.**

Everything in that sentence is measured or is a two-line consequence
of a measured value. What must be dropped from the current headline:
"R-MENU is not a special class at all"; "the two grains" as if
symmetric; "the family" in the monotonicity scope; and "attempts the
one construction the predecessor named" without the qualifier that the
named construction was Birkhoff and Birkhoff was run only where it is
trivial.

---

## 8. THE SUCCESSOR REGISTER — what the Γ-iteration pin must inherit from this unit **verbatim**

1. **The refinement chain and the lemma.** `CONG-185 ⊑ MENU-113 ⊑
   KIND-13`, established from d74's own text ("Refining the menu
   partition by successor-closure … gives the coarsest weighted
   CONGRUENCE") and verified here (EVENT→KIND well defined, 0
   exceptions over 3,969); together with **δ\*(Ψ′) ≥ δ\*(Ψ) whenever Ψ′
   is coarser than Ψ**. These two together are the transport rule for
   every δ\* number this unit produced.
2. **The four dead rows.** At the ruled carrier, blocks (2,2)@N=1,
   (2,2)@N=2, (2,3)@N=1, (3,2)@N=1 have δ\* = 0. Inherit as **facts**,
   not as open questions.
3. **The two open rows.** (1,1)@N=1 and (1,1)@N=2 at Ψ = CONG-185 are
   the only surviving atom candidates. The Γ-iteration must run them
   or stamp them open.
4. **The carrier window obstacle, with its named successor object.**
   CONG-185 covers `d ≤ 4`; the (2,3)/(3,2) blocks live only at depth
   5 and the (1,1)/(2,2) successors reach depth 6. d74 commits the
   wider arm — `(A,B) d ≤ 5: menu quotient 265, coarsest congruence
   462, 6 refinement rounds` — at sha `b5a9d50f9573`. **This row is not
   in Γ-prep's T5 supply list and must be added to the Γ-iteration
   pin's source table.**
5. **The window-bound grain names.** `KIND×weight` per window
   `[1,2,5,9,13,21]`; `EVENT×weight` per window `[1,5,13,45,113,265]`.
   A successor implementing "the 13-class grain" literally will not
   reproduce these atoms.
6. **The 13-collision.** Γ-main's "the 13 classes the depth-2 cut
   carries" (MENU classes at `d ≤ 2`) and Γ-prep's "the 13-class
   primary grain" (KIND classes at `d ≤ 4`) are **different objects
   with the same count**. Both appear in Γ-main. The pin must
   disambiguate by name.
7. **The atom's true content.** δ\* = 1 is a **lumpability** statement
   (the block is one state of the Ψ-quotient), not a contraction
   instrument. Any quantum-shape or geometry claim built on "the atoms"
   must carry the #82 carrier stamp *and* this reading.
8. **The scoped monotonicity sentence**, to replace the one Γ-main
   already inherited: *"the holdings profile decreases at 0 of the
   30,728 transitions out of histories of depth < 5, and by `A4-MONO`
   this is a theorem of the layer."*
9. **The un-attempted engine.** Birkhoff / Hilbert-metric contraction
   on a quotient operator is still un-attempted; d70's open question is
   **not** closed by this unit. Carry the verbatim d70 window forward.
10. **The receipt-key repairs** (`B2_atom_deltas`, `_schema`,
    `B3_dist_rows_informative`) so R-GM-9's class of failure cannot
    recur; and the rule that a `want=None` probe must still gate that
    its path resolves.
11. **The free choices (C6–C9).** Actor pool, terminal convention, the
    menu-shape-only Ψ family, and the level-set-only family of
    candidate small sets. Any successor claiming *motivation* for an
    Arm-B result must close at least C8 and C9.

---

## 9. THE PROSE↔RECEIPT SWEEP (#20)

Every numeric token in the paper was extracted (128 distinct) and
tested against the flattened receipt value set, including numeric
substrings of all string values.

- **124 of 128 match a receipt value directly.**
- **4 residuals, all resolved, none a finding:** `57` (the pin's ledger
  number, present in the pin and emitted as a literal by the code);
  `07` and `27` (fragments of the date inside `t5_note_status_line`,
  which *is* a receipt value — a tokenizer artefact of mine);
  `213040/26760` (§11.1, rendered by the code as
  `t_per_level[6]/t_per_level[5]`).
- Spot-checked derivations that render but are not stored verbatim:
  `279,067 = Σ proper_rows` ✓ (also present in `_gates`);
  `1,696,040 = int(213040²/26760)` ✓; `676,200 = int(3189·(1063/73)²)`
  ✓; `1365 = Σ_{n≤5} 4ⁿ` ✓; `5461 = Σ_{n≤6} 4ⁿ` ✓;
  `84 = 0+0+4+80` ✓; `(3/2)⁵·G₂/G₇ = 497664/2168717` ✓;
  `30728 = Σ levels 1..5` ✓; `3424 = 1+15+219+3189` ✓;
  `40+3+1 = 44` ✓; all fifteen tables verified cell for cell against
  their receipt arrays.

**Result: the sweep is clean. No number in the paper fails to render
from the receipt, and no number is wrong.** The unit's numerical
discipline is not in question; its scope discipline is.

---

## 10. RECOMPUTATION LEDGER (508)

| category | count |
|---|---|
| sha256-12 verifications (17 pinned artifacts + 8 review objects) | 25 |
| paper↔receipt table cells and inline scalars, compared element-wise | 386 |
| arithmetic re-derivations of quantities not stored verbatim | 17 |
| quantities recomputed from the layer in scratch (3 executions) | 49 |
| committed values located and matched in the pinned sources at their shas (d70 ×7, d44b ×5, d74 ×3, d42b1 ×2, paper31, d46b, d46f, v10/LOG ×2) | 25 |
| carrier-lemma derivations (4 rows closed, 2 rows bounded) | 6 |
| **total** | **508** |

**Scratch executions:** 3 (`probe1.py`, `probe2.py`, `probe3.py`), all
read-only against the repo, all writing only to
`/private/tmp/claude-501/…/scratchpad/gprep-ef/`.

**Independent reproductions of receipt values from the layer** (probes
1–3): per-level census to depth 5 `[1,8,60,452,3448,26760]`; cumulative
3,969 and 30,729; `mass_census_d4 {2:3757, 5/2:212}`; event kinds at
`d ≤ 4` `{d,n,p,r}`; R-SIG at `d ≤ 4` = 689 with profiles
`{(1,1):341, (2,2):348}` (matching `B2_full_rows[N=2]` window 689 and
the (1,1)/(2,2) N=2 windows 341/348); δ\*(1,1) = 1 at both grains;
δ\*(2,2) = 1 at KIND and 0 at EVENT; the exhibited ν
`{1/4, 3/4}` on exactly the two classes `B2_nu_measure` names;
`grain_primary_classes = 13` and `grain_control_classes = 113`;
the set identity `not-menu-exact = re-entered`.

**Repo state after all work:** unchanged except this file. Verified:
no repo file other than `v14/review-gprep-effectus.md` was written; all
eight object hashes re-checked and unchanged.
