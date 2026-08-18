# JCV hostile review — operator, instrument, and ontology seat

Status: **INDEPENDENT REPORT FROZEN FOR PANEL ADJUDICATION**.

Immutable review target: `35c2511657efbee6c1c1887f2d7626faa4d396ea`.

Grade: **ACCEPT-WITH-FIXES**.

## Executive verdict

The exact finite primary survives this seat.  Independently of the physical
scorer, I recover 16 chart-sign gauge orbits, 7 nonempty shared-law sectors,
one two-dimensional active sector, 6 one-dimensional dark sectors, 9
independent-triangle control sectors, and the 2 control-only mixed-handoff
sectors.  The two displayed rational active witnesses obey every equation and
give the reported outcome-zero probabilities `0` and `49/625`.  There are
**zero numerical discrepancies** with the frozen receipt.

The boundary object is a valid quantum instrument on the declared fixed
two-dimensional interface.  Each branch is completely positive, and the two
polynomial completeness equations are exactly the coefficients of the
all-input operator identity.  This licenses a fixed-boundary, outcome-resolved
CPTP statement.  It does not license a changing-carrier no-signalling theorem,
an EPR composite dynamics, a Hamiltonian, geometry, backreaction,
actualization, particles, species, or an all-arity law.  The paper's consequence
wall correctly refuses or leaves open all of those promotions.

The fixes are interpretive and certificate-strengthening, not a primary
demotion.  Most importantly, the two published active witnesses vary the
outcome **unravelling** of the same unconditioned channel.  They still define
operationally distinct instruments because the outcome register is declared
physical, so the registered primary follows.  But the paper should say this
instead of letting “physical weight freedom” sound like demonstrated movement
of the unconditioned dynamics or a derived ontic history decomposition.  The
active family also contains a direction that really changes the unconditioned
channel, and one exact witness for it is given below.

## Independence, read set, and tools

I did not read, list, or receive any other JCV reviewer report.  I derived the
gauge quotient, sector conditions, dimensions, witnesses, and operator form
directly from the frozen fixture before inspecting the corresponding scorer
branches.  I did not import or execute `jcv_score.py` or use it as an oracle.

Content read:

- `v16/note-jcv-hostile-protocol.md`;
- `v16/code/jcv_fixture.json`, `v16/code/jcv_receipt.json`, and
  `v16/code/jcv_output.txt`;
- `v16/paper-02-joint-comparison-fixed-point.md`;
- `v16/note-jcv-pin.md`, `v16/note-jcv-solver-freeze.md`,
  `v16/note-jcv-solver-postcommit.md`, `v16/note-jcv-fixture-freeze.md`,
  `v16/note-jcv-official-run-failure.md`, `v16/note-jcv-scorer-repair.md`,
  and `v16/note-jcv-postcommit-verification.md`;
- `v16/code/jcv_score.py`, inspected only after the independent reconstruction;
- `v16/paper-01-joint-relational-history-law.md`,
  `v16/note-jrh-delta-adjudication.md`, and
  `v16/note-jrh-terminal-verification.md`;
- `v12/paper1-composition-defect.md`, specifically the record definition,
  Theorems 4.1--4.3, and the cited division-event paragraph;
- `v14/paper-38-epr.md`;
- `v15/note-scoutpsi.md`, `v15/note-dc-causality-addendum-v2.md`,
  `v15/note-dc-ontology-addendum-v3.md`, and `v15/paper-43-contract.md`.

Provenance-only byte checks also read the frozen and repaired scorer/fixture
blobs at commits `ee8e414`, `b0c0d24`, and `c561acc`; the substantive source
diff is reproduced below.  No unrelated SCOUT-T path was read.

Tools/runtime:

- Python `3.13.5`, standard library only (`fractions`, `itertools`, `json`,
  `hashlib`, and `pathlib`) for independent exact checks;
- exact hand-derived `Q(sqrt(2))` matrix arithmetic implemented independently
  in a no-write command;
- Git `2.50.1` for immutable-tree and source-delta inspection;
- `shasum` `6.02` for SHA-256.

