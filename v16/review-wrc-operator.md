# Hostile review — WRC Paper 8, Seat O

Status: **FROZEN INDEPENDENT OPERATOR / INSTRUMENT REVIEW**  
Seat: O — operator algebra, instruments, exact reconstruction, and the
`psi/rho` fork  
Target: `v16/paper-08-walk-reconstruction.md`, SHA-256
`6934297cc2a79a8d7ebfa4dd7c52a58d601d686adf9d91b15c45fe416291e0f5`  
Grade: **ACCEPT-WITH-FIXES**

I read the frozen WRC protocol, pin and addendum, core and freeze notes,
fixture, repaired scorer, transcript, receipt, candidate, verification note,
the Seat-O antecedents, and the narrow JS/SCOUT-T methodological seam routed
after review began. I did not read, request, summarize, or infer either sibling
WRC review.

## 1. Verdict

The mathematical primary survives independent reconstruction:

```text
WRC-WALK-REPRESENTABLE-MODULO-CELL-HIT-INSTRUMENT
```

The coordinate vector is independently forced as

```text
(referent, transport, cuts, observables, instrument, beable)
= (true, true, true, true, false, true).
```

The fixed-carrier walk, its branch process, all nine inherited observable
families, and the count-field history map reproduce exactly. The literal
CELL-HIT operation is nonaffine on the full density-operator state space; this
is a theorem, not an inference from the displayed mixture. Therefore the
literal source operation is not an affine CP instrument.

The main correction is a quantifier correction. The displayed projective CP
repair is only one member of the complete affine family. I constructed a
different all-input complete CP instrument that preserves the outcome
probability **and the one registered conditioned continuation exactly**. No
affine CP instrument can preserve the source non-collapse continuation on all
inputs, or even on the registered two-cell state family, but the single
continuation witness does not by itself prove that. Thus the primary stays;
the repair qualifier must be explicitly scoped to the displayed projective
completion.

Two procedural repairs are also mandatory before terminal promotion. The
purportedly independent primary comparator calls the same decision function as
the builder, contrary to the RUNBOOK's comparator-independence rule. And the
post-result Questions replay repair is scientifically confined but makes a
result-bearing board state an accepted runtime anchor. Neither moved the
scientific result, but neither should be inherited as clean design.

WRC remains a reconstruction on one declared matrix fixture. It generates
lawful sampled label histories on a fixed carrier; it does not instantiate a
relational-carrier rewrite or prove that accumulated “geometry” is more than a
predictively useful memory encoding. That broader joint-law type is **not
instantiated**, not refuted.

## 2. Independent exact reconstruction

I rebuilt the arena without importing either WRC Python module. Arithmetic was
implemented directly as pairs `a+b w` over rational numbers with
`w^2+w+1=0`.

### 2.1 Carrier and transport

- Sites: `Z_3^2`, nine elements.
- Link labels: `(1,0)`, `(0,1)`, `(1,1)`.
- One-excitation cells: `9 x 3 = 27`.
- Local coin:

  ```text
  (1/3) [-1  2  2]
        [ 2 -1  2]
        [ 2  2 -1].
  ```

- Record phases: `1,w,w^2`.
- Shift: the plus-link permutation.

The coin is exactly unitary, every phase has unit norm, and the shift is a
permutation. Their composition is unitary. Its support contains exactly `81`
ordered input/output pairs and equals the declared “same input site, arbitrary
output link, then shift” support.

For the frozen initial state, the post-coin and post-shift labelled
probability vectors differ at exactly cells

```text
0, 1, 2, 4, 9, 14.
```

This independently recovers the six-cell cut discriminator.

### 2.2 Five-tick process

At every reached history I checked the input, post-coin, and post-shift norms,
and the sum of all CELL-HIT probabilities. Every check equals one exactly.
The nonzero branch counts and total masses are

| tick | branches | mass |
|---:|---:|---:|
| 1 | 3 | 1 |
| 2 | 27 | 1 |
| 3 | 486 | 1 |
| 4 | 10,527 | 1 |
| 5 | 284,078 | 1 |

The final quantities independently reproduce:

- exit probability `927415552/847288609443`;
- inverse participation
  `35971074413334039128803/239299329230617529590083`;
