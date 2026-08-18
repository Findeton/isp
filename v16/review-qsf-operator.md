# QSF Paper 9 hostile review — Seat O: operator, instrument, and completion family

**Date:** 2026-08-18

**Seat:** O only. I did not read, list, request, or infer either sibling QSF
report.

**Grade:** `ACCEPT-WITH-FIXES`.

**Proposed primary:** `QSF-METHOD-INCONCLUSIVE`.

The conservative synthesis survives, but Arm A needs a material typing repair.
Under the pin's literal notation, one output state per `(record n, outcome c)`
does **not** interpolate the reached process: two reached histories have the
same complete count record and the same next outcome with nonzero probability,
yet demand different output rays. If “context” is enlarged to include that
ray or the ordered history, the interpolation becomes tautologically exact but
is not one affine law on density operators. The paper understands the second
point informally; the scorer does not measure either point and instead writes
the A0 and aggregate-family dispositions as literals.

The exact rank-one completion theorem, the 0/9 projective regression, the
fitted one-input control, and the local branch-level obstruction all survive
independent reconstruction. Branch obstruction remains logically distinct
from aggregate feasibility. I exhibit an exact aggregate match with branch
mismatch and prove that the delivered method cannot close the A1/A2 aggregate
question because it constructs no output-state variables, positivity cone,
mixed-state propagation, aggregate equations, or quotient.

## 1. Frozen object and authentication

I reviewed these immutable candidate bytes:

| artifact | SHA-256 |
|---|---|
| `v16/code/qsf_core.py` | `6dd6b4999c0474a362f56bb70271845fb5f322c6676a4de90c79b64ce753736f` |
| `v16/code/qsf_fixture.json` | `7fe949383d1e27017b972f941c4cf1875d3c574d3120d9993240bd7a0756404f` |
| `v16/code/qsf_score.py` | `e5cebe8f40760277942d325b1cd257108c20c323e8a5d05b4c86d878471077bf` |
| `v16/code/qsf_output.txt` | `ecc8abf7dd17951b262641870ee2ec3748f83bba70434a55354bdad8ff0b78d1` |
| `v16/code/qsf_receipt.json` | `15f689c2eda69509c5da0f152bf68365cec45c626d2203c699fcda98f92ade4e` |
| `v16/paper-09-quantum-seam.md` | `cad1925b2f687aff83cc298225dae65931189071ed5397c524d39762c88ff2af` |
| `v16/note-qsf-hostile-protocol.md` | `90ee36c402baf96e783742212aa5f61f2dbd2414576a09b1656bd7f3501002d9` |

My exact scratch reconstructions imported no QSF executable. They used my own
independent `Q(omega)` walk algebra. Their hashes are:

| scratch evidence | SHA-256 |
|---|---|
| `/private/tmp/qsf_operator_independent.py` | `f3b17ba980838a76c304f976106daa7b9ca06cbb94cbeef163aac3d35d517eac` |
| `/private/tmp/qsf_collision_witness.py` | `9748a745e4b3ecc8706eaf2e1dbf05ef9bbb6da24e54983a7f2644523140751d` |

The scratch files are receipts for this review, not corpus artifacts.

## 2. Rank-one affine-completion theorem

Let `J` be a CP operation with Kraus operators `K_r` and effect

```text
J*(I) = sum_r K_r^dagger K_r = E = |e><e|,
```

where `e` is normalized and `E` has rank one. For every `x` in `ker E`,

```text
0 = <x|E|x> = sum_r ||K_r x||^2,
```

so every `K_r x` vanishes. Hence each Kraus operator factors as
`K_r=|v_r><e|`, and therefore

```text
J(rho) = Tr(E rho) sigma,
sigma = sum_r |v_r><v_r| >= 0.
```

The prescribed effect is exactly `E` iff `Tr sigma=1`. Conversely every
normalized positive `sigma` gives such a CP operation; its Choi matrix is
`E^T tensor sigma >= 0`. For an orthogonal rank-one effect family
`sum_c E_c=I`, arbitrary normalized choices `sigma_c` give

```text
sum_c Tr J_c(rho) = Tr rho,
```

