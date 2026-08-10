# R4 — HOSTILE REVIEW, REVIEWER R2 (EFFECTUS / STRUCTURAL LENS)

**Unit:** R4, the QFT rung — `v14/paper-10-defect-on-the-stage.md`.
**Protocol:** PANEL B of `v14/note-gmain-r4-protocols.md` (`a3a39813e5b5`).
**Pin:** `v14/note-r4-qft-pin.md` (`1582cea5df51`).
**Lens:** the MEANING audit — what the measured objects are entitled to mean.

**Hashes re-verified at the start and the end of this review (sha256-12):**

| artifact | expected | measured |
|---|---|---|
| `v14/paper-10-defect-on-the-stage.md` | `f3e8cc1618f8` | `f3e8cc1618f8` ✓ |
| `v14/code/r4_defect_stage_exact.py` | `b079bb3b8d55` | `b079bb3b8d55` ✓ |
| `v14/code/r4_defect_stage_output.txt` | `58ec08893526` | `58ec08893526` ✓ |
| `v14/code/r4_defect_stage_receipt.json` | `3214f4da3af2` | `3214f4da3af2` ✓ |
| `v14/note-gmain-r4-protocols.md` | `a3a39813e5b5` | `a3a39813e5b5` ✓ |
| `v14/note-r4-qft-pin.md` | `1582cea5df51` | `1582cea5df51` ✓ |
| `v12/paper1-composition-defect.md` (seed) | `81bdab5673fb` | `81bdab5673fb` ✓ |
| `v14/note-r3-adjudication.md` (gate design) | pin says "hash at freeze" (not recorded) | `dc2c2525e1f2` |

Commit `264cb54` verified. **Path note (minor, N1):** the pin §preamble names the
artifacts `r4_defect_stage_exact_output.txt` / `_receipt.json`; the delivery ships
`r4_defect_stage_output.txt` / `_receipt.json`. The protocol's hashes match the
shipped names, so this is a pin/delivery naming drift, not a substitution.

**Grade: ACCEPT-WITH-FIXES.**

**Recomputations: 62 delivered quantities independently reproduced with 0
discrepancies**, over ≈ 24.0 million exact-field operations in an independent
reimplementation (Q(ζ₈) as 4-tuples of `Fraction`s rather than integers over a
common denominator; unitarity decided by the character modulus as well as by the
autocorrelation; nothing imported from the delivery). Six new measurements and
one new theorem are reported below. **Every number the paper prints that I could
reach, I reproduced exactly** — including the 34,925-node/121-leaf/0-non-monomial
five-point sweep, the eight defect values with all eight multiplicities, and
588/3364, 150, 738, 0-of-1792, 216/576, 372/1188, 22, 38, 15/256, 18.

The unit is arithmetically clean. Every finding below is about **meaning**: what
the reproduced numbers are entitled to assert.

---

## 0. FINDINGS, RANKED

### MAJOR

**F1 — THE UNIQUE SCALE IS CONNECTIVE-RELATIVE, AND THE UNIT'S OWN CHOICE
INVENTORY SAYS THE CONNECTIVE IS FREE.** §3.4 classes *the neighbourhood
connective* as `GENUINELY-FREE | 2, both swept`. I recomputed the admissible set
under each of the two declared connectives:

| connective | locality threshold (d=2) | admissible sizes (locality ∧ non-monomial local axis) |
|---|---|---|
| max-norm (Moore) | 4 | **[4]** |
| sum-norm (von Neumann) | 2 | **[2, 4]** |

Under the second declared connective the uniqueness **fails**: L = 2 carries
locality *and* a non-monomial local axis (ord 2 → 16 non-monomial generators over
the very alphabet the unit declares; e.g. c₀ = 1/√2, c₍₁,₀₎ = i/√2 is a unitary,
non-monomial, translation-covariant generator on (Z₂)²). RUNBOOK §15 is explicit:
*claims of physical significance are entered only for quantities GATED as
invariant across the unit's admissible arenas.* `SCALE=L=4-UNIQUE` is not
invariant across an axis the unit itself declares free, and it is entered as the
paper's boldest claim (the title).

The unit's own code shows the way out — and does not take it.
`G-LINKS-IN-BALL` (code line 967) checks the anchored links
{(1,0),(0,1),(1,1)} against a **hard-coded max-norm ball**. Since (1,1) has
sum-norm 2, the anchored link set *forces* the max-norm connective. So the truth
is one of two things, and the paper asserts neither:

- (A) the connective is genuinely free → the SCALE claim is arena-relative and
  §15 bars it as physics; or
- (B) the connective is FORCED by the anchored link set → §3.4's inventory row is
  **a false classification**, the parity witness (Δ = −2) is not the death
  certificate of a live alternative but the measurement of a *forbidden* one, and
  the SCALE segment must carry `CONNECTIVE=MAX-NORM(FORCED-BY-ANCHORED-LINK-(1,1))`.

(B) is correct on the code, and it is the repair I recommend — but it relocates
the headline: **the unique scale is a theorem about I7's declared link set** (the
diagonal link is what makes the Chebyshev ball the adjacency), not a law of the
substrate. This is also the #313 boundary-parity addendum only half-honoured: the
parity witness fires, but its consequence is never propagated into
`G-UNIQUE-SCALE`, which reads `moore_rows` only. No mutant can catch this,
because the alternative connective is never routed into the admissibility loop.

**Repair.** (i) Reclassify the connective row as `FORCED (anchored)`, fibre 1,
with the (1,1)-link reason printed; (ii) carry the connective in the SCALE
segment; (iii) add a mutant that routes the sum-norm rows into the admissibility
loop and dies at a gate that names the anchored-link forcing; (iv) correct §2's
scope line (below, F9).

**F2 — A FALSE BICONDITIONAL INSIDE A GATED VERDICT SEGMENT.** The verdict reads

```
SCALE=L=4-UNIQUE(LOCALITY-IFF-L>=4;NON-MONOMIAL-LOCAL-AXIS-IFF-L<=4)
```

