# D11 — complete Bloch–Lorentz SCIR packet protocol

**Status:** frozen before D11 executables, numerical outcomes, literature
search, or hostile review, 2026-07-11.

> **Post-review adjudication (2026-07-11):** This protocol remains the frozen
> target, but D11 does not pass it. The executable supplies a globally
> normalized sequential kernel with incidence-scoped instruments, not a
> decentralized local click law. G0 proves a dual-covariance template but
> does not transform a generated multi-frame history. G3 proves prefix mass
> normalization and one disjoint-SPLIT state/probability cell, not the
> canonical truncation pushforward required here. JOIN is only a
> sibling-merge. The round-1-repaired executable adds actual packet matrices,
> typed durable outcomes, explicit multi-parent provenance, an owned
> root-intervention witness, exact algebraic sign tests, and the selected
> schedule probability, but these do not close the larger gates. Under the
> verdict definitions in section 7, the adjudicated primary verdict is
> **`INCOMPLETE-PACKET`**. The frozen numerical label `INTERACTION-INERT` is
> retained only as a registry outcome; the physical diagnosis is
> **population-extinct / interaction-sparse**.

## 1. Question

D8 supplied a complete SCIR architecture. D10 supplied a conditional
complex-qubit/Lorentz ordered-space isomorphism but not a complete growing
packet. D11 asks:

> Can one fully specified, incidence-local SCIR packet use the D10 event
> algebra to generate variable record histories, owned joins, Born seals, and
> an intervention-defined influence envelope compatible with the same round
> `3+1` cone?

D11 does not ask again whether `Herm_2(C)_+` is a Lorentz cone; that is exact.
It tests whether a complete dynamics can be wired to it without a universe
update clock, an external `S^2` direction oracle, or nonlocal graph inspection.

## 2. Frozen primitive packet

### 2.1 Event/effect algebra

The declared local ordered space is

\[
V=\operatorname{Herm}_2(\mathbb C),\qquad V_+=\{X\succeq0\}.
\]

An event displacement is an unnormalized `X in V_+`. A local quantum state is
the normalized ray

\[
\rho={X\over \langle e,X\rangle},
\]

relative to a positive local order unit/effect `e`. In the root gauge `e=I`
and `Tr rho=1`. The declared click scale is `s=2`, so a pure normalized state
produces the null increment `Delta Y=2 rho`, with `Delta t=1`. This scale is
primitive packet data, not derived metres or seconds.

### 2.2 Dual `SL(2,C)` gauge

For a local frame change `A in SL(2,C)`, freeze

\[
X' = AXA^\dagger,
\quad
E'=A^{-\dagger}EA^{-1},
\quad
e'=A^{-\dagger}eA^{-1}.
\]

The operational probability is the ratio

\[
p(E|X,e)={\operatorname{Tr}(EX)\over\operatorname{Tr}(eX)}.
\]

For an instrument leg `K: H_a -> H_b`, freeze

\[
K'=A_b K A_a^{-1}.
\]

Completeness is expressed relative to the endpoint order units:

\[
\sum_o K_o^\dagger e_b K_o=e_a.
\]

These formulae must be proved gauge covariant exactly. A nonunitary physical
filter and a frame transformation remain distinct: gauge transforms states,
dual effects, order units, and instrument representations together.

### 2.3 Typed records and ports

Every open carrier is a typed tuple

```text
(record_id, owner, qubit_state, event_position, local_order_unit,
 frame_link_to_parent, ancestry_word, status=OPEN).
```

Every candidate token stores its rule type, exact owner ports, anchor record,
activity, and packet matrices. Tokens may inspect only their incident owned
ports and recorded anchor. No all-pairs graph search is a generative rule.

### 2.4 Root

The unique root has `Y=0`, `rho=P0`, `e=I`, one open qubit port, and no
pre-existing spatial coordinate system beyond its declared local algebraic
frame.

## 3. Frozen rewrite grammar

All activities are `1`. The auxiliary continuous-time race therefore has
unit exponential waiting per enabled token. Conditional on the fired token,
Born/instrument probabilities below select the outcome. Disjoint firings are
quotiented by commuting-instrument equivalence; overlapping firings have
recorded physical order.

### 3.1 `SPLIT`

