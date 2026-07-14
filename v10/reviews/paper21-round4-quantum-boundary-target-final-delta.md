# Paper 21 round 4 — quantum-boundary target final delta

**Target:** repaired commit `aa1a258`, audited against every `M1`–`M2` and
`m1`–`m2` in
`paper21-round3-quantum-boundary-target-hostile-delta.md`.

**Exact verdict:** **SUBSTANTIVELY DELTA-CLEAN — 0 BLOCKER / 0 MAJOR /
2 MINOR / 1 NIT.**

Both previous majors and both previous minors are closed.  The repaired §10
now defines a usable operational quantum quotient, keeps the relevant width
invariants noninterchangeable, types the finite consistency gates correctly,
and makes no unearned quantum-profinite claim.  Two fresh measure/channel
precision issues and one width-definition nit should be repaired before the
D34e code pin; none changes Paper 21's scientific result or reopens D34d.

## 1. Prior finding disposition

### M1 — inequivalent quantum widths: CLOSED

Section 10.6 now freezes three separate quantities:

```text
d_carrier = minimal retained memory Hilbert dimension under declared
            record/port ownership constraints,
d_op      = real or complex dimension of the span of conditional operational
            boundary functionals,
chi_cut   = operator-Schmidt/bond rank of the conditional comb across one
            explicitly named cut.
```

It separately lists density-operator rank, channel Choi/Kraus rank and minimal
ancilla-memory dimension and forbids substitution among them without a
theorem.  This closes the former undefined phrase “operator-space or memory
rank.”  The capacity ledger in §10.4 and the audit instructions in §10.7 also
require the chosen widths to be printed separately from current-past size and
resolution.

No result in the paper now infers Hilbert carrier dimension from the rank of a
conditional density operator, or process memory from a Choi/Kraus rank.

### M2 — positivity, restriction, comb causality and CP: CLOSED

The repaired quantum ledger has four correctly separated gates:

1. each finite history functional `D_n` is normalized, Hermitian and strongly
   positive;
2. the named restriction/incidence map obeys the exact projective equation
   `R_(n+1->n)(D_(n+1))=D_n`;
3. each conditional-comb Choi operator is positive semidefinite, obeys the
   causal trace constraints, and has compatible marginals under named
   trace/link maps;
4. a physical encoder/update map must separately satisfy complete positivity
   and causality.

Strong positivity is no longer attributed to the restriction map.  Finite
projectivity is no longer treated as a substitute for positivity, causal
normalization or physical implementability.

### m1 — operational instruments and durable outcomes: CLOSED

The passive and controlled branches are now explicitly different inputs.  A
passive marked-history measure supplies a regular conditional kernel only
almost surely; it does not silently supply intervention responses.  The
controlled branch instead requires a causal family indexed by licensed
classical policies or quantum instrument sequences and compares

```text
P(r | I,h)
```

for every licensed typed instrument sequence `I` and durable outcome word
`r`.  The instrument family must state whether adaptive choices and entangled
ancillas are allowed.  The probabilities must be obtained by contraction with
the supplied conditional process/decoherence object, never from unlicensed
fine-history diagonals.

The quotient is correspondingly law-, region-, query-, instrument- and
stopping-relative.  This is the correct operational type for the proposed
D34e target.

### m2 — scope of the auxiliary P,E example: CLOSED

Section 10.6 now states exactly that the auxiliary `P,E` witness demonstrates
failure of a reduced one-time state and supplies a negative control.  It
explicitly says that the witness neither constructs nor proves the necessity
of a process-memory carrier for the SHARD boundary.

The repaired wording makes no inference from the auxiliary process to the
memory width of the D34b–D34c history law.

## 2. Fresh MINOR findings

### m1 — operational sufficiency needs a simultaneous almost-sure domain

Section 10.2 currently requires

```text
K^I_(tau,A)(h,.) = Kbar^I_(tau,A)(B_A(h),.)  mu-a.s.
```

“for every licensed `I`.”  Read literally, this can mean that each instrument
has its own `mu`-null exceptional set.  For an uncountable instrument family,
the union of those exceptional sets need not be null.  That is weaker than the
simultaneous operational statement used immediately above it, where one past
`h` is compared under every licensed instrument.

This is harmless when the registered instrument family is finite or
countable: intersect the corresponding full-measure sets.  It is not harmless
for a continuum of instruments unless a common version or a
measure-determining dense instrument class plus an appropriate continuity
theorem is supplied.

**Required repair:** make the quantifier order explicit.  Either require one
common `mu`-full reachable set `H_0` such that

