# U3 — result: **S-FAIL-DS, on every generated matrix that is square at all — and both passers are the flat matrix.** Seven of the eleven screened readings fail the doubly-stochastic precondition with exact imbalances (the `Ẑ` sibling's is `5/7` of one unit of mass); the two that pass are `J/2` and `J/8`, orthostochastic with real orthogonal certificates, so nothing committed and generated forces `i`. The K1 **outcome space** is of size `≤ 2` — *measured* at four committed pools, unproved beyond them — and at that size `i` is undecidable; the corpus **does** generate multiplicity-`3` conflicts, and they carry `2`-outcome laws. The `U(1)` loop-class theorem reproduces in one clause of three: the loop class is gauge-invariant and non-trivial, but every measured value is a positive real and `ℝ⁺ ∩ U(1) = {1}`. The v7 amplitude form is carriable on the gauge stratum and is carried by the identity.

**Read the scope before the headline.** This unit screens **matrices**.
A matrix that passes the screen is not thereby a quantum system, a
Hilbert space, or a dynamics: the map from a screened `Γ` to a physical
system is missing and this unit does not supply it. Correspondence is
not identity. The screen is also **closed and undilated**: `[B3]` calls a
quantum system *"either a unistochastic process itself, or (if a
nontrivial dilation was required) a subsystem of a unistochastic
process"*, and only the first disjunct is decided here. No CP statement,
no Bell statement, no locality statement, no covariance claim appears
anywhere in the receipt; L-1's bound stands untouched.

**Status: GREEN-UNREVIEWED-REPAIRED, STRICT, 2026-07-28.** Pin
`v11/note-u3-unistochasticity-screen-pin.md` (binding, frozen before any
code was written). Binding specification: paper 0 §7 (U3), §5 (the gauge
stratum), §6; `[V11-CAT]` §7 rank 4 and its §4.3 / §4.6 / §4.7 graded
entries; U1 §11's handover and §6's sharpening. Parents: v10 **paper 31
§4.3** (the K1 arbitration operators), the **D75 Barandes audit** pin (b)
(the `Ẑ` sibling's specification and the screen's shape), **D74 TERMINAL**
(the transport loop census, group `⟨2,3⟩`, `R⁺`, odd sector empty), **LD**
(the walled odd sector), **v6 paper 7** Thms 7.1 and D3 (the `U(1)`
loop-class theorem), **v7 paper 30** (the `i`-twist amplitude form), and
`[B3]` (*Quantum Systems as Indivisible Stochastic Processes*,
arXiv:2507.21192 — the unistochasticity criterion, the dilation clause,
and the Schur-Hadamard gauge).
Receipt `v11/code/u3_unistochasticity_screen_exact.py`, output
`v11/code/u3_output.txt` — run from the repository root, **exit 0**,
**50 PASS / 0 FAIL / 0 ANCHOR-FAIL** of which **6 carry no independent
information and are labelled as such** (**44 independent-evidence
passes**), **15 s** wall clock against the pin's ~25 min budget. Re-run
at `PYTHONHASHSEED=7`: **output identical apart from timings** (7
timing lines differ, 0 substantive).

**Lean: NONE**, as the pin declares. `S-PASS`, `S-FAIL-DS` and
`S-FAIL-UNI` are all reportable, and the census is the result.

**Exact arithmetic end to end, and no tolerance anywhere.** Rationals are
`fractions.Fraction`; real algebraic quantities live in the `Q`-span of
`√d` for squarefree `d`, with an exact sign oracle by rational interval
refinement (`16` of the printed `4096`-bit cap actually used); complex
algebraic quantities live in `Q(ζ₈)` and `Q(ζ₁₂)`, implemented as
`Q[x]/Φ_N(x)` with `Φ₈` and `Φ₁₂` verified in-receipt to have degree
`φ(N)` and to divide `x^N − 1` with remainder exactly zero. `1/√8` and
`1/√3` are exact elements of those fields, so the DFT certificates are
algebraic objects and not approximations.

## 1. The verdict

`[B3]`'s criterion is `Γ_ij = |U_ij|²` for one unitary `U` **of the same
size**, with no ancilla and no ancilla sum. Theorem D1 — the
ancilla-summed Stinespring/Naimark dilation every stochastic matrix
admits — is set aside throughout, as `[V11-CAT]` §7 rank 4 requires.

- **The census is mixed and the census is the result.** Of eleven
  readings: `2` are non-square and unscreenable, `7` fail the
  doubly-stochastic precondition, `0` reach the `S-FAIL-UNI` cell, `2`
  pass with an exhibited unitary, and `0` are `EXCLUDED-BY-CAP`. The
  eleven are **not** eleven independent matrices: they are `4` distinct
  committed generated matrices, `5` constructed or convention-relative
  readings of those, `1` transpose duplicate and `1` by-specification
  control (§3).