## Artifact and total-seal audit

All five protocol hashes match:

| artifact | observed SHA-256 | match |
|---|---|---|
| fixture | `ad887c213d14781838c6e70227b8f2c162f1392a08060de7c6e57829a8db012b` | yes |
| scorer | `66b87bdf68f7210d959e13bfacae4c5957413e6d8f234647bfe3ad4a19619a03` | yes |
| paper | `b54858c394fe22626ef1e233781737b7199cc56bf816f52e8aae063a99deaefc` | yes |
| transcript | `b1d950c804c8b568514f1a0206853496b2f578650a3d98187e64c1c8a9b70d6d` | yes |
| receipt | `a1b0baeee418d3f2c82e1ec6d07993cb51f69f3f51d63a9996dae9fb177fe3d1` | yes |

I independently canonicalized every non-manifest top-level receipt value and
recomputed its digest.  All 17 of 17 sealed keys match, the top-level payload
has exactly the declared 17 keys excluding the manifest, and the fixture,
scorer, paper, and transcript cross-hashes match their bytes.  Seal
discrepancies: **0**.

## Independent exact reconstruction

### Comparison maps and gauge quotient

Let `E_Z=I` and `E_X=H`, with the exactly normalized Hadamard matrix over
`Q(sqrt(2))`.  An edge comparison is

`P_ij = E_j diag(s_+,s_-) E_i^T`.

For each of the 5 edges and all 4 sign pairs, independent exact arithmetic
gives `P_ij^T P_ij=I` and `P_ij O_i=O_j P_ij`: 40 checks, 0 failures.  For
all 1024 raw sign assignments, path equality versus direct equality at both
triangles agrees with the two channel holonomies: 2048 checks, 0 failures.

An independent sign `t_i^+` and `t_i^-` at each of the four charts acts on an
edge sign as `s_ij^c -> t_i^c s_ij^c t_j^c`.  Each channel is a connected
five-edge/four-vertex graph of cycle rank two.  Its vertex-sign action has one
global stabilizer and orbit size 8.  The two-channel orbit size is therefore
64.  Direct enumeration gives `1024/64=16` orbits, all four-bit holonomy keys
occur, and exactly one orbit has each key.  Orbit discrepancies: **0**.

The four invariants are exactly

`q=(ace,bdf,cgj,dhk)`.

For every raw assignment,

`ac-e=e(q012+ -1)`, `bd-f=f(q012- -1)`,

`cg-j=j(q123+ -1)`, `dh-k=k(q123- -1)`.

These are 4096 raw channel identities, with 0 failures.

### Shared-law and control sectors

Write the holonomy key as `(q1,q2,q3,q4)`.  The plus column `(x,u)` can be
nonzero exactly when `q1=q3=1`; otherwise both entries are forced to zero.
The minus column `(y,v)` can be nonzero exactly when `q2=q4=1`; otherwise
both entries are forced to zero.  Normalization requires at least one live
column.  Hence the shared-law variety is nonempty exactly when

`(q1=q3=1) OR (q2=q4=1)`.

This gives 7 sectors.  If exactly one column is live, the variety is a circle,
for example `y=v=0` and `x^2+u^2=1`, so its algebraic dimension is 1.  There
are 6 such sectors.  If both columns are live, the only key is `(1,1,1,1)`
and the two independent equations in four variables give dimension 2.  Its
real active open subset is nonempty.  These dimensions and keys agree with
every receipt row.

With independent weights at the two triangles, each local triangle is
nonempty unless both of its channel holonomies are `-1`.  Thus `3*3=9`
control sectors survive.  Their dimensions are the sums of the two local
dimensions: four sectors of dimension 2, four of dimension 3, and one of
dimension 4.  The two control-only keys are exactly

`(-1,1,1,-1)` and `(1,-1,-1,1)`.

They are the mixed handoffs.  This verifies the finite price of the declared
shared-law homogeneity; it does not derive that homogeneity.

### Active witnesses and moving probability

For the two frozen active witnesses, in `(x,y,u,v)` order,

`w1=(12/25,-12/25,16/25,9/25)`,

