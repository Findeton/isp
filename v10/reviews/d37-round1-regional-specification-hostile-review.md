# D37 round 1 — regional-specification hostile review

**Frozen target:** commit
`6a4a217f4316233bf88700cb85fec4bb2a2f14a2`.

**Lane:** registered opportunity complexes, exact K3/K2/K1 and joint-mode
conditionals, finite-cover descent, forcing-theorem width, boundary locality,
countable completion, covariance, anti-dilution and click attribution.

**Independence disclosure:** this is a coordinator self-hostile review of D37,
not the independent Paper 26 review.  The clean-room counts below do not close
that separate paper-level stream.

**Verdict:** **D37 PROMOTION WITHHELD FOR ONE RECEIPT-STRENGTH REPAIR; THE
REGIONAL-SPECIFICATION FAMILY, K2 PROGRESS RESULT, K1 WITNESS, JOINT
BIRTH/ARBITRATION COUNTS AND COUNTABLE COMPLETION ARGUMENT SURVIVE.**

**Count:** **0 blockers / 1 major / 3 minors / 0 nits.**

## 1. Frozen reproduction

I ran the frozen executable under `PYTHONHASHSEED=32452843` and `49979687`.
Both runs exited zero, were byte-identical to each other and were
byte-identical to the committed receipt.  Both print `PASS 9/9`.

The frozen hashes are:

```text
source
815589b997f191278cd78bf63d6a35ccb5d2f9f39dd361711f7331c1577a5f9d

complete stdout / committed receipt
27589e3af36652a526654c326879e9b3b16c883ca95268149116f86b68dcef20

printed stdout body
ab69b2b11f9b21c1edd348122509b63cf709db1718ad7174c216f3a21db33c16

internal science
cf9997407d8cb8b974f442ab341b7f4d3e6a1b3d3db3c43c6c4207189c0df0bf

note
21a2e5ec85845fe6028264599fcf8ad5ff722808ef1c806c4b3195c4755079e9

Paper 26 candidate
3d914159077307ed15615ae6032ffee833662e82d0fba823b1dccd1efde25017
```

`git diff --check 6a4a217^ 6a4a217` is clean.

The structural headline is independently arithmetically consistent:

```text
vertices   2+3+3+2+2+4+5+7                         = 28;
edges      1+2+3+0+1+2+4+6                         = 19;
regions    3+7+7+3+3+15+31+127                     = 196;
oriented rows on the five D36-defined cells
           3+7+7+3+3                               = 23.
```

The repaired registry correctly distinguishes D36's two-proposal no-conflict
cell from the two-edge disconnected factorization cell.

## 2. Core mathematics that passes

### 2.1 K3 and finite forcing

The K3 conditional code enumerates every positive exterior boundary on the
registered finite graphs and compares the intrinsic local activity law with
the conditional of the full joint.  The nested tower and boundary-mixture
checks are exact `Fraction` identities.  The printed
`508/7,098/138` census reproduces.

For a finite feasible selected set `S`, fixed feasible-addition odds give

```text
mu(S)/mu(empty) = product_(v in S) lambda_v.
```

This is deletion-order independent and normalizes to the hard-core law.  The
context-dependent odds control correctly produces both `2` and `4`, and the
maximal-support control correctly lacks positive feasible support.  Minor m1
below narrows which hypotheses this proof actually uses; it does not refute
the conclusion.

### 2.2 K2 progress and the completion argument

Uniform maximal independent sets are exactly the configurations satisfying
independence plus domination.  On the triangle the three maximal sets are the
three singletons.  Restriction to `P-Q` therefore gives

```text
{}:1/3, {P}:1/3, {Q}:1/3,
```

whereas direct K2 on the edge gives `{P}:1/2,{Q}:1/2`.  The empty restricted
outcome is explained by the selected exterior vertex.  The blocker/demand
kernel restores the conditional law exactly.  The printed
`188/165/1,224` census reproduces.

For the countable theorem, a countable greedy enumeration supplies at least
one maximal independent set, so the K2 admitted configuration space is
nonempty.  Independence and domination are closed local constraints.  On a
locally finite graph the sufficient demand data depend on a finite radius-two
collar, not an unbounded exterior.  The compactness/subsequence proof can
therefore pass each finite DLR identity to a limit.  No uniqueness conclusion
is earned or claimed.

### 2.3 Clean-room K1 path-five reconstruction

I re-enumerated the five-path without importing the D37 module.  Uniform
priority orders give the following full selected-set counts out of `5!=120`:

```text
{A,C,E}   56
{A,D}     20
{B,D}     24
{B,E}     20.
```

The two atoms whose exterior intersection with `{C,D,E}` is `{D}` have counts
20 and 24.  Hence

```text
P({A} | exterior {D}) = 20/(20+24) = 5/11;
P({B} | exterior {D}) = 24/(20+24) = 6/11.
```

The only atom with exterior `{E}` is `{B,E}`, so

```text
P({B} | exterior {E}) = 1.
```

The `20` count for `{A,D}` is also obtained directly from the independent
order constraints `A<B` and `D<C,D<E`: `120*(1/2)*(1/3)=20`.  For `{B,D}`,
the constraints `B<A`, `D<E` give 30 orders; the six orders with C before
both B and D are excluded, leaving 24.  The receipt's `5/11--6/11` witness is
therefore correct.

### 2.4 Clean-room `34/93` reconstruction

