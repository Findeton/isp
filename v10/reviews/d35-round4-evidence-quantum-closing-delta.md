# D35 round 4 — evidence/quantum closing delta

**Frozen target:** commit
`d414c56de480fd692630c1d7b3b10ada44cb60f7`.

**Delta lane:** the round-3 disconnected-source minor, exact D-reach mass, and
regression of the accepted common-input instrument and D24 birth result under
typed storage.

**Verdict:** **CLEAN. THE DISCONNECTED CONTROL IS NOW THE CLAIMED MARKED
ANCESTOR-GADGET COPY, ITS BIT FACTORS FROM THE COMPLETE CONNECTED A LAW, AND
THE ACCEPTED QUANTUM/BIRTH RESULTS ARE UNCHANGED.**

**Count:** **0 blockers / 0 majors / 0 minors / 0 nits.**

## 1. Fresh exact reproduction

I ran `d35d_typed_identity_terminal_exact.py` under fresh hash seeds `31337`,
`2026071401` and `2147483629`. All three executions exited zero and were
byte-identical to the committed receipt.

```text
source SHA-256
9ef590992e04beec0672a3772d41e1e01cde8315b65b7cd0aaa207a649c56e28

stdout SHA-256
2150ddecfe92d3d0f2db6505a3e3ccc1c5c8685a4a2ea5a0497280939a023574

internal science SHA-256
79e29b8fd5f5a294b3c2faf438ffcca45434ec78af55b4150324b9939a03f26c

verdict
PASS 18/18
```

`git diff --check 8a9bb98..d414c56` is clean.

## 2. The disconnected control is the claimed isomorphic record gadget

I reconstructed both four-event marked ancestry graphs directly from the
stored actor/event objects. After quotienting only their identity domains and
names, the isomorphism is:

| connected D ancestry | disconnected control | kind | actor incidence | predecessor |
|---|---|---|---|---|
| `A0` | `u0` | seed | root actor | none |
| `AB` | `uv` | seed-birth | root, child | seed |
| `BD` | `vw` | seed-birth | child, grandchild | first birth |
| `D-source-seal` | `w-source-seal` | source-seal | grandchild | second birth |

The induced actor relations are likewise identical:

```text
A -> B -> D
u -> v -> w.
```

For source bit zero, both terminal flags are exactly
`("bounded-source-bit", 0)`; for source bit one, both are exactly
`("bounded-source-bit", 1)`. Exhaustive comparison of actor parent/child
incidence, event kind, actor touches, predecessor incidence and flags returns
exact equality in both Q cells and at both bit values.

The differences are precisely the declared ones:

- supplied connected identities and control identities inhabit disjoint
  `TypedId` domains;
- the control chain is a separate component with no actor edge, event touch or
  predecessor crossing into the A component; and
- `do(control=0)` versus `do(control=1)` changes only the terminal bounded-bit
  mark.

This is an isomorphism of the stated four-event **record ancestor gadget**. It
does not assert that the disconnected control is an independently callable
logical actor network or that its quantum preparation equals the connected
A/B/D carrier. The note claims neither stronger object.

The round-3 minor is therefore closed. The former one-event
`remote-display-collision` fixture has been replaced by the required marked
seed/birth/birth/source-seal component.

## 3. Disconnected intervention factorization

I independently enumerated the histories from otherwise identical initial
states under `do(control=0)` and `do(control=1)`.

For both Q1 and Q2:

```text
root-observable distributions equal                 yes
complete connected physical distributions equal     yes
connected physical atoms under each intervention     16
probability mismatch                                  0.
```

The second comparison is stronger than the receipt's printed coarse
projection. It includes the full connected actor rows, generated event rows,
carrier amplitudes and transfer rows used by the physical history quotient.
The disconnected source mark does not enter any queried route, generated
record, carrier action or A2 evidence field.

The control works by actual graph disconnection, not by a special probability
renormalization: the opportunity menus and all branch weights are identical
before projection.

## 4. Independent connected reach masses

The six queried histories have a simple exact decomposition.

In Q1, D is reached either through root visit-B or through root fork:

