# R4c (paper-22, two excitations: statistics as a measurement) — EFFECTUS-LENS HOSTILE REVIEW

**Lens:** meaning, scope, motivation, licensure. **Grade: AWF**
(accept-with-fixes). **Recomputations: 65 distinct propositions**,
independent and exact, over roughly 302,000 instance evaluations;
the delivered instrument was never imported and never executed.
**False computed numbers found: 0.** Every count I could rederive
from first principles rederived — 30 of 30 structural counts, the
1536-row three-site enumeration and its 0 completions, the
support-overlap law's shape on an independent model. The findings
are all about what the delivered sentences *claim* versus what the
arena *forces* — and in this unit the balance runs the unusual way:
**two of the headline claims are stronger than delivered (they are
theorems, and the paper calls them measurements), and one piece of
evidence is weaker than delivered (it is not evidence at all).**

**Object verified.** All five pinned digests match at `4f89135` and
in the worktree, sha256-12: paper `1b4ac134e727`, code
`deb0c1c83a76`, output `45866a3ed5e3`, receipt `5c058006db78`, pin
`162553b03ca9`. Re-verified at the close of this review; nothing
drifted.

**Concurrent workers disclaimed.** At review time the working tree
carried one untracked file from another unit,
`v14/code/perl_exact.py`. I did not open it. No git operation was
performed beyond read-only `log`/`show`/`status`; all execution was
scratch-only under `scratchpad/r4c-ef/`. This file is my single
repository write.

---

## 0. What I recomputed, and what it confirms

**Structural counts (30 of 30 reproduced), from L, d, the alphabet's
own structure and combinatorics alone:** |X| = 16; 256 = 16²;
136 = 16·17/2; 120 = C(16,2); 136 − 120 = 16; 3364 = 58²;
1764 = 42²; 42 = 58 − 16; 1176 = 1764 − 588; 6728 = 2·3364;
588 + 2776 = 3364; 48 = 64 − 16; 3306 = 58·57; 120 = C(16,2)
two-site supports; 43200 = 120·120·3; 32760 = 120·C(14,2)·3;
10080 = 120·(2·14)·3; 360 = 120·3; 42840 = 32760 + 10080;
6960 = 58·120; 7888 = 58·136; 928 = 58·16; 16 doubled-momentum
cells = |X|; 29696 = 58·16·16·2; 1536 = 3·8³; 25 = 1 + 3·8;
512/640 coins; 32 = 2·16 links; 69 verdict values. Zero mismatches.

**The paper's verdict fence is byte-identical to the receipt's
verdict string** (2353 characters), and my own numeral sweep of the
prose (151 tokens, 47 distinct) finds every numeral present in the
receipt. **The value denominators check out**: the single-excitation
census lives on {2, 4, 8} and the two-excitation censuses reach 128,
exactly as §5 says.

**Forced identities, exercised on exact Gaussian-rational unitaries
(≈600 instances in dimensions 3, 4, 5):** P(U⊗U)P⁻¹ = U⊗U;
P(U⊗V)P⁻¹ = V⊗U; U⊗V ≠ V⊗U at every non-proportional ordered pair;
B(U⊗U) = B(U)⊗B(U); the derivation law; the ordered-sector
set-equality and its converse on 200 random row-stochastic pairs;
a monomial leg annihilating the defect on either side; unitary
row-monomiality ⟺ column-monomiality; **and the hard-core leak law
(240 unitaries, 0 violations)**. Each of these is discussed below,
because each of them is a clause the paper reports as a measurement.

**Two independent rebuilds.** (i) The support-overlap law's *shape*,
on a 4-site model with rational rotations sharing nothing with this
arena: both legs non-monomial, zero defect at overlap 0 and 1 at
both excitation numbers, nonzero at overlap 2 — R5's law reproduces
away from this alphabet entirely. (ii) The three-site emptiness,
rebuilt in Z[ζ₈] with ζ₈ scaled to integer coordinates: **1536
full-support unit rows enumerated (the receipt's number, and the
enumeration is provably complete — the only squared-modulus
solution over {1, 1/4, 1/2} summing to 1 is {1/2, 1/4, 1/4}), and
0 completions over all 192 global-phase representatives of the first
row, 300,288 exact inner products.** The measurement stands. Its
stated *reason* does not (MINOR-1).

---

## 1. THE HEAD'S VERB — "ADMITS" is earned as a THEOREM, and the paper sells one leg of it as a measurement

**The question.** Is `BOTH-ADMITTED` earned by measurement, or is the
head partially definitional?

**The answer: it is definitional, at all four arenas, and the paper
half-knows it.** The unit discloses the first forcing beautifully —
the head itself carries `EXCHANGE=COMMUTES-AT-64-OF-64(FORCED-BY-
THE-FREE-LIFT)`, §3 says "the paper says so rather than reporting it
as a finding", and the waiver ledger names the mechanism. That is
the era's discipline working. But the forcing does not stop where
the paper stops it.

**A1 (`BOTH-ADMITTED`) is forced end to end.** P(U⊗U)P⁻¹ = U⊗U for
every U whatever (disclosed). Both sectors are then invariant
(disclosed). The restriction of a unitary to an invariant subspace
is unitary — forced, undisclosed. The Born shadow of a unitary is
doubly stochastic, rows and columns being unit vectors — forced,
undisclosed. So the head's second clause,
`BOTH-SECTORS-CLOSED-UNITARY-STOCHASTIC=64-OF-64`, is the first
clause's corollary and carries no information about R4's family; it
carries a forcing tag on neither side.

**A2 is forced too, and this is the one that matters**, because §3
designates A2 as the measurement that stands in for the disclosed
commutation: *"the measurement that takes its place is the hard-core
census of the next section, whose split is not forced and which
separates the pool."* The receipt's waiver ledger seals the same
sentence: *"G-HARDCORE-LEAK-PER-GENERATOR, whose split is NOT forced
and separates the pool 48 to 16."*

**The split is forced.** Two lines: the entry of Sym²(U) from the
hard-core configuration (x, y), x ≠ y, into the doubly occupied
configuration (a, a) is proportional to U_ax·U_ay + U_ay·U_ax =
2·U_ax·U_ay, so no cancellation is possible and the cell is nonzero
exactly when row a of U has two nonzero entries. A unitary has a row
with two nonzero entries iff it is not monomial (row-monomiality and
column-monomiality coincide for unitaries — checked, 180 instances).
Therefore **Sym²(U) leaks out of the hard core iff U is
non-monomial, for every unitary family whatever.** I exercised this
on 240 exact unitaries in dimensions 3, 4, 5, monomial and not: zero
violations. `G-HARDCORE-ANTISYMMETRIC-CLOSED` is already waived as
forced; its twin is the same theorem read on the other sector.

