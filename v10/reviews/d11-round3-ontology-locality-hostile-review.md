# D11 hostile ontology/locality review — round 3 closure

**Date:** 2026-07-11  
**Verdict:** **PASS AT NARROWED `INCOMPLETE-PACKET` SCOPE**

## Reproduction

The repaired exact engine reproduces **73/73** checks and the frozen receipt:

```text
c45eea0b4d50ec1644627a722bfa6f010f238ae581f66391eba7aeff4c32b62e
```

Artifacts audited at these SHA-256 hashes:

```text
58601cdab90c1916c220cb5e93c1da239d182afaa81e2e439e8867844b5bfa90  d11_complete_bloch_lorentz_exact.py
efad9e513715c4defb0433a9805da127c02b8d8c0bfa4866b2cf5c67c7815bc7  note-d11-complete-bloch-lorentz-scir-investigation.md
044154486930da0ddc0c00aac2bc0fbcb817d370497a68a4db365c5b0675486f  relativistic-isp-v10-paper12-complete-lorentz-rulebook-that-cannot-grow-a-universe.md
```

## Sole blocker closure

The durable records now agree with the executable instrument semantics:

- SPLIT stores `K_g^dagger K_g = I_2/2` on its one-qubit input;
- sibling-MERGE stores `J_b^dagger J_b`, a `4 x 4` effect on its owned
  two-qubit input;
- terminal-SEAL stores `P_b` on its one-qubit input.

The rule-dependent gate checks the stored input-space dimensions and values,
and the additional exact gate reconstructs the SPLIT, sibling-MERGE, and
terminal-SEAL Born weights. Thus the immutable outcome no longer disagrees
with the evidence law that produced it. Runtime probabilities, provenance,
interaction witnesses, and the extinction theorem remain unchanged.

A nonblocking hardening opportunity remains: make the reconstruction gate
read every enumerated `DurableOutcome.effect` directly, rather than partly
repeating the constructor's Kraus expression. Source inspection and the
present exact gates are sufficient for closure, but direct record-by-record
round-tripping would make future metadata regressions harder.

## Scope audit

No claim expansion accompanied the repair. D11 still explicitly retains as
open:

- decentralized proper-time/local clicking beyond the global enabled-token
  race;
- integrated generated-history multi-frame gauge covariance;
- canonical construction-order/projective pushforward;
- joining of unrelated components or a general bridge-birth law;
- a physical spacetime metric or macroscopic influence envelope; and
- any derivation of the proposed continuing `COMMIT` ontology.

Sibling-MERGE remains sibling-only, algebraic positive-cone containment
remains distinct from intervention and physical spacetime, Barandes remains a
boundary comparison rather than an implemented ISP dynamics, and COMMIT
remains a candidate next packet. The primary verdict therefore remains
honestly limited to:

```text
INCOMPLETE-PACKET
+ COMPLETE GLOBALLY RACED FINITE-PREFIX KERNEL
+ INCIDENCE-SCOPED EXACT INSTRUMENTS
+ TYPED DURABLE INPUT-SPACE EFFECTS
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

**PASS AT NARROWED `INCOMPLETE-PACKET` SCOPE.** The sole round-2 ontology
blocker is repaired, the repaired executable reproduces exactly, and no new
ontology, locality, or physics-scope blocker appears. This PASS closes D11's
finite globally raced packet; it does not promote D11 to the final dynamic
interacting local click law.