```text
visit route:  P(A visits B) P(B visits D) = (1/8)(1/4) = 1/32;
fork route:   P(A forks)    P(B visits D) = (1/8)(1/4) = 1/32;
total                                                = 1/16.
```

The fork's C subtree sums to one and therefore contributes no additional
factor. In Q2:

```text
visit route:  (3/20)(3/10) = 9/200;
fork route:   (1/10)(3/10) = 3/100 = 6/200;
total                                    = 15/200 = 3/40.
```

Direct summation over independently selected final A2 source fields reproduces:

```text
Q1: 6 queried, 10 unqueried, reach mass 1/16;
Q2: 6 queried, 10 unqueried, reach mass 3/40.
```

The history count follows independently: root visit-B with D's two leaf
outcomes gives two queried histories; root fork with D's two outcomes and C's
two outcomes gives four. Thus `2+4=6` without using the candidate's counter.

## 5. Quantum-instrument regression

D35d hash-locks the accepted D35c source and changes storage identities, not
the local operator constructors. I nevertheless compared typed D35d and
pristine D35c in separate module instances.

For both Q cells:

```text
complete typed versus D35c physical distribution     exact equality
root kind distribution                               exact equality
instrument tuple                                     (5, 8, 48, 10, 4)
```

The five raw-operator hashes remain:

```text
Q1 birth  50411bd0ccb8a28031c7ec652f534da514f78facdbfa42c6001fff7b19133640
Q2 birth  21a92ed93b2afb3bac8ce121472c3f9f90ac046657c79f52421303763a8f468a
fork      7d6ab12b0c580ab41af98729c0bcc6c583846dbec45c2ed582c10daa67d234fd
idle      33eeaa6d614191358e3359af8c0ba003616407e4161fda2588c081b34a8b7a85
visit B   33e61064fabc430049252482d1e1aa5fd00e12e46952ce5ac9b4fc9a2605372c
visit C   d638d1f1dd9dfde312c2794b58afbb7c514202c39cfa99f04d73ff76db3cbe95
```

Consequently the already independently accepted identities remain literal
matrix identities:

```text
common input dimension                    8
direct-sum output dimension              48
self-Gram identities                    5/5
cross-alternative zero Grams           10/10
weighted Gram identity                    I_8 exactly
bounded action-kind rank                   4.
```

Typed identity storage does not add a carrier factor, change a matrix entry or
alter an opportunity weight. The final wording remains appropriately limited
to a classical-output common-input direct-sum instrument at the registered
local sector, not a coherent graph-sector sum.

## 6. D24 birth regression

The typed birth constructor still reads parent occupancy immediately before
adding the fresh child, applies the same controlled rotation, and reads the
child immediately afterward. Independent enumeration found 12 generated-birth
checks per Q cell, all satisfying `after = g before` exactly.

The distinct rows are unchanged:

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

No typed identity enters `p_one`, the exact carrier amplitudes or the D24
coupling. The accepted newborn-instant result and the refusal to select a
unique `g` both survive unchanged.

## 7. Final disposition

| Delta target | Disposition |
|---|---|
| Fresh exact receipt reproduction | pass |
| Four-event marked gadget isomorphism | pass |
| Control identity/domain separation | pass |
| No cross-component actor/event incidence | pass |
| Disconnected `do(0/1)` root projection | pass |
| Complete connected physical-law equality | pass |
| Q1 reach mass `1/16` | pass |
| Q2 reach mass `3/40` | pass |
| Six queried / ten unqueried histories | pass |
| D35c versus typed physical distribution | pass |
| Common `8 -> 48` instrument | unchanged and pass |
| D24 newborn instant | unchanged and pass |
| Coherent-sector and uniqueness refusal | honest |

**Final count:** **0B / 0M / 0m / 0n.**

**Final verdict:** the evidence/quantum delta is terminally clean at the
declared supplied A-rooted laminar scope. The disconnected-control wording may
now use “isomorphic marked ancestor gadget.” Nothing in this delta promotes
the result to a callable disconnected actor theorem, a coherent support-sector
law, a unique birth law or a root-free universe law.
