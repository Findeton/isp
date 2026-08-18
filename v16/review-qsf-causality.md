# QSF hostile review — Seat C: composite, steering, and causality

Status: **FROZEN INDEPENDENT HOSTILE REPORT**.

I read the frozen QSF protocol completely and worked only from the immutable
candidate, its frozen antecedents, primary literature, and independent exact
arithmetic under `/private/tmp`.  I did not read, list, request, summarize, or
infer either sibling QSF report.  I made no candidate or git mutation.

## 1. Grade and proposed primary

**Grade: ACCEPT-WITH-FIXES.**

The fixed-factor steering calculation is correct and stronger than the paper's
single displayed statistic suggests.  The exact `2 x 27` construction has one
Bob density operator, two complete Alice instruments, and the required HJW
conditional ensembles.  After Alice outcomes are summed, Bob's literal WRC
count-record law depends on Alice's setting at ticks two and three, with exact
total variations

```text
0, 1/2, 211/324.
```

The same numbers occur at ordered-history and count-record grain.  The latter
is the important calibrated witness: it does not require Bob to recover the
order of his hits.  A second exact mutually unbiased Alice basis gives the
same result.  Two distinct affine instruments give zero, and in fact every
fixed-factor affine local instrument is blind to the choice by a one-line
linearity theorem.

The candidate is also right about its limit.  This kills only the extension
that combines standard fixed tensor factors, HJW remote preparation, actual
Alice outcomes, and the literal ontic-ray/count rule.  There is no relational
composite, dynamic separation condition, changing Bob algebra, or physical
light cone.  Failure to construct those objects is incompleteness, not a
no-signalling theorem and not a refutation of every future ISP composite.

My proposed overall primary remains:

```text
QSF-METHOD-INCONCLUSIVE
```

with Arm B sharpened to:

```text
PHRASABLE-SIGNALLING-WITNESS
[NATURAL-FIXED-FACTOR EXTENSION;
 BOB COUNT-RECORD GRAIN AT TICKS 2 AND 3;
 RELATIONAL COMPOSITE UNBUILT]
```

The fixes are principally lineage, all-window coverage, generic-affine
control, and language.  They do not erase the witness.

## 2. Frozen target and hashes

The six frozen candidate hashes independently reproduce:

| artifact | SHA-256 |
|---|---|
| `v16/code/qsf_core.py` | `6dd6b4999c0474a362f56bb70271845fb5f322c6676a4de90c79b64ce753736f` |
| `v16/code/qsf_fixture.json` | `7fe949383d1e27017b972f941c4cf1875d3c574d3120d9993240bd7a0756404f` |
| `v16/code/qsf_score.py` | `e5cebe8f40760277942d325b1cd257108c20c323e8a5d05b4c86d878471077bf` |
| `v16/code/qsf_output.txt` | `ecc8abf7dd17951b262641870ee2ec3748f83bba70434a55354bdad8ff0b78d1` |
| `v16/code/qsf_receipt.json` | `15f689c2eda69509c5da0f152bf68365cec45c626d2203c699fcda98f92ade4e` |
| `v16/paper-09-quantum-seam.md` | `cad1925b2f687aff83cc298225dae65931189071ed5397c524d39762c88ff2af` |

The sealed result payload is
`69bf58d9542b1a778d0adb33f03a66579bb2b3e3a342541fe0f0b98bd5237e69`.
The pin, core-freeze note, fixture-freeze note, candidate verification, and
hostile protocol hash respectively to

```text
6b70803366ddaf481e4dfb53c4150507a1dfbda86a0c5131021c03ec2ce0bbf3
9449293dd7be73d16a31e3ca152740ae99aa9c8ca7442eea0a34ed076cab9e26
9cd58d6662135e0e54d296ad4a6b1f12208406bef9cf34f7eed23dc07468ecc6
650d8ca4e9073003b8342eb27e8e7bb8a4c04009a4eecc4ac0ea2c5eac27f467
90ee36c402baf96e783742212aa5f61f2dbd2414576a09b1656bd7f3501002d9
```

## 3. Independent `2 x 27` construction

Let `C_0` be WRC's post-coin unitary at the uniform initial record and let
`|0_cell>`, `|1_cell>` denote post-coin cells zero and one.  I independently
constructed

```text
|e0> = C_0^dagger |0_cell>,
|e1> = C_0^dagger |1_cell>.
```

Exact `Q(omega)` arithmetic gives

```text
<e0|e0> = <e1|e1> = 1,
<e0|e1> = 0,
C_0|e0> = |0_cell>,
C_0|e1> = |1_cell>.
```

