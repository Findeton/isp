# v11 L0 — THE SCALE NO-GO, RESTATED AS A KINEMATIC LEMMA

**Status:** LEMMA, STRICT, 2026-07-27.  Unit L0 of Phase I
(`note-L1-L0-boundary-lemmas-pin.md`; paper 0 §7, §9b).  This is a
**restatement lemma**, and its import is marked throughout:
**[IMPORTED-NO-GO]**.  The source is a corpus theorem at its own
scope; v11 imports its conclusion as a design constraint and does
**not** re-prove it on v11's carrier.  Receipt:
`code/L1_L0_text_anchors.py` → `code/L1_L0_anchors_output.txt`.

---

## 1. The source, verbatim

Source file:
`/Users/felixrobles/workspace/isp/v6/relativistic-isp-v6-paper57-gravity-from-sealed-records.md`,
§2 *The unified no-go on Newton's constant `G`* (lines 31–51).

**§2.1, the result (line 33), verbatim:**

> SHARD does not, and provably cannot, fix the absolute scale `σ_A` — which has length-weight −2 and is in bijection with Newton's `G` (weight +2) via `G·σ_A = 1/4`, so fixing one fixes the other (they are linked, never equal). This is not an absence of success but a single structural theorem.

**The two invariants (line 35), verbatim — this is the displayed
form, and it is the form v11 uses:**

> **`κ·σ_A = 2π`  and (separately)  `G·Λ² = const`**  (two weight-zero invariants — *each* a fixed pure number, not numerically equal to one another; what they share is the structure, not a value; paper6 Corollary 2; the structural lemma *invariant ⟺ weight-zero*, not the implementation-audit monomial count; here `Λ` is the inverse-length UV/spectral cutoff, distinct from the unimodular cosmological constant `Λ₀` of §1.5)

**§2.2, the mechanism — the weight-counting lemma (line 39),
verbatim:**

> *every dimensionful record quantity is `(pure number) × l^{±k}` (one record length), and every intrinsic record functional factors through the record sector, hence is `g_λ`-invariant (paper6 Theorem G), hence weight-zero; so no intrinsic quantity can have the weight −2 that `σ_A` needs.*

**The unification (line 51), verbatim:**

> *deriving `1/G` always trades it for a labeling-equivalent cutoff; the missing datum is exactly one absolute length unit, which no weight-zero record functional can be.*

**The single load-bearing premise (line 37), verbatim:**

> **gate G1** — *no sealed law consumes the record area `A_rec` (a weight-`±k` dimensionful datum) except through the continuum labeling map `ℓ`.*

with the scope sentence, verbatim:

> the no-go is airtight *iff* G1 holds

and the uniqueness statement the seal-rate attack establishes,
verbatim:

> the seal-spacing length `l_step` is provably the unique dimensionful primitive and the sole gauge direction.

The catalog carries the graded entry at
`note-v11p0a-reproduction-catalog.md` §2.2 (lines 721–800):
**[THEOREM], and structurally UNCONDITIONAL**, presupposing *"the
sealed-record weight calculus (Theorem G / Corollary 2 of v6 paper 6)
and **gate G1**"* and **explicitly not** presupposing axiom (R), the
focusing gate, or `θ = σ = 0`.  The catalog co-tags the same entry
**[LATER-CORRECTED]** in one respect — the compressed equality chain,
§2 below — and L0 carries both tags together, never the grade alone.

---

## 2. The compressed form is an ERRATUM and is not used

The pin and several corpus summaries compress the result to
`κ·σ_A = G·Λ² = const`.  **That compression is a filed error and is
not quoted in this lemma.**  `v8/LEDGER.md` correction **#13**
(line 47), verbatim:

> per v7 paper 16 §5 / paper 57, these are *separate* record-scale invariants (each constant under `l → μl`), **not numerically equal to each other** — the "= const" chain must not read as an equality between them.

The catalog records the same correction, §2.2(c) (lines 771–774),
verbatim:

> the compressed form *"`κ·σ_A = G·Λ² = const`"* is
> **WRONG AS AN EQUALITY** — these are two *separate* weight-zero invariants,
> each a fixed pure number, **not numerically equal**.

