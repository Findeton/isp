# v11 L-1 — THE FINITE-STOCHASTIC LORENTZ NO-GO, RESTATED

**Status:** LEMMA, STRICT, 2026-07-27.  Unit L-1 of Phase I
(`note-L1-L0-boundary-lemmas-pin.md`; paper 0 §7, §9b).  This is a
**restatement lemma**: it takes a committed corpus theorem, restates
it in v11's stratum language, and derives what it forbids.  It
asserts nothing new about the generated record.  Receipt:
`code/L1_L0_text_anchors.py` → `code/L1_L0_anchors_output.txt`.

---

## 1. The source, verbatim

Source file:
`/Users/felixrobles/workspace/isp/v3/relativistic-isp-v3-paper8-continuum-qft-reconstruction-no-go.md`.

**Lemma 2.3 (lines 110–114), verbatim:**

> Let `K:X\to X` be a stochastic map on a finite set, represented by a
> row-stochastic matrix. If `K` has an inverse `L` that is also stochastic, then
> `K` is a permutation matrix.

**Corollary 2.4 (lines 132–137), verbatim:**

> An exact covariance action by invertible stochastic maps on a fixed finite
> configuration set can only act by permutations. Therefore a nontrivial Lorentz
> boost cannot be represented in this paper as an exact stochastic automorphism
> of one fixed finite regulator state space.

**The admissible remainder (lines 139–147), verbatim:**

> The only admissible finite covariance statements in this paper are:
>
> 1. equality or convergence of declared finite-battery statistics for sampled
>    Lorentz-related tests;
> 2. projective compatibility of different finite batteries approximating
>    Lorentz-related continuum tests;
> 3. an imported continuum covariance representation listed as enrichment.
>
> None of these is a finite-regulator proof of full Lorentz covariance.

The catalog carries the graded entry at
`note-v11p0a-reproduction-catalog.md` §1.3 (lines 289–333), grade
**[THEOREM]**, with presuppositions recorded as *"a finite
configuration set and row-stochastic maps.  **Nothing else — no
background metric, no action, no Hilbert space.***"

---

## 2. The source proof, reproduced

The proof of Lemma 2.3 is short, so L-1 is re-derived rather than
imported.  The source proof (lines 116–130) runs:

Write `KL = I`.  For `x ≠ z`, `0 = (KL)_{xz} = Σ_y K_{xy} L_{yz}`.
Every summand is nonnegative, so whenever `K_{xy} > 0` one must have
`L_{yz} = 0` for all `z ≠ x`; since row `y` of `L` sums to one, this
forces `L_{yx} = 1`.  If a row of `K` had two positive entries
`K_{xy₁}` and `K_{xy₂}`, then rows `y₁` and `y₂` of `L` would both be
the point mass at `x`, making `L` non-invertible.  Hence every row of
`K` has exactly one positive entry, equal to one, and invertibility
forces distinct rows to hit distinct columns.  `K` is a permutation.

The argument uses only: finiteness of the configuration set,
row-stochasticity of both matrices, and `KL = I`.  It uses no metric,
no time parameter, no Hilbert space, and no property of the Lorentz
group.  It therefore transfers to v11's grain with the configuration
set replaced and nothing else changed.

---

## 3. L-1, at v11's cut grain

**Setting (paper 0 §3, §4).**  KINEMATICS supplies the generated
causal order and its antichain cuts.  THE LAW is the sparse family
`Γ(cut′ ← cut)` of row-stochastic matrices, conditioned only at
division events, and division events are renewals (paper 0 §4
[POSIT]).  Let `C` denote the renewal-grain configuration space.
Paper 0 §4 grades its fixedness **[THEOREM-GRADE CONVERGENCE]**
(:143–150), not [POSIT]; this note **consumes** that clause as a
hypothesis and does not verify it, which is a conservative reading
of paper 0's own grade and is marked here as this note's own.  On
that hypothesis `C` is **one** finite set, fixed and identical
across runs.

**L-1 (a) — the imported half, re-derived at v11's grain.**
*Let `C` be finite.  Let `G` be a group and `g ↦ R_g` an exact
covariance action on `C` by stochastic maps: each `R_g` is
row-stochastic on `C`, `R_e = I`, and `R_g R_h = R_{gh}`.  Then every
`R_g` is a permutation matrix of `C`.*

*Proof.*  `R_g R_{g⁻¹} = R_e = I` and `R_{g⁻¹}` is stochastic, so
`R_g` is an invertible stochastic map with stochastic inverse.
Lemma 2.3 applies verbatim (§2 above).  ∎

