# W5 — BARANDES RECAST AS CHART THEORY

**Status:** RESULT, STRICT, **GREEN-UNREVIEWED** (not citable; terminal is
conferred by a hostile round), 2026-07-28.
**Programme:** v12 — THE WELD (`v12/LOG.md` #1–#8).
**Pin:** `v12/note-w5-barandes-recast-pin.md` (frozen before this note).
**Binding:** paper 0 v2.1 §1 (T1 scope notes, T2′, T3′, T5′) and §4 W5.
**Receipt:** `v12/code/w5_ltp_lemma_exact.py` → `v12/code/w5_output.txt`
(29 gates, 29 pass, 0 fail; 9 anchors, 0 anchor failures; 8 controls, 0
control failures; exit 0; runtime 3.5 s as printed; byte-identical under
`PYTHONHASHSEED` 0 and 12345 modulo timings).
**Lean:** NONE.

**Verdict.** [B3]'s apparatus recasts into weld language as **twenty**
identifications: **14 FAITHFUL, 3 EXTENSION, 3 TENSION**. Of the five
identifications the pin names: **two survive as written** (unistochasticity
= shadow-of-lift, I-12; the Schur-Hadamard gauge = the fibre phase
freedom, I-13 — sharpened, the fibre sits over *pairs* of configurations);
**two split** into a faithful half and a v12 half (I-8/I-9: division events
kill the defect *on the actual distribution* by [B3]'s own law of total
probability, but kill it *as matrices* only under a reading his text
resists; I-2/I-3: the epistemic axiom separates the epistemic layer but
does not index it by chart); and **one is corrected by [B3]'s own text**
(I-16/I-17: "dilation = chart enlargement" is false for the chart's *base*
and true only for its *fibre*). The LTP lemma is proved and its forcing is
exhibited exactly.

---

## 0. Scope, and the atlas line

This note is about **[B3]'s formal apparatus as published** (J. A.
Barandes, *Quantum Systems as Indivisible Stochastic Processes*,
arXiv:2507.21192, 30 July 2025; 35 pages; page numbers below are that
document's own, verified against the PDF read in-session). It makes no
claim about nature, no Bell-inequality claim, no locality claim and no
covariance claim. [B3]'s equivalence theorem (the stochastic-quantum
theorem, p.19) is proven mathematics and is **not under test**
(`bc/LOG.md` #1).

**The atlas line, policed at every joint.** Paper 0 v2.1's T1 engraves
that the **atlas move** — replacing Barandes' one global process by a
family of context-local processes — is **v12's own postulate, not derived
from [B1–B3]**. Every identification below therefore carries exactly one
mark:

- **FAITHFUL** — [B3]'s own text supports the identification; his words
  are quoted.
- **EXTENSION** — the atlas postulate speaking; v12's, not his.
- **TENSION** — his text resists the reading; both sides are quoted and
  the resolution v12 adopts is stated.

Marks are assigned to the *identification*, not to the sentence: where an
identification is faithful in one reading and resisted in another, it is
**split into two numbered entries**, so that no single mark is doing two
jobs (I-2/I-3, I-8/I-9 and I-16/I-17 are the three splits).

---

## 1. The recast, identification by identification

### 1.1 The kinematical layer — the chart and its base

**I-1. The configuration space `C` is the chart's base.** **FAITHFUL.**

> "one can take the sample space to be the system's **configuration space
> C**, which is a **fixed ingredient of the model**, meaning that it
> remains the same for every physical run or instantiation of the model"
> ([B3] p.5).
>
> "**Kinematical axiom:** … The configuration space is a **fixed feature
> of the model**, meaning that it does not vary between real-world runs or
> instantiations of the model." ([B3] p.29.)

A *chart* in T1's sense is exactly a [B3] model: definite configurations,
an ordinary probability law over them. Nothing is added; "chart" renames
"model".

**I-2. The epistemic layer is separable from the nomological layer.**
**FAITHFUL.**

> "the configuration space `C` is one of the **fixed** ingredients of the
> model, and provides the model with its **kinematics** … Meanwhile, the
> standalone probability distribution `p(i, t)` is a **contingent**
> ingredient, and provides the model with its informational or
> '**epistemic**' content" ([B3] p.5).
>
> "**Epistemic axiom:** … This standalone probability distribution … is
> **contingent**, meaning that it can vary between runs of the model."
> ([B3] p.29.)

The weld reading — *the probability assignment is carried by the
description, not by the law* — is [B3]'s own tripartite split
(kinematical / nomological / epistemic), quoted.

**I-3. The standalone distribution is chart-relative.** **EXTENSION.**

[B3] indexes the contingency of `p` by **run or instantiation** (p.29,
quoted at I-2). v12 additionally indexes it by **which chart** — which
context-local description — is being written. That indexing is the atlas
postulate speaking; [B3] nowhere states it.

The extension is **ontologically free**, and this is worth recording:
because `p` is epistemic in [B3]'s own classification (I-2), making it
chart-relative does not touch his ontology, and therefore does not collide
with p.28's realist disclaimer (quoted at I-7). What the corpus has
*measured* about this object is BC2's finding that the **composite's
slice-indexed** distribution at an intermediate division event is
frame-relative (`bc/note-bc2-bell-two-frames.md` §5–§6, as rescoped by
`bc/LOG.md` #4).

### 1.2 The nomological layer — division events

**I-4. The dynamical axiom is the chart's transition data, defined only at
the division events.** **FAITHFUL.**

> "the laws of an indivisible stochastic process contain **only
> first-order transition probabilities** connecting target times `t` with
> conditioning times `t₀`" ([B3] p.9, eq. 18).
>
> "Note that **no assumption is made** here that the transition
> probabilities `p(i,t|j,t₀)` exist as part of the laws for **all**
> real-valued choices of `t₀`. Allowed conditioning times `t₀` are called
> **division events** for the given system, and, without any real loss of
> generality, are assumed to include an 'initial' time `0`." ([B3] p.9.)
>
> "**Dynamical axiom:** For arbitrary target times, and for conditioning
> times corresponding to **division events**, the model's dynamical laws
> consist of transition probabilities … At the level of the given model,
> the dynamical laws are **fixed features**." ([B3] p.29.)

The chart's law is *sparse in the conditioning slot and free in the target
slot* — "The target time `t`, by contrast, can be treated as a **free
variable**" ([B3] p.10). This asymmetry is what the lemma of §3 turns on.

**I-5. System-centricity is chart-relativity of the division-event
structure.** **FAITHFUL.**

> "**Division events are not global properties of the whole universe, but
> are system-centric**, just like various other kinds of spontaneous
> time-translation-breaking in physics. In practice, a system may have
> multiple exact division events, or they may be generated to an extremely
> good approximation through interactions with other systems, **after
> marginalizing over those other systems**." ([B3] p.10.)

This is the **germ of the atlas inside [B3]**: the nomological layer is
already indexed by *which system* is being described. What BC1 measured is
that the germ does not extend to a compatible family — the assignment is
not restriction-compatible across the subsystem lattice
(`bc/note-bc1-division-event-composition.md`, R1/R2/R4).

**I-6. The atlas — a context-indexed family of charts.** **EXTENSION.**

[B3] models the whole system as **one** indivisible process with definite
global configurations. Replacing that by a family of context-local
processes is paper 0 v2.1 T1's scope note 1, verbatim: "the **atlas move**
… is v12's own postulate, **not** derived from [B1–B3]". Nothing in [B3]
supplies it; nothing in [B3] is cited for it.

**I-7. Charts as ontologically autonomous.** **TENSION.**

[B3]'s side:

> "from a more fundamental perspective, **the system ultimately takes only
> one trajectory**, and if one knew that trajectory in detail, then
> probabilities would not strictly be needed in the first place" ([B3]
> p.11).
>
> "This interpretation has a **thoroughly realist orientation**, and does
> not entail parallel universes, nor does it involve **perspectival or
> relational notions of ontology**." ([B3] p.28.)

v12's side: paper 0 v2.1 T5′ — "What Fine/AB obstruct is a global
**context-independent catalogue of values** … **not** the existence of one
actual world or one actual configuration history. Barandes keeps definite
configurations at all times; v12 no longer contradicts that."

**Resolution adopted here:** the atlas is a family of **descriptions over
one configuration history**, never a family of histories. Read that way
the tension is discharged and I-3 costs nothing. Read the other way —
charts with autonomous ontologies — the recast contradicts [B3] p.28
directly, and this note does not take that reading.

**I-8. A division event is where the defect dies — on the actual
distribution.** **FAITHFUL.**

> "The only available Chapman-Kolmogorov equations (5) take the simple
> form `p(i,t) = Σⱼ p(i,t|j,t₀) p(j,t₀)`, which is just the **law of total
> probability**. … Equivalently, in matrix notation, `p(t) = Γ(t←t₀)
> p(t₀)`." ([B3] p.9, eqs. 19–20.)
>
> "Importantly, notice that the law of total probability (19) is
> **linear**" ([B3] p.9).

Applying eq. (20) at **two** of the model's own division events forces the
declared-law residual `D₂₁₀ = Γ(t←0) − Γ(t←t′)Γ(t′←0)` of paper 0 v2.1's
T2′ to annihilate the standalone distribution the model runs on. That is
not a v12 postulate: it is a two-line consequence of [B3]'s own equations,
proved and gated at §3 below. It is also the exact sense in which paper 0
§4's "division events = where the defect dies" is *[B3]'s* statement — for
the **declared-law** defect `D₂₁₀`, on the **actual** distribution.

**I-9. A division event is where the defect dies — as matrices.**
**TENSION.**

[B3]'s side:

> "Crucially, an indivisible stochastic process, as befits its name, will
> **not generally obey a divisibility condition** like (7) or (14)." ([B3]
> p.10.)

