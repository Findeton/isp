# R4c (paper-22) — K1 OPERATOR REVIEW

**Seat:** K1, operator lens (rebuild from nothing; attack the headline; verify
claimed theorems *as theorems*).  **Protocol:** v14 ledger #200, row K1.
**Object:** commit `4f89135`.

**Hashes, verified at start and at end** (sha256-12, worktree against
`git show 4f89135:`):

| object | hash | start | end |
|---|---|---|---|
| `v14/paper-22-multi.md` | `1b4ac134e727` | ✓ | ✓ |
| `v14/code/r4c_multi_exact.py` | `deb0c1c83a76` | ✓ | ✓ |
| `v14/code/r4c_multi_output.txt` | `45866a3ed5e3` | ✓ | ✓ |
| `v14/code/r4c_multi_receipt.json` | `5c058006db78` | ✓ | ✓ |
| `v14/note-r4c-pin.md` | `162553b03ca9` | ✓ | ✓ |

**GRADE: AWF (accept with fixes).**  Every *computed number* I could reach is
correct — I reproduced the entire census independently and found no false
number anywhere.  Three claims are nevertheless wrong as written, one of them
the unit's own headline finding, and all three are repairable without moving a
single measured value.

---

## 1. What I rebuilt, and with what

Nothing below reads `r4c_multi_exact.py` as an oracle.  I built my own machinery
from the parents' *definitions* and gated it against the parents' *published
receipts*:

- **Field.** Q(ζ₈) as integer 4-tuples over a tracked power-of-two denominator
  (`(a₀,a₁,a₂,a₃)`, ζ⁴ = −1), with a second, independent pure-`Fraction` dense
  implementation used as a third route for the decisive witness.  Where Born
  shadows leave Q — they do, for coin composites — I carried them exactly in
  Z[√2] as integer pairs `(p,q) ↦ p+q√2`.  No float anywhere; every product is
  int64 with a proved magnitude bound (max intermediate ≈ 9·10⁶).
- **Family.** Rebuilt from paper-10 §3: 9 axes (nonzero offsets mod sign), the
  stencil {0,a,−a}, the delta-autocorrelation unitarity criterion, the declared
  25-element alphabet, the global-phase gauge quotient.
- **Controls.** Rebuilt from the parents' declared definitions (Hadamard coin on
  the parity dominoes along e ∈ {(1,0),(0,1)}; the declared site transpositions
  (0,5) and (1,11)).
- **Sectors.** My own wedge and my own normalised symmetric square, my own
  256-dimensional lift and my own exchange operator, checked against each other.
- **Off-tree.** All runs in
  `…/scratchpad/r4c-op/` and in a provisioned mirror built with
  `git show 4f89135:<path>`; the repo tree was never written to except this file.

**Recomputations: 88**, counted honestly (one per independently recomputed
quantity or per-object predicate family, not one per cell).  Listed inline
below; the heavy ones are the 3364-pair defect census (three sectors), the
43200-row overlap census, the 29696-cell velocity census, and the 3306-pair
distinguishable-lift census.

**Gate on my own rebuild.** My 58 gauge classes stand in bijection *both ways*
with R4's published pool (zero collisions, zero unmatched), monomiality agrees
object by object, and my 16 monomial names are literally the parent's anchored
list `C004 C007 C008 C011 C018 C019 C026 C027 C034 C035 C042 C043 C046 C053
C054 C057`.  Per-axis raw unitary counts reproduce R4's order census exactly
(72 at each of the six order-4 axes, 32 at each of the three order-2 axes).
Unitarity re-verified by the adjoint route on all 58.  *(recomputations 1–13)*

---

## 2. What reproduces — the census of confirmations

Every one of these is my own number, obtained without the delivered program.

**The exchange census (target 1).** Commutation of my exchange with my free lift
at **64 of 64**; both sectors invariant (I measured the off-block matrix
elements ⟨anti|Λ|sym⟩ and ⟨sym|Λ|anti⟩ directly, not merely the restriction's
unitarity) at 64/64 each; both restrictions unitary at 64/64 by two routes; both
Born shadows stochastic **in rows and in columns** at 64/64; the two routes to
the sector Born shadow agree 128/128.  *(14–21)*