- **Every generated object that would have had to be argued at the phase
  level is already excluded at the mass level.** The screen never gets to
  a phase question on a committed matrix, because the mass question
  answers first.
- **Both passers are the flat matrix, and they pass for one reason.**
  `K1-2CONF` is `[[1/2,1/2],[1/2,1/2]] = J/2` and `ARMC2-8x8` is `J/8`.
  Each is column-constant, and by the lemma L1 the only doubly-stochastic
  column-constant law is the uniform one — which is `J/n`, unistochastic
  at every `n` (the DFT) and orthostochastic at every `n = 2^k`
  (Sylvester). Both certificates are real orthogonal and verified entry
  by entry. The ortho/uni gap, which the D75 audit identifies as the
  exact place the necessity of `i` lives, is **empty on this census**,
  and **the passes carry no quantum content**.
- **The K1 outcome space is of size `≤ 2` — measured, not proved.** The
  corpus **does** commit multiplicity-`3` conflicts: the committed
  `(A,B,C)` pool's `3,424` histories carry `216` of them, the shallowest
  at depth `3`. What bounds the screen is not the conflict's size but the
  **size of the K1 law's outcome space**, which is the number of maximal
  independent sets of the realised conflict graph — and that is `≤ 2` at
  every one of four committed pools, three gated in-receipt and the
  fourth round-verified (§4). At size `≤ 2` the
  necessity of `i` is undecidable, and deciding it requires a
  `≥ 3`-outcome K1 law: **a fact about the actor pool and the value
  alphabet, not about structure and not about depth.**
- **The loop-class theorem reproduces in one clause of three**, and the
  obstruction to the other two is exact and structural rather than a
  failure to find (§6).
- **The v7 amplitude form is carriable and carried trivially** (§7).

## 2. The instrument, and what it can and cannot decide

**The precondition.** A unitary has orthonormal rows *and* orthonormal
columns, so unistochastic `⟹` doubly stochastic. The precondition is
run in exact rationals, on both conventions: `[B3]`'s `Γ` is
column-stochastic (`Σ_i Γ_ij = 1`, eqs. 9/24/26) and the corpus's
generated `Ẑ` is row-stochastic. Double stochasticity is exactly the
statement that the choice does not matter, and on the sibling it does.

**`n = 2`.** Constructed, not cited: for `B = [[p, 1−p], [1−p, p]]` the
real matrix `[[√p, √(1−p)], [√(1−p), −√p]]` is exactly orthogonal in the
`√` ring and its modulus-squares are `B`. The construction is uniform in
`p`, so every `2×2` bistochastic matrix is **orthostochastic**.

**`n = 3`.** The triangle (chain-link) criterion, stated and cited to
Au-Yeung–Poon (1979), Nakazato (1996) and Bengtsson–Ericsson–Kuś–Tadej–
Życzkowski, *Commun. Math. Phys.* **259** (2005) 307–324; the corpus's
own floating-point implementation is
`v8/code/f6_unistochastic_record_blind_probe.py:224-246`, run on textbook
fixtures only at `v8/code/p18_seal_divisibility.py:318-362`. It is
implemented here as one **exact rational discriminant**
`T = 2(ab+bc+ca) − a² − b² − c²` on the squared phasor moduli — `T ≥ 0`
iff the triangle closes, and `T` is `16 ×` the Heron area squared.

**The criterion's own well-definedness is proved here, not assumed.**
The criterion is stated for one column pair. That is legitimate only if
the discriminant is pair-independent. `T` has degree at most `4` in each
of the four free entries of a bistochastic `3×3`, so agreement on a
product grid with `5` distinct values per variable forces identity: all
six discriminants — three column pairs and three row pairs — agree at
every one of the `5⁴ = 625` grid points, **`0` mismatches**. "The"
triangle discriminant is well defined.

**Every `n`.** The polygon obstruction: if `Γ = |U|²` then for each pair
of distinct columns the `n` numbers `conj(U_ip) U_iq`, of moduli
`√(Γ_ip Γ_iq)`, sum to zero, so no modulus may exceed the sum of the
others. **Necessity holds at every `n` and requires no
bistochasticity** — it decides `S-FAIL` outright on a matrix that has
already failed DS, giving second, independent certificates. It is
decided exactly by the `√`-ring sign oracle.

**The asymmetry is deliberate.** The negative direction is elementary and
is not taken on citation. The positive direction **never** rests on the
criterion: every `S-PASS` in this receipt exhibits a unitary of the same
size and verifies `U†U = I` and `|U_ij|² = Γ_ij` entry by entry in exact
algebraic arithmetic. The cited `n = 3` sufficiency is therefore never
load-bearing. A matrix with no obstruction *and* no certificate would be
reported `EXCLUDED-BY-CAP`; that cell is empty.