At equal mode weights and activity one, every admitted path atom has equal
weight.  For an independent selected set `S`, selected vertices have two
present-mode choices and unselected vertices have three mode choices.  The
path therefore has

```text
|S|=0:  1 * 2^0 * 3^3 = 27;
|S|=1:  3 * 2^1 * 3^2 = 54;
|S|=2:  1 * 2^2 * 3^1 = 12;
total                         93.
```

Fixing Q to BORN gives nine atoms with Q selected and 25 with Q unselected,
for 34.  TOKEN is symmetric.  With `NO_BIRTH`, Q cannot be selected and the
two endpoints contribute `(3+2)^2=25` atoms.  Thus

```text
P_Q(BORN)       = 34/93;
P_Q(TOKEN)      = 34/93;
P_Q(NO_BIRTH)   = 25/93;
P_Q(selected)   = 18/93 = 6/31.
```

This confirms the joint table independently of the production implementation.
It does not substitute for the still-open independent Paper 26 reviewer, who
must repeat at least one K1 and one joint-mode derivation.

## 3. MAJOR M1 — K1 marked anti-dilution is not equality-gated

S8 claims exact disconnected factorization for four families.  For K3, K2 and
the joint mode law, `anti_dilution_checks()` constructs the product law and
compares the complete union distribution against it.  K1 receives a weaker
test:

```text
restrict selected-set output to the left component;
compare only the number of union atoms with the product of component counts.
```

No equality compares the complete `PriorityAtom` distribution on the two-edge
union with the product of the two component-mark laws.  Equal atom count plus
one selected-set marginal does not in general imply factorization or correct
atom weights.

The implemented `priority_law()` does sample one order independently per
connected component, so direct inspection indicates that the desired product
identity is true.  The defect is nevertheless receipt-level: S8 could remain
green after a probability correlation or mark-identity regression that
preserved the tested count and marginal.

**Required repair:** construct the exact product of the left and right
`PriorityDistribution` objects and require complete atom-by-atom rational
equality with `priority_law(two_pairs)`.  Retain the selected-output marginal
as a separate anti-dilution check.  Regenerate every hash and run a closing
delta before declaring the D37 hostile stream closed.

## 4. MINOR m1 — Theorem 1's Markov premise is redundant as written

The forcing proof uses exact positive feasible support and the constant ratio

```text
mu(S union {v}) / mu(S) = lambda_v
```

for every feasible addition.  It does not use a separate Markov-boundary
hypothesis.  A finite conditional is already well-defined on every
positive-mass exterior; context-independent full-exterior odds directly give
the ratio used by the deletion path.

The Markov property remains important as a separate locality statement about
K3's regional kernel.  It is not an independent load-bearing premise of this
forcing argument once context-independent odds have been assumed.

**Required repair:** state the forcing theorem with two mathematical premises:
exact positive feasible support and fixed feasible-addition odds.  Present the
one-hop Markov boundary as a separately checked property of K3.  Alternatively
weaken the odds assumption so that Markov locality is genuinely needed and
show that use in the proof.  The first repair matches the executed receipt.

## 5. MINOR m2 — K2's sufficient collar is radius two

The K2 demand field asks whether a rejected exterior vertex adjacent to D is
already dominated outside.  Answering that question reads selected neighbors
of that exterior vertex, which can lie two graph steps from D.  The compressed
demand delivered to D is boundary data, but deriving it is not a one-hop
operation.

The code is correct and local finiteness still makes the countable continuity
argument work.  The frozen output, note and paper call the field
`blockers+domination-demands` without printing the numerical width required by
S8's own pin.

**Required repair:** print and state `two-hop blocker/demand collar` wherever
the K2 width matters, especially the countable-completion proof and the
per-family anti-dilution calibration.  Do not describe K2 as sharing K3's
one-hop collar.

## 6. MINOR m3 — the S4 verdict does not require the retained witness

`find_k1_one_hop_counterexample()` returns the correct nonempty path-five
witness, but `gates["S4"]` never tests that the return value is nonempty.  S4
could print an empty witness and remain `PASS` if the other K1 checks survived.

**Required repair:** make nonemptiness of the retained witness a fail-closed
S4 condition.  The manual reconstruction in section 2.3 shows that this
strengthening changes no scientific result.

## 7. Other attacked scopes that pass

1. The receipt does not call the supplied opportunity complex generated.
2. Mathematical role coordinates are not treated as dormant TOKEN records.
3. BORN/TOKEN exchange is asserted only at equal supplied mode weights.
4. K1's infinite quasilocal completion remains explicitly unproved.
5. Pairwise cover agreement is not promoted to positive joint extendability.
6. D26 visibility is a conditional BORN-sector observable, not a universal
   event rate.
7. Click randomness is represented by priority, mode and outcome marks rather
   than Python enumeration order.
8. The countable theorem proves existence but neither uniqueness nor phase
   selection.
9. The oriented interface is explicitly only a finite typed boundary layer,
   not a generated authenticated record DAG.
10. The quantum join and action bridge remain open.

## 8. Disposition

```text
B  blockers  0
M  majors    1
m  minors    3
n  nits      0
```

D37's substantive family theorem survives, but `PASS 9/9` is not yet a
hostile-closed receipt because the complete K1 marked factorization is not
equality-gated.  Paper 26 remains an exact-receipt candidate.  After the D37
repair and focused closing delta, the independent paper-level review must
still re-derive at least one K1 path-five atom and one `34/93`-family count.
