# D75 — THE BARANDES AUDIT: which base principles the program states, which it followed, which it violated, and which it never operationalized

**Status: AUDIT, 2026-07-27. NOT a pin, NOT a receipt, NOT a result.**
Nothing below is new evidence about the world. Every number and every
quoted sentence is copied from a committed file (or from the two Barandes
manuscripts archived at the repository root) and attributed by path and
line. The only forward-looking objects are §8's pins, which are
suggestions for the principal to freeze, amend or discard.

**The question, as put:** *"If we come from ISP principles based on
Barandes' ideas, how do we NOT have 'quantum interference = the holonomy
of probability transport' as a BASE? And check what other ISP/Barandes
principles we're maybe not following or missing."*

**The adjudicator's hypothesis under test (stated as hypothesis):** that
v10's generated line, via its closure theorems ((H1)/(H2) = Markov on
`sigma`), built a *divisible* process — definitionally classical in
Barandes' framework — so that the 0-for-5 phase absence is a **corollary
of violating the indivisibility principle** rather than a discovery; that
the phase hunt computed holonomy on conditional (divisible) transport,
which is gradient by construction; that division events may be required
to be **sparse**; and that the phase may be **gauge** in Barandes'
dictionary, the derivable things being indivisibility and
unistochasticity, neither ever tested on the generated law.

**Provenance labels** (book §0.1 convention): `[THEOREM]` / `[EXACT]` =
argued depth-free and gated; `[MEASURED]` = true on a declared finite
window; `[STATED]` = asserted in a committed document without proof;
`[SILENT]` = the corpus does not address it; `[OPEN]`; `[MY READING]` =
this note's inference, load-bearing on nothing.

**Primary sources used.** Beyond the corpus: the three Barandes
manuscripts archived at the repository root —
`Quantum Systems as Indivisible Stochastic Processes.mhtml`,
`The Stochastic-Quantum Correspondence.mhtml` (arXiv:2302.10778v3),
`The Stochastic-Quantum Theorem.mhtml`. Quotations from these are marked
`[BARANDES]` and are text-extracted from the archived HTML; they are the
author's own wording, not the corpus's paraphrase.

---

## §0. THE ONE-PARAGRAPH ANSWER

The program **does** have "interference = holonomy of probability
transport" as a base — it is written at `README.md:43-44` and
`first-principles-conceptual-leap.md:11,31`. The problem is that **it is
the program's own slogan and it is not Barandes' base.** Barandes'
interference is a *temporal composition defect*: the failure of
`Gamma(t2<-t0) = Gamma(t2<-t1) Gamma(t1<-t0)`. The program's holonomy is
a *spatial/order comparison defect*: the failure of two localized
transports to commute. These are different objects, and the corpus has
spent v1–v10 operationalizing the second while the first — written into
`first-principles-conceptual-leap.md:92` as **axiom 2 of the target
theorem** — was witnessed twice in v1 and then never tested again. v10's
generated line is, by construction and then by theorem, divisible at
every step; on the corpus's own reading of Barandes that is the
definition of no interference. The 0-for-5 is therefore substantially a
**corollary**, not a discovery — with one important qualification, given
in §3.3, that keeps the transport-scope door genuinely open.

---

## §1. THE BASE PRINCIPLES, ENUMERATED

### 1.1 What the founding documents actually say

The program has **three** founding statements of principle, and they do
not agree about how load-bearing indivisibility is.

**(P-A) The central thesis / the holonomy slogan.** `README.md:39-44`:

> "Quantum phase is not a primitive add-on to probability. It is the
> geometric curvature, or exchange defect, of real stochastic transports
> across incompatible Cauchy hypersurfaces." … "Put more simply: the
> framework asks whether quantum interference can be understood as the
> **holonomy of probability transport itself**."

Operationally unpacked at `README.md:99-105` as a five-step
order-comparison: start with a record distribution, apply deformation
one, apply deformation two, reverse the order, compare. `:105` — "If the
two orders disagree, the stochastic transport has curvature." Slogan
form, `:115`: `quantum phase = stochastic holonomy`. Grade: `[STATED]`
(and it is a *question* — "asks whether" — not a claim).

**(P-B) The three ingredients that make it non-classical.**
`README.md:130-137`:

> "- **indivisible process level:** the transition kernel is fundamental,
> not decomposed into independent microscopic jumps;
> - **hypersurface dependence:** different Cauchy slices and local
> deformations are compared rather than reduced to one global time;
> - **exchange defect:** incompatible local transports leave a measurable
> finite mismatch."

Indivisibility is listed **first**. Grade: `[STATED]`.

**(P-C) The Barandes-alignment list.** `README.md:143-154` — five
bullets, of which the fourth is the one that matters here:

> "- actual finite records come first;
> - stochastic maps between records are primitive;
> - Hilbert-space, QFT, gauge, and continuum objects are reconstructed or
> represented as effective descriptions;
> - **non-Markovianity is allowed at the level of whole process kernels**;
> - continuum fields are not assumed as primitive objects when a
> finite-record descent statement is intended."

**This is the softest statement of the principle anywhere in the corpus,
and it is in the front door.** "Allowed" is a permission, not a
requirement. `[STATED]`.

**(P-D) The seven axioms of the target theorem.**
`first-principles-conceptual-leap.md:88-98` lists the hypotheses of the
aspirational Stochastic Geometry Reconstruction Theorem. Axiom 2, `:92`:

> "**Temporal indivisibility:** generic algebraic intermediate maps fail
> to be stochastic."

This is the strong form — the same definition Barandes uses — and it is a
**required hypothesis**, not a permission. Related, `:26`: the thing that
"cannot be globally removed" is "**failure of stochastic divisibility**
and nontrivial localized exchange defects" (both, conjoined). And `:13`:

> "The deep object is a causal rule for transporting probability
> distributions between hypersurfaces **whose failure to divide through
> intermediate hypersurfaces is controlled by local curvature data**."

That sentence is the program's actual thesis: *divisibility-failure
controlled by curvature*. Not curvature alone. `[STATED]`.

**(P-E) The lift-gauge discipline.**
`first-principles-conceptual-leap.md:197`:

> "**Gauge:** Schur-Hadamard freedom is lift gauge; physical gauge fields
> are connection holonomy; **do not conflate them**."

Restated as discipline in v2 (`v2/…paper6…:95`): "Schur-Hadamard gauge is
real gauge. **Phases in a chosen lift are not automatically physical
beables.**" `[STATED]`, and see §6.

**(P-F) The anti-import discipline.** `README.md:163-164`: "do not
silently import the structure the theory is trying to explain."
`[STATED]`.

### 1.2 What Barandes' own base is

`[BARANDES]`, *The Stochastic-Quantum Correspondence* §3.5, verbatim from
the archived manuscript:

> "One sees from this analysis that **interference is a direct
> consequence of the stochastic dynamics not generally being divisible.**
> More precisely, **interference is nothing more than a generic
> discrepancy between the actual indivisible stochastic dynamics and a
> heuristic-approximate divisible stochastic dynamics.** Interference
> encodes the fact that the underlying stochastic dynamics is
> indivisible, despite the way that unitary time-evolution operators look
> superficially divisible."

And §3.8:

> "superpositions and coherences are merely indications that one is
> catching a given system when it is in the midst of an indivisible
> stochastic process, **between division events** … coherences and
> superpositions are **mathematical artifacts of the fundamental
> indivisibility** of the underlying stochastic process."

And the operational form, §3.6:

> "given any probabilistically evolving system with indivisible or
> non-Markovian dynamics, one should now be able to interpret **any
> discrepancies between the behavior of such a system and the behavior of
> a heuristic-approximate divisible or Markovian approximation as
> manifestations of interference.**"

> **THE STRUCTURAL FINDING OF §1.** Barandes' interference is a
> **temporal composition defect** (a two-step object: `Gamma(t2<-t0)`
> versus `Gamma(t2<-t1)Gamma(t1<-t0)`). The program's holonomy is an
> **order-comparison defect** (a commutator of two localized transports
> at comparable times). *These are not the same object, and the corpus
> nowhere proves they are.* The program's slogan is therefore not a
> restatement of Barandes' base; it is an independent conjecture that
> was never reduced to it. `[MY READING]` on the significance; both
> clauses quoted verbatim above.

### 1.3 Barandes' division events — the definition, from the primary source

This matters because the corpus uses the term in two incompatible senses.

`[BARANDES]`, *Quantum Systems as Indivisible Stochastic Processes*:

> "Allowed conditioning times `t_0` are called **division events** for the
> given system … Division events are not global properties of the whole
> universe, but are **system-centric**."

`[BARANDES]`, *The Stochastic-Quantum Theorem*, after displaying the
divisibility condition (35):

> "As such, **conditioning times like `t'` will alternatively be called
> division events.**"

`[BARANDES]`, *The Stochastic-Quantum Correspondence* §3.7:

> "It is therefore natural to refer to the new conditioning time `t'` as a
> **division event**. … Suppose that these kinds of division events can
> be approximated as occurring **regularly** over a characteristic time
> scale `δt` … **The stochastic dynamics therefore takes the form of a
> discrete-time Markov chain.**"

> **A division event is a time at which the process DOES divide.**
> Divisibility holds *at* division events and fails *between* them.
> Dense division events ⟹ a Markov chain ⟹ (by §1.2) no interference.
> This is Barandes' own §3.7 argument for why classical stochastic
> modelling works so well.

**The corpus gets this right once and inverts it once.**