`w2=(16/25,-9/25,12/25,12/25)`.

Both obey

`x^2+y^2+u^2+v^2=1`, `xy+uv=0`,

`Delta=xv-yu=12/25`, and

`Delta*x*y=-1728/15625 != 0`.

Their registered outcome-zero probabilities on the calibrated plus input are
respectively `0` and `49/625`.  Every reported residual is zero.

There is an operator-level qualification.  Both witnesses have

`r^2=x^2+u^2=16/25`, `s^2=y^2+v^2=9/25`.

Consequently they induce the same unconditioned channel and differ in how its
Kraus operators are resolved into the two durable outcomes.  This remains an
operational difference for a calibrated outcome-resolved instrument, but it
is not evidence that the unconditioned transfer moved.

The active variety also contains exact movement of that transfer.  For
example

`w3=(3/13,-48/65,4/13,36/65)`

obeys the same two completeness equations, has
`Delta=60/169` and `Delta*x*y != 0`, while its unconditioned coherence
eigenvalue is `lambda=-119/169`, versus `lambda=7/25` at `w1,w2`.  Thus the
positive-dimensional weight freedom survives even if one quotients ordinary
Kraus-unravelling freedom; this stronger discriminator simply was not one of
the frozen registered observables.

### Frozen classifier

The frozen decision table is mechanical.  The measured summary is

`nonempty=7`, `active=1`, `dark=6`, `active_max_dimension=2`, and
`observable_moves=true`.

The core branch therefore returns
`JCV-PAIRING-SELECTED-WEIGHTS-FREE`.  Because an active sector and dark
sectors both exist, the compound branch returns `JCV-STRATIFIED`.  Neither
word is imported from the paper prose.  Classifier discrepancies: **0**.

## Operator and instrument audit

Define

`K0=x I+y Z`, `K1=u I+v Z`.

Then, for real coefficients,

`K0^dagger K0+K1^dagger K1`

`=(x^2+y^2+u^2+v^2) I + 2(xy+uv) Z`.

The two fixture equations therefore imply the identity operator for every
point of the solution variety, not only for the eight witness rows.  Each
outcome map `rho -> Ki rho Ki^dagger` is completely positive at every ancilla
dimension.  Appending an orthogonal classical outcome register gives Kraus
operators `Li=|i> tensor Ki`; their adjoint sum is `I`, so the complete
outcome-record channel is CPTP for all inputs and all ancillas.  Each branch
is trace nonincreasing because its positive effect is bounded by their sum.

The scorer's `P-INSTRUMENT` numerical subcheck exercises the two calibrated
eigenstates at eight witnesses.  That is enough for each displayed diagonal
two-level witness, but the solution-wide all-input certificate actually comes
from the frozen polynomial equations plus the symbolic operator identity
above.  The paper is mathematically correct; a future gate should compute and
seal that symbolic identity instead of storing its coefficients only as
strings.

The sample-space typing is coherent.  Rows are mutually exclusive outcome
records.  Columns are amplitude contributions inside each row and are summed
before squaring.  `p_plus` and `p_minus` are not complementary outcomes; they
are the probability of outcome 0 on two different calibrated input states.
The branch/output distinction is maintained.

The six dark sectors are genuinely rank deficient at this fixture.  In each,
one whole column of `W` is zero and the other has norm one, so `rank(W)=1`,
`Delta=0`, and `xy=0`.  The comparison mismatch occurs only in the zero
column and therefore changes no `Ki` or probability for any boundary input.
It is silent for this one-step instrument.  Nothing here proves that the same
mismatch stays silent under a future law that repopulates the channel.

### What the active family actually parameterizes

On a full-rank real component the two column vectors are orthogonal.  Up to a
discrete orientation they can be written

`(x,u)=r(cos theta,sin theta)`,

`(y,v)=s(-sin theta,cos theta)`, with `r^2+s^2=1`.

The unconditioned map is

`E(rho)=sum_i Ki rho Ki^dagger = r^2 rho+s^2 Z rho Z`.