The natural fixed-factor joint state is the rank-one density operator of

```text
|Omega> = (|0_A>|e0_B> + |1_A>|e1_B>)/sqrt(2)
```

on `C^2 tensor C^27`.  The calculation needs no irrational runtime number:
its `54 x 54` density matrix consists of four `27 x 27` blocks
`|ea><eb|/2`.  It has trace one and Bob marginal

```text
rho_B = (|e0><e0| + |e1><e1|)/2.
```

Alice's Z instrument has projectors `|0><0|, |1><1|`.  Her X instrument has
projectors onto `(|0> +/- |1>)/sqrt(2)`.  Each pair sums to the identity.  Each
outcome has probability `1/2`.  Conditioning the joint state gives Bob

```text
Z:  {1/2, |e0>}, {1/2, |e1>}
X:  {1/2, (|e0>+|e1>)/sqrt(2)},
    {1/2, (|e0>-|e1>)/sqrt(2)}.
```

Both average exactly to `rho_B`.  Alice's outcome is absent from every Bob key
used below: the two conditional rows are weighted by `1/2` and summed before
the Bob distributions are compared.

This is a correct HJW realization for the fixed-factor surrogate.  It is not
a relational separation theorem.  The subsystem algebras are the declared
matrix factors `M_2 tensor I_27` and `I_2 tensor M_27`; no graph construction
derives them.

## 4. Independent literal histories and total variations

I rebuilt the WRC phase, Grover coin, shift, noncollapse CELL-HIT rule, and
append-only count update without importing QSF or WRC modules.  For each
Alice setting I propagated the two Bob conditional rays, weighted the complete
local hit histories, and then summed Alice outcomes.

The exact comparison is:

| tick | ordered-history TV | count-record TV | ordinary cell-screen TV |
|---:|---:|---:|---:|
| 1 | `0` | `0` | `0` |
| 2 | `1/2` | `1/2` | `0` |
| 3 | `211/324` | `211/324` | `0` |

One concrete tick-two certificate is useful.  For Bob history `(0,3)`, the Z
preparation has probability `0` and the X preparation has `1/9`.  For history
`(0,10)`, the probabilities are `2/9` and `1/9`.  There are twelve differing
two-hit rows whose absolute differences sum to one, hence TV `1/2`.

At this window the first hit is cell zero or one and the second lies among
cells `3,4,5,9,10,11`.  The append-only 27-count vector therefore identifies
the two hits even after order is forgotten.  That is why the count-record TV
equals the ordered-history TV.  The witness is not an artifact of giving Bob
an uncalibrated “full trace.”

Removing the Bob record readout while keeping hidden record feedback makes the
registered ordinary cell screens equal through tick three.  Extending the same
independent run one step gives screen TV

```text
tick 4: 1664/19683.
```

This agrees with the candidate's five-window history table and exposes an
important distinction: removing the **readout** delays the accessible signal;
it does not remove decomposition sensitivity if the hidden record still feeds
future transport.  Removing both the record readout and record-controlled
continuation reduces this control to an affine unitary process and removes the
witness.

## 5. Local calibration, conditioning, and causality type

The count-record witness has a complete finite lineage:

```text
fixed Bell/HJW preparation
 -> Alice chooses one complete local projective instrument
 -> Alice outcomes are summed
 -> Bob receives no setting or outcome variable
 -> Bob applies the same literal local WRC successor
 -> Bob reads the same append-only 27-count register
 -> the tick-two count distribution depends on Alice's setting.
```

No classical message enters the Bob state, record, transition, or readout.
There is no Alice--Bob interaction after the initial joint preparation.  A
common relabeling of Bob's count cells only permutes both distributions and
leaves total variation invariant.  Swapping Alice outcome names likewise
leaves the summed law unchanged.

The fixture nevertheless has no physical distance, causal cone, contact
event, or dynamical notion of separation.  “Pre-contact tick” is therefore
too physical a phrase for this surrogate: there is simply no cross-factor
interaction in the declared evolution.  The exact result is remote-setting
dependence, or parameter dependence, in the natural fixed-factor extension.
Calling it faster-than-light signalling would require a later spacetime
calibration that QSF does not construct.

Carrier availability and event rate are trivial controls here: the Bob carrier
is fixed at 27 cells for both settings and exactly one CELL-HIT is entered per
tick.  Their distributions are identical delta functions.  Bob's pure ray is
not itself counted as a calibrated observable; the count readout supplies the
operational witness.

There is one ontological premise.  The extension must treat Alice outcomes and
Bob CELL-HIT/count facts as actual local events.  If the theory refuses
actualization, it has not produced a communication protocol—but it has also
not produced a complete operational theory.  “No actual outcomes” is
incompleteness, not a no-signalling repair.