- maximum cell count `4`;
- determinant set `{0, 3/4, 1, 7/4, 2, 3}`;
- positive-definite distribution
  `{8: 927415552/847288609443,
  9: 846361193891/847288609443}`;
- curvature-constant probability `7598838656/22876792454961`.

I compared the independently produced values directly with the committed v14
receipt. All nine observable families match: site distribution, inverse
participation, emission field, link-class marginal, admissibility exit,
positive-definite distribution, determinant values, maximum cell count, and
curvature-constant probability. This is an exact regression, not a new
prediction.

## 3. The CELL-HIT affinity theorem

Let

```text
F_E(rho) = Tr(E rho) U rho U* ,
```

where `U` is unitary and `rho` ranges over the full convex density-operator
space. Put `f(rho)=Tr(E rho)`. For any density matrices `rho,sigma` and
`0<t<1`, direct expansion gives

```text
F_E(t rho+(1-t)sigma)-t F_E(rho)-(1-t)F_E(sigma)
=t(1-t)(f(rho)-f(sigma)) U(sigma-rho)U*.
```

If `F_E` is affine, unitarity makes the last factor nonzero whenever
`rho != sigma`; hence `f(rho)=f(sigma)` for every pair of states. Constant
expectation on every pure state implies `E=lambda I`. Conversely, scalar `E`
makes `F_E` a scalar multiple of unitary conjugation and therefore linear.

So the paper's theorem is correct on the full density-operator domain:

```text
F_E affine  iff  E is scalar.
```

On a restricted preparation set, the precise condition is only that
`Tr(E rho)` be constant on that set's affine hull; one must not promote the
full-space scalar conclusion to an arbitrary restricted domain. WRC explicitly
uses the full density space, so this caveat does not weaken its result.

Here `E_0=C*|0><0|C` is a rank-one projector in dimension 27, hence
non-scalar. For the registered half-mixture of the two coin-pulled basis
states, my independent defect matrix has exactly two nonzero entries:

```text
Delta[4,4] =  1/4,
Delta[9,9] = -1/4.
```

The witness is correct, and the theorem extends it to every density matrix.

## 4. Complete affine instruments: the missing classification

### 4.1 The displayed projective completion

For

```text
K_c = S P_c C,
```

I independently obtain

```text
sum_c K_c* K_c = C* (sum_c P_c) C = I.
```

This is an all-input complete affine CP instrument, not merely a normalized
map at one preparation. At the registered coherent preparation
`(3/5)|0>+(4/5)|1>` at the post-coin cut, outcome zero has probability
`9/25` for both the source rule and this projective instrument.

At the next record-dependent coin the six moved cells and exact pairs are

| cell | source | projective repair |
|---:|---:|---:|
| 3 | `64/225` | `0` |
| 4 | `16/225` | `0` |
| 5 | `64/225` | `0` |
| 9 | `1/25` | `1/9` |
| 10 | `4/25` | `4/9` |
| 11 | `4/25` | `4/9` |

This difference is calibration-invariant under any simultaneous cell
permutation, not merely under global phase: the source screen has support six,
the projective screen support three, and their probability multisets differ.
No relabelling can identify them.

### 4.2 Every probability-preserving affine completion

The paper stops one theorem too early. Suppose an affine CP operation
`J_c` has the exact registered outcome probabilities on every input. Then its
dual effect is fixed:

```text
J_c*(I)=E_c=C*P_c C=|e_c><e_c|.
```

For Kraus operators `A_alpha`,
`sum A_alpha* A_alpha=|e_c><e_c|`. If `v` lies in the kernel of `E_c`, then

```text
0=<v|E_c|v>=sum_alpha ||A_alpha v||^2,
```

so every `A_alpha` vanishes on that kernel. Therefore

```text
A_alpha=|v_alpha><e_c|,
J_c(rho)=Tr(E_c rho) sigma_c,
```

where `sigma_c=sum |v_alpha><v_alpha|` is one fixed normalized output state.
Conversely, every choice of normalized `sigma_c` defines such a CP operation;
because `sum E_c=I`, the family is complete.

Thus all affine probability-preserving completions are measure-and-prepare at
this rank-one cut. The projective repair is the special choice
`sigma_c=S|c><c|S*`.

