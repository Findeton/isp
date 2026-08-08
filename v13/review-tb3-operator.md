# TB3 — HOSTILE REVIEW R1, OPERATOR / ALGEBRAIC LENS

**Reviewer:** R1 (operator-system / algebraic).
**Protocol:** `v13/note-tb3-hostile-protocol.md` (FROZEN, kill-shots K1–K5).
**Pin:** `v13/note-tb3-third-base-pin.md`.
**Object, SHA-256 verified before reading (all four match the protocol):**

| file | sha256-12 declared | measured | ✓ |
|---|---|---|---|
| `v13/paper-tb3-third-base.md` | `0a9c5dff0e92` | `0a9c5dff0e92` | ✓ |
| `v13/code/tb3_third_base_exact.py` | `0fe72a05970b` | `0fe72a05970b` | ✓ |
| `v13/code/tb3_third_base_output.txt` | `a14684073857` | `a14684073857` | ✓ |
| `v13/code/tb3_third_base_receipt.json` | `3cd7981d173e` | `3cd7981d173e` | ✓ |

**Method.** Nothing of the instrument is imported. I re-derived the base from
§2's declarations and the operational definitions in the source, in an
independently written library using different data structures (row-major
sparse rational matrices against the instrument's column-major), a different
graph traversal (DFS spanning trees in declared / reversed / four shuffled
link orders against its BFS), and a different group-order algorithm (a
Schreier orbit-stabiliser chain that never enumerates the group, cross-checked
against explicit enumeration and against orbit × stabiliser at the first moved
point). The triangle census is taken by a third route again: the triangle
defect is a product of three drawn wing maps and therefore always lies in the
six-element wing group, so I count with multiplicity lists and a 6 × 6
multiplication table on wing indices — no adjacency walk, no matrix, no rule
triple loop. All arithmetic is exact over ℚ.

**Recomputation count: 119 distinct claim-level recomputations**, across nine
independently written scripts (base declarations 19; A1 census and group
family 31; A2 forms, cocycle and reference structure 14; A3 censuses and
criterion counts 13; A4 4; A5 2; controls, scope sweeps and forced-ness probes
15; the naming addendum 10; the two-sevens / linearity audit 11), plus a
normalising-but-escaping probe search in two concurrent scans (201 normalising
instances fully censused, ≈2,800 instances screened).

**Headline.** I found **no computational error**. Every number I recomputed
from the delivered receipt matched exactly, including the four holonomy orders,
the 1,226,304-triangle census, the two-wing anchors and the negative controls.
The defects are of a different kind: several of the unit's headline counts are
**algebraic identities presented as measurements**, two stated conclusions are
**scope-dependent in a way that reverses them**, one stated mechanism is
**measured false**, and the flagship A3 census's zero is **forced**. All are
repairable inside the delivered framework.

---

## 1. FINDINGS

### F1 — MAJOR. A2's headline counts are algebraic identities, not measurements.

The instrument *defines* the defect by reading it off the conjugated leg
matrix: `D = (P u P⁻¹)ᵀ u`. For **any** orthogonal `u` and **any** permutation
matrix `P` this is, in one line,

    (P u P⁻¹)ᵀ u  =  P uᵀ Pᵀ u  =  P u⁻¹ P⁻¹ u  =  [P⁻¹, u].

So `F3 ≡ D` identically. Recomputed on **40 random orthogonal 64 × 64 legs
built from Givens rotations that have nothing to do with this base: 0
deviations.** The "54 of 54" is not a measurement that could have come out
otherwise, and no perturbation of the physics can move it.

The same line forces the rest of §4.1's table:

- `F1 = P u⁻¹ P u` equals `D` **iff `P² = 1`**, for every `u`. Random-leg sweep
  over 240 cells: `F1 = D` at **160/160** involution cells and **0/80**
  three-cycle cells. So "36 of 54, precisely at the involutions" is
  9 members × |{P ∈ S₃ : P² = 1}| = 9 × 4 = 36, forced.
- `F1 = (Σ Vᵀ Σ V) ⊗ Σ²`, so "F1 splits off the pointer identity at 36 of 54"
  is the same statement about `Σ² = 1` again.

The unit correctly labels the **cocycle** a disclosure ("forced by algebra in
one line") but does not extend the same label to the form comparison, which is
forced by the same line. §4.1's "evaluated blind … read off the conjugated leg
matrices, not off any formula" and deviation 6's "it is not chosen to make an
equality come out" both read as claims of empirical content that does not
exist. RUNBOOK §14 addendum (v13 #208): *analytically-forced clauses are
disclosures, not must-pass gates.*

Consistently, no mutant in the 42-mutant table can falsify the 54/54: the two
that hit `TB3-A2` are `cocycle-drop` and `form-order`, and `form-order` works
by replacing F3's *expression* with garbage, not by perturbing a computation.

**Repair.** State the identity in §4.1; mark 54/54, 36/54 and the pointer-split
row `[FORCED]`; keep `TB3-ONE-LAW-GENERALIZES` but present its content as what
it is — *the four-factor writing is order-of-conjugation dependent and
coincides with the group commutator exactly on involutions* — an algebraic
remark, correctly drawn, about a two-wing notational accident.

**Related (MINOR).** The generalised form is unique only relative to a side
convention. The declaration `σuσ⁻¹ = u·D⁻¹` yields `D = [P⁻¹,u]`; the equally
natural `σuσ⁻¹ = D⁻¹·u` yields `D′ = u σ u⁻¹ σ⁻¹ = [u⁻¹, σ⁻¹]`, a conjugate of
`D` with the same order generating a conjugate subgroup. The unit does not vary
this convention, so "the right extension or one of several" is answered only
within one side convention.

### F2 — MAJOR. §3.2's stated mechanism — "the profile is what the geometry sees" — is measured FALSE.

§3.2: *"at three wings a single completion carries a **profile** of six orders,
and the profile is what the geometry sees."* The unit never tests this.

I tested it. On a random sample of **260 completions** at the same preparation,
setting, rule and base node, grouped by the full six-order profile over S₃:
**14 of the 153 distinct profiles carry more than one holonomy order.**
Examples, all checkable by re-running the instrument at those `Q`:

| profile (ABC, ACB, BAC, BCA, CAB, CBA) | holonomy orders realised |
|---|---|
| (1, 4, 4, 3, 3, 3) | 1008, 2160, 15120 |
| (1, 3, 5, 5, 5, 3) | 360, 15120 |
| (1, 5, 5, 2, 2, 3) | 360, 2160 |
| (1, 4, 3, 3, 3, 3) | 1008, 15120 |

So the holonomy order is not a function of the six-order profile any more than
of `ord[P*,u]`. The unit's own S7 argument (a lazy test passes vacuously,
so use a fixed-order sample) applies verbatim here and was not applied.

Aggravating: the receipt's only profile-adjacent field,
`a1_ord_sweep.the_order_is_a_function_of_ord_at_P_star_alone`, is **`true`** —
computed across four targets whose `ord`s are 1, 2, 3, 6, i.e. all distinct, so
the predicate cannot be false. It contradicts §3.3 and S7 and is untagged. See
F12.

**Repair.** Delete the mechanism sentence or replace it with the measured
statement; add the profile-collision test as a `[SAMP]` with its refutation;
tag or remove the receipt field.

### F3 — MAJOR. "The dihedral prediction holds at 0 of 4 targets" is setting-scoped, and the law SURVIVES at 3 of 4 at another setting.

Re-running the four rule-selected targets at other declared settings, same
instrument, same preparation, same completion rule:

| setting | stabiliser | ord 1 | ord 2 | ord 3 | ord 6 | targets where \|Hol\| = 2·ord |
|---|---|---|---|---|---|---|
| `TB-000` (R0,R0,R0) | 6 | 1 | 1008 | 72 | 15120 | **0 of 4** |
| (R1,R1,R1) | 6 | 1 | 1008 | 72 | 15120 | 0 of 4 |
| (R0,R0,R1) | 2 | 1 | **4** | 1 | 1 | 1 of 4 |
| **(R1,R2,R2)** | **2** | 1 | **4** | **6** | **12** | **3 of 4** |
| (R0,R1,R2) | 1 | 1 | 1 | 1 | 1 | 0 of 4 |

At `(R1,R2,R2)` the committed two-wing law `|Hol| = 2·ord[P,u]` is measured to
**hold** at three of the four targets. Deviation 2 discloses that A1 runs at
the fully symmetric setting only, but the abstract ("holds at 0 of 4 targets …
does not survive the wing-count change"), §3.2, §7's S5 row and §10's verdict
line ("fails at 4 of 4 targets") all state the failure unscoped.

This is not merely a scope defect — it is the unit's own thesis, measured and
missed. The law survives exactly where the setting's stabiliser has order 2,
i.e. where the *effective* symmetry group is the two-element one the law was a
law of. §1 argues in words that the law is a law of a two-element group; A1's
measurement scope excluded the settings that would have shown it.

**Repair.** Qualify every dihedral-law statement with the setting; add the
`(R1,R2,R2)` row; restate the finding as the stronger positive one — the law
tracks the setting's stabiliser, not the wing count.

### F4 — MAJOR. The ord-1 target's failure is a two-wing-known failure that this unit's own two-wing control reproduces, and the positive control conceals it.

XBA's committed corollary predicts `|⟨W,D⟩| = 2·ord`, i.e. **2** at `ord = 1`
(the receipt carries `XBA.group_orders_by_defect_order = {1: 2, 2: 4, 3: 6}`).
PSI's committed two-wing transport measures **1** at `ord = 1`, because the
identifications are refused. This unit's own two-wing positive control measures
**1** as well — I reproduce the whole row independently: 8 nodes, 11 links,
5 identification links, cycle rank 4, 52 based closed reduced walks,
`|Hol| = 1`.

So the dihedral law already failed at **two** wings at `ord = 1`. The receipt
handles this by recording `the_law_predicts_a_group_of_order: 1` at that row —
reading "the law's prediction" off PSI's *measured* order rather than off the
law `2·ord` (recorded separately as `twice_the_defect_order: 2`) — and then
reporting `the_prediction_is_met: true`. §8.1's "the group-order law's
prediction is **read out of PSI's receipt** rather than typed here, and met at
both orders" is literally true of that implementation and materially misleading
about the law.

Consequence for A1: one of the four "dihedral failures" is a failure already
present at two wings and for the same mechanism (refused identifications). The
wing-count-specific content of A1 is **3 of 4**, not 4 of 4.

**Repair.** Print XBA's `2·ord` prediction beside PSI's measured order at both
control rows; record that the two committed receipts disagree at `ord = 1`;
recount A1's headline.

### F5 — MAJOR. The A3 flagship census's zero is algebraically forced, and the "normalises" refinement's entire separation from the committed criterion is one forced cell.

The triangle defect is `d = P₃P₂P₁` with each `Pᵢ` a **drawn wing map**, so `d`
always lies in the six-element wing group `W`. At the declared base instance
all six wing symmetries lie in the level-1 group (I measure wings-in-Hol
**6/6**, matching `drawn_maps_contained_in_the_level_1_group: 6`). Hence every
one of the **1,226,304** triangle defects lies in `G` *by algebra*: the escape
count **cannot** be non-zero at that instance. §5.2 states the containment
mechanism honestly; the abstract, §5.1's table and §10 nonetheless present
"0 of 1,226,304 escape" as a measurement, and §8.2's control map claims the
census has teeth *at* the instances it is read at.

The criterion table is weaker than 5/5 vs 4/5 suggests. My own census (third
route) reproduces every cell:

| instance | \|Hol\| | triangles | escapes | cent | norm | why the agreement |
|---|---|---|---|---|---|---|
| declared base, TB-000 | 2160 | 1,226,304 | 0 | 1/6 | 6/6 | **closure forced** (`W ⊆ G`); normalisation forced by the same containment |
| equivariant control | 1 | 600 | 0 | 6/6 | 6/6 | normalisation **automatic** (`G = 1`) |
| partially symmetric TB-001 | 6 | 343,296 | 62,784 | 1/6 | 2/6 | genuine |
| asymmetric TB-012 | 1 | 216,720 | 0 | 6/6 | 6/6 | normalisation **automatic** (`G = 1`) |
| W-class, TB-000 | 6 | 343,296 | 62,784 | 1/6 | 2/6 | genuine — and numerically identical to row 3 |

Of the five agreements, two are automatic on the normaliser side, one is
forced on both sides, and the two genuine ones are the *same* instance
structurally (identical triangle count, identical escape count, identical
`|Hol|`, identical cent/norm). **The single instance at which the normaliser
criterion and the centraliser criterion disagree is the declared base — the one
whose closure is algebraically forced.** So "normalises 5/5 against centralises
4/5" rests on one forced cell.

Further, §11.5's claim that the refinement's *"sufficiency direction is forced
by the same argument COC gave"* is unsupported. COC's argument (COC §5,
verbatim: *"at an atlas whose generating group centralises the level-1
holonomy the conjugation in the telescoped defect is trivial"*) runs through
the **telescoped** defect, and §5.1 of this very paper declares the two-seed
telescoping reduction **unavailable** at six seeds. Neither direction is forced
at this atlas.

I attacked the refinement directly by hunting a **normalising-but-escaping**
probe over a grid of 9 preparations × up to 12 completions × up to 27 settings
in two concurrent scans; **201 normalising instances were carried all the way
through their triangle censuses** (each 216,720–1,226,304 triangles) and
**none escaped**. So the refinement is **not refuted** — its sufficiency
survives my attack empirically. But the mechanism I can state exactly is
neither containment nor normalisation:

> the cocycle closes at an atlas **iff every realised triple product of drawn
> maps lies in the level-1 group.**

Containment of the wing group in `G` is *sufficient* (forced). Containment of
the *drawn maps* is not necessary — the equivariant control has
`drawn_maps_contained = 0 of 5` and still closes, because its drawn maps are
the chart translations and telescope to the identity.

**Repair.** State the containment lemma and mark the reference instance's zero
`[FORCED]`; annotate the criterion table with which agreements are automatic;
withdraw "forced by the same argument COC gave"; state the criterion as the
triple-product condition, with containment as the sufficient condition it
actually is.

### F6 — MODERATE. "The maximum order the carrier admits is 6" is false; the carrier admits 7.

Exhaustive 5,040-completion censuses at every non-identity `P ∈ S₃`:

| P | σ cycle type | ord distribution | max |
|---|---|---|---|
| ACB (`P*`), BAC, CBA | 2²1⁴ | 48 / 384 / 1728 / 1152 / 1152 / 576 | 6 |
| BCA, CAB (3-cycles) | 3²1² | 18 / 270 / 1080 / 1296 / 648 / 432 / **1296** | **7** |

The measured quantity is the maximum **at `P*`**. Deviation 1 says so, but
§3.1's sentence ("The **maximum order the carrier admits** is 6, measured,
never typed") and the receipt key
`ord_census.the_maximum_order_the_carrier_admits: 6` are wrong as written, and
the receipt key is the one a downstream unit would read.

**Repair.** Rename to `the_maximum_order_at_P_star` in both places.

### F7 — MODERATE. "ord = 1 gives |Hol| = 1" is false; exhaustively, 46 of 48.

Exhaustive sweep of **all 48** completions with `ord([P*,u]) = 1` at ψ-G1,
TB-000:

| \|Hol\| | 1 | 18 | 24 | 72 | 360 | 1008 | 15120 |
|---|---|---|---|---|---|---|---|
| completions | **2** | 6 | 6 | 14 | 4 | 8 | 8 |

Only 2 of 48 give 1. A1's `ord = 1` row and §8.2's A1 negative control ("the
equivariant target: ord = 1 gives `|Hol| = 1` and the identifications
refused") are properties of the **identity completion**, not of `ord = 1`. This
also measures XBA's *existence* corollary read at the declared symmetry — "the
geometry is larger than ⟨P⟩ exactly where `[P,u] ≠ 1`" — **false at 46 of 48**
at three wings, which is a genuine and reportable new negative result the unit
does not have.

**Repair.** Say "the identity completion" rather than "ord = 1"; add the
48-completion sweep; add the corrected existence statement.

### F8 — MODERATE. "Two genuinely independent routes" fails the paper's own §11.8 criterion at two of the four censuses.

§11.8: *"'Two routes' here means two computations that share no intermediate
value, not two readings related by an algebraic identity."*

**(a) The holonomy group.** Routes A and B differ only in spanning tree
(breadth-first declared order vs depth-first reversed) and closure side. That
the based holonomy group is independent of the spanning tree is a **theorem**;
the routes are related by that identity, and their agreement carries no
information about the value. Deviation 7 explains why the base node was made
common — which removes the last source of independence. I confirmed the values
by a route that *is* independent (a Schreier orbit-stabiliser chain that never
enumerates the group; and orbit × stabiliser at the first moved point):
2160 = 3 × 720, 1008 = 3 × 336, 72 = 3 × 24, 15120 = 3 × 5040. **All four
confirmed.** The numbers are right; the independence claim is not. I also
re-ran with four further shuffled spanning trees: same group every time, as the
theorem requires.

**(b) The ord census.** Route 2 (the label commutator `σ⁻¹q⁻¹σq`) agrees with
route 1 (the 64 × 64 matrix defect) **only because `H(ψ_G1)` is Σ-equivariant
at all six wing symmetries** — which I measure, and which makes the matrix
defect reduce to `Σ V⁻¹ Σ⁻¹ V`, conjugate to the inverse of the label
commutator and therefore of equal order. At a non-equivariant member the two
"routes" measure different things: at ψ-W3 they **disagree at 400 of 400**
completions. Route 2 is not an independent route to the matrix defect; it is a
route to another object that coincides at the reference preparation.

**Repair.** Describe route B as an implementation cross-check and add a
genuinely independent order computation; scope route 2 with the equivariance
that makes it valid, and print the equivariance measurement beside it.

### F9 — MODERATE. "readable generators 47/61" and "leave the permutation class at 14 of 61" are spanning-tree artifacts.

Same 90-link graph at ψ-W4, six different spanning trees:

| tree | declared-DFS | reversed | shuffle-0 | shuffle-1 | shuffle-2 | shuffle-3 |
|---|---|---|---|---|---|---|
| readable / 61 | 45 | 40 | 45 | **34** | 43 | 41 |

The receipt's 47 is one tree's value; the range I measure is 34–45. The
invariant statement — *the holonomy group is not a permutation group*, i.e.
some loop's holonomy is not a permutation matrix — is true and well made
(§11.7 is exemplary about not filtering the unreadable loops away). The
**fraction** is not a property of the preparation.

**Repair.** Drop the fraction, or print it with its tree and the measured range
across trees.

### F10 — MODERATE. The `TB3-A3-CRITERION` gate contains no predicate about the criterion, and half its clauses are analytically forced.

    any(closes) and any(not closes) and cent_matches <= n and norm_matches <= n

The last two clauses are true for every possible input — a count of agreeing
rows over `n` rows cannot exceed `n`. RUNBOOK §14 addendum (v13 #208) forbids
analytically-forced clauses as must-pass content. What remains gates only the
census's non-degeneracy. **If `norm_matches` had come out 2 of 5, the gate
would still pass.** Consistently, the only mutant that falsifies this gate is
`legkey-lax`, which destroys the admission table — nothing tests the criterion
computation itself.

**Repair.** Re-derive the two agreement counts inside the gate from the
per-instance closure/centralise/normalise booleans and gate the derivation
(the §13 #234 pattern the unit applies correctly elsewhere); add a mutant that
perturbs the normaliser test.

### F11 — MODERATE. A typed boolean in a results table.

`a1_ord_sweep.the_two_wing_law_is_twice_the_commutator: False` is a hard-coded
literal in the source (`tb3_third_base_exact.py:1769`), not derived from
`dihedral_hits`. It happens to agree with the measurement. RUNBOOK failure
catalogue #24 — *"hard-coded 6561 (true 729) survived unit + round → counts
computed, never typed"* — is exactly this shape.

**Repair.** `"the_two_wing_law_is_twice_the_commutator": dihedral_hits == len(rows)`.

### F12 — MODERATE. A receipt field asserting the opposite of the paper's finding, computed vacuously.

`a1_ord_sweep.the_order_is_a_function_of_ord_at_P_star_alone: true`. Its
predicate compares the number of distinct `(ord, |Hol|)` pairs with the number
of distinct `ord`s over the four targets — whose `ord`s are 1, 2, 3, 6, all
distinct — so it is `true` for every possible input. §3.3 and §7's S7 conclude
the opposite from a purpose-built sample. A downstream reader of the receipt
alone is told the refuted proposition.

**Repair.** Remove it, or compute it on the S7 sample and name it after what it
measures.

### F13 — MINOR. "The commutator subgroup" is not the commutator subgroup.

Throughout, "the commutator subgroup" denotes `⟨[P,u] : P ∈ S₃⟩`, not the
derived subgroup `[Hol, Hol]`. They differ everywhere:

| instance | ⟨defects⟩ | [Hol, Hol] |
|---|---|---|
| reference | 360 | **1080** |
| target ord 2 | 168 | **504** |
| target ord 3 | 12 | **36** |
| target ord 6 | 2520 | **7560** |

In a paper whose thesis is *"the defect is the group commutator"*, using the
standard term for a non-standard object is a reading trap.

**Repair.** Rename to "the defect subgroup" and print `[Hol, Hol]` beside it.

### F14 — MINOR. Clause 1 of the admission predicate is vacuous by construction, not "measured inert".

`PCARR[π][0] = 0` for every `π ∈ S₃`, because label 0 = |000⟩ is fixed by every
wing permutation — and `admission()` already ranges over `S₃` only, so the
`j₀` filter can never reject. §2.8's "0 of 10 cells change" is correct but
reports as a measurement what is an identity. (Clauses 3 and 4 are genuinely
measured inert; only clause 1 is forced.)

### F15 — MINOR. A4's `E_P` biconditional is forced by the Householder construction.

`E_P(ψ) = Σ⁻¹H⁻¹ΣH = 1 ⟺ ΣH = HΣ`, and with `w = ψ − e₀`, `Σe₀ = e₀`, this is
`Σw = ±w`, i.e. `Σψ = ψ` (up to the degenerate `Σψ = 2e₀ − ψ` branch). I
measured it on **2,400 random (ψ, P) cells** built from rational unit vectors
unrelated to the family: **0 deviations**. "0 deviations over 54 cells, both
directions" is a disclosure, not a discovery. (The paper's *use* of it — the
per-member `E_P = 1` locus in §6.1 — is fine and informative.)

### F16 — MINOR. The "independent construction" gate on the three forms tests the tensor factorisation, not the forms.

`indep[F3] = kron(Σ Vᵀ Σ⁻¹ V)` differs from `F3 = P uᵀ P⁻¹ u` only by
substituting `P = Σ⊗Σ` and `u = V⊗I`, both separately measured elsewhere. The
gate is a real check on those two factorisations; §4.1's "a form that is not
what its name says kills the run before the verdict is read" overstates it,
since the 162-cell equality is an identity given the factorisations.

---

## 2. ADDENDUM (coordinator's charge): NAMING, THE ×7, AND THE CEILING

**Verdict: `TB3-NAMING-DECIDED — the ×7 is STRUCTURAL (an alternating point
stabiliser realised by genuine carrier 7-torsion), the embedding is CONCRETE,
the 168 is GL(3,2) acting linearly on the Fano points of this very substrate,
15120 is the construction's algebraic CEILING, and no name-collapse or
label-aliasing is present.`**

### (3) Name-collapse audit — done first, as instructed. Clean.

My groups are sets of explicit 64-point permutation tuples; there is no
canonicalisation, naming, hashing or label-collapse layer anywhere in my route.
Every order is confirmed by **three** routes:

| instance | explicit enumeration | Schreier chain (no enumeration) | orbit × stabiliser |
|---|---|---|---|
| reference / GHZ | 2160 | 2160 | 3 × 720 |
| target ord 2 | 1008 | 1008 | 3 × 336 |
| target ord 3 | 72 | 72 | 3 × 24 |
| target ord 6 | 15120 | 15120 | 3 × 5040 |

Every element was verified to be a genuine permutation of all 64 points. **No
counting artifact; the delivered orders are the true orders.**

**Route audit for label leakage.** The transport graph's links carry only leg
**matrices** (24 of them, 64 × 64 over ℚ) and `PCARR[π]` **carrier
permutations** (87 at the ord-6 target). The completion `Q` enters the counting
route at exactly one place — as input to `V = H(ψ)·M_Q` inside the preparation
leg — and no label tuple, completion index or census value is read by the
spanning tree, the generators, the closure or the order computation. The
5,040-completion census is a separate computation whose only output into this
route is the *choice* of `Q`. **There is no path by which a completion label
could be counted as a group element.**

### (3b) THE TWO SEVENS — audited, and they are the same seven, legitimately.

The coordinator is right that two sevens exist and right to demand they be
separated. My finding: **they are the same seven, and that identity is
structural rather than aliasing.**

The seven is `|F₂³ \ {0}| = 7`: the system-triple label space of three binary
wings **is** `F₂³`; the completion rule fixes label `0 = |000⟩` (so that
`Ve₀ = ψ`), leaving seven moved labels — which is simultaneously why the census
is `7! = 5,040` and why the defect groups act on seven points.

That the group-theoretic seven is *not* a label leak is settled by exhibiting
genuine 7-torsion **on the carrier**:

- `Hol` at the ord-6 target contains **720 elements of order 7**, all of them
  in `⟨defects⟩ = A₇`.
- An explicit witness, as a permutation of the **64 configurations**, has cycle
  type **8 seven-cycles + 8 fixed points** — e.g. the cycles
  `(8 16 24 32 40 48 56)`, `(9 17 25 33 41 49 57)`, `(10 18 26 34 42 50 58)` —
  and `x⁷ = id` verified. Its system-label part is the 7-cycle
  `(1 2 3 4 5 6 7)`; its **pointer-label part is the identity**, so the
  7-torsion is carried by the system factor of the carrier and nothing else.
- **The reference geometry (2160) contains 0 elements of order 7.** The ×7 is
  therefore exactly the 7-torsion the GHZ geometry lacks and the ord-6 target
  has — a genuine group-theoretic step, not a numerical coincidence.

### (3c) THE 168 IS `GL(3,2)` ON THE FANO POINTS OF THIS SUBSTRATE.

Simplicity was tested **first**, as instructed: the normal closure of every
non-identity conjugacy class of the order-168 defect group is the whole group,
so it is **simple**; simple of order 168 forces `PSL(2,7) ≅ PSL(3,2) ≅ GL(3,2)`
uniquely (of the many groups of that order, exactly one is simple).

The structural reading is then **earned**, not assumed:

- Every one of the 168 system images is **`F₂`-linear** on `F₂³` — i.e.
  `α(x ⊕ y) = α(x) ⊕ α(y)` for all 64 label pairs — at **168 of 168**.
- I built `GL(3,2)` independently by brute force over all 5,040 label
  permutations fixing 0: **168 elements**, and the ord-2 target's defect group's
  system image **equals that set exactly**.
- It permutes the **7 lines** of `PG(2,2)` (the triples `{x, y, x⊕y}`):
  **every element, all 7 lines**.

So this is not "a group that happens to have order 168": it is
`Aut(F₂³) = GL(3,2)` in its natural action on the Fano plane whose seven points
are the seven non-zero states of three binary wings. Given a base that is three
binary wings by construction, that is the most natural group the substrate
admits, and its appearance at a rule-selected completion is structural.

The neighbours confirm the reading by contrast: the ord-6 target's `A₇` is
**not** linear (exactly **168 of its 2520** elements are — precisely the
`GL(3,2)` inside `A₇`), and the reference's `A₆` is not linear either
(**24 of 360**). So `GL(3,2) ⊂ A₇` in the natural containment, and the ord-2
target is the completion at which the geometry sees the substrate's own linear
group and no more.

### (1) The five isomorphism types, decided by spectrum + simplicity + faithful degree — not by order.

Every holonomy element at these instances is of **product form**
`(α on the 8 system labels) × (β on the 8 pointer labels)` (measured, all four
instances), and every system-label image lies in the alternating group
(measured). That gives the faithful degree needed to fix the type.

| object | order | element-order spectrum | simple? | degree | **TYPE** |
|---|---|---|---|---|---|
| ⟨defects⟩, target ord 3 | 12 | {1:1, 2:3, 3:8} | no (min normal 4) | 4 | **A₄**, natural degree-4 action |
| ⟨defects⟩, target ord 2 | 168 | {1:1, 2:21, 3:56, 4:42, 7:48} | **yes** | 7 | **GL(3,2) ≅ PSL(3,2) ≅ PSL(2,7)**, and measured `F₂`-linear at 168/168 — the natural Fano action (§3c) |
| ⟨defects⟩, reference/GHZ | 360 | {1:1, 2:45, 3:80, 4:90, 5:144} | **yes** | 6 | **A₆** |
| ⟨defects⟩, target ord 6 | 2520 | {1:1, 2:105, 3:350, 4:630, 5:504, 6:210, 7:720} | **yes** | 7 | **A₇** |
| Hol, target ord 2 | 1008 | — | no (min normal 168) | 7 | **PSL(2,7) × S₃** |
| Hol, reference/GHZ | 2160 | — | no (min normal 360) | 6 | **A₆ × S₃** |
| Hol, target ord 6 | 15120 | — | no (min normal 2520) | 7 | **A₇ × S₃** |
| Hol, target ord 3 | 72 | {1:1, 2:21, 3:26, 4:18, 6:6} | no (min normal 12) | 7 | **NOT a direct product** |

Order alone does not fix any of these (162 groups of order 360, 15 of order
168, 5 of order 12); the spectra plus simplicity plus degree do. Each simple
identification is the *unique* simple group of its order.

The three direct products are verified internally: `C_Hol(⟨defects⟩)` has order
6, is non-abelian (spectrum {1:1, 2:3, 3:2}, hence `≅ S₃`), meets `⟨defects⟩`
trivially, and together they generate `Hol`.

**The `72` case breaks the paper's pattern and the paper does not say so.**
There `C_Hol(A₄) = C₃` only, `[Hol,Hol] = 36`, and `Hol ≅ (A₄ × C₃) ⋊ C₂` — the
wings' transpositions act on `A₄` as the outer automorphism. §3.2's "of order
6 × the commutator subgroup" is a correct *count* at three of four targets but
hides that only two of them (and the reference) are direct products.

### (2) The ×7: the embedding is CONCRETE, not merely numerical.

`|Hol_ord6| / |Hol_GHZ| = 15120 / 2160 = 7` exactly, and the containment is
real, not just divisibility:

- **`Hol_GHZ ⊆ Hol_ord6` as subgroups of Sym(64): TRUE. 0 of 2160 elements
  fall outside.**
- `⟨defects⟩_GHZ ⊆ ⟨defects⟩_ord6` (`A₆ ⊆ A₇`): **TRUE**.
- The mechanism is exact: the system-label image of `Hol_ord6` is `A₇` on the
  seven non-zero labels; the system labels fixed by **every** element of
  `Hol_GHZ` are `{0, 7}`, and the **stabiliser of label 7 inside `A₇` has order
  360 and is exactly the system image of `Hol_GHZ`** (verified as sets).

So `×7 = [A₇ : A₆]`, the index of a point stabiliser in the natural degree-7
alternating action. Label 7 = |111⟩ is a support label of
`ψ_G1 = ³⁄₅|000⟩ + ⁴⁄₅|111⟩`; the reference completion `Q = (1 3)` cannot move
it, which is precisely why the GHZ geometry sits one point-stabiliser step
below the ord-6 target.

### The ceiling — the structural fact the paper is missing.

Every defect is a commutator of label permutations fixing label 0, hence an
**even** permutation of the seven non-zero system labels; every wing `Σ_π` is
even too (`Σ` for a transposition is `(1 2)(5 6)`, for a 3-cycle
`(1 2 4)(3 6 5)`). I measured "system image inside Alt" = **true** at all four
instances. Therefore

> the system image of **any** holonomy group at this base lies in `Alt(7)`, and
> with the six wing symmetries the algebraic ceiling is
> `|A₇| × |S₃| = 2520 × 6 = **15120**`.

**The ord-6 target attains the ceiling** (verified: `|Hol| = 15120`). This is
the exact answer to the pin's A1 question — *"does S₃'s non-abelianity open a
larger family?"* — that the paper does not give: the family is the lattice of
subgroups realisable below `A₇ × S₃`, its top is realised, and the largest
number in the paper is a maximum rather than a discovery. It also explains the
whole delivered family at once: `A₄ × ⋯ < PSL(3,2) < A₆ < A₇` are all subgroups
of `Alt(7)` in its degree-7 action, and `1, 72, 1008, 2160, 15120` are their
six-fold extensions (except at 72, where the extension is non-split).

**Repair.** Add the `Alt(7)` ceiling lemma, the naming table, the concrete
containment and the point-stabiliser mechanism to §3.2 and §4.4; add the
`GL(3,2)`/Fano identification with its linearity measurement and the carrier
7-torsion witness; correct the "6 × the commutator subgroup" row to distinguish
the three direct products from the non-split case at 72.

**Why this matters beyond naming.** The delivered family
`1, 72, 1008, 2160, 15120` is not an unstructured list of "what the geometry
opens up". It is the ladder
`1 < A₄ < GL(3,2) < A₆ < A₇` inside `Alt(7) = Aut(F₂³)`-adjacent structure,
six-fold extended by the wing group, with `GL(3,2)` the substrate's own linear
group and `A₇` the ceiling. That is a stronger and cleaner answer to the pin's
A1 question than "it opens a larger family", and it is available from the
delivered numbers without any new machinery.

---

## 3. WHAT SURVIVED — recomputed exactly, no deviation

Reported so the fixes above are read against a correct instrument.

**Base (§2).** 64 configurations and the index bijection; wing group order 6,
measured non-abelian, element orders {1,2,3}, closed over all 36 compositions;
`P_π = Σ_π ⊗ Σ_π` at all 6; `P U_w P⁻¹ = U_{π(w)}` at **54/54**; all rotations
and all legs exactly orthogonal; distinct-wing legs commute at all 27 unordered
pairs; 27 settings with stabiliser profile **{6:3, 2:18, 1:6}**; all nine
preparations' classes, 3-tangles, norms, wing stabilisers and Born-shadow
stabilisers (including ψ-W4's asymmetry: wing stabiliser 1, Born-shadow
stabiliser 2); the completion rule returns `Q = (1 3) = (0,3,2,1,4,5,6,7)`;
`V` orthogonal with `Ve₀ = ψ`.

**A1.** Census size **5,040**; distribution **48 / 384 / 1728 / 1152 / 1152 /
576**; max at `P*` = 6; **310** distinct profiles over S₃; the lex-first `Q`
per order, all six, identical to the receipt; the matrix route's orders at all
six; a third route on 300 sampled completions, 300/300. The four target rows —
links **99 / 150 / 111 / 111**, cycle rank **70 / 121 / 82 / 82**, holonomy
**1 / 1008 / 72 / 15120**, defect subgroup **1 / 168 / 12 / 2520**,
⟨defects, wings⟩ **1 / 1008 / 72 / 15120** — all reproduced by three routes.

**A2.** Form hits **36 / 36 / 54**; involution hits **36 / 36 / 36**; pointer
splits **36 / 54 / 54**; cocycle 0 deviations at 54 cells; the factorisation
instantiation 0 deviations; **my own** 200 seeded triples (seed
`sha256("R1-OPERATOR-LENS-TB3-2026-08-08")`, not theirs) give 0 cocycle
deviations, 200/200 exactly orthogonal draws and **172** triples where the
mirror order differs — so the non-vacuity claim replicates under a different
seed. Reference: `|Hol| = 2160`, defect subgroup **360**, **normal** under the
wings and in `Hol`, `Hol = ⟨defects, wings⟩` and **not** `⟨defects⟩` alone.

**A3.** All five instances by my third census route: **1,226,304 / 0**,
**600 / 0**, **343,296 / 62,784**, **216,720 / 0**, **343,296 / 62,784**; 36
charts over 6 seeds (6 charts at the equivariant control); centralising counts
1/6, 6/6, 1/6, 6/6, 1/6 and normalising counts 6/6, 6/6, 2/6, 6/6, 2/6 — every
cell matches.

**A4.** The `E_P = 1` locus per member; the witness pair — `psi-W1` and
`psi-W4` share the Born shadow of `V`, agree on the admission table cell for
cell, both carry 90 links and cycle rank 61, and `psi-W4`'s generators leave
the permutation class; the in-family negative control `psi-G3` reproduces
`psi-G1` exactly (same Born shadow, same admission table, `|Hol| = 2160` both).

**A5.** The S7 sample: the same five lex-first `ord = 3` completions,
`|Hol| = 72, 72, 72, 72, 2160` — **two values**, refutation reproduced.

**Controls.** Two-wing positive control at both realised orders, element by
element: `ord = 3` → 8 nodes, 13 links, 7 identification links, rank 6, **364**
based closed reduced walks, `|Hol| = 6`, class profile
**42 / 46 / 46 / 72 / 78 / 80**; `ord = 1` → 8, 11, 5, 4, **52**, `|Hol| = 1`.
Negative controls: equivariant 99 / 70 / 1, transposition (1 2) 111 / 82 /
**18**, asymmetric 75 / 46 / 1, reference 150 / 121 / 2160.

**K2's two-wing coherence check — PASSES.** Restricting the generalised law to
two wings: over 4 completions × 3 settings × 2 wing symmetries = 24 cells,
`F1 = F2 = F3 = D` at **24/24**, because `P² = 1` there. The generalised form
`[P⁻¹, u]` therefore recovers PSI's committed `D = [P, u]` **verbatim** at two
wings, and the committed corpus is not disturbed. This is the one place the
generalisation had to be checked and it is clean.

---

## 4. GRADE

The instrument is sound and the arithmetic is correct: across 119 independent
recomputations I found **zero** wrong numbers in the delivered receipt, and the
one place where the corpus could have been broken — the two-wing restriction of
the generalised law — is clean. The unit's discipline (declared arena, printed
scopes, the ψ-W4 absence carried rather than hidden, the `[SAMP]` tags, the
deviations appendix) is largely of the standard the programme asks for.

But four stated conclusions do not survive contact:

- the profile mechanism (§3.2) is **measured false** (F2);
- the dihedral headline is **reversed at another declared setting** (F3), and
  one of its four failures is **already a two-wing failure** (F4);
- the flagship 1,226,304-triangle zero and the criterion refinement's
  separation from the committed criterion are **algebraically forced** (F5);
- and A2's headline counts are **identities presented as measurements** (F1).

None of these is a false number and none requires new machinery to repair; all
are statements the delivered instrument can correct in a fix pass. That is the
boundary between AWF and REJECT, and this falls on the AWF side.

**Binding fixes (F1, F2, F3, F4, F5, F6, F7, F8, F10, F11, F12) must be made
before A1's and A3's statements can stand as written. F9, F13–F16 are
recommended. The naming addendum's content — the `Alt(7)` ceiling, the four
isomorphism types, the concrete index-7 embedding, the carrier 7-torsion
witness and the `GL(3,2)`/Fano identification — should be added; it strengthens
A1 rather than weakening it, and it supplies the structural answer the pin's A1
question asked for and the paper left as a list of numbers.**

> ### GRADE: ACCEPT-WITH-FIXES