This is v3 paper 8 Corollary 2.4's first sentence, with `X` replaced
by `C` — and with one addition, marked.  Cor 2.4 hypothesizes
*invertible* stochastic maps; L-1(a) hypothesizes a **group action**
and **derives** invertibility from `R_g R_{g⁻¹} = R_e = I`.  That is
a mild generalization **[V11-STEP]**, not a pure restatement: it
covers covariance actions that were never announced as invertible.
The covariance action is whatever action a
v11 covariance claim would exhibit — the conjugation form
`Γ(g·cut′ ← g·cut) = R_g Γ(cut′ ← cut) R_g⁻¹` is one instantiation
and is not required by the lemma.

**L-1 (b) — the boost step. [V11-STEP]**
*If `G` contains a one-parameter boost subgroup isomorphic to `(ℝ,+)`,
the restriction of `R` to that subgroup is trivial: `R_b = I` for
every boost `b`.*

*Proof.*  By (a) the image lies in `Sym(C)`, a finite group.  `(ℝ,+)`
is divisible, so its homomorphic image is a divisible subgroup of a
finite group, hence trivial.  ∎

**Marking.**  (b) is **not** in the source text.  v3 paper 8 asserts
the conclusion *"a nontrivial Lorentz boost cannot be represented …
as an exact stochastic automorphism"* directly, without spelling out
the step from *"only permutations"* to *"only the identity"*.  (b)
supplies that step at v11's grain and is marked as v11's own, not as
an import.  It is **weaker and more precise** than the source's
literal sentence, not stronger: the source writes that a boost
*"cannot be represented"*, whereas (b) concludes `R_b = I` — a boost
**is** representable in the group-action setting, but only trivially.
(b) is therefore a sharpening and a correction of an imprecise
sentence, not an extension of it.

**L-1, as a single sentence.**  *Because THE LAW is a family of finite
row-stochastic matrices on one fixed finite renewal-grain
configuration space, exact Lorentz covariance implemented by
stochastic automorphisms of that space is excluded by the argument of
v3 paper 8 Lemma 2.3 / Corollary 2.4; the most v11 may claim is a
statistical or approximate covariance statement of one of paper 8's
three admissible kinds.*

Paper 0 already states the bound it takes from this lemma
(§7, lines 266–277), verbatim:

> v11 may expect at most
> statistical/approximate Lorentz invariance at renewal grain,
> never exact covariance

and

> Any v11 claim of exact finite covariance
> is pre-refuted by this lemma and forbidden.

L-1 discharges those two sentences.  They are now lemma, not posit.

---

## 4. The collision with paper 0 §4, and its resolution

**The collision.**  Paper 0 §4 (lines 143–150) grounds the whole
re-founding on the claim that Barandes' kinematical axiom is

> because renewals reset
> to the root: the configuration space at division events is small,
> fixed, and identical across runs.

That is *exactly* the hypothesis of Corollary 2.4.  The catalog
states the collision plainly (§1.3(e), lines 322–333): Cor 2.4 says
that **on exactly such a space, no nontrivial boost can act as an
invertible stochastic map**, and records it as *"a **binding
constraint that paper 0 does not currently carry**"*.

**The resolution, in three parts.**

1. **The law is not required to be invertible.**  Cor 2.4 bites on a
   putative *covariance action*, not on `Γ` itself.  Nothing in paper
   0 asks `Γ(cut′ ← cut)` to have a stochastic inverse; [B3]'s own
   interpolant test ([B3] eqs. 22–23, paper 0 §2) is the observation
   that `Γ⁻¹` is generically pseudo-stochastic.  The renewal-grain
   fixed configuration space and the finite-stochastic no-go are
   therefore compatible; what dies is exact covariance, not the
   posit.

2. **The two non-invertibilities are the same object read twice.**
   The catalog's reading (§1.3(e), lines 331–333), verbatim:

   > the very non-invertibility that Cor
   > 2.4 treats as the obstruction to covariance is what Barandes treats as the
   > signature of indivisibility.

   and again at §7 rank 2 (lines 3141–3143), verbatim:

   > the non-invertibility Cor 2.4 treats as the obstruction to covariance is
   > the same non-invertibility Barandes treats as the signature of
   > indivisibility.

   This is a **reframing, not a theorem**.  The catalog carries it as
   `[MY READING]`; L-1 carries it at the same grade.  No v11 text may
   promote it.  Establishing that the *same* matrices witness both
   would be a result, and it is not claimed here.