This yields two exact conclusions which must both appear:

1. No one affine completion reproduces the non-collapse source on all inputs,
   because its conditioned `sigma_c` is fixed while `U rho U*` varies with
   `rho`. It already fails on the two post-coin preparations `|0>` and
   `(3/5)|0>+(4/5)|1>`, both of which give outcome zero nonzero probability
   and have different source successors.
2. The **single registered continuation can be fitted**. Choose
   `sigma_0` to equal the source output for that registered preparation, and
   choose any normalized `sigma_c` for the other outcomes. The resulting
   instrument is all-input affine, CP, complete, gives probability `9/25`,
   and reproduces that one conditioned future exactly.

Therefore equal probability plus the displayed future difference proves
non-equivalence to the displayed projective completion. It does not by itself
invalidate every affine completion. The all-input nonaffinity theorem—not the
one continuation—is what excludes standard affine-instrument equivalence.

This correction changes the qualifier, not the primary, because WRC's
instrument coordinate asks whether the **literal source operation** is
all-input affine.

## 5. The `psi/rho` fork

The exact ontic domain can be stated cleanly as

```text
X = projective pure states P(H) x count records Z^27.
```

At a record `n`, the law sends the ray deterministically to `U_n psi`, samples
`c` with `|(C_n psi)_c|^2`, and changes the record to `n+e_c`. This is a
well-defined stochastic process on `X`; global phase is gauge. It exactly
reproduces the source branches.

A classical mixture in this ontology is a probability measure `mu` over pure
rays, not merely its barycentre `rho=int |psi><psi| dmu`. The measure evolves
linearly as an epistemic distribution over ontic states, but two measures with
the same density matrix can evolve differently because the source retains the
individual pure ray. Equivalently, the nonlinear formula on `rho` is not a
preparation-independent ensemble law.

“Outside the affine class” is therefore necessary but not sufficient wording.
The branch is an exact **alternative ontology and dynamics**, not standard
quantum equivalence. WRC supplies no cross-block entanglement, steering
protocol, changing Bob algebra, or no-signalling theorem. It proves neither
signalling nor safety. Those remain prohibited by the paper's scope walls.

## 6. Beables, ports, recurrence, and law selection

The exhaustive two-tick census contains 27 nonzero labelled histories and
zero violations of

```text
n_t = n_0 + histogram(c_1,...,c_t).
```

This is a valid beable dictionary at the declared count-field reading. It
depends on retaining the sampled outcome port. If the ports are forgotten,
there is a probability distribution over possible records, not one actual
record. The histogram also forgets order, so it is not an injective history
encoding. The source and projective repair can retain the same outcome label
and make the same record update while carrying different conditioned process
states; a beable record is not the complete process state.

The recurrence and coin checks also reproduce exactly:

- four local record signatures, all repeated across distinct site tokens;
- Grover short-horizon inverse participation `33596579/129140163`;
- hidden admitted-coin value `51246599/129140163`.

This proves that the declared matrix fiber contains distinct unitaries with
different calibrated behavior. It does **not** prove that both are rivals under
a derived symmetry/locality law or that a universal recurring vertex type has
been selected. Equal signatures are repeated numeric inputs to one declared
rule. The scorer even publishes `couplings_selected=False` as a typed constant,
not as the output of a selector. The honest qualifier is “repeated local
signatures and an unselected declared coin fiber,” not a derived recurring
coupling law.

## 7. What kind of histories WRC constructs

The data-declared coin, phase, and shift do generate a genuine finite
stochastic history process: each nonzero post-coin cell is sampled, its label
is appended, the count record changes, and that record affects later phases.
The labels are not inert decoration.

But the relational carrier never changes, and the matrix rule is supplied as
fixture data. These are Born-outcome histories on a fixed catalogue, not
histories generated by a relational successor grammar whose output graph
computes the next transport. Consequently:

- the fixed record is load-bearing memory;
- dynamic relational geometry is not instantiated;
- the complete joint-law type is not refuted;
- every finite table remains compilable into lookup memory against an
  unrestricted adversary.

A better family-level question is whether the proposed geometry is a
**sufficient statistic of the past** for future calibrated observations under
one uniform law. In WRC, `(psi,n)` is sufficient by construction; `n` alone is
not, and the transport reads only `n mod 3` even though record observables can
read the full counts. No minimality or predictive quotient is computed.

