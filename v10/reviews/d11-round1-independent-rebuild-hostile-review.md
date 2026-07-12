# D11 hostile review, round 1: independent rebuild and reproduction

**Referee:** independent clean-room reconstruction  
**Date:** 2026-07-11  
**Verdict:** **MAJOR REVISION — extinction and kinematic containment reproduce, but the advertised complete typed packet and intervention receipt are overgraded**

The strongest D11 result is solid: with equal SPLIT, SEAL, and sibling-JOIN
activities, the open-port population has drift
`-j/(2p+j)`, immediate extinction probability `1/2`, and extinction almost
surely. I independently reproduced the frozen 72-history lifetime summaries
with a topology-only simulator, and both production programs are deterministic
at their frozen hashes. The Lorentz-cone placement identities and exact
instrument algebra also reproduce.

The package does not yet justify “complete typed rulebook” at the frozen
protocol's own level. Runtime tokens carry instrument **labels**, while their
actual matrices and firing logic live in global module state; JOIN outputs
silently inherit one input's order unit/frame link and have no parent link;
and the disjoint-schedule gate compares histories but not the promised path
probabilities. More seriously, the numerical `join_transfers` count does not
test changed later seal probabilities, which is D11's frozen definition of
influence. It counts any post-JOIN state **or position** difference. The exact
JOIN witness also compares `P0` with `P1`, not the frozen root intervention
`P0` versus `P+` propagated through an owned split/JOIN history.

These defects do not rescue the extinct population and do not refute the
existence of interaction in the partial-iSWAP channel. They require narrowing
or rewiring before the packet and influence claims receive PASS.

## 1. Frozen snapshot and exact reproduction

The submitted artifact hashes reproduce:

```text
728775ae57c90f6737ee1655933ec43ff29cf1f11003f521e5f087bc42b8fd08  v10/code/d11_complete_bloch_lorentz_exact.py
04d529f3ae790bf8bb39ad52d4c653fa450cb5841bd408524f853da8d116ccd0  v10/code/d11_generated_history_geometry.py
3679e66ef46eb554c7723b19cf5e1e81fc24798be4a8567b473d728c11f99940  v10/note-d11-complete-bloch-lorentz-scir-protocol.md
af87777d63cb929e744bbee4ce04c60e36facf4b84c2ee4af92014d59fc12634  v10/note-d11-complete-bloch-lorentz-scir-investigation.md
8e32c4d226ba4b5bd4675f852c0e5b829a0f558a6a5431a6d7096d084058d599  v10/note-d11-literature-audit-complete-packet-and-extinction.md
ff7bd46237eb0a4e58365c264219c49ac7a230c8a6ff5824a042eb38d0915ff5  v10/relativistic-isp-v10-paper12-complete-lorentz-rulebook-that-cannot-grow-a-universe.md
```

Commands executed:

```bash
PYTHONDONTWRITEBYTECODE=1 \
  python3 v10/code/d11_complete_bloch_lorentz_exact.py

PYTHONDONTWRITEBYTECODE=1 \
  python3 -O v10/code/d11_complete_bloch_lorentz_exact.py

PYTHONDONTWRITEBYTECODE=1 \
  /Users/felixrobles/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 \
  v10/code/d11_generated_history_geometry.py
```

The normal and optimized exact outputs are byte-identical:

```text
be58dff995e1103e08236d735370bf996e9cbd81de071d0d8e3bbd2e31b807be
```

They report 65 frozen checks, 117 cutoff-three path rows, 113 depth-12
projectors, support `0.914143429015`, and internal receipt digest
`64cbb0bd2691713145f8679211d01dda023b78f9f5b32d64e146c08ad3ff9de8`.

I ran the numerical campaign twice. Both complete outputs have SHA-256:

```text
3107fb0719a3de929fee1de3fdc086ebf535a56bf9e11d84e3cf49143a8295a7
```