Thus one continuous coordinate changes a dephasing/phase-flip channel, while
the other changes its outcome-resolved Kraus unravelling.  The latter is
physical only because the fixture declares and calibrates a durable outcome
register.  This decomposition is the clean operator meaning of “dimension
two”; it should be stated in the paper.

The term “internal interference” is also conditional.  The cross term `4xy`
distinguishes the coherent sum `xI+yZ` from an incoherent mixture **given the
declared I/Z history-column decomposition**.  Process data alone do not prove
that those two operator summands are ontically distinct carrier histories; a
single diagonal Kraus operation realizes the same boundary map.  The paper
does acknowledge that the comparison doctrine is postulated, so this is a
wording repair rather than a false calculation.

## Ontology and consequence wall

### Comparison, law, and records

The comparison maps have earned the status of exact calibrated coordinate
dictionaries.  They have not earned an ontic cross-carrier referent: the
fixture contains no graph rewrite, carrier transport, or record-generated
identification.  The paper correctly calls them representational and the
doctrine postulated.

`W` is candidate nomological data for this boundary instrument.  Because a
continuous family survives, it is not a selected law.  It is still further
from the complete successor law `(relations, geometry, process state) -> ...`.

An orthogonal classical output flag can be appended to the instrument, but
“durable” additionally requires preservation and availability under licensed
future continuations.  No such continuation exists here.  The flag's record
status is therefore a declared interface type, not a derived permanence
theorem.  The probability law likewise does not make one outcome actual.
Actualization remains a separate postulate exactly as the paper says.

### Fixed boundary, EPR, and no-signalling

The JCV instrument is affine in `rho`.  Equal ensemble decompositions of one
density matrix therefore give the same complete outcome-record state at this
boundary, unlike the decomposition-sensitive SCOUT-PSI rule.  If this map is
declared local on one factor `A` of a fixed `A tensor B`, then summing its
outcomes leaves Bob's reduced state unchanged: fixed-factor no-signalling
follows from trace preservation.

JCV itself supplies no `A tensor B`, relational separation predicate,
entangled preparation, steering intervention, changing output factorization,
or sector embeddings.  It therefore cannot discharge the standing DC
bipartite-causality obligation, cannot turn paper 38's reading-zero into an
intervention theorem, and cannot establish no-signalling for back-reacting
locality.  The paper's `OPEN` row is correct.

### Hamiltonian and generator

The unconditioned channel above is generically nonunitary.  It can be written
as a phase-flip/dephasing channel, but a single discrete channel supplies no
clock duration and selects neither a Lindblad rate nor a dilation.  Some
parameter values admit many semigroup embeddings; negative coherence factors
require an additional unitary choice or a more general time dependence; a
zero coherence factor is noninvertible and is not a finite-time bounded
homogeneous generator image.  The outcome-resolved instrument carries still
more unravelling data.  No system Hamiltonian is reconstructed, and a larger
unitary dilation would add environment, clock, and embedding choices.  The
Hamiltonian `OPEN` wall is exact.

### Particles, species, arity, and phenomenology

The two coherent columns are not two particles, the four charts are not four
actors, and the two triangles are not an interaction-arity theorem.  There is
no vacuum, spectrum, representation of permutations or braids, scattering
map, stable excitation sector, regional all-`n` composition, or refinement
fixed point.  No species or interaction list follows.

Likewise there is no metric, source, relation rewrite, scale, gravitational
constraint, affine/cosmological value, continuum map, or typed comparison
observable against QFT/GR.  Every positive promotion on those topics is
properly refused.  Consequence-wall discrepancies: **0**.

## First-run failure and serializer repair

The immutable history supports the repair record:

- at the fixture freeze and failed-run record, the scorer hash is
  `768c4bbc...` and the fixture hash is unchanged;
- neither the failure-record commit `b0c0d24` nor the repair-freeze commit
  `c561acc` contains a physical paper, transcript, or receipt;
- the entire scorer delta from `ee8e414` to `c561acc` is one three-line branch
  that recursively serializes sets/frozensets and orders their serialized
  values by canonical JSON;