* CORRECT — `v10/note-d12-v6-v10-compatibility-ledger.md:41-43`:
  "An eventless collar may admit a reversible Markov presentation while
  the sealed sequence remains indivisible: **Chapman–Kolmogorov
  composition holds at commits and may fail across unsealed
  intervals.**" `[STATED]`, and it is the correct dictionary.
* INVERTED — `v6/relativistic-isp-v6-paper10.md:376-383`: "division
  events are exactly where record dynamics **visibly fails
  Markovianity** (P4 s10) … the indivisible (non-Markov) structure lives
  precisely where the positivity theorem does not need to hold". Under
  the primary-source definition this is backwards: division events are
  where the process is momentarily *divisible*. `[MY READING]` that this
  is an error; the two clauses are quoted verbatim and the reader can
  compare them with the Barandes quotations above. **Flagged for the
  errata, not repaired here.**

---

## §2. WHAT THE CORPUS PROVED ABOUT INDIVISIBILITY

### 2.1 The definition the corpus adopted — and its one defect

`v1/relativistic-isp-v1-paper22-entropy-indivisible.md:120-150`,
Definition 2:

> "A stochastic process `Γ(t←t_0)` is *indivisible* if for every
> intermediate time `t_0 < t' < t` there exists **no** genuine stochastic
> matrix `Γ̃(t←t')` such that `Γ(t←t_0) = Γ̃(t←t')Γ(t'←t_0)`.
> Equivalently, the algebraic 'intermediate' matrix
> `Γ̃ = Γ(t←t_0)[Γ(t'←t_0)]^{-1}` has at least one negative entry for
> some `(t,t',t_0)`. We call such `Γ̃` *pseudo-stochastic*."

**Defect, flagged:** the first sentence quantifies universally over `t'`;
the "equivalently" clause quantifies existentially. They are not
equivalent. `v1/…paper21…:95-97` uses the universal form.
`v1/…paper0…:83-89` (Definition 5) gives the foliation-relative version.
`[MY READING]`: everything the corpus proves is the **existential** form —
non-divisibility across specific intermediates — which is the weaker and
the honest claim.

### 2.2 The two constructed witnesses — both in v1, both abandoned

These are the only objects in the corpus **shown** to be indivisible
rather than labelled indivisible.

**(W1) The qubit Rabi process.**
`v1/…paper22-entropy-indivisible.md:243-284`, Theorem 1: for
`Θ(t) = e^{-iωtσ_x/2}` and mixed initial `p(t_0) = (1-ε, ε)`,

> "The process is indivisible on those intervals because the intermediate
> matrix `Γ̃_{01} = [p_0(t) - p_0(t')]/[1 - 2p_0(t')]` goes negative
> whenever `p_0(t) < p_0(t')`, which holds precisely during the
> entropy-decreasing phase."

`[THEOREM]` at its scope. `Γ(t'←t_0)` is invertible, so `Γ̃` is the
*unique* candidate intermediate; a negative entry therefore proves no
valid stochastic intermediate conditional exists.

**(W2) The free lattice-Dirac finite slab.**
`v1/…paper0-relativity-indivisible-rewrite.md:728-743`, Proposition 4D:

> "(The algebraic intermediate map acquires negative entries
> perturbatively). … `J_Δ := Γ_{2Δ}Γ_Δ^{-1}`. Then for the representative
> channel `B=(n,↑)` one has
> `J_Δ((n+4,↑)|(n,↑)) = -5Δ^8/(16384 a^8) + O(Δ^{10})`.
> Hence the exact finite-slab algebraic intermediate map is **not
> stochastic even for arbitrarily small positive `Δ`**: its negative
> entries already appear perturbatively."

`[THEOREM, proof sketch]`. This is a field-theoretic witness, not a toy.

**And here is the pivot the whole audit turns on.** The very next
paragraph, `v1/…paper0…:765`, demotes it:

> "Proposition 4D sharpens the finite-slab picture, but the ratio
> `Γ_{2Δ}Γ_Δ^{-1}` is still a *global* equal-time comparison. It is
> therefore **best read as a diagnostic warm-up rather than as the final
> relativistic deformation object.** We record it because it shows how
> exact slabs already package mass information and pseudo-stochasticity
> into a thickness-dependent family **before turning to the genuinely
> local construction.**"

> **THE HISTORICAL FINDING.** At paper zero the program held the
> indivisibility witness in its hand, judged it insufficiently
> relativistic, and **traded it for the exchange-defect (holonomy)
> route**. Every later "indivisible" object in the corpus is a label
> inherited from that trade. The trade was defensible on covariance
> grounds and was never revisited. `[MY READING]` on the significance;
> the demotion clause is verbatim.

### 2.3 Everything from v5 onward is a label, a target, or a refutation

* **v6 paper 4 (the SHARD foundational record paper) says so against
  interest.** `v6/…paper4…:489-490`: "| Barandes-level warning |
  **hidden-state model is still a Markov completion upstairs** | not yet
  full indivisible-process theorem |"; `:523-530`: "It is **not yet the
  full Barandes theorem.** The toy model still has a Markov completion
  upstairs in the retained holonomy."
* **v6 paper 56 is explicitly a program paper**, `:5`: "Nothing here is
  claimed proved." Its definition, `:33`: "A process is **divisible**
  (his Markovian) iff `Γ(t₂,t₀) = Γ(t₂,t₁)·Γ(t₁,t₀)` for *every*
  intermediate `t₁`; it is **indivisible** iff composition fails except
  at **sparse division events**." Its open target, `:154`: "construct the
  functor … and exhibit a `Γ_grav` that fails Chapman–Kolmogorov … **This
  is the genuine barrier crossing**" — `[OPEN]`. Its axis discipline,
  `:64`: "CP-divisibility and Barandes-indivisibility are **independent
  axes**."
* **v6 paper 57 §4.2 names the missing ingredient by name — sparseness.**
  `:73`: "**The functor is constructible; the open content is
  sparseness.** … whether the gravitational decoherence functional has
  non-trivial off-diagonal support *between* sparse seals (Tier-1
  indivisible) or is **diagonal at all times (continuous sealing →
  classical/divisible)**."
* **v6 paper 56:25 states the mechanism of the classical collapse
  exactly:** "A classical noise `δE(t)` is, by construction, **a definite
  recorded value at every instant — it seals continuously — and a
  continuously-sealed process is fully refinable, fully divisible, and
  carries no holonomy.**"
* **The one direct probe of whether the seal forces the matrix-level
  structure returned the opposite of what the program wanted.**
  `v7/…paper16…:34`, citing `v7/code/p18_seal_divisibility.py` and
  `v7/code/f6_unistochastic_record_blind_probe.py`: the seal "forces only
  the scalar `S = exp(−κχ)` — **not** the matrix-level CK-divisibility …
  and **not** the doubly-stochastic or unistochastic class (Barandes's
  assumed envelope)"; "**The seal motivates the survival, never the
  kernel.**" The receipt's own verdict lines, `p18_seal_divisibility.py:517`:
  `Q1 divisible Markov SEMIGROUP exp(chi L) … FORCED (the FENCE)`.
  `[MEASURED]`.
* **The corpus's own signature list names indivisibility first, with a
  falsifiable lab face — and points at v1.** `v6/…paper40…:245-248`:
  "`S1 INDIVISIBILITY (the process). No valid stochastic factorization
  through unrecorded intermediate times (Barandes). Lab face: quadratic
  / Zeno-class onset (Khalfin); corpus: v1p0, v5p2, v5p4.`" The corpus
  pointer is **v1p0** — the corpus itself locates its indivisibility
  content in paper zero.
* **The only measured non-Markovianity in the SHARD line is
  visible-level and hidden-Markov-reproducible.** `v6/…paper4…:518`:
  `max |P(X_3=1|X_2,X_1)-P(X_3=1|X_2)| = 0.130068881646990` — a
  first-order Markov failure of a *projection*, which any hidden-Markov
  model reproduces trivially, and which the same paper concedes is "still
  a Markov completion upstairs" (`:489-490`). `[MEASURED]`.
* **Two live refutations of the strong reading.** (i) magic ≠
  indivisibility — `v6/…paper40…:386-389`: "**magic = Wigner negativity
  is strictly finer than indivisibility.**" Binding constraint C7 at
  `v6/…paper56…:140`: "Indivisibility is necessary but **not**
  sufficient for nonclassicality." (ii) Bell — `v5/…paper14…:345-348`:
  "**Non-Markovianity does not evade Bell.**"
* **A terminological drift worth naming.**
  `v5/…paper5-entanglement-as-indivisible-record-nonfactorization.md:16`
  — "entanglement is indivisibility of the underlying finite stochastic
  process" — uses "indivisible" for *spatial* non-factorization
  (Definition 15.1 is the Bell LHV factorization). Nothing about
  intermediate times appears in that file. Two different notions share
  one word across the corpus. `[MY READING]`.

> **§2 VERDICT.** The corpus's indivisibility content is: **two exact
> witnesses in v1** (both on externally supplied unitary dynamics, both
> demoted), **one measured CK-defect-equals-interference-cross-term
> identity** (`v7/code/f3d_foundational_supports.py`, gap `< 1e-120`),
> **one measured negative** (the seal forces divisibility), **two
> refutations of over-strong readings**, and **everything else a label or
> a `[TARGET]`.** `v10/THE-THEORY-SO-FAR.md:15069` still carries the
> honest grade: "The SHARD↔Barandes dictionary identifying sealed
> holonomy with the interference cross-term is a `[TARGET]`, not a
> theorem."

---

## §3. THE DIVISIBILITY STATUS OF THE GENERATED LAW

This is the section the hypothesis stands or falls on. The answer is
**scope-dependent**, and the distinction is load-bearing.

### 3.1 The construction is a chain rule — divisible on histories by definition

The generated line's measure is *defined* by one-step conditionals:

* `v10/THE-THEORY-SO-FAR.md:5817` — "`μ(h·e) := μ(h)q(e|h)`".
* `v10/THE-COMPLETION-DICHOTOMY.md:239,385` — the completion transfer
  `q'(e|h) = q(e|h)·Z(h+e)/Z(h)` with `Z(h) = Σ_e q(e|h)Z(h+e)`.