Paper 0 §7 already carries the corrected form (*"only κ·σ_A = 2π and,
separately, G·Λ² = const are weight-zero"*, lines 280–283).  L0
follows paper 0 and the ledger.  **No v11 text may write the equality
chain.**  Note also that `Λ` here is the inverse-length UV/spectral
cutoff, **distinct** from the unimodular cosmological constant `Λ₀`.

---

## 3. L0, at v11's grain

**Setting.**  KINEMATICS (paper 0 §3) supplies the event grammar, the
actor alphabet, the generated causal orders, and configurations on
cuts.  THE LAW is `Γ(cut′ ← cut)`.  Every quantity v11 can compute is
a functional of these data: counts, orders, ratios, rational
transition weights, and functionals thereof.

**L0 [IMPORTED-NO-GO].**  *No internal observable of the generated
record may be identified with a dimensionful length or scale.  Any
v11 construction that fixes Newton's `G` — or any other dimensionful
constant — from inside the generated record is excluded in advance.*

**Status of the transfer, stated exactly.**  The theorem is proved
for the SHARD sealed-record ontology, on the sealed-record weight
calculus and gate G1.  v11's carrier is not that carrier: v11's
records are generated, and the corpus's own doctrine (catalog §0.5)
is that *the v10 generated grammar is not derived from the sealing
formalism* and *v10's actors are not v6's division events*.  The
catalog's transfer judgement is `[MY READING]`, §2.2(e) (lines
785–787):

> **KINEMATICS** — a theorem about what a counting ontology can carry — and it **transfers to v11 almost unchanged**, since v11's kinematics is also a bare causal order with no absolute length.

Paper 0 §11 item 1 lists the `G` no-go under *what transfers intact*.
**L0 does not rest on that judgement.**  L0 imports the *conclusion*
as a **prohibition on v11 claims**.  That import direction is safe
without a transfer proof: a no-go used to forbid v11 from announcing
a scale cannot overclaim, whatever the carrier.  The converse
direction — asserting that v11's carrier *provably* cannot carry a
scale — would require re-proving Theorem G and re-auditing G1 on the
generated grammar, and is **not claimed here**.  When a v11 unit
wants that stronger statement, it must build it.

**The dimensional-analysis caveat, carried from the corpus against
itself** (`v6/publishable/companion-G-scale-grading.md`, via catalog
§2.2(e) lines 793–797), verbatim:

> the grading-homomorphism and weight-zero-subring structure is **standard** — it is the algebra of a graded ring and the content of dimensional analysis (Buckingham-Π; Coleman–Weinberg).  **This note proves no new mainstream theorem.**

L0 therefore claims no novelty.  Its value is that it is engraved
*before* U5 runs.

---

## 4. The only permitted target form: `c_m = Gm²/ℏc`

The no-go leaves exactly one door open, and the source names it.
Paper 57 abstract (line 9), verbatim:

> not the dimensionless gravitational coupling-per-species `c_m = Gm²/ℏc`, which is weight-zero and intrinsic and therefore *eligible* to be a record output (the open hierarchy question)

**Rule.**  Any v11 target in the gravity sector must be
**dimensionless and weight-0**.  `c_m` is the only such target the
corpus has ever identified.  Paper 0 §11 (lines 456–458) states the
count: *"No coupling constant or dimensionless number of nature is
reproduced anywhere in v1–v10 … the one open eligible target is c_m,
and it belongs to Phase IV under L0's bound."*

**Three qualifications, none of which may be dropped.**

1. **Eligible ≠ derivable.**  Paper 57 says *eligible* and calls it
   *the open hierarchy question*.  Nothing in the corpus derives
   `c_m`.
2. **`c_m` rides the MODE axis, not the SCALE axis.**  v7 paper 17
   (line 25), verbatim: *"carrying with it the matter hierarchy
   `c_m = Gm²/ℏc`, which is itself weight-`0` and so *not* a
   scale-orbit datum, but whose value is import-fixed through the same
   mode-canonicalization the rank label awaits, per Papers 5/VIII"*.
   So `c_m` is outside L0's wall but inside a **different** wall
   (MODE, graded **IMPORT-FIXED**).  A v11 unit that reaches `c_m`
   has cleared L0 and has not cleared MODE.
3. **The record-unit attack is already closed.**  Paper 57 §2.3
   (line 51) records that measuring a mass in record units to claim
   `G = c_m/m_rec²` smuggles in the record-length↔lab-length
   conversion the gauge acts on.  A v11 construction of that shape is
   pre-refuted.

---

## 5. The Jacobson–Clausius conditionality of the `G`-leg, carried verbatim