Its internal digest is
`f073ed07f712c0d578dcd360ccf312be49129428beac20cf9c6bab8e142888e0`.

The exact executable freezes `EXPECTED_CHECKS=65`. The numerical campaign is
deterministic but has no analogous expected-output gate; its hash is frozen
only in the external receipt.

## 2. Independent transition and population reconstruction

For a state with `p>0` open ports and `j` enabled sibling joins, the enabled
race contains:

```text
p SPLIT tokens: Delta p=+1
p SEAL tokens:  Delta p=-1
j JOIN tokens:  Delta p=-1
```

A port can belong to at most one live sibling JOIN: splitting or sealing
either owner invalidates that JOIN, and a JOIN consumes both owners. Therefore
`0<=j<=floor(p/2)`. Unit activities give

$$
P(\Delta p=+1\mid H)={p\over2p+j},
\qquad
P(\Delta p=-1\mid H)={p+j\over2p+j},
$$

and hence

$$
E[\Delta p\mid H]=-{j\over2p+j}\le0.
$$

The total SEAL probability is

$$
{p\over2p+j}\ge {p\over 2p+p/2}={2\over5}.
$$

At the root `p=1,j=0`, so SEAL fires first with probability `1/2` and absorbs
the history immediately.

The almost-sure extinction argument is valid. The nonnegative population is
a supermartingale absorbed at zero. Stopping at `0` or `M` gives probability
at most `1/M` of reaching `M` from one port. Conditional on remaining in
`1,...,M-1`, a run of at most `M` SEAL firings has probability bounded below
by `(2/5)^M` and reaches zero. Repeated bounded blocks therefore cannot avoid
absorption forever. Letting `M` grow removes the escape alternative.

This proof depends only on ownership and race counts, not on quantum outcomes
or numerical seeds.

## 3. Independent numerical population campaign

I wrote a separate topology-only simulator using the frozen NumPy generator
and seeds. It represents only port IDs and live sibling pairs; it does not
import either D11 production module. It consumes the same one uniform draw per
selected instrument outcome because outcomes do not alter topology.

It reproduced exactly:

| cutoff | terminal | median clicks | maximum | longest event counts `S/Q/J` | maximum open |
|---:|---:|---:|---:|---|---:|
| 512 | 24/24 | 1 | 49 | seed 20276009: `24/19/6` | 7 |
| 1024 | 24/24 | 3 | 171 | seed 20277010: `85/70/16`; seed 20277013: `85/71/15` | 12/11 |
| 2048 | 24/24 | 1 | 47 | seed 20278003: `23/21/3` | 6 |

The next-longest histories and their counts also match production. This is a
strong independent confirmation that termination is a property of the frozen
token race, not the Bloch geometry implementation.

The production numerical summaries also reproduce deterministically:

```text
JOIN-transfer histories   3/24, 9/24, 5/24
rank-four clouds           3/24, 5/24, 4/24
median support             -1.0000, -0.8515625, -1.0000
ancestry violations        0
reported influence violations 0
valid generated F_dom      1,3,1
valid generated F_m4       1,0,0
M4 m4-axis valid           24/24 at each rung
M4 dom-axis valid          0/24 at each rung
```

No survivor conditioning or parameter sweep occurs. Invalid `F` values remain
NaN and are not averaged. The failure precedence returns `INTERACTION-INERT`
because its JOIN gate fails before support/rank are graded.

The population and verdict failure are robust to the influence-count defect
below: a stricter seal-probability transfer count can only reduce the current
`3/9/5`, so it cannot reach `20/24`.

## 4. Exact algebra that passes

Independent matrix arithmetic confirms:

- dual event/effect/order-unit transformation leaves
  `Tr(EX)/Tr(eX)` invariant;
- endpoint-transformed Kraus legs satisfy the transformed completeness law;
- the two SPLIT legs each have weight `1/2` and produce
  `U_g rho U_g^dagger` plus a fresh `P0` ancilla;