The recast's side: with the epistemic axiom read at full strength — the
standalone distribution "**can vary between runs**" while the dynamical
laws "are **fixed features**" ([B3] p.29, both quoted at I-2/I-4) — the
residual annihilates every distribution realizable across runs, and if
those span, `D₂₁₀ = 0` **as matrices**, i.e. exact divisibility **across
any two division events**.

**Resolution stated, not assumed:** the two are compatible, and the
reconciliation is informative. [B3]'s indivisibility is a statement about
times that are **not** division events — his eq. (22) discussion is
explicitly about trying to manufacture a leg `Γ̃(t←t′)` for a `t′` the law
does not serve (I-18). Across a **pair of division events** the framework's
own law of total probability leaves no room: **indivisibility lives
between division events, never across them.** The matrix form nevertheless
needs the spanning hypothesis, which [B3] does not state; the receipt
gates that the hypothesis is load-bearing (L2/L3) — and also that on the
BC2 model it is **not needed**, because the model's own declared `p(0)`
already witnesses the violation (G3).

### 1.3 The lift — Born, gauge, dilation

**I-10. The Born projection `B(U) = |U|^{∘2}` is [B3]'s eq. (25).**
**FAITHFUL.**

> "`Γᵢⱼ(t←0) = |Θᵢⱼ(t←0)|²`. Note that this formula is **not a postulate,
> but an identity**, and that the potential matrix `Θ(t←0)`, which will be
> called a **time-evolution operator** in what follows, is **not
> unique**." ([B3] p.11, eq. 25.)
>
> "One can then regard (25) as expressing the transition matrix `Γ(t←0)`
> as a **Schur-Hadamard factorization** of the complex-conjugated
> potential matrix `Θ̄(t←0)` with `Θ(t←0)` itself" ([B3] p.11, eq. 28).

The entrywise squaring that paper 0 v2.1 calls the *Born projection* is
[B3]'s dictionary, and his own word for the inverse operation is
"potential" — the electromagnetic analogy is his (p.12).

**I-11. `Δᴮ` as the primary interference invariant.** **EXTENSION.**

