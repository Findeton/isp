# D12 hostile review, round 1: independent rebuild and reproducibility

**Referee:** independent clean-room reconstruction  
**Date:** 2026-07-11  
**Verdict:** **MAJOR REVISION — dynamical nonuniqueness is proved, but the restored implementation does not pass the protocol's whole-process, projective, frame, or construction-gauge gates**

D12's main no-go result is correct. I independently reconstructed both
counterexamples:

- the positive parity laws `P_r(x,y,z)=(1+rxyz)/8` have identical one- and
  two-record shadows while their next-record conditionals differ; and
- quarter-iSWAP and half-iSWAP share the advertised unitary symmetries and
  collar types while predicting `1/2` and `0` for the same later record.

Those two model pairs are enough to refute unique interaction selection from
the shared premises they actually instantiate. All three executables are
deterministic, standard-library-only, optimization-safe, and pass their fixed
check-count and semantic-receipt gates.

The 25-check “restored process” receipt is substantially overnamed. It models
one two-leg interaction followed by two pointer records. Its “256 commits”
test only subtracts two interface counters and adds two back; it does not
compose 256 quantum diamonds, histories, collars, or conditional laws. Its
projectivity check deletes one of two pointer observations in one diamond. Its
frame test is one global `H tensor H` basis conjugation. Its construction-order
test is operator commutation on two disjoint tensor factors. None implements
the canonical history fibers, truncation pushforwards, independently changed
vertex frames, links/screens/anchors, or continuing whole-history process
required by frozen gates U3, U4, U5, and U7.

Because the protocol explicitly assigns `INCOMPLETE-INVESTIGATION` when a
promised architecture class or decisive gate is not executed, the paper cannot
yet award `LOCAL/CONSTRUCTION/FRAME/PROJECTIVE GATES = PASS`. The narrower
logical conclusion—shared record structure does not select a unique process—
survives and should be retained.

## 1. Commands, determinism, and hashes

For each script I ran:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 SCRIPT.py
PYTHONDONTWRITEBYTECODE=1 python3 -O SCRIPT.py
```

Source hashes:

```text
0cfd533c70d29b3f82107927cb7d96b9333af185de57d3161e36800cdb4118fa  v10/code/d12_restored_diamond_process_exact.py
e5a8a50ffe03459cf62ca5b5168fd48079c6309fb3ae7ac2d7310203c1669b1f  v10/code/d12_diamond_law_nonuniqueness_exact.py
34215f2605f68029e4bce59c9e471d8af5892269d6b4b0ee7ac0193f67fe55dc  v10/code/d12_symmetric_interaction_family_exact.py
88142db43046b729bb88b4d5fd2fe345384d2431a6c239e91419a02b748de5b8  v10/note-d12-diamond-restoration-uniqueness-protocol.md
ed40587879c7cdbd6259bb65a84cf63e77aed382021ad1530655aea601c8980d  v10/relativistic-isp-v10-paper13-the-click-law-is-the-whole-history-process.md
```

Complete stdout hashes, identical under normal and optimized execution:

```text
d12_restored_diamond_process_exact.py       7d97f74d547ca13aab6d4978a69732afe27caf0568a2394b512da2e000237586
d12_diamond_law_nonuniqueness_exact.py      ffaf1bb6bb8125ca4f4d08d048d8828f6c48b81eb5e99f14ba6b0b3f8621ff7d
d12_symmetric_interaction_family_exact.py   a2da06a85371f83de4b22047f734747a988254cfce887039563b34161b3ba73f
```

The programs report `25`, `42`, and `18` checks respectively. Their internal
semantic receipt hashes reproduce Paper 13 exactly:

```text
c31174cbc695de30169e5acf1492998990609ea68e2b20e09b98d6370e039391
1f9472d6ed613ad96fe875d68cf0a773062c077e9a44fc357f65ccfd93bd4b97
7da912f8deb705aaa1467d3428aacf7cc626b249bf16c324c5c365f376b89db9
```

Each executable freezes both its expected check count and expected semantic
receipt. It uses explicit exceptions, not optimization-sensitive Python
`assert` statements. Imports are limited to the standard library:
`dataclasses`, `fractions`, `decimal`, `hashlib`, `itertools`, and
`__future__`.

Generated `d12_*.pyc` files already exist under `v10/code/__pycache__`. They
are not used in these runs because bytecode writing was disabled, but a final
self-containment receipt should remove or explicitly exclude them.

## 2. Independent classical whole-history reconstruction

For

$$
P_r(x,y,z)={1+rxyz\over8},\qquad |r|<1,
$$

all eight cells are strictly positive. Summing over any one sign cancels the
`rxyz` term, so every pair marginal is exactly `1/4`; summing again gives
uniform one-record marginals.

Conditioning gives

$$
P_r(z=1\mid x,y)={1+rxy\over2}.
$$

Thus after `x=y=1`:

```text
r=1/2 -> 3/4
r=1/3 -> 2/3
```

For fixed `y=1`, changing `x` changes this conditional, so the process is not
first-order Markov in the latest record `y`. Independent product gluing
normalizes because each factor has mass one. Splitting every atom into two
equal neutral refinements and summing the refinement label pushes back to the
original law.

This cleanly proves that projective compatibility and lower-order cylinder
data do not select the full history measure. A complete three-body coefficient
would identify `r`; it would not explain why nature chose it.

## 3. Independent quantum interaction reconstruction

On the one-excitation sector, the common family is

$$
U_\theta|01\rangle
=\cos\theta|01\rangle+i\sin\theta|10\rangle.
$$

Therefore a later second-leg-`1` record has probability `cos^2(theta)`:

```text
theta=pi/4 -> 1/2
theta=pi/2 -> 0
```

Both matrices are unitary, commute with leg exchange and total excitation
number, preserve the same input/output dimension and Born order unit, and
commute with operations on disjoint tensor factors. On the unnormalized
`|++>` vector, the coefficient determinant `ad-bc` is nonzero for both chosen
angles, so both have entangling capacity.

The SWAP/CNOT control independently gives probabilities `0` and `1` for the
same second-leg proposition on input `|01>`. The endpoint dual-gauge algebra
is correct for both. These witnesses establish at least two inequivalent
models under the shared instantiated constraints. The nonuniqueness theorem
does not depend on the stronger restored-process receipt.

The one-mode commitment root and evidence arithmetic also reproduce:

```text
h=0.609377863436006231536803371168398695428539279312854...
S(I+J)=S(I)S(J) for S(I)=exp(-I)
```

Using the same scalar coefficient and evidence clock for two supplied
operators cannot select between them.

## 4. What the 25-check implementation actually establishes

For one supplied diamond and initial state `|01>`, it constructs four fine
pointer histories `(first_record,second_record)`. The class operator is the
interaction followed by the second-leg and first-leg projectors. Fine pointer
histories decohere exactly because distinct final pointer projectors are
orthogonal. Their diagonal weights sum to one.

For each value of the second-leg record, summing over the later first-leg
record equals direct evaluation with only the second-leg projector. This is a
valid one-cell coarse-graining identity. Dividing a nonzero fine mass by its
coarse mass gives the corresponding conditional probability.

Conjugating the state, interaction, and both pointer families by the same
global `H tensor H` unitary leaves that four-cell law invariant. Two copies of
the interaction on disjoint tensor factors commute. These are correct finite
algebraic witnesses.

The restored program also embeds the classical parity conditional in the same
function-level API. That shows the API can accept a non-Markov law; it does not
make the quantum diamond model itself a multi-diamond non-Markov process.

## 5. Exact opening ledger

### Opening 1 — **MAJOR** — “continuation through 256 commits” is integer bookkeeping

The continuation loop is:

```python
live = len(diamond.outgoing)
for _ in range(256):
    live -= len(diamond.incoming)
    live += len(diamond.outgoing)