* `v10/note-d70-horizon-limit-pin.md:28` and `note-d46b-…:22` — the
  horizon/Martin kernels `k_r(e|h) = q(e|h)·G(h+e, r−1)/G(h, r)`, Doob
  `h`-transforms of the same conditional.
* `v10/THE-THEORY-SO-FAR.md:5700` — L1 past-locality:
  "`q(e|h) = Q(e, D(e))`; 2,708 keys, 0 [violations]".

> **On the history space the generated law is trivially divisible: a
> valid stochastic conditional exists at every step, by construction.**
> `[THEOREM]` — it is the definition, not a discovery. But this is *not*
> yet a Barandes-classicality verdict: Barandes' divisibility is a
> statement about the **configuration space**, and "the whole history so
> far" is not a configuration — any process is Markov on its own
> history. The real question is whether the law remains divisible after
> coarse-graining to a genuine state. `[MY READING]`, and it is the
> qualification that keeps §8's pin non-trivial.

### 3.2 Closed scope: (H1)+(H2) make it a genuine Markov chain — Barandes-classical

At two-actor delivery-free d42a scope the corpus *proved* the
coarse-grained law is Markov on a 36-state space.

* **(H1)** `v10/note-d61-h1-closure-result.md:25-28`: "For all histories
  `h, h'` of ANY depth, `sigma(h) = sigma(h')` implies `menu(h) =
  menu(h')` as renamed event-multisets **with exact weights**."
  `[THEOREM]` at that scope. *This is sufficiency of the statistic: the
  one-step law depends on the history only through `sigma`.*
* **(H2)** `v10/note-d62-h2-update-table.md:44-47`: "For every history `h`
  of ANY depth and every event `e` admissible at `h`, `sigma(h + [e])` is
  a **function of** `(sigma(h), e renamed …)`." `[THEOREM]` at that
  scope. *This is closure of the statistic: `sigma` updates
  autonomously.*
* Together, `note-d62-…:49-58`: "**d44a's closure theorem is
  UNCONDITIONAL at two-actor delivery-free d42a scope**: the 36-state
  closure, the six-state chain and the Perron package hold **at every
  depth**."

> **(H1) + (H2) = "`sigma` is a sufficient statistic that updates
> autonomously" = the process is a MARKOV CHAIN on the 36 `sigma`
> states.** A Markov chain satisfies Chapman–Kolmogorov at *every*
> intermediate time; its algebraic intermediate maps are its own
> transition matrices, which are stochastic by construction. So on the
> corpus's own adopted definition
> (`v1/…paper22…:120-150`) the closed-scope generated law is
> **DIVISIBLE AT EVERY TIME — i.e. every time is a division event, and by
> Barandes §3.7 that is exactly the discrete-time Markov chain limit.**
> `[MY READING]` on the classification; the two theorem statements are
> quoted verbatim and the inference is one line.

**A terminological fact that matters for how this was missed.** The
generated-record line **never uses the word "Markov"**: `grep -c "Markov"`
returns **0** on `relativistic-isp-v10-paper30-…md` and on every
`note-d42*`/`d43*`/`d44*`/`d46*`/`d49*`. The string `sigma-Markov` occurs
nowhere in the v10 tree. The property is stated instead as lumpability
and determinism — paper 30 `:744-753`: "transitions are determined:
`sigma(h + [e])` is a function of `(sigma(h), renamed e)`, with 176
abstract transition keys", and `note-d49-…:87-88`: "the completed MENU is
a function of `sigma(h)` alone". `[MY READING]`: **the line proved the
Markov property under two other names and therefore never had to notice
what it costs in Barandes' framework.** (The word does appear, correctly
and at length, in the earlier D34b/D34d line — e.g.
`note-d34d-predictive-state-clock-status.md:499`, "the ideal chosen D34b
law is a time-homogeneous strong Markov process on its complete global
Harris configuration", and `paper21-…:57`, "**Every consistent SHARD
history law is Markov on an appropriately enlarged local state**, while
every physically observable record process is generally
non-Markovian." That last sentence is the corpus's own statement of the
hidden-Markov escape hatch — and §3.1's caveat is exactly why it does
not by itself buy indivisibility.)

**This is the audit's central collision, and the corpus predicted it at
paper zero.** `v1/…paper0…:578`, `[THEOREM]`-grade:

> "Take two Dirac wave-packet superpositions `ψ_A + e^{iφ}ψ_B` whose
> packets remain spatially disjoint … For different relative phases `φ`,
> the entire local probability history on that interval can be identical
> … Once the packets later overlap, however, the subsequent probabilities
> generally depend on `φ`. **Therefore future probabilities are not
> determined uniquely by past local probability histories alone. Any
> exact memory-kernel formulation on retained probability data must
> either fail to close uniquely or else carry hidden coherence data
> through its kernel or initial-slip term.**"

D61/D62 achieved **unique closure on retained probability data with no
hidden coherence data**. On the disjunction of `v1/…paper0…:578` that
forces the other branch: the closed law is one that *cannot* be
phase-sensitive. The 0-for-5 is the disjunction being cashed.

And `v1/…paper0…:590` states the discipline that the closed scope
violates:

> "One should **not** then iterate a single slab kernel as an ordinary
> Markov chain **unless genuine division events occur**."

### 3.3 Transport scope: divisible-by-construction on histories, UNTESTED at coarse grain

D70/D74 work at transport scope with the same per-history conditionals
(§3.1), so the same trivial-divisibility remark applies. But the
coarse-grain question is **open, and D74 built exactly the object needed
to ask it**:

* `v10/note-d74-transport-holonomy-pin.md:26-28` anticipated the failure
  of the closed-scope machinery: "the D62 sigma machinery at transport
  scope **is NOT expected to work** — say what does."
* `v10/LOG.md:11866-11868` (D74 delivered): "**THE CARRIER** constructed,
  not searched: the **coarsest descent quotient exists uniquely (the menu
  partition**; the coarsest weighted congruence closes the same squares
  on all six arms)".
* And the object that has no home in any corpus formalism,
  `v10/LOG.md:11874-11878`: "a sharp dichotomy — 44 curvature-type + **44
  DESCENT-OBSTRUCTION-type squares (different menus in the two orders:
  closable in NO quotient**; the invisible half all `(r,d)` at `1/2`).
  **No corpus formalism handles the second kind.**"

> **`[MY READING]`, offered as the audit's most testable conjecture:**
> the 44 descent-obstruction squares are the closest thing in the
> generated corpus to a Barandes obstruction — a pair of orders whose
> menus differ so that no quotient of the state space carries a
> well-defined induced transition. That is a *state-space* failure, and
> it is precisely the kind of failure that can make a coarse-grained
> `Gamma` family non-divisible. **It has never been tested as a
> divisibility question.** This is pin (a) in §8.

### 3.4 Which Barandes-classicality criterion each scope satisfies

| scope | object | conditionals exist at every step? | Barandes verdict | grade |
|---|---|---|---|---|
| history space, all scopes | `μ(h·e) = μ(h)q(e|h)` | yes, by definition | divisible — but **vacuously**, the state is the history | `[THEOREM]` (definitional) |
| closed scope (2-actor, delivery-free, d42a) | 36-state `sigma` chain | yes — (H1) sufficiency + (H2) autonomy | **DIVISIBLE. Every time a division event. Markov chain. Barandes-classical.** | `[THEOREM]` for the premises; `[MY READING]` for the classification |
| transport scope (D72/D74) | menu-partition descent quotient | **UNKNOWN** — never computed | **UNDECIDED**; 44 descent obstructions are the live candidate | `[SILENT]` |
| what D74 measured on it | exchange-square holonomy | n/a — this is the *order* defect, not the *composition* defect | measures the wrong defect for interference | `[MEASURED]` (the holonomy), `[MY READING]` (the "wrong defect") |

> **On the adjudicator's clause "the phase hunt computed holonomy on
> conditional (divisible) transport, which is gradient by
> construction":** *half confirmed, and the other half is more
> interesting.* The gradient part is confirmed at closed scope —
> `note-d74-transport-holonomy-pin.md:6-8` records the closed-scope
> theorem that "`μ` is an exact gradient there". But at transport scope
> the holonomy is **not** a gradient: D74 found it "GENUINE,
> IRREMOVABLE, `R⁺`-VALUED MODULUS CURVATURE" with group `⟨2,3⟩`
> (`LOG.md:11860-11870`). So the transport-scope hunt did *not* compute a
> trivially-flat object. What it computed was the **modulus** sector of
> an order defect — and the modulus sector is exactly the part that
> cannot carry a phase (§6). The hunt was not vacuous; it was
> **aimed at the wrong defect**.

---

## §4. DIVISION EVENTS AND SPARSENESS