`Δᴮ(U₂,U₁) = B(U₂U₁) − B(U₂)B(U₁)` is paper 0 v2.1 T2′'s object. [B3]
names no such invariant. What he does assert is the phenomenon:

> "indivisible stochastic processes generically exhibit all the hallmark
> empirical features of quantum systems, including **interference**,
> decoherence, entanglement, and noncommutative observables" ([B3] p.2).

So the identification "interference = failure of the shadow to compose" is
v12's **naming and organization** of a phenomenon [B3] asserts, not a
result imported from him. W1′ (`v12/note-w1p-three-class.md`, TERMINAL at
LOG #7) separates `Δᴮ` from `D₂₁₀` and from `d_div` by exact
counterexample; this note keeps them separate (§3, gate G8).

**I-12. Unistochasticity is the shadow-of-lift statement.** **FAITHFUL.**

> "an `N × N` matrix is called **unistochastic** if its individual entries
> are expressible as the modulus-squares of the corresponding entries of
> an `N × N` unitary matrix. It follows that (64) is just the statement
> that the system's transition matrix `Γ(t←0)` can be taken to be
> unistochastic" ([B3] p.18).
>
> "an indivisible stochastic process can be viewed either as a
> unistochastic process itself, or (if a nontrivial dilation was required)
> as a **subsystem of** a unistochastic process. This statement is called
> the **stochastic-quantum theorem**." ([B3] p.19.)

"The chart's law is the Born shadow of an amplitude transport" is a
rewording of p.18; "the lift exists, after dilation if necessary" is
[B3]'s theorem, cited and not re-derived.

**I-13. The Schur-Hadamard gauge is the fibre phase freedom — over pairs
of configurations.** **FAITHFUL.**

> "the Schur-Hadamard product (27) of the time-evolution operator `Θ(t←0)`
> and a matrix of arbitrary, time-dependent phases `exp(iθᵢⱼ(t))` is a
> transformation of `Θ(t←0)` with **no physical effects**, and therefore
> corresponds to a genuine form of **gauge invariance**" ([B3] p.12,
> eq. 29); "`Θᵢⱼ(t←0) ↦ Θᵢⱼ(t←0) e^{iθᵢⱼ(t)}`" ([B3] p.12, eq. 30).
>
> "this form of gauge invariance is **not** equivalent to changing merely
> the relative phases of state vectors alone" ([B3] p.12, fn. 11).
>
> "To the author's knowledge, this kind of gauge invariance has not yet
> been described in the research literature, and is therefore a **new
> result**." ([B3] p.13.)

**The sharpening the recast owes:** the phases are indexed `(i,j)` — **one
`U(1)` per ordered pair of configurations, per time** — not one per
configuration. The base of the phase freedom is `C × C × T`, and [B3]
makes the pair-indexing explicit in the dilated version:

> "`V^I_{(ij)}(t)` are a set of `N²` unitary, `D × D` matrices, where each
> such unitary matrix as a whole is **labeled by a specific pair `(ij)` of
> configuration labels**" ([B3] p.27, eq. 106).

The word "fibre" is v12's here (it is [B3]'s at I-15); the content is his.
The base-of-the-fibration question is exactly where v12's own v1
formulation went wrong (LOG #2–#3), and [B3]'s text answers it: pairs, not
points.

**I-14. Fixing the unitary lift is a partial gauge fixing: the fibre
freedom does not act on the lifts.** **FAITHFUL.**

> "Note that a unitary time-evolution operator `U(t←0)` will **not
> generically remain unitary** under arbitrary Schur-Hadamard gauge
> transformations (30). Hence, writing a unistochastic transition matrix
> `Γ(t←0)` in terms of a unitary time-evolution operator `U(t←0)`
> corresponds to making a **gauge choice** — or, somewhat more precisely,
> to a **partial fixing of the gauge freedom** (30)." ([B3] p.19.)

Recast: the group of fibre phases is strictly larger than the subgroup
that preserves the amplitude lift's unitarity. Any construction that puts
a phase group on the lifts must first restrict to that stabilizer. This is
a standing constraint on W2b (paper 0 v2.1 §4: the projective-descent
question over the generated `⟨2,3⟩`), stated here as a fact about [B3]'s
text, not as a result about W2b.

**I-15. The Foldy-Wouthuysen gauge is the fibre frame over the time base —
and [B3]'s own bundle is flat.** **FAITHFUL.**

> "if `V(t)` depends nontrivially on time, and if one regards the system's
> Hilbert space at each moment in time as a **fiber over a
> one-dimensional base manifold** parameterized by the time coordinate
> `t`, then `V(t)` represents a **local-in-time, unitary transformation of
> each individual Hilbert-space fiber**" ([B3] p.20).
>
> "the Hilbert-space formulation of an indivisible stochastic process is
> ultimately a collection of **gauge-dependent quantities, or gauge
> variables**. In any physical theory, one does not typically try to
> assign gauge variables an ontological meaning." ([B3] p.20.)
>
> "The fact that one can set `H_V(t) = 0` for all `t` is a manifestation
> of the fact that the fiber bundle in this case, consisting of copies of
> the system's Hilbert space fibered over a one-dimensional base manifold
> parameterized by the time `t`, has **vanishing curvature**." ([B3] p.21,
> fn. 16.)

Recorded exactly: **[B3] himself computes the curvature of the only bundle
he builds, and gets zero** — necessarily, the base being one-dimensional.
This is not the statement LOG #2 killed (that was `H¹` of a two-chart
nerve, a different object), and it is not evidence about any other
carrier; it is the observation that no holonomy content lives in [B3]'s
own fibre-bundle language.

**I-16. Dilation is fibre enlargement — the base is fixed.** **FAITHFUL.**

