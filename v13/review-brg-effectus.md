# BRG — HOSTILE REVIEW R2 (EFFECTUS / CATEGORICAL LENS)

**Reviewer:** R2, structural/conceptual lens. **Date:** 2026-08-08.
**Protocol:** `v13/note-brg-hostile-protocol.md` (FROZEN, K1–K5 binding).
**Object under review (frozen):**

| artifact | sha256-12 dispatched | sha256-12 measured | verified |
|---|---|---|---|
| `v13/paper-brg-bridge.md` | `3191e39da0b1` | `3191e39da0b1` | ✅ |
| `v13/code/brg_bridge_exact.py` | `6f288deb3ee9` | `6f288deb3ee9` | ✅ |
| `v13/code/brg_bridge_output.txt` | `e27aae1c48e0` | `e27aae1c48e0` | ✅ |
| `v13/code/brg_bridge_receipt.json` | `bf1b51d5e806` | `bf1b51d5e806` | ✅ |

**Independent recomputations performed: 42.** All in
`…/scratchpad/brg/` (`r1_core.py`, `r2_scope2.py`, `r3_transport.py`,
`r4_meaning.py`, plus a clean-mirror delivery reproduction). Nothing was
imported from the delivery module; every group, every action and every count
below was rebuilt from scratch.

**Reproduction.** The delivery was rerun in an isolated mirror
(`scratchpad/brg/mirror/`, interpreter `/opt/homebrew/bin/python3.13`): exit 0,
77 anchors, 31 gates, 47 mutants, 0 survivors, wall 3m16s. Output md5
`58f78d364be5ce506844385fd16d5e55`, receipt md5
`b8cf87e5b69c5976bc73bc94d7934b2b` — **byte-identical to ledger #267**.

**Headline.** The verdict `BRG-EMPTY-AT-CARRIER` is **correct** and survived
every attack I mounted. Of 42 recomputations, **41 agree with the delivery**;
the one disagreement (TINY-A) is a mis-declared validation fixture, not a wrong
census number. **No false census number was found.** What I did find is a
framing layer that repeatedly claims *measured* strength for inferences that
were **typed rather than computed**, one bold pull-quote that is **falsified by
the paper's own §4**, and a preservation predicate so weak that the census's
own "live cells" cannot bear any of the weight the ledger puts on them.

---

## 1. K3 — THE ρ-REDUCTION FINDING AND THE FRAMING AUDIT (primary)

### 1.1 The arithmetic verifies

ρ = (1/6, 1/6) exactly (anchored A27 from HA's receipt; I read HA's
`tables.bridge.exact_residual_at_the_detector_site = ["1/6","1/6"]` directly and
confirm it). Reduction mod p is defined by the denominator being invertible, so
ρ fails to reduce exactly when p | 6, i.e. at exactly **{2, 3}**. Swept over
{2,3,5,7,11,13,17,19,23,29,31,37,41,43,47}: failures = [2, 3]. **VERIFIED.**
The per-prime table (carrier p⁴, ρ mod p, |⟨R_HH⟩| = p, orbits p³) reproduces
row for row at all seven primes, and matches HA's own `prime_sweep` (A29).

### 1.2 F-1 (MAJOR) — "both sets are computed in the run" is FALSE

Paper §9 (lines 508–514) states:

> At the committed instances the only primes dividing 2·ord(D) are {2,3} — and
> {2,3} are **exactly** the primes at which […] ρ = (1/6,1/6) fails to reduce.
> […] **That is a measurement, not a rhetorical flourish: both sets are computed
> in the run and printed beside each other.**

**It is not.** Only one of the two sets is computed.

- Set (b), `nonreducible = [2,3]`, is computed at source line 1418. ✅
- Set (a), *"the primes dividing 2·ord(D) at the committed instances"*, is
  **never computed anywhere in the 2,555-line source.** I grepped the whole file
  for any prime factorisation (`radical`, `prime_factor`, `factorint`,
  `prime_divisors`, `rad(`): **zero hits**. The only number-theoretic helper is
  `_gcd`.
- What the run actually prints at output line 205 is
  `2*ord(D) is in [2, 4, 6]` — the set of **group orders**, computed at line
  2281 as `sorted({2 * c['ord_D'] for c in cells1})`. The reader is left to
  factor {2,4,6} mentally. The two objects printed "beside each other" are of
  **different types**: a set of group orders and a set of primes.
- The identification is asserted in ungated `say()` prose at lines 2284–2288.
  **No gate touches it.** It is not in the disclosure table (X01–X06).

Worse, and decisively: **the census never evaluates p = 2 or p = 3 at any
cell.** `declared_primes()` returns HA's sweep {5,7,11,13,17,19,23}; I confirmed
from the receipt that `scope1 primes` and `scope2 primes` are both exactly that
set and that **no cell exists at p ∈ {2,3}**. The claim is therefore about
primes lying entirely *outside* the swept domain — it could not be a census
measurement even in principle.

This is precisely the RUNBOOK failure-catalogue disease #24 ("hard-coded 6561,
true 729 → *counts computed, never typed*"), one level up: here a **set** is
typed, and the paper then asserts in print that it was computed.