The wall and the *naming* of the wall have different statuses, and
the corpus polices the difference.  Source:
`/Users/felixrobles/workspace/isp/v7/relativistic-isp-v7-paper17-three-walls-classification-theorem.md`
§4.1 (lines 117–128).

**Line 119, verbatim:**

> the SHARD *derivation* that `G` is record-un-derivable does **not** stand on its own. It rides the entropic equation-of-state route

**Lines 121–126 — the four named premises, verbatim:**

> Concretely the `G` leg is conditional on **four** named premises, all isolated in Paper 57 §1:
>
> - **(i) the Jacobson–Clausius premise itself** — that `δQ = T dS` over all local horizons *is* the equation of state of spacetime; the locus of the Padmanabhan "interpretation-not-derivation" critique;
> - **(ii) AXIOM (R)** — the modular / Euclidean-rotation identification fixing the temperature *value* `β = 2π`. Gibbs thermality at *some* `β` is unconditional (record passivity / a finite Lenard theorem), but the value `2π` — hence `T = a/2π` and the Clausius coefficient `η = 1/4G` — rests on this unproven axiom;
> - **(iii) Jacobson's LOCAL-EQUILIBRIUM premise** `θ = σ = 0` at the bifurcation surface — presumed, not derived — which selects pure Einstein over the nonequilibrium `f(R)` / Lovelock branch (Eling–Guedens–Jacobson 2006: dropping it forces a dissipative treatment);
> - **(iv) the CONTINUUM FOCUSING GATE** `θ' = −R_{kk}`, the one imported continuum input (now reduced to two native conditional gates: a finite double-null affine-pair readout and a cofinal-tightness / no-silent-refinement condition).

**Line 128 — the internal asymmetry, verbatim:**

> **The internal asymmetry, stated honestly.** Paper 57's §2 **scale no-go proper** — the weight-counting lemma that every intrinsic record functional is weight-`0` while `σ_A` is weight `−2`, so the absolute unit is outside the `g_λ` gauge orbit — does **not** itself depend on axiom (R). That part is the structural fact the receipt verifies. But the classification *claim* that this missing weight-`(−2)` unit **is gravity's Newton `G`** is delivered through the Jacobson / Clausius Einstein-form route. So the `G` **leg of the classification** is honestly a **conditional no-go** — conditional on the Jacobson–Clausius premise plus the three Paper 57 conditionals. We do **not** present it as a clean structural no-go on a par with tensor and mode. The headline is **two structural no-gos + one conditional**, never a clean threefold all-experiment-fixed symmetry — a load-bearing honesty constraint of this paper.

v10's compression, carried in catalog §2.3(a) (lines 813–815),
verbatim:

> the wall stands unconditionally, the `G`-naming of it is
> conditional.

**The discipline v11 adopts**, catalog §2.3(e) (lines 836–840):
every v11 result of the form *"the records cannot supply X"*

> must state, separately, what identifies the
> missing quantity with a physical constant — and grade that identification on
> its own.

---

## 6. What L0 gates

**U5 — dilation-emergeables (paper 0 §7, lines 322–336; §9b Phase
IV).**  U5 dilates the record Hilbert space by an internal factor and
asks which internal observables the crystal's symmetries force.

- **L0-G1.** U5 may **never announce a scale.**  No observable a dilation
  forces may be reported as a length, an area, a time, a mass, a
  volume, or any quantity of nonzero length-weight.
- **L0-G2.** Every U5 observable is reported with its **weight**.  An
  observable whose weight is not stated is not reportable.
- **L0-G3.** A U5 observable of nonzero weight **may not be reported as
  a second scale.**  The prohibition is on the announcement, not a
  description of the generated carrier: the source's positive reading
  — that such a quantity is a relabeling of *the one record length* —
  belongs to the SHARD sealed-record ontology, where `l_step` is the
  unique dimensionful primitive, and v11's generated carrier has no
  `l_step` to relabel.  Paper 57's second-scale sweep (line 37, line
  39) closed correlation lengths, transmuted scales, and UV fixed
  points by exactly that route; a v11 candidate of any of those shapes
  is pre-refuted **as an announcement of a second scale**, and may be
  reported only as a weighted quantity, never as a discovery.
- **L0-G4.** U5's only admissible gravity-sector target is dimensionless
  (§4).  Reaching `c_m` is not reaching `G`.