so the instrument is trace preserving. This proves the WRC/QSF normal form,
positivity, CP, and completeness without privileging a Kraus factorization.

It also identifies the exact obstruction. One fixed affine operation at a
fixed classical law context cannot return two different normalized states for
the same nonzero rank-one outcome. Any selector that chooses `sigma` from the
input ray is outside this affine map.

## 3. Independent walk and the two registered controls

I rebuilt the nine-site, three-link, 27-cell walk directly over `Q(omega)`.
The literal branch counts are

```text
3, 27, 486, 10527, 284078,
```

and all nine sealed WRC families match the candidate exactly. The displayed
projective completion instead gives branch counts

```text
3, 9, 27, 81, 243
```

and preserves zero of nine families. Representative exact movements are:

```text
exit probability:       927415552/847288609443 -> 0
curvature probability:  7598838656/22876792454961 -> 0
maximum count:           4 -> 3
IPR: 35971074413334039128803/239299329230617529590083
     -> 6454657/43046721
determinant set: {0,1,2,3,3/4,7/4} -> {1,3/4,7/4}.
```

The site mass, emission field, link marginal, and positive-site distribution
also all move, independently reproducing the candidate's 0/9 vector.

For the fitted control, the 27 effect vectors form an orthonormal basis, every
chosen output is normalized, and the complete instrument has total effect
`I`. At the registered input and outcome zero it has probability `9/25` and
matches the literal conditioned state exactly. It fails on a second nonzero
input, as the theorem requires. The displayed projective continuation moves
cells `3,4,5,9,10,11`; this is one completion comparison, not a family theorem.

An additional exact completion outside both controls is

```text
sigma_c = |S(c+1 mod 27)><S(c+1 mod 27)|.
```

With `K_c=|S(c+1)><e_c|`, every operation is CP, the total is TP, and its
output differs from the projective completion for all 27 outcomes. Thus the
controls correctly demonstrate nonselection but do not census the family.

## 4. A0 is either false at record grain or not an affine law

The pin writes A0 as one `sigma_(n,c)` per reached record context `n` and
outcome `c`. I found a direct mandatory collision at past depth three:

```text
ordered histories:  (0,12,13) and (0,13,12)
common record:       entries 0,12,13 equal 2; all others equal 1
common next outcome: c=0
both probabilities: 19/2187.
```

The demanded normalized output rays differ. With the first nonzero coordinate
normalized to one, coordinate 2 is respectively

```text
11/3 - (2/3) omega    and    8/3 + (1/3) omega.
```

Therefore no fixed `sigma_(n,0)` reproduces both branches. Across the complete
registered census I found 4,080 full-record keys carrying more than one ray
(maximum four), and 109,986 `(full record, next cell)` keys carrying more than
one demanded ray (maximum four). The explicit witness, rather than those
large counts, is the load-bearing result.

There are only two coherent readings:

1. If A0 means one map per count record and outcome, `a0_context_exact=true`
   is refuted.
2. If A0 means one map per `(ray, record, ordered history, outcome)`, exact fit
   is tautological, but the map-selector depends on the state it is supposed
   to act on. It is a finite ontic-state lookup, not one affine operation on
   the convex density-state domain.

The paper nearly says this by calling A0 an interpolation table. It must also
repair the formula and stop using A0 as a positive affine-base coordinate.

## 5. The local branch obstruction survives, with a covariance caveat

My independent raw census exactly reproduces:

```text
contexts                  11044
nonzero alternatives      295121
declared signatures       30
conflicting signatures    30
maximum rays/signature    8861.
```

This proves failure of literal branch reproduction for the scorer's raw
dictionary. But raw global output rays at different sites are not the correct
comparison for a relabeling-natural A2 law; outputs must be transported to a
common frame. The delivered scorer does not perform that transport.

The obstruction is nevertheless real. Two stricter independent checks give:

```text
same absolute site + local residues + link:
    261 conflicting keys of 264; maximum 6756 rays
translation-align event site to the origin before comparing:
    30 conflicting keys of 30; maximum 48154 rays.
```