3. **The surviving target is statistical, and it has its own gate.**
   Paper 8's admissible list (§1 above) permits sampled-battery
   statistics.  The catalog's existence proof that such a target is
   *achievable somewhere* is §1.5 (lines 365–394): sprinkled division
   events are statistically Lorentz-invariant, `s²` boost-invariant to
   `10⁻⁹⁷`, no frame recoverable, the arrow reading the frame-invariant
   causal order at `0/3200` mismatches.  **That result presupposes what
   v11 exists to generate** — the catalog records its presupposition as
   *"**a background Minkowski space to sprinkle into**"* — so it proves
   the weaker target is not vacuous, and proves nothing about v11's
   carrier.

   And the weaker target is itself gated.  Catalog §1.6(e) (lines
   423–428), verbatim:

   > v11's crystals are finite-valency by construction, so BHS says their renewal
   > sublattice **cannot** be statistically Lorentz-invariant in the sprinkling
   > sense.  U4 must therefore test a *weaker* covariance (order-level, per
   > P-Lor) and say so in advance — otherwise it will manufacture a false
   > negative.

   **The ladder v11 stands on, each rung with its grade.**

   1. **Exact stochastic covariance** — **excluded by L-1** (§3).
      Grade: **[THEOREM]** at the source, re-derived here.
   2. **Sprinkling-grade statistical covariance on a finite-valency
      generated carrier** — grade **[MY READING]**.  The BHS theorem
      itself is **[NO-GO, narrow scope]** (catalog §1.6(c)), but the
      *application* quoted just above is catalog §1.6(e), which the
      catalog grades **[MY READING]**; this note inherits the
      application's grade, not the theorem's.  Two steps are
      unproved.  **(i) Embedding.**  BHS presupposes a Poisson
      sprinkling *into Minkowski* (catalog §1.6(d)); v11's generated
      carrier has no embedding into Minkowski, so the theorem's
      hypothesis is not exhibited on it.  **(ii) Graph versus point
      set.**  BHS blocks Lorentz invariance of a *finite-valency
      graph*; it does not block Lorentz invariance of the point set
      the graph is built on.  The step from the first to the second
      is nowhere made in the corpus.  The committed corpus fact that
      actually bears on a crystal is weaker, and is a measurement,
      not a no-go: catalog §1.5(a) (:368–369) records that
      *"a regular lattice **is** frame-recoverable"* — grade
      **[MEASURED]**.  That is what a regular generated carrier must
      expect, and it is not BHS.
      **The catalog is internally inconsistent on this rung, and
      this note inherits neither voice**: §1.6(e) grades the
      application **[MY READING]**, while §7 rank 5 (:3179–3180)
      writes that sprinkling-grade covariance is *provably*
      unavailable on v11's finite-valency crystals.  Until a v11
      unit settles it, rung 2 is carried at the weaker grade and is
      **undecided**, not excluded.
   3. **Order-level covariance** (P-Lor) — **untested on a generated
      carrier.**  The corpus does hold order-level receipts, but on
      other carriers: `v7/note-C2-covariance-premise-deferral.md`:21
      (receipt `c2` — on a finite 1+1 Minkowski sample the causal
      order is invariant under a boost at rapidity `0.9`) and catalog
      §1.7 (:438–439 — a boost at rapidity `0.8` leaves the order and
      link skeleton bit-identical, on a sprinkling).  Neither carrier
      is generated.

   **Where the rungs sit in paper 8's admissible list.**  Rung 2 is
   paper 8's admissible form 1 (declared finite-battery statistics
   for sampled Lorentz-related tests).  Paper 8's form 2 (projective
   compatibility of different finite batteries) is **not** touched by
   the BHS block — it constrains how batteries at different
   refinements cohere, not whether a finite-valency graph can be
   Lorentz-invariant — so it remains available to U4, and §5 records
   that L-1 does not forbid it.  Paper 8's form 3 (imported continuum
   covariance) remains available as **enrichment** only.  **Rung 3 is
   not on paper 8's list at all.**  Order-level covariance is a
   statement about the generated causal order, not about declared
   finite batteries and not about a continuum representation; it is a
   **fourth form, outside paper 8's three**, and its admissibility is
   v11's to argue when U4 runs.  L-1 neither supplies that argument
   nor forbids the form.

   L-1 forbids rung 1.  It does not decide rung 2, it does not
   license rung 3, and it does not close paper 8's forms 2 and 3.

   Paper 0 §7 (:272–275) attaches to its bound the clause that
   statistical/approximate covariance at renewal grain is *"precisely
   the form U4 tests"*.  This ladder **narrows** that clause: the
   sprinkling-grade reading of it is rung 2, whose availability is
   undecided, and the order-level reading is rung 3, which is outside
   paper 8's list.  The routing of that narrowing into paper 0 is
   **deferred to the Phase-I-end single edit pass**; no paper 0 text
   is changed by this note.