## 6. Relabeling and a second mutually unbiased basis

The result is not special to real X phases.  In the same exact number field I
used the Alice projectors

```text
P_+ = 1/2 [[1,  omega^2], [omega,  1]],
P_- = 1/2 [[1, -omega^2], [-omega, 1]].
```

They are orthogonal, sum to the identity, and form another basis mutually
unbiased to Z.  The remote Bob ensemble is

```text
{1/2, (|e0>+omega^2|e1>)/sqrt(2)},
{1/2, (|e0>-omega^2|e1>)/sqrt(2)}.
```

Its density operator is again `rho_B`.  Comparing Z with this phase basis
independently returns

```text
ordered-history TV: 0, 1/2, 211/324
count-record TV:     0, 1/2, 211/324
cell-screen TV:      0, 0,   0.
```

Swapping the two outcomes in any basis gives zero change, as required.
Swapping the names of Alice's two settings reverses the sign of distribution
differences but not their total variation.  These controls support a genuine
decomposition-sensitive effect rather than a label convention.

## 7. Mandatory controls

### 7.1 Remove steering while retaining the density operator

I held Bob's ontic Z ensemble fixed under both Alice setting labels, allowing
only an outcome-name swap.  The Bob density remains `rho_B`, but Alice no
longer remotely changes the ontic ensemble.  History, count-record, and screen
TV are exactly zero at all three registered windows.  Thus the witness is
carried by remote ensemble selection, not by the setting label itself.

This is a control, not the missing relational theory.  To use the frozen
outcome `REMOTE-DECOMPOSITIONS-ONLY-EPISTEMIC`, a successor must construct a
joint ontic law in which this fixed-ensemble statement is true **and** still
reproduce observed steering correlations.  QSF does neither.

### 7.2 Remove Bob's durable history readout

At ticks one through three the ordinary cell screen is identical, so deleting
the count/history readout removes the registered witness.  At tick four hidden
record feedback makes the cell screen differ by `1664/19683`.  Consequently:

- erasing only the readable record is not a permanent cure if the same record
  remains dynamically active; and
- a claim that the signal is operational at tick two specifically depends on
  the count register being a calibrated, readable Bob beable within that
  window.

Absolute record permanence is not needed for a finite protocol, but local
readability before any allowed eraser/contact must be modeled in a physical
successor.

### 7.3 Replace the literal rule by generic affine instruments

The displayed projective measure-and-prepare control returns zero history,
record, and screen TV at all three windows.  I also tested a distinct complete
fixed-output family that prepares a cyclically shifted basis ray after each
outcome.  It likewise returns zero at every grain and window.

The general statement is stronger than either test.  For any Alice-independent
local affine instrument and any Bob history `h`, composition—including
classical feed-forward on prior Bob outcomes—defines one linear CP
trace-nonincreasing map `J_h`.  Therefore

```text
P(h | Alice setting s) = Tr[J_h(rho_B^s)].
```

Since `rho_B^Z=rho_B^X`, every complete history law and every coarse local
readout agrees.  Ancillas do not change the result when the local maps are CP.
This is the correct generic positive control and explains the two exact
fixtures.

The candidate runs only the projective member numerically.  That is adequate
as one control but does not by itself discharge the pin's generic-affine
obligation; the theorem should be rendered and gated.

### 7.4 Attempt a relational composite

WRC supplies one fixed 27-cell carrier.  QSF adds a standard `2 x 27` tensor
factor, but no relational graph for Alice and Bob, no law-generated separation
condition, no carrier-changing successor, no transport of subsystem algebras
through a rewrite, and no definition of “Bob” after factorization changes.

Taking a disjoint union of two fixed carriers and declaring the product law
merely recreates the natural fixed-factor surrogate.  Creating/deleting cells
or shared relations requires new comparison maps and a new joint successor;
those are not inferable from the candidate.  The relational composite is thus

```text
UNPHRASABLE-BECAUSE-COMPOSITE-DYNAMICS-UNBUILT.
```

That word applies to the unbuilt relational arm only.  It cannot be used to
turn the failed natural fixed-factor extension into a no-signalling result.

## 8. Literature guardrail