**The known-answer controls, run before the instrument is pointed at
anything generated.**

| control | source | required answer | returned |
|---|---|---|---|
| `KA-1` flat `J/3` | the `3`-point DFT; Bengtsson et al. | **UNISTOCHASTIC** | `T = +1/27`, `0` polygon violations, and the DFT exhibited in `Q(ζ₁₂)`: `0` unitarity residuals, `0` modulus mismatches |
| `KA-2` `B = (1/2)(J − I)` | the canonical counterexample; the corpus's own print at `p18_…:346-347` | **BISTOCHASTIC, NOT UNISTOCHASTIC** | DS holds; `T = −1/16`; the polygon fires — moduli `(0, 0, 1/2)` and `1/2 > 0 + 0` |
| `KA-3` `J/3` is **not** orthostochastic | the parity argument, exhaustive | the ortho/uni gap is real | all eight sign patterns give an odd numerator; never `0` |
| `KA-4` `n = 2` | constructed | orthostochastic | `0` residuals, `0` mismatches |
| `KA-5` a row-stochastic non-DS matrix | constructed | caught by the precondition | caught, with the exact per-column excess |
| `KA-6` Sylvester `H₈` | Sylvester (1867) | `H Hᵀ = 8I` | exact over `Z`, all `64` inner products |

`KA-3` matters: it exhibits the one canonical matrix on which the complex
numbers *are* forced, so the orthostochasticity question asked of the
passers in §4 is not vacuous.

## 3. Arm A — the screen census

| matrix | shape | verdict | the exact datum |
|---|---|---|---|
| `K1-BORN-COL-PAIR` | `4×1` | **N/A-SHAPE** | the criterion is undefined at this shape; the trivial column completion is D1's move and is set aside |
| `K1-BORN-COL-SINGLE` | `2×1` | **N/A-SHAPE** | same |
| **`K1-2CONF`** | `2×2` | **S-PASS (FLAT `J/2` — degenerate)** | `[[1/2,1/2],[1/2,1/2]]`; real orthogonal certificate, `0` residuals, `0` mismatches |
| `K1-PAIR-FULLIDX` | `4×4` | **S-FAIL-DS** | column sums `2, 0, 0, 2`; `Σ|·| = 4` |
| `K1-SINGLE-2x2` | `2×2` | **S-FAIL-DS** | column sums `2, 0`; `Σ|·| = 2` |
| `K1-JOIN-MENU` | `3×3` | **S-FAIL-DS** | column sums `3/2, 3/4, 3/4`; `Σ|·| = 1` |
| **`K1-3CONF`** | `2×2` | **S-FAIL-DS** | the committed K1 law on the first generated **multiplicity-`3`** conflict, on its own `2`-element outcome space: `[[2/3,1/3],[2/3,1/3]]`, column sums `4/3, 2/3`, `Σ|·| = 2/3`; **and** the polygon obstruction fires on the row pair (moduli `2/3 > 1/3`, slack `−1/3`) |
| **`ZHAT-6x6`** | `6×6` | **S-FAIL-DS** | column sums `25/28, 1, 59/64, 55/64, 31/32, 19/14`; deficits `−3/28, 0, −5/64, −9/64, −1/32, +5/14`; `Σ|·| = 5/7` |
| `ZHAT-6x6-TRANSPOSED` | `6×6` | **S-FAIL-DS** | the same imbalance, on the rows: `[B3]`'s convention does not rescue it |
| `ZHAT-CLOSED-3x3` | `3×3` | **S-FAIL-DS** | column sums `7/8, 7/8, 5/4`, `Σ|·| = 1/2`; **and** `T = −1/4096 < 0` |
| **`ARMC2-8x8`** | `8×8` | **S-PASS (FLAT `J/8` — degenerate)** | real orthogonal certificate (Sylvester `H₈/√8`), `0` residuals, `0` mismatches; the complex DFT certificate is exhibited too |

**Eleven readings, recomposed honestly.** They are `4` distinct
committed generated matrices — `K1-2CONF`, `K1-3CONF`, `ZHAT-6x6` and its
closed `3×3` sub-block — plus `5` constructed or convention-relative
readings of those (the two Born columns, the two untrimmed-index rows,
the normalised join menu), `1` transpose duplicate (`ZHAT-6x6-TRANSPOSED`)
and `1` by-specification control (`ARMC2-8x8`). Eleven rows are not
eleven pieces of evidence.