- **L0-G5.** The pre-registered spin-2 negative (paper 0 §7, line 331)
  stands independently of L0 and is not weakened by it.

**Phase IV — the gravity road (paper 0 §9b, lines 394–403).**  Phase
IV proposes to derive from renewal counting the two ingredients
Jacobson assumes: the area coefficient and the pure-area property.

- **L0-G6.** Success at that target **may be reported as the Einstein
  form only, never as the Einstein scale.**  L0 forbids the
  announcement of `G` whatever the derivation delivers; it does not
  assert what the generated carrier yields.
- **L0-G7.** Any Phase IV result naming the missing weight-`(−2)` unit
  *as* Newton's `G` inherits §5's four premises **verbatim** and must
  carry them in the same paragraph as the claim.  The wall may be
  stated unconditionally; the naming may not.
- **L0-G8.** The Fisher-identity bridge Gb2 (paper 0 §9b) joins v11 to
  SHARD.  If it runs, paper 57's own **gate G1** becomes a live v11 audit
  obligation — the no-go is airtight *iff* G1 holds, and G1 has never
  been audited on a generated carrier.

---

## 7. Import ledger

| item | status | home |
|---|---|---|
| The unified scale no-go (`σ_A` ↔ `G`, absolute scale un-fixable) | **[IMPORTED-NO-GO]**; source grade **[THEOREM], structurally unconditional** at its own scope, co-tagged **[LATER-CORRECTED]** (the equality chain, §2) | v6 paper 57:31–51 |
| `κ·σ_A = 2π` and, separately, `G·Λ² = const` | **[IMPORTED, verbatim]** — two invariants, never an equality chain | v6 paper 57:35; `v8/LEDGER.md`:47 |
| The weight-counting lemma | **[IMPORTED, verbatim]**, not re-proved on v11's carrier | v6 paper 57:39 |
| Gate G1, and *"airtight iff G1 holds"* | **[IMPORTED, verbatim]**; **never audited on a generated carrier** | v6 paper 57:37 |
| `l_step` the unique dimensionful primitive | **[IMPORTED, verbatim]** | v6 paper 57:37 |
| `c_m = Gm²/ℏc` weight-0, intrinsic, **eligible** | **[IMPORTED, verbatim]**; eligible ≠ derived | v6 paper 57:9 |
| `c_m` import-fixed via mode canonicalization | **[IMPORTED, verbatim]** — a second, different wall | v7 paper 17:25 |
| The four Jacobson premises on the `G`-naming | **[IMPORTED, verbatim]** | v7 paper 17:121–126 |
| The internal asymmetry (wall vs naming) | **[IMPORTED, verbatim]** | v7 paper 17:128 |
| The compressed-equality erratum | **[LATER-CORRECTED]**, carried and obeyed | `v8/LEDGER.md`:47; catalog §2.2(c) |
| Transfer of the no-go to v11's generated carrier | **[MY READING]** in the catalog; **NOT** relied on — L0 imports the conclusion as a prohibition only | catalog §2.2(e) |
| "This note proves no new mainstream theorem" | **[IMPORTED, verbatim]**, corpus against itself | catalog §2.2(e); `v6/publishable/companion-G-scale-grading.md` |

**Nothing in this note is a claim about the generated record.**

---

## 8. Citations, file:line

- `v6/relativistic-isp-v6-paper57-gravity-from-sealed-records.md`
  :9 (abstract, `c_m`), :31 (§2 heading), :33 (§2.1), :35 (the two
  invariants), :37 (gate G1; the seal-rate closure; `l_step` unique),
  :39 (§2.2, the weight-counting lemma), :41–49 (§2.3, the seven
  levers), :51 (the unification).
- `v7/relativistic-isp-v7-paper17-three-walls-classification-theorem.md`
  :25 (`c_m` on the MODE axis), :117 (§4.1 heading), :119, :121–126
  (the four premises), :128 (the internal asymmetry).
- `v8/LEDGER.md`:47 (correction #13, the equality-chain erratum).
- `v11/note-v11p0a-reproduction-catalog.md`
  :721–800 (§2.2), :802–840 (§2.3), :118–134 (§0.5, the doctrine).
- `v11/relativistic-isp-v11-paper0-the-indivisible-record-law.md`
  :278–285 (§7 L0), :322–336 (§7 U5), :394–403 (§9b Phase IV),
  :456–458 (§11, the one open eligible target).