The construction uses, rather than merely invokes, the content of
Hughston--Jozsa--Wootters, [*A Complete Classification of Quantum Ensembles
Having a Given Density Matrix*](https://doi.org/10.1016/0375-9601(93)90880-9):
the exact Alice projectors remotely realize two ensembles of the same Bob
density operator.

The causality inference is consistent with, but not replaced by, the primary
nonlinear-quantum literature.  Gisin's [1989 stochastic-dynamics
paper](https://www.e-periodica.ch/cntmng?pid=hpa-001%3A1989%3A62%3A%3A1121)
constructs nonlinear pure-state trajectories whose **ensemble** evolution is
a lawful quantum dynamical semigroup, so trajectory nonlinearity alone is not
a signal.  Gisin's [1990
paper](https://doi.org/10.1016/0375-9601(90)90786-N) and Polchinski's [1991 EPR
analysis](https://doi.org/10.1103/PhysRevLett.66.397) show why remote steering
is load-bearing when evolution depends on a decomposition rather than only on
the density operator.  QSF earns its narrower result by explicit finite
distributions; it does not inherit a universal theorem from those papers.

## 9. All-window and all-variable audit

The fixture registers Arm B windows `[1,2,3]`, while the same source process
and Arm C calculation run to tick five.  The fixed-factor surrogate contains
no later contact event, so the DC requirement to test all no-interaction
windows is not met merely by stopping Arm B at three.  The already-computed
five-window table shows continuing history/count differences and ordinary
screen differences at ticks four and five:

| tick | history TV | count TV | screen TV |
|---:|---:|---:|---:|
| 4 | `180223/236196` | `12415/17496` | `1664/19683` |
| 5 | `1694745299/2066242608` | `820725659/1162261467` | `3747023/43046721` |

Those rows should be bound into Arm B rather than left visible only in the
history arm.  A future relational unit must replace “all five algorithmic
ticks” by the physically meaningful requirement “every window before the
first allowed causal contact.”

The Arm B gate currently requires only nonzero **ordered-history** TV.  It
serializes record TV and screen TV but does not gate the calibrated
count-record witness.  The `ontic-history` mutant destroys ordered labels and
kills that gate even though the count record still signals.  This is a test
surface weakness, not a counterexample to the result.  Direct count-record,
event-rate, carrier-availability, and ordinary-screen predicates should be
separate gates.  A Bob-readout mutant should target the count map itself; an
Alice-outcome relabel mutant should prove invariance rather than deleting the
whole setting.

## 10. Scope ruling

The following implications are licensed:

- the literal rule is decomposition-sensitive on the displayed HJW pair;
- the standard fixed-factor ontic extension has remote-setting dependence in
  a calibrated Bob count record;
- the displayed effect survives a second exact mutually unbiased basis and
  common relabelings; and
- affine local instruments do not have this defect.

The following are not licensed:

- every nonlinear stochastic process signals;
- the literal rule signals in every possible composite extension;
- ISP has constructed spacelike separation or violated Lorentz causality;
- unphrasability of a relational composite is safety;
- remote decompositions are merely epistemic in an ISP joint ontology;
- a positive no-signalling theorem for all allowed preparations/instruments;
- dynamic geometry, carrier growth, QFT/GR, actualization, or empirical
  deviations.

The witness rejects one natural completion of the ontology.  It does not
reject the abstract possibility of a different relational composite, but any
such composite now owes both steering reproduction and a general
no-signalling theorem.

## 11. Integrity and mutant audit

I copied only the frozen runtime and its ten hash-bound antecedents to a fresh
`/private/tmp` tree containing no `.git`, invoked the copied scorer from the
alien CWD `/private/tmp`, and reproduced byte-identical artifacts:

```text
transcript ecc8abf7dd17951b262641870ee2ec3748f83bba70434a55354bdad8ff0b78d1
receipt    15f689c2eda69509c5da0f152bf68365cec45c626d2203c699fcda98f92ade4e
paper      cad1925b2f687aff83cc298225dae65931189071ed5397c524d39762c88ff2af
```

The clean run returns 14/14 gates and the sealed payload.  `--selftest`
returns zero.  An unknown argument returns code two.  A second clean invocation
refuses to overwrite.  I then moved only the generated receipt aside and
re-ran; the surviving transcript/paper make the partial-artifact run refuse,
so no silent partial replay occurs.  The receipt was restored unchanged.

I traced all 20 registered mutations to an upstream refusal:

| mutation | refusal surface |
|---|---|
| `anchor-hash` | `QSF-ANCHORS` |
| `fixture-answer` | `QSF-FIXTURE-NEUTRAL` |
| `coin-entry` | walk normalization/regression |
| `shift-orientation` | `QSF-WRC-REGRESSION` |
| `literal-collapse` | `QSF-PACKET-TYPE` |
| `a0-output`, `signature-split` | `QSF-AFFINE-RECURRENCE` |
| `hjw-density` | `QSF-COMPOSITE-HJW` |
| `alice-setting`, `ontic-history` | `QSF-NATURAL-COMPOSITE-WITNESS` |
| `affine-control` | `QSF-AFFINE-CONTROLS` |
| `record-retention`, `history-window` | `QSF-HISTORY-BOUNDARIES` |
| `predictive-merge` | `QSF-S1A` |
| `s1b-entry` | `QSF-S1B-DISPOSITION` |
| `scope-promotion` | `QSF-SCOPE` |
| `primary-comparator` | `QSF-PRIMARY-COMPARATOR` |
| `exactness` | `QSF-EXACTNESS` |
| `transcript-seal` | `QSF-TRANSCRIPT-SEAL` |
| `paper-claim` | `QSF-PAPER-CLAIM` |

The main routine performs no artifact write until all scientific, transcript,
and paper checks have passed, so each refusal is no-write by construction.
The registered set is effective against its named claims.  It is incomplete
at the causality seam in the two ways identified above: no pure outcome-label
invariance mutant, and no count-readout mutant independent of ordered-history
labels.

The chronology is also clean at the level claimed.  The generic core was
frozen before the physical fixture and contains no WRC dimension, matrix,
target, or verdict.  The fixture was frozen before the scorer and contains no
answer-bearing key.  The public HJW/nonlinearity assay is calibration evidence,
not a prediction of WRC's physical numbers.

## 12. Numbered repairs and kill conditions

1. **KEEP the candidate synthesis `QSF-METHOD-INCONCLUSIVE`.**  Render Arm B
   with the fixed-factor/count-record/relational-unbuilt qualifiers above.
2. **GATE the count-record witness directly.**  Require exact TV
   `0,1/2,211/324` independently of ordered-history labels.  Kill condition:
   if the declared Bob count readout is setting-independent after Alice
   outcomes are summed, the registered operational witness fails even if an
   inaccessible ray decomposition differs.
3. **ADD the exact phase-MUB and outcome-relabel controls.**  Bind completeness,
   common `rho_B`, conditional ensembles, and invariant TV.  A label swap may
   not create or erase the verdict.
4. **RENDER and gate the generic affine theorem.**  The projective control is
   one example.  Add a second non-projective/fixed-output member and the
   history-map linearity proof covering arbitrary CP local instruments,
   ancillas, and Bob outcome feed-forward.
5. **SEPARATE “remove readout” from “remove feedback.”**  The former hides the
   tick-two record signal but an ordinary screen moves at tick four; the latter
   gives the affine/unitary null.  Do not call either control more general than
   it is.
6. **EXTEND Arm B through every available no-interaction window.**  Bind the
   already-computed tick-four and tick-five history, count, and screen rows.
   In a future relational composite, pre-register a physical first-contact
   event and test every earlier window.
7. **ADD all-variable causal rows.**  State explicitly that carrier
   availability and event rate are identical delta laws on this fixed fixture;
   do not count the ontic ray as an observable.  Give each calibrated Bob
   readout its own gate and upstream mutant.
8. **NARROW causal language.**  Use “remote-setting dependence in a
   no-interaction fixed-factor surrogate.”  Reserve “superluminal” or Lorentz
   violation for a constructed separation geometry and causal cone.
9. **KEEP actualization explicit.**  The signal rejects the natural extension
   only when Alice outcomes and Bob count facts are physical.  Refusing
   actualization returns `INCOMPLETE`, not `SAFE`.
10. **DO NOT promote relational unphrasability.**  A successor must construct
    the composite state, changing subsystem algebras, separation condition,
    steering implementation, and all-input no-signalling theorem.  Kill
    condition for an ontic successor: one remotely controllable Bob marginal
    movement at any calibrated grain/window.
11. **ADD causality-specific mutants.**  One must only relabel Alice outcomes;
    one must erase/alter Bob's count-readout map while leaving ontic histories
    intact; one must mutate the tick-four screen row.  The existing
    `alice-setting` and `ontic-history` mutations do not cover these claims.
12. **PRESERVE the broad scope wall.**  This fixed-factor witness neither
    constructs nor refutes a relational growth law, dynamic geometry,
    continuum/Lorentz structure, QFT/GR, particles/species, Hamiltonian
    selection, constants, or deviations.

## 13. Report SHA-256

Normalized report SHA-256:
`0a206f1775f595e622332c17180bad0ac701d219c2533efd4cbcbc6883794786`.

The normalized digest is computed with the 64 hexadecimal characters in the
preceding field replaced by 64 zeroes.  The ordinary SHA-256 of the final file
bytes is reported separately to the panel coordinator because embedding that
digest would change the bytes being digested.