Sufficiency would be necessary for a useful state description but still not
sufficient for ontology. Invertible memory encodings can be equally
sufficient. An ontological geometry claim additionally needs operationally
identified graph facts, interventions, invariant calibration, and exclusion
of a predeclared geometry-blind class at resource parity.

The required successor test therefore needs one uniform rule over a graph or
carrier family, a frozen training/held-out split and interventions, and matched
bounds on state dimension, memory, parameters, description length, ancillas,
and computation. A memoryless adversary is too weak; unbounded memory is
unbeatable on finite data. Only exclusion of a bounded class licenses a
class-relative result. If “geometry” is just the accumulated record renamed,
geometry-versus-memory remains an ontological naming question.

This is precisely the seam that WRC does not run. JS-S1a asks for a two-axis
predictive quotient and a predeclared stabilization test. SCOUT-T's relevant
artifacts remain untracked and procedurally unsealed, and in any event address
a different event-kernel feasibility problem on fixed `G`; feasibility there
would not establish ontology. WRC does not consume that candidate and should
not be used to bypass it. Its Q8 retirement is sound only for exact finite-walk
reconstruction, not predictive minimality or a joint successor law.

## 8. Primary logic and instrumentation

Given the six measured coordinates, the frozen outcome table makes index one
unambiguous: transport/cuts/observables pass, the literal instrument fails,
and the beable map passes. There is no silent replacement of full process
equivalence by selected screens because the word explicitly says “modulo
CELL-HIT instrument,” and the target table separately reports the failure.

However, the scorer's gate is not an independent comparator. The builder calls
`derive_primary_code(coordinates)` and the comparator calls the same function
again. The `primary-comparator` mutant changes only the printed offset. It
catches output corruption but cannot catch a shared error in the decision
function. This violates the RUNBOOK rule that comparator and builder share no
code. My independent Boolean derivation recovers the same word, so this is a
repairable instrument defect, not a changed primary.

Three more under-instrumented seams should be fixed:

1. `WRC-CP-REPAIR-DISCRIMINATOR` does not require `continuation_moves`; the
   positive movement appears only later as a qualifier predicate.
2. `WRC-BEABLE-MAP` does not require zero histogram violations, although the
   coordinate does. Its only named “histogram” mutant changes the readout type,
   not the histogram computation.
3. `WRC-BEABLE-VS-STATE` requires label equality but not state inequality.

The clean values are independently correct. These are missing hostile controls
against bugs that could change a coordinate or qualifier while leaving a
nominal assay gate green.

## 9. Artifact and replay audit

### 9.1 Frozen bytes and independent replay

All protocol-bound hashes match, including:

| artifact | SHA-256 |
|---|---|
| core | `94c74731179c1302254a3b7424dcb66d1154518bcf936c5531b05a52f42fa6b3` |
| fixture | `4ced0a163d645072ded79c51c92cf6f847576f062f35091df67db6d6f8a971c8` |
| repaired scorer | `58555958108ea62d28ebb541c5da8f6e9a3ec9ea50ef9a16540ee0df0ce1a128` |
| transcript | `45d386714b600ae3dc78369e3785cd78788333a3d0b6bdd31917289d03c2c34c` |
| receipt | `017debe87508bd91b64fa413870af47c5969b442240bff2fa998a538b2de4fef` |
| paper | `6934297cc2a79a8d7ebfa4dd7c52a58d601d686adf9d91b15c45fe416291e0f5` |

A clean alien-CWD run is byte-identical. I then copied the declared runtime
set to a fresh tree containing no `.git` directory and ran the copied scorer
there; all three artifact hashes are again identical.

The receipt has 31 unique green gates and 34 unique named mutants. I executed
all 34 mutations independently through the frozen scorer; every one refused.
Code order proves fail-before-write because artifact writes occur only after
`score` returns. Selftest exits `0`; an unknown option exits `2`; an illegal
selftest/output combination and an existing output target refuse. Independent
AST and recursive value scans find no float literal or runtime float in the
fixture, core, scorer, or receipt.