**The readings are declared, and the convention-relative ones are marked
as such.** `V_single` and `V_pair` are isometries with **one column**
(`2×1` and `4×1`), rebuilt here from U1's own `Q(√2)` arithmetic lifted
by AST, with the isometry defect exactly `0` and Born `= K1` recomputed
from the committed `d42b3` layer. Barandes' criterion is a statement
about a square `Γ` against a square unitary, so the operators themselves
are not screenable objects: what is screenable is the induced `Γ`, and
`K1-2CONF` is the only reading in which the K1 layer's `Γ` is square on
the **realised support at both ends** — it replicates a source-
independent branch law over the conflict's own two-token source index,
and both ends are realised. Every other square K1 reading needs an
untrimmed index. `K1-PAIR-FULLIDX` and `K1-SINGLE-2x2` are those readings
whose failure is a support mismatch and not a mass defect of the law;
they are reported because the pin asks for the row and transfer readings
both, and they are labelled convention-relative in the receipt.
`K1-JOIN-MENU` is a declared reading, and it exists to put the
column-constant lemma against a **non-uniform** generated row.

**The `Ẑ` sibling — the pin's flagged threat — is rebuilt, not quoted.**
The closed-scope `d42b3` family to depth `6` reproduces d43b's census
`[1,7,39,215,1191,6471,34375]`; the uniform-lookahead partition
stabilises at six states at lookahead `2`; the exact `6×6` transfer is
well-defined on all `215` depth-`≤3` members with row sums
`(2,2,2,5/2,2,2)`; `T f = 2 f` exactly; and the completion
`Ẑ(i→j) = T_ij f_j/(λ f_i)` has every row summing to `1`, the conflict
row exactly `{0: 1/7, 3: 3/4, 5: 3/28}`, and the column sums the audit
specified. **The `19/14` disqualifies it, exactly, and the exact
imbalance is the headline.**

**The audit's `[MY READING]` is confirmed and sharpened.** D75 §5.3
reasoned that unistochastic `⟹` doubly stochastic `⟹` uniform stationary
law for an irreducible chain, and predicted that a chain with this
structure would not have one. It is worse than predicted: the chain is
**not irreducible**. States `{2,4,5}` form the unique closed
communicating class and states `{0,1,3}` — **including the conflict state
`3`** — are transient. The unique stationary law is exactly
`(0, 0, 1/4, 0, 1/4, 1/2)`: three of six entries are exactly zero, so it
is not merely non-uniform but singular with respect to the uniform law.
A doubly-stochastic matrix always has the uniform law stationary, so
this is a **second exact certificate**, independent of the column sums.

**The one generated `3×3` matrix in the corpus fails the screen twice
over.** The closed class `{2,4,5}` is a genuine generated `3×3`
stochastic matrix. Its columns sum to `7/8, 7/8, 5/4` and its unitarity
triangle has `T = −1/4096 < 0`. The triangle's necessity does not
require bistochasticity, so the second obstruction is not a corollary of
the first: even a mass repair that fixed the column sums would have to
move a phasor modulus as well.

**The degenerate control passes, and the lemma explains why.** ARM-C2's
matrix is taken **by specification** from U1's committed receipt (§5.5:
the renewal chain is i.i.d. uniform on `8` labels and `Γ(r2←r1)` is
column-constant with every entry `1/8`) and is not re-derived here, U3
being a file-disjoint parallel unit. The verdict is made independent of
that quote by a theorem: **an `n×n` matrix all of whose rows equal one
probability vector `v` is doubly stochastic if and only if `v` is
uniform** — its column sums are `n·v_j`, and `n·v_j = 1` for every `j`
iff `v_j = 1/n`. Verified on `30` constructed column-constant matrices at
six sizes. **Among column-constant generated transfers the only
doubly-stochastic one is the maximally forgetful one**, which is why
ARM-C2 passes and `K1-JOIN-MENU`, with row `(1/2, 1/4, 1/4)`, does not.

## 4. The two structural verdicts, and the multiplicity census behind the second

**The ortho/uni gap is empty on this census, and both passers are flat.**
Both carry a real orthogonal certificate, exhibited and verified, and
both are `J/n`. A matrix that is unistochastic but **not**
orthostochastic is one that cannot be lifted with real amplitudes — the
`i` is forced by the matrix's own entries — and this census contains no
such matrix. `KA-3` shows the property is not vacuous: `J/3` is exactly
such a matrix, and nothing committed and generated resembles it.

**The multiplicity census, measured on the committed pools.** Paper 31
§4.3's `{1, 2}` is a line about a **fixture**, and its own Scope sentence
says so: *"Scope: the pair-plus-path fixture, grammar = the terminal
admission layer plus the click refinement; realized component sizes at
the two cuts are exactly `{1, 2}` and the constructed family covers
precisely those."* A two-actor fixture bounds a fixture. The corpus's
**three**-actor pool is committed (`v10/code/d42b1_transport_exact.py`,
declared at `:435`), and it is enumerated and censused here:

| pool | histories | admissible arbitration events, by `\|ckey\|` | by `\|MIS\|` |
|---|---|---|---|
| `d42b1` `(A,B,C)` `d ≤ 3` | `3,424` | `{1: 3096, 2: 1536, 3: 216}` | `{1: 3096, 2: 1752}` |
| `d42b1` `(A,B)` `d ≤ 4` | `3,969` | `{1: 3468, 2: 1264}` | `{1: 3468, 2: 1264}` |
| `d42b3` closed scope `(A,B)` `d ≤ 6` | `34,375` | `{1: 35412, 2: 8944}` | `{1: 35412, 2: 8944}` |

**Multiplicity `3` is committed.** `216` admissible arbitration events on
`36` distinct histories, the shallowest at depth `3`:
`[('p','A',v0,0), ('p','B',v0,0), ('p','C',v0,1)]`, with committed menu
weights `1/6` and `1/12` and committed K1 law `{A0,B0} → 2/3`,
`{C1} → 1/3`. The menu and the law are locked together by the layer's
own pricing — the menu weight is exactly `1/4 · PK1(winner)` at a single
available component. **The claim that "the corpus has committed none"
was a fixture-scope reading of a two-actor Scope line, and it is
withdrawn wherever it appeared.**

**But the outcome space is `2`, not `3`.** A conflict component of size
`m` does **not** give an `m × m` `Γ`. The K1 law is supported on the
**maximal independent sets** of the realised conflict graph — the layer's
own `mis_of`, and `admissible()` refuses every `wkey` outside it — so the
square `Γ` the screen sees has size `|MIS|`. On the witness the conflict
graph is `A0 — C1` and `B0 — C1` and **not** `A0 — B0`, because `A` and
`B` propose the same value; its maximal independent sets are `{A0,B0}`
and `{C1}`, exactly two.

**And `|MIS| ≤ 2` at every pool measured.** Across all three pools above
the `|MIS|` census never leaves `{1, 2}`, on every admissible arbitration
event. The **measured mechanism**: the realised conflict graph on every
component is exactly the complete multipartite graph whose parts are the
proposal-**value** classes (edge iff the two proposals differ in value —
`0` exceptions over all three pools, and `|MIS|` equals the number of
value classes on every event), and the committed proposal alphabet is
**binary**, so there are at most two parts. The round's fourth pool —
`(A,B,C,D)` at `d ≤ 4`, `332,697` histories, `|MIS|` census
`{1: 232264, 2: 98304}`, never `3` — **agrees, and is carried as
round-verified evidence, not as a gate of this receipt.**

**The no-go, restated honestly.** **The K1 outcome space is `≤ 2` —
measured at the four committed pools, unproved beyond them.** By lemma
L1 the only column-constant `2`-outcome law that is doubly stochastic at
all is the uniform one, and every `2×2` bistochastic matrix is
orthostochastic (constructed and re-verified across a printed sweep of
the branch weight), `1×1` trivially so. **So `i` is undecidable at these
pools.** Deciding `i` requires a `≥ 3`-outcome K1 law, which needs
**non-binary proposal values or non-complete-multipartite conflict
graphs** — a **CAP** fact about the actor pool and the value alphabet,
not a structure fact, and not a fact about depth.

**The one substantive non-flat K1 object fails at the mass level.** Read
as the square transfer on its own two-element outcome space, the
multiplicity-`3` law is column-constant with row `(2/3, 1/3)`; its column
sums are `(4/3, 2/3)` and by L1 it is not doubly stochastic. The exact
price is `2/3`, and the polygon obstruction fires independently on the
row pair. So the first genuinely non-degenerate generated K1 matrix gets
the same verdict as every other substantive generated transfer.

## 5. The price of enrichment

For every doubly-stochastic `D`, `‖M − D‖₁ ≥ Σ_j |c_j(M) − 1|`, because
`Σ_j |c_j(M) − c_j(D)| ≤ Σ_ij |M_ij − D_ij|` and `c_j(D) = 1`. Here
`‖·‖₁` is the **entrywise** sum `Σ_ij |M_ij − D_ij|`, not an operator
norm. The exact prices:

| matrix | mass that must move, at least | out of a total mass of |
|---|---|---|
| `ZHAT-6x6` | `5/7` | `6` |
| `ZHAT-CLOSED-3x3` | `1/2`, **and** a phasor modulus, since `T = −1/4096` | `3` |
| `K1-JOIN-MENU` | `1` | `3` |
| `K1-3CONF` | `2/3` | `2` |