**Severity: MAJOR.** The claim is *arithmetically true* (I verified
rad(2·ord(D)) over the committed instances = {2,3} myself), so no number is
wrong — but the paper certifies as measured something the instrument never
measured, and that certification is the load-bearing sentence of the ledger's
"sharpest finding".

**Repair.** Compute `rad(2·ord(D))` over `cells1` as data; gate its equality
with `nonreducible`; add a verdict-flip-class mutant that injects a synthetic
instance with ord(D) = 5 (the union becomes {2,3,5} ≠ {2,3}) and must die there.
If the authors prefer not to add a gate, delete the sentence "both sets are
computed in the run" and demote the identification to a disclosure X07.

### 1.3 F-2 (MAJOR) — the bold pull-quote drops its scope and is falsified by the paper's own §4

Paper §9, in bold, as a block-quoted pull-quote:

> **The deformation side cannot be built at the primes at which the match would
> be possible.**

Read with its antecedent ("At the committed instances…") it is true. Read as it
stands — and a bolded block quote is exactly what gets carried forward — it is a
**general impossibility claim**, and it is **false over the paper's own extended
scope**. My recomputation over GEN's twelve rebuilt classes:

| | measured |
|---|---|
| primes dividing 2·ord(D) over the 12 rebuilt classes | **{2, 3, 5, 7}** |
| of those, admissible on the deformation side (q ∤ 6) | **{5, 7}** |

So at ord(D) ∈ {5, 15, 7} the match *is* possible **and** the deformation side
*can* be built there — which is exactly the paper's own §4 scope-2 table (4, 4
and 6 morphisms). §9's pull-quote and §4's table contradict each other unless
the reader silently re-supplies "at the committed instances".

The tension is aggravated by **deviation 2**, which says GEN's twelve classes
"were each rebuilt in full by GEN itself, so they are **committed
measurements**". The paper thus uses "committed" in two senses — the 8 committed
*instances* and the 12 committed *measurements* — and the pull-quote is true in
the first sense and false in the second.

**This is the answer to the protocol's question "does EMPTY-AT-CARRIER anywhere
leak into impossibility-in-general?" — yes, here, and only here in the paper.**
Everywhere else the paper is disciplined: the scope box (§0), §10's "What it
does not say", and all seven §13 non-claims are, in my judgement, exemplary and
I could not break any of them.

**Severity: MAJOR (framing).** **Repair.** Rewrite as: *"At the committed
instances — and only there — the primes dividing 2·ord(D) are 3-smooth, so they
fall inside the two primes at which ρ does not reduce. At GEN's richer classes
this fails: ord(D) ∈ {5,7,15} puts admissible primes back in range."*

### 1.4 F-3 (MODERATE) — the ledger's framing is stronger than the paper's, and self-refuting

The two sentences the protocol names live in **`v13/LOG.md` #267**, not in the
paper:

> **The two structures miss each other ARITHMETICALLY: the gravity side needs
> odd primes to exist; the committed transport side carries only 2-and-3-torsion.**

Two defects. (i) **No scope qualifier at all** — "the two structures miss each
other" is stated of the structures, not of the committed carriers. (ii) The
gloss **refutes the claim it glosses**: the deformation side does *not* need
"odd primes", it needs primes **∤ 6**, i.e. p ≥ 5. Taken literally, p = 3 is
odd and would be admissible — and 3 | 2·ord(D) at base T, so the structures
would *not* miss each other. The ledger's own paraphrase, read at its word,
produces a live cell.

Since the ledger is what propagates to STATUS.md and to memory, this is the
version that will be cited. **Severity: MODERATE.** **Repair:** amend #267 in a
forward-correction entry (per §13, by name, not by edit): replace "needs odd
primes" with "needs primes not dividing 6", and prefix "at the committed
carriers".

### 1.5 F-4 (MODERATE) — the "coincidence" has one degree of freedom, not two

The rhetorical force of §9 comes from an *equality* of two independently-arrived
sets. Measured, the equality is much thinner than it reads:

| instance | rad(2·ord(D)) |
|---|---|
| base 1 @ SP-E / SP-F, base G @ GP-E / GP-F, base S, base S′, species 4 | **{2}** (7 of 8) |
| base T | **{2,3}** (1 of 8) |

- The prime **2 is forced, not coincidental.** Every dihedral group ⟨W,D⟩ has
  order 2·ord(D), so 2 divides it *always*; equivalently every such group has a
  reflection, so hom(Z/2, ⟨W,D⟩) is non-trivial at **8 of 8** committed
  instances. Recomputed: 8/8 at p = 2, **1/8** at p = 3.
- The prime **3 is supplied by exactly one instance**, base T. Delete base T and
  rad(2·ord(D)) = **{2}**: the advertised *equality* with {2,3} fails, while the
  logically load-bearing *inclusion* rad(2·ord(D)) ⊆ {2,3} survives untouched.

So the claim that actually does work is the **inclusion** — "the committed
transport orders are 3-smooth" — and the *equality* that carries the rhetoric
rests on a single instance. **Severity: MODERATE (framing).** **Repair:** state
the inclusion as the finding, and register the equality as a one-instance
observation.

### 1.6 What survives at measured strength