### 4.1 Does the corpus distinguish record-forming from non-record events?

**v6 does, explicitly and structurally. v10 does not.**

* `v6/…paper40…:78-82`: "The program's ontology has a *record layer* (the
  ledger: **discrete, sparse, sealed commitments — division events**,
  seams, letters) and a *law layer* (everything that assigns weights …)."
* `v6/…paper2…:208`: "division events = a causal set, memory = the
  indivisible [structure]"; `:426`: "normal-ordering (`:·:`) | **no
  vacuum division events**"; `:546`: "**objective division events:** the
  event set is an observer-independent physical point process".
* `v6/…paper56…:33`: indivisible "iff composition fails **except at
  sparse division events**".
* `v6/…paper57…:73`: "**the open content is sparseness**".
* And the instruction was written into v10's own opening ledger and then
  not carried: `v10/note-d12-v6-v10-compatibility-ledger.md:13` —
  | **sparse indivisible face** | V7 P1: `S(nd)=S(d)^n`; free inter-seal
  profile and spacing | **retain non-Markov coherence between seals** |
  profile and spacing |

### 4.2 What v10 built instead

* `v10/note-d11-round1-opening-repairs.md:68-70`, an accepted scope
  downgrade recorded at the very start of v10 and never lifted:

  > "**ISP implementation remains open.** D11 is **Markov on augmented
  > typed history**. Barandes allows more general indivisible
  > non-Markovian measures but does not select this kernel."

* The generated line then made **every event a ledger write**, and the
  grammar says so at the alphabet level. `note-d42a-…:54` and paper 30
  `:147` both close the six-type alphabet with **`('n', a)` — recorded
  idle, the budget absorber**: *"nothing happened"* is itself a written
  record. Weight law, `d42a:66-70`: "idle = remainder (absorbs each
  unavailable total — redistribution, never dilution)"; paper 30 `:185`:
  "**Randomness enters only as recorded click outcomes.**" Orphaned
  proposals are "censused, never silently dropped" (`d42a:44`).
* **The word "sparse" does not occur in any d42 file or in paper 30**
  (grep clean), and "division events" appear there only as an inherited
  v6 residue (paper30`:996`, `note-d42-…-pin.md:12`), never as an object
  of this grammar. `[SILENT]`.
* Time in the generated line **is** record depth `|h|`; `sigma` is a
  function of the history at every depth. There is no event class that is
  not conditionable, and no state that exists between records — deliveries
  are single atomic two-wire events (`d42b1:48-56`, "the send *is* the
  receive"), and the base grammar has no delivery at all (`d42a:140-142`).
  `[MY READING]` from the construction; see §7's row.

> **On the adjudicator's sparseness clause: CONFIRMED as a corpus-level
> discipline that v10 dropped.** v6 states sparse division events as
> structure (five citations above), v6 paper 57 names sparseness as *the*
> open content, the v10 opening ledger instructed "retain non-Markov
> coherence between seals", and v10's first unit recorded "Markov on
> augmented typed history" as an accepted downgrade. Nothing after D11
> reopened it. The corpus's own mechanism sentence
> (`v6/…paper56…:25`) says what continuous sealing costs: "a
> continuously-sealed process is fully refinable, **fully divisible, and
> carries no holonomy**."

### 4.3 Is there ANY indivisible bridge in the committed corpus?

Checked against the candidates named in the assignment:

| candidate | is it a multi-step transition with no valid intermediate conditional? | grade |
|---|---|---|
| **blind conflict groups** | **No.** A blind group is a set of candidate events *available at one record point* whose component key is not in the initiator's own view (`v10/code/d42b3_placement_exact.py:499-513`; law at `note-d42b3-…:51-57`, "per-actor excess = (#blind ckey groups)/4, each blind group contributing EXACTLY 1/4"). Every constituent **is** a recorded event. What is non-conditionable is the **denominator**, not an intermediate state — `d42a:163-168`: "the arb split uses `past(e)` … **the join is precisely where it first exists as a record** … GLOBAL per-step normalization is NOT claimed". This is a **locality/visibility defect of the conditional**, not a missing intermediate. | `[MEASURED]` |
| D74's 44 **descent-obstruction** squares | **the only live candidate** — "different menus in the two orders: closable in NO quotient" (`LOG.md:11875-11877`). Never posed as a divisibility question. | `[MEASURED]` as an obstruction; `[SILENT]` as a divisibility test |
| the `2 → 5/2` jump | **No.** `N` is the per-cut **menu mass** (`note-d42b3-…:19-27`; row sums of the exact 6×6 transfer, `note-d43b-…:126-127`, `5/2` at state 3 = the conflict pair). "**The weights do not sum to 1. Menus sum to 2 or 5/2**" (`THE-COMPLETION-DICHOTOMY.md:219`). This is a **normalization** failure plus foliation-dependence of the naive normalizer — paper30`:553-557`: `N` "is **not a discrete gradient**: its chain products are foliation-dependent". | `[EXACT]`, wrong object |
| the D65/D74 mass ratios `{4/5,5/4}`, `{1/2,2/3,3/2,2}` | holonomy *values* on closed exchange squares — order defects, not composition defects | `[MEASURED]`, wrong object |
| deliveries in flight | **there is no in-flight state.** A delivery is one atomic recorded two-wire event (`d42b1:48-56`); the base grammar has none (`d42a:140-142`). Nothing lives between two records (paper30`:738-753`). | `[THEOREM]` (definitional) |
| the closed-scope `sigma` chain | explicitly the opposite — (H1)+(H2) prove conditionals exist at every step | `[THEOREM]` |
| v1 (W1), v1 (W2) | **yes — the two real bridges in the whole corpus**, §2.2 | `[THEOREM]` |

**And the line did not merely fail to build a bridge — it demolished the
one candidate it had.** `note-d42b2-elementary-click-refinement.md:13-19`:

> "Claim: both kernel draws and the merge click **refine EXACTLY into
> chains of elementary recorded clicks with past-conditioned Fraction
> weights, preserving every composite weight**"

with `:23-33` (K1: `q_i = 1/(|C|−i+1)`, chain weight exactly `1/|C|!`,
"**each click's enabled set is past-computable**") and `:34-42` ("Every
conditional is an exact Fraction"). The composite arbitration winner draw
— admitted as ONE composite click at `d42a:126-127` (RF3) — was
*deliberately* decomposed into a chain with a valid conditional at every
link. `[EXACT]`. **`[MY READING]`: this is the single most on-the-nose
instance of the audit's thesis. The one object in the generated line
that had the shape of an indivisible bridge was refined until it did not.**

**The one named, open exception, and it is a legislation gap not a claim
of indivisibility.** `note-d42b2-…:87-104` (B1): "The sector share is
fixed at the chain-opening join, from ITS past … **Carried question,
NAMED: MID-CHAIN DRIFT — component growth, base supersession, or delivery
arriving between clicks; the fixture-level receipts hold the environment
quiescent mid-chain and say so; the full refined grammar must legislate
it.**" (paper30`:460-464`, residue 4 at `:1094-1100`.) `[OPEN]`.

**The corpus's one genuine composition-failure object — and it convicts a
normalizer, not the law.** paper30`:600-608`: "Ratio preservation forces
`Z(h+e)/Z(h) = 1/N(h)`; no cut function has these increments, because
`N`'s chain products are foliation-dependent: **36 of the 202 canonical
diamonds refute integrability**." `[THEOREM]`. Against that, the flatness
ladder at paper30`:656-661` — raw weight products `0` violations, naive
cut-normalized `36`, gradient-completed `0` — i.e. **the law itself
composes path-independently and the completion restores it.**

> **No object generated by the v10 line has ever been shown to lack a
> valid intermediate conditional; none has ever been tested for it; and
> the one candidate was refined away on purpose.** `[SILENT]` as a test,
> `[EXACT]` as a construction choice.

---

## §5. UNISTOCHASTICITY

### 5.1 What Barandes needs it for

`[BARANDES]`, *The Stochastic-Quantum Correspondence* §3.4:

> "The system's transition matrix `Γ(t←0)` is then said to be a
> **unistochastic matrix**. That is, a unistochastic matrix is a square
> matrix whose individual entries are the **modulus-squares of the
> corresponding entries of a unitary matrix**. … The term orthostochastic
> matrix now refers to a square matrix whose entries are the
> modulus-squares of the corresponding entries of a **real orthogonal**
> matrix. Every orthostochastic matrix is unistochastic. Importantly,
> however, **the reverse is not generally true, meaning that the complex
> numbers generically play a necessary role in formulating a
> unistochastic transition matrix `Γ(t←0)` in terms of a unitary
> time-evolution operator.**"

> **This is the sentence the phase campaign never used.** Barandes'
> account of *why complex numbers are necessary* is not a holonomy
> argument at all. It is a **lift-obstruction** argument: the gap between
> orthostochastic and unistochastic. A real-weight transition matrix that
> is unistochastic but **not** orthostochastic is one that *cannot* be
> lifted with real amplitudes — the `i` is forced by the matrix's own
> entries. That is a computable property of a committed `Gamma`, and it
> has never been computed anywhere in the corpus. `[MY READING]` on the
> significance; the Barandes clause is verbatim.

### 5.2 Has any unit ever tested it? — the decision procedure exists; it was never pointed at a corpus matrix

**Two dedicated receipts exist** (duplicated byte-identically at
`v7/code/` and `v8/code/`), and they asked **"do the records FORCE the
class?"**, not "is THIS matrix in it".

`v8/code/f6_unistochastic_record_blind_probe.py:19-23` (docstring):

> "(Q3) Is UNISTOCHASTICITY (`Gamma_ij=|U_ij|^2` for a unitary U;
> strictly stronger than doubly-stochastic for `n>=3`) **RECORD-BLIND** —
> do the records, seeing only the real transition probabilities / the
> moment algebra M, fail to distinguish unistochastic from merely
> doubly-stochastic, because the distinguishing data are **unitary PHASES
> in ker R**…?"

Verdicts, `v8/code/p18_seal_divisibility.py:517-522`:

```
Q1  divisible Markov SEMIGROUP exp(chi L), L a Q-matrix     FORCED      (the FENCE)
Q2  DOUBLY-stochastic (columns sum 1)                       NOT/PERMITTED (un-forced)
Q3  UNISTOCHASTIC vs doubly-stochastic                      RECORD_BLIND (the FILLING)
```

**Three facts about these receipts change the shape of the pin.**

1. **The decision procedure is already written and already runs.**
   `f6_…:224-246` implements `unistochastic_3x3()` — the Bengtsson et al.
   chain-link / unitarity-triangle criterion. `p18_…:318-347` runs it on
   the textbook cyclic matrix and prints `:346` — "**Q3a: B is NOT
   unistochastic (unitarity-triangle FAILS for every column pair)**",
   `:347` — "`t=(1/2,0,0): 1/2 > 0+0 => no unitary U with |U_ij|^2=B_ij`".
   Positive control: the 3-dim DFT (`:355-362`).
2. **Every matrix these receipts test is a TEXTBOOK FIXTURE.** The DFT
   matrix and the canonical cyclic `B`. Neither receipt ever applies the
   criterion to a `Γ` produced by the click law, the seal semigroup, the
   K1 kernel, or any other committed corpus object.
3. **`f6` explicitly retracts the record-blindness reading that `p18`
   prints.** `f6_…:284-296`:

   > "**(R-a) The PARTITION 'unistochastic vs not' is, for a GIVEN
   > matrix, decidable from the real entries alone** … So a record CAN,
   > in principle, tell that `B_not` is not `|U|²` of any unitary. ⟹
   > **unistochasticity is NOT globally record-blind as a yes/no
   > partition.** (R-b) BUT the program never hands the records a free
   > doubly-stochastic matrix. The seal hands them `Gamma=|U|^2` **BY
   > CONSTRUCTION**"

   and `:328-329`: "the STRONG claim 'records cannot tell unistochastic
   from doubly-stochastic' is **FALSE in general** — we must NOT overclaim
   it." **Two committed receipts disagree in grade.** Errata item, §8.3.

**A confusion to head off.** `v6/relativistic-isp-v6-paper7.md:656`,
"**Theorem D1 (constructive unistochastic dilation)**", is *not* a
unistochasticity result in Barandes' sense: `:657-661` gives a unitary on
`C^{d²}` with `Σ_a |U_{(j,a),(i,0)}|² = Γ(j|i)` — the **ancilla-summed
Stinespring/Naimark dilation** (`:673`), which **every** stochastic matrix
admits trivially. Barandes' unistochasticity is `Γ_ij = |U_ij|²` on `C^d`
with **no ancilla sum**, and is a genuine restriction. The corpus's
`code/v6_p7d_dilation_campaign.py:4` phrasing — "every record law IS
unistochastically representable: (Q)-existence DISCHARGED" — reads as if
the question were closed. **It is not.** `[MY READING]`, and it is the
reason the question looks answered when it has not been asked.

**And the question is already on the books as un-run.**
`v10/LOG.md:11477-11478`: "…with the unistochasticity question (**is the
click-law kernel `Gamma(U)` for some `U`?**) as its companion arm."