What remains contingent in §4 is **not the split but its size**:
which generators of *this* pool are monomial (16 of 64 — anchored
from the parent at `PV-PARENT-MONOMIALS` and re-measured here by
support), hence 48 rather than some other number. That is a family
fact inherited from R4, not a two-excitation measurement.

**A3 is a dimension formula typed in the source** (`n*(n-1)//2`),
and the paper declares it as a degenerate control — honest.

**A4 is forced as well.** U⊗V = V⊗U iff V = cU (pick u_ij ≠ 0; then
V = (v_ij/u_ij)·U), and a unit-modulus c mapping this alphabet to
itself lies in μ₈, which `G-GAUGE-ORBITS-FREE` excludes between
distinct pool members. So "fails to commute at 3306 of 3306" is a
theorem about a gauge-reduced pool, not a discovery; and "where it
fails neither sector is invariant" is forced by orthogonality of the
two sectors under a unitary. The receipt calls it
`G-A4-NEITHER-REACHED ... kind: MEASURED`.

**What ADMITS-NOT would have looked like — the two-way design is
real as a design and empty as evidence.** The four arenas do
demonstrate that the head law *discriminates*: the same two-argument
law returns four distinct pre-registered names, and the mutants
(MUT-A3-LIVES, MUT-A3-DIM, MUT-A4-COMMUTE, MUT-BOTH-ADMITTED) prove
the branches are reachable in code. That satisfies #34's
reachability requirement. What it does not do is show that any
arena's verdict was ever in doubt for *this* family: change the
family entirely, keep the free lift and a ceiling of two, and A1
still returns `BOTH-ADMITTED`. The genuinely family-dependent
content of the unit lives in §5–§9 (the defect census, the
discrimination, the overlap law, the velocity failure), not in the
head.

**This is not a demotion of the result.** A theorem is better than a
census. `BOTH-ADMITTED` is *correct*, and it is correct for a reason
stronger than measurement: no unitary substrate lifting freely can
select an exchange shape, because the free lift commutes with
exchange identically. The repair is to say so, and to stop
designating a second forced clause as the measured content that
replaces the first.

→ **MAJOR-1** (§8).

---

## 2. THE CEILING'S STATUS — the deepest row

**Is the ceiling a declaration, a measurable of some pinned layer, or
open?** It is **a declaration of this unit, with a genuinely open
question behind it** — and the paper's own answer is right. What is
not right is the one sentence of positive evidence it offers.

**The licensed half.** "The record layer declares the site lattice,
the link set and the chart group and declares no occupancy ceiling"
is TRUE and I checked it: the stage receipt
(`v13/code/ha_successor_receipt.json`, anchored `542b8735daf0`)
carries 27 declaration keys — `L`, `d`, `links_d2`, `chart_group`,
`lapse_family`, `records_d2`, `registers`, … — and **not one of them
is occupancy-shaped**; a case-insensitive scan of the whole file for
`occupan*` returns nothing. Good.

**The unlicensed half.** §4 continues: *"and its own count registers
are integer valued and run to 6 and 12. If that argues anything it
argues against the hard core."* The head carries the same value as
`OCCUPANCY=CEILING-DECLARED-NOT-ANCHORED(STAGE-COUNT-REGISTER=6)`,
and the gate `G-OCCUPANCY-NOT-ANCHORED` seals the inference in its
description. I traced the anchor. `PV-COUNT-REGISTER` reads
`declarations/count_lattice/axis_max` and `PV-DIAG-REGISTER` reads
`declarations/count_lattice/diag_max`, and the stage's own
description of that object is:

> "the declared box of count vectors (n_e1, n_e2, n_diag) **swept**
> for the link-locality theorem's witnesses"

So the number 6 is (i) a **link** register — a division-event count
on the three link classes, from the weld dictionary
`DIVISION-COUNT → n_ℓ(x)` — and not a site register at all; and (ii)
not a capacity or a measured maximum, but **the upper bound of a
search box v13 chose to sweep**. Raising it to 7 would have been a
free edit in another unit. It cannot bear on how many excitations a
site may hold, in either direction, and the one stage declaration
that *is* site-indexed and integer valued — `registers` = {"m == 0":
the zero address register, "m == 1": the unit address register} — is
binary, so a reader minded to argue by analogy could run the
argument the other way with equal (that is, no) force.

The hedge "if that argues anything" is doing real work, and the
instrument's decision to carry the value "as an anchored value
rather than as a reading" is the right instinct. But the sentence
still puts a thumb on the scale for the ceiling of two in a unit
whose entire finding is that **nothing** puts a thumb on that scale,
and the gate's sealed description asserts an interpretation its
predicate cannot falsify (it tests `regval == 6 and regval > 1`) —
E-23's exact shape.

→ **MAJOR-2** (§8), with a repair that *strengthens* the section: a
positive gate over the stage's declaration keys, proving the silence
rather than arguing from a borrowed integer.

**THE FORCING QUESTION — the register row.** What would it take for
a deeper layer to force the ceiling, and what would follow?

> **The licensed conditional.** Suppose a deeper layer supplies
> (i) an assignment of excitations to record-layer actors that is
> **injective at each instant**; and suppose (ii) the R=3 weld's
> dictionary is used as delivered — `ACTOR → SITE` with fiber 1, a
> bijection on the saturating stratum (paper-19, WELD3-FOUND,
> fibers 1/1/1); and suppose (iii) a law is *required* to be closed
> and unitary with a stochastic Born shadow **on the declared
> configuration space** (no enlargement of the space permitted); and
> (iv) the generator family is the declared 64-member pool, not one
> of its sub-families. **Then** the hard core is forced, and by this
> unit's §4 the symmetric shape is not a law of that coupled theory
> — it leaks at exactly the 48 non-monomial generators — while the
> antisymmetric shape is closed at all 64. **Fermionic-shape becomes
> a theorem of the coupled theory**, at n = 2, d = 2, L = 4, under
> the free lift, with no spin and no relativity anywhere in the
> derivation.
>
> **Four things that conditional is not.** (a) Premise (i) is a
> *declaration* — the weld maps actors to sites, and "an excitation
> is an actor" is a further identification nobody has priced; it is
> the whole content of the successor unit. (b) Premise (iii) is a
> declaration too: leakage forces a choice between "the symmetric
> shape is excluded" and "the declared configuration space was too
> small", and only the first reading yields the theorem. (c)
> Premise (iv) is load-bearing: **on the 16 monomial generators both
> shapes survive the hard core**, so the theorem is a statement
> about the family, not about every dynamics on this stage. (d)
> **The forcing is one-way.** A deeper layer that forces ceiling ≥ 2
> forces *nothing*: both shapes remain admissible, and statistics
> stays undetermined by this route. Exclusion can select a shape;
> permission cannot. That asymmetry is itself a result of this unit
> and is worth stating in §10.