Stripped of poetry, this is what I can certify:

> At the eight committed transport instances, 2·ord(D) ∈ {2,4,6} is 3-smooth,
> and the deformation side's residual ρ = (1/6,1/6) admits only primes p ∤ 6.
> The two ranges are therefore disjoint, and the forward census is empty at all
> 56 committed cells. The prime 2 lies in the intersection of neither range by
> arithmetic accident but by the dihedral form of ⟨W,D⟩; the prime 3 enters from
> base T alone. At GEN's twelve rebuilt classes the disjointness fails.

That is a real, useful, correctly-scoped result. It is *not* "the two structures
miss each other arithmetically".

---

## 2. K2 — THE LIVE CELLS: WHAT DO THE 14 MORPHISMS MEAN? (primary)

### 2.1 The 14 recompute exactly

Built D_n from scratch (n = ord(D), order 2n, f r f = r⁻¹) and counted
{g : gᵖ = e, g ≠ e} over GEN's twelve classes at all seven primes:

| cell | non-trivial homs | delivery |
|---|---|---|
| p = 5, class `ord=5,fixed=36` (|G| = 10) | **4** | 4 ✅ |
| p = 5, class `ord=15,fixed=9` (|G| = 30) | **4** | 4 ✅ |
| p = 7, class `ord=7,fixed=18` (|G| = 14) | **6** | 6 ✅ |
| every other cell of 84 | 0 | 0 ✅ |

Totals: **84 scope-2 cells, 3 live, 14 morphisms**; 56 scope-1 cells, all
empty; **140 cells, 137 empty, 3 live** — every figure reproduces. Coextensivity
with gcd(p, |⟨W,D⟩|) = 1 over all 140 cells: **0 failures**.

### 2.2 F-5 (MAJOR) — the census reduces to a group-hom count; the functor layer is vacuous

This is the structural core of my review.