Thus a repaired, transported census still kills literal branch-exact descent.
The candidate's specific `30/8861` row should be described as the raw A1
dictionary result, while A2 requires the aligned gate. “A1 and hence A2” is
licensed only after the two family definitions and their inclusion map are
made coordinate-covariant.

## 6. Branch mismatch does not decide aggregate feasibility

I constructed the protocol's required aggregate-match/branch-mismatch mutant.
At the terminal tick, replace every context-indexed literal output `phi` by

```text
D phi,   D = diag(omega,1,...,1),
```

while leaving effects and record writes unchanged. Each context-indexed
outcome operation still has the rank-one CP form. The output ray moves in all
10,527 terminal input contexts, but `D` preserves every basis probability.
Consequently branch counts and all nine terminal observable families are
byte-for-byte equal to the literal packet.

This is not an A1/A2 solution: it remains a state/context-indexed A0 lookup.
It is a decisive logical control showing that failure of exact conditioned-ray
descent does not imply failure of the aggregate packet.

Nor does the current program attempt the remaining aggregate problem. It
creates no variables `sigma_s`, no Choi or density matrices for A1/A2, no PSD
constraints, no mixed-state successor, no recurrence/covariance equations, no
aggregate target equations, and no operational-null quotient or solver. It
simply assigns:

```text
aggregate_variety_closed = False
a1_exact_branch_reproduction = False
a2_exact_branch_reproduction = False.
```

At repeated uses, aggregate constraints are polynomial in output-state
entries, with PSD and trace constraints. The object is generally a
PSD-constrained semialgebraic set, not merely a linear SDP. The collision
census contains insufficient information to decide whether this set is empty.
This is a proof of method nonclosure, not a proof of aggregate infeasibility.
The candidate's `METHOD-INCONCLUSIVE` wording is therefore correct.

## 7. Dimension and operational-null audit

The real affine dimension of one unconstrained 27-dimensional density state
is `27^2-1=728`; the independent 27-outcome family at one fixed context has
dimension `27*728=19656` before recurrence or data constraints. Exact rational
pure outputs `(1,0)`, `(3/5,4/5)`, and `(5/13,12/13)` already give three
distinct complete members in one two-coordinate slice.

If the branch grain fixes the normalized output density matrix for every
nonzero reached occurrence, the operational CP map on **those named rows** is
unique, so dimension zero is defensible after quotienting Kraus/unravelling
gauge. It is not the dimension of a global affine law: unreachable contexts,
off-window rows, and recurrence remain unparameterized. At the nine-observable
aggregate grain, the terminal phase construction supplies an explicit
nontrivial null family. Thus the paper's carefully qualified “reached exact-fit
dimension zero; off-window null uncounted” may survive only after A0 is retyped
as a branch lookup and the quotient is stated. The scorer currently measures
none of this.

## 8. Pipeline and antecedent audit

The clean source regression has a complete preparation-to-walk-to-record/state
to-calibrated-output lineage. The projective and fitted controls also change an
upstream operation and derive their screens. In contrast, A0 exactness,
aggregate nonclosure, both A1/A2 Boolean dispositions, S1b non-entry, and the
synthesis comparator share answer-bearing scorer literals. The `a0-output`
mutant changes the census horizon; it never mutates or validates an A0 output
operation. This repeats the hard-coded-doctrine failure that RUNBOOK E-36 was
written to prevent. Fixture neutrality alone does not cure answer literals in
the executable.

QSF does not improperly cite unsealed SCOUT-T. The pin explicitly dispositions
it as unsealed evidence, absorbs its question through tracked JS-S1a, and the
paper reports a finite two-axis predictive census. S1b is appropriately not
executed while the family is unclosed, but after repair that non-entry must be
derived from a declared method-state object rather than the literal Boolean
above.

The fixed matrices do recursively generate reached histories; they are not a
prelisted history table. They remain imported, fixed-carrier dynamics, not a
generator of changing relational carriers. QSF makes no geometry claim and
retains the relevant walls. Per E-37, nothing here establishes geometry as a
sufficient statistic, let alone a load-bearing ontology under resource parity
and held-out family scaling.

## 9. Integrity audit