- the repaired scorer hash is the frozen `66b87bdf...`; no fixture equation,
  witness generator, classifier, wall, renderer, or promotion rule moved.

One chronology phrase needs precision.  The first attempt's clean `run_core`
and paper rendering occurred in memory before the mutation survey reached the
set serializer.  Thus the failure was not literally before all physical
calculation.  It was before any classifier word or physical numeral was
printed, written, or promoted; the traceback disclosed only the set-type
exception.  I find no evidence that the repair author saw a result before the
refreeze and no channel by which the three-line serializer change could move
physical truth.  Result-leakage discrepancies: **0**.  The failure note should
say “before result disclosure or promotion,” not be read as “before internal
calculation.”

## Sentences stronger than their certificates

I find no geometry, backreaction, EPR, Hamiltonian, species, constant, or
phenomenology promotion.  The following are the complete residual scope
overstatements in the candidate paper:

1. Line 17, “dynamical weights,” is stronger than the object constructed.
   These are boundary-instrument/history coefficients; no dynamical successor
   or repeated process is built.
2. Line 29, “A durable outcome flag is ontic record content,” omits that
   durability and onticity are declared interface typing.  Future permanence
   and objective actualization are not certified.
3. Lines 50--51 and 63--66, “internal coherent response,” “coherent history
   channel,” and “dynamically silent,” are valid only relative to the declared
   I/Z history decomposition and this one-step instrument.  The boundary
   channel alone does not identify ontic histories or future silence.
4. Lines 58--60, “physical weight freedom,” should say
   “outcome-resolved instrument freedom within the declared calibrated record
   basis.”  The two displayed witnesses have the same unconditioned channel.
5. Lines 78--81, “selects the coherent holonomy class,” is correct only on the
   explicitly registered nonzero locus and inside the postulated comparison
   doctrine.  The surrounding qualifiers mostly supply this scope; the
   conclusion sentence should retain them locally.
6. Lines 87--88 and the title call the result a “fixed point,” but no
   self-map whose fixed point is being solved is defined.  The exact object is
   a joint constraint/solution locus.  “Fixed point” should remain reserved
   for the future record-generated comparison law unless a self-consistency
   map is written.
7. Line 131, “the deepest circularity has been narrowed,” is an interpretive
   summary, not an exact consequence.  The unit localizes the obstruction but
   does not make the comparison doctrine or record basis self-generated.

The motivational questions at lines 7--13 and 21--26 mention genuine carrier
rewrites, but the paper later explicitly says the fixture does not construct
them.  They are acceptable as motivation only, not as descriptions of the
computed arena.

## Required minimal repairs

1. Amend the active-witness paragraph to disclose that the two frozen points
   share `E(rho)=(16/25)rho+(9/25)Zrho Z` and differ in the outcome-resolved
   instrument.  Either keep the primary at that declared operational scope or
   add the exact `w3`/`lambda` observation as a clearly post-review analytic
   corollary, not as a silently preregistered measurement.
2. Qualify “interference,” “history channel,” “durable,” and “dynamically
   silent” by the declared decomposition, record typing, and one-step scope.
3. Replace “fixed point” by “joint constraint locus,” or define the actual
   record-to-comparison/law self-map whose fixed point is claimed.
4. Add the symbolic Kraus identity and the fixed-factor/no-growing-factor
   distinction to the certificate text.  No new numerical run is needed to
   establish it, but a successor instrument should gate it algebraically.
5. Clarify the failed-run heading as “before result disclosure/promotion.”

These repairs leave both frozen classifier words and every exact finite count
unchanged.  They prevent a valid boundary instrument from being mistaken for
the missing joint relational successor law.

## Final grade

**ACCEPT-WITH-FIXES.**  Exact numerical discrepancies: **0**.  Exact sector,
dimension, gauge, witness, CP, TP, classifier, consequence-wall, seal, and
serializer-truth discrepancies: **0**.  The required fixes concern the
operator meaning of the surviving two-dimensional family and the ontology
claimed for its declared outcome/history decomposition.

The report SHA-256 is intentionally supplied by the delivery message rather
than self-embedded in this file.