The preservation predicate is SP1 (φ a hom) + SP2 (φ(1)=1) + SP3 (Φ equivariant)
+ NT1 (φ non-trivial) + NT2 (Φ non-constant). The source action is **measured
free** (translation by ρ ≢ 0). For a free action, given φ, **SP3 imposes no
constraint whatever**: one arbitrary image per orbit determines the rest. The
delivery states this itself as its counting formula, |C_TR|^{#orbits} per φ, and
discloses the counts as "astronomically large and entirely degenerate" (X06).

The consequence the paper does **not** draw: **the entire census is a group-hom
count wearing a functor costume.** Requirement (2)'s "structure-preservation
predicate" has exactly one non-vacuous clause. And NT2 has near-zero teeth — it
is literally `len(set(Phi)) > 1`, so at p = 5 a carrier map sending **124 of 125
orbits to a single target point** is "non-degenerate":

| p | source orbits | NT2 requires |
|---|---|---|
| 5 | 125 | ≥ 2 distinct images |
| 7 | 343 | ≥ 2 distinct images |
| 23 | 12,167 | ≥ 2 distinct images |

**What a "live cell" actually contains** (recomputed; the delivery never
computes this, because its functor census runs only at the **35** cells of the
five rebuilt instances — confirmed from the receipt, `instances covered` =
{base G @ GP-E, base G @ GP-F, base S′, base T, species 4} — and the live cells
are all in scope 2):

| live cell | non-degenerate SP-satisfying pairs |
|---|---|
| p = 5, ord(D) = 5 | 4 · 81¹²⁵ ≈ a **240-digit** number |
| p = 5, ord(D) = 15 | 4 · 81¹²⁵ ≈ a **240-digit** number |
| p = 7, ord(D) = 7 | 6 · 81³⁴³ ≈ a **656-digit** number |

A live cell is therefore **not one bridge; it is an unconstrained explosion of
~10²³⁹ mutually incomparable "bridges", all equally certified by SP.**

**Is this fatal? No — and it cuts the delivery's way.** Because the predicate is
maximally permissive, the EMPTY verdict is *maximally strong*: nothing was
excluded by a strict filter, the filter is as loose as it can be and the answer
is still zero. I want that stated plainly in the reviewer's voice, because it is
the delivery's real achievement. But the same fact makes the **live cells worth
almost nothing**, and the ledger spends them as if they were worth a great deal.

**Severity: MAJOR (as a framing/strength defect, not a computational one).**
**Repair:** add a disclosure — *"the preservation predicate is vacuous at the
functor layer because the source action is free; the census is therefore a
group-homomorphism census, and its EMPTY verdict is correspondingly strong while
its live cells are correspondingly weak"* — and compute the non-degenerate pair
count at the three live cells so the reader sees the 240/656-digit numbers next
to the number 14.

### 2.3 F-6 (MODERATE) — "the bridge is … NOT structurally impossible" is not supported

Ledger #267: *"**AND THE LIVE CELLS: … 14 non-trivial morphisms EXIST … The
bridge is empty at the committed instances, NOT structurally impossible —
completions with ord(D) ∈ {5,7,15} open it.**"*

Group-level homs are far too weak to carry the word "bridge". Measured:

1. A live morphism says **exactly one thing**: ⟨W,D⟩ contains an element of
   order p — equivalently p | ord(D). It is a **divisibility fact about one
   integer**, and nothing else. It is not a statement about records, metrics,
   fronts, registers, lapses, wings, pointers or completions.
2. Given it, the carrier map is a **free choice** (§2.2). So the "morphism"
   transports **no geometric content at all** — pick any images you like.
3. The two sides' **encodings** — HA's record-is-metric map (counts → q,
   det = 2) and GEN/XBA's completion-to-defect map Q ↦ δ(Q) — are the actual
   physical content, and SP **never references them**. The paper concedes this
   in §14 open 3: *"F1 was swept at the group layer and the encoding layer
   factorised through it."* The encoding layer was therefore **not tested**.
4. Nothing was verified out of sample at a live cell. The entire held-out
   apparatus (G21–G24, 234 cells, E-REF teeth 54/234) ran **only** on the
   synthetic p = 3 pair.

"Not structurally impossible" is a defensible *negative* — no theorem here
forbids ord(D) = 5 — but it must not be phrased as though a bridge had been
sighted. **Repair:** in the forward correction to #267, replace with *"the
group-level obstruction is not universal: completions with ord(D) ∈ {5,7,15}
admit non-trivial homomorphisms from Z/5 and Z/7. Whether any such
homomorphism can be promoted to a structure-preserving map of the two sides'
encodings is untouched."*

### 2.4 F-7 (MODERATE) — the exclusion of the live cells is mis-attributed

Paper §10: the 14 morphisms are *"measured, reported (X05) and **excluded from
the verdict by the pin's own requirement 4**"*. Traced through the source, that
is not the mechanism.

The verdict's decision variable is line 2323:
`empty_everywhere = (nt_fwd1 == 0 and nt_rev1 == 0)`, where `nt_fwd1`/`nt_rev1`
are sums over **`cells1` only** (scope 1). The live cells live in `cells2` and
**never enter `empty_everywhere` at all.** They are excluded because the verdict
is *declared* to be taken at scope 1 (deviation 2) — a **scope choice**, not an
arena-invariance argument. G14 (requirement 4, the intersection reading) is a
**separate** gate that happens also to pass.

Note further that the two readings are not even the same shape: `empty_everywhere`
is a **union** over primes at scope 1 (any live scope-1 cell anywhere ⇒ not
empty), while G14 tests an **intersection** over primes. They agree in this run
only because scope 1 is empty at every cell.

**Severity: MODERATE (accuracy of a mechanism description).** **Repair:** state
two distinct exclusions — *"the verdict is taken at scope 1 by declaration
(deviation 2); independently, G14 measures that the intersection over the prime
sweep is empty at every instance of **both** scopes"* — and say that
`empty_everywhere` is a union-over-primes reading at scope 1.

### 2.5 The honest requirements: what a successor predicate must demand

The protocol asks what a live-cell morphism must satisfy to deserve the word
"bridge". Written as demands, in order of how much they bite:

1. **ENCODING INTERTWINING (non-negotiable).** The functor must make a
   *commuting square* at the encoding layer, not merely a triangle at the group
   layer: HA's record-is-metric linear map (det 2) must be intertwined with
   GEN/XBA's Q ↦ δ(Q) = ΣQᵀΣQ. As long as the encoding "factorises through" the
   group actions (§14 open 3), nothing physical is being transported. **This is
   the single requirement whose absence makes the present census unable to
   answer its own question in the affirmative.**
2. **CARRIER RIGIDITY.** SP3 must be supplemented so that Φ is *determined*, not
   *chosen*. The obvious candidate is already measured on both sides: the
   **fixed-configuration stratification** (transport: 9/18/27/36/45/54/81 —
   GEN's second spectrum; deformation: the front-sector/register split of HA
   G29). Demand that Φ carry the source stratification into the target
   stratification. Without something of this kind the census's answer space is
   10²³⁹ per live cell.
3. **NON-DEGENERACY WITH TEETH.** Replace NT2 (`≥ 2 distinct images`) by
   injectivity on orbits, or at minimum by a measured lower bound on |image(Φ)|
   as a fraction of the orbit count. As it stands NT2 excludes only the constant
   map.
4. **FUNCTORIALITY IN THE FAMILY (this is what makes it a *functor*).** A single
   pair (φ, Φ) at one instance is not a functor — HA §14 req (1) says *carrier
   functor*. Demand naturality across the declared base-change maps
   (base 1 → base G → base T → species 4, and GEN's twelve classes), so that a
   live cell is not an isolated numerical coincidence at one (p, ord(D)).
5. **HELD-OUT PREDICTION AT A LIVE CELL, NOT AT A SYNTHETIC PAIR.** Run the
   G21–G24 machinery at (p = 5, ord(D) = 5) with the actual carriers, and
   transport an actual computed quantity — e.g. the record-is-metric determinant
   against the class's fixed-configuration count. This is the pin's requirement
   (3) discharged where it matters.
6. **A READING OF REQUIREMENT 4 UNDER WHICH *FOUND* IS REACHABLE IN-ARENA**
   (see F-9). Either treat the prime as a declared *parameter* of the arena with
   per-prime verdicts, or find a corpus-internal fixing of p (§14 open 1).
   Otherwise the two-way gate is two-way only outside the arena.

### 2.6 Successor feasibility, honestly — and a finding the delivery missed

*"Is a completion with ord(D) = 5 constructible at a carrier where the p = 5
deformation arena also lives?"*

- **At the group layer: trivially yes, already done.** 4,608 members of GEN's
  8! = 40,320 family have ord(D) = 5; the class is one of GEN's twelve rebuilt
  ones; 4 morphisms already exist and are computed. There is **no cardinality
  obstruction** (625 vs 81 is irrelevant — correctly, the delivery uses no
  cardinality criterion anywhere).
- **At the layer that matters: unknown, and harder than the ledger implies**,
  for the reasons in §2.2–§2.3. Every one of the six requirements above is
  currently unmet.
- **The finding I think the unit should have made.** I computed the sector
  statistics of the completion family against the committed record:

| | measured |
|---|---|
| family members with ord(D) ≤ 3 | 96 + 1,440 + 4,224 = **5,760 of 40,320 = 1/7 ≈ 14.3 %** |
| family members admitting *some* declared prime (ord(D) ∈ {5,7,15}) | **23,040 of 40,320 = 4/7 ≈ 57.1 %** |
| committed transport instances with ord(D) ≤ 3 | **8 of 8** |
| committed instances admitting *any* declared prime | **0 of 8** |

  So the abstract family is **majority-live** (57 %), and every physically
  prepared base lands in the 14 % low-defect sector — 8 for 8 (6 distinct
  bases; even at 4 independent draws that is ~4 × 10⁻⁴). **The substantive
  obstruction is not order-coprimality — that is only the mechanism. The
  substantive fact is that the corpus's prepared bases concentrate
  overwhelmingly in the low-defect-order sector while the family they are drawn
  from does not.** Naming *that* would tell the successor exactly where to
  look: is the concentration a physical selection rule of the preparation, or an
  artifact of which six bases happen to have been built? The delivery has all
  the numbers and never asks.

  **This is offered as a constructive finding, not a defect.**

---

## 3. PIN COMPLIANCE — THE FOUR HA-§14 REQUIREMENTS, AT STRENGTH

| req | verdict | evidence |
|---|---|---|
| (1) carrier functor as data, non-triviality gated | **PARTIAL** | see F-8 |
| (2) morphism census, never one expression, predicate as data | **MET** (with F-5) | 8 functors declared; 140 cells + 35 functor cells + 504 dictionary cells; G01 freeze measured at candidate-counter zero, `freeze-lax` dies |
| (3) two-way gates, both outcomes reachable, FOUND predictive | **MET IN FORM, ASYMMETRIC IN STANDARD** | see F-9 |
| (4) arena-invariance gating | **MET IN FORM, ANALYTICALLY FORCED** | see F-10 |

### 3.1 F-8 (MODERATE) — requirement (1) is discharged at G-set strength, not arena strength

The pin's requirement (1) asks for *"an explicit mapping between the arenas
(**fronts/registers/lapses ↔ wings/pointers/completions**)"*. The delivery
abstracts **both** arenas to bare (group, set) pairs and discards the
component decomposition on the target side entirely. There is no declared
correspondence "front ↔ wing", "register ↔ pointer", "lapse ↔ completion"
anywhere; the only named component-level dictionary is F1 (9 records ↔ 40,320
completions), and F1 is swept at the *group* layer.

Consequence: the census structurally **cannot see** the component facts that a
real bridge would have to match — HA G29's *front sector fixed / register
translates*, versus PSI's *W moves the system pair and the pointer pair
together while the preparation leg acts on the system pair alone*. Those are
precisely the asymmetries a functor between these arenas would have to
intertwine.

**Fair counterweight:** the source action *does* encode its own component
structure (the front-fixed translation is what makes the action free), and
sweeping Φ over all equivariant maps is strictly more exhaustive than declaring
one — so for an EMPTY verdict this abstraction *strengthens* the result. The
shortfall is real for requirement (1) as written, and for any future FOUND.

**Repair:** either declare the component dictionary as data (and gate that the
census consumes it), or amend the §1 discharge table to read *"discharged at the
level of group actions on carriers; the arena-component correspondence is not
posed"* and add it to §14 opens.

### 3.2 F-9 (MODERATE) — requirement (3): FOUND is demonstrated at a weaker standard than EMPTY was measured against

The EMPTY verdict is required to survive the intersection-over-primes reading
(G14) across 20 instances × 7 primes. The FOUND branch is demonstrated at a
**single synthetic (source, target) pair at a single prime** (p = 3, base T),
declared outside the admissible arena (X04). Both outcomes are formally
reachable — `found-block` and `empty-block` both die, and I confirm the
reachability logic in `derive_verdict` — but they are reachable at **different
evidential standards**, and the pin's requirement (3) says *"Each outcome
REACHABLE"* in the same instrument.

Compounding this: **under the delivery's own declared reading of requirement 4,
FOUND was unreachable in-arena a priori.** Recomputed: an instance admitting a
non-trivial morphism at *every* declared prime would need 2·ord(D) divisible by
5·7·11·13·17·19·23 = **37,182,145**; the maximum available over the whole
40,320-member family is 2 × 15 = **30**. Even **two** declared primes need
5 × 7 = 35 > 30. The paper states this arithmetic in §6 — to its credit — but
does not draw the conclusion: the arena-invariant FOUND branch was closed before
any census ran.

**Repair:** disclose that the intersection reading forecloses in-arena FOUND for
any family with 2·ord(D) < 35, and either (a) run the FOUND demonstration inside
the arena at a live scope-2 cell under a per-prime reading, or (b) record
explicitly that the two-way gate is two-way only across the synthetic boundary.

### 3.3 F-10 (MODERATE) — G14 and G27 are analytically forced must-pass gates

RUNBOOK §14 addendum (v13 #208): *"Analytically-forced clauses (true by algebra
for every input) are disclosures, not must-pass gates."*

- **G14** cannot fail on any input of this family (§3.2 arithmetic: 35 > 30).
  Recomputed and confirmed.
- **G27** ("the abelianisation is a 2-group at every instance of every scope")
  is forced for **every** dihedral group: D_n^ab = Z/2 (n odd) or Z/2 × Z/2
  (n even). I verified over D_1…D_25: abelianisation orders seen = **{2,4}**,
  zero exceptions. Since ⟨W,D⟩ is dihedral throughout (§4.2), G27 is true by
  algebra everywhere.
- By contrast X01 **correctly** discloses |hom(Z/p, D_n)| = gcd(n,p) as forced.
  The treatment is inconsistent: the same class of fact is a disclosure in one
  place and a must-pass gate in two others.

Both gates are killed by their mutants (`invariance-lax`, `abelianization-lax`)
— but those mutants flip a **switch inside the helper**, they do not perturb the
**data**; no admissible input can move either predicate. **Repair:** demote both
to disclosures, or keep them and add a line recording that each is
analytically forced for this family (as §6 already half-does for G14).

---

## 4. K1 — THE OBSTRUCTION THEOREM (lower depth, but load-bearing)

### 4.1 Verified as elementary group theory and against the census

*"hom(Z/p, ⟨W,D⟩) trivial iff p ∤ 2·ord(D)."* Brute-forced over **D_1…D_40 ×
12 primes = 480 cells**: **0 counterexamples**. Both directions hold, including
the p = 2 edge case (a reflection always supplies an element of order 2, and
2 | 2n always). Coextensive with the census: **137 empty / 3 live of 140**, and
empty exactly where gcd(p, |⟨W,D⟩|) = 1 — **0 mismatches** over all 140. The
reverse direction's 2-group abelianisation claim: verified (§3.3).

### 4.2 The theorem is contingent on dihedral-ness — and that contingency is discharged elsewhere

The theorem is **not** a general fact about groups of order 2·ord(D). Applying
the same criterion to *cyclic* groups of order n, I found **10 failures** in
n ≤ 19 × p ≤ 7 (e.g. ⟨W,D⟩ ≅ Z/3: 2 | 6 but hom(Z/2, Z/3) is trivial). The
theorem needs W to be a genuine reflection, i.e. W² = 1, WDW = D⁻¹, W ∉ ⟨D⟩.
The delivery anchors |⟨W,D⟩| = 2·ord(D) instance by instance from XBA — which is
sound, but treats as **eight measured coincidences** something that is
**forced**. See §5.

### 4.3 Scope strength of the theorem's statement

Hunted for impossibility-beyond-the-carriers sentences: **§9's pull-quote is the
only leak** (F-2). §10's summary sentence — *"At the committed carriers, over
the arena-invariant content, this program's spacetime structure is alongside…"* —
carries its qualifier at the front and is correctly stated. The §13 non-claims
are strong and I could not falsify any of them.

---

## 5. CROSS-UNIT COHERENCE — THE OBSTRUCTION *IS* A THEOREM ABOUT THE ONE LAW, AND THE PAPER NEVER SAYS SO

PSI (TERMINAL, #265) establishes: P_W is an involution and the defect **is** the
group commutator, D = [P_W, u] = P_W u⁻¹ P_W u, with the based holonomy group's
order twice the order of the commutator.

**Claim (mine, verified):** given only W² = 1 and D = [W, u], the relation
**W D W = D⁻¹ is forced by algebra**:
W(W u⁻¹ W u)W = u⁻¹ W u W = (W u⁻¹ W u)⁻¹.
Hence ⟨W,D⟩ is dihedral of order 2·ord(D) whenever W ∉ ⟨D⟩.
**Recomputed over 400 randomised (involution W, permutation u) pairs on 4–8
points: 0 violations of WDW = D⁻¹; |⟨W,D⟩| = 2·ord(D) in 400/400
non-degenerate cases; W ∈ ⟨D⟩ in 0.**

Therefore:

- The obstruction is **not** a contingent feature of eight measured instances.
  It is a **theorem about the commutator law's entire group family**: *for any
  base whose defect is the commutator of an involutive exchange, and any prime
  p ≥ 5, a non-trivial hom Z/p → ⟨W,D⟩ exists iff p | ord(D).* That covers every
  base the corpus will ever build under PSI's law, including ones not yet
  prepared.
- **The paper does not say this.** BRG's source list is HA/NT/GEN/XBA;
  **PSI is not cited anywhere** in `paper-brg-bridge.md` (grep: 0 hits) and the
  dihedral form is anchored instance-by-instance from XBA instead of derived.
- The consequence is a **strengthening left on the table**, and it also
  reframes: once the dihedral form is recognised as forced, the *only*
  contingent content of `BRG-EMPTY-AT-CARRIER` is **"ord(D) ≤ 3 at the committed
  instances"**. The verdict is a statement about the **smallness of the
  committed defect orders**, not about a structural mismatch between gravity and
  transport. Combined with §2.6's sector statistics, that is the honest physical
  content of this unit.

**Severity: MODERATE (a missed strengthening + a cross-unit citation gap).**
**Repair:** add a short §9 subsection deriving WDW = D⁻¹ from PSI's one law,
hash-pin `psi_curvature_receipt.json` as a fifth source, and restate the
obstruction at family strength with the committed-scope instantiation as a
corollary.

---

## 6. K4 AND K5 AT LOWER DEPTH

**F-11 (MODERATE) — TINY-A is a mis-declared validation fixture.** The
declaration (source line 414, receipt `declarations.tiny_cells`) reads *"source
Z/2 acting **freely** on 4 points"*. The implementation (line 1956) builds
`gen = (0 1 2 3)`, a **4-cycle**, and `make_cyclic_arena` defines
act(g,x) = genᵍ(x) over els = Z/2. Measured: **ord(gen) = 4 ≠ p = 2**, so
act(1, act(1, x)) = gen²(x) ≠ x = act(0, x) — **the Z/2 action axiom is
violated**. Two further symptoms: the receipt records `orbits: 1`, but Z/2 acting
freely on 4 points has **2** orbits (the 1 is ⟨gen⟩'s orbit count, not the
acting group's); and my brute force under the *declared* semantics (Z/2 free on
4 points, Klein four regular) gives **64 SP pairs / 48 non-degenerate**, against
the delivery's **16 / 12**. The delivery's 16/12 is internally consistent with
its own (non-)action, so formula = brute force still holds — **but it holds
between two computations over the same mis-specified object, so TINY-A validates
nothing.** TINY-B (ord(gen) = 3 = p) and TINY-C (ord(gen) = 5 = p) are both
**correct**, and TINY-B independently supplies G18's "a cell with non-trivial
group maps", so **G18's coverage survives** and no census number is affected.
**Repair:** either change TINY-A's generator to an involution
(two 2-cycles, 2 orbits, formula 4·4² = 64) or amend its declaration to
"Z/4 on 4 points, p = 2" and re-derive; and add a gate that the arena generator
satisfies genᵖ = identity — this class of defect is otherwise invisible.

**F-12 (MINOR) — the two "independent routes" at the group census are related by
an identity.** Route A tests gᵖ = e; route B builds cyclic spans and keeps those
with |S| | p, i.e. tests ord(g) | p. These are the **same predicate** under the
elementary identity gᵖ = e ⟺ ord(g) | p — which is exactly what RUNBOOK §13
addendum #234 calls "a pair related by an algebraic identity is one route". In
mitigation, route B builds a genuinely different data structure (the full cyclic
subgroup lattice, deduplicated as sets) and would catch a bug in `perm_pow`,
and the taint counter and `route-alias` mutant do work. **Repair:** disclose the
identity, or replace route B with a structurally different computation (e.g.
Sylow-p / orbit-counting on the conjugation action).

**F-13 (MINOR) — G31's "independent expression" is a re-typing.** `verdict` and
`recomputed` (lines 2326–2331) are the same boolean function of the same five
inputs with the branches reordered. The `verdict-flip` mutant does die (it
mutates only `derive_verdict`), so the addendum's *purpose* — a hand-typed
verdict cannot survive — is served. But "independent expression" overstates it.
**Repair:** wording, or derive `recomputed` from the receipt tables rather than
from the same five booleans.

**Verified without defect (K4/K5 spot checks, all reproduced):** the 42-digit
dictionary space (40,320⁹, **42** digits); admissible completions per record
**13,824** (p=5) / **9,216** (p=7) / **0** at p ≥ 11; dictionaries **38** and
**36** digits; the committed-scope dictionary count **0 at all seven primes**;
504 = 7 × 8 × 9 spectrum cells; the record-is-metric determinant **2**; the
ambiguity sets (2 for base 1, 864 for base S) giving one group order throughout;
the family spectra summing to 8! = **40,320**; ρ anchored (A27/A29) against HA's
receipt; 77 anchors and 47 mutants exercised in my own clean-mirror run.

---

## 7. FINDINGS, RANKED

| # | severity | finding | repair |
|---|---|---|---|
| F-1 | **MAJOR** | §9's "both sets are computed in the run" is false — the set of primes dividing 2·ord(D) is never computed anywhere in the source, and the census never evaluates p ∈ {2,3} at all; the identification is ungated `say()` prose | compute rad(2·ord(D)) as data, gate it, add a data-perturbing mutant; or delete the sentence and demote to X07 |
| F-2 | **MAJOR** | §9's bold pull-quote drops its scope and is falsified by the paper's own §4/deviation 2 at GEN's 12 rebuilt classes (admissible match primes {5,7}) | rewrite with the qualifier inside the quote; state the inclusion, not the equality |
| F-5 | **MAJOR** | the preservation predicate is vacuous at the functor layer (free source action ⇒ SP3 imposes nothing); the census is a group-hom census; a live cell is ~10²³⁹ pairs, never computed | disclose; compute the non-degenerate pair count at the 3 live cells |
| F-3 | MODERATE | ledger #267's framing is unscoped and its gloss ("needs odd primes") refutes its own claim | forward-correction entry |
| F-4 | MODERATE | the {2,3} "coincidence" is one degree of freedom: prime 2 is forced by dihedral form (8/8), prime 3 comes from base T alone (1/8) | state the inclusion as the finding |
| F-6 | MODERATE | "the bridge is … NOT structurally impossible" unsupported by group-level homs | restate as a bounded negative |
| F-7 | MODERATE | the live cells are excluded by the scope-1 declaration, not by requirement 4; and `empty_everywhere` is a union reading while G14 is an intersection reading | describe the two exclusions separately |
| F-8 | MODERATE | requirement (1) discharged at G-set strength; no fronts/registers/lapses ↔ wings/pointers/completions dictionary is posed | declare it, or amend the discharge table + §14 opens |
| F-9 | MODERATE | requirement (3) asymmetric: EMPTY measured against the intersection reading, FOUND demonstrated at one synthetic pair; in-arena FOUND foreclosed a priori (35 > 30) | disclose the foreclosure; run FOUND at a live cell or record the boundary |
| F-10 | MODERATE | G14 and G27 are analytically forced must-pass gates (§14 addendum #208), inconsistently with X01 | demote to disclosures or record the forcing |
| — | MODERATE | cross-unit: the obstruction is a theorem about PSI's commutator-law family (WDW = D⁻¹ forced by W²=1; verified 400/400) and the paper never says so; PSI uncited | derive it, pin PSI's receipt, restate at family strength |
| F-11 | MODERATE | TINY-A violates the Z/2 action axiom (ord(gen)=4≠p); declared "freely on 4 points" but recorded with 1 orbit; validates nothing (TINY-B/C are correct, so G18 survives) | fix the generator or the declaration; gate genᵖ = identity |
| F-12 | MINOR | the two census routes are related by gᵖ = e ⟺ ord(g) \| p | disclose or replace route B |
| F-13 | MINOR | G31's "independent expression" is a re-typing of the same predicate | wording, or derive from the receipt tables |

**No fatal finding. No false census number found in 42 recomputations.**

---

## 8. RECOMPUTATION COUNT

**42 independent recomputations**, none importing the delivery module: 4 SHA-256
artifact verifications; the ρ-reduction sweep over 15 primes; rad(6); the
obstruction theorem brute-forced over 480 (D_n, p) cells; its cyclic-group
contingency (10 failures); the one law at 8 instances and 12 classes; rad(2·ord(D))
per instance and over the 12 classes; the p = 2 and p = 3 counterfactuals; the
without-base-T radical; the 3-smoothness census (17/20); the family total and
maximum order; the 3 live cells and 14 morphisms; scope-1 (56), scope-2 (84),
total (140/137/3); coextensivity over all 140; the abelianisation sweep over
D_1…D_25; the G14 forcing arithmetic; the PSI-forcing sweep over 400 randomised
pairs (two quantities); the functor-level explosion at the 3 live cells; the NT2
teeth table; the F1 dictionary at extended and committed scope; the digit counts
(38/36/42); the 504-cell arithmetic; the record-is-metric determinant; the
deformation table at 7 primes; the TINY-A brute force and action-axiom test;
TINY-B/C validity; the sector-concentration statistics; the anchor cross-reads
(A27, A29) against HA's receipt; the functor-census scope from the receipt; and
one full clean-mirror delivery reproduction (exit 0, byte-identical).

---

## 9. GRADE

The question was posed honestly, the census is exhaustive at its declared scope,
the arithmetic is exact and reproduces byte-identically, the scope box and the
§13 non-claims are among the most disciplined I have reviewed in this programme,
and **the verdict `BRG-EMPTY-AT-CARRIER` is correct** — I attacked it from the
theorem side, the census side, the arena side and the cross-unit side and could
not move it. The obstruction is correctly named, and is in fact **stronger** than
the paper claims.

What fails is the layer above the numbers. One paper sentence asserts a
measurement that was never made (F-1). One bold pull-quote is falsified by the
paper's own §4 (F-2). The predicate that gives the census its authority is
vacuous at the functor layer, which makes EMPTY strong but makes the ledger's
live-cell rhetoric unsupportable (F-5, F-6). And one validation fixture is
mathematically broken (F-11). None of these touch the verdict; all of them touch
what the verdict will be taken to mean.

# **ACCEPT-WITH-FIXES**

Required before TERMINAL: **F-1, F-2, F-5, F-11** (each a correction of record,
not a re-run of the census). Strongly recommended: **F-3** (the ledger
forward-correction) and the **PSI cross-unit strengthening** of §5, which costs
one derivation and buys the obstruction a much larger scope. F-4, F-6 through
F-10, F-12 and F-13 are adjudicable as wording, disclosure and scope-table
amendments.