- partial-iSWAP is unitary and the two measured/discarded JOIN legs are
  complete;
- projective SEAL is complete and repeatable;
- `Y_c=Y_a+Y_b-Y_o` puts the JOIN output in both parents' algebraic futures;
- setting the output naively to `Y_a` can violate the other parent's future;
  and
- the exact H/T orbit counts and external sampled support match D10.

The positivity containment is a construction theorem, not an emergent
measurement, and Paper 12 mostly says so correctly.

## 5. Numbered hostile openings

### Opening 1 — **MAJOR** — tokens do not contain the frozen packet matrices

Protocol section 2.3 requires every candidate token to store its packet
matrices. The executable token is:

```python
Token(tid, kind, owners, anchor, activity, packet)
```

but `packet` is only a string such as `"K_H/K_T"`, `"P0/P1"`, or
`"J0/J1"`. `fire()` dispatches by `kind` into functions that read global
module matrices `H,T,P0,P1,j0,j1,u_ps` and global rewrite code. Thus the
next-history law is reproducible as a Python module, but it is not contained
in the typed token/history object promised by the protocol.

This is silent global packet state, exactly the failure mode the review was
asked to exclude. The investigation note accurately says “instrument labels,”
but Paper 12 says a token stores its “instrument packet” and calls the rulebook
fully specified locally.

**Required repair:** store immutable matrix/outcome data or a frozen typed
packet identifier resolved through an explicitly declared packet registry that
is part of the history-law definition. State which data are universal packet
constants versus record-carried fields; do not claim the token itself stores
matrices if it stores labels.

### Opening 2 — **MAJOR** — JOIN continuation typing silently chooses the left input frame

The protocol requires each open carrier to have a parent frame link and local
order unit. `join_outcomes()` consumes two parents and creates:

```python
Port(..., parent=None,
     order_unit=left.order_unit,
     frame_link=left.frame_link, ...)
```

The record incidence correctly lists both parents, but the continuing port has
no parent link and silently inherits only the left parent's frame data. This is
harmless in the current root-gauge simulations because all generated links are
the identity/inherited copy. It is not a complete covariant multi-parent port
rule once the noncommuting local frames tested in G0 are allowed.

The algebraic gauge witness and the generative history engine are therefore
parallel constructions, not yet one fully typed gauge-covariant JOIN packet.

**Required repair:** give JOIN outputs explicit links from the anchor and/or
both inputs, transform both input states into the recorded anchor frame before
applying `J_b`, and derive the output order unit/link. Add a nonunitary,
different-parent-frame generative JOIN test rather than only a separate static
matrix identity.

### Opening 3 — **MODERATE** — construction gauge omits schedule probabilities

Frozen G3 requires disjoint schedules to give identical canonical histories
**and probabilities**. Production deterministically chooses one SPLIT outcome
on each child and checks only

```python
canonical(lr) == canonical(rl)
```

It never multiplies the enabled-token race shares and Born weights for the two
orders.

For this particular witness the missing equality is true: the first selected
SPLIT has race share `1/5`, the second `1/7`, and both selected H/T outcomes
have weight `1/2`, giving `1/140` in either order. But the receipt did not
execute its preregistered probability gate, and a future activity or
state-dependent outcome change could break it silently.

**Required repair:** compute and compare the two full path weights, including
race denominators and outcome probabilities.

### Opening 4 — **MAJOR** — numerical `join_transfers` is not the frozen influence observable

D11 defines intervention by a changed later seal distribution. Numerical code
increments `join_transfers` when an input differed and the JOIN output has
either a different density matrix **or a different event position**:

```python
if (left_changed or right_changed) and
   (differs(rho, rhoi) or differs(y, yi)):
    join_transfers += 1
```

It does not test whether `Tr(P0 rho)` differs from `Tr(P0 rhoi)` after the
JOIN, nor whether any later seal distribution changes. A pure phase/coherence
difference or coordinate-only difference can therefore be counted as
“JOIN-transmitted influence” even when the packet's only P0/P1 seal law is
unchanged.

