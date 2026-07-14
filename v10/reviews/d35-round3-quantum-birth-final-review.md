# D35 round 3 — quantum, birth and carried-evidence final review

**Frozen target:** commit
`8a9bb98da2a37d61f5887fa69d397792ed0f4807`.

**Lane:** common-input variable-support operators, direct-sum flags, D24 birth
instant, bounded outcome versus structural provenance, and the D-source
intervention.

**Verdict:** **THE TWO ROUND-2 MAJORS ARE CLOSED. THE LIMITED CONNECTED
ACQUISITION RESULT AND THE REGISTERED-SECTOR DIRECT-SUM INSTRUMENT ARE
EARNED. ONE DISCONNECTED-CONTROL DESCRIPTION REMAINS TOO STRONG.**

**Count:** **0 blockers / 0 majors / 1 minor / 0 nits.**

The closing companion supplies the missing mathematics rather than repeating
the D35b labels. It constructs five maps on one common local input, injects
them into genuinely disjoint output blocks, and transports a non-A bit through
actual D-to-B-to-A returns into durable A2 fields. It continues to refuse a
coherent superposition over graph sectors and a unique birth law. The only
remaining defect in this lane is that the disconnected source is called
“isomorphic” although the coded remote specimen is not isomorphic to the
connected D source seal.

## 1. Independent exact reproduction

I ran the closing executable under fresh hash seeds `173`, `20260714` and
`4294967291`. All three executions exited zero and were byte-identical to the
committed receipt.

```text
source SHA-256
50f1e710cc04de3576b24bd5e7414764f1dea1ebb86f0b0b5747d2b18109c765

stdout SHA-256
d8f0ef0c4320ff58badcff6ce6916fe7a3f4adb94b58de8afd95c4aa09bb6f42

internal science SHA-256
da82ce3ca611fd2e51f0d0e4fd3a36ec74edb895c279e9f6bcd48ac8ceb5aebf

verdict
PASS 16/16
```

The reproduced receipt gives, in each of Q1 and Q2:

```text
common input                         8
direct-sum output                    48
structural alternatives             5
bounded action kinds                 4
self-Gram identities                 5/5
cross-alternative zero Grams         10/10
weighted Gram identity               exact
D queried / unqueried histories      6 / 10
first / second projectivity          16 / 408 / 408.
```

The calculations below use independent matrix and history constructors. I did
not use `common_flagged_instrument` or `remote_evidence_gate` to generate the
expected answers.

## 2. Common-input reconstruction

### 2.1 Five maps and their placement

I independently ordered the local input basis lexicographically as
`|A B C>` and reconstructed the alternatives in the executable's menu order:

| alternative | raw map | action on the common input | rows in the 48-dimensional output |
|---|---:|---|---:|
| birth | `16 x 8` | controlled D24 birth `A -> N`, identity on B and C | `0..15` |
| fork `(B,C)` | `8 x 8` | controlled rotation `A -> B`, then `A -> C` | `16..23` |
| idle | `8 x 8` | `I_A tensor I_B tensor I_C` | `24..31` |
| visit B | `8 x 8` | controlled rotation `A -> B`, identity on C | `32..39` |
| visit C | `8 x 8` | controlled rotation `A -> C`, identity on B | `40..47` |

Thus every raw map has eight columns. Birth has sixteen rows because it maps
`|A B C>` to `|A B C N>`; the other four have eight. Their row counts sum to
`16+8+8+8+8=48`. Padding each raw map with zero rows outside its assigned block
produces five explicit `48 x 8` injections `W_o`.

The independently serialized raw matrices have these SHA-256 fingerprints:

```text
Q1 birth  50411bd0ccb8a28031c7ec652f534da514f78facdbfa42c6001fff7b19133640
Q2 birth  21a92ed93b2afb3bac8ce121472c3f9f90ac046657c79f52421303763a8f468a
fork      7d6ab12b0c580ab41af98729c0bcc6c583846dbec45c2ed582c10daa67d234fd
idle      33eeaa6d614191358e3359af8c0ba003616407e4161fda2588c081b34a8b7a85
visit B   33e61064fabc430049252482d1e1aa5fd00e12e46952ce5ac9b4fc9a2605372c
visit C   d638d1f1dd9dfde312c2794b58afbb7c514202c39cfa99f04d73ff76db3cbe95
```

All five independently constructed matrices equal the candidate matrices
entry for entry in both parameter cells.