> "for any integer `D ≥ 2`, one can freely **enlarge, or dilate, the
> Hilbert-space formulation** to a larger dimension `ND` by the following
> dilation transformation" ([B3] p.26, eq. 98).
>
> "a Hilbert-space formulation is merely a collection of mathematical
> tools … The indivisible stochastic process itself is ultimately defined
> by **a configuration space and a dynamical law that stand apart from any
> arbitrary choice of Hilbert-space formulation**." ([B3] p.25.)
>
> "whether or not one actually carries out this formal dilation of the
> Hilbert-space formulation, **the stochastic dynamics of the underlying
> indivisible stochastic process will still be the same**. Any emergent
> patterns … were always there all along" ([B3] p.28).

What grows under dilation is the **internal space `H_I` over each
configuration pair** (eq. 98 sends `Θ ↦ Θ ⊗ 1_I`, `Pᵢ ↦ Pᵢ ⊗ 1_I`,
`Pⱼ ↦ Pⱼ ⊗ P^I_γ`). The configuration space is untouched.

**I-17. Dilation as *chart* enlargement — the base grows.** **TENSION.**

The pin's phrase is "dilation = chart enlargement". On the chart's base
that reading is **contradicted by [B3] p.28**, quoted at I-16: the
underlying process, i.e. the chart, is unchanged. The only reading in
which the base grows is a **different** statement of his:

> "an indivisible stochastic process can be viewed either as a
> unistochastic process itself, or (if a nontrivial dilation was required)
> **as a subsystem of a unistochastic process**" ([B3] p.19).

There the chart at issue is the *larger* system's, and the original chart
is its **marginal** — which is a genuine enlargement of the base, and
which BC1 measured: the reduced processes are generically **not**
unistochastic (402 of 1,152 fail double stochasticity outright, 12 more
fail the polygon obstruction; `bc/note-bc1-…md` R5), so the two readings
are not interchangeable even in outcome.

**Correction adopted:** the recast says **"dilation = fibre enlargement"**
(I-16), and reserves "chart enlargement" for p.19's subsystem disjunct,
naming it as such. The pin's phrasing is superseded by this note.

**I-18. Eq. (22)'s interpolant is the would-be bridge, and
pseudo-stochasticity is the defect made visible.** **FAITHFUL.**

> "it might seem reasonable to try to define an intermediate transition
> matrix `Γ̃(t←t′) ≡ Γ(t←t₀)Γ⁻¹(t′←t₀)` … **at least if `Γ(t′←t₀)` is
> invertible**. … However, it turns out that a matrix `Γ̃(t←t′)` defined
> according to (22) will **generically fail to be a column stochastic
> matrix**, and, indeed, will typically have negative entries, and so will
> form a so-called **pseudo-stochastic matrix**." ([B3] p.10.)

[B3]'s own diagnosis of what goes wrong when one tries to restart at a
time the law does not serve *is* the weld's statement that the shadow does
not compose there. Measured datum, carried from BC2 and reproduced in this
unit's receipt (gate A4): on the Bell composite the interpolant's
hypothesis fails outright — the exact rank of `Γ(2←0)` over `K` is 18 or
9, **never 36** — so the pseudo-stochastic diagnosis is not even reached.

**I-19. Beables and emergeables are [B3]'s own base-carried / lift-only
split.** **FAITHFUL.**

> "In keeping with Bell's terminology, random variables will now be called
> **be-ables**, or beables … When the system is any given configuration
> `i`, each beable `A(t)` has a definite, underlying value `a(i,t)`."
> ([B3] p.15.)
>
> "**Observables that are not beables** are non-diagonal self-adjoint
> operators that correspond to emergent patterns that show up when systems
> interact with measuring devices, and will be called **emergeables**."
> ([B3] p.16.)

This is [B3]'s version of paper 0 v2.1 T1's scope note 2 — *"locally there
is no quantum **ontology**" is the claim; "locally no quantum
**mathematics**" is not* — written before v12 wrote it: what the chart's
base carries (diagonal, definite per configuration) versus what only the
lift carries (non-diagonal).

**I-20. One world.** **FAITHFUL.**

> "the system ultimately takes only one trajectory" ([B3] p.11); "a
> thoroughly realist orientation, and does not entail parallel universes"
> ([B3] p.28).

Paper 0 v2.1's T5′ is worded so as not to contradict this ("'One world'
survives; 'one counterfactual value-table' does not"). The recast inherits
that wording and adds nothing.

---

## 2. The marks, counted

| mark | count | identifications |
|---|---|---|
| **FAITHFUL** | **14** | I-1, I-2, I-4, I-5, I-8, I-10, I-12, I-13, I-14, I-15, I-16, I-18, I-19, I-20 |
| **EXTENSION** | **3** | I-3 (chart-relative `p`), I-6 (the atlas), I-11 (`Δᴮ` as the invariant) |
| **TENSION** | **3** | I-7 (autonomous charts), I-9 (matrix-form divisibility), I-17 (base enlargement) |
| **total** | **20** | — |

**The five identifications the pin names, adjudicated:**