- A clean replay to absent temporary targets reproduced the frozen transcript,
  receipt, and paper hashes exactly.
- All 20 registered mutants were executed. Every mutant returned nonzero and
  wrote zero artifacts. The refusals hit their named gate or seal.
- An unknown argument returned argparse status 2.
- Reusing any existing target returned status 1 with `refusing to overwrite an
  existing artifact`; all three hashes remained unchanged.
- Removing the bound public-core receipt in an isolated copy produced an
  anchor row with `observed: null`, returned status 1, and wrote no targets.
- A true off-tree copy containing no `.git`, invoked by absolute path from the
  alien CWD `/private/tmp`, reproduced all three frozen artifact hashes exactly.
- Atomic write, transcript, paper, exactness, primary-comparator, and anchor
  mutants all refused before publication.

The scorer's operational integrity surface is strong. The scientific weakness
is not a seal failure; it is that several Arm-A scientific dispositions are
not computations at all.

## 10. Numbered repair and kill list

1. **REPAIR — type A0 literally.** Replace the ambiguous `n` by either the
   full classical law context or the full `(ray,record,history)` lookup key.
   Record-indexed A0 is killed by the explicit `(0,12,13)/(0,13,12)` witness;
   state-indexed A0 must be called interpolation, not an affine law.
2. **REPAIR — remove answer-bearing Arm-A literals.** Construct and gate the A0
   operations, their CP/TP properties, and the exact branch comparison. Replace
   `aggregate_variety_closed=False` by a derived method-status object.
3. **REPAIR — align covariance.** Transport outputs into a common local frame
   before using recurrence collisions against A2. Bind the same-site and
   translation-aligned controls or equivalent exact certificates.
4. **REPAIR — separate grains.** Keep branch-exact infeasibility distinct from
   nine-packet feasibility in the data model, gates, receipt, and prose. Add
   the terminal-phase aggregate-match/branch-mismatch mutant.
5. **REPAIR — parameterize the aggregate question or name non-entry.** To close
   it, introduce PSD trace-one output variables, mixed-state propagation,
   recurrence/covariance equations, all nine aggregate constraints, and the
   operational-null quotient. Otherwise retain `METHOD-INCONCLUSIVE` and do
   not call the unconstructed object a measured variety.
6. **REPAIR — state the dimension quotient.** Keep dimension zero only for
   branch-fixed operational maps on named reached rows, modulo Kraus gauge.
   Report the `728`-per-output ambient dimension and the explicit aggregate
   null family separately.
7. **REPAIR — strengthen family controls.** Add the cyclic completion or an
   equivalent third member so the control surface directly demonstrates the
   normal-form family rather than two selected points.
8. **REPAIR — rebuild synthesis independently.** Derive the primary from
   measured arm objects rather than hard-coded A0/aggregate booleans shared by
   the builder and comparator.
9. **KILL CONDITION — affine branch law.** Kill any record-indexed or
   signature-indexed exact affine completion if the same classical key and
   outcome require two different normalized states with nonzero probability.
   The record-indexed and registered local versions are killed here.
10. **KILL CONDITION — aggregate no-go.** Do not emit no-completion at A1/A2
    unless the full PSD-constrained aggregate set is certified empty. No such
    certificate exists in this candidate.
11. **KILL CONDITION — selected affine base.** Do not promote an affine base
    until an A2 survivor is selected or all survivors are proven empirically
    equivalent under the registered continuations. QSF correctly does not
    promote one.
12. **KILL CONDITION — primary.** Kill `QSF-METHOD-INCONCLUSIVE` only if a
    branch earns a positive selected/viable theorem or every registered base
    is decisively refused. Neither condition is established, so the proposed
    primary remains the conservative result.

## 11. Report checksum

Normalized/self convention: hash the UTF-8 bytes of this report after replacing
the value on the next line by the literal token `<NORMALIZED-SELF-SHA256>`.

Normalized/self SHA-256: `0bc88f69b2bd79799bdb092d1c4c2c1b9a7bd543ce29e4af4b0f94eccec16502`

The ordinary whole-file SHA-256 is necessarily reported out of band in the
freeze dispatch, because embedding it would change the file being hashed.