`SPLIT` consumes one open qubit port. It has two outcomes `g in {H,T}` with
Kraus/isometry legs

\[
K_g|\psi\rangle={1\over\sqrt2}
       (U_g|\psi\rangle)\otimes|0\rangle,
\quad U_H=H,\quad U_T=T.
\]

Thus `sum_g K_g^dagger K_g=I`. The outcome label is sealed. The normalized
children are

\[
\rho_a=U_g\rho U_g^\dagger,
\qquad
\rho_b=P_0.
\]

Their positions in the anchor frame are

\[
Y_a=Y_o+2\rho_a,
\qquad
Y_b=Y_o+2P_0.
\]

`SPLIT` emits exactly two open child ports and one sibling `JOIN` token owned
by those two ports and anchored at `o`. The first child carries the transformed
state; the second is a newly prepared finite ancilla carrier. No cloning claim
is made.

### 3.2 `JOIN`

`JOIN` is enabled only while both direct sibling ports named by its token remain
open. It consumes both. In their recorded common anchor frame it applies the
partial-iSWAP at the frozen D9 angle `theta=pi/4`, then measures/discards the
second output in the `P0/P1` basis:

\[
J_b=(I\otimes\langle b|)U_{\rm pSWAP}(\pi/4),\qquad b\in\{0,1\}.
\]

`sum_b J_b^dagger J_b=I_4`. Outcome `b` is sealed and the normalized first
output becomes one new open carrier. Its event position is

\[
Y_c=Y_a+Y_b-Y_o.
\]

Because the join is between direct children,

\[
Y_c-Y_a=Y_b-Y_o\in V_+,
\quad
Y_c-Y_b=Y_a-Y_o\in V_+.
\]

The common-future property is therefore local, anchor-carried, linear, and
cone covariant. `JOIN` never scans for unrelated records. It is a genuine
interaction but does not join previously unrelated root components.

### 3.3 `SEAL`

`SEAL` consumes one open port with projective outcomes `P0,P1`, records the
Born outcome durably, and emits no continuation. It competes with `SPLIT` and
any owned `JOIN` sharing that port.

### 3.4 Candidate emission and invalidation

- every new open port emits one `SPLIT` and one `SEAL` token;
- every `SPLIT` emits the one sibling `JOIN` token described above;
- consuming a port invalidates every other token naming it;
- no rule silently creates a root, carrier, bridge leg, frame link, or owner.

This finite grammar plus the declared matrices/activities supplies a full
finite-cutoff path measure. Linear opportunity growth gives a Yule domination
and nonexplosion.

## 4. Frozen observables

Four relations must remain distinct:

1. **graph ancestry** `a <_G b` from recorded rewrite incidence;
2. **algebraic positivity** `a <_+ b` iff `Y_b-Y_a in V_+`;
3. **coordinate shadow** `(t,x)` extracted from `Y=tI+x.sigma`;
4. **interventional influence**: a later seal distribution changes when one
   earlier local state/instrument is changed while the remainder of the packet
   is held fixed.

The packet must prove `ancestry subset positivity`. It must not assume the
converse or equate pairwise positivity with influence.

The **influence envelope** is the closure of displacement directions in which
some positive-probability continuation seal is changed by the intervention.
Envelope equality with the Lorentz cone is weaker than pairwise
order/influence equality and is graded separately.

## 5. Frozen exact gates

### G0 — dual gauge

At 100-plus-digit or exact algebraic precision:

- event/effect pairing and the probability ratio are invariant under at least
  one nonunitary boost and noncommuting vertex-local frame changes;
- transformed instruments satisfy endpoint-order-unit completeness;
- state/effect/link path and diamond formulae are covariant;
- applying a physical filter without the dual transformation changes a
  declared control probability.

### G1 — instruments

`SPLIT`, `JOIN`, and `SEAL` are completely positive/instrument-complete;
outcome probabilities are nonnegative and normalized; seals are repeat-durable;
the join depends on both input states for at least one exact witness.

### G2 — grammar and ownership

Root uniqueness, local token emission, exact ownership, port consumption,
join-anchor provenance, invalidation, and absence of silent bridge legs pass
on exhaustive bounded histories.

### G3 — projectivity and construction gauge

Deleting terminal continuations gives the parent cylinder law. Two disjoint
firings executed in both schedules give identical canonical marked histories
and probabilities. An overlapping split/join-or-seal control detects physical
order.