The payload digest, all 12 component manifest entries, transcript and paper
digests, 13 once-rendered claims, and all component seals recompute exactly.

### 9.2 Generic-core blindness and prefreeze exposure

The generic core is genuinely blind to the WRC physical carrier, Grover coin,
horizon, observables, and outcome word. It is not hypothesis-neutral—the pin
already asked it to support the literal nonlinear rule and CP comparison—but
it is answer-blind with respect to the physical fixture.

Successful temporary physical runs did expose enough of the result to permit
test overfitting before the fixture/scorer freeze. The disclosed post-exposure
changes strengthened observable binding and controls, but the continuation
and hidden-coin witnesses are constructed calibrations, not held-out
predictions. The exact algebraic theorem, exhaustive branch values, and direct
artifact reproduction remain mathematically safe because they can be—and here
were—rebuilt independently. What loses evidential force is any suggestion that
the physical fixture was an untouched prospective discriminator.

### 9.3 The Questions replay repair

The first addendum repaired a genuine pre-result transcription error in the
Questions digest. A second issue appeared after candidate commit #94: the same
commit updated `QUESTIONS.md` with the result, so replaying the scorer saw the
post-result hash rather than the pre-result hash used during generation.

The #95 repair changes only the scorer's anchor acceptance branch: it admits
the exact post-result Questions hash if three exact result-bearing tokens are
present. It does not change the fixture, walk, instrument, rendering,
comparator, or outcome vocabulary. Across #94 and regenerated #96:

- transcript SHA-256 is identical;
- paper SHA-256 is identical;
- every scientific `results` component is identical;
- receipt movement is confined to scorer hash, Questions anchor evidence,
  the duplicated anchor gate evidence, dependent anchor/gate seals, and the
  payload digest.

So the repair is scientifically provenance-only and minimal in result-bearing
scope. It is not ideal causal hygiene: the replay scorer now accepts a board
whose tokens state the answer. The board is not used to derive any scientific
branch, but future units should bind a pre-result snapshot or keep status-board
retirement outside the scientific runtime set.

Q8 retirement itself is bookkeeping, not evidence. The scorer currently makes
that qualifier mandatory, so reopening it causes a gate refusal; manually
removing the editorial qualifier leaves all six coordinates and the primary
unchanged. The gate should be decoupled from the primary.

### 9.4 Dependencies

The primary does not depend on any Paper 3–7 verdict. It is conditional on the
pin's declared affine-instrument target class, and its exact proof is
self-contained. The Paper 7 anchor supports only the broader coupling-language
context. Papers 3–7 have since been adjudicated, but WRC still does not
instantiate their requested changing-carrier joint law. That is a missing
construction, not a no-go against the type.

## 10. Mandatory attack answers

1. **Is the primary forced?** Yes, by the independently rebuilt coordinates.
   The scorer's comparator is not independent, but the external derivation is.
2. **Was equivalence weakened to selected screens?** No for the literal target:
   the primary explicitly records instrument failure. Yes if one were to read
   the displayed continuation as excluding all affine completions; it does not.
3. **Does the affinity result hold outside the two-vector witness?** Yes, on
   the full density space by the scalar-effect theorem.
4. **Does equal Born probability plus a moved future invalidate the source?**
   Only relative to that displayed projective repair. The all-input affinity
   theorem is the actual standard-instrument obstruction.
5. **Can a larger affine instrument preserve the continuation?** It can preserve
   the single registered preparation exactly. No probability-preserving
   affine instrument can preserve the non-collapse successor on two distinct
   nonzero-probability inputs or on all states.
6. **Does WRC distinguish nonlinear pure-state unravelling from operational
   quantum equivalence?** Mathematically yes, but the ontology must explicitly
   carry the pure-state ensemble measure. No standard mixed-state, steering,
   or no-signalling equivalence follows.
7. **Did replay repair move science?** No. It moved only anchor acceptance and
   dependent provenance bytes; the accepted post-result input should still be
   retired from future scientific runtime designs.

## 11. Shared procedural answers

1. **Generic core answer-blind:** yes with respect to WRC physical answers;
   it is intentionally specialized to the pinned operator question.
2. **Prefreeze overfitting exposure:** yes. Exact proofs and exhaustive
   recomputations survive; “held-out” physical witness language does not.