**These are absolute quantities, in units of probability mass.** A
row-stochastic `n×n` matrix carries total mass `n`, so `Ẑ`'s `5/7` is
five sevenths of **one** unit out of six — it is not five sevenths of the
matrix. **And this is a mass statement, not a phase statement.** No
amount of phase freedom repairs a column sum. Whatever a quantum-eligible
completion of the record chain is, it must move that much probability
mass before any question about `i` is even posable.

## 6. Arm B — the loop-class reproduction

**The theorem, located.** `v6/relativistic-isp-v6-paper7.md:612-618`
(Theorem 7.1, the canonical phase group) and `:676-689` (Theorem D3, loop
phases are the retained holonomy). `[V11-CAT]` §4.3(c)'s corrections
travel with the citation: the standing is contested and unresolved at
four documents, and Thm D1 is not the unistochasticity answer.

**The carrier is D74's, and it re-anchors exactly.** `AB4`: `3,969`
histories, `1,546` closed squares, `88` non-unit with spectrum
`{1/2: 70, 2/3: 2, 3/2: 6, 2: 10}`, `40` half-open (`28` AB-only, `12`
BA-only), `142` both-blocked. `ABC3`: `3,424` histories, `1,554` closed,
`12` non-unit. The carrier: `113` menu classes and `185` congruence
classes at `AB4`, both closing `44` of the `88`; `117 / 162` at `ABC3`,
both closing `0` of `12`. **The `88 / 40 / 12` census is reproduced to
the unit**, and `exit 1` is reserved for these gates and is not reached.

D3 has three separable clauses and each is tested on its own.

- **Clause (i) — the loop class is gauge-invariant: REPRODUCED.**
  Applying the printed non-constant vertex potential
  `φ(node_i) = (i+1)/(i+3)` over all `81` carrier nodes and regauging
  every edge by `q' = q·φ(target)/φ(source)` leaves the entire self-loop
  holonomy spectrum unchanged, value for value and count for count. The
  gate is an identity of its own definitions and is labelled as carrying
  no independent information; what carries the clause is the measured
  fact that **the loop class is non-trivial at all** — `44` non-unit
  self-loops at `AB4` with spectrum `{1/2: 26, 2: 10, 2/3: 2, 3/2: 6}`,
  and `44` non-trivial independent cycles out of `134`.
- **Clause (ii) — Theorem 7.1's conclusion, that the loop class is
  `U(1)`-valued: NOT REPRODUCED, and the obstruction is structural.**
  Every non-unit holonomy measured on either arm — raw squares, carrier
  self-loops and independent carrier cycles alike — lies in
  `{1/2, 2/3, 3/2, 2}`, and the group they generate is `⟨2,3⟩`, free
  abelian of rank `2`, index `1` in `Z²`. **The reason the intersection
  with `U(1)` is trivial is positivity, not torsion-freeness:** every
  element of `⟨2,3⟩` is a positive real, and `ℝ⁺ ∩ U(1) = {1}`.
  Torsion-freeness would not do it — `⟨e^{2πi√2}⟩` is torsion-free and
  sits *inside* `U(1)` — and the appeal to it is withdrawn. Freeness of
  rank `2` is retained for what it does establish, which is the size of
  the character group below. Every measured holonomy has unimodular part
  exactly `1`, and no root of unity other than `1` occurs. **There is no
  `U(1)` content to find at any depth, for a reason that is a property of
  the value set and not of the window.**
  **And the object tested is not the object `D3` is about.** `D3`'s
  `B(ℓ)` is a product of entries of **Theorem D1's dilating unitary** —
  the construction this unit sets aside at its first line. What is
  measured here is a ratio of committed **menu weights**, positive
  rationals by construction, which could never have landed in `U(1)`.
  Clause (ii)'s non-reproduction is therefore **partly an artifact of
  refusing `D1`'s hypothesis**, and the substantive content of this arm
  is what survives that concession: the positivity obstruction on the
  generated value set, and the unselected `T²` below.
- **Clause (iii) — interference is the loop-phase law: DEGENERATE, as a
  corollary of clause (ii) and not as a second measurement.**
  `P = |A|² + |B|² + 2|A||B| cos(arg B(loop))` requires the cosine to
  range over `[−1, 1]`. On this carrier `arg B(loop) = 0` at every
  measured loop, so the exact range of the cosine is the single point
  `{1}`, the cross term sits at its **maximum**, no cancellation is
  available anywhere, and the law collapses to `P = (|A| + |B|)²` — the
  classical no-interference sum. The gate that records this carries **no
  independent information** and is labelled so: the cosine set is read
  off positivity, and `1 + 1 + 2 = (1 + 1)²` cannot fail.

