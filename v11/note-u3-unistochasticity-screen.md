# U3 — result: **S-FAIL-DS, on every generated matrix that is square at all — and the ortho/uni gap is EMPTY.** Six of the ten committed readings fail the doubly-stochastic precondition with exact imbalances (the `Ẑ` sibling's is `5/7`); the two that pass are *orthostochastic*, exhibited with real orthogonal certificates, so nothing committed and generated forces `i`. The K1 arbitration layer **cannot ever** force it at its committed scope, because its conflicts have multiplicity at most `2`. The `U(1)` loop-class theorem reproduces in one clause of three: the loop class is gauge-invariant and non-trivial, but it is valued in `⟨2,3⟩`, which is torsion-free, so `⟨2,3⟩ ∩ U(1) = {1}` and the interference law collapses to the classical sum. The v7 amplitude form is carriable on the gauge stratum and is carried by the identity.

**Read the scope before the headline.** This unit screens **matrices**.
A matrix that passes the screen is not thereby a quantum system, a
Hilbert space, or a dynamics: the map from a screened `Γ` to a physical
system is missing and this unit does not supply it. Correspondence is
not identity. No CP statement, no Bell statement, no locality statement,
no covariance claim appears anywhere in the receipt; L-1's bound stands
untouched.

**Status: GREEN-UNREVIEWED, STRICT, 2026-07-28.** Pin
`v11/note-u3-unistochasticity-screen-pin.md` (binding, frozen before any
code was written). Binding specification: paper 0 §7 (U3), §5 (the gauge
stratum), §6; `[V11-CAT]` §7 rank 4 and its §4.3 / §4.6 / §4.7 graded
entries; U1 §11's handover and §6's sharpening. Parents: v10 **paper 31
§4.3** (the K1 arbitration operators), the **D75 Barandes audit** pin (b)
(the `Ẑ` sibling's specification and the screen's shape), **D74 TERMINAL**
(the transport loop census, group `⟨2,3⟩`, `R⁺`, odd sector empty), **LD**
(the walled odd sector), **v6 paper 7** Thms 7.1 and D3 (the `U(1)`
loop-class theorem), **v7 paper 30** (the `i`-twist amplitude form), and
`[B3]` (the unistochasticity criterion and the Schur-Hadamard gauge).
Receipt `v11/code/u3_unistochasticity_screen_exact.py`, output
`v11/code/u3_output.txt` — run from the repository root, **exit 0**,
**45 PASS / 0 FAIL / 0 ANCHOR-FAIL** of which **4 carry no independent
information and are labelled as such** (**41 independent-evidence
passes**), **12 s** wall clock against the pin's ~25 min budget. Re-run
at `PYTHONHASHSEED=7`: **output identical apart from timings** (0
differing lines).

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

- **The census is mixed and the census is the result.** Of ten committed
  readings: `2` are non-square and unscreenable, `6` fail the
  doubly-stochastic precondition, `0` reach the `S-FAIL-UNI` cell, `2`
  pass with an exhibited unitary, and `0` are `EXCLUDED-BY-CAP`.
- **Every generated object that would have had to be argued at the phase
  level is already excluded at the mass level.** The screen never gets to
  a phase question on a committed matrix, because the mass question
  answers first.
- **Both passers are orthostochastic.** `K1-2CONF` carries the `2×2`
  Hadamard certificate and `ARMC2-8x8` carries Sylvester's order-`8`
  Hadamard matrix — real orthogonal, verified entry by entry. The
  ortho/uni gap, which the D75 audit identifies as the exact place the
  necessity of `i` lives, is **empty on this census**.
- **And it is empty at the K1 layer for a structural reason, at every
  depth.** Paper 31 §4.3's own scope line reads: *"realized component
  sizes at the two cuts are exactly `{1, 2}` and the constructed family
  covers precisely those."* Every `2×2` bistochastic matrix is
  orthostochastic — constructed and verified across a printed sweep of
  the branch weight — and `1×1` trivially so. **No ortho/uni gap can open
  anywhere in the K1 arbitration family at its committed scope.**
  Deciding the necessity of `i` requires a generated conflict of
  multiplicity `≥ 3`, and the corpus has committed none.
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
| **`K1-2CONF`** | `2×2` | **S-PASS** | real orthogonal certificate, `0` residuals, `0` mismatches |
| `K1-PAIR-FULLIDX` | `4×4` | **S-FAIL-DS** | column sums `2, 0, 0, 2`; `Σ|·| = 4` |
| `K1-SINGLE-2x2` | `2×2` | **S-FAIL-DS** | column sums `2, 0`; `Σ|·| = 2` |
| `K1-JOIN-MENU` | `3×3` | **S-FAIL-DS** | column sums `3/2, 3/4, 3/4`; `Σ|·| = 1` |
| **`ZHAT-6x6`** | `6×6` | **S-FAIL-DS** | column sums `25/28, 1, 59/64, 55/64, 31/32, 19/14`; deficits `−3/28, 0, −5/64, −9/64, −1/32, +5/14`; `Σ|·| = 5/7` |
| `ZHAT-6x6-TRANSPOSED` | `6×6` | **S-FAIL-DS** | the same imbalance, on the rows: `[B3]`'s convention does not rescue it |
| `ZHAT-CLOSED-3x3` | `3×3` | **S-FAIL-DS** | column sums `7/8, 7/8, 5/4`, `Σ|·| = 1/2`; **and** `T = −1/4096 < 0` |
| **`ARMC2-8x8`** | `8×8` | **S-PASS** | real orthogonal certificate (Sylvester `H₈/√8`), `0` residuals, `0` mismatches; the complex DFT certificate is exhibited too |

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

