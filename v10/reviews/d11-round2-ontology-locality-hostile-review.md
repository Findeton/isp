# D11 hostile ontology/locality review — round 2 closure

**Date:** 2026-07-11  
**Verdict:** **MAJOR REVISION — ONE NEW BLOCKER**

The round-1 locality and scope blockers have either been repaired at their
declared finite-packet scope or explicitly retained as open. D11 now honestly
describes a globally raced finite-prefix kernel with incidence-scoped
instruments, sibling-only interaction, a separate covariance template, and
algebraic cone containment. It no longer presents that packet as the final
decentralized click law, a generated spacetime, an ISP implementation, a
general bridge law, or a derivation of COMMIT.

One new ontology blocker prevents PASS. The immutable `DurableOutcome`
objects do not consistently store the outcome effect belonging to the rule
and owned input space. The executable branch probabilities remain correct,
but the durable records are not yet truthful self-descriptions of the events
that created them.

## Frozen repaired artifacts audited

- `v10/note-d11-round1-opening-repairs.md`
- `v10/code/d11_complete_bloch_lorentz_exact.py`
- `v10/note-d11-complete-bloch-lorentz-scir-investigation.md`
- `v10/relativistic-isp-v10-paper12-complete-lorentz-rulebook-that-cannot-grow-a-universe.md`

Their SHA-256 hashes at review were:

```text
74005bf2c840835b9c75cf59ee6081098405f53e564918ec54e3f5b8100cc0b4  note-d11-round1-opening-repairs.md
248dc3dad3ba33b4b1a5e3f61c82a0cbe75ec74ad9e7b22ad9b9c68ba5006313  d11_complete_bloch_lorentz_exact.py
71cd88673aff81dd9dff145225c5479c6b053547cdd0a0192223f62e5523a92b  note-d11-complete-bloch-lorentz-scir-investigation.md
1fe738a570ded336d1dc8d1067511461c42091fa87b049e48036aa324e4d3452  relativistic-isp-v10-paper12-complete-lorentz-rulebook-that-cannot-grow-a-universe.md
```

The exact engine reproduces **72/72** checks. Its internally frozen summary
receipt is:

```text
7ae48df9da9853a581f262fbc74f183ead19f2745e64b57ebef0362addf7f5d6
```

## Round-1 closure table

| Obligation | Round-2 finding |
|---|---|
| Actual matrices in executable tokens | **CLOSED.** `Token.packet` contains `(K_H,K_T)`, `(P0,P1)`, or `(J_0,J_1)`, not matrix names or placeholders. |
| Durable typed outcomes | **BLOCKED.** The type exists and survives in history, but SPLIT and sibling-MERGE store the wrong input effects; see the blocker below. |
| Multi-parent JOIN provenance | **CLOSED at sibling-only scope.** A merged carrier stores both input ports in `parents`; the opportunity carries its common anchor position, order unit, and frame link; the child inherits those anchor data rather than arbitrarily copying one input. |
| Growing ancestry payload | **CLOSED for the identified payload.** `ancestry_word` is absent. Live ports retain parent identifiers and provenance is distributed through immutable records. Expanding identifiers and exact coordinate-description capacity remain acknowledged future finite-record questions, not secretly solved ones. |
| Global race versus local clicking | **HONESTLY OPEN.** Candidate construction is incidence-scoped, but normalization is over all enabled tokens. Paper and notes explicitly refuse equivalence to decentralized proper-time clocks. |
| Generated gauge history | **HONESTLY OPEN.** The dual `SL(2,C)` calculation is called a separate covariance template; generated histories still run in one root frame. |
| Construction-order gauge | **HONESTLY OPEN.** One disjoint-SPLIT cell has equal canonical state and exact presentation mass `1/140` in either order. No general canonical marked-history pushforward is claimed. |
| General joining or component bridge birth | **HONESTLY OPEN.** `JOIN` is renamed/qualified as sibling-MERGE and cannot connect unrelated components. |
| Physical spacetime | **HONESTLY OPEN.** The text distinguishes ancestry, positive displacement, coordinate shadow, and intervention. Cone containment is not promoted to a derived physical metric or influence envelope. |
| ISP / Barandes dynamics | **HONESTLY OPEN.** D11 is presented as a Markov law on augmented typed history. Barandes is used as a boundary comparison, not as a theorem selecting this grammar or race. |
| COMMIT successor ontology | **HONESTLY OPEN.** COMMIT is a motivated next packet, not a consequence of sealing, SHARD, or Barandes. Alternative terminal and birth ontologies remain live. |
| `INTERACTION-INERT` semantics | **CLOSED in interpretation.** The frozen registry string remains for provenance, but the physical diagnosis is now `population-extinct / interaction-sparse`; the exact sibling-interaction mechanism is not denied. |
| Primary verdict | **CLOSED.** `INCOMPLETE-PACKET` accurately reflects the unclosed decentralized law, integrated gauge, projective pushforward, general bridge, and spacetime envelope. |

