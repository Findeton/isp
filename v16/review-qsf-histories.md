# QSF Paper 9 hostile review — Seat H: histories, division, Barandes, and predictive sufficiency

Status: **FROZEN INDEPENDENT HOSTILE REPORT**. I did not read, list,
request, summarize, or infer either sibling QSF report. I reviewed the frozen
candidate bound by `v16/note-qsf-hostile-protocol.md`, rebuilt the relevant
walk and history calculations without importing QSF or WRC executable code,
and made no candidate, board, ledger, protocol, or git change. Scratch
calculations were confined to `/private/tmp`.

## Verdict

**Grade: ACCEPT-WITH-FIXES.**

The proposed synthesis primary survives:

```text
QSF-METHOD-INCONCLUSIVE
```

It survives because it is cautious. The exact history calculation does prove
that one density operator is not a sufficient input for the retained
state-record output at any registered window from one through five. It does
not prove that no genuine stochastic division boundary exists. On the finer
state space consisting of a projective pure ray and the count record, the WRC
rule is already a normalized stochastic kernel and is affine on probability
measures over that finer state. Whether that is accepted as ontology is the
same pure-state fork, not a history theorem.

Two delivered subordinate claims need material repair. First,
`QSF-HISTORY-NO-AFFINE-RECORD-BOUNDARY-WITHIN-1-5` is defensible only when
read as **no density-operator-sufficient retained state-record boundary**.
The paper's broader sentence that the existing records do not supply a lawful
history boundary is not established. Second, the S1 calculation is not the
complete predictive quotient required by its pin: its “future law” contains
only future ordered trigger suffixes and omits the final count record and
process state. At the final-record grain the quotient is already discrete on
all six registered rows.

The proposed Seat-H disposition is therefore:

```text
PRIMARY: QSF-METHOD-INCONCLUSIVE
ARM C: NO-RHO-SUFFICIENT-RETAINED-STATE-RECORD-BOUNDARY-WITHIN-1-5
DIVISION: FINE-STATE-DIVISION/RECOVERABILITY UNTESTED
S1: ORDERED-FUTURE-SUFFIX-ONLY; NO STABILIZATION WITHIN THE TESTED RANGE
```

## 1. Frozen object and source audit

The chronology is clean: pin `d058f389d719e8dfef2da99dac84a6d3d4293e11`,
generic core `88f487c60deddebea3387f31f481fff01756009d`, physical fixture
`4d959e71ea3799cfb4f2059440ecdb34a87018aa`, candidate
`67d8b76e4479bce29e23521ab9eb200d1105e077`, and hostile protocol
`75810d2f1bb8ca57ff73525502709ab7d6ce932c`. The six frozen file hashes
recompute exactly:

| artifact | SHA-256 |
|---|---|
| `v16/code/qsf_core.py` | `6dd6b4999c0474a362f56bb70271845fb5f322c6676a4de90c79b64ce753736f` |
| `v16/code/qsf_fixture.json` | `7fe949383d1e27017b972f941c4cf1875d3c574d3120d9993240bd7a0756404f` |
| `v16/code/qsf_score.py` | `e5cebe8f40760277942d325b1cd257108c20c323e8a5d05b4c86d878471077bf` |
| `v16/code/qsf_output.txt` | `ecc8abf7dd17951b262641870ee2ec3748f83bba70434a55354bdad8ff0b78d1` |
| `v16/code/qsf_receipt.json` | `15f689c2eda69509c5da0f152bf68365cec45c626d2203c699fcda98f92ade4e` |
| `v16/paper-09-quantum-seam.md` | `cad1925b2f687aff83cc298225dae65931189071ed5397c524d39762c88ff2af` |

I independently implemented exact arithmetic in
`Q(omega)`, `omega^2+omega+1=0`, the 27-cell walk, complete literal
histories, direct-sum record blocks, and predictive partitions from the
result-neutral fixture. No QSF/WRC module was imported. The candidate paths
were clean before review.

