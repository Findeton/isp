# JRH hostile review — Seat O: operator / exact demolition

**Target:** commit `2f117f2`, with the four SHA-256 artifact digests frozen in
`v16/note-jrh-hostile-protocol.md`.

## Executive finding

The load-bearing qubit algebra is correct.  Independently reconstructed Z- and
X-resolving instruments are CP and trace preserving; the two HJW ensembles give
the same complete classical-quantum output; the Bell steering comparison is
no-signalling in the registered fixed tensor factorization; the nonlinear
control is genuinely decomposition-sensitive; and the Z/X rival laws predict
different records.

The frozen paper nevertheless does **not** establish the registered joint
relational-history object.  Its geometry and collar tests are disconnected
labels or separately chosen maps, its relabelling and diamond gates do not act
on complete boundary successors, its alleged triangle holonomy is an open
two-edge transport, and its no-forced-deviation gate is a logical non sequitur.
The exact engine faithfully seals these predicates; sealing does not make the
predicates adequate.  The result that survives is a narrower one: an
uncalibrated classical-quantum successor **schema** is consistent and radically
underdetermined.  “Dynamic geometry,” complete regional covariance, and a
family-wide QFT/GR consequence are not demonstrated.

## O1. Independent quantum rebuild

Let

`P0 = |0><0|`, `P1 = |1><1|`,
`Q+ = |+><+|`, and `Q- = |-><-|`.

For either pair `K = (P0,P1)` or `K = (Q+,Q-)`, each branch
`J_z(rho)=K_z rho K_z^dagger` is CP because, for every ancillary positive
operator `X`,

`(I tensor K_z) X (I tensor K_z)^dagger >= 0`.

This is the substantive Kraus theorem.  The candidate's Choi object
`|vec(K_z)><vec(K_z)|` is a valid rank-one Gram certificate, and its 15
nonempty principal minors per 4-by-4 Choi matrix explain the reported 90 checks
over 6 branches.  It is not an independent discovery of CP: the certificate is
constructed from the same Kraus operator that defines the map.  There is no
error in using it once that distinction is made.

Trace preservation follows exactly from

`P0 + P1 = I`, `Q+ + Q- = I`,

and, for the reset control, from
`|0><0|^dagger|0><0| + |0><1|^dagger|0><1| = I`.

The two ensembles are

`E_Z = {1/2,P0; 1/2,P1}` and
`E_X = {1/2,Q+; 1/2,Q-}`,

and both average to `I/2`.  My independent rational-matrix rebuild gives the
following **complete unnormalised output blocks**, not merely outcome
marginals, for the Z instrument:

```text
geometry/record 0: [[1/2, 0], [0, 0]]
geometry/record 1: [[0, 0], [0, 1/2]]
```

Both `E_Z` and `E_X` give exactly those blocks.  For the X rival both ensembles
instead give

```text
geometry/record 0: 1/4 [[1,  1], [ 1, 1]]
geometry/record 1: 1/4 [[1, -1], [-1, 1]]
```

Thus complete classical branch identity, geometry label, probability, and
post-state all agree in the safe comparisons.