## 4. The two structural verdicts

**The ortho/uni gap is empty on this census.** Both passers carry a real
orthogonal certificate, exhibited and verified. A matrix that is
unistochastic but **not** orthostochastic is one that cannot be lifted
with real amplitudes — the `i` is forced by the matrix's own entries —
and this census contains no such matrix. `KA-3` shows the property is
not vacuous: `J/3` is exactly such a matrix, and nothing committed and
generated resembles it.

**The K1 layer cannot force the complex numbers at its committed scope,
at any depth.** This is a no-go, not a null result. Its two premises are
paper 31 §4.3's own scope line (component sizes exactly `{1,2}`) and the
uniform `2×2` orthostochastic construction, re-verified across a printed
sweep of `p`. Together they close the question: **the necessity of `i`
is not decidable at the K1 arbitration layer at all**, and any unit that
wants to decide it must first generate a conflict of multiplicity `≥ 3`.

## 5. The price of enrichment

For every doubly-stochastic `D`, `‖M − D‖₁ ≥ Σ_j |c_j(M) − 1|`, because
`Σ_j |c_j(M) − c_j(D)| ≤ Σ_ij |M_ij − D_ij|` and `c_j(D) = 1`. The exact
prices:

| matrix | mass that must move, at least |
|---|---|
| `ZHAT-6x6` | `5/7` |
| `ZHAT-CLOSED-3x3` | `1/2`, **and** a phasor modulus, since `T = −1/4096` |
| `K1-JOIN-MENU` | `1` |

**This is a mass statement, not a phase statement.** No amount of phase
freedom repairs a column sum. Whatever a quantum-eligible completion of
the record chain is, it must move that much probability mass before any
question about `i` is even posable.

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
- **Clause (ii) — the loop class is `U(1)`-valued: NOT REPRODUCED, and
  the obstruction is structural.** Every non-unit holonomy measured on
  either arm — raw squares, carrier self-loops and independent carrier
  cycles alike — lies in `{1/2, 2/3, 3/2, 2}`, and the group they
  generate is `⟨2,3⟩`, free abelian of rank `2`, index `1` in `Z²`.
  `⟨2,3⟩` is therefore **torsion-free**, so its intersection with `U(1)`
  is exactly `{1}`: a positive rational of modulus `1` is `1`. Every
  measured holonomy has unimodular part exactly `1`, and no root of
  unity other than `1` occurs. **There is no `U(1)` content to find at
  any depth, for a reason that is a property of the value group and not
  of the window.**
- **Clause (iii) — interference is the loop-phase law: DEGENERATE.**
  `P = |A|² + |B|² + 2|A||B| cos(arg B(loop))` requires the cosine to
  range over `[−1, 1]`. On this carrier `arg B(loop) = 0` at every
  measured loop, so the exact range of the cosine is the single point
  `{1}`, the cross term sits at its **maximum**, no cancellation is
  available anywhere, and the law collapses to `P = (|A| + |B|)²` — the
  classical no-interference sum.

**The expected obstruction is confirmed by measurement and sharpened.**
D74's `R⁺`-only verdict said a unimodular part could only ever be the
sign `−1` and that `−1` is *realised nowhere*. The sharper statement is
that the search **could not have succeeded**: `−1` is not in the
multiplicative group of positive rationals at all, so its absence is a
theorem about the value group rather than a census outcome.

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
- **The unitarity-preserving subgroup is proper, and that is gated on a
  generated object.** The separable gauge `θ_ij = α_i + β_j` (printed:
  `α_i = 2i`, `β_j = 3j` in units of `2π/8`) preserves unitarity
  exactly — `0` residual entries. A single non-separable element —
  flipping the sign of the `(0,0)` entry alone, a legitimate
  Schur-Hadamard transformation with `θ₀₀ = π` — leaves `Γ` **exactly**
  invariant and destroys unitarity, with `14` non-zero entries in
  `U†U − I`. **`Γ`-invariance and unitarity-preservation are genuinely
  different conditions, and "the phase is gauge" does not mean "any phase
  will do."**
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
- **The two passers pass for degenerate reasons, and the note says so.**
  `K1-2CONF` passes because every `2×2` bistochastic matrix does, and
  `ARMC2-8x8` passes because it is the flat matrix — the ur-example of
  the class. The census therefore **cannot** decide the four-way
  contest over v6 paper 7's `C`-derivation in the positive direction; it
  decides it in the negative direction, for these objects, and it closes
  the K1 layer permanently at its committed scope.
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
family at paper 31 §4.3's fixture (realised component sizes exactly
`{1,2}`); the `Ẑ` sibling on the closed-scope `d42b3` family to depth
`6`; the D74 anchor arms at `(A,B)` depth `≤ 4` and `(A,B,C)` depth
`≤ 3`. ARM-C2's `8×8` matrix is taken **by specification** from U1's
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

- **To U2 and to any weld:** the corpus owns **no quantum-eligible
  generated matrix**. The two `S-PASS` objects are orthostochastic and
  degenerate; every substantive generated transfer fails at the mass
  level. Any weld that wants a quantum object must first supply the mass
  named in §5.
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
- **The one thing that would change the answer:** a generated conflict of
  multiplicity `≥ 3` whose transfer is doubly stochastic. Until one
  exists, the necessity of `i` is not a decidable question about this
  corpus's committed objects, and §4's no-go says why.