**The decomposition (target 1).** P² = I and tr P = 16, hence dim(+1) = 136 and
dim(−1) = 120, 136 + 120 = 256.  The no-parastatistics argument holds exactly as
the paper scopes it: over a field of characteristic ≠ 2, C[S₂] has two
irreducible characters, so the isotypic decomposition of *any* S₂-module has
exactly two components — an argument about n = 2 and nothing more, which §3 and
§10 say.  *(22–23)*

**The ceiling-1 leak (target 3).** The symmetric sector leaks at **48 of 64**,
and the leaking set *equals* the non-monomial set element for element; the
antisymmetric sector leaks at 0/64.  *(24–26)*  — but see **MAJOR-2**.

**The fixed-point theorem (target 2).** Verified, and strictly stronger than
gated.  The one-excitation configuration sets of the two ceilings are the same
16 configurations; for **all 64 generators** the one-excitation restriction is
the same matrix *and* the same Born shadow; and the entire single-excitation
defect census (4096 ordered pairs of the full pool) is bit-for-bit the same
object under both declarations.  Universality therefore holds as a theorem and
not as an induction over observables: the two arenas are *equal as labelled
dynamical systems* at one excitation, so every function of them agrees.  No
single-excitation observable whatever can separate the ceilings.  *(27–29)*
— but see **MINOR-3** on how this is gated.

**The four arenas (target 4).** A4: the exchange fails to commute with the
distinguishable lift at **3306 of 3306** ordered pairs of distinct circulants
(zero proportional pairs), and — measuring what the instrument only asserts — at
all 3306 **neither** sector is invariant.  Two-way control: on the free lift both
sectors are invariant at 64/64.  A3: dim Λ² = n(n−1)/2 = 0 and dim Sym² = 1 at
n = 1, confirmed by explicit construction.  *(30–34)*

**The defect census (target 5).** Single-excitation nonzero **588 of 3364**;
symmetric **1764**; antisymmetric **1764**, and the two nonzero *sets* coincide;
ordered-sector nonzero **588**, set-equal to the single-excitation set; genuine
two-body **1176**; losses **0**; the per-pair predicate NONZERO ⟺ BOTH LEGS
NON-MONOMIAL with **0 mismatches over 6728** tests; 42 non-monomial circulants,
42² = 1764.  Functoriality of both sector lifts verified over the **whole**
census (3364/3364), not a window — this is the binding the paper's "second code
path" claims, obtained here by a different construction.  *(35–48)*

**The value censuses, cell for cell.** My antisymmetric two-excitation value
multiset equals the receipt's exactly — 28 distinct values, every cell count
identical, **1,126,656** cells in total — computed by a construction that shares
no code, no field representation and no scaling convention with the instrument.
My block-restricted symmetric multiset likewise reproduces the receipt's 30
values exactly (which is what makes MAJOR-3 below a scope defect and not a
disagreement).  *(87–88)*

**The parent reproduction (targets 5, 9).** My single-excitation value multiset,
read in the parent's separation-indexed form, equals R4's published multiset
value for value and cell count for cell count: +1/2:108, +1/4:336, +1/8:144,
+5/8:24, −1/2:108, −1/4:336, −1/8:192, −3/8:24.  Eight distinct values.
*(49–52)*  R4b: speed spectrum {0,1,2}, **1856** velocity cells, **320**
antipodal-tie cells in **19** families — all reproduced under R4b's declared
convention.  *(53–55)*

**The 588 triple set equality (target 8).** All three characterisations return
the *same 588 pairs*, as sets: (i) the single-excitation defect set; (ii) the
set where the two shapes' two-excitation defect **value multisets** differ;
(iii) the set where the declared contact handle moves the symmetric shape's
defect.  A fourth, the ordered-sector defect set, is the same set again.  I
additionally probed the handle's declared phase: the moved set is the same 588
at ζ₈¹, ζ₈², ζ₈³ **and** ζ₈⁴ = −1 — the claim is not phase-relative.
*(56–61)*  — but characterisation (ii) is not what the paper says it is: see
**MAJOR-1**.

**The support-overlap lift (target 6).** With my own coin alphabet and my own
declared coin pairs (different coins from the instrument's, since the alphabet
enumeration order differs): 640 coins, 512 interfering, 32 links, 120 two-site
supports — R5's anchored counts.  The table:

| overlap | rows | one excitation | antisymmetric | symmetric |
|---|---|---|---|---|
| 0 | 32760 | 0 | 0 | 0 |
| 1 | 10080 | 0 | 0 | 0 |
| 2 | 360 | 360 | 360 | 360 |

42840 of 42840 rows carry no defect at overlap ≤ 1, at all three levels; 360 of
360 carry one at overlap 2; each of my three coin pairs gives the whole table on
its own (10920 / 3360 / 120).  The three-site question: 1536 full-support unit
rows over the alphabet, **0** completions to a unitary.  *(62–68)*

**Motion (target 7).** Eigenphase additivity verified as exact eigenvector
identities (not symbol arithmetic): 928 single-excitation cells, **6960**
antisymmetric and **7888** symmetric two-excitation cells, **0** failures.
Spectral split at 58/58 families with a gap of **16** doubled-momentum cells.
Velocity: **7168 of 29696** cells fail to add, failing lift pairs exactly
{(2,2), (−2,−2)}; speed spectrum {0,1,2} at one and at two excitations.
*(69–78)*  — with two refinements, **MINOR-4** and **MINOR-5**.

**Artifacts and CLI (target 10).** The verdict string is byte-identical across
paper, receipt and (re-joined) output — 2353 characters, string equality.  An
off-tree mirror run reproduces **both artifacts byte-identically** to the
committed objects (`45866a3ed5e3`, `5c058006db78`), exit 0, 63/63 gates, 56/56
mutants dead.  Five hostile argv probes (`--nope`, `--mutant`, `--mutant NOPE`,
`--break-anchor NOPE`, `--verify-paper --nope`) each exit 2.  Three mutants
re-run **outside** the harness, from the mirror, each dying at its declared gate
with the raising gate parsed from the message:

| mutant | died at | target | verdict | exit |
|---|---|---|---|---|
| `MUT-CEILINGS` | `G-CEILINGS-AGREE-AT-ONE-EXCITATION` | same | ON TARGET | 1 |
| `MUT-LEAK-ZERO` | `G-HARDCORE-LEAK-PER-GENERATOR` | same | ON TARGET | 1 |
| `MUT-DISCRIMINATION` | `G-SHAPES-DISCRIMINATED` | same | ON TARGET | 1 |

*(79–86)*  Numeral sweep: every numeral in the prose is confirmed by my own
measurement, with the single exception recorded in MAJOR-3.

---

## 3. Findings

### MAJOR-1 — the discrimination claim is a *value-multiset* claim, and the paper states it as a claim about the defects.  The unit's headline finding is wrong as written.

The instrument's `differing` set is built from `value_multiset(Dw) != value_multiset(Ds|block)`
(`raw_defect_census`), and `G-SHAPES-DISCRIMINATED`'s own gate text says so
("differ **as value multisets**").  The paper drops the qualifier everywhere:

- §6: "the symmetric and antisymmetric two-excitation defects **differ at 588 of
  3364 ordered pairs and agree at 2776**";
- §6: "**Where the substrate is classical across the cut, the two shapes are
  indistinguishable by the defect.**";
- §6/§9: "a statistics the composition defect can read — **and it can read it
  nowhere else**";
- §10 bullet 5; and the verdict segment `DISCRIMINATION=THE-SHAPES-DIFFER-BY-THE-DEFECT-AT-588-OF-3364-PAIRS…;AGREE-AT-2776`.

Measured entrywise, on the same shared hard-core block, in the same row/column
ordering, at a common denominator:

> **the two shapes' two-excitation defects differ at 1764 of 3364 ordered pairs
> and agree at 1600** — and the differing set is *exactly* the set on which the
> two-excitation defect is nonzero, i.e. exactly the pairs whose two legs are
> both non-monomial.  They agree only where both defects vanish.

Witness, verified by three independent routes (numpy int64 4-tuples; the same
with a different scaling convention; and a dense pure-`Fraction` route sharing
no code with either): the pair **(C000, C012)** carries **no** single-excitation
defect at all, and its two-excitation defects differ at **576** cells —
e.g. at row {0,4}, column {0,1}: symmetric **+1/32**, antisymmetric **−1/32**;
at row {0,4}, column {0,5}: **−1/32** against **+1/32**.  Their value multisets
are equal ({±1/32: 128 each, ±1/64: 128 each, ±1/128: 32 each}), which is why
the instrument's criterion does not fire.