The first conjunct is a true biconditional (measured, and provable for all L at
d = 2 under the anchored adjacency). **The second is false.** At L = 3 the order-3
row of the unit's own table is `distinct 24 / monomial 24 / non-monomial 0`
(reproduced exactly): L = 3 satisfies "L ≤ 4" and carries **no** non-monomial
local axis. The set of swept sizes with a non-monomial local axis is {2, 4}, not
{2, 3, 4}. The paper's prose §3.3 is correct — it says *"a non-monomial local-axis
generator **requires** L ≤ 4"*, an implication. The verdict string strengthens
`requires` to `IFF` and thereby prints a false claim, in the one place the
programme treats as load-bearing. The paper's own table refutes its own verdict
segment.

**Repair.** `NON-MONOMIAL-LOCAL-AXIS-ONLY-IF-L<=4;PRESENT-AT-L-IN-{2,4}`, and a
gate that derives the parenthetical from the measured `ordc` rows rather than
composing it from typed text (the present segment is assembled as a literal).

**F3 — THE TITLE AND THE §9 BULLET ARE REFUTED BY AN EXACT CONSTRUCTION.** The
title reads *"One Lattice Size Admits an Indivisible Family At All, and On It the
Defect Is Present"*; §9's Decided list reads *"One lattice size in the swept
range admits the construction at all."* Both are false without the word **local**.

Constructive counterexample, exact and rational, verified at L ∈ {4, 5, 6, 7, 9}:
the Householder/Grover circulant c(v) = δ_{v,0} − 2/L² on (Z_L)² is unitary
(autocorrelation δ, checked at every lag), non-monomial (full support),
translation-covariant, and carries a nonzero composition defect at **every** size:

| L | unitary | support | Δᴮ(c,c) nonzero cells | values |
|---|---|---|---|---|
| 4 | yes | 16 | 16 | +105/256, −7/256 |
| 5 | yes | 25 | 25 | +4416/15625, −184/15625 |
| 6 | yes | 36 | 36 | +595/2916, −17/2916 |
| 7 | yes | 49 | 49 | +18048/117649, −376/117649 |
| 9 | yes | 81 | 81 | +50560/531441, −632/531441 |

So a spatially structured, translation-covariant, defect-carrying family exists at
*every* swept size. What is unique to L = 4 is the existence of such a family
among **local** (radius-1) generators. The verdict's parenthetical protects this
distinction; the title and the §9 bullet drop it. Per the §13 addendum (#20,
"prose renders from the receipt") this is exactly the surface where the
programme's false claims have historically lived.

**Repair.** Title → *"One Lattice Size Admits a **Local** Indivisible Family, and
On It the Defect Is Present"*; §9 bullet → *"One lattice size in the swept range
admits the **local-move** construction at all; non-local non-monomial unitaries
exist at every size and carry a defect (exhibited)."*