> **VERDICT ON THE ADJUDICATOR'S CLAUSE. CONFIRMED, with the grade
> corrected from `[SILENT]` to `[OPEN, REGISTERED, NEVER RUN]`.** No unit
> has ever asked whether a committed corpus transition matrix is
> unistochastic. The corpus owns a working decision procedure, ran it
> only on textbook fixtures, once mislabelled the property record-blind
> and then corrected itself in a second receipt, holds a dilation theorem
> that is frequently mistaken for the answer, and has the real question
> written down in the LOG as a companion arm of a unit that was never
> executed.

### 5.3 What the test would need — and the matrices are already committed

* **Use the COMPLETED law, not the raw one.** The raw generated weights
  are not a stochastic matrix at all: "**The weights do not sum to 1.
  Menus sum to 2 or 5/2**" (`THE-COMPLETION-DICHOTOMY.md:219`). The
  root-free completion is the honest object — paper30`:779-790`:
  `Zhat(h) = 2^(-|h|)·f(class(sigma(h)))`, `f = (4,4,3,7,3,3)/3`,
  `lambda = 2`, "per-cut normalized, foliation-invariant". Its induced
  state-to-state transfer **is** stochastic: `note-d49-…:92-94` — "the
  completed state-to-state transfer is **a function of the state alone**,
  with d43b's conflict row `{1/7, 3/4, 3/28}`" (which sums to `1`), and
  `:88-89` — "the completed weights of all depth-`D` histories sum to
  exactly 1 for `D = 1..6` (**it is a measure**)."
* **Arm 1, the screen (minutes).** Unistochastic ⟹ **doubly stochastic**
  ⟹ **uniform stationary law** for an irreducible chain. The completed
  six-state chain has the conflict row `{1/7, 3/4, 3/28}` and a
  non-constant Perron vector `f = (4,4,3,7,3,3)/3`
  (`note-d44a-…:15`). `[MY READING]`: a chain with that structure will
  not have a uniform stationary law, hence is **not doubly stochastic,
  hence not unistochastic**. Cheap, and decisive in the negative
  direction. Note the corpus has already found the same shape once, on a
  different object — `v8/…paper2…:192`: "**the seal forces a
  forward-stochastic kernel but not double-stochasticity** (an explicit
  sealed semigroup carries a non-uniform stationary law)".
* **Candidate matrices, in order of cheapness:** (i) the **completed**
  six-state transfer above; (ii) the 36-state `sigma` chain
  (`note-d61-…:40`, 36 classes, 176 transition keys); (iii) the
  transport-scope descent quotient of D74 — the only one where an
  indivisible answer is even possible.
* **A committed v10 object already assumes the form.**
  `v10/code/d46e_smeared_interacting_exact.py:983-985` uses "`Gamma(U)` is
  doubly stochastic (`|U|²` with `U` unitary), so every order-`p > 0`
  coefficient has vanishing row AND column sums", gated at
  `data/d46e_…out:328` (`SG2-B` PASS, max row/col sum `3.74e-50`). That is
  the trivial direction (unitary ⟹ doubly stochastic) used as a **lemma**,
  never the converse tested on an emergent `Γ`. `[MEASURED]`.