So the shapes are told apart by the defect wherever the two-excitation defect
lives — including all 1176 genuine two-body pairs, where the substrate's
one-excitation composition does *not* interfere.  What is confined to the 588 is
the *relabelling-invariant* (multiset-level) discrimination.  The physical
sentence the unit closes on — statistics is readable "exactly where the
substrate is quantum", "and nowhere else" — is false at the natural reading and
true only at the multiset reading, which the paper never states.

**Repair (exact).**
1. Instrument: add the entrywise census beside the multiset one, and gate it —
   `G-SHAPES-DISCRIMINATED-ENTRYWISE`: the set of pairs at which the two
   shapes' two-excitation defects differ cell by cell equals the two-excitation
   nonzero set (1764), a set equality; keep `G-SHAPES-DISCRIMINATED` with its
   existing multiset clause and set equality against the 588.
2. Verdict: `DISCRIMINATION=THE-SHAPES-DIFFER-CELL-BY-CELL-AT-1764-OF-3364(=THE-TWO-EXCITATION-DEFECT-SET);VALUE-MULTISETS-DIFFER-AT-588-OF-3364=EXACTLY-THE-SINGLE-EXCITATION-DEFECT-SET(SET-EQUALITY);MULTISETS-AGREE-AT-2776;…`
3. Paper §6: state both readings, and replace the closing paragraph with the
   corrected physics — the exchange shape has Born-level consequences at every
   pair where the two-excitation defect lives; what is confined to the pairs
   where the substrate already interferes at one excitation is the coarser,
   relabelling-invariant signature.  §9's "again, that set" must acquire the
   same qualifier (the handle comparison *is* entrywise — that one is sound).
4. §10 bullet 5 and the abstract sentence "and it can read it nowhere else"
   must be rewritten or deleted.

Note the repaired statement is *cleaner*, not weaker: the entrywise-differing
set is exactly the both-legs-non-monomial set, so §5 and §6 collapse into one
law rather than two.

### MAJOR-2 — §3's claim that the hard-core leak census's "split is not forced" is false; the leak split is a one-line theorem, and it is the gate the unit nominates to replace the disclosed exchange commutation.

§3: "It is registered as a disclosure with its forcing named, and the
measurement that takes its place is the hard-core census of the next section,
**whose split is not forced** and which separates the pool."  §11 repeats the
nomination ("the exchange commutation against the hard-core leak"), and the
waiver ledger says the antisymmetric closure's "measured content beside it is
the symmetric sector's leak, which fires".

**Theorem.** Let U be any unitary on C^X.  In the normalised symmetric square,
the matrix element from a hard-core configuration {x,y} (x ≠ y) to a doubly
occupied configuration {a,a} is √2·U[a,x]·U[a,y] — a single product, and the
field is a domain, so it vanishes iff one factor does.  Hence Sym²(U) leaks out
of the hard core iff some row of U carries two nonzero entries, i.e. iff U is
not monomial (a unitary with at most one nonzero per row is monomial).  The
wedge has no doubly occupied configuration, so Λ²(U) never leaks. ∎

Both halves are therefore forced, for every unitary whatever — not properties of
this family.  Measured confirmation out of family: on the 3364 **composites**
U₂U₁ (unitaries the pool does not contain, with column supports up to 9), the
equivalence leak ⟺ non-monomial holds with **0 mismatches**; 2976 of them are
non-monomial and every one leaks.

What survives as measured content is only (i) the pool's monomial/non-monomial
split, which is *inherited* from R4 and re-verified here, and (ii) the ceiling
difference 136 vs 120.

**Repair.** Register `G-HARDCORE-LEAK-PER-GENERATOR` as `kind="DISCLOSURE"` with
the forcing named (the one-line proof above) and add it to the waiver ledger;
delete "whose split is not forced" from §3 and name instead what the census
does buy — that the pool contains both kinds, and that the ceiling therefore
*separates* two laws; adjust §11's disclosure list; adjust the §4 sentence "and
that too is forced" so that it covers both sectors rather than only the wedge.
The verdict segment needs no numeric change (48 and 0 stand).