| pin's phrase | outcome |
|---|---|
| division events = where the defect dies | **SPLIT**: I-8 FAITHFUL (vector form, forced by eqs. 19–20) + I-9 TENSION (matrix form, needs H-SPAN) |
| dilation = chart enlargement | **CORRECTED**: I-16 FAITHFUL as *fibre* enlargement; I-17 TENSION as base enlargement — the pin's phrase is superseded |
| Schur-Hadamard gauge = the fibre phase freedom | **FAITHFUL**, sharpened: the base is pairs `(i,j)`, not points (I-13) |
| unistochasticity = shadow-of-lift | **FAITHFUL** (I-12) |
| the epistemic axiom = chart-relative probability | **SPLIT**: I-2 FAITHFUL (the epistemic layer is separable) + I-3 EXTENSION (chart-indexing is v12's) |

---

## 3. The LTP lemma

The pin's third item: bc #4's M-1 incidental, formalized as a lemma
**about [B3]'s own framework**.

### 3.1 Statement

> **LEMMA (LTP-FORCING).** Let `M` be a model satisfying [B3]'s three
> axioms ([B3] p.29) with finite configuration space `C`, `|C| = N`. Let
> `0` and `t′` be two **division events** of `M` ([B3] p.9; `0` is one by
> [B3]'s own convention), and let `t` be any target time ([B3] p.10: the
> target time is a free variable). The dynamical axiom supplies `M` with
> the fixed column-stochastic matrices `Γ(t′←0)`, `Γ(t←0)` and `Γ(t←t′)`,
> and [B3]'s law of total probability (eqs. 19–20, p.9) holds at **both**
> conditioning times. Write
>
> `D₂₁₀ := Γ(t←0) − Γ(t←t′) Γ(t′←0)`
>
> for the **declared-law residual** of paper 0 v2.1's T2′ (not `Δᴮ`, not
> `d_div`). Then:
>
> **(a) Vector form, no extra hypothesis.** For every standalone
> distribution `p(0)` the model actually runs on, `D₂₁₀ p(0) = 0`.
>
> *Proof.* `p(t′) = Γ(t′←0) p(0)` and `p(t) = Γ(t←0) p(0)` by eq. (20) at
> the division event `0`; `p(t) = Γ(t←t′) p(t′)` by eq. (20) at the
> division event `t′`. Substituting the first into the third and
> subtracting the second gives `D₂₁₀ p(0) = 0`, using only associativity
> of the matrix action. ∎
>
> **(b) Matrix form, under H-SPAN.** If the standalone distributions
> admissible across runs span `ℝᴺ` — the epistemic axiom read at full
> strength ("contingent, meaning that it **can vary between runs**")
> against dynamical laws that "are **fixed features**" ([B3] p.29) — then
> `D₂₁₀ = 0` exactly, as matrices.
>
> **(c) The forcing (contrapositive of (a)).** If the model exhibits a
> target time `t` and an admissible `p(0)` with `D₂₁₀ p(0) ≠ 0`, then
> **`t′` is not a division event of that model**. No hypothesis beyond
> [B3]'s own eqs. (19)–(20) is used; H-SPAN is **not** needed for (c).

**Scope, engraved.** (a)–(c) concern the **declared** leg `Γ(t←t′)` that
the model's own dynamics supplies. They say nothing about whether *some*
other column-stochastic bridge exists (`d_div`), and nothing about `Δᴮ`,
which by W1′'s C+1 can be nonzero on a divisible process
(`v12/note-w1p-three-class.md`: `Δᴮ₀₀ = −4032/15625 ≠ 0` with
`K = S(−175/527)` stochastic and `K·B(U₁) = B(U₂U₁)`).

### 3.2 What is gated, and what is not

The proof of (a) uses exactly one non-trivial step, and the receipt gates
it formally rather than asserting it:

- **L1** — with all `2N² + N` entries **indeterminate** over `ℚ` at
  `N = 3`, `Γ₂₁(Γ₁₀ p₀) − (Γ₂₁Γ₁₀)p₀` is identically the zero polynomial
  vector: associativity of the matrix action, no property of
  stochasticity assumed.
- **L2** — **H-SPAN is load-bearing**, by exact separating instance:
  `D = [[1,−1],[−1,1]]` is nonzero yet annihilates `p = (1/2, 1/2)`. The
  vector form is therefore **strictly weaker** than the matrix form, and
  (b) genuinely needs the full-strength epistemic reading.
- **L3** — and spanning restores it: the same `D` fails to annihilate the
  point mass `δ₀`, so admitting the `N` point masses across runs already
  forces `D = 0`.
- **L4** (control) — a difference of two column-stochastic matrices has
  identically zero column sums, so `D₂₁₀ p(0)` always sums to zero: the
  violation is **cancelling mass**, and detection counts entries, never
  totals.

### 3.3 The gate: the forcing exhibited exactly on the committed BC2 model

**Provenance, declared.** The committed BC2 receipt prints **censuses, not
matrices** (`bc2_output.txt` SEC 6: supports, exact value censuses,
nonzero counts, column-support censuses, distinct-value counts; no
transition matrix appears entry by entry). The matrices are therefore
**not extractable** from the committed output. This unit **rebuilds** the
model from the singlet dictionary and the construction declared in the
committed receipt (read via `git show
f6d07ee:bc/code/bc2_two_frames_exact.py`), in its **own** field arithmetic
— `K = ℚ[x]/(8x⁴ − 8x² + 1) = ℚ(cos π/8)`, irreducibility certified
in-receipt (K1/K2), no code imported, no AST lift — and then **anchors the
rebuild against every number the committed receipt prints**.

**The anchor battery (9 anchors, all pass, exit-1 on failure).**

| gate | committed number reproduced |
|---|---|
| M1 | `U_prep` exactly orthogonal; `j0` column exactly `(0, 1/√2, −1/√2, 0)` |
| M2 | all 7 time-evolution operators exactly real orthogonal (1,296 inner products each) |
| M3 | `[U_A(a), U_B(b)] = 0` exactly at all 9 setting pairs |
| A1 | the exact singlet law `P(α,β) = (1 − αβ cos(a−b))/4` and both marginals `1/2`, both frames, all six setting pairs — 96 identities in `K` |
| A2 | the entire SP-A inventory, both frames: supports and exact value censuses of `p(1), p(2), p(3)` (incl. `{1/16: 4, 3/16±(1/8)√2: 2}`) and nonzero counts / column-support censuses / distinct-value counts of `Γ(1←0), Γ(2←0), Γ(3←0), Γ(3←2)` — 14 objects, 34 printed numbers |
| A3 | the divisibility census `(0, 0, 576, 576, 0, 576)` at SP-A…SP-F, **both frames** |
| A4 | the eq.-(22) ranks `(18,18), (18,18), (9,18), (9,18), (18,18), (18,18)`, never 36 |
| A5 | the committed §5.2 mismatch table, cell for cell: 36 differing-entry counts across six objects and six setting pairs |
| A6 | the basis-free certificate: `Pr[pointer B still ready]` at Alice's division event `= 1` in F1 and `= 0` in F2, all six setting pairs |