For the Barandes typing I checked the two primary sources named by the pin:
[The Stochastic-Quantum Correspondence](https://arxiv.org/abs/2302.10778)
and [Quantum Systems as Indivisible Stochastic Processes](https://arxiv.org/abs/2507.21192).
Their underlying object is an ordinary probability law on a fixed
configuration space; a division event is an allowed conditioning time for
the first-order transition law. Density-operator CP is a Hilbert-space
representation condition, not the definition of a division event.

## 2. Five complete-history windows rebuilt

Let `Z` be the equal mixture of the two orthogonal pre-coin rays `e0,e1`, and
let `X` be the equal mixture of `(e0+e1)/sqrt(2)` and
`(e0-e1)/sqrt(2)`. The two preparations have exactly the same density
operator. Exact independent enumeration reproduces every published total
variation:

| tick | ordered-hit TV | count-record TV | published diagonal screen TV | full discarded density difference | retained state-record block |
|---:|---:|---:|---:|---|---|
| 1 | `0` | `0` | `0` | identical | different |
| 2 | `1/2` | `1/2` | `0` | identical for this `Z/X` pair | different |
| 3 | `211/324` | `211/324` | `0` | identical for this `Z/X` pair | different |
| 4 | `180223/236196` | `12415/17496` | `1664/19683` | 462 of 729 entries differ | different |
| 5 | `1694745299/2066242608` | `820725659/1162261467` | `3747023/43046721` | all 729 entries differ | different |

At ticks four and five the diagonal total variation of the full density
difference is exactly the published screen TV. At ticks one through three the
stronger full discarded density—not merely its diagonal—is identical for this
particular pair. That equality is preparation-specific and does not establish
an affine map on all inputs.

### 2.1 The tick-one witness is real, but it is not in the count law

Write `s0=S|0>` and `s1=S|1>`; in the frozen carrier these are cells 9 and 4.
For record sector `n0+e0`, the two unnormalized state blocks are

```text
Z:  (1/2) |s0><s0|
X:  (1/4) (|s0><s0| + |s1><s1|),
```

and the opposite exchange holds in sector `n0+e1`. Thus the direct-sum block
has four nonzero difference entries and trace distance `1/2`, although both
classical count distributions are `(1/2,1/2)`. This independently confirms
that the tick-one witness lives in the retained **state-record correlation**,
not in ordered-history or count frequency.

The scorer's probe is selected inside the post-fixture scorer as
`shift_images()[0]=9`; the result-neutral fixture names no probe cell. Its
lineage is therefore incomplete. The fact survives a hostile probe change:
in the two record sectors, cell 9 moves by `(+1/4,-1/4)` and cell 4 by
`(-1/4,+1/4)`. Only those two basis probes move at tick one; all 27 basis
probes move at every later registered tick. The existence result is robust,
but the calibration must be predeclared and its exact values gated.

### 2.2 Erasure controls

- Erasing only the ordered internal label while retaining the count record
  leaves the count TV nonzero from tick two onward. At ticks four and five it
  reduces, but does not erase, the distinction: ordered/count TVs are
  `180223/236196` versus `12415/17496`, then
  `1694745299/2066242608` versus `820725659/1162261467`.
- Summing the state-record blocks after one tick erases the distinction
  exactly. If the record is also prevented from feeding any later coin, the
  discarded process state is the fixed unitary evolution
  `U^k rho U^(dagger k)` at every window. This controls the process-state
  map only; retaining multi-time hit labels can still expose decomposition
  sensitivity.
- Erasing the final record after it has already fed back is not an eraser of
  the dynamics. The discarded density differs at ticks four and five for the
  registered pair.
- The exact count update is append-only within WRC, but it records only an
  unordered histogram. Already at depth three there are 486 ordered histories
  and 477 count records. Append-only storage is not recoverability of order,
  actualization, or permanence under an enlarged continuation grammar.

## 3. Determine nonlinearity before Choi language

The candidate correctly refuses to compute a Choi matrix after nonaffinity.
However, it does not actually build the declared all-input maps
`Phi_k^discard` and `Phi_k^record`; it tests one equal-density pair and one
diagonal screen. An independent all-input witness closes the missing typing.

Take

```text
rho = (|0><0| + |3><3|)/2
f0  = (3|0> + 4|3>)/5
f1  = (-4|0> + 3|3>)/5.
```

The equal mixtures of `{|0>,|3>}` and `{f0,f1}` are exactly the same `rho`.
After two discarded-history steps their full densities differ in 72 entries.
All carrier-basis diagonals remain equal, so the registered style of screen
would miss the failure. One exact off-diagonal is

```text
(rho_Z-rho_F)_[1,7] = (448 + 224 omega)/151875.
```

The calibrated effect
`(|1>+|7>)(<1|+<7|)/2` detects probability difference `112/50625`.
At tick three the same pair differs in 477 density entries and has diagonal
TV `99328/4100625`.

The correct map ledger is therefore:

| output grain | tick(s) | status before Choi |
|---|---:|---|
| discarded process state | 1 | fixed unitary channel; affine and CP |
| discarded process state | 2 | nonaffine on the full input space; registered `Z/X` screen is blind |
| discarded process state | 3 | nonaffine; an unregistered equal-density pair moves the diagonal screen |
| discarded process state | 4–5 | nonaffine already on registered `Z/X` pair |
| classical ordered/count law | 1 | Born outcome law is affine |
| classical ordered/count law | 2–5 | not a function of `rho`; registered same-`rho` laws differ |
| retained state-record block | 1–5 | not a function of `rho`; tick one is the block witness above |

No Choi/CP assertion is licensed for any nonaffine row. Conversely, a zero TV
for one ensemble pair or one screen never licenses affinity. This is the main
missing mandatory control in Arm C.

## 4. What the result says about a genuine division boundary

Four notions must remain separate.

1. **Internal CELL-HIT label.** This is an algorithmic emission alternative.
   Ordered labels are not retained by the count histogram.
2. **Count record.** It is a declared, append-only integer field under WRC's
   own successor. It retains counts, not order, and no one-actual-history
   postulate is supplied.
3. **Density-operator boundary.** The same `rho` has different retained block
   futures, so `rho` is not a sufficient boundary state. This is the result
   Arm C actually proves.
4. **Stochastic division event.** In Barandes's framework this is an allowed
   conditioning time of a stochastic law on its configuration space, with
   the law of total probability. It is not defined by a Choi test and is not
   synonymous with a durable record.

Indeed, if the ontic pure-state branch is admitted, WRC itself defines the
fine-state kernel

```text
([psi],n) --c with probability |(C_n psi)_c|^2-->
([S C_n psi], n+e_c).
```

The probabilities sum to one. The kernel acts linearly on probability
measures over `projective-ray x count-record`, and its iterates compose by
ordinary kernel composition. Thus the density failure does not force a
different history boundary; it says the decomposition/pure ray must remain in
the boundary state if this branch is taken. That choice has operational costs,
but those belong to the composite/steering assay, not to a claim that history
composition itself failed.

QSF enters neither an exact Barandes cut-composition residual nor a
recoverability test over a closed continuation catalogue. Its receipt says
`cut_cp_test_entered=false` and
`record_recoverability_absolute=false`. The scoped phrase “no lawful
density-operator boundary” is therefore exact; “the existing retained records
do not supply a lawful history boundary” is too broad. The v12 result that a
legitimate division was a record event was a theorem of its registered model,
not Barandes's definition and not a universal biconditional to import here.

## 5. Predictive sufficiency rebuilt at both axes

The scorer's six suffix-law rows reproduce exactly:

| past | future | histories | ordered-future-suffix quotient | first registered sufficient summary |
|---:|---:|---:|---:|---|
| 1 | 1 | 3 | 1 | `NO-TRACE` |
| 1 | 2 | 3 | 1 | `NO-TRACE` |
| 2 | 1 | 27 | 2 | `PREVIOUS-TRIGGER` |
| 2 | 2 | 27 | 15 | `UNORDERED-COUNTS` |
| 3 | 1 | 486 | 126 | `FULL-ORDERED-TRACE` |
| 3 | 2 | 486 | 485 | `FULL-ORDERED-TRACE` |

These numbers are correct for exactly what `future_distribution` returns: a
probability distribution over the future trigger suffix. They are not the
complete future law required by JS S1a and the relational-sufficiency method.
The scorer omits the final count record and final process state.

### 5.1 Complete-grain quotient

I recomputed each row at four observation grains:

| past | future | suffix | final count record | final projective ray | joint ray-record / complete |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 3 | 1 | 3 |
| 1 | 2 | 1 | 3 | 1 | 3 |
| 2 | 1 | 2 | 27 | 3 | 27 |
| 2 | 2 | 15 | 27 | 21 | 27 |
| 3 | 1 | 126 | 486 | 252 | 486 |
| 3 | 2 | 485 | 486 | 486 | 486 |

Because WRC declares the count field a calibrated readout, the final-record
column cannot be omitted. `NO-TRACE` is therefore not sufficient at past
depth one; `PREVIOUS-TRIGGER` is not sufficient at past depth two; and the
published S1 table cannot serve as the complete predictive benchmark. The
complete future record law distinguishes every reached history in the frozen
range.

This does not imply absolute ordered-history memory. The law-native present
state `([psi],n)` screens off the past by construction. For predicting only
future hit suffixes, `[psi]` together with `n mod 3` is sufficient at every
future horizon because the coin reads only those residues. To predict the
absolute future count readout, retain exact `n`. At past depths 1, 2, and 3,
the projective-ray-plus-residue summary has respectively 3, 27, and 486
blocks. It is a present state, not a growing ordered trace.

### 5.2 An unregistered coarser statistic and window extension

The exact next-hit probability vector is an unregistered coarser statistic.
At past depth three/future one it has 126 blocks—exactly the predictive
quotient—and is sufficient, whereas the registered `FULL-ORDERED-TRACE` has
486 singleton blocks. It fails at future two. This is a useful control: “first
registered sufficient” does not mean minimal.

Extending the suffix window to three gives quotient 3 at past depth one and
27 at past depth two, compared with 1 and 15 at future two. At past depth
three, the only future-two merged pair is histories `(1,3,12)` and
`(1,3,14)`; future three separates it with exact TV
`143335590784/2541865828329`. Hence the future-three quotient is 486. The
suffix partitions do not stabilize in the frozen future range. The pin
required a predeclared stabilization predicate and a
`JS-NO-STABILIZATION-WITHIN-<range>` disposition; the scorer implements
neither.

The correct conclusion is twofold: the suffix-only benchmark shows finite
partition refinement, while the complete record benchmark is already
discrete. Neither proves infinite memory, absolute minimality, or that an
ordered history is ontic.

## 6. Integrity and adversarial controls

The complete executable integrity battery was run from the repository, an
alien working directory, and a minimal off-tree copy containing no `.git`.
The clean, alien-CWD, and off-tree runs each exited zero and reproduced the
frozen transcript, receipt, and paper byte for byte. A deleted byte-bound
antecedent caused refusal before any artifact write. A pre-existing output
sentinel was preserved and the other targets were not created. Unknown argv
returned exit 2 with no artifact, and `--selftest` returned zero.

All 20 registered mutants were executed separately. Each returned nonzero and
wrote none of its three targets:

| mutants | result |
|---|---|
| `anchor-hash`, `fixture-answer`, `coin-entry`, `shift-orientation`, `literal-collapse` | refused, no write |
| `a0-output`, `signature-split`, `hjw-density`, `alice-setting`, `ontic-history` | refused, no write |
| `affine-control`, `record-retention`, `history-window`, `predictive-merge`, `s1b-entry` | refused, no write |
| `scope-promotion`, `primary-comparator`, `exactness`, `transcript-seal`, `paper-claim` | refused, no write |

The exact last-gate mapping and replay hashes are retained in the off-repo
integrity receipt. No integrity failure changes the scientific corrections
above.

## 7. Proposed primary and numbered repair / kill list

The paper should retain `QSF-METHOD-INCONCLUSIVE`. It should not promote a
history base. The following repairs are required before adjudication can call
the Seat-H arm closed.

1. **REPAIR — retype Arm C.** State that the five-window result excludes a
   `rho`-sufficient retained state-record boundary. Do not say it excludes a
   finer pure-ray/configuration stochastic boundary.
2. **REPAIR — tick-one wording.** Replace “the retained count-record sectors
   distinguish them at every window” with “the retained state-record blocks
   distinguish them; at tick one the classical count law is identical.”
3. **REPAIR — build the declared maps.** Construct the full discarded density
   and full direct-sum state-record output, not only a diagonal screen and one
   probe. Add the exact `{0,3}` versus `3-4-5` rotated-decomposition witness;
   it kills discarded-state affinity at tick two while every basis diagonal
   is blind.
4. **REPAIR — probe lineage.** Put the block probe in the frozen fixture and
   add the cell-4/cell-9 sign-swap control. A scorer-local “first shifted cell”
   is not a calibrated observable lineage.
5. **REPAIR — division typing.** Specify the configuration space and test the
   stochastic law-of-total-probability/cut-composition condition separately
   from density affinity and CP. If the fine state is `([psi],n)`, say so and
   price the ontic decomposition explicitly.
6. **REPAIR — recoverability.** Test count-sector recoverability under the
   licensed continuation grammar, include a genuine eraser/reconvergence
   control, and distinguish unordered count permanence from ordered-label
   permanence and actualization.
7. **REPAIR — S1 target.** Recompute predictive equivalence using the complete
   registered future instrument: at minimum final record, final process
   state, and calibrated probes. Label the current table
   `ORDERED-FUTURE-SUFFIX-ONLY`.
8. **REPAIR — S1 stabilization.** Freeze the partition-equality predicate,
   publish the complete partition rather than dimensions alone, add future
   horizon three, and emit the required no-stabilization word for the suffix
   benchmark.
9. **REPAIR — present-state control.** Include projective ray plus exact count
   (and the modulo-three suffix-only quotient) among candidate summaries. A
   full ordered trace is trivially sufficient and does not establish memory
   minimality.
10. **KILL CONDITION — Barandes overreading.** If “Barandes division” is meant
    to require density-operator CP by definition, remove the attribution. That
    is QSF's operational quantum-seam requirement, not Barandes's stochastic
    definition.
11. **KILL CONDITION — history-base promotion.** Any promotion to
    `QSF-HISTORY-BASE-VIABLE-AT-GENUINE-BOUNDARY` is forbidden until cut
    composition, recoverability, actualization domain, and complete S1 all
    pass at one declared boundary grain.
12. **KILL CONDITION — absolute memory.** Any claim that the finite quotient
    proves irreducible or infinite ordered-history memory is unsupported. The
    delivered fine present state already screens the past.

## Hash seal

Ordinary SHA-256 of the report body above this `## Hash seal` heading
(including the newline immediately before the heading):
`0ac9a99e53b9c1374c4f083f82026722b4352902e9b1bdd814ca9ddf9e037be3`.

Normalized/self SHA-256 of the complete report: replace the two 64-hex digest
values in this seal with 64 ASCII zeroes, preserve all other bytes, and hash the
UTF-8 file:
`1b24a33e0ce395ddbbc83a786d6173d31e0489e31e63a878fd6542178d7bf4bc`.