Paper 12 reports histories with “JOIN-transmitted influence” and says those
counts prove a working local mechanism. That noun does not follow from the
implemented metric.

**Required repair:** count a transfer only when a declared downstream
instrument distribution differs, preferably by explicitly continuing to a
seal. Report state transfer, coordinate response, and seal-probability
influence as separate observables.

### Opening 5 — **MODERATE** — the exact JOIN influence witness is not the frozen root intervention history

The exact receipt proves that nonselective JOIN outputs differ for first input
`P0` versus `P1`, with second input `P0`, and that one P0 seal probability
changes. That is a valid channel-dependence witness. Frozen G5, however,
specifies worlds with root `P0` and root intervention `P+`, followed through
the packet, including a JOIN.

The carrier/ancilla checks use the frozen `P0/P+` pair, but no owned
split-sibling JOIN continuation is constructed from those worlds and checked
at a later seal. The generic `P0/P1` channel witness and the frozen causal
intervention were silently combined in the prose label “JOIN transfer.”

**Required repair:** build the same typed split/JOIN/seal history in both
`P0/P+` worlds and compare its exact later P0/P1 law, or narrow G5 and the
paper to an independent channel-dependence witness.

### Opening 6 — **MODERATE** — finite-cutoff mass is overnamed cylinder projectivity

The executable iterates a normalized kernel to cutoffs one through three and
checks total mass one. Terminal histories are carried forward by an absorbing
self-loop. This proves finite-level normalization for the enumerated path
rows. It does not explicitly push the cutoff-`n+1` cylinder law back to
cutoff `n` and coalesce prefixes.

That projective identity follows from a normalized kernel, so the path measure
claim is repairable and likely correct. The receipt should execute the actual
prefix marginal rather than label total-mass checks “projective.”

### Opening 7 — **MINOR** — numerical receipt integrity is external only

The numerical program has no frozen expected summary/hash gate and does not
support an optimized-mode comparison. Its deterministic hash is preserved in
the pre-review Markdown receipt, and I reproduced it twice, but a changed
campaign would still exit successfully while printing a new digest.

Add a small standard-library wrapper that executes the bundled interpreter,
checks the frozen stdout hash, and records its NumPy/Python versions.

## 6. Other scope findings

The extinction theorem is not blocked by any opening above. Nor is the
negative numerical diagnosis: all 72 histories terminate, and a stricter
influence definition only strengthens failure of the frozen `20/24` gate.

The `SEAL -> COMMIT` proposal is presented as a next hypothesis, not a derived
law. Its population arithmetic is correct: increments `+1,0,-1` give drift
`(p-j)/(2p+j)>0` because `j<=p/2`. Positive drift does not establish a viable
or nonexplosive cosmology, and both note and paper retain that caveat.

The M4 convention handling is honest: the m4/time-axis controls are averaged
only when valid, the diagonal/dominant-axis controls are refused rather than
imputed, and no generated roundness claim is made.

Existing `__pycache__` artifacts are present under `v10/code/`. They are not
used by the commands above because `PYTHONDONTWRITEBYTECODE=1` was set, but a
final self-containment receipt should remove or explicitly exclude generated
bytecode artifacts.

## 7. Final determination

The independently supported D11 result is:

$$
\boxed{
\text{the frozen equal-activity topology becomes extinct almost surely,}
\quad
\text{while its supplied algebraic placements remain cone-positive.}
}
$$

That is a valuable and reproducible falsification. The stronger label
`COMPLETE-KINEMATICS/INFLUENCE-ENVELOPE-OPEN` is premature because the
generative token objects do not contain their promised packet data, the JOIN
frame/link output is under-typed, and the numerical JOIN influence statistic
does not implement the declared seal-distribution observable.

**Round-1 independent-rebuild verdict: MAJOR REVISION.**