For `|Phi+>`, Alice's Z measurement prepares Bob's `E_Z`, while her X
measurement prepares `E_X`, with exact weight `1/2` in every branch.  Applying
either fixed Bob instrument to the two unconditioned ensembles gives the same
blocks above.  This is the standard HJW structure
([Hughston–Jozsa–Wootters](https://doi.org/10.1016/0375-9601(93)90880-9))
and is consistent with the usual no-signalling constraint on quantum dynamics
([Simon–Buzek–Gisin](https://doi.org/10.1103/PhysRevLett.87.170405)).  It proves
the registered one-step, fixed-factorization comparison; it is not the v15
addendum's all-preparations, all-windows theorem on a changing factorization.

The positive control is also genuine.  For

`D(E)=sum_j p_j (Tr[Z rho_j])^2`,

the exact values are `D(E_Z)=1`, `D(E_X)=0`, and
`D({1,I/2})=0`, whereas averaging the two pure Z members gives `1`.  If Alice's
remote basis choice is allowed to select the decomposition supplied to this
rule, Bob receives deterministic local statistics `1` versus `0`.  The control
therefore shows both preparation dependence and the conditional signalling
mechanism discussed by
[Gisin](https://doi.org/10.1016/0375-9601(90)90786-N).  It is deliberately not
a well-defined density-operator map, which is the point of the control.

## O2. The rival and what it actually demolishes

I marched the X rival independently through the protocol's named surface.

| requirement | result | exact reason |
|---|---|---|
| normalization and CP/TP | pass | `Q+ + Q- = I`; each branch is Kraus rank one |
| mixture affinity | pass | each complete block is linear in `rho` |
| HJW and Bell no-signalling | pass | both remote ensembles average to `I/2` before the fixed local instrument |
| branch/geometry resolution | pass as a label grammar | on input `P0`, both X outcomes have probability `1/2` and carry distinct output bits |
| idle spectator | pass at the matter-map level | `(Q_z tensor I)` reduces exactly to `Q_z` after tracing the spectator |
| disjoint diamond | pass at the matter-map level | operators on different tensor factors commute |
| collar dependence | existential pass only | X versus outcome-swapped X differs on `Q+`; unlike the main law's test, it does not differ on `P0` |

On the same input `P0`, main record probabilities are `(1,0)` while rival
probabilities are `(1/2,1/2)`.  No frozen JRH or parent rule selects the Z basis
over the X basis.  Jointness, CP, affinity, label covariance, and one-step
no-signalling therefore do not select a prediction-equivalence class.

Two qualifications are mandatory.

First, the “same ontology” claim is true only while outcome `z`/“flux” is an
uncalibrated branch bit.  A Z result and an X result are different observables.
The paper supplies no independently fixed conservation law, stress/flux
referent, or common later calibration that proves they are two laws for the
same physical quantity.  The missing readout acknowledged in the choice table
is therefore load-bearing.  Minimal repair: freeze one operational calibration
of record/flux and show both laws reproduce it while retaining different later
predictions.  Otherwise say “same carrier and output grammar,” not “same
physical ontology.”

Second, the rival uses a different collar witness state (`Q+`) from the main
law (`P0`).  This is legitimate for an existential collar-dependence property,
but not for a claim that identical registered rows were replayed.  The receipt
must record that distinction.

The countermodel proves underdetermination by the **current weak structural
requirements**.  It does not prove underdetermination after conservation,
overlap gluing, refinement/path independence, a calibrated flux observable,
or a continuum deformation algebra is imposed.  The paper mostly respects
this wall.

## O3. Arity, locality, and holonomy

The independent graph calculation is immediate: for a connected graph the
cycle rank is `m-n+1`.  It gives `0` for `K2`, `0` for the three-vertex path,
and `1` for the triangle.  Consequently, three actors are the first **possible
loop carrier**.  Nothing about minimum event arity follows.

The reported Gaussian-rational product is also arithmetically correct.  With
`q_i=i sigma_x` and `q_j=i sigma_y`, `q_j q_i = i sigma_z = diag(i,-i)`.
But the code supplies only those two edge transports.  A triangle holonomy
requires an oriented product around all three edges, with reverse edges bound
to inverses.  An open two-edge transport is gauge-dependent and can be changed
by endpoint frame choices.  Even for a genuine loop, the displayed matrix is
basepoint-gauge covariant by conjugation; only its conjugacy class, trace, or
eigenvalues are gauge-invariant.  Minimal repair: declare `U_01`, `U_12`, and
`U_20`, calculate `U_20 U_12 U_01`, test reversal and basepoint change, and
report a conjugacy invariant.  Until then, “triangle holonomy” fails; the graph
cycle-rank sentence survives.

The L2 object is a typed qubit instrument with an attached pair key and two
output labels.  It does not contain an input relation value whose change is
compared with `R'`, nor does it make its output geometry alter a later
successor law.  The idle-spectator test tensors an identity qubit onto one
product input.  This correctly demonstrates an ordinary local CP extension,
not physical two-actor gravitational backreaction.  The disjoint-diamond test
is stronger in using a correlated Bell input, but it compares only the two
orders of the matter Kraus maps; it never composes relation, geometry, collar,
or record outputs.  Hence the transcript's phrase “complete maps” is false for
that gate.

The three-qubit parity projectors form a valid CP/TP two-outcome instrument and
have three-qubit dependency support.  No complete relational successor is
attached to them, and the construction neither proves robust irreducibility
nor excludes a sequential ancilla implementation.  The paper explicitly
refuses both claims.  It also supplies no all-`n` extension.

## O4. Hamiltonian and modes

The fourth-root calculation is correct but narrower than “Hamiltonian
reconstruction.”  If the one-step image is `diag(1,i)`, every integer pair
`(4m,1+4n)` has the same image under the registered fourth-root map.  The five
listed pairs merely fix `m=0` and sample five values of `n`; they are witnesses,
not all logarithm branches.  Restoring physical units and the conventional
sign adds the chosen interval and a factor `pi/2`.  What is proved is:

> one discrete transfer, with one chosen clock interval, does not select a
> logarithm branch.

It does not prove that no continuity, locality, ground-state, or energy
condition could select a generator, and it does not prove that Hamiltonians
are non-ontic.

For input `Q+`, the Z instrument's unconditional classical-quantum block state
has purity `1/2`, versus input purity `1`.  Therefore no unitary endomorphism of
the original two-dimensional matter sector realizes that channel.  This does
not obstruct a unitary Stinespring dilation on a larger space
([Stinespring](https://doi.org/10.1090/S0002-9947-1955-0069403-4)), nor does it
prove nonexistence of a global Hamiltonian after an embedding, clock, and
environment are chosen.  The paper states this distinction correctly; the
gate evidence incorrectly calls the four-dimensional direct-sum output
“same-sector.”

Finally, identity on a four-cycle has one eigenvalue with multiplicity four,
whereas the cyclic shift has exact one-dimensional eigenmodes with eigenvalues
`1,i,-1,-i`.  This proves only that spectra depend on an unspecified transfer
law.  Since no vacuum, stability criterion, statistics, or mode-to-particle map
exists, it does not itself prove a particle-species theorem.  The honest result
is “species remain open and unselected,” not “four species.”

## O5. Instrument hostility

After completing the independent rebuild, I black-boxed an off-tree copy that
contained the frozen 13-source whitelist but no `.git` directory.

- Two plain runs from a foreign working directory regenerated paper,
  transcript, and receipt at the exact three frozen SHA-256 digests.
- Unknown CLI exited `2` and wrote nothing.  `--selftest` exited `0` at
  `G-SOURCE-ANCHOR`.  `CP_BREAK`, `GEOMETRY_ERASE`, `RIVAL_IDENTICAL`, and
  `NONLINEAR` each exited `3` at its named gate and changed no artifact bytes.
- All 13 receipt mutants have distinct before/after digests and die at their
  named gates.  A no-op passed to `Mutator.change` is rejected before it can be
  counted as movement.
- I independently recomputed all 18 receipt-key seals, all 37 row digests and
  the ledger head, paper/output hashes, the 13-entry read-set equality, and all
  115 numeral-token occurrences.  They reconcile exactly.
- In-memory post-seal addition, sealed-value edit, unsealed-key injection, and
  paper claim drift all fail the independent totality/hash checks.

The integrity machinery is therefore strong.  Four scientific predicate
defects remain:

1. **Relabelling does not test the law.** `G-A4` relabels a literal containing
   only actor names and writes, then compares it with a typed literal.  It does
   not apply `law(relabel(input)) = relabel(law(input))` to `R,G,C,S` and every
   complete successor.  This violates the pin's full-boundary requirement.
2. **Geometry/collar are not causally bound.** The “later probe” is the identity
   dictionary `{g:g}`.  The successor function ignores its input `collar`, and
   `G-C4` manually chooses two different Kraus dictionaries outside that
   function.  Thus neither future influence nor one collar-dependent law is
   measured.  `G-C1` merely checks three tuple fields were filled with the same
   `z`.
3. **Several gates restate constructed data.** `G-A3` checks a hand-written
   one-row payload; `G-E3` checks that a hand-written dictionary has six named
   keys; `G-F5` checks that a hand-written empty list is empty.  Mutants show
   code reachability, not physical discrimination.
4. **`G-F4` is invalid logic.** The code sets the no-forced-deviation result
   equal to “the rival has different microscopic statistics.”  Two models can
   differ on one observable and still share another invariant deviation.  No
   QFT/GR comparison observable, map, or exhaustive surviving family was
   constructed.  The licensed conclusion is “no QFT/GR deviation is presently
   typed or predicted,” not “none is common across the family.”

One smaller integrity mismatch should also be repaired: the selftest mutates
the **expected** source digest and leaves the observed digest untouched, while
the frozen gate requires corrupting an observed anchor.  It still proves the
equality check fails and writes nothing, but it does not exercise the observed
digest path in the prescribed direction.

## Defects, consequences, and minimum repairs

| severity | exact object | consequence | minimum repair or kill |
|---|---|---|---|
| CRITICAL | `G-C2`, `G-C4`, and `successor()` | no measured geometry-dependent continuation or collar-dependent joint law; registered A–E existence is not established | make `(R,G,C,S)` an actual input to one law; use two same-`R,G,S` inputs differing only in `C`; compose a later instrument whose exact distribution depends on output `G,C`; include erasure controls |
| CRITICAL | `G-F4-DEVIATION-STANDARD` | family-wide no-deviation claim does not follow | delete the gate/verdict or define one exact QFT/GR comparison observable and enumerate/certify the whole registered survivor family |
| MAJOR | `G-A4` and `G-D3` | covariance and complete disjoint composition are not tested | compare full successor dictionaries/direct-sum blocks under an explicit boundary isomorphism, including relation, geometry, collar, state, and records |
| MAJOR | `G-D4` | open path is mislabeled a holonomy | bind three oriented edge transports and report a gauge-invariant loop conjugacy datum |
| MAJOR | X-rival “same ontology” wording | the rival may change the physical observable called flux | add a common operational calibration/conservation referent, or narrow to same uncalibrated carrier/grammar |
| MINOR | generator lift inventory | five witnesses are not all logarithm branches | state the full `(4m,1+4n)` family, clock/unit/sign conventions, and keep the five only as test witnesses |
| MINOR | source-anchor selftest | required observed-path corruption is not exercised | mutate the observed digest after the logged read, not the frozen expected digest |

## Grade and highest licensed verdicts

**GRADE: REJECT.**  This grade rejects the frozen paper's claim to have proved
the complete JRH candidate and “37 of 37” scientific gates.  It does not reject
the confirmed qubit instrument algebra or the useful underdetermination
counterexample.

**Highest licensed primary reading:**
`JRH-CONSISTENT-BUT-UNDERDETERMINED` only after explicit narrowing to a
**finite, uncalibrated classical-quantum geometry-labelled successor schema**.
No frozen primary verdict is licensed for the claimed joint dynamic-geometry
law until C2/C4, full relabelling, and complete diamond composition are rebuilt.
`JRH-INCONSISTENT` is also not licensed: the defects are missing bindings, not a
no-go for every candidate.

**Highest licensed secondary verdicts:**

- `L2-VIABLE` — typed CP fixture only, not physical gravitational backreaction;
- `TRIANGLE-FIRST-LOOP-NOT-FIRST-EVENT` — graph-theoretic possibility only;
- `EPR-SAFE-INSTRUMENT` — registered one-step fixed-factorization comparison;
- `HAMILTONIAN-RECOVERABLE-ONLY-RELATIVE-TO-FROZEN-SECTOR-AND-CLOCK` — read as
  single-transfer logarithm ambiguity, not a global nonexistence theorem;
- `SPECIES-UNSELECTED`;
- `AFFINE-CHANNEL-TERM-UNSELECTED`.

`NO-FORCED-QFT-GR-DEVIATION-IN-REGISTERED-FAMILY` is **not licensed** by the
implemented gate.  The supported replacement is: **no QFT/GR deviation is yet
typed or predicted by this unit**.