**This confirms D74's a-priori settlement; it does not sharpen it.**
D74's committed note already settles the scalar odd sector *before any
fixture is run*: gate `D2` states that every committed weight is a
positive rational, that *"the only positive rational of modulus `1` is
`1`"*, and that this *"settles the scalar odd sector a priori, in one
line, before any fixture is run"*
(`v10/note-d74-transport-holonomy-result.md:248`, and `:107-109`). What
this unit adds is **confirmation on a different object** — the loop class
of the carrier, its self-loops and independent cycles, rather than the
raw square holonomies — together with the priced residue below.

**The residue, priced exactly.** `⟨2,3⟩` is free of rank `2`, so
`Hom(⟨2,3⟩, U(1)) = U(1)²`: a character is fixed by its values on the two
free generators `2` and `3`, chosen independently. **D3's `U(1)` loop
class is attachable to the generated carrier in a `2`-real-parameter
family, and the generated data selects no point of it** — the trivial
character is the only one anything committed picks out. The price of the
reproduction is two real numbers, unsourced.

## 7. Arm C — the gauge candidate

**`[B3]`'s gauge, quoted at eqs. (29)/(30) and after (64):** entrywise
phases `Θ_ij ↦ Θ_ij e^{iθ_ij}` are a genuine gauge invariance; **and**
*"a unitary time-evolution operator `U(t←0)` will not generically remain
unitary under arbitrary Schur-Hadamard gauge transformations (30)"*, so
writing a unistochastic `Γ` in terms of a unitary is a **partial fixing**
of that freedom.

- **The action on `Γ` is an identity, and is gated as one.** Attaching
  the printed non-separable phase matrix `θ_ij = ζ₈^{i·j² + 3i}` to the
  `8×8` passer's certificate leaves `|U_ij|² = 1/8` at all `64` entries
  exactly. This is eq. (28) read as a definition; the gate cannot fail as
  posed and is excluded from the evidence count. **Attaching phases
  entrywise is not a test of anything.**
- **The unitarity-preserving subgroup is proper.** The separable gauge
  `θ_ij = α_i + β_j` (printed: `α_i = 2i`, `β_j = 3j` in units of `2π/8`)
  preserves unitarity exactly — `0` residual entries. A single
  non-separable element — flipping the sign of the `(0,0)` entry alone, a
  legitimate Schur-Hadamard transformation with `θ₀₀ = π` — leaves `Γ`
  **exactly** invariant and destroys unitarity, with `14` non-zero
  entries in `U†U − I`. **`Γ`-invariance and unitarity-preservation are
  genuinely different conditions, and "the phase is gauge" does not mean
  "any phase will do."** **Scope, plainly:** this is a sign flip on the
  textbook `DFT₈` attached to a **by-specification flat** matrix.
  **Nothing generated enters it.** It gates Barandes' clause; it does not
  gate it on generated data.
- **The odd channel is empty where the holonomy lives, measured here.**
  Over every linear extension of the **opposite poset** of every one of
  `AB4`'s `176` defective-square endpoints — `304` of them — not one
  reversed record is admissible. D74's committed `0 of 304` is
  reproduced, both numbers.
- **No committed generated quantity selects a non-trivial phase — `0` of
  `4` candidate carriers.** The transport holonomy `r` is `R⁺`-valued
  with no unimodular content, and traversal reversal acts on it by
  `r ↦ 1/r`, an even-channel action on `log r`. `J` is reversal-**even**
  by construction. The odd-ring port-flip parity class is label-holonomy,
  which free relabelling trivialises, and `[V11-CAT]` §4.7(c) forbids
  citing it for `Φ(O)`. The reversed record itself is refused at
  admission on `662/662` holonomy-carrying loops, on the Born `= K1` row,
  and on all `40` half-open squares.
- **Verdict: the v7 form is carriable, and it is carried by the
  identity.** With `Φ(O)` empty, `A(R) ~ e^{−K(E)}·e^{iΦ(O)}` reduces to
  a real positive amplitude times `e^{i·0} = 1`. The identity preserves
  both `Γ` and unitarity, so the form is **consistent** with `[B3]`'s
  gauge structure on both passers. It is consistent and empty:
  consistency at the identity is not evidence that the stratum is
  occupied.

**What a non-trivial occupation would cost is now stated exactly:** two
real parameters at the loop-class level (§6), and at the lift level a
choice inside the unitarity-preserving subgroup rather than the full
entrywise group. Neither is supplied by anything generated.

## 8. What this does and does not say

- **It is a matrix screen and nothing else.** No claim is made that a
  passing matrix is a quantum system. The map from a screened `Γ` to a
  physical system is missing, and correspondence is not identity.
- **The two passers pass for one degenerate reason, and it is the same
  reason.** `K1-2CONF` is `J/2` and `ARMC2-8x8` is `J/8`. Both are
  column-constant, so by lemma L1 each is doubly stochastic **only
  because** its row is uniform — and the uniform column-constant law is
  `J/n`, which is unistochastic at every `n` and orthostochastic at every
  `n = 2^k`. **The pass carries no quantum content whatever.** The census
  therefore **cannot** decide the four-way contest over v6 paper 7's
  `C`-derivation in the positive direction; it decides it in the negative
  direction, for these objects, and it leaves `i` undecidable at the four
  committed pools whose outcome spaces are measured (§4).