* **The `n = 3` sharpener that makes this more than a screen.** For a
  `3×3` unitary, the rephasing-invariant phase content (the
  Bargmann/Jarlskog invariant) has its **magnitude fixed by the moduli**
  and only its **sign** free. `[MY READING]`, standard linear algebra,
  not a corpus result. If any committed `3×3` block is unistochastic
  and non-orthostochastic, then the corpus's own real data **determines a
  non-trivial phase invariant up to one sign** — and the corpus has
  already found a `Z/2` twice: the port-flip parity class
  (`note-d66-arbitration-crystal-result.md:373 ff`, non-zero on odd
  rings at five ring sizes) and the chirality/time-asymmetry theorem
  (`v6/publishable/paper-I-psd-words.md:11,75` — "the obstruction … is
  precisely the **chirality — the time-asymmetry**"). **That would
  convert the phase from "gauge" to "derived up to a sign fixed by the
  arrow of time."** Speculative, cheap to test, and it is the strongest
  reason to run pin (b).

---

## §6. THE PHASE-AS-GAUGE READING

### 6.1 What is gauge, and what is not

**Pointwise phases are gauge — and the corpus proves it, once, properly.**
`v2/…paper6-qft-reconstruction-no-go-investigation.md:554-570`,
Proposition 2 (diagonal phase ambiguity), `[THEOREM]`:

> "Let `U` be an `n × n` unitary matrix and let `D₁,D₂` be diagonal
> unitary matrices. Define `U' = D₁ U D₂`. Then `Γ(U')_ij = |U'_ij|² =
> |U_ij|² = Γ(U)_ij`. **Hence `Γ(U)` cannot determine `U` as a complex
> unitary matrix.**"

Proposition 3, `:585-600`, extends it to every Γ-derived functional.
Flagged at the point of definition in v1 — `v1/…paper0…:35`:

> "`Γ` may be represented as `Γ_{ij}=|Θ_{ij}|²`, but that representation
> is **not unique: phases and other lift data are not fixed by `Γ`
> alone**."

**But phase is operationally real, and the corpus proves that too.**
`v2/…paper6…:531-535`, `[THEOREM]` (the Mach–Zehnder no-go):

> "The phase shifter has no visible effect at the stochastic component
> level: `Γ(D_φ) = I`. Yet it controls the final interference pattern.
> **Therefore phase is not an optional bookkeeping convention. It is
> operationally real when coherent recombination is allowed.**"

`Γ(D_φ) = I` for every `φ` (`:330-337`) while `P_0(0|0)=1` versus
`P_π(0|0)=0` (`:395`). **Read together, Prop 2 and the MZ no-go say
exactly one thing: the phase is not a function of `Γ` and is not
disposable — so it must be fixed by something the corpus has not yet
supplied.** That is the whole content of the phase question, stated in
v2 and never retired.

The gauge group is exhibited: `v1/…paper22…:172` —
"`Θ'_{ij}(t) = e^{iφ_{ij}(t)}Θ_{ij}(t) … leaves Γ_{ij} invariant`";
`:176` — "a novel symmetry **without a classical analogue**". Discipline
restated at `v2/…paper6…:95`: "Schur-Hadamard gauge is real gauge.
**Phases in a chosen lift are not automatically physical beables.**"
Founding statement: `first-principles-conceptual-leap.md:197`.

**But the LOOP CLASS is not gauge — and that is the corpus's own
theorem.** `v6/…paper7…:676-689`, Theorem D3, as transcribed in
`v10/note-d71b-holonomy-phase-identity.md:179,348-356`:

> "…the Bargmann loop products `B(ℓ)=∏_k U_{i_{k+1}i_k}` are invariant
> (machine: `0.0e+00`), and **two-route interference is exactly the
> loop-phase law `P = |A|²+|B|²+2|A||B| cos(arg B(loop))`** (machine gap
> `2.8e-17`). Hence the **gauge-invariant content of the dilation is its
> loop class**."

`[THEOREM]` at v6 scope.

> **THE PRECISE ANSWER TO THE PHASE-AS-GAUGE QUESTION.** The
> adjudicator's clause is **half right, and the correct half is the
> important one**: individual phases are gauge (`[THEOREM]`), but the
> *holonomy* — the loop class — is gauge-**invariant** and is exactly
> what interference reads (`[THEOREM]`). So "quantum interference = the
> holonomy of probability transport" is **not** refuted by the gauge
> argument. What refutes it as stated is narrower and sharper:
> **that holonomy is the holonomy of the LIFT (`U` matrix elements), not
> of `Γ`.** The corpus's own theorem computes loop products of *unitary
> matrix elements*. `Γ` alone does not fix them (`v1/…paper0…:35`)
> **unless** additional structure — unistochasticity plus a dimension
> count — pins them (§5.3). D74 measured the holonomy of the *probability*
> transport and found it `R⁺`-valued: that is the **modulus** sector of
> the loop class, and the modulus sector is precisely the sector that the
> phase is *not* in. `[MY READING]` on the synthesis; every clause is
> quoted above.

### 6.2 The corpus already ran the discard-the-phase experiment

`v10/note-d71-phase-archaeology.md:1080-1092`, Clause 2, quoting the
gated receipt table at `v6/…paper4…:483`:

> "whose 'classical composition / **discard retained holonomy**' row
> returns '**no interference**, phase span = 0.000, **FAIL-BORN**',
> against 'complex holonomy composition … PASS-INTERFERENCE'. … And v8
> generalises it: '**positive (Boltzmann) real weights provably cannot
> produce the phase cancellation**' (`v8/…paper4…:94`). **The corpus's
> own position is that a positive-real weight sum is not the whole law.
> v10's generated line is a positive-real weight sum.**"

`[EXACT]` at fixture scope.

### 6.3 The one place a phase was derived, and its retraction

`note-d71-phase-archaeology.md:1065-1078`, Clause 1: v6 paper 7 Theorems
7.1–7.3 **derive** that the value space of an alternative is
`R⁺ × U(1) ∪ {0} = C`, using positivity to select `U(1)` over the
split-complex alternative; meanwhile v6 companion-B says the seal is
blind to the selector, paper Va lists complex weights as an admitted
**INPUT**, and v8 paper 2 proves the selecting bit lies in `ker R`.
"**These four documents disagree, and nobody owns the disagreement.**"
`[THEOREM]`/`[NO-GO]`/`[OPEN]` as marked there. Nothing in D75 changes
that; it is recorded here because §7's table needs it.

### 6.4 A guard: "the records are blind to phase" is WITHDRAWN, verbatim

Any audit conclusion of the form "v10 has no phase because records cannot
see one" is barred by the corpus's own retraction.
`note-d68-functional-slot-result.md:717-722` strikes four sentences,
including "~~a record measure of that shape cannot see a phase~~" and
"~~LOG #479's RECORDS CANNOT SEE A PHASE~~", as "**false as physics
sentences**" (`:714`). What replaced them: `:330-333` — "an imaginary
entry of `9/2048` leaves determinant `3887/67108864 > 0` and one of
`9/1024` gives `−1/67108864 < 0`. ***The linear system is phase-blind;
the constraint set C1–C4 is not.***" `[EXACT]`; and `:336-338` — the
constraint rank on the antisymmetric block is **268** at depth 2 and
**3,739** at depth 3, so "**a record demand of paper 29's shape does see
a phase**" `[MEASURED]`. What kills coherence is instead the *dynamical*
demand C5 (`cohdim = 0` at depths 2–5, `:396`).

Likewise the v10 gauge declaration is circular and its own referee says
so: `note-d44f-foliation-and-measure.md:130` declares "complex phases
belong to the same zero-`|amp|²` gauge sector (declared in-gate)", and
`reviews/d44f-round1-hostile-review.md:236` records "**Complex phase
(i/√2, 1/√2): convicted, but spuriously (real-only battery) — not a
battery pass, and not honestly a battery test either.**"

> **So the honest statement is narrow: the generated line's *weights* are
> positive-real by construction and its *holonomy* is `R⁺`-valued by
> measurement. Neither fact says the records could not have carried a
> phase.** `[MY READING]`.

---

## §7. THE AUDIT TABLE

Every base principle located in §1–§2, with its status. "Followed"
requires an operationalization, not an endorsement.

| # | principle | source | status | where / by what |
|---|---|---|---|---|
| 1 | **records first; stochastic maps between records primitive** | `README.md:145-149` | **FOLLOWED** | the entire v10 generated line; `μ(h·e)=μ(h)q(e|h)` (`THE-THEORY-SO-FAR.md:5817`). `[THEOREM]` |
| 2 | **Hilbert space is effective, not primitive** | `README.md:150-151` | **FOLLOWED** | no primitive Hilbert object anywhere in v10; `[THEOREM]` |
| 3 | **do not silently import what you are explaining** | `README.md:163-164` | **FOLLOWED, at cost** | the discipline is why `e^{iS}` was refused (`note-d71-…:1051-1063`); it is also why the phase slot is occupied by `+1` without an argument (`note-d71-…:1094-1104`). `[MEASURED]` |
| 4 | **exchange defect / holonomy of probability transport** (P-A) | `README.md:43-44,99-115` | **FOLLOWED — and it delivered a real object** | D72/D74: genuine irremovable `R⁺` curvature, group `⟨2,3⟩`, J-governed (`LOG.md:11860-11884`). `[MEASURED]`, 8 scopes |
| 5 | **…as the source of quantum PHASE** (the slogan's second half) | `README.md:115` | **FALSIFIED AT FIVE ADDRESSES** | 0-for-5 (`LOG.md:11934`, `THE-THEORY-SO-FAR.md:6175`). And §6.1 explains why: `Γ`-level holonomy is the modulus sector. `[MEASURED]` |
| 6 | **temporal indivisibility: generic algebraic intermediate maps fail to be stochastic** (P-D axiom 2) | `first-principles-…:92` | **VIOLATED at closed scope; NEVER OPERATIONALIZED at transport scope** | violated by (H1)+(H2) (`note-d61-…:25`, `note-d62-…:44`) which make the `sigma` law a Markov chain — divisible at every time. The line never uses the word "Markov" (§3.2), so the cost was never priced. Never tested at transport scope. `[THEOREM]` for the premises, `[MY READING]` for the classification |
| 6b | **the one candidate indivisible bridge in the generated line** | `d42a:126-127` (RF3) | **DELIBERATELY REMOVED** | `note-d42b2-…:13-19` refines the composite arbitration draw into "chains of elementary recorded clicks with past-conditioned Fraction weights". `[EXACT]`. Residual named gap: MID-CHAIN DRIFT (`d42b2:87-104`), `[OPEN]` |
| 7 | **the failure to divide is controlled by curvature** (the actual thesis) | `first-principles-…:13` | **NEVER OPERATIONALIZED** | no unit anywhere relates a divisibility defect to a holonomy value. The two sides have never been computed on the same object. `[SILENT]` |
| 8 | **sparse division events** | `v6/…paper40…:78-82`, `v6/…paper56…:33`, `v6/…paper57…:73` | **VIOLATED / DROPPED** | v10 makes every event a ledger write; recorded as an accepted downgrade at `note-d11-round1-opening-repairs.md:68-70` and never reopened. The v10 opening ledger had instructed the opposite (`note-d12-v6-v10-compatibility-ledger.md:13`). `[STATED]`→dropped |
| 9 | **non-Markovianity is allowed at whole-kernel level** | `README.md:152` | **FOLLOWED — and it is the weak clause that licensed everything** | "allowed", not required; v10 exercised the permission not to. `[STATED]` |
| 10 | **unistochasticity** (`Γ = \|U\|²`) | `[BARANDES]` §3.4; `v1/…paper1…:65` | **REGISTERED, NEVER RUN on any corpus matrix** | the decision procedure exists (`f6_…:224-246`) and runs — **only on textbook fixtures** (DFT; the cyclic `B`, `p18_…:346`). Two receipts disagree on the record-blindness grade (`p18_…:476-486` vs `f6_…:284-296`). The real question is written in `LOG.md:11477-11478` as an un-run companion arm. `[OPEN]` |
| 10b | **the dilation theorem is not the unistochasticity answer** | `v6/…paper7…:656-673` | **CONFLATION RISK** | Thm D1 is the ancilla-summed Stinespring/Naimark dilation on `C^{d²}`, which every stochastic matrix admits; `code/v6_p7d_…:4` phrases it as "(Q)-existence DISCHARGED". Barandes' `Γ_ij=\|U_ij\|²` on `C^d` is a genuine restriction and is untested. `[THEOREM]` (the dilation), `[MY READING]` (the conflation) |
| 11 | **the orthostochastic/unistochastic gap = where complex numbers are necessary** | `[BARANDES]` §3.4 | **NEVER OPERATIONALIZED — the largest single miss** | zero corpus hits. This is Barandes' actual derivation of the `i`, and the phase campaign never ran it. `[SILENT]` |
| 11b | **"records are blind to phase"** | `note-d68-…:717-722` | **WITHDRAWN by the corpus itself** | four sentences struck as "false as physics sentences"; the constraint set sees the imaginary part (rank 268 / 3,739, `:336-338`). Any audit must not lean on record-phase-blindness. `[EXACT]`/`[MEASURED]` |
| 12 | **phases in a lift are gauge; the loop class is not** (P-E) | `first-principles-…:197`; `v1/…paper0…:35`; `v6/…paper7…:676-689` | **FOLLOWED for the first half; the second half is un-propagated** | the gauge discipline is enforced corpus-wide; the gauge-*invariance* of the loop class (v6 p7 Thm D3) is cited nowhere in v10 (`note-d71-…:27-31,89-90`). `[THEOREM]`, un-propagated |
| 13 | **interference = the CK defect** | `[BARANDES]` §3.5 | **MEASURED ONCE, at v7 fixture scope, never on a generated object** | `v7/code/f3d_foundational_supports.py` — CK gap `0.329` unsealed, `0.0` at a seal, entrywise identity to the interference cross-term `< 1e-120`. Model-relative `[POSITED]` per `v8/…paper1…:30` |
| 14 | **indivisibility ⇒ nonclassicality** | (never a corpus principle) | **REFUTED, correctly** | `v6/…paper40…:386-389` magic = Wigner negativity is strictly finer; C7 at `v6/…paper56…:140`. `[MEASURED]` |
| 15 | **indivisibility ⇒ Bell exemption** | (never a corpus principle) | **REFUTED, correctly** | `v5/…paper14…:345-348`. `[THEOREM]` |
| 16 | **division events = where divisibility HOLDS** (dictionary direction) | `[BARANDES]`, three manuscripts | **FOLLOWED once, INVERTED once** | correct at `note-d12-v6-v10-compatibility-ledger.md:41-43`; inverted at `v6/…paper10…:376-383`. `[MY READING]` that the latter is an error |
| 17 | **the SHARD↔Barandes functor** | `v6/…paper56…:48,154` | **NEVER OPERATIONALIZED** | still `[TARGET]` at `THE-THEORY-SO-FAR.md:15069`; `v6/…paper4…:489-490` records that the SHARD model "is still a Markov completion upstairs" |

**Headline rows.** **FOLLOWED:** 1, 2, 3, 4, 9, 12 (first half), and the
two correct refutations 14, 15. **VIOLATED:** 6 (indivisibility, by
(H1)+(H2) at closed scope), 6b (the one candidate bridge, refined away on
purpose), 8 (sparseness, by every-event-a-record — including a *recorded
idle*), 5 (the slogan's phase half, empirically, at five addresses), 16
(the dictionary direction, once). **NEVER OPERATIONALIZED:** 7 (the
actual thesis — divisibility-failure controlled by curvature), 10 and 11
(unistochasticity, and the orthostochastic gap where Barandes locates the
necessity of `i`), 13 (the CK defect on a generated object), 17 (the
functor). **GUARDS:** 10b (the dilation theorem is not the answer) and
11b (record-phase-blindness is withdrawn) — two ways this audit could
have reached a wrong conclusion, both blocked by the corpus's own record.

---

## §8. THE VERDICT, AND THE PIN

### 8.1 Does the adjudicator's hypothesis survive?

**Yes, in its main clause, with two corrections and one strengthening.**

**SURVIVES — the closure theorems built a divisible process.** (H1)
(`note-d61-…:25-28`) plus (H2) (`note-d62-…:44-47`) are exactly
sufficiency-plus-autonomy of `sigma`, i.e. the Markov property on 36
states. A Markov chain divides at every time. On the corpus's own
adopted definition (`v1/…paper22…:120-150`) that is the definition of
*not* indivisible; on Barandes' §3.7 it is the classical limit. And the
program's own paper zero stated the disjunction in advance
(`v1/…paper0…:578`): a law that closes uniquely on retained probability
data *cannot* be phase-sensitive. **So at closed scope the 0-for-5 is
substantially a corollary of the closure theorems, not an independent
discovery.** That sentence should be added to how the result is quoted.

**SURVIVES, AND HARDER THAN THE ADJUDICATOR PUT IT — the line did not
merely fail to build an indivisible bridge, it removed the one it had.**
`note-d42b2-elementary-click-refinement.md:13-19` refines the composite
arbitration draw into "chains of elementary recorded clicks with
past-conditioned Fraction weights, preserving every composite weight".
`[EXACT]`. The refinement was good practice by every other standard in
the program — it is what makes the weights auditable — and it is exactly
what a Barandes-faithful construction must not do everywhere.

**SURVIVES — sparseness was a corpus principle and v10 dropped it.**
Five v6 citations state sparse division events as structure; v6 paper 57
names sparseness as *the* open content; the v10 opening ledger instructed
"retain non-Markov coherence between seals"; D11's round 1 recorded
"Markov on augmented typed history" as an accepted downgrade; nothing
reopened it. §4.

**CORRECTION 1 — "the phase hunt computed holonomy on divisible transport,
which is gradient by construction" is only true at closed scope.** At
transport scope D74 found genuine irremovable curvature with group
`⟨2,3⟩` across eight scopes and 27,186 non-unit squares
(`LOG.md:11860-11880`). The hunt was not vacuous. It was aimed at the
wrong *kind* of defect: an order-comparison (spatial) defect rather than
a composition (temporal) defect, and it therefore saw the `R⁺` modulus
sector, which is exactly the sector a phase cannot live in (§6.1).

**CORRECTION 2 — "the phase is gauge" is half right, and the wrong half
is the one that matters.** Pointwise phases are gauge (`[THEOREM]`,
`v1/…paper0…:35`), but the **loop class is gauge-invariant and is exactly
what interference reads** (`[THEOREM]`, v6 p7 Thm D3 via
`note-d71b-…:179`). The correct statement is not "the phase is gauge" but
"**the interference-carrying holonomy is a holonomy of the lift, and `Γ`
alone does not determine it**".

**CORRECTION 3 — "unistochasticity was never tested" is right about the
corpus's matrices and wrong about its tooling.** The decision procedure
is implemented and runs (`f6_…:224-246`), the corpus once printed a
record-blindness verdict and then corrected itself in a second receipt,
it holds a dilation theorem widely mistakable for the answer, and the
real question is registered at `LOG.md:11477-11478` as an un-run
companion arm. The correct grade is `[OPEN, REGISTERED, NEVER RUN]`, and
that makes pin (b) cheaper than it looked, not harder.

**STRENGTHENING — the derivable thing the adjudicator named is sharper
than stated.** Barandes' own account of why complex numbers are
*necessary* is the **orthostochastic/unistochastic gap** (§5.1), a
decidable property of a committed matrix. The corpus has never computed
it. And at `3×3` the moduli fix the rephasing-invariant phase up to a
single sign — a `Z/2` the corpus has already found twice (§5.3). This
converts "the phase may be gauge" into a testable programme rather than a
resignation.

### 8.2 The pins, ranked

---

**PIN (a) — THE INDIVISIBILITY TEST AT TRANSPORT SCOPE. RANKED FIRST.**

*One unit. Reuses D72/D74's committed census machinery and D74's already-
constructed carrier. Exact `Fraction`s throughout.*

**The object.** D74 constructed "the coarsest descent quotient … (the
menu partition)" on the transport-scope grammar (`LOG.md:11866-11868`).
Take the induced transition family on that quotient — and on the coarser
register-overlap classes as a second arm — for the d42b1 grammar at the
D72/D74 depths and actor pools.

**The test (v1 Prop 4D, ported to the generated line).** For each pair of
depths `t0 < t' < t`, form `Γ(t←t0)` and `Γ(t'←t0)` on the quotient and
compute the algebraic intermediate `J = Γ(t←t0)·Γ(t'←t0)^{-1}`. Report
(i) whether `Γ(t'←t0)` is invertible; (ii) the sign pattern of `J`;
(iii) if singular, run the LP feasibility form directly — does there
exist a stochastic `X` with `X·Γ(t'←t0) = Γ(t←t0)`?

**Falsifier, sharpest form.** *If for every committed quotient, every
depth triple, and every scope in D74's eight, a valid stochastic
intermediate exists, then the generated law is divisible at coarse grain,
the generated line is Barandes-classical, the 0-for-5 is a theorem-level
corollary, and the enrichment fork is the only remaining route.* That is
a first-class negative and it retires the phase hunt honestly.

**Positive outcome.** One negative entry in `J`, or one infeasible LP,
**exhibits the corpus's first generated indivisible bridge** — the first
since v1, and the first ever on the program's own generated law. It would
also relocate the phase hunt: interference would have an address (the
composition defect), and the 0-for-5 at holonomy addresses would become
unsurprising rather than damning.

**Pre-registered prime suspect.** The 44 descent-obstruction squares
("different menus in the two orders: closable in NO quotient" —
`LOG.md:11874-11877`). If anything in v10 fails to admit an intermediate,
it is these. **Gate them first and separately from the 44 curvature-type
squares.**

**Why first.** It is the only pin that directly decides the adjudicator's
hypothesis; the object already exists and is committed; the negative is
as reportable as the positive; and it is the first test of
`first-principles-conceptual-leap.md:92` — the program's own axiom 2 —
in nine versions.

---

**PIN (b) — THE UNISTOCHASTICITY TEST ON THE COMMITTED CHAIN. RANKED
SECOND; cheap enough to ride along with (a), and already registered at
`LOG.md:11477-11478`.**

*The decision procedure is already written: reuse `unistochastic_3x3()`
from `v8/code/f6_unistochastic_record_blind_probe.py:224-246`, with its
own DFT/cyclic controls, and point it at corpus matrices for the first
time.*

**Arm 0 — use the right matrix.** The raw generated weights are not
stochastic (menus sum to `2` or `5/2`,
`THE-COMPLETION-DICHOTOMY.md:219`). The object is the **completed**
transfer: `Zhat` root-free completion (paper30`:779-790`), whose
state-to-state matrix is a function of the state alone with conflict row
`{1/7, 3/4, 3/28}` (`note-d49-…:92-94`) and total mass exactly `1`
(`:88-89`).

**Arm 1 — the screen (minutes).** Is that completed six-state transfer —
or the 36-state `sigma` chain — **doubly stochastic**? Prerequisite for
unistochastic. The non-constant Perron vector `f = (4,4,3,7,3,3)/3`
(`note-d44a-…:15`) and the lopsided conflict row make a uniform
stationary law unlikely. **Falsifier:** if not doubly stochastic, then
not unistochastic, and **the generated law is not a closed
Barandes-quantum system — at best an open subsystem, whose phase content
then provably sits in a dilation the corpus has never constructed.**
Report that as a structural finding, not a failure. Precedent for the
same shape on a different object: `v8/…paper2…:192`.

**Arm 2 — the real question (only if arm 1 passes anywhere).** For each
doubly-stochastic block: is it **unistochastic**? And is it
**orthostochastic**? The gap between the two is where Barandes locates
the necessity of complex numbers (§5.1). **Falsifier:** if every
committed block that is unistochastic is also orthostochastic, then the
generated law's real weights admit a *real* amplitude lift, and the `i`
is not forced by the process — the enrichment fork is then correctly
framed as an axiom, permanently. **Do not accept
`v6/…paper7…:656` (Theorem D1) as an answer to this arm** — it is the
ancilla-summed dilation, §5.2.

**Arm 3 — the sharpener.** On any `3×3` unistochastic non-orthostochastic
block, compute the rephasing-invariant phase magnitude from the moduli
and check whether its free sign correlates with a committed `Z/2` — the
D66 port-flip parity (`note-d66-…:373 ff`) or the chirality of
`v6/publishable/paper-I-psd-words.md:11,75`. A correlation would be the
first derivation of phase content *from* the corpus's real data.
`[MY READING]`, speculative, cheap.

---

**PIN (c) — THE SPARSE-RECORDS GRAMMAR VARIANT. RANKED THIRD; the repair,
not the diagnosis.**

Build a d42-family grammar in which only a declared subclass of events is
a ledger write (the others advance state without being conditionable),
and ask whether the record-to-record law between writes admits valid
intermediate conditionals. **Falsifier:** if indivisibility does *not*
appear between sparse records, sparseness is not the missing ingredient
and the enrichment fork is forced. **Why third:** it is a *construction*,
so it costs a grammar, a new admissibility layer, and a fresh receipt
chain — and if (a) returns "indivisible", (c) is unnecessary; if (a)
returns "divisible", (c) becomes the obvious next unit with its
hypothesis already sharpened. Note also that v6 already named its cost
(`v6/…paper56…:25`): continuous sealing is what makes a process fully
divisible. Note further that the generated grammar makes even *idleness*
a record (`d42a:54`, `('n', a)` — recorded idle), so a sparse variant
must legislate a non-recording step class, which is exactly the "MID-CHAIN
DRIFT" gap already named at `note-d42b2-…:87-104`. **That named gap is
where pin (c) should start.**

---

**A FOURTH PIN, already written down by someone else and worth noting so
it is not lost.** `note-d71-phase-archaeology.md:1188-1201` proposes
replacing the committed positive root `√(1/2)` by `e^{iθ}√(1/2)` and
re-running the existing batteries. It has not been executed. It tests a
*different* question from (a)/(b) — whether the committed record demands
would notice a phase if one were inserted — and after `note-d68-…:717-722`
(§6.4) the answer is no longer obviously "no". Rank it after (b); it is
the cheapest of all four, but it probes the instrument rather than the
process.

### 8.3 Housekeeping items this audit turned up (not repaired here)

1. **`v6/…paper10…:376-383` inverts the Barandes dictionary** (division
   events described as where Markovianity fails). Compare
   `v10/note-d12-v6-v10-compatibility-ledger.md:41-43`, which has it
   right, and the three primary quotations in §1.3. Errata candidate.
2. **`v7/…paper19…:102`** ("CP-divisibility is incompatible with
   Barandes-indivisibility") contradicts **`v6/…paper56…:64`**
   ("CP-divisibility and Barandes-indivisibility are **independent
   axes**") and `:39` ("a closed unitary qubit is Barandes-indivisible
   yet, as a channel, trivial"). Paper 56 is the correct statement.
   Errata candidate.
3. **`v1/…paper22…:120-150` Definition 2 mixes quantifiers** (universal
   in the sentence, existential in the "equivalently" clause). Every
   corpus result establishes the existential form only. Any pin that
   quotes "indivisible" should say which form it means. **Pin (a) above
   means the existential form.**
4. **Two committed receipts disagree on the unistochasticity grade.**
   `p18_seal_divisibility.py:476-486` prints `Q3 … RECORD_BLIND` flatly;
   `f6_unistochastic_record_blind_probe.py:284-296,328-329` explicitly
   rejects that as an overclaim ("the STRONG claim … is **FALSE in
   general**"). `f6` is right. `v8/…paper2…:192` carries the softened
   version. Errata candidate, and it matters because pin (b) depends on
   the property being decidable.
5. **`v6/…paper7…:656` Theorem D1 ("constructive unistochastic
   dilation") should be retitled or annotated.** It is the ancilla-summed
   Stinespring/Naimark dilation, which every stochastic matrix admits;
   `code/v6_p7d_dilation_campaign.py:4`'s "(Q)-existence DISCHARGED"
   reads as though Barandes' question were closed. §5.2.
6. **`v5/…paper5…` uses "indivisible" for spatial non-factorization**
   (`:16,23`; Definition 15.1 is the Bell LHV factorization), a different
   notion from the temporal one used everywhere else. Glossary candidate.

---

## §9. COVERAGE AND LIMITS OF THIS AUDIT

* **Read in full or near-full:** `README.md`,
  `first-principles-conceptual-leap.md`, `v1/…paper0…`, `v1/…paper22…`,
  `v5/…paper14…`, `v5/…paper4…`, `v5/…paper5…`, `v6/…paper56…`,
  `v6/…paper57…` §4, `v6/…paper40…`, `v7/…paper16…`, `v7/…paper19…`,
  `v4/…paper24…` (null), `v10/note-d61-…`, `v10/note-d62-…`,
  `v10/note-d70-…`, `v10/note-d71-…`, `v10/note-d71b-…`,
  `v10/note-d74-…` (pin and result), `v10/note-d12-v6-v10-compatibility-ledger.md`,
  `v10/note-d11-round1-opening-repairs.md`, `v10/note-d42a-…`,
  `note-d42b1-…`, `note-d42b2-…`, `note-d42b3-…`, `note-d42b7-…`,
  `relativistic-isp-v10-paper30-…`, `THE-COMPLETION-DICHOTOMY.md`,
  `note-d43b-…`, `note-d49-…`, `note-d68-functional-slot-result.md`,
  `v2/…paper6…`, `v6/…paper7…` (§7 and §D), `v8/…paper2…`,
  `v7,v8/code/p18_seal_divisibility.py`,
  `v7,v8/code/f6_unistochastic_record_blind_probe.py`,
  `v10/code/d42b3_placement_exact.py`,
  `v10/code/d46e_smeared_interacting_exact.py`,
  and the three archived Barandes manuscripts.
* **Corpus-wide greps** for `Barandes`, `indivisib`, `divisib`,
  `unistochastic`, `doubly stochastic`, `division event`, `Markov`,
  `Chapman`, `|U|^2`, `dilation`, across `v1 … v10`, `publishable/`,
  root-level papers and `code/`.
* **Not done here:** no computation of any kind. Every classification of
  the generated law as divisible is an *inference from committed theorem
  statements*, labelled `[MY READING]` where it is an inference. Pin (a)
  exists precisely because the transport-scope question **cannot** be
  settled by reading.
* **Not done here:** the `~/workspace/physics` tree was not swept; the
  one v10 reference to it (`note-d71b-…:746`) concerns gauge-field
  holonomy homonyms, which §6 excludes from this thread by the same
  argument D71b uses.
* **This note edits nothing and commits nothing.**