---

## 5. Scope guard — what L-1 does NOT forbid

Stated so that no later unit reads the lemma wider than it is.

- It does **not** forbid a permutation action.  Discrete symmetries of
  `C` acting by permutation matrices are untouched; Cor 2.4's
  conclusion is *"can only act by permutations"*, which is a
  restriction, not an emptiness.
- It does **not** forbid covariance implemented by **non-invertible**
  stochastic maps — but the loophole is narrower than it reads: inside
  a *group* action L-1(a) **derives** invertibility, so what actually
  escapes is a covariance carried by a semigroup or by a non-group
  action, not a non-invertible map inside a group action.
- It does **not** forbid covariance acting on the **order** rather
  than on configurations.  Catalog §1.6 records the order-level leg
  (P-Lor) as *reduced*, not blocked.
- It does **not** forbid paper 8's admissible item 2, projective
  compatibility of different finite batteries.  That form survives
  both L-1 and the BHS block (§4(3)) and stays on the table for U4.
- It does **not** forbid a covariance representation on a projective
  limit or a continuum completion.  Paper 8's admissible item 3 lists
  exactly that, as **enrichment**, and paper 8's own Lemma 2.2 (the
  layer-ledger criterion, lines 95–99) forbids re-quoting a theorem
  proved at the enriched matching layer as a *Gamma-only
  reconstruction theorem* — the source's phrase.
- It does **not** say anything about whether v11's records *are*
  Lorentz-covariant in any weaker sense.  L-1 is a prohibition on
  claims, not a measurement.

---

## 6. Design constraints on U1 and U4 language

The lemma's operational content, written as constraints on wording so
that a unit cannot violate it by accident.

**Binding on U4 (the relativity test, Phase III).**

- **C1.** No U4 result may be stated as *exact*, *full*, or
  *automorphic* Lorentz covariance of the renewal-grain law.  Any
  such phrasing is pre-refuted by L-1 and must be rewritten before it
  is committed.
- **C2.** U4's target is named in advance, **and its form is named
  with it.**  If the target is one of paper 8's three admissible
  forms, U4 says which.  If the target is **order-level** covariance,
  U4 states that this is a **fourth** form, outside paper 8's list
  (§4(3)), and argues its admissibility in the same text — L-1 does
  not supply that argument.  A sprinkling-grade target (paper 8's
  form 1) may be pre-registered, but only with the BHS application's
  grade attached: **[MY READING]**, undecided on a generated carrier,
  expected-to-fail *if* catalog §1.6(e)'s reading holds.  Paper 8's
  form 2 (projective compatibility) is untouched by the BHS block and
  remains available.
- **C3.** A negative U4 result at sprinkling grade is **not** evidence
  against v11.  It is what catalog §1.6(e)'s BHS reading predicts —
  a **[MY READING]**, not a theorem on this carrier (§4(3)) — and it
  must be reported with that reading and its grade attached, or it
  manufactures a false negative.
- **C4.** Any covariance claim states, separately, (i) what acts,
  (ii) on what set, (iii) whether the acting maps are invertible.
  A claim missing any of the three is not evaluable against L-1.

**Binding on U1 (the census, Phase I).**

- **C5.** U1's interpolant arm and L-1 examine the **same** algebraic
  fact — the failure of a stochastic matrix to have a stochastic
  inverse.  U1 may cite that coincidence as framing.  U1 may **not**
  report it as a derivation of indivisibility from the covariance
  no-go, nor as a derivation of the covariance no-go from
  indivisibility; the link is `[MY READING]` (§4(2)).
- **C6.** If U1 finds every interpolant stochastic (outcome U1-DIV),
  **no covariance conclusion follows.**  Divisibility does not entail
  invertibility, and L-1's hypothesis is invertibility with a
  stochastic inverse.  U1-DIV may not be reported as bringing v11
  nearer to, or further from, exact covariance.  What U1 *may* report
  is the separate and directly checkable fact of whether any `Γ` in
  the census is invertible with a stochastic inverse: if one is, L-1
  says it is a permutation matrix, and that is a reportable
  structural finding.