### MAJOR-3 — the published symmetric value census is taken on the hard-core block, not on the symmetric sector, and nothing says so.

`raw_defect_census` builds `svals` from `Ds` restricted to `i < npairs` and
`k < npairs` — the 120×120 hard-core block of the 136×136 symmetric sector.
That restricted object is the right one for the *comparison* against the wedge,
and it is also what the receipt publishes as `defect_values/symmetric` and
`symmetric_distinct = 30`.  But §5 ("There are 28 distinct values in the
antisymmetric shape and **30 in the symmetric**") and the verdict segment
`VALUES=…SYMMETRIC-30-DISTINCT-ALL-RATIONAL` present it as the symmetric shape's
value census, and the declared verdict arena A1 is the ceiling-2 arena whose
symmetric sector is 136-dimensional.

Measured: the symmetric sector's two-excitation defect carries **39** distinct
values, all rational.  The nine the block never sees are
±3/8, 5/8, 5/32, 5/128, −3/128, −19/128, −27/128, 101/128 (denominators still
reach 1/128, so that clause survives).  `G-DEFECT-RATIONAL`, whose text reads
"every two-excitation defect value is rational, in both shapes", likewise never
reaches those nine — the claim is true (I checked) but the gate does not bite on
it (#34 reachability).

**Repair.** Separate the two objects: keep the block-restricted multiset for the
like-for-like comparison, and publish `symmetric_distinct_full_sector = 39`
beside it; §5 and the verdict then read "28 in the antisymmetric shape, 39 in
the symmetric sector (30 on the hard-core block the wedge also carries)".
Extend `G-DEFECT-RATIONAL` to the full 136×136 symmetric defect.

### MINOR-1 — the ordered-sector segment is analytically forced and is not disclosed; and its "law" has a one-parameter fibre.

`B(V⊗V) = B(V)⊗B(V)` is an entrywise identity, so with X = B(U₂U₁) and
Y = B(U₂)B(U₁) the ordered-sector defect is X⊗X − Y⊗Y, and
X⊗X − Y⊗Y = (X−Y)⊗X + Y⊗(X−Y) is an algebraic identity holding for *any*
matrices whatever.  Its measured consequence is forced too: for row-stochastic
nonnegative X, Y, summing X_ij X_kl = Y_ij Y_kl over (k,l) gives 16·X = 16·Y, so
X⊗X = Y⊗Y ⟺ X = Y, whence the ordered defect set *must* equal the
single-excitation set and there can be no genuine two-body defect on the
labelled sector.  §5 names the mechanism but §11's disclosure register does not
list it, and the verdict reports it as a measured 3364-of-3364.

Further, the law's terms are not forced: I verified at 3364/3364 that
Δ₂ = Δ⊗Y + X⊗Δ holds equally, and so does the whole affine family
Δ₂ = Δ⊗(tX+(1−t)Y) + (tY+(1−t)X)⊗Δ (measured at t = 2 and t = ½).  "X the
coherent and Y the restarted composite" is one point on a line of exact
readings.

**Repair.** Register `G-DERIVATION-LAW` as a disclosure with the identity named;
state the fibre in §5 ("the splitting is not unique: any convex/affine mixture
of X and Y gives an exact derivation law") or drop the definite article.

### MINOR-2 — A4's "neither sector is invariant" is asserted, never measured.

`raw_distinguishable` measures only `tensor2(U,V) != tensor2(V,U)`, and
`arena_census` sets *both* `antisymmetric_lives` and `symmetric_lives` from that
one predicate; "and where it fails NEITHER sector is invariant" lives in a
`detail` string and in §1's prose.  So one arena's two head-inputs are one
measurement used twice, and the head-law reachability argument leans on it.

I measured it: at all **3306** pairs, ⟨anti|U⊗V|sym⟩ ≢ 0 *and*
⟨sym|U⊗V|anti⟩ ≢ 0 — neither sector is invariant.  The claim is **true**.
**Repair.** Compute the two cross-blocks and gate them
(`G-A4-NEITHER-INVARIANT`, per-pair, #87), then derive A4's two head-inputs from
two measurements rather than from one.

### MINOR-3 — the decisive fixed-point gate compares a constant with itself.

`G-CEILINGS-AGREE-AT-ONE-EXCITATION` evaluates
`one_ceiling1 == one_ceiling2 == NS` where both variables are set to `NS` in the
same function; only the hand-injected `MUT-CEILINGS` can separate them.  The
gate binds a cardinality (16 == 16), not the objects (#87), and no mutant that
actually changed one restriction could die there.  The claim is true and much
stronger than gated (see §2 above).
**Repair.** Build the one-excitation restriction *from each occupancy
declaration* as data — configuration set, per-generator transition matrix, Born
shadow — and gate object-by-object equality across all 64 generators, with the
single-excitation defect census as the two-way witness.

### MINOR-4 — the velocity-failure attribution admits 4096 counterexample cells as stated.

§8: "the failure … occurs exactly when the two single-excitation phase advances
are **equal and nonzero**, so that their sum reaches the antipodal tie".  The
census contains **4096** cells with dd₁ = dd₂ = 4 — equal, nonzero — that do
**not** fail (their sum is 0, and the tie-averaged lift of 0 is 0 = 0+0).
Measured, the failures are exactly the raw pairs **(2,2)** (3584 cells) and
**(6,6)** (3584 cells).  Also unremarked and worth having: the pairs
(2,4), (4,2), (4,6), (6,4) never occur in the census at all, which is *why* the
failing-lift-pair list is clean — the instrument records `(lift(dd₁), lift(dd₂))`,
which maps dd = 0 and dd = 4 both to 0 and would have hidden the distinction.
**Repair.** Replace "equal and nonzero" with "equal to ±π/2 per momentum step
(dd ∈ {2,6})"; publish the raw-advance pair census beside the lift-pair one.

### MINOR-5 — "the speed ceiling does not widen" is forced by the dual torus.

The declared speed is the branch-free circle distance on Z/8, halved; its range
is {0,1,2} for *every* argument, so no family and no excitation number could
widen it at L = 4.  §8's "two excitations move no faster than one" and §10's
bullet are therefore forced, not measured; what is measured is that all three
values are *attained*.
**Repair.** Name the forcing (a disclosure beside `G-SPEED-CEILING-UNCHANGED`)
and restate the content as attainment.

### MINOR-6 — the three-site emptiness has a measured proof and a decorative one.

§7 attributes the emptiness to the alphabet carrying "no element of modulus
1/√3".  The actual proof is the exhaustive sweep (the only unit row with three
nonzero entries has moduli (1/√2, 1/2, 1/2); 1536 such rows; no mutually
orthogonal triple), which I reproduced independently: 1536 rows, 0 completions.
The 1/√3 remark is a heuristic about the equal-amplitude case only.
**Repair.** Keep the sweep as the reason; demote the 1/√3 sentence to an aside
or delete it.

---

## 4. What I did not reach

- The seal/coverage/injection machinery (K3's seat) beyond what a plain mirror
  run and the argv probes exercise.
- R5's 18-row two-excitation table is cited-not-re-run by the pin; I did not
  re-run it either.
- The instrument's third defect route (the interference cross-term sum on the
  144-pair window) I did not rebuild separately; my functoriality check over the
  whole 3364 supersedes the second route's binding, and the ordered-sector
  identity was checked directly against a from-scratch 256×256 tensor Born
  construction on a 200-pair window.
- General n, other lattice sizes, other alphabets: out of the declared scope and
  properly walled by the paper.

## 5. Bottom line

The measurements are sound: 88 independent recomputations, zero false computed
numbers, and the head `R4C-STATISTICS-BOTH-ADMITTED` is unaffected by every
finding above.  The three MAJORs are all readings, not values — one headline
sentence that the multiset criterion cannot support (MAJOR-1), one meta-claim
about forcing that a one-line theorem refutes (MAJOR-2), and one published count
whose scope stamp is missing (MAJOR-3).  All three repair without moving a
number, and MAJOR-1's repair makes the unit's central law *simpler*: the two
exchange shapes are told apart, cell by cell, at exactly the pairs whose two
legs are both non-monomial — the same set the defect census already names.
