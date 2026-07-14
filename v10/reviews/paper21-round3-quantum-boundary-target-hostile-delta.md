# Paper 21 round 3 — quantum predictive-boundary target hostile delta

**Frozen target:** commit `caaba6e`, reviewed only for the new/renumbered §10
exact-next-target development.  The terminal D34d results and their clean
review chain are not reopened.

**Verdict:** **MAJOR REVISION OF THE QUANTUM D34e PIN**.

**Counts:** **0 BLOCKER / 2 MAJOR / 2 MINOR / 0 NIT**.

The classical architecture of the target is strong: it fixes the law-relative
predictive quotient before proposing a collar carrier, separates sufficiency
from minimality, allows exact obstruction, and refuses an unearned profinite
bridge.  The quantum paragraph is not yet exact enough to govern D34e.  It
conflates several inequivalent notions of rank and assigns “strong positivity”
to restriction maps rather than to the finite history functional.  Those are
object-type errors in the investigation pin, not failures of D34d's already
reviewed finite `P,E` calculation.

## 1. What the new section gets right

### 1.1 Predictive quotient before carrier

Sections 10.1–10.3 correctly distinguish:

- the complete marked past;
- the law/query/instrument-relative predictive equivalence class;
- an active collar message proposed as a physical realization;
- exact sufficiency versus an injective/minimal realization;
- bounded, growing, whole-component and nonexistent record-carried
  realizations.

The implication

```text
B_A(h)=B_A(h')  =>  h ~_(mu,A,Q) h'
```

is the correct sufficiency direction.  Adding the converse modulo declared
carrier gauge makes the realization exact rather than merely redundant.  The
capacity paragraph also correctly refuses to hide an entire history in one
unbounded real coordinate or infer bounded collar capacity from finite
per-click content.

### 1.2 Retained boundary versus eliminated process

Section 10.5 correctly recognizes two descriptions at different widths:

- if every relevant boundary memory degree is retained, the predictive object
  may be a joint state/boundary functional on those degrees and open legs;
- if those degrees are eliminated, future interventions are represented by a
  multi-time process tensor/quantum comb rather than one reduced density
  operator at the cut.

This is consistent with paper §7.3 and does not claim that a per-record rebit
state is already sufficient.

### 1.3 Profinite nonclaim

Section 10.4 is appropriately conditional.  It demands finite marked
quotients/partitions, compatible bonding maps, constancy of future laws on the
identified stem fibers, cylinder continuity or a stated measurability
replacement, and a pushforward/lift of the supplied law.  It explicitly says
that topology alone does not select `mu`, the event grammar or the encoder,
and that continuous/unbounded marks need not yield a profinite object.

No classical or quantum factorization through the v9 profinite stem spectrum
is claimed.  The section also keeps committed-prefix depth distinct from stem-
spectrum resolution.  This opening is well stated and survives the hostile
audit.

## 2. Major findings

### M1 — “operator-space or memory rank” conflates inequivalent widths

Section 10.5 asks for “its minimal operator-space or memory rank,” while §10.3
uses the unqualified phrase “classical/quantum rank.”  There is no single
canonical rank behind those words.  At least the following quantities can
differ:

1. Hilbert dimension of a retained quantum memory/boundary carrier;
2. rank of one conditional density or boundary operator;
3. real/complex linear dimension of the span of conditional operational
   boundary functionals;
4. Choi rank of a channel or one process-tensor marginal;
5. operator-Schmidt/bond rank of a comb across a temporal or spatial cut;
6. minimal ancilla-memory dimension over all realizations of the declared
   comb and instrument family.

For example, paper §7's conditional joint middle states are pure (operator
rank one), while the retained E carrier still has dimension two and transports
one bit of past information.  Density-matrix rank is therefore already not the
memory width displayed by the paper's own witness.  A channel's Choi/Kraus
rank is likewise not automatically the minimal predictive memory dimension.

Because D34e is supposed to decide whether width is bounded, leaving the width
invariant undefined makes its central pass/fail result uninterpretable.

**Required repair:** freeze separate names and report them separately.  A
defensible minimum is:

```text
d_carrier = minimal retained memory Hilbert dimension under declared
            record/port ownership constraints;
d_op      = dimension of the span of conditional operational functionals;
chi_cut   = declared operator-Schmidt/bond rank of the conditional comb
            across a named cut.
```

If D34e optimizes only one of these, say which one and state that the others
remain open.  Do not use density-operator rank, Choi rank, bond rank and memory
dimension interchangeably.

### M2 — restriction maps do not “remain strongly positive”

The final sentence of §10.5 asks whether “its restriction maps remain strongly
positive.”  Strong positivity is a property of a decoherence functional (all
finite event matrices are positive semidefinite), not an untyped property of a
restriction map.  In the process-tensor language, the Choi operator is positive
semidefinite and satisfies causal trace constraints; intervening dynamics are
completely positive maps.  Projective restriction is a separate consistency
equation.

This distinction is exactly what D34c's terminal theorem used:

```text
each finite D_n is strongly positive,
incidence/restriction pushdown sends D_(n+1) exactly to D_n.
```

The restriction map itself was not christened a strongly positive functional.
For a comb tower, the analogous conditions are positivity/causality of each
finite Choi operator plus exact compatibility under the declared partial trace
or link-product marginal.  The literature likewise treats strong positivity
as a decoherence-functional condition; see Dowker–Wilkes, [*An Argument for
Strong Positivity of the Decoherence
Functional*](https://arxiv.org/abs/2011.06120).

**Required repair:** replace the single phrase with a typed three-row gate:

1. `D_n` is normalized, Hermitian and strongly positive at every finite
   history level;
2. the declared restriction/incidence map satisfies
   `R_(n+1->n)(D_(n+1))=D_n` exactly;
3. any conditional process-tensor/comb Choi operator is positive semidefinite,
   obeys its causal trace constraints, and its finite marginals are compatible
   under the named trace/link maps.

If an encoder/update channel is part of the physical boundary realization,
gate complete positivity and causality of that channel separately.

## 3. Minor findings

### m1 — operational equivalence needs typed instruments and outcomes

Section 10.1 defines `Q_A` as a class of “interventions and readouts” and then
writes

```text
Law_mu(q | h)=Law_mu(q | h').
```

This is serviceable shorthand classically, but it is not an exact operational
quantum type: an intervention is chosen, while outcomes are random.  For
quantum histories, equality of fine-path probabilities is not licensed either.

**Required repair:** define a conditional operational functional.  For
example, for every licensed instrument sequence `I` with typed input/output
ports and every durable outcome word `r`, require

```text
P_mu(r | I,h)=P_mu(r | I,h').
```

Equivalently define `T_h[I](r)` and quotient by equality of `T_h` on the entire
declared instrument family.  In a quantum lift, these probabilities must arise
from contractions of the conditional comb/decoherence functional with
licensed instruments, never from unlicensed fine-history diagonals.  Also
state whether adaptive instruments and ancillary entanglement are admitted;
that choice changes the quotient and its minimal memory.

### m2 — the auxiliary `P,E` witness does not prove SHARD needs process memory

Section 10.5 says the finite `P,E` witness “proves the need for such memory but
does not construct the SHARD boundary process.”  The second clause is correct;
the first is too broad in the context of the proposed SHARD investigation.

The witness proves only that, in that auxiliary fixed process, the reduced
one-time P state is insufficient and retaining E or a reduced multi-time
description is necessary.  It does not prove that the chosen D34b–D34c history
law has nonzero process-memory rank, nor that its predictive quotient cannot
be represented by some other record-carried state.

**Required repair:** say:

> the finite auxiliary `P,E` witness demonstrates why a reduced one-time state
> can fail and supplies a negative control for D34e; it neither constructs nor
> proves the necessity of a process-memory carrier for the SHARD boundary.

## 4. Profinite-quantum disposition

The section makes no false profinite claim.  In particular, it does **not**
assert:

- that operational predictive equivalence is continuous in the v9 stem
  topology;
- that quantum marks factor through finite stem partitions;
- that a process-tensor tower has been supplied;
- that positive finite objects automatically extend to the inverse limit;
- that profinite topology selects the law or quantum operations.

A future quantum bridge would require a typed inverse system of finite
operational objects: strongly positive history functionals or positive causal
comb Choi operators at each level, exact compatible marginals, and an extension
theorem at the chosen measurable/topological limit.  Section 10.4 correctly
lists these as required work rather than D34d output.

## 5. Claim-by-claim disposition

| New §10 claim/target | Disposition |
|---|---|
| Law/query/instrument-relative predictive quotient precedes carrier | **PASS** |
| Collar sufficiency and exact minimality directions | **PASS** |
| Record ownership/capacity restrictions | **PASS** |
| Exact obstruction as a valid outcome | **PASS** |
| Retained boundary state versus eliminated comb/process tensor | **PASS, typed refinement required by m1** |
| Minimal “operator-space or memory rank” | **UNDEFINED — M1** |
| “Restriction maps remain strongly positive” | **TYPE ERROR — M2** |
| Auxiliary `P,E` witness proves generic reduced-state insufficiency | **PASS** |
| Auxiliary witness proves SHARD requires process memory | Correctly must be **NO — repair m2** |
| Profinite predictive-boundary bridge exists | Correctly **NOT CLAIMED** |
| D34e finite campaign proves all-future sufficiency | Correctly **NOT CLAIMED** |

## 6. Adjudicated status

Paper 21's terminal D34d noun remains accepted and is not reopened by these
findings.  The new §10 classical/profinite target is also accepted in outline.
What is not yet accepted is the **quantum exactness of the D34e pin**.

After M1 chooses explicit width invariants, M2 separates positivity from
restriction/causality, m1 types the operational quotient, and m2 narrows the
auxiliary witness, this stream can move to a focused textual/mathematical
delta.  No existing D34c/D34d executable or finite `P,E` calculation needs to
be changed.