### 2.2 Self, cross and weighted Gram identities

Direct exact multiplication gives

```text
W_o^T W_o = I_8                         for all 5 alternatives;
W_o^T W_p = 0_8                         for all 10 unordered o != p pairs.
```

The weights used in the two cells are:

```text
Q1: birth 1/4, fork 1/8, idle 3/8, visit-B 1/8, visit-C 1/8;
Q2: birth 1/5, fork 1/10, idle 2/5, visit-B 3/20, visit-C 3/20.
```

They sum to one exactly. Therefore the independently accumulated matrices
satisfy

```text
sum_o q_o W_o^T W_o = I_8
```

entry for entry in Q1 and Q2. This closes round-2 M1: the cross-range result is
now an operator calculation on one common domain, not the cardinality of five
Python labels.

### 2.3 Spectators and the actual quantum noun

Basis support checks establish all intended spectator identities:

```text
birth preserves B and C on every nonzero matrix element;
visit-B preserves C on every nonzero matrix element;
visit-C preserves B on every nonzero matrix element.
```

The maps are local maps on the `A/B/C` registered sector; any carrier outside
that sector is an identity extension. The receipt does not claim that 48 is
the dimension of the complete grown universe carrier.

For density operators the branch operations can be written exactly as

```text
I_o(rho) = q_o W_o rho W_o^T.
```

Their sum is trace preserving, and the direct-sum blocks retain the classical
alternative. “Classical-output common-input direct-sum quantum instrument at
the registered local sector” is therefore earned. No appeal to a tuple label
or an unconstructed square root is needed.

The terminal section correctly stops short of the stronger claims rejected in
the earlier rounds. It does not call this a coherent amplitude sum over
changing support graphs, does not claim NSE closure for the complete history
law, and does not select D24 from the broader D25/D27/Busch class. Earlier
pre-review Busch language is preserved as historical candidate text; section
17's final noun is the narrower one supported by the closing construction.

## 3. D24 birth instant and nonselection

The independently reconstructed birth map obeys the operator identity

```text
B_g^T (I_ABC tensor |1><1|_N) B_g
  = g (|1><1|_A tensor I_B tensor I_C)
```

with `g=9/25` in Q1 and `g=16/25` in Q2. This proves
`P(N=1)=g P(A=1)` for arbitrary input density operators, including inputs
entangled with spectators.

The executable also evaluates the marginal at the correct event instant:
parent occupancy is read, the fresh child is created in zero, the controlled
rotation is applied, and the newborn occupancy is checked before any later
event. Independent enumeration found 12 generated-birth checks per cell and
only these exact distinct rows:

```text
Q1, g=9/25:
16/25 -> 144/625
144/625 -> 1296/15625
1296/15625 -> 11664/390625

Q2, g=16/25:
16/25 -> 256/625
256/625 -> 4096/15625
4096/15625 -> 65536/390625.
```

Every row is exact. Q1 and Q2 still disagree on both birth and visit
probabilities, so the closing does not convert D24 into a uniqueness or
selection theorem.

## 4. Bounded outcomes versus structural provenance

The five root alternatives comprise four bounded action kinds:

```text
idle, birth, visit, fork.
```

The second visit sector is not a fifth action kind; it is the same `visit`
outcome with different port incidence. The complete alternative still records
which port was used, while transaction number, path, address and route remain
in structural provenance. Section 17.4 states this distinction explicitly and
does not call the unbounded provenance a bounded-rank flag. This is the
separation requested by round-2 M1.

The full classical sector at degree two has five alternatives, while its
coarse action-kind alphabet has four values. Those two statements are
compatible and are not evidence that general degree has a five-dimensional
outcome space.

## 5. D-source paired intervention

### 5.1 Independent pairing and exact support

I paired `do(D=0)` and `do(D=1)` branches by an independently constructed
structural signature consisting of generated event address, initiator,
operation, typed target legs, route and coupling. Source values, generated
payloads and the candidate's `physical_key` pairing helper were excluded.

For both Q1 and Q2 the result is:

```text
branches under do(D=0)             16
branches under do(D=1)             16
distinct paired structural keys    16
support mismatch                     0
probability mismatch                 0
D queried through A->B->D            6 histories
D not queried                        10 histories.
```

The probability mass of the six queried histories is `1/16` in Q1 and `3/40`
in Q2. In every queried pair the durable A2 fields change exactly from