**F4 — THE STATE-MOTION "BACKGROUND" HALF IS AN IDENTITY, SO FR2 IS ANSWERED BY
CONSTRUCTION, NOT MEASURED.** §8 presents two facts. The second (18 distinct
responses) is a measurement. **The first is a tautology of linear algebra.** The
code defines δ(p) = Δᴮ·p (line 2252) and reconstructs the coefficient from the
sixteen point-mass responses (line 2268), i.e. from the sixteen columns of Δᴮ in
the standard basis. `recon == Dm` is the statement that the matrix of a linear map
in the standard basis is that matrix. It is true for **every** Δᴮ, every family,
every arena. I confirmed it holds at 64 of 64 nonzero probe pairs — as it must.
`MUT-STATE-BACKGROUND` kills the gate by setting `recon = {}`; it breaks the code,
not the world. Per the §14 addendum (#208), *analytically-forced clauses are
disclosures, not must-pass gates*.

This matters because the paper offers it as *"the honest answer to the successor
requirement that coefficients move with the state"* (FR2). FR2 is not tested. On
this arena it **cannot** be tested: a coefficient can only move with the state if
the generator's coefficients are functionals of the state, which requires either
a self-consistent (nonlinear/mean-field) law, state-dependent division-event
times, or leaving the single-occupation sector so that one excitation's effective
coefficient depends on another's occupation — precisely the interaction term the
unit disclaims. That is the honest statement, and it is a stronger result than the
one delivered: **the frozen-stage stratification is not confirmed at the quantum
layer here; it is enforced by the arena.**

**Repair.** Re-register `G-STATE-COEFFICIENT-BACKGROUND` as `FORCED` (a
disclosure, third never-falsified entry with a machine-checked forcing); rewrite
§8 to say that state-coupling is *out of scope by the single-occupation sector and
the linear law*, and name the three routes above as the successor's requirement;
keep `G-STATE-OBSERVABLE-MOVES` as the measurement it is. Verdict segment →
`STATE=BACKGROUND-COEFFICIENT-BY-CONSTRUCTION(LINEAR-LAW;SINGLE-OCCUPATION);
OBSERVABLE-MOVES-AT-18-DISTINCT-RESPONSES`.

**F5 — "INDIVISIBLE" IS DECLARED, NEVER MEASURED, AND THE SEED FORBIDS THE
INFERENCE.** The seed engraves (`81bdab5673fb` §2.3, Theorem 2.2 and the
box that follows): *"Δᴮ ≠ 0 does not imply stochastic indivisibility… **Engraved.**
Δᴮ is an amplitude-level coherence measure. It is not a divisibility measure, not
a witness of indivisibility."* The seed separates three objects: Δᴮ, the residual
D of a declared law, and existential divisibility d_div = inf_K‖Γ₂₀ − KΓ₁₀‖.

The delivery measures the first, declares the second (the Born declaration), and
**never touches the third**: `grep -i "divisib\|divisor"` over the instrument
returns only the ARENA prose string; no stochastic-divisor search is run. Yet §9's
Decided list asserts *"a spatially structured **indivisible** family exists."* On
this family that is a restatement of the declared division-event times (t = 0, 2
are events; t = 1 is not), not a measured property — and by the seed's Theorem 2.2
the declared and existential readings can come apart.

**Repair.** Either (i) measure it — for the 588 nonzero pairs, search for a
stochastic K with K·B(U₁) = B(U₂U₁) (the seed's S(c) construction generalises;
this is a small LP/exact search on 16×16 column-stochastic matrices) and carry
`INDIVISIBILITY=MEASURED-AT-<n>-OF-588`; or (ii) demote the word everywhere to
`declared-indivisible` and carry `INDIVISIBILITY=DECLARED-BY-DIVISION-EVENT-TIMES`
in the SCOPE segment. (ii) is cheap and honest; (i) is the real result.

**F6 — THE VERDICT-BEARING STRATUM IS ABELIAN, AND THE MANDATORY GATE EXCLUDES
EXACTLY THE NON-COMMUTING GENERATORS.** Measured, exhaustively:

| stratum | non-commuting ordered pairs |
|---|---|
| the 58 FULL-transport circulants (the verdict's stratum) | **0 of 3,364** |
| the 4 excluded brickwork generators, among themselves | 4 of 16 |
| circulant × brickwork | 128 of 232 |
| pairs involving a scrambled control | 104 |

Circulant convolution on an abelian group commutes; the entire verdict-bearing
family is therefore a commutative algebra, simultaneously diagonalised by the
lattice characters. **Every commutator, every plaquette holonomy and every Wilson
loop assembled from R4's verdict stratum is the identity by a theorem.** The only
non-commutativity on this stage lives in the 4 brickwork generators — which the
realization-census gate removes from the verdict. This is the decisive input to
R5 (§6 below) and it also rules on K4: the gate is not neutral bookkeeping; it
selects the commutative sector.

### MODERATE

**F7 — THE "FIRST EXCITATION-TYPE TABLE" HAS 22 ROWS AND 14 LABELS.** The declared
class invariants (support, radius, ord(axis), transport level, projective period,
plus orbit size and kind) are constant on every orbit — I verified this, 0
violations. But they do **not separate the classes**: the 22 extended classes carry
only **14 distinct invariant tuples**; six labels are shared, one of them by four
classes at once:

| shared label (size, kind, supp, radius, ord, level, period) | classes |
|---|---|
| (4, CIRC, 3, 1, 4, FULL, 4) | **4** |
| (4, CIRC, 1, 1, 4, FULL, 4) | 2 |
| (4, CIRC, 2, 1, 4, FULL, 2) | 2 |
| (2, CIRC, 2, 2, 2, FULL, 4) | 2 |
| (4, CIRC, 3, 2, 4, FULL, 4) | 2 |
| (1, CIRC, 2, 2, 2, FULL, 4) | 2 |

Adding the self-defect value multiset as a further invariant changes nothing
(still 14). Adding the **direction** — the D₄-orbit of the axis, of which there
are five: {(1,0),(0,1)}, {(1,1),(1,3)}, {(1,2),(2,1)}, {(2,0),(0,2)}, {(2,2)} —
raises it to 17 of 22; the residual five collisions are mirror/chirality pairs.
So the label set is completable, and **the two missing labels are a direction
label and a chirality label** — i.e. exactly the momentum-like and parity-like
quantum numbers the census is missing (F8, §K3). As delivered, the table is an
orbit census with an *incomplete* invariant system; Wigner's (m, s) is complete,
and the analogy should not be drawn without this disclosure.

**Repair.** Print the collision structure; add the axis D₄-orbit and a chirality
invariant; or state plainly that the declared invariants are constant but not
separating.

**F8 — "TRANSLATIONS ACT TRIVIALLY" IS FORCED, NOT MEASURED.** §6 gives this its
own paragraph and says *"That is measured, not assumed."* A circulant is by
definition a matrix commuting with every lattice translation; conjugating it by a
translation returns it **identically**, for every circulant, on every lattice,
always. The 58 singleton orbits are an identity of the construction. Per #208 this
is a disclosure; `G-CLASS-TRANSLATION-TRIVIAL` carries a declared falsifier that
can only fire when the code misreports, never when the world differs. (The
non-trivial half — that the *controls* move — is a genuine measurement and should
be the sentence that survives.)

**F9 — §2'S SCOPE LINE MISDESCRIBES ITS OWN TABLE, AND THE BOLD CLAIM DROPS THE
QUALIFIER.** The locality table's scope line reads *"exhaustive over L ∈ {2,…,9}
and d ∈ {1,2,3}, both declared connectives."* The rows shown are max-norm; under
the sum-norm connective rows L = 2 and L = 3 **flip** to `locality = yes`
(measured: thresholds 4 vs 2, the unit's own Δ = −2). The following bolded
sentence, *"Locality on this stage requires L ≥ 4,"* is true only under the
anchored adjacency. The paper does print the vN threshold two paragraphs earlier —
so this is not concealment, it is a conclusion drawn one qualifier short.

**F10 — THE MANDATORY GATE'S CLASSIFICATION IS A FUNCTION OF THE DECLARED KIND
FOR 62 OF 64 GENERATORS, AND 114 OF ITS 150 EXCLUSIONS ARE THE NEGATIVE CONTROL.**
Measured levels: CIRC → FULL (58/58), BRICK → OCC (4/4), SCRAM → {NONE, OCC}. So
the "realization census" re-derives the partition the pool was built on;
it discriminates only inside the 2-element scrambled control. And the excluded
nonzero defects break down as

| excluded pairs | count |
|---|---|
| involving a scrambled control | **114** |
| brickwork without a scramble | 36 |
| total | 150 |

§7 says *"The brickwork controls are the substance of that exclusion."* By count
they are not: the deliberately scrambled negative control — an object excluded by
construction, never a candidate for the verdict — supplies 114 of the 150. The
gate's *principled* bite is 36. The verdict's `EXCLUDED-NONZERO=150` therefore
overstates the gate's contentful bite roughly four-fold.

**F11 — THE 5-POINT "DECLARED EXTENSION" IS RUN WHERE NOTHING COULD BE FOUND.**
The extension sweeps the von Neumann stencil at L = 5 — above the collapse
threshold, where the *same* two-lag argument that proves the 3-term theorem
already applies to any support inside the ball (see the theorem in §K2 below). It
therefore tests the stencil-class question at the one size where the answer is
forced. Run at **L = 4** it is informative: I swept it (150,125 nodes, 1,561
leaves) and found **160 non-monomial** five-point generators — a second, wider
local family at the unique scale, entirely unexamined by the unit.

**F12 — MEASURED RESTRICTIONS MISSING FROM THE SEGMENTS (K5).** See §K5. Six,
two of them decisive.

### MINOR

**N1** — pin/delivery artifact-naming drift (top of this file).
**N2** — the state-motion probe is a **single** pair (`circ_pool[0], circ_pool[1]`
with a fallback scan); the segment reads as a family-wide statement. It happens to
be robust (I measured 18/18 at 64 of 64 nonzero pairs) but the delivery does not
know that. Print the probe count.
**N3** — §5.1's *"This is verified as an exact matrix identity on the probe pairs"*
verifies B(U₂U₁) = B(U₂)B(U₁) + Δᴮ, which is the definition of Δᴮ rearranged. The
paper registers the coherence law FORCED in §5.3 but not this one. Same class as F4.

---

## K1 — THE DEFECT CENSUS: DERIVABILITY, AND THE UNIT'S REAL CONTRIBUTION

**The operator's derivability question lands, and lands hard.** I tested a purely
combinatorial predictor against the full circulant census:

> *nonzero(v, u) ⟺ ∃ s such that |supp(v) ∩ (s − supp(u))| ≥ 2*
> (i.e. some separation is reached by at least two paths)

over all 3,364 circulant ordered pairs:

| | predicted nonzero | predicted zero |
|---|---|---|
| **measured nonzero** | 588 | **0** |
| **measured zero** | **0** | 2,776 |

Perfect agreement. The count **588 of 3,364 is a function of the 58 support sets
alone** — it does not depend on a single coefficient value, and would be unchanged
by any alphabet substitution preserving supports and unitarity. Splitting per #208:

| clause | status | why |
|---|---|---|
| `DEFECT=588-OF-3364` | **FORCED-GIVEN-NO-CANCELLATION** (support combinatorics) | one-overlap ⇒ no cross term ⇒ Δ = 0 is algebra; the count is then a count of support intersections |
| `MARKOV=0-OF-1792` | **FORCED** | the seed's Theorem 2.7 annihilator, restated; a monomial factor gives exactly one path per cell |
| `VALUES=8-DISTINCT`, `ALL-RATIONAL-ROWS=588` | **MEASURED** (alphabet arithmetic) | the moduli {1, ½, 1/√2} put every cross term in (1/8)ℤ; that the irrational parts always cancel is a fact about the declared alphabet, not about the stage |
| `LOCALITY=216-OF-576 / 372-OF-1188` | **FORCED** by the same support criterion | radius does not enter the criterion at all |
| `TWO-POINT=SEPARATIONS=16;MAX-DEFECT-RADIUS=2` | **CEILING** | 16 = all separations on a 16-site torus; 2 = the Chebyshev diameter of Z₄². Both are arena maxima, not profiles (F12/§K5) |
| `EQUAL-TIME=15/256` | **FORCED** by the state | 1/16 − 1/256; a function of \|X\| and the declared uniform state, identical for every family |
| `STATE=BACKGROUND-COEFFICIENT` | **FORCED** (F4) | identity of linear algebra |
| `CLASSES=22/38` | **MEASURED** | genuine orbit computation; invariants constant (measured), not separating (F7) |
| `REALIZATION=EXCLUDED-NONZERO=150` | **MEASURED but mostly control** (F10) | principled bite 36 |

**What remains measured, and is the unit's real contribution.** Three things, and
they are worth having:

1. **The no-cancellation fact.** Every one of the 588 candidate pairs that *could*
   have cancelled exactly, did not: **0 exact cancellations in 3,364 pairs.** The
   defect never accidentally vanishes on this family. This is the genuinely
   contingent half of the census and the paper does not currently claim it.
2. **The eight exact values with their multiplicities**, and the all-rational
   result (588 of 588) inside a field carrying irrational elements — a real
   measurement about the declared alphabet's arithmetic.
3. **The orbit census** (22/38 with constant invariants) and the transport-level
   census as *data*, whatever their labelling defects.

**Recommendation.** Restate §4.2 as: *the nonzero set is exactly the
two-path-overlap set (588 of 3,364, derived), and the measurement is that no
overlap cancels (0 of 588) and that every value is rational (588 of 588).* That is
a stronger paper than "588 pairs carry a defect", because it says *why*.

---

## K2 — THE L = 4 UNIQUENESS THEOREM: GRADED

### The theorem itself: CORRECT, and I strengthen it

I re-derived the order-collapse proof line by line. It is valid. For n ≥ 5 the
offsets 0, ±a, ±2a are distinct, so A(2a) = c₋ₐ·c̄ₐ = 0 and
A(a) = c₀c̄ₐ + c₋ₐc̄₀ = 0; the case split is exhaustive and forces support ≤ 1. It
uses only field operations, so it is alphabet- and field-independent, as claimed.
The machine confirmation reproduces exactly (8/32/24/72/24/24/24/24/24 distinct,
with monomial splits 8/16/24/24/24/24/24/24/24).

**New theorem (I supply it; the unit should adopt it).**

> **Moore-ball collapse.** *Let L ≥ 5 and let U be a unitary generator on (Z_L)²
> whose coefficient map is supported inside the radius-1 Chebyshev ball
> {−1,0,1}². Then U is monomial.* (Any field closed under conjugation.)
>
> *Proof.* Write the ball's three columns X = (c₋₁,ⱼ), Y = (c₀,ⱼ), Z = (c₁,ⱼ),
> j ∈ {−1,0,1}. For L ≥ 5 there is no wraparound, so the lag (2,t) receives
> contributions only from column −1 paired with column +1:
> A(2,t) = Σⱼ c₋₁,ⱼ · conj(c₁,ⱼ₊ₜ) = 0 for every t ∈ {−2,…,2}. That is the
> vanishing of the entire aperiodic cross-correlation of the length-3 sequences X
> and Z, i.e. X(x)·Z̃(x) ≡ 0 in the Laurent polynomial ring — an integral domain —
> so **X ≡ 0 or Z ≡ 0**. Say Z ≡ 0. Then the lag (1,t) receives contributions only
> from column −1 paired with column 0, giving likewise **X ≡ 0 or Y ≡ 0**. Either
> way the support lies in a single column; the vertical lags (0,t) then give the
> vanishing aperiodic autocorrelation of a length-3 sequence, which by the unit's
> own two-lag argument forces support ≤ 1. The case X ≡ 0 is symmetric. ∎

This closes the paper's largest self-declared scope hole ("the 9-point stencil is
not swept"): **no local stencil whatsoever — 3-term, 5-point, 9-point, or any
subset of the radius-1 ball — admits a non-monomial unitary at any L ≥ 5, over any
field.** I also confirmed it by brute force at L = 5 on the full 9-point stencil:
**23,465,025 nodes visited, 217 complete assignments, 0 non-monomial.**

**Second scope hole closed.** The paper declares the order-3 emptiness
alphabet-relative, and it is: over Q(ζ₃, 1/√3) the Gauss-sum sequence
c_v = ω^{v²}/√3 has A(m) = (ω^{−m²}/3)Σ_v ω^{−2vm} = 0 for m ≠ 0 — a non-monomial
unitary 3-term generator at order 3. But this **cannot** disturb the uniqueness:
L = 3 (and L = 1) fail locality under the anchored adjacency regardless of the
field. Hence **the admissible set is {4} for every alphabet enlargement**, and the
declared alphabet-relativity caveat, while true of the table row, is irrelevant to
the verdict. The paper is entitled to say so and currently does not.

### How much physics hangs on the 3-term axis choice: LESS THAN I EXPECTED, BUT THE HEADLINE STILL OVER-READS

With the new theorem, the stencil-class relativity that PANEL B asks about is
**largely dissolved within the local class**. What remains is the boundary of the
word *local*, and there the headline breaks (F3): the Householder circulant
δ_{v,0} − 2/L² is unitary, non-monomial, rational, translation-covariant and
defect-carrying at **every** L. So the honest statement of the theorem is:

> **At d = 2, under the anchored (max-norm) adjacency, L = 4 is the unique lattice
> size in {2,…,9} at which a *local* generator can superpose. Non-local superposing
> generators — and hence a nonzero composition defect — exist at every size.**

Everything the unit measures about "quantum structure at exactly one scale" is
therefore about **the locality of the moves**, never about the existence of
quantum structure. The unit's own pool concedes it: 5 of its 9 axes are *non-local*
and contribute 372 of the 588 verdict-bearing nonzero defects.

### Charge without momentum, and whether the theorem forbids motion

At the unique scale, translations act trivially on the whole circulant family
(F8 — forced), the family is abelian (F6 — forced), and every non-monomial
generator has **exactly zero one-step drift**:

| support | generators | nonzero drift ⟨Δx⟩ |
|---|---|---|
| 1 (monomial) | 16 | **12** |
| 2 | 18 | 0 |
| 3 | 24 | 0 |

So on the delivered family, **the generators that move never interfere, and the
generators that interfere never move**. That is "charge without momentum" made
exact, and it is a striking measured statement the paper does not make.

**Does the theorem forbid motion-carrying excitations? No — and I show it
constructively.** The drift-free-ness above is *alphabet*-relative, not
theorem-forced. Over the declared moduli {1, ½, 1/√2}, unitarity on a two-term
support {a, −a} forces |c_a|² + |c₋ₐ|² = 1 with both moduli in the set, hence
|c_a| = |c₋ₐ| and zero drift. Widen the modulus set by one element and the
obstruction vanishes. In Q(i, √3), on the order-4 axis a = (1,0) at L = 4:

> c_a = 1/2, c₋ₐ = i·√3/2, c₀ = 0 →
> **unitary** (all lags verified), **support 2** (non-monomial),
> **⟨Δx⟩ = −1/2 ≠ 0** (motion), **Δᴮ(c,c) = +3/8 at s=(0,0), −3/8 at s=(2,0)**
> (interference). The same coefficients are *not* unitary at L = 6 — the collapse
> theorem still bites.

**So a motion-carrying, interference-carrying generator already exists at the
unique scale**; it is excluded only by the declared 25-element alphabet.

**What a successor needs for motion-carrying types (precise):**

1. **Widen the modulus set** so unitarity admits unequal weights on +a and −a
   (e.g. add √3/2 and 1/2 as a pair). Then drift and defect coexist, measured.
2. **Classify states, not generators.** The translation-triviality is a fact about
   circulant *operators*; translations act *faithfully* on the state space. The
   momentum labels are already in the delivery's hands: every circulant is
   diagonal in the lattice characters, and I measured that **57 of 58 have a
   non-constant eigenphase** — a genuine dispersion relation θ(k) exists in this
   very family and is never reported. Types should be orbits of the joint action
   on (state, generator), labelled by (k, θ(k)); then translations act
   non-trivially and the label set separates (F7).
3. **The theorem forbids none of this.** It constrains the *support* of local
   generators at L ≥ 5; it says nothing about drift, dispersion, or the state
   sector, and nothing at all at L = 4.

### Verdict on K2: law of the substrate, or of the instrument's declared family?

**Neither, exactly: it is a law of the declared *stage*.** The L ≥ 4 half is a
theorem about I7's anchored link set (the diagonal link forces the Chebyshev
ball — F1); the L ≤ 4 half is a theorem about perfect autocorrelation inside a
radius-1 ball, alphabet- and field-independent, and now (with the new theorem)
stencil-independent within the local class. What is *not* substrate is the word
"quantum-spatial structure": that exists at every scale (F3). The defensible
headline is **"local superposition has a unique admissible scale on this stage"**,
which is a good result and should be the title.

---

## K3 — THE TRANSFORMATION-TYPE CENSUS: HONEST AT WHAT STRENGTH

**Reproduced exactly:** 22 classes under the extended group (order 128), 38 under
the anchored chart group (order 32), sizes {1, 2, 4}, orbits partition the pool,
invariants constant on every orbit (0 violations), 58 translation singletons,
projective periods {1, 2, 4}, raw orders {2, 4}.

**Honest strength: it is a conjugacy census of *laws*, with a constant but
non-separating label system.** Three limits, in order of severity:

1. **Category.** Wigner classifies unitary irreps of the symmetry group acting on
   *states*; the labels (m, s) are complete and are physical properties of
   *excitations*. This census classifies *generators* by conjugation. A
   "transformation-type" here is a conjugacy class of dynamical laws. That is a
   legitimate and interesting object — but it is not an excitation type, and the
   pin's phrase "the first excitation-type table of the programme" over-reads it.
   The paper's own care with the word *particle* should extend to *excitation*.
2. **Labels do not label** (F7): 22 classes, 14 distinct invariant tuples, one
   label shared by four classes. Wigner's labels separate; these do not. The
   missing invariants are a direction label (→17 of 22) and a chirality label.
3. **No momentum, by construction** (F8): translations act trivially on circulants
   as an identity, so the census's group action is *entirely* the point group. The
   table's charges are point-group charges only. That is exactly the
   charge-without-momentum tension PANEL B names — and its cause is not the
   unique scale but the choice to classify circulants by conjugation. Momentum is
   available (the character basis; 57/58 non-constant eigenphases) and unused.

**The Wigner analogy's limits, stated for the paper.** Keep: *orbits of a
symmetry group, labelled by invariants that are constant on orbits.* Drop: any
suggestion of completeness, of state-classification, or of a mass/momentum
analogue. The honest sentence is: *"the first conjugacy census of the programme's
dynamical laws under a declared spatial symmetry group, with a constant but
non-separating invariant system."*

**Is "translations act trivially" a real finding?** No — forced (F8). The real
finding in that paragraph is its converse: the controls *do* move, which is what
makes the covariance gate non-vacuous.

---

## K4 — THE GATES: RULINGS

### The realization gate's 150 exclusions: BOOKKEEPING, and applied outside its motivating conditions

**Ruling: bookkeeping, with a physics cost.** Four grounds:

1. **It removes no artifact.** R3's motivation (adjudication §2.10, §1.C) was that
   a defect existing *because the record fails to transport* is an artifact of an
   incomplete realization, and that maximal transport dissolves it. That condition
   is not met here. The brickwork generators are ordinary local unitaries — a
   two-site coin on a parity class of dominoes — whose defects are genuine
   interference of a genuine quantum walk. Excluding them does not purify the
   census; it restricts to a covariant sub-family. The excluded defects are not
   *contradicted* at maximal transport, they are simply a different family.
2. **It re-derives the pool's own partition** (F10): level is a function of the
   declared kind for 62 of 64 generators.
3. **Its measured bite is mostly the negative control** (F10): 114 of the 150
   involve a deliberately scrambled generator, excluded by construction. The
   principled bite is 36.
4. **It does no work on the head.** DEFECT-PRESENT holds at either reading (588 of
   3,364, or 738 of 4,096). The gate moves segments, never the verdict.

**But it is not harmless, and this is the finding that matters:** it selects the
*commuting* sub-family (F6). The 58 admitted generators pairwise commute, 0 of
3,364; the 4 excluded ones are the entire source of non-commutativity on the
stage. A gate designed to purify a *transport* question turns out, at this arena,
to be a projector onto the abelian sector. That is a general lesson for the
programme — an inherited gate must be re-motivated at each arena — and it is a
binding constraint on R5.

**Repair.** Keep the gate (it is the pin's mandate) but (i) report the principled
bite 36 alongside 150; (ii) state that the excluded stratum is not a degraded
realization but a distinct, non-commuting family; (iii) print the commutator
census — it costs 3,364 comparisons and it is the most consequential structural
fact on the stage.

### The state-motion verdict: BACKGROUND-COEFFICIENT is half identity, half measurement

Ruled at F4. The label `BACKGROUND-COEFFICIENT-OBSERVABLE-MOVES` should read
`BACKGROUND-BY-CONSTRUCTION / OBSERVABLE-MOVES-MEASURED`. **What the frozen-stage
stratification is confirmed at, here, is the arena, not the quantum layer.** On a
linear law over a single-occupation sector, no coefficient can move with the
state; R3's finding (a central extension with a background coefficient) is
*reproduced* by a system that could not have done otherwise.

**What state-coupling would require** (the successor's list, in increasing cost):
(a) a two-excitation sector, so that one excitation's effective coefficient is a
functional of the other's occupation — the smallest honest interaction, and the
first place Δᴮ could acquire state dependence; (b) state-dependent division-event
times (the cut moves with p), which is within the declared-freedom of the arena
and costs nothing structurally; (c) a self-consistent (mean-field) generator
U[p] — the largest departure, and the one that would genuinely break linearity.
Any of these makes `G-STATE-COEFFICIENT-BACKGROUND` falsifiable for the first time.

### The other gates named in PANEL B

- **Light cone.** `LIGHTCONE=ONE-NEIGHBOURHOOD-PER-STEP` is supp(c∗d) ⊆
  supp(c)+supp(d) — forced. The measured half is the *non*-saturation (33 of 58
  attain the half-width), and that is the sentence that should carry the claim.
- **Two-point tables.** `EQUAL-TIME=15/256` is p(1−p) at p = 1/16 — a function of
  \|X\| and the declared uniform state, identical for every family on 16 sites.
  It carries no information about the dynamics and should be labelled a state
  arithmetic disclosure, not a two-point measurement.
- **Projective-period gauge self-test.** This one is genuinely good and is the
  model the rest of the unit should follow: the invariant is measured under the
  symmetry's own action, the raw order moves, the projective period does not, and
  the negative direction fires at all 42 combinations. §14-compliant, and I
  reproduce {1,2,4} projective / {2,4} raw.

---

## K5 — ARE ALL MEASURED RESTRICTIONS CARRIED IN SEGMENTS?

**No.** The SCOPE segment carries `D=2;L=4;FIELD=Q(ZETA-8);ALPHABET=25;
GENERATORS=64;FINITE-LATTICE-ONLY;NO-CONTINUUM-CLAIM;
NO-INTERACTING-THEORY-CLAIM-BEYOND-THE-COMPOSED-SEGMENT-DEFECT`. Missing:

| restriction | where it bites | severity |
|---|---|---|
| **STENCIL = 3-term axis** (5-point at one size; 9-point never) | the entire SCALE segment | decisive |
| **CONNECTIVE = max-norm** (the other declared one gives {2,4}) | the SCALE segment (F1) | decisive |
| **SWEPT RANGE L ∈ {2..9}** — the paper says "in the swept range", the verdict says `L=4-UNIQUE` flat | SCALE | moderate |
| **SECTOR = single occupation** (one excitation, ever) | STATE, TWO-POINT, and the whole no-interaction disclaimer | moderate |
| **INDIVISIBILITY = DECLARED** by the division-event times, never measured (F5) | the head's noun | moderate |
| **probe scope = 1 pair** for the state-motion segment (N2) | STATE | minor |
| **ceiling saturation**: `SEPARATIONS=16` is all 16 separations on a 16-site torus; `MAX-DEFECT-RADIUS=2` is the Chebyshev diameter | TWO-POINT | moderate |

The ceiling item deserves its own sentence, because it is a structural
consequence of the unit's own theorem: **the unique admissible scale is exactly
the scale at which the free-field-analog observables are ceiling-saturated.** At
L = 4 the lattice diameter is 2 and there are only three Chebyshev separation
classes, so no decay profile and no dispersion curve can be resolved. The
uniqueness theorem confines the two-point benchmark to the one lattice where it
carries almost no information. That tension is real physics and the paper should
say it: *the local family lives only where the propagator cannot be resolved.*
(Both routes out are visible: the wider-alphabet family of §K2, and the non-local
family of F3, live at larger L.)

---

## THE R5 RECOMMENDATION

R5 in the charter is **gauge/QCD: the declaration-connection's holonomy algebra
under refinement, then Yang–Mills-likeness and the confinement analog.** R4 now
supplies the stage, CR-D supplies the alternating-tower datum, and Γ-main supplies
holonomy machinery (rank-2 ⟨2,3⟩ reproduced, rank-3 k-primes, rank-7 Γ-primes,
REC flat at all readings, plus the scramble caveat that a group reading is not
automatically a discriminating statistic). My recommendation is shaped by **F6**,
which is the single most consequential thing this review found.

### The datum the pin must start from

> **R4's verdict-bearing stratum is abelian: 0 of 3,364 commutators are nonzero.
> Every plaquette holonomy and every Wilson loop built from it is the identity by
> a theorem. The only non-commuting generators on the stage are the 4 brickwork
> generators — exactly the ones R4's mandatory realization gate excludes.**

A gauge rung built on R4's FULL stratum is **pre-committed to flat, abelian
holonomy**. It would return a trivial answer at exit 0 and could not be falsified.
The pin must say this explicitly, in its §1, as an inherited fact.

### What the pin should pose

**THE ARENA (declared as data, §15):** the *sub-maximal-transport* stratum R4
excluded, promoted to a first-class family — **link-indexed** unitaries on the
L = 4 torus: a coin per link (32 links, 16 plaquettes), from a declared coin
alphabet, applied in declared parity strata (the brickwork/Floquet shape,
generalised so the coin may vary from link to link). This is the lattice-gauge
shape the charter names, and R4 proved it is where the non-commutativity is.
Boundary = (Z₄)² with its links and plaquettes; family = link-indexed coins; law =
Barandes' Γ = |Θ|∘²; state = single occupation, with one declared two-excitation
extension pre-registered (see G3); arena = the order-32 chart group and the
order-128 extension, both censused, per R4.

**THE QUESTION:** *does the declaration-connection on the record stage carry a
non-abelian holonomy group, does it survive one refinement step, and does its
curvature couple to Δᴮ?*

### Pre-registered gates

- **G1 — NON-ABELIAN NON-VACUITY (decisive).** The plaquette-holonomy group is
  *measured*: its commutator subgroup must be gated nontrivial, and the group is
  reported as an isomorphism class with its rank, never as matrices. **R4's FULL
  stratum is the mandatory NEGATIVE control** — it must return the trivial group
  (0 of 3,364; a theorem, so this is the flat control that REC plays for Γ-main).
  Without a negative control that is *provably* flat, a non-abelian result is
  uninterpretable.
- **G2 — GATE-INHERITANCE AUDIT (binding, and the R4 lesson).** The
  realization-census gate **may not be inherited unmodified**. R5 must state at
  pin time whether "maximal declared transport" is compatible with non-abelian
  holonomy *on its arena*, and must census which transport level each link-local
  generator attains. **If the maximal level again selects a commuting sub-family,
  the verdict is `R5-BLOCKED-AT-THE-GATE` — first-class, and a real result about
  the programme's own gate.** (R4 shows a gate motivated by one unit's transport
  question acting as a projector onto the abelian sector at the next arena.)
- **G3 — CURVATURE ⟺ DEFECT, AT MATCHED COORDINATES (§15 addendum).** Measure
  whether a nonzero plaquette commutator is accompanied by a nonzero Δᴮ across the
  same cut, with coin values, division-event times, leg declaration and gauge
  fixing all held equal; the matched table is the primary object and the contrast
  is read off it. Pre-register three outcomes: `CURVATURE-CARRIES-DEFECT` /
  `CURVATURE-DEFECT-INDEPENDENT` / `DEFECT-WITHOUT-CURVATURE`. (R4 supplies the
  third as a measured baseline: 588 defects at exactly zero curvature.)
- **G4 — GAUGE SELF-TEST IN BOTH DIRECTIONS (§14, and the Branch-A disease).** A
  site-diagonal gauge action; Wilson traces invariant under it; a declared handle
  that moves the untraced holonomy at every checked loop. Holonomy enters any
  claim only as a conjugacy class. R4's projective-period self-test is the working
  template and should be cited as such.
- **G5 — DECLARATION SEGMENTS (from F1/F12).** The verdict must carry
  `CONNECTIVE`, `LINK-SET/STENCIL`, `SECTOR`, `SWEPT-RANGE` and
  `INDIVISIBILITY=DECLARED|MEASURED` as explicit segments; any quantity not gated
  invariant across the declared free axes is entered arena-relative or not at all.
  R4's SCALE segment is the cautionary case.
- **G6 — REFINEMENT (the charter's actual question).** The holonomy group at
  L = 4 versus the declared doubling to L = 8 (or R6a's move if it has landed);
  the **isomorphism class is the invariant**, the plaquette count is the extensive
  control. Success = a stable non-abelian isomorphism class under refinement;
  `NO-STABLE-GROUP` is first-class. Report where the group sits against CR-D's
  ladder (alternating 3-of-4, linear 0-of-4, ceiling attained) — that is the
  programme's existing group-family prior and the natural comparator.
- **G7 — THE SCRAMBLE CAVEAT, INHERITED.** Γ-main's finding that the q-reading's
  group is *not* a discriminating statistic must be pinned as a standing warning:
  R5 must show its holonomy group separates the physical case from a scrambled
  control before any group-theoretic claim is entered.

### What R5 must not do

No confinement-analog language before G1 passes. No silent inheritance of the
maximal-transport gate. No matrix-valued holonomy reported as physics. And no
claim that curvature implies quantum character — R4 measured 588 defects at
identically zero curvature, which settles that implication in the negative on
this stage.

---

## SUMMARY OF REPAIRS (in priority order)

1. Retitle: *"One Lattice Size Admits a **Local** Indivisible Family…"*; correct
   §9's bullet; carry the Householder counterexample as a disclosure (F3).
2. Fix the verdict's false biconditional → `ONLY-IF-L<=4;PRESENT-AT-L-IN-{2,4}`,
   derived in-gate from the ord census (F2).
3. Reclassify the connective as FORCED-by-anchored-link, carry it in the SCALE
   segment, add the routing mutant, correct §2's scope line (F1, F9).
4. Re-register `G-STATE-COEFFICIENT-BACKGROUND` as FORCED; rewrite §8 with the
   three state-coupling routes (F4).
5. Demote "indivisible" to "declared-indivisible" and carry it in SCOPE — or
   measure d_div and carry the number (F5).
6. Add the commutator census (0 of 3,364) and the principled-bite figure (36 of
   150) to §7; state that the excluded stratum is non-commuting (F6, F10).
7. Adopt the Moore-ball collapse theorem and the alphabet-independence argument;
   they close two declared scope holes and make the unit stronger (§K2).
8. Print the class-label collisions (22 classes, 14 labels) and the direction /
   chirality completion; retire "excitation-type" for "conjugacy type" (F7).
9. Re-register `G-CLASS-TRANSLATION-TRIVIAL` and §5.1's splitting identity as
   FORCED (F8, N3); print the state-motion probe count (N2).
10. Carry the ceiling disclosure on `SEPARATIONS=16` / `MAX-DEFECT-RADIUS=2`, and
    the observation that the unique scale is where the propagator cannot be
    resolved (K5).
11. Fix the pin/delivery artifact naming (N1).

---

## RECOMPUTATION LEDGER

| block | independent recomputation | result |
|---|---|---|
| locality | 48 rows (2 connectives × 3 dims × 8 sizes) | thresholds Moore 4/4/4, vN 4/2/2 — delivery's Moore rows reproduced |
| admissibility | 16 determinations | **[4] / [2,4]** — F1 |
| order census | 9 orders × 25³ = 140,625 coefficient triples, with a character cross-check at n \| 8 | all 27 delivered numbers reproduced |
| 5-point stencil, L=5 | 34,925 nodes | 121 leaves, 0 non-monomial — delivered numbers reproduced exactly |
| 5-point stencil, L=4 | 150,125 nodes | **160 non-monomial** (new, F11) |
| 9-point Moore stencil, L=5 | 23,465,025 nodes | 217 leaves, **0 non-monomial** (new, §K2) |
| pool | 9 axes × 25³ = 140,625 triples; 66 gauge orbits; 64 dense unitarity checks | 64 = 58 + 4 + 2, all orbits size 8, 0 unitarity failures |
| transport levels | 64 generators × (16 translations + 128 extended) | 1 NONE / 5 OCC / 0 OCC+AXIS / 58 FULL; level = kind for 62/64 (F10) |
| defect census | 4,096 ordered pairs, exact | 3,364 / 588 / 150 / 738 — reproduced |
| values | 588 nonzero rows | 8 values, all 8 multiplicities reproduced; 588/588 rational |
| column sums | 3,364 circulant rows | 0 violations |
| Markov | 1,792 / 2,304 pairs | 0 nonzero / 738 nonzero — reproduced |
| locality split | 576 / 1,188 pairs | 216 / 372, max radius 2 — reproduced |
| derivability | 6,728 predictor evaluations + 3,364 cancellation checks | **TP 588 / FP 0 / FN 0**, 0 cancellations (new, §K1) |
| classes | 64 × (128 + 32 + 16) conjugations | 22 / 38 / sizes {1,2,4} / 58 singletons — reproduced |
| labels | 22 classes × 3 label schemes | **14 distinct labels**; 17 with direction (new, F7) |
| periods | 22 classes × up to 16 powers | projective {1,2,4}, raw {2,4} — reproduced |
| dispersion | 58 × 16 character evaluations | **57/58 non-constant eigenphase** (new, §K2) |
| drift | 58 generators | **0 of 42 non-monomial drift; 12 of 16 monomial** (new, §K2) |
| state motion | 64 probe pairs × 18 states | 18/18 distinct at all 64; reconstruction exact at 64/64 (identity — F4) |
| Householder | 5 lattice sizes, all lags + defect | unitary and defect-carrying at every L (new, F3) |
| Q(i,√3) generator | full lag set + defect | unitary, drift −1/2, Δᴮ = ±3/8 (new, §K2) |
| commutators | 3,732 ordered pairs | **0 of 3,364 in the FULL stratum**; 4 of 16 among brickwork (new, F6) |
| exclusions | 150 excluded nonzero, by kind | 114 involve the scrambled control; 36 principled (new, F10) |

**Delivered quantities reproduced: 62. Discrepancies: 0. New measurements: 6.
New theorem: 1.** Total exact-field operations ≈ 2.40 × 10⁷.

---

## GRADE

**ACCEPT-WITH-FIXES.**

The instrument is sound and the arithmetic is clean — every delivered number I
could reach reproduced exactly, and the unit's hardest technical claim (the
collapse theorem) is not only correct but extends further than the unit knew. The
fixes are required because four claims exceed what was measured: a false
biconditional inside a gated verdict segment (F2), a title refuted by an exact
construction (F3), an arena-non-invariant quantity entered as the headline (F1),
and a linear-algebra identity offered as the answer to a successor requirement
(F4). All four repairs are local — a verdict-segment rewrite, a title, a choice-
inventory reclassification, and two FORCED re-registrations. None touches the
census, the head, or the instrument's architecture, and the corrected unit is
stronger than the delivered one: *local superposition has a unique admissible
scale on this stage; the defect is present there; the defect is present at every
other scale too, non-locally; and the stage's covariant sector is abelian,
momentum-blind and curvature-free* — which is precisely the fact R5 needs.

---

*Single-file confirmation: this review is the only repository write made by
reviewer R2 for unit R4. All hostile work — the independent reimplementation, the
stencil sweeps, the counterexample constructions and the commutator census — ran
in* `/private/tmp/claude-501/-Users-felixrobles-workspace/82d34949-326c-4269-8dd0-587362126fa5/scratchpad/r4eff/`. *No
delivery module was imported; no git write was made; all eight pinned hashes
re-verified unchanged after all work.*