3. **Wrong Questions hash and #95:** the first defect was provenance only; the
   second was a replay-order defect. #95 is confined and honest, though a
   pre-result snapshot would have cleaner causal structure.
4. **#94/#96 invariance:** transcript and paper are byte-identical; scientific
   receipt content is identical; only the disclosed provenance closure moves.
5. **Q8 reopening:** the current gate refuses, but the scientific primary is
   unchanged. Board status must not be treated as evidence.
6. **Papers 3–7:** no primary dependence. Any creation-event or joint-law
   ontology remains conditional, and WRC supplies no changing-carrier instance.

## 12. Grade

**ACCEPT-WITH-FIXES.**

The fixed-arena reconstruction, nonaffinity theorem, and primary are correct.
The report should not be rejected: I found no false load-bearing walk number
and no affine counterexample to the all-input source obstruction. It should not
be accepted unchanged because the full CP-completion family materially narrows
the continuation reading, the ontic mixture domain is unstated, the comparator
violates independence, and status-board/predictive-sufficiency boundaries need
engraving.

## 13. Numbered repair / kill list

1. **REPAIR — classify all affine completions.** Add the rank-one-effect
   measure-and-prepare theorem and state that the displayed `S P_c C`
   instrument is one completion.
2. **REPAIR — narrow the continuation qualifier.** Rename it to
   `DISPLAYED-PROJECTIVE-CP-REPAIR-MOVES-CONDITIONED-FUTURE`; state that another
   complete affine instrument matches the one registered continuation.
3. **REPAIR — add the two-preparation discriminator.** Test outcome zero on
   both `|0>` and `(3/5)|0>+(4/5)|1>` at the post-coin cut. This is the smallest
   exact witness excluding every fixed-output affine completion on the tested
   two-cell family.
4. **REPAIR — type the ontic mixtures.** Define the domain as pure rays plus
   record and classical probability measures over rays; prohibit any claim of
   standard mixed-state, EPR, steering, or no-signalling equivalence.
5. **REPAIR — make the comparator independent.** Reparse the sealed coordinate
   object and implement a separate decision tree sharing neither
   `derive_primary_code` nor target literals with the builder. Add a mutant in
   the shared decision logic, not only a printed-word offset.
6. **REPAIR — close assay predicates.** When the positive qualifiers are
   emitted, require continuation movement, zero beable violations, and
   conditioned-state inequality in their respective gates; add direct
   computation mutants.
7. **REPAIR — decouple Questions/Q8.** Keep retirement editorial and outside
   the primary gate. Future replay should bind a pre-result snapshot rather
   than recognize result-bearing status text.
8. **REPAIR — price exposure.** Call the continuation, alternate coin, and
   post-exposure controls exact constructed calibrations, not held-out physical
   predictions.
9. **REPAIR — narrow recurrence language.** Replace “recurring vertex
   couplings” by repeated local signatures under one declared rule and an
   unselected declared coin fiber. Do not treat hard-coded
   `couplings_selected=False` as a measured selector result.
10. **REPAIR — engrave predictive sufficiency.** State that WRC does not run
    JS-S1a, does not consume unsealed SCOUT-T, and does not distinguish
    geometry from resource-matched generic memory over held-out carrier
    families.
11. **KILL CONDITION — primary mathematics.** Kill the primary if an affine CP
    family with effects `E_c` reproduces the literal non-collapse successor on
    two distinct nonzero-probability inputs, or if an independent exact walk
    reconstruction fails any committed observable family. Neither kill fires.
12. **KILL CONDITION — broader ontology.** Any future claim of irreducible
    dynamic geometry must die unless one uniform graph-dependent rule excludes
    a predeclared geometry-blind adversary at matched resources on held-out
    carriers. WRC does not attempt that claim.

## 14. Report checksum

Normalized/self convention: hash the UTF-8 bytes of this report after replacing
the value on the next line by the literal token `<NORMALIZED-SELF-SHA256>`.

Normalized/self SHA-256: `5c474f507d94c46aa837aacf461f583d64ca7f2f2bc2fb3637e5da345902780a`

The ordinary whole-file SHA-256 is necessarily reported out of band in the
freeze dispatch, because embedding it would change the file being hashed.