**Whose unit.** Not FCK. The ceiling is a property of the
configuration space, not of number-changing dynamics — FCK
*inherits* the ceiling as an input (it is precisely the difference
between a fermionic and a bosonic Fock space) and cannot settle it.
The owner is a unit that welds the excitation layer to the record
layer: pinned at paper-19 (the weld dictionary), paper-20 (the
coupling), and this paper, asking whether `ACTOR → SITE`'s
injectivity descends to excitations. Recommended name: **OCC**, and
it should be posed before FCK, because FCK's creation operator needs
the answer to type-check.

---

## 3. THE PAULI SENTENCE — how far "exclusion → antisymmetry with no spin and no relativity" is licensed

**First, the walls: the paper does not claim it.** The words *Pauli*,
*spin*, *relativity*, *spin-statistics*, *anyon* and *braid* do not
occur in paper-22 at all. "Exclusion" occurs once, in §1, in a
strictly technical sense ("the exclusion read as a dimension count").
"Particle" occurs twice, both times as a wall ("Reading a statistics
is not building a particle"; "No particle is named"). *fermionic-shape*
and *bosonic-shape* occur three times, always hyphenated, always
with their definition attached. **The paper does not claim to explain
spin-statistics, and could not: there is no spin here.** Walls held.

**So this row is about the gloss, not the paper** — about what the
orchestrator, the ledger, or a reader may say downstream. Here is
the exact licensed sentence:

> **Licensed.** On this arena (d = 2, L = 4, the 64-generator pool,
> the free lift, two excitations), *if* the occupancy ceiling is
> declared to be one, *then* the symmetric shape fails to be a
> closed stochastic law at 48 of the 64 generators, while the
> antisymmetric shape is closed at all 64. The implication
> **exclusion ⟹ antisymmetry** therefore runs on this arena, and it
> runs with no spin, no Lorentz group, no field, no relativity and
> no continuum in the derivation.
>
> **Not licensed.** (a) That the implication is a *discovery about
> this substrate*: I proved it is a theorem about Sym² of any
> unitary (§1 above), so it holds for any lattice, any alphabet, any
> family. Its content is mathematical, and its interest is that this
> programme's Born-shadow layer inherits it. (b) That the symmetric
> option is *inconsistent*: it is not. It fails to be closed **on the
> declared configuration space**, and only at 48 of the 64
> generators; on the monomial sub-family it is perfectly consistent
> under a hard core, and on the full family it becomes consistent
> again the moment one enlarges the space (which is what a ceiling
> of two does). "Forced" is licensed only in the conditional form of
> §2 above, with all four premises attached. (c) That anything here
> bears on the **spin-statistics theorem**. That theorem derives the
> *correlation* between spin and exchange symmetry from Lorentz
> invariance and positivity. This unit has no spin to correlate and
> no Lorentz group to invoke; it derives an exchange shape from an
> **occupancy declaration**, which is the *other* half of the
> textbook story (Pauli exclusion as a consequence of antisymmetry)
> run backwards. The honest gloss is: *the substrate reproduces the
> exclusion ⟷ antisymmetry link without spin and without
> relativity, and says nothing whatever about why spin-½ should be
> the antisymmetric one.*

**The 48-generator leak census is the mechanism, and it supports the
weaker verb.** It shows *where* the symmetric option breaks (exactly
the non-monomial generators, i.e. exactly the generators that
interfere) and therefore that the breakage is not an artifact of one
coin. It does not show inconsistency, and the paper's §4 correctly
says "does not give a stochastic law on the declared configuration
space" rather than "is inconsistent" — one qualifier short of exact
(MINOR-4).

---

## 4. THE INDISTINGUISHABILITY SENTENCE — the licensure path is sound, and shorter than delivered

The claim: *"The entire excess of 1176 pairs is created by erasing
those labels — by exchange symmetrisation — and by nothing else in
the construction."*

**The path, verified.** (i) On the ordered/labelled sector the Born
shadow is multiplicative: B(U⊗U) = B(U)⊗B(U), entrywise, forced.
(ii) Hence Δ₂ = X⊗X − Y⊗Y with X = B(U₂U₁), Y = B(U₂)B(U₁), and the
delivered derivation law Δ₂ = Δ⊗X + Y⊗Δ is the algebraic identity
(X−Y)⊗X + Y⊗(X−Y) — I verified it on 36 exact pairs and it is
one line of algebra. (iii) The consequence — the ordered sector's
nonzero set is exactly the single-excitation set, so labelled
excitations carry **no** genuine two-body defect — is *also* forced:
X⊗X = Y⊗Y ⟺ X = Y whenever X and Y are row-stochastic (sum the
identity X_ik·X_jl = Y_ik·Y_jl over l and use Σ_l X_jl = Σ_l Y_jl =
1). Verified on 200 random row-stochastic pairs, 0 violations. (iv)
The distinguishable *arena* is a different object and the paper says
so, in parentheses, correctly — the exchange symmetry there is
*broken by the law*, not *dropped by the description*.

**So the sentence is licensed, and it is licensed universally, not
locally.** For *any* unitary family whatever, on *any* lattice: the
free lift of labelled excitations carries no genuine two-body
defect, so any two-body interference in the Born shadow of a free
lift is the work of symmetrisation. That is a considerably better
result than 3364 pairs of one family, and it generalises to n by the
telescoping identity Xⁿ − Yⁿ = Σ_k Y^{⊗k} ⊗ Δ ⊗ X^{⊗(n−1−k)} with
the same set-equality corollary (verified, 160 exact trials at
n = 2, 3, zero failures).

**What must be repaired is the paper's account of its own
epistemics.** §5 says: *"Both sides are built and compared at every
pair, with zero failures, and the consequence is measured rather
than argued."* It is argued — it cannot fail to hold — and §11's
totality claim ("Gates whose clause is analytically forced are
registered as disclosures") makes the omission a violation of the
unit's own stated discipline. → **MAJOR-3**.

**Description-stamp discipline: sound in doctrine, incomplete in
inventory.** §11 claims *every* quantum-layer claim carries a stamp,
and 7 stamps are sealed. The indistinguishability claim — a
Born-level claim if ever there was one, since Δᴮ is a function of an
orthonormal basis and symmetrisation *is* a change of description —
has **no stamp of its own** and **no `paper_claims` row**
(`defect_census/ordered_sector_nonzero` is load-bearing for a
headline sentence and appears in no claim, so the polarity machinery
never perturbs it). The prose language is otherwise exactly right —
"erasing labels", "excitations that carry labels" — and the ontology
is the programme's own (quantum as the shadow of a coarse
description). Repair is small and mechanical. → folded into
**MAJOR-3**.

---

## 5. THE 588 TRIPLE IDENTITY — what it licenses, and the one arena it has not been asked about

Three sets coincide element for element on the circulant stratum:
the single-excitation defect set; the set where the symmetric and
antisymmetric two-excitation defects differ; and the set where the
declared contact handle moves the symmetric defect. All three are
gated as set equalities, not cardinalities — the right gate, and the
receipt's `set_equality: true` /
`moved_set_is_the_single_excitation_set: true` carry it.

**The licensed meaning.** On the verdict-bearing circulant stratum,
every probe of the doubly occupied channel available to this unit —
the choice of exchange shape, and a declared contact interaction —
has Born-level consequences **exactly on the ordered pairs whose
one-excitation composition already fails to restart at the cut**,
and none anywhere else. Equivalently: *where the substrate is
classical across the cut, statistics is unobservable and contact is
invisible; where it interferes, both become observable, and on
precisely the same pairs.* The mechanism §9 gives is coherent — a
phase has unit modulus and is invisible to a single Born shadow, so
it can only show across a cut where a doubly occupied intermediate
interferes with one that is not — and the symmetric sector's
composition passes through doubly occupied intermediates the wedge
does not have, which is why the shape difference is the same kind of
probe.

**The over-reach.** §9 closes: *"on this arena, everything that can
see the doubly occupied channel … sees it exactly where the
substrate's one-excitation composition already fails to restart at
the cut, and is blind everywhere else"*, and §6 closes *"it can read
it nowhere else"*. **The evidence is stratum-wide, not arena-wide.**
The unit's own second window — the 2-site local coin alphabet —
contains **360 rows at overlap 2 on which the one-excitation defect
is nonzero at 360 of 360**, and on those rows the shape
discrimination was *never measured*: `raw_overlap` computes
`defect(wedge(U2), W1)` and `defect(symsq(U2), S1)` per row and
records only whether each is nonzero, never comparing them. So there
are 360 rows in this arena where the substrate demonstrably
interferes and the paper's "exactly where" has not been tested.
Worse for the sentence as written, if the two shapes agree there,
"exactly where" is false at arena scope and true only on the
circulant stratum.

This also touches R5's terminal claim, at link grain, that "the
fibre-2 choice is not load-bearing" — a sentence this unit's
headline bears on directly and never mentions. The two are at
different grains and are not in conflict; but which of them holds at
the *local* grain is exactly what those 360 rows would say.

→ **MAJOR-4**, with a repair that is a few lines of the instrument's
existing machinery and decides the question either way.

---

## 6. THE NO-PARASTATISTICS CLAIM — n = 2 stamped, topology not

**n = 2 is stamped, thoroughly.** The head carries
`N=2-ONLY-NO-GENERAL-N-CLAIM`; §1 says "the argument that forbids a
third shape is an argument about two"; §10 says the general-n sector
"where parastatistics-shaped representations genuinely exist" is not
built; the output's NOT-EXECUTED block repeats it; and the gate
`G-SECTOR-DECOMPOSITION` names S₂'s two irreducible characters as
the reason. Correct and complete.

**Topology is not stamped, and this arena is two-dimensional.** The
head clause `DECOMPOSITION=256=136+120(NO-THIRD-SECTOR-AT-TWO-
EXCITATIONS)` will be read by anyone from physics as "no anyons",
and in d = 2 that reading is both wrong in general and unaddressed
here. The S₂ argument constrains representations of the *permutation*
group; braid statistics concerns B₂ ≅ Z, which has a continuum of
one-dimensional representations, and it arises from the topology of
the configuration space of indistinguishable points in a plane —
an object this unit never builds. What actually excludes a third
shape *here* is that exchange is implemented by a single finite
operator P with P² = 1 on a discrete lattice with no exchange paths
at all, so only S₂ is representable by construction. That is a
perfectly good reason; it is simply a different reason from the one
a reader will supply, and in d = 2 the difference is exactly where
the interesting physics is claimed to live.

→ **MAJOR-5**: one sentence in §10, and one clause in SCOPE.

---

## 7. THE CHOICE INVENTORY, and the prose↔receipt sweep

### 7.1 The inventory is missing

This is the unit whose entire headline is *"the coordinate that
selects is a declaration"*. It publishes **no choice inventory.**
`published_keys` has 29 entries and `choice_inventory` is not among
them; the only occurrence of the string in the receipt is a path
into the *parent's* inventory (`choice_inventory/12/value`). Both
parents publish one — R4 fifteen items, R5 twenty, and R5's includes
the very item this unit exists to resolve: *"the two-excitation
extension, GENUINELY-FREE, fibre 2"*. The prose does carry the
substance, in the SCOPE segment and in §10's "not decided" list, and
no free item is *hidden*. But the RSQ standard is an inventory with
fibres and a verdict-determining flag, sealed as data, and §15's
"match every coordinate" wants the same. Its absence here is
conspicuous precisely because the answer would be so striking:

| item | fibre | class | verdict-determining |
|---|---|---|---|
| **the occupancy ceiling** | **2** (hard core / two) | **GENUINELY-FREE** | **YES — the head changes name** |
| **the lift** | **3 declared** (free / distinguishable / contact) | **GENUINELY-FREE** | **YES — A4 returns NEITHER** |
| the lattice (verdict arena vs the one-site control) | 2 declared | DECLARED CONTROL | yes, at A3 |
| the division-event times and the leg at the cut | inherited | GENUINELY-FREE (parent's) | no (fixes the defect's meaning) |
| the velocity convention | 2 (fwd/bwd) × tie reading | INHERITED AS DECLARED | no — but it *owns* the 7168 |
| the third route's window | 12 generators / 144 pairs | GENUINELY-FREE | no |
| the local window and its 3 coin pairs | declared | GENUINELY-FREE | no (gated separately) |
| the contact phase (ζ₈) | 1 declared of 8 | GENUINELY-FREE | no |
| the symmetrised basis (orthonormal) | 1 | FORCED | no |
| d, L, alphabet, stencil, axes, connective | 1 each | FORCED (anchored/inherited) | no |

Two verdict-determining free items, and the paper's thesis is that
one of them is the whole story. Publishing this makes the thesis
*machine-checkable*: gate that the set of head names returned across
the arena census is exactly the set obtained by moving the
verdict-determining items, and nothing else.

→ **MAJOR-6**.

### 7.2 The sweep

Everything I could cross-check between prose, output, receipt and
head agrees. The verdict fence is byte-identical; the four-arena
table matches `arena_census` row for row; §5's table matches
`defect_census`; §7's table matches `overlap_census/by_overlap`; §8's
numbers match `motion`; §9's match `contact_handle`; the "eighths"
and "1/128" claims match the value denominators; "58 of 58
families", "19 families", "320 tie cells", "1856 cells" match
`parent_reproduction` and R4b's anchors. Four small discrepancies,
all in the sealed *descriptions* rather than the numbers:

- **the overlap description stamp says "one declared interfering
  coin pair"** while the measurement is three, each gated separately
  (`coin_pairs: 3`, `per_coin_pair` with three rows, head
  `COIN-PAIRS=3-EACH-GATED-SEPARATELY`). Stale text. (MINOR-3)
- **`G-CONTACT-TWO-WAY`'s claim says "the zero is a measurement and
  not a vacuity"**, dropping the qualifier the *paper* gets right
  ("not a vacuity **of the handle**"). The antisymmetric zero is
  forced — the wedge has no doubly occupied configuration — and §9's
  prose says so. Align the receipt to the paper. (MINOR-7)
- **§4's "does not give a stochastic law … at all"** reads as
  universal over generators; it holds at 48 of 64. (MINOR-4)
- **§7's "because the alphabet carries no element of modulus
  1/√3"** is a non-sequitur (MINOR-1, below).

### 7.3 E-24 — fractions

E-24 (bought #192): *"A unit publishing a fraction either declares
the measure with it or stamps it COUNTING-ONLY."* Paper-22 publishes
fractions everywhere — 1764 of 3364, 48 of 64, 588 of 3364, 7168 of
29696, 42840 of 42840 — and the strings `COUNTING-ONLY`,
`counting only`, `uniform measure` and `not a probability` appear
nowhere in the paper, the code or the receipt. The SCOPE segment's
`NO-CONFIGURATION-MEASURE` is a statement that no measure was built,
which is adjacent to but not the same as the stamp E-24 requires.
**Birth-date note, in fairness:** the pin froze at #174 and E-24 was
engraved at #192, so this is a post-pin standard reaching a pre-pin
unit; delivery (#195) is post-engraving. The repair is one clause.
(MINOR-2)

---

## 8. FINDINGS, RANKED

### MAJOR-1 — the hard-core split is FORCED, and paper and receipt both say it is not

**Where.** Paper §3 ("whose split is not forced and which separates
the pool"); receipt `waiver_ledger[0].forcing` (same sentence,
sealed); `G-HARDCORE-LEAK-PER-GENERATOR` marked `kind: MEASURED`.

**Why it is wrong.** Sym²(U)'s cell from (x, y), x ≠ y, into (a, a)
is 2·N·U_ax·U_ay — no cancellation — so it is nonzero iff row a of U
has two nonzeros, iff U is non-monomial (unitary). 240 exact
unitaries, dims 3–5, zero violations.

**Exact repair.**
1. Add a fourth waiver:
   `{"gate": "G-HARDCORE-LEAK-PER-GENERATOR", "kind": "FORCED",
   "forcing": "the Sym^2 cell from a hard-core configuration (x,y),
   x != y, into a doubly-occupied (a,a) is 2 U_ax U_ay, which
   cannot cancel, so the symmetric sector leaks iff some row of U
   carries two nonzero entries iff U is non-monomial -- an identity
   of Sym^2 for every unitary, not a property of this family.  The
   measured content beside it is which generators of THIS pool are
   monomial (16 of 64, the parent's Markovian set name for name,
   G-MONOMIAL-CLASSIFIER) and hence the SIZE of the split."}`
   and set `kind="DISCLOSURE"` on the gate.
2. §3: replace *"the measurement that takes its place is the
   hard-core census of the next section, whose split is not forced
   and which separates the pool"* with *"the measurement that takes
   its place is the defect census of section 5, whose per-pair law
   is not forced in the direction that matters: that both legs being
   non-monomial suffices for a two-excitation defect is a fact about
   this family, and section 7 exhibits non-monomial pairs elsewhere
   in the arena that carry none."*
3. §4: after "the leaking set is exactly the non-monomial set, with
   no mismatches", add *"— which is forced: the symmetric square's
   only route out of the hard core is the cell 2·U_ax·U_ay, so it
   leaks exactly when a row of U carries two nonzero entries. What
   this family contributes is the size of the split, 48 against 16."*
4. Optional but consistent with the head's own practice: tag the
   head clause
   `AT-CEILING-1-SYMMETRIC-LEAKS=48-OF-64-EXACTLY-THE-NON-MONOMIAL(FORCED-BY-SYM-SQUARED;THE-48-IS-THE-FAMILY)`
   and `BOTH-SECTORS-CLOSED-UNITARY-STOCHASTIC=64-OF-64(FORCED-BY-THE-FREE-LIFT)`.

### MAJOR-2 — the "count registers run to 6 and 12" argument is not evidence

**Where.** Paper §4; head `(STAGE-COUNT-REGISTER=6)`; gate
`G-OCCUPANCY-NOT-ANCHORED`'s sealed description.

**Why.** `declarations/count_lattice` is v13/HA's *"declared box of
count vectors (n_e1, n_e2, n_diag) swept for the link-locality
theorem's witnesses"* — a **link** register and a **sweep bound**,
not a site capacity. The stage's only site-indexed integer
declaration (`registers`) is binary, so the analogy runs both ways,
i.e. neither way.

**Exact repair.**
1. §4: delete *"and its own count registers are integer valued and
   run to 6 and 12. If that argues anything it argues against the
   hard core, and the instrument carries it as an anchored value
   rather than as a reading."* Replace with: *"and there is no
   occupancy-shaped declaration anywhere in it: its integer count
   registers are link registers — the division counts (n_e1, n_e2,
   n_diag) whose swept box carries the bounds 6 and 12 — and its one
   site-indexed register is binary. The stage is silent on site
   occupancy, and neither of its integers argues either way. The
   ceiling is therefore this unit's declaration, and it is censused
   both ways."*
2. Intro, second paragraph: cut *"and its own count registers are
   integer valued and run to 6"*.
3. Gate: strip the inference from the description and **add the
   positive measurement it should have been** —
   `G-STAGE-DECLARES-NO-OCCUPANCY`: enumerate the stage receipt's
   `declarations` keys and require that none matches
   `occup|ceiling|capacity|multiplicity` (27 keys, 0 matches, which
   I verified), with a mutant that injects such a key and dies.
   That converts the section's load-bearing claim from an argument
   into a measurement.
4. Head: `OCCUPANCY=CEILING-DECLARED-NOT-ANCHORED(STAGE-DECLARES-NO-OCCUPANCY-KEY-IN-27)`;
   keep `PV-COUNT-REGISTER`/`PV-DIAG-REGISTER` as anchors of what the
   stage *does* declare, re-labelled `LINK-COUNT-BOX-BOUND`.

### MAJOR-3 — the ordered-sector derivation law and its consequence are theorems, and the claim they carry is unstamped and unclaimed

**Where.** §5 (*"the consequence is measured rather than argued"*);
`G-DERIVATION-LAW`, `kind: MEASURED`; §10 bullet 4; §11's totality
sentence. Also: no `paper_claims` row and no description stamp for
the unit's second headline.

**Why.** Δ(U₂⊗U₂, U₁⊗U₁) = X⊗X − Y⊗Y = Δ⊗X + Y⊗Δ identically, and
X⊗X = Y⊗Y ⟺ X = Y for row-stochastic X, Y. Both verified (36 pairs;
200 random stochastic pairs). It generalises to n by telescoping
(160 trials, 0 failures).

**Exact repair.**
1. Fifth waiver on `G-DERIVATION-LAW`, `kind: FORCED`, forcing:
   *"B(U tensor U) = B(U) tensor B(U) entrywise, so the ordered
   defect is X tensor X - Y tensor Y = Delta tensor X + Y tensor
   Delta identically; and X tensor X = Y tensor Y iff X = Y for
   row-stochastic X, Y (sum over a free index).  Labelled
   excitations therefore carry no genuine two-body defect for ANY
   unitary family.  The measured content beside it is the
   symmetrised census, whose 1176 genuine pairs are family facts."*
2. §5: replace *"and the consequence is measured rather than
   argued"* with *"and the consequence is not merely measured but
   forced: X⊗X = Y⊗Y only when X = Y, so the ordered sector's defect
   set is the single-excitation set for any unitary family whatever.
   The check at every pair is an implementation check, and the
   *strength* of the statement is what it buys — the excess is the
   work of symmetrisation not only here but wherever a free lift is
   read in a labelled basis."*
3. Add `CL-ORDERED` to `paper_claims`, path
   `defect_census/ordered_sector_nonzero`, text `"588 of 3364"`
   as it appears in §5's table row, so the claim acquires polarity.
4. Add the eighth description stamp: claim *"the entire two-body
   excess is created by exchange symmetrisation"*, stamp naming the
   ordered/labelled sector, the free lift, ceiling 2, the parent's
   division-event times and the orthonormal symmetrised basis (the
   description whose change *is* the symmetrisation).

### MAJOR-4 — "exactly where the substrate interferes" is a stratum claim wearing an arena claim's clothes

**Where.** §6 final paragraph ("it can read it nowhere else"); §9
final paragraph ("on this arena, everything that can see the doubly
occupied channel …"); `G-CONTACT-SET-IS-THE-INTERFERING-SET`'s claim
text ("Everything that can see the doubly-occupied channel on this
arena …").

**Why.** All three set equalities are measured on the 3364 circulant
pairs. The same arena's local window carries 360 overlap-2 rows
where the one-excitation defect fires at 360 of 360 and the shape
discrimination is never taken: `raw_overlap` computes both shapes'
defects per row and records only nonzero-ness.

**Exact repair (preferred — it is cheap and it decides).** In
`raw_overlap`, for the overlap-2 rows only, restrict both sector
defects to the hard-core block (the §6 like-for-like recipe) and
record whether they differ; publish
`overlap_census/overlap_2_shapes_differ` and gate it two-way:
*"at the local grain the two shapes are discriminated at N of 360
rows"*, with N > 0 confirming the arena reading and N = 0 forcing
the stratum reading. Then either keep §9's sentence with the local
window cited beside the stratum, or rewrite it as *"on the
verdict-bearing circulant stratum"*. If the measurement is not run,
the fallback repair is mandatory: insert "on the circulant stratum"
into §6's and §9's closing sentences and into the gate's claim.
**Either way, add one sentence to §7 reconciling with R5's terminal
"the fibre-2 choice is not load-bearing", which was a link-grain
statement and is untouched by this unit's stratum-grain
discrimination.**

### MAJOR-5 — the third-shape exclusion needs its topological scope stamp, in d = 2 above all

**Where.** Head `(NO-THIRD-SECTOR-AT-TWO-EXCITATIONS)`; §3; §10.

**Exact repair.** Add to §10's "not decided" list: *"Nothing here
bears on braid statistics. Exchange is implemented by a single
finite operator P with P² = 1 on a discrete lattice; the
configuration space of indistinguishable points, whose topology is
what admits anyonic representations in two dimensions, is never
built. The two-irrep argument constrains representations of the
permutation group and no more — and this arena is two-dimensional,
so the omission is not idle."* And append `NO-BRAID-CLAIM;
NO-CONFIGURATION-SPACE-TOPOLOGY` to the SCOPE segment.

### MAJOR-6 — no choice inventory, in the unit whose thesis is that a choice decides

**Exact repair.** Publish `choice_inventory` on the R4/R5 schema
with the ten rows of §7.1, `verdict_determining: true` on the
occupancy ceiling and the lift; add
`G-CHOICE-INVENTORY-VERDICT-DETERMINING` gating that the head names
returned across `arena_census` are exactly those obtained by moving
the verdict-determining items; add the inventory to
`published_keys`, to `seals`, and to §10 as a table.

### MINOR findings

1. **§7's false mechanism.** *"none completes to a unitary, because
   the alphabet carries no element of modulus 1/√3"* — a
   non-sequitur: **none of the 1536 swept rows contains such an
   element** (their squared moduli are 1/2, 1/4, 1/4, the only
   solution over this alphabet), so the absence of 1/√3 cannot be
   what defeats their completion. I reproduced the enumeration
   (1536) and the emptiness (0 completions over all 192
   global-phase representatives, 300,288 exact inner products), so
   only the reason is at fault. **Repair:** *"…and none completes to
   a unitary: over this alphabet the only full-support unit row has
   squared moduli (1/2, 1/4, 1/4), and no two further alphabet rows
   are orthogonal to it and to each other — 1536 rows swept, zero
   completions."*
2. **E-24.** No fraction is stamped. **Repair:** append
   `COUNTING-ONLY` to the SCOPE segment and one sentence to §11:
   *"Every fraction in this paper is a count over a declared
   enumeration and is not a probability; no measure on generator
   pairs, configurations or rows is declared."*
3. **Stale description stamp:** the overlap stamp says "one declared
   interfering coin pair"; make it "three declared interfering coin
   pairs, each gated separately".
4. **§4 "at all":** *"the symmetric shape does not give a stochastic
   law on the declared configuration space at all"* → *"…at 48 of
   its 64 generators; on the 16 monomial ones it still does."*
5. **Untagged forced head clauses:**
   `BOTH-SECTORS-CLOSED-UNITARY-STOCHASTIC=64-OF-64` (free-lift
   corollary), `ANTISYMMETRIC-LEAKS=0-OF-64` (waived in the receipt,
   untagged in the head), `THE-TWO-CEILINGS-AGREE-AT-ONE-
   EXCITATION=16-OF-16` (a tautology — one excitation cannot doubly
   occupy), and `…ANTISYMMETRIC-AT-0` in the contact clause (the
   wedge has nothing to act on). Tag or group them under one
   `(STRUCTURAL)` marker; the paper's prose already concedes each.
6. **§10 bullet 3 and description stamp 3** state the per-pair law
   ("nonzero at exactly the pairs whose legs are both non-monomial")
   without the stratum qualifier, while §7 correctly explains that
   it holds because circulant pairs share every site. The unit's own
   overlap census contains 42,840 rows of both-non-monomial pairs
   with **zero** two-excitation defect, and my independent 4-site
   model reproduces that. **Repair:** insert "on the full-support
   circulant stratum" into the bullet and the stamp.
7. **`G-CONTACT-TWO-WAY`'s claim text** should carry the paper's own
   qualifier: "not a vacuity **of the handle**".
8. **`LOSSES=0` is entailed**, not independent: a single-excitation
   defect forces both legs non-monomial (monomial legs annihilate
   the defect — forced), which the measured law then carries to two.
   Worth half a line in §5 so it is not read as a third
   measurement.

---

## 9. THE LICENSED CLAIM

Everything below is at d = 2, L = 4, |X| = 16, Q(ζ₈), the
25-element alphabet, the 3-term axis stencil, the 64-generator pool
(58 circulants + 6 controls), two excitations, the free lift U⊗U,
the parent's declared division-event times with the leg B(U₂) at the
cut, and R4b's velocity convention inherited as declared. Counts,
not probabilities. Shape words only.

**Forced, and true of any unitary family whatever (not findings
about this substrate):**

1. The free lift commutes with exchange, so both exchange sectors
   are invariant, unitarily restricted and Born-stochastic. **No
   substrate that lifts freely can select an exchange shape.**
   `BOTH-ADMITTED` is a theorem, and the right verb.
2. Under a hard core the symmetric sector leaks **iff** the
   generator is non-monomial; the antisymmetric sector never leaks.
   So **exclusion selects the antisymmetric shape**, whenever a law
   is required to close on the declared space — with no spin and no
   relativity in the derivation, and no bearing on spin-statistics.
3. On the labelled (ordered) sector the defect obeys
   Δ₂ = Δ⊗X + Y⊗Δ and vanishes exactly where the one-excitation
   defect vanishes: **labelled excitations carry no genuine two-body
   defect**, at n = 2 and (by telescoping) at every n. Hence any
   two-body interference in a free lift's Born shadow is the work of
   **symmetrisation alone** — a statement about descriptions, which
   is where this programme locates the quantum layer.
4. Both ceilings restrict identically at one excitation, so **no
   single-excitation measurement could have decided the ceiling** —
   the parent's whole arena is a fixed point of both.
5. The symmetric spectrum exceeds the antisymmetric by exactly
   |X| = 16 cells, the same 16 by which the sectors' dimensions
   differ. Two bases, one number, different subspaces — as the paper
   says.

**Measured, and contingent on this family:**

6. 16 of the 64 generators are monomial, so the hard-core split is
   48 against 16.
7. At two excitations the defect is nonzero at exactly the 1764 =
   42² pairs whose legs are **both** non-monomial (0 mismatches over
   6728 per-pair tests). The reverse implication is the content: at
   one excitation only 588 of those pairs carried a defect. **1176
   genuine two-body pairs, 0 losses.** Scope: the full-support
   circulant stratum — the same law fails elsewhere in this arena,
   where non-monomial pairs of disjoint support carry nothing.
8. The two shapes are discriminated by the defect at 588 of 3364
   pairs, and that set **is** the single-excitation defect set,
   element for element; the declared contact handle moves the
   symmetric defect on the same 588 and the antisymmetric on none
   (the latter forced). Scope: the circulant stratum; 360 interfering
   rows of the local window are untested (MAJOR-4).
9. R5's support-overlap law survives the lift and the generalisation
   to every 2-site support: 0 defects at 42840 of 42840 rows at
   overlap ≤ 1, 360 of 360 carrying at overlap 2, each of three coin
   pairs on its own. Independently reproduced in shape on an
   unrelated model.
10. Eigenphases add exactly (forced); velocities do not, failing at
    7168 of 29696 cells and **only** at the antipodal tie — an
    aliasing signature of the inherited convention, which the paper
    correctly declines to dress as an interaction. The speed ceiling
    {0, 1, 2} does not widen with excitation number.
11. Over this alphabet no three-site local unitary has full support
    (1536 rows swept, 0 completions — independently reproduced).

**Declared, and decisive:** the occupancy ceiling. The unit measures
what each declaration costs and does not claim to have found the
substrate's own. **Not claimed, correctly:** any particle, any spin,
any general n, any braid statistics, any configuration measure, any
action, any coupling, any transport number, any continuum.

---

## 10. THE SUCCESSOR REGISTER

**(R1) THE CEILING-FORCING QUESTION — a new unit, OCC, before FCK.**
Owner: not FCK (which *consumes* the ceiling) and not SPT. Pin at
paper-19 (the weld dictionary `ACTOR→SITE`, fibers 1/1/1, a
bijection on the saturating stratum), paper-20 (the coupling) and
this paper. The question: **does the weld's injectivity descend from
actors to excitations, and at what price?** Carry §2's conditional
verbatim as the pre-registered payoff, including its four premises
and its one-way asymmetry (exclusion can select a shape; permission
cannot). Pre-registered outcomes should include
`OCC-BLOCKED-AT-THE-EXCITATION-ACTOR-IDENTIFICATION`, which on
present evidence is the likeliest.

**(R2) THE 360 ROWS — this unit's own repair, or its first
successor.** Do the two shapes differ at the local grain? Decides
whether "exactly where the substrate interferes" is an arena law or
a stratum law, and settles the relation to R5's terminal "the
fibre-2 choice is not load-bearing". Cost: a few lines in
`raw_overlap`.

**(R3) WHAT FCK (the Fock rung) INHERITS VERBATIM.**
- **The occupancy ceiling as a priced free item, fibre 2,
  verdict-determining.** FCK cannot dodge it: the ceiling *is* the
  choice between a fermionic and a bosonic Fock space, and its
  creation operator does not type-check without it. If OCC has not
  reported, FCK must carry it as declared and census both ways, as
  this unit did.
- **The leak theorem, as a mechanism and not as numbers:** the
  Sym² cell 2·U_ax·U_ay argument works at every n (take a
  configuration with two distinct occupied sites and map both to
  one), so *exclusion excludes the symmetric shape at every
  excitation number* under the same closure premise. Free, and
  should be re-derived rather than cited.
- **The ordered-sector theorem at general n**, by telescoping:
  Xⁿ − Yⁿ = Σ_k Y^{⊗k} ⊗ Δ ⊗ X^{⊗(n−1−k)}, with
  X^{⊗n} = Y^{⊗n} ⟺ X = Y for row-stochastic X, Y. So **labelled
  quanta never carry a genuine n-body defect under a free lift**;
  every many-body interference in a free theory's Born shadow is
  symmetrisation. FCK gets this for nothing and should gate it.
- **The n = 2 sector count does NOT lift.** S_n has more than two
  irreps for n ≥ 3 and parastatistics-shaped sectors genuinely
  exist. FCK/SPT must re-ask "how many sectors" and will get a
  different answer; nothing in this unit forecloses it.
- The description-stamp discipline, the four walls, the shape words,
  the counting-only stamp, and `NO-TRANSPORT-NUMBER-INHERITED`.

**(R4) WHAT SPT (the species table) INHERITS — the sector
structure.**
- The sector decomposition **only as an n = 2 template**; the
  species table is stratified at fixed excitation number until FCK
  lands, exactly as the charter amendment (#194) says.
- **The defect as a species discriminator, with its measured
  blindness.** The transferable statement is not "588" but: *a
  species table built on the composition defect can only separate
  species on the pairs where the substrate interferes, and is blind
  on the Markovian complement.* Here that is 588 of 3364 — the
  blindness is the larger set. Any species claim resting on
  Born-level discrimination must publish its blind set.
- **The spectral discriminator**, which is independent of the defect
  and has the same size (16 cells at 58 of 58 families): two
  channels, one gap. SPT should carry both, because they are
  different subspaces with the same dimension and only the number is
  claimed here.

**(R5) THE CONTACT HANDLE'S SCOPE — inheritable, with its price
list.** It is a *declared operator, not a theory*: diagonal in the
configuration basis, exchange invariant, a single ζ₈ phase on the 16
doubly occupied configurations, one free parameter of a declared
eight, no configuration measure and no action behind it. Its
invisibility to the antisymmetric shape is **forced** (the wedge has
no doubly occupied configuration) and generalises to every n (the
wedge has no repeated site at any n); its *visibility* census —
58 of 58 families, 588 of 3364 pairs — does not generalise and is a
family fact of this stratum. Anyone promoting it to an interaction
owes a configuration measure and an action, which the charter
assigns to SMU/ACT, and owes a re-pricing of the phase.

**(R6) A REGISTERED CURIOSITY, offered without a claim.** The unit's
three probe sets coincide, and the two-excitation nonzero set is
exactly 3× the single-excitation one (1764 = 3·588). Nothing in the
paper claims the factor and nothing here licenses it; but if it
survives at L = 8 or d = 3 it is a law, and if it does not it is an
arithmetic coincidence of one stratum. The persistence units
(PER-L, paper-28) can answer it at no marginal cost.

---

## 11. GRADE

**AWF — accept with fixes.** Zero false computed numbers in 65
independent recomputations; every structural count rederived; the
head derived, pre-registered, rendered from the receipt and
byte-identical to the paper's fence; the gates bind objects; the
disclosure machinery exists and works where it is applied; the
walls hold (no particle, no spin, no general n, shape words only);
and the paper's central honesty — *the substrate does not select a
statistics, a declaration does* — is exactly right and is the most
important sentence in the unit.

The six MAJORs are all repairable in prose plus roughly forty lines
of instrument, and two of them **strengthen** the paper: the
indistinguishability result and the exclusion result are theorems,
not censuses, and the unit is entitled to say so. The one finding
that subtracts is MAJOR-2, and it subtracts an argument the paper
did not need — the record layer's silence on occupancy is a better
fact than any inference from a sweep bound, and it is measurable.

I would not sign the paper while §3 and the sealed waiver ledger
assert that a forced split is not forced, while §4 argues from a
link-count sweep box to a site occupancy, or while §9 says "on this
arena" about a stratum. With those three repaired and the other
three landed, this is a terminal-grade unit.

*Every number in this review was recomputed under
`/opt/homebrew/bin/python3.13` in exact arithmetic
(`fractions.Fraction`, Z[ζ₈] integer coordinates), scratch-only, with
no import of the delivered instrument. Between delivery and
adjudication every headline is a candidate reading, this one
included.*