## New blocker — the durable record misidentifies its evidence effect

**Severity:** major

`DurableOutcome.effect` is naturally read as the effect on the owned input
space whose Born weight produced that outcome. Terminal-SEAL satisfies that
meaning, but SPLIT and sibling-MERGE do not.

### SPLIT

Each SPLIT leg is

```text
K_g = 2^(-1/2) (U_g tensor |0>),  g in {H,T}.
```

Therefore its input-space outcome effect is

```text
E_g = K_g^dagger K_g = I_2/2.
```

The immutable outcome instead stores `I2`. The executable separately assigns
the correct branch probability `1/2`, so the transition law is right while
the durable record says the event had unit weight. This breaks the intended
link from finite evidence record to the actual outcome law.

### Sibling-MERGE

Sibling-MERGE owns two qubit inputs and uses

```text
J_b : C^4 -> C^2.
```

Its input-space outcome effect is consequently

```text
E_b = J_b^dagger J_b,
```

a `4 x 4` operator on the joint owned domain. The immutable outcome stores
the `2 x 2` projector `P_b`. That projector labels the measured discarded
output; it is not the POVM effect on the two input records. The current type
does not name an operator domain or distinguish a pointer/readout projector
from an input evidence effect.

### Terminal-SEAL

For terminal-SEAL, `P0/P1` is correctly the effect on its one-qubit input.
This confirms that the defect is rule-specific rather than a reason to reject
the entire outcome representation.

The bug does **not** alter path probabilities, interaction witnesses, or the
extinction theorem: those calculations use the correct matrices in
`Token.packet`. It does invalidate the stronger claims that all generated
outcomes are already completely typed and that the immutable record itself
contains the correct evidence operator.

## Required repair and closure test

Choose and enforce one explicit record ontology:

1. Store the actual input-domain effects `K_g^dagger K_g`, `P_b`, and
   `J_b^dagger J_b`, together with an explicit domain type tied to
   `owner_ports`; or
2. rename the current field as a typed pointer/readout operator and add a
   separate input-effect field from which the branch probability can be
   reconstructed.

The receipt must then check, for every rule and outcome:

- operator dimensions match the owned input domain;
- the stored input effect equals `K_o^dagger K_o` exactly;
- the stored effect reconstructs the emitted conditional Born weight;
- summing stored effects gives the correct order unit on that domain; and
- pointer/readout projectors, if retained, are typed separately from input
  effects.

## Accepted narrowed result

Subject only to that repair, the following ceiling is ontologically honest:

```text
INCOMPLETE-PACKET
+ COMPLETE GLOBALLY RACED FINITE-PREFIX KERNEL
+ INCIDENCE-SCOPED EXACT INSTRUMENTS
+ SEPARATE DUAL SL(2,C) COVARIANCE TEMPLATE
+ ALGEBRAIC POSITIVE-CONE CONTAINMENT
+ OWNED SIBLING-INTERACTION WITNESS
+ ALMOST-SURE TERMINAL-SEAL EXTINCTION
- DECENTRALIZED LOCAL CLICK LAW
- GENERATED MULTI-FRAME GAUGE
- CANONICAL PROJECTIVE PUSHFORWARD
- GENERAL BRIDGE/JOIN BIRTH
- PHYSICAL SPACETIME INFLUENCE ENVELOPE
```

## Verdict

**MAJOR REVISION — ONE NEW BLOCKER.** The round-1 ontology and locality
downgrades are real rather than cosmetic, and no round-1 global/local,
gauge, bridge, spacetime, ISP, COMMIT, or construction-order claim needs to be
reopened. But a sealed record cannot be called fully typed while its stored
effect has the wrong normalization or acts on the wrong Hilbert-space domain.
Repair the durable outcome effect typing and add exact reconstruction gates;
then this narrowed `INCOMPLETE-PACKET` should be eligible for PASS.