- **C7.** No U1 or U4 text may quote paper 8 Cor 2.4 as a statement
  about the continuum, or about any layer other than the finite one
  (paper 8 Lemma 2.2).

---

## 7. Import ledger

| item | status | home |
|---|---|---|
| Lemma 2.3 (stochastic isomorphisms are permutations) | **[THEOREM]**, re-derived here at v11's grain | v3 paper 8:110–130 |
| Corollary 2.4, first sentence (action is by permutations) | **[THEOREM]**, re-derived here as L-1(a) | v3 paper 8:132–137 |
| Corollary 2.4, second sentence (no nontrivial boost) | **[THEOREM]** in source; the step to it supplied here as L-1(b) **[V11-STEP]** | v3 paper 8:132–137 |
| The three admissible finite covariance statements | **[IMPORTED, verbatim]** | v3 paper 8:139–147 |
| Layer-ledger criterion (Lemma 2.2) | **[IMPORTED, paraphrase]** — **unanchored**: not blockquoted here, so the receipt carries no anchor for it; the source's own phrase (*Gamma-only reconstruction theorem*) is used in §5 | v3 paper 8:95–99 |
| Renewal grain fixes the configuration space | paper 0 §4 grades it **[THEOREM-GRADE CONVERGENCE]**; L-1 consumes it as hypothesis and does not verify it — that conservative reading is **this note's own**, not paper 0's grade | paper 0:143–150 |
| Non-invertibility ↔ indivisibility identification | **[MY READING]**, not promoted | catalog §1.3(e), §7 rank 2 |
| Statistical Lorentz invariance of sprinkled division events | **[MEASURED]**, presupposes background Minkowski | catalog §1.5 |
| BHS theorem (no Lorentz-invariant finite-valency graph on a sprinkling) | **[NO-GO, narrow scope]** + **[OPEN]** | catalog §1.6(c); v7 `note-C2-covariance-premise-deferral.md` |
| BHS *applied* to v11's finite-valency generated carrier | **[MY READING]** (the catalog's own grade at §1.6(e)); two unproved steps — embedding into Minkowski, and graph-LI ⇒ point-set-LI (§4(3)).  The catalog's §7 rank 5 *"provably"* is inconsistent with its own §1.6(e) grade; this note takes neither voice | catalog §1.6(e); catalog §7 rank 5 |
| A regular lattice **is** frame-recoverable | **[MEASURED]** — the corpus fact that bears on a crystal | catalog §1.5(a):368–369 |
| Order-level invariance receipts (rapidity 0.9 / 0.8) | **[MEASURED]**, on **other** carriers — Minkowski sample and sprinkling, never generated | v7 `note-C2`:21; catalog §1.7:438–439 |

**Nothing in this note is a claim about what the generated record
IS.**  The one claim it makes about the generated law is conditional
and prohibitive (§3, single-sentence form): *if* THE LAW is a family
of finite row-stochastic matrices on one fixed finite renewal-grain
configuration space, *then* exact Lorentz covariance by stochastic
automorphisms of that space is excluded, and v11 may not claim it.
No measurement of the generated record is asserted anywhere.

---

## 8. Citations, file:line

- `v3/relativistic-isp-v3-paper8-continuum-qft-reconstruction-no-go.md`
  :95–99 (Lemma 2.2), :110–114 (Lemma 2.3), :116–130 (its proof),
  :132–137 (Corollary 2.4), :139–147 (admissible statements).
- `v11/relativistic-isp-v11-paper0-the-indivisible-record-law.md`
  :111–130 (§3 strata), :132–160 (§4 renewals), :143–150 (the
  fixed-configuration posit), :266–277 (§7 L-1), :373–384 (§9b Phase I).
- `v11/note-v11p0a-reproduction-catalog.md`
  :289–333 (§1.3), :365–394 (§1.5, with :368–369 the regular-lattice
  frame-recoverability), :396–428 (§1.6), :432–444 (§1.7, with
  :438–439 the rapidity-0.8 order invariance), :3130–3144 (§7 rank
  2), :3179–3180 (§7 rank 5, the *"provably"* sentence).
- `v7/note-C2-covariance-premise-deferral.md` (the BHS block's home);
  :21 (the rapidity-0.9 order-invariance receipt `c2`).