```

No output quantum state is fed into a later diamond. No later class operator,
history atom, screen, frame link, seal, birth, or conditional probability is
constructed. Since both arities equal two, `live` remains two identically.

This proves only an arity-level nonterminal type declaration. It does not
establish “continuation through 256 internal commits,” an indefinitely
continuing process, or a full projective whole-history law.

**Required repair:** compose at least several diamonds with explicit output
collars, states, ownership, outcomes, and truncation maps; then prove the
all-depth extension separately.

### Opening 2 — **MAJOR** — cylinder projectivity is one pointer deletion, not U3

Frozen U3 requires explicit truncation maps from fine/canonical diamond
histories to coarse histories and equality of pushed cylinder masses. The
program checks only four identities obtained by deleting the later first-leg
observation in one two-record diamond.

It has no multi-diamond history carrier, no canonical construction fibers,
and no family indexed by truncation depth. The summary line
`cylinder_projectivity=PASS` and Paper 13's unqualified projective PASS exceed
the receipt.

**Required repair:** rename this result `ONE-DIAMOND-POINTER-COARSE-GRAINING`,
or implement a genuine compatible cylinder family with explicit bonding maps.

### Opening 3 — **MAJOR** — integrated frame covariance is one global basis change

Frozen U7 requires independently changed vertex frames and transport of
states, effects, order units, instruments, links, anchors, screens, outcomes,
and canonical history data. Production applies the single frame
`H tensor H` to the initial state, interaction, and two pointer families.

There are no vertices, link transports, differing endpoint frames, order
units, screens, anchors, or output-collar frame data in `SealedDiamond`.
The resulting equality is valid representation covariance of one circuit,
not integrated generated-history gauge.

**Required repair:** rename the line `GLOBAL-CIRCUIT-BASIS-COVARIANCE`, or
construct the typed multi-vertex gauge test preregistered in U7.

### Opening 4 — **MAJOR** — construction-order gauge has no canonical fibers or weights

The code verifies

$$
(U\otimes I)(I\otimes U)=(I\otimes U)(U\otimes I).
$$

That is the expected disjoint-operator commutator. Frozen U4 additionally
requires all bounded auxiliary linearizations to be grouped into canonical
physical history fibers and their pushed probability or decoherence weight to
agree, while overlapping operations retain order.

No history linearizations, canonicalization map, fiber sum, probability
pushforward, or overlapping control is present in the restored executable.

**Required repair:** downgrade to `DISJOINT-OPERATOR-COMMUTATION`, or execute
the full history-level gate.

### Opening 5 — **MAJOR** — seal-and-birth is metadata, not an implemented rewrite

`SealedDiamond` declares equal incoming/outgoing type tuples and
`terminal=False`. Positive branches do not construct output collar objects,
durable record objects, owners, screens, frame links, or new opportunities.

This is enough to specify the intended countermodel type abstractly, but not
to claim that U1/U5 or `typed_seal_and_birth=PASS` was implemented.

**Required repair:** represent and validate the durable record and emitted
collars, including their state and ownership; distinguish declared metadata
from an executed birth operation.

### Opening 6 — **MAJOR** — promised architecture-class adjudication is incomplete

The protocol says every surviving class A–E must be implemented or killed by
theorem before selection. D12 supplies finite witnesses for a terminal global
control, a primitive classical history law, and a one-diamond amplitude law.
It does not execute a continuing local-evidence SCIR, a multi-time process
tensor/decoherence functional with canonical histories, or a threshold
representation proved equivalent to the same projective measure.

The nonuniqueness counterexample already refutes **unique derivation** among
the instantiated models. It does not make the promised comparative
investigation complete. Under the frozen verdict definitions this triggers
`INCOMPLETE-INVESTIGATION`.

### Opening 7 — **MODERATE** — `nonmarkov_full_history_api=PASS` is a detached classical cell

The non-Markov calculation is the three-bit parity law evaluated directly in
a separate dictionary. It shares no `SealedDiamond`, class operator, collar,
frame, seal/birth, or continuation object with the restored quantum model.

It proves that disintegration need not be Markov. It does not prove that the
implemented diamond process retains non-Markov dependence across diamonds.

**Required repair:** rename the receipt line to
`SEPARATE-NONMARKOV-DISINTEGRATION-WITNESS`, or integrate memory into the
diamond process.

### Opening 8 — **MODERATE** — next-click disintegration is tested only on deterministic conditionals

For the quarter-iSWAP input, the only nonzero fine histories are `(0,1)` and
`(1,0)`. Conditioning on the second-leg result therefore makes the later
first-leg record deterministic, and the check verifies two ratios equal to
one. It does not enumerate a nontrivial conditional distribution, prove its
normalization generally, or address zero-mass pasts.

The ratio formula is mathematically correct whenever the denominator is
positive. The receipt should describe this as a finite witness, not a general
implemented disintegration theorem.

### Opening 9 — **MINOR** — semantic hashes do not freeze complete stdout

All scripts gate a short semantic summary hash and expected check count, but
none gates the full stdout hash observed above. A changed sequence of detailed
checks could preserve the semantic summary. The source hashes and hostile
reproduction compensate manually.

Add a small wrapper that freezes normal/optimized complete stdout hashes for
the final receipt.

### Opening 10 — **MINOR** — generated bytecode remains under `v10/code`

Two D12 `.pyc` artifacts are present under `v10/code/__pycache__`. They are
not research sources and should not be part of a self-contained frozen
artifact set.

## 6. Claims that survive

The following Paper 13 claims are independently supported:

1. a supplied whole-history measure determines its positive-mass conditional
   extension law by cylinder ratios;
2. projective compatibility hosts many measures and does not select one;
3. the parity twins refute selection from all one/two-record shadows;
4. the quarter-/half-iSWAP family refutes selection by the shared executed
   symmetry, unitarity, conservation, entangling, and collar metadata;
5. complete log-RN coordinates identify a supplied positive finite law rather
   than choosing it;
6. an evidence clock or commitment coefficient conditional on supplied
   opportunities does not select the interaction operator;
7. V9 geometry cannot be used post hoc as a derivation principle; and
8. fields, action/process measure, couplings, initial state, extension grammar,
   record instrument, and scale remain empirical primitive data under the
   audited principles.

The boxed classical conditional

$$
P(e\mid H)={\mu([He])\over\mu([H])}
$$

is a definition/disintegration of a supplied measure, not a derivation of
that measure. Paper 13 generally states this distinction well.

The quantum diagonal formula additionally requires a consistent durable
record partition and decoherence (or a specified operational process-tensor
instrument). The one-diamond pointer model satisfies it; the code does not
establish it for an arbitrary continuing universe history.

## 7. Final determination

The clean no-go theorem is:

$$
\boxed{
\text{the audited shared structural constraints admit inequivalent laws,}
\quad
\text{so they do not uniquely derive the interaction/process measure.}
}
$$

That conclusion is valuable and should remain the headline. The executable
does not earn the stronger statement that a restored universal whole-history
diamond law passes local, projective, frame, construction, and continuation
gates. Several objects promised by the frozen protocol were not executed.

**Round-1 independent-rebuild verdict: MAJOR REVISION / `INCOMPLETE-INVESTIGATION`.**