- **No indivisibility claim is made or used.** `[B3]`'s criterion is
  unistochasticity; indivisibility is U1's axis and is not crossed here.
- **No CP statement of any kind. No Bell or locality statement of any
  kind.** No covariance claim: L-1's bound stands untouched, and nothing
  here is a law at renewal grain.
- **Theorem D1 is set aside**, per the audit's guard and the catalog's
  instruction, and no positive verdict uses a dilation.
- **The `n = 3` sufficiency is cited and is never load-bearing**, because
  no positive verdict in this receipt is returned without an exhibited,
  verified certificate.
- **`0` verdicts are `EXCLUDED-BY-CAP`.** The instrument decided every
  object it was given.

## 9. Scope

The committed matrices only, at their own scopes: the K1 arbitration
family at paper 31 §4.3's **pair-plus-path fixture** (realised component
sizes `{1,2}` — a fixture line, not a bound on the grammar), **together
with** the committed three-actor pool, whose conflicts reach multiplicity
`3`; the `Ẑ` sibling on the closed-scope `d42b3` family to depth `6`; the
D74 anchor arms at `(A,B)` depth `≤ 4` and `(A,B,C)` depth `≤ 3`. **The
outcome-space bound `|MIS| ≤ 2` is measured** on three pools in-receipt
and on a fourth in the round; it is **not proved** for the grammar, and
no claim is made that it survives a wider actor pool or a non-binary
value alphabet. **The screen is closed and undilated:** `[B3]` allows a
quantum system to be *"either a unistochastic process itself, or (if a
nontrivial dilation was required) a subsystem of a unistochastic
process"*, and every `S-FAIL` verdict here leaves the second disjunct
untouched. ARM-C2's `8×8` matrix is taken **by specification** from U1's
committed receipt and is not re-derived, the verdict being made
independent of the quote by the column-constant lemma. Unistochasticity
is decided constructively at sizes `1, 2, 3, 6, 8`; the general-`n`
instrument is the exact polygon obstruction plus explicit certificate
construction, and **full phase-elimination (resultants / Gröbner) for
`n > 3` is not implemented** — a matrix with no obstruction and no
certificate would be `EXCLUDED-BY-CAP`, and that cell is empty. The
`√`-ring sign oracle's refinement cap is `4096` binary digits, of which
`16` are used. Determinism: every printed census is ordered by a
hash-seed-independent key, and the `PYTHONHASHSEED=7` re-run is
byte-identical apart from timings.

## 10. Handover, and the declared follow-ups

- **To U2 and to any weld:** the corpus owns **no closed, undilated
  quantum-eligible generated matrix**. The two `S-PASS` objects are the
  flat matrix; every substantive generated transfer fails at the mass
  level. The qualifier is `[B3]`'s own: a quantum system is *"either a
  unistochastic process itself, or (if a nontrivial dilation was
  required) a subsystem of a unistochastic process"* — this unit screens
  the first disjunct and says nothing about the second. Any weld that
  wants a closed quantum object must first supply the mass named in §5.
- **To U1b:** by the column-constant lemma, the only way a
  renewal-to-renewal transfer can pass the doubly-stochastic
  precondition is by being **uniform** — which is exactly the degenerate
  case ARM-C2 already occupies. A biting (non-column-constant) renewal
  transfer is screenable and is a **declared follow-up** of this unit,
  not a claim of it.
- **Named but not screened, and owed forward:** the `36`-state `σ` chain
  (`v10/note-d61-…:40`, `36` classes, `176` transition keys) and the
  transport-scope descent quotient of D74 read as a transition matrix.
  Both are on the D75 audit's candidate list at §5.3 and neither is on
  this pin's list.
- **To paper 0 §5 (the gauge stratum):** the stratum is **carriable and
  unoccupied**, and its non-trivial part is priced — a `2`-torus at the
  loop-class level, and a proper subgroup condition at the lift level.
- **The one thing that would change the answer:** a generated K1 law with
  **three or more outcomes** — that is, `≥ 3` maximal independent sets in
  a realised conflict — whose transfer is doubly stochastic. Multiplicity
  `≥ 3` is not enough and is already committed (§4): what is needed is
  **non-binary proposal values or a conflict graph that is not complete
  multipartite**, which is a fact about the actor pool and the value
  alphabet. Until such a law exists, `i` is undecidable at the four
  committed pools measured here, and §4 says exactly why — and says
  exactly how far the measurement reaches.