**The result.** With `t′ = 2` (the first measurement, a division event by
[B3] p.29's "division events are generated during a measurement process")
and `t = 3`, evaluated on the model's own declared `p(0) = δ_{j0}`:

| setting | frame | `‖r‖₀` of 36 | `D₂₁₀` differing of 1296 |
|---|---|---|---|
| SP-A (0°,45°) | F1 / F2 | 0 / 0 | 0 / 0 |
| SP-B (0°,135°) | F1 / F2 | 0 / 0 | 0 / 0 |
| **SP-C (90°,45°)** | F1 / F2 | **16 / 16** | **576 / 576** |
| **SP-D (90°,135°)** | F1 / F2 | **16 / 16** | **576 / 576** |
| SP-E (0°,0°) | F1 / F2 | 0 / 0 | 0 / 0 |
| **SP-F (45°,45°)** | F1 / F2 | **16 / 16** | **576 / 576** |

**The 16-of-36 witness, in full** — SP-C, frame F1 = (prep, A, B),
`rᵢ = pᵢ(3) − [Γ(3←2) p(2)]ᵢ`, exact in `ℚ(√2)`:

```
   4 (00|++) −1/32−(1/32)√2    13 (01|++)  1/32−(1/32)√2
   5 (00|+−) −1/32+(1/32)√2    14 (01|+−)  1/32+(1/32)√2
   7 (00|−+)  1/32+(1/32)√2    16 (01|−+) −1/32+(1/32)√2
   8 (00|−−)  1/32−(1/32)√2    17 (01|−−) −1/32−(1/32)√2
  22 (10|++) −1/32−(1/32)√2    31 (11|++)  1/32−(1/32)√2
  23 (10|+−) −1/32+(1/32)√2    32 (11|+−)  1/32+(1/32)√2
  25 (10|−+)  1/32+(1/32)√2    34 (11|−+) −1/32+(1/32)√2
  26 (10|−−)  1/32−(1/32)√2    35 (11|−−) −1/32−(1/32)√2
```

Four distinct values, `±1/32 ± √2/32`, each occurring four times (G5): the
violation is **irrational**, so it cannot be an artefact of rational
truncation, and it sums to zero exactly (G2), as L4 requires.

**The substantive gates.**

- **G1** — the residual is exactly the `j0` column of the matrix residual
  in all twelve cells: the model's `p(0)` is a point mass, so nothing is
  hidden by the choice of distribution.
- **G3** — vector and matrix violations coincide in 12 of 12 cells. **A
  reported negative:** this model supplies **no** cell where the matrix
  residual is nonzero and the vector residual vanishes, so the abstract
  separation L2 exhibits is not realized here — and the forcing therefore
  **needs no H-SPAN** on this model.
- **G4** — `16 × 36 = 576`: the vector count and the committed matrix
  count are the same fact, seen once per column.
- **G6** — **the forcing fires.** At SP-C, SP-D and SP-F, in both frames,
  [B3]'s own eqs. (19)–(20) at the division events `0` and `t′ = 2` are
  contradicted by the model's own declared law on the model's own declared
  `p(0)`. By lemma (c), `t′ = 2` **is not a division event** of those
  models — at exactly the place [B3] p.29 says a measurement generates
  one. **The denial is forced by the framework, not imposed from
  outside.**
- **G7** — bc #4's M-1 biconditional ("legitimate division event ⟺ the
  process divides at it") is the **model-level corollary**, not the lemma.
  The lemma proves one direction. The converse holds *here* because the
  declared leg `Γ(3←2)` is column-stochastic at every setting pair (M5),
  and is **not** claimed in general.
- **G8** — the three defects stay distinct. On this model `D₂₁₀` **equals**
  `Δᴮ(Θ(3←2), Θ(2←0))` because the amplitude propagators compose exactly
  (M4: `Θ(3←0) = Θ(3←2)Θ(2←0)` at all 1,296 entries, all twelve cells), so
  the 576/16 counts are simultaneously a declared-law residual and a
  Born-shadow defect. The **existential** object `d_div` is **not decided
  here** (no LP is run; that census is U1's and BC1's), and by W1′'s C+1
  `Δᴮ ≠ 0` does not imply `d_div ≠ 0`.

### 3.4 What the lemma changes, and what it does not

It changes the reading of "indivisible": **indivisibility is a property of
the intervals between division events, never of the step across a pair of
them.** A model that declares a division event where its own law fails to
compose on the actual distribution is not exhibiting indivisibility; it is
inconsistent with eq. (20), and the framework's own remedy is to withdraw
the division event.

It does **not** show [B3] inconsistent. [B3] states no model. What it
shows is that the natural [B3] model of a two-measurement Bell experiment
— built by BC2 to [B3]'s own prescriptions — cannot keep both the
measurement-generated division event of p.29 and the law of total
probability of p.9 at three of six declared setting pairs, and that the
framework itself decides which one goes.

---

## 4. The survives / doesn't table

Which [B3] claims survive globalization — the atlas move plus the demand
that the charts be descriptions of one world. Every row is carried by a
**committed** citation; nothing below is re-derived here.

| # | [B3] claim, page-cited | under globalization | carrier |
|---|---|---|---|
| **C1** | The configuration space is a fixed feature, one set per model (p.29) | **SURVIVES.** The atlas varies the *description*, not `C`; BC2 runs both frames and all six setting pairs on one fixed `C` of 36 configurations | BC2 §2 |
| **C2** | Division events are system-centric (p.10) — hence a wing has its own description | **SURVIVES at wing-local grain.** Each wing's marginal, evaluated at *that wing's own* division event, is exactly frame-invariant, at every setting pair | BC2 §7 E3a |
| **C3** | The measuring device ends in a measurement-outcome configuration with Born-rule probability (p.16) | **SURVIVES exactly.** `Γ(3←0)` and `p(3)` agree entry by entry across frames; 96 exact singlet identities; paper 8's admissible form 1 holds exactly, not approximately | BC2 §4, §8; bc #4 M-3 |
| **C4** | The composite's slice-indexed joint at an intermediate division event | **DOES NOT SURVIVE.** At every setting pair with two different settings, no permutation of the 36 configurations carries F1's specified content onto F2's — 16 of 16 cells empty, four grains, two time correspondences, search complete | BC2 §6.1; rescoped by bc #4 |
| **C5** | Division events are assignable system by system (p.10) | **DOES NOT GLUE.** GS1 restriction-compatibility fails 527/1,296 (marginal) and 361/1,296 (conditional); GS2 gluing fails 85/77 in the population though it held on all eight hand-picked models; **10 slices admit only the empty assignment** | BC1 R1, R3, R4 |
| **C6** | "Division events are generated during a measurement process" (p.29) | **DOES NOT SURVIVE AS STATED** on a composite where the declared law fails to compose: the framework's own eqs. (19)–(20) force denying the division event at 3 of 6 setting pairs, both frames | bc #4 M-1; **this unit's §3** (G6) |
| **C7** | `Γ` can be taken unistochastic; a subsystem may need a dilation (pp.18–19) | **SURVIVES for the composite, FAILS for the parts.** 21 of 32 composite instances certified with the model's own unitary exhibited; of 1,152 reduced processes, 402 are not doubly stochastic and 12 more fail the polygon obstruction | BC1 R5 |
| **C8** | The refusal to fix a Kolmogorov tower makes the content minimal (pp.10–11) | **SURVIVES as a fact about the content; buys nothing.** The objects that fail to correspond are the *sparsest* content the framework has — single-time distributions at division events, division-event transition matrices, and the induced order of the division-event set | BC2 §9 |
| **C9** | Eq. (22)'s interpolant, "at least if `Γ(t′←t₀)` is invertible" (p.10) | **HYPOTHESIS FAILS** on the Bell composite: exact rank 18 or 9, never 36, both frames, every setting pair | BC2 §4; reproduced here at A4 |
| **C10** | "locality in space is preserved at the cost of non-Markovianity" (p.29, deferred to future work) | **NOT TESTED.** No locality claim and no Bell-inequality claim is made or used anywhere in BC or in this unit | BC2 §10 |
| **C11** | The stochastic-quantum theorem (p.19) | **NOT UNDER TEST.** Proven mathematics; excluded by the programme's founding scope | `bc/LOG.md` #1 |
| **C12** | "a thoroughly realist orientation … no perspectival or relational notions of ontology" (p.28) | **SURVIVES the recast**, on the resolution adopted at I-7: the atlas is a family of descriptions over one configuration history | this note §1, I-7; paper 0 v2.1 T5′ |

**Reading of the table.** Five rows survive (C1, C2, C3, C8, C12), four
fail (C4, C5, C6, C7-for-the-parts), one hypothesis fails outright (C9),
two are untested by construction (C10, C11). The line separating them is
sharp and is the same line in every case: **everything indexed to one
system at its own division events survives; everything that requires a
composite's description at a shared intermediate time does not.**

---

## 5. The honest close: what [B3] is a theory of, under the recast

**This is v12's READING, not [B3]'s claim.** [B3] defers the relativistic
and Bell-theorem treatment to future work in its own words — "These
theorems will be addressed in detail in future work" (p.29) — and this
note tests the apparatus as published, not a successor.

Under the recast, **[B3] is an exact and complete theory of one chart and
its defect**:

1. **A chart** — a fixed configuration space, definite at all times, with
   an ordinary contingent probability distribution over it (I-1, I-2).
2. **A sparse law on that chart** — transition matrices from division
   events to arbitrary target times, and nothing between them (I-4).
3. **A complete account of the chart's amplitude lift** — the dictionary
   `Γ = |Θ|²` as an identity rather than a postulate, the two gauge
   freedoms that make the lift non-unique (phases per configuration pair;
   unitary frames per time), the partial gauge fixing that unitarity is,
   and the dilations that enlarge the lift's fibre without touching the
   chart (I-10, I-12, I-13, I-14, I-15, I-16).
4. **A diagnosis of what goes wrong when the chart is restarted at a time
   its law does not serve** — the pseudo-stochastic interpolant (I-18).

What it is **not**, under the recast and on the committed measurements: a
**global world-process**. A global world-process would have to supply
three things the corpus has measured the framework not to supply:

- **(i)** a frame-independent slice-indexed joint for a composite across
  spacelike separation — BC2: no relabelling of any kind relates the two
  frames' specified content at unequal settings (C4);
- **(ii)** a restriction-compatible division-event assignment across the
  subsystem lattice — BC1: ten slices where only the empty assignment is
  consistent (C5);
- **(iii)** a division-event set its own law of total probability
  tolerates wherever a measurement occurs — **this unit**: the forcing
  fires at 3 of 6 setting pairs, both frames (C6).

Each of the three is *local to a joint*: (i) the joint between two wings
at one time, (ii) the joint between a system and its parts, (iii) the
joint between two successive conditioning times of one composite. The
recast's summary sentence, stated as a reading:

> **[B3] is a theory of charts and of the defect that appears when charts
> are joined. Every one of its successes is a statement about one chart;
> every one of the committed failures is a statement about a joint.**

That is also the honest measure of what the atlas postulate buys. It does
not rescue the joints — the corpus's three measurements are of the joints
failing, and re-describing a global process as an atlas does not make a
non-existent global section exist. What it buys is **bookkeeping**: it
names the surviving objects (chart-local content, at chart-local division
events) as the primitives, and demotes the failing objects (composite
slice-joints, cross-lattice assignments, cross-division-event composition)
from things the theory has to things the theory has to *explain the
absence of*. Whether that bookkeeping is worth its postulate is not
settled by this unit; W4′ asks whether the three failures are one
invariant or three, and the U2 precedent (assumed-one, measured-three)
stands as the named warning.

---

## 6. What this note does not claim

- Nothing about nature. Every statement is about [B3]'s formal apparatus,
  on the committed toy models.
- No Bell-inequality claim, no locality claim, no covariance claim. BC2
  owns the frame question; it is cited as data and never re-derived here.
- Nothing about [B3]'s equivalence theorem, which is not under test.
- Nothing about existential divisibility `d_div`: no LP or Farkas search
  is run in this unit. The lemma decides the **declared-law** residual
  only.
- Nothing about `Δᴮ` beyond the identification at G8: on this model the
  two objects coincide because the amplitude propagators compose; in
  general they do not, per W1′ C+1.
- No claim that the atlas move is correct, useful, or forced. It is a
  postulate (I-6), it is marked as such at every joint, and §5's reading
  of what it buys is a reading.
- No claim about whether [B3] *could* be given a formulation in which the
  joints survive. [B3] p.29 defers exactly those questions.

---

## 7. Import ledger

| item | status | home |
|---|---|---|
| The three axioms; "division events are generated during a measurement process"; the kinematical/epistemic/dynamical split | **[IMPORTED, verbatim]** | [B3] p.29 |
| Division events; the initial time 0; the free target time; system-centricity | **[IMPORTED, verbatim]** | [B3] pp.9–10 |
| Eqs. (19)–(20), the law of total probability, and its linearity | **[IMPORTED, verbatim]** | [B3] p.9 |
| Indivisibility; eqs. (22)–(23); the pseudo-stochastic interpolant; fn. 7 | **[IMPORTED, verbatim]** | [B3] p.10 |
| The refusal to fix a Kolmogorov tower / realizer; "only one trajectory" | **[IMPORTED, verbatim]** | [B3] pp.10–11 |
| Eq. (25) as an identity; non-uniqueness of `Θ`; the Schur-Hadamard factorization | **[IMPORTED, verbatim]** | [B3] p.11 |
| Schur-Hadamard gauge transformations (29)–(30); fn. 11; the "new result" claim | **[IMPORTED, verbatim]** | [B3] pp.12–13 |
| The dictionary (39); the Born rule (46); beables; emergeables; measurement-outcome configurations | **[IMPORTED, verbatim]** | [B3] pp.14–16 |
| Stinespring dilation to unitarity; unistochasticity; the stochastic-quantum theorem; unitarity as partial gauge fixing | **[IMPORTED, verbatim]** | [B3] pp.18–19 |
| Foldy-Wouthuysen gauge (74); gauge variables and ontology; fn. 16's vanishing curvature | **[IMPORTED, verbatim]** | [B3] pp.20–21 |
| Dilations (98)–(106); the pair-labelled internal unitaries; "the stochastic dynamics … will still be the same" | **[IMPORTED, verbatim]** | [B3] pp.25–28 |
| The realist / non-perspectival disclaimer; the deferral of Bell | **[IMPORTED, verbatim]** | [B3] pp.28–29 |
| BC2's model, its two frames, the six setting pairs, and every number in §3.3's anchor table | **[CITED, COMMITTED, and REPRODUCED in this unit's own arithmetic]** | `bc/note-bc2-bell-two-frames.md` @ cbb7279; `bc/code/bc2_output.txt` @ f6d07ee |
| bc #4's M-1 (the LTP violation at SP-C/D/F), M-2, M-3 | **[CITED, COMMITTED]** | `bc/LOG.md` #4 @ f6d07ee |
| BC1's C-OBSTRUCTION: GS1/GS2/GS3 censuses, the ten empty-only slices, R5's reduced-process screen | **[CITED, NOT DUPLICATED]** | `bc/note-bc1-division-event-composition.md` @ 42d8610 |
| T1's scope notes, T2′'s three defects, T3′, T5′, and the W-unit statements | **[IMPORTED, verbatim]** | `v12/relativistic-isp-v12-paper0-the-weld.md` v2.1 |
| T3′'s theorem **statement** (records ⇒ `D₂₁₀ = 0` on the record algebra) — cited as a statement, not a result | **[CITED, PIN ONLY]** | `v12/note-w3p-records-kill-defect-pin.md` |
| `Δᴮ ≠ 0` does not imply indivisibility (C+1); the `Δᴮ`/`D₂₁₀`/`d_div` separation | **[CITED, TERMINAL]** | `v12/note-w1p-three-class.md` (LOG #7) |
| The lemma, its proof, the H-SPAN analysis, the model rebuild, and every number in §3.3 | **[THIS UNIT]** | `v12/code/w5_ltp_lemma_exact.py` |

---

## 8. Caps

- **One [B3] paper.** The recast is of [B3] as published; [B1] and [B2]
  are cited by paper 0 and are not recast here.
- **One model in the gate.** `|C| = 36`, six declared setting pairs, two
  frame orderings, `t′ = 2`, `t = 3`. The lemma is general; its
  exhibition is not.
- **The model is rebuilt, not lifted.** The committed receipt prints no
  matrices, so the matrices could not be extracted; the rebuild follows
  the construction declared in the committed source (read via `git show`)
  in this unit's own arithmetic and is anchored against 9 gates covering
  every printed number the committed receipt reports for these objects.
  **Declared:** a printed number the committed receipt does not report
  cannot be checked by this route, and none is claimed.
- **No LP.** `d_div` is not decided. No Farkas certificate, no simplex.
- **No frame claim.** BC2's search, its escape battery and its verdict are
  cited, never re-run; A5/A6 reproduce its *numbers* as anchors on the
  rebuild, not as re-derivations of its verdict.
- **Retrodictive matrices are not computed** (BC2's cap, inherited).
- **The mark assignments are judgements about two texts**, made by this
  unit and open to a hostile round; the quotes are verbatim and
  page-cited so that each judgement can be checked against its evidence.

---

## 9. Files

- `v12/note-w5-barandes-recast.md` (this note)
- `v12/code/w5_ltp_lemma_exact.py`
- `v12/code/w5_output.txt`
- `v12/note-w5-barandes-recast-pin.md` (the pin; superseded on one point —
  see I-17)