```text
(output bit, positive-source set) = (0, empty)
```

to

```text
(output bit, positive-source set) = (1, {(0,0)}).
```

In all ten unqueried pairs both A2 fields remain unchanged. The structural
route separately records a queried zero-valued D source, so absence from the
positive-source set is not used as the complete provenance record.

### 5.2 The evidence is carried and durable

On each queried branch the source occurs on three generated records:

```text
D result   route (root,B,D), output 1, sources {D};
B merge    route (root,B),   output 1, sources {D};
A2 merge   route (root),     output 1, sources {D}.
```

The bit and source set are fields of `CarriedReturnEnvelope`; the evidence
digest is computed from those fields, and the return signature covers that
digest. The accepted result is stored in `output_payloads` and
`output_sources` indexed by the immutable generated event and is included in
the physical history key. All 408 second-call refinements preserve the earlier
payload fields. This is a durable record field, not only a transient mailbox
bit or a digest whose decoded content was discarded.

I additionally drove the concrete `A visit B; B visit D; D idle` branch and
attacked the pending D return four ways. Exact results were:

| attack | rejected | complete logical state unchanged | reason |
|---|---:|---:|---|
| change output bit | yes | yes | `return payload mismatch` |
| change source set | yes | yes | `return source-set mismatch` |
| change evidence digest | yes | yes | `return evidence mismatch` |
| change signature | yes | yes | `invalid return signature` |

The unmodified return then completed D-to-B and B-to-A with A2 bit one and D
in its source set. The connected queried/unqueried comparison therefore
closes round-2 M2 at the manuscript's deliberately limited width: one bounded
classical evidence channel, not arbitrary quantum information or all ancestral
correlations.

## 6. Minor finding

### m1 — the disconnected source is not isomorphic to the connected D source

Section 17.1 says that changing “an isomorphic disconnected source” leaves the
A2 projected law fixed. The executable does not construct that specimen.

The connected intervention adds `D-source-seal` to the existing D wire with
predecessor `BD`, flag `("bounded-source-bit", bit)`, actor evidence fields and
an address `(0,0)`. The disconnected control instead reuses D35b's
`remote_collision` fixture: one `REMOTE-X` actor in the shared audit world and
one predecessor-free `remote-display-collision` event whose flag is a changed
metadata string. It is not in `network.actors`, has no source-set field, and is
not structurally isomorphic to the D source seal. The comparison then applies
`root_observable_distribution`, which intentionally projects away all remote
metadata.

This does show that the supplied remote metadata collision cannot affect the
chosen A2 projection. It does not establish the stated isomorphic-disconnected
control. Repair either by:

1. constructing a disconnected actor/wire/source-seal copy with the same
   bounded source fields and comparing the complete connected-component A2
   law; or
2. replacing “isomorphic disconnected source” by “supplied disconnected
   metadata source” and treating the connected unqueried D pairs as the
   load-bearing exclusion control.

This is minor because the operational acquisition theorem already has the
strong paired connected control: the same D source, same structural support
and same branch weights change A2 in exactly the six histories that query D
and in none of the ten that do not. No probability, carrier or connected
acquisition conclusion depends on the remote fixture.

## 7. Final disposition

| Audit target | Disposition |
|---|---|
| Fresh exact receipt reproduction | pass |
| Common `8`-dimensional input | pass |
| Explicit `48 x 8` flagged injections | pass |
| Five self-Gram identities | pass |
| Ten cross-range zeros | pass |
| Q1/Q2 weighted completeness | pass |
| Named-target spectator placement | pass |
| D24 marginal at the birth instant | pass |
| D24/weights/coupling uniqueness refusal | honest |
| Bounded action kind versus structural incidence | pass |
| Coherent graph-sector refusal | honest |
| D-source paired structural support and probabilities | pass |
| Carried D bit/source through D-to-B-to-A | pass |
| Durable A2 evidence fields | pass |
| Unqueried connected exclusion | pass |
| Isomorphic disconnected source control | **not constructed; minor** |

**Final count:** **0B / 0M / 1m / 0n.**

**Final verdict:** accept the registered-sector classical-output direct-sum
instrument and the limited connected remote-evidence acquisition theorem.
Do not promote either to a coherent graph-sector law, a complete quantum
acquisition theorem, a unique D24/Busch law, or a root-free universe law. Fix
or narrow the single disconnected-control sentence before calling that
particular control isomorphic.