### G4 — common future

Every enumerated split and join ancestry edge has a positive displacement.
The join identity is also checked after nonunitary frame changes. A deliberately
naive endpoint-copy join is retained as a negative control and must exhibit a
possible cone violation.

### G5 — influence

Compare exact finite continuation laws for `rho_root=P0` and the intervention
`rho_root=P+`. Require:

- no changed seal probability outside graph descendants;
- a changed probability along the carrier child;
- transfer through a `JOIN` for a declared witness;
- every changed descendant displacement lies in `V_+`;
- at least one positivity-related but branch-disjoint pair has zero influence,
  proving pairwise `positivity != influence`.

### G6 — direction support

The positive-word `H/T` carrier orbit is the same nested family as D10.
Finite-depth counts and support diagnostics must reproduce independently. The
claim that its union is dense is conditional on the cited Clifford+T theorem
plus the compactness lemma, not inferred from a finite run.

## 6. Frozen numerical geometry protocol

The exact gates are primary. A secondary generated-history campaign uses the
complete grammar with no parameter sweep:

```text
cutoffs N = 512, 1024, 2048;
24 fresh seeds per cutoff, seed blocks 20276000, 20277000, 20278000;
all token activities = 1;
theta = pi/4;
click scale s = 2;
root state P0;
intervention state P+;
```

For each history report:

- counts of SPLIT/JOIN/SEAL and maximum open ports;
- unique null carrier directions and external diagnostic covering support;
- covariance eigenvalues/rank of `(t,x1,x2,x3)` positions;
- fraction of ancestry edges violating positivity (must be exactly zero);
- fraction of positivity-related pairs that are ancestry-related;
- paired-history changed-seal support and every influence-cone violation;
- average-cloud `F` only if the inherited instrument has enough valid
  projections; otherwise refuse rather than impute;
- a same-pipeline `M4` control and convention/systematics labels.

The numerical campaign may demonstrate typical angular filling and expose
degeneracy. It cannot upgrade the built-in four-factor coordinate count into a
derivation of dimension.

### Frozen numerical verdict

`GENERATED-ENVELOPE-CONSISTENT` requires, at all three cutoffs:

1. zero ancestry/influence cone violations across all seeds;
2. nonzero join-transmitted influence in at least 20/24 seeds;
3. median generated direction support nondecreasing with cutoff and at least
   `0.80` by `N=2048`;
4. four positive covariance eigenvalues in at least 20/24 histories at
   `N=2048`;
5. no claimed `F` pass unless both inherited conventions are valid.

Failure of (1) gives `REFUTED-CAUSAL-WIRING`. Failure of (2) gives
`INTERACTION-INERT`. Failure of (3) or (4) gives `GENERATIVE-DEGENERACY`.
Otherwise the numerical result is `MIXED`.

## 7. Frozen primary verdicts

Exactly one primary verdict is issued:

- `COMPLETE-CONDITIONAL-BLOCH-LORENTZ-SCIR`: exact G0–G6 pass, the finite
  grammar supplies every next-history probability, and the generated envelope
  meets the frozen numerical conjunction;
- `COMPLETE-KINEMATICS/INFLUENCE-ENVELOPE-OPEN`: the path law is complete and
  exact causal containment passes, but generated envelope/dimension gates are
  mixed or insufficient;
- `REFUTED-CAUSAL-WIRING`: any exact or numerical influenced descendant lies
  outside the algebraic future cone;
- `INCOMPLETE-PACKET`: any root, token, ownership, instrument, activity,
  invalidation, frame, position, or outcome rule remains unspecified.

Secondary labels must state:

- complex/rank-two selection remains primitive or open;
- scale `s=2` and `theta=pi/4` are primitive packet data;
- cone containment/common-future are construction theorems, not emergent
  discoveries;
- pairwise positivity is not influence;
- full unrelated-component joining is absent;
- no claim to Einstein dynamics, absolute units, or Newton's `G`.

## 8. Review protocol

After exact code, generated-history code, notes, literature audit, paper, and
pre-review receipt are frozen, three independent hostile streams audit
mathematics; ontology/locality/gauge; and clean-room reproduction. Every valid
opening is investigated before a later round. Production claims are amended,
never silently overwritten.