```text
for every h in H_0 and every licensed I,
K^I_(tau,A)(h,.) = Kbar^I_(tau,A)(B_A(h),.),
```

or preregister a finite/countable operationally determining instrument family
and prove extension to the advertised larger family.  If interventions may
occur before the conditioning stop, also use the appropriate controlled past
law or a declared dominating measure instead of passive `mu` automatically.

Without this repair, a future “exact operational carrier” verdict could hide
instrument-dependent null histories.

### m2 — outcome-conditioned updates are instrument branches, not channels

The fourth quantum consistency row currently says that any physical
“encoder/update channel” is completely positive and causal.  That is correct
for a deterministic unconditional update, but an update conditioned on a
durable outcome is normally one branch of an instrument: before
normalization it is completely positive and trace-nonincreasing; the sum over
outcomes is the trace-preserving causal channel.  The normalized conditional
state update is generally nonlinear and should not itself be called a quantum
channel.

This distinction matters here because the target explicitly retains durable
outcome words and permits adaptive instrument sequences.

**Required repair:** type row 4 as follows:

```text
deterministic encoder/update:
    completely positive, trace preserving and causal;

outcome-resolved encoder/update instrument:
    each branch completely positive and trace nonincreasing,
    with the branch sum trace preserving and causal;

normalized conditional update:
    derived by conditioning, not asserted to be a linear channel.
```

The named ports, trace convention and any subnormalized boundary state should
be fixed with the comb link convention.  This is a protocol correction, not a
counterexample to the current finite quantum receipt.

## 3. Fresh NIT

The new width definitions are noninterchangeable in substance, but one phrase
can still be sharpened.  `d_carrier` is a minimum over **record-native retained
carriers subject to ownership constraints**, while “minimal ancilla-memory
dimension” is later listed as a distinct minimum.  Add that the latter is the
minimum over the declared unrestricted comb/process realizations.  Otherwise
a reader can reasonably ask why two quantities both called minimal memory
Hilbert dimensions are distinct.

Likewise, use “operator-Schmidt rank of the comb Choi operator under the named
tensor bipartition” for `chi_cut`; call it a bond rank only when that algebraic
tensor-network convention is declared.  This does not reopen M1 because the
paper already forbids substitution and names the cut.

## 4. Profinite-quantum disposition: PASS

The repaired paper still makes no intrinsic quantum-profinite claim.  Section
10.5 carefully distinguishes:

1. measurable factorization of a completed-history observable through the v9
   map;
2. factorization of the online predictive kernel through an adapted posterior
   measure;
3. construction of a compatible finite/profinite realization of the online
   boundary itself.

It says the third object may define a new inverse limit and requires commuting
maps, compatibility and adaptedness before identifying it with `X_stem`.  It
also distinguishes Borel almost-sure sufficiency from continuous profinite
realization, and does not claim that continuous functions factor through one
finite level.

Section 10.6 does not promote the finite `D_n` tower or conditional combs to a
quantum object on the profinite limit.  In particular, it does not claim:

- that strong positivity plus finite projectivity alone proves an infinite
  quantum extension;
- that operational instrument responses are continuous in the v9 stem
  topology;
- that quantum marks or comb ports factor through finite stem partitions;
- that the profinite topology selects the history law, intervention family or
  physical carrier.

The quantum bridge therefore remains correctly classified as unproved future
work.

## 5. Final delta disposition

| Audit item | Disposition |
|---|---|
| `d_carrier`, `d_op`, `chi_cut` separately defined | **PASS** |
| Density, Choi/Kraus, cut and ancilla ranks noninterchangeable | **PASS WITH NIT** |
| Strong positivity belongs to each `D_n` | **PASS** |
| Exact projective restriction typed separately | **PASS** |
| Comb PSD, causal trace and marginal compatibility | **PASS** |
| Encoder/update complete positivity | **PASS WITH m2 PRECISION** |
| Typed instruments, durable outcomes and contractions | **PASS** |
| Adaptive and entangled-ancilla scope declared | **PASS** |
| Simultaneous operational almost-sure factorization | **m1 REPAIR REQUIRED** |
| Auxiliary `P,E` claim limited to negative control | **PASS** |
| No intrinsic profinite quantum extension claimed | **PASS** |

The maximum current claim remains:

> **D34e TARGET IDENTIFIED; PREDICTIVE RECORD-DAG BOUNDARY UNCONSTRUCTED.**

After the two minor typing/quantifier repairs and the width-definition nit,
the quantum-boundary target is ready to freeze.  No Paper 21 theorem, D34d
receipt, or terminal scientific conclusion requires revision.
