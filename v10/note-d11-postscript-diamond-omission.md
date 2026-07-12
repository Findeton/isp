# D11 postscript — the omitted diamond structure

**Status:** correction frozen before D12 construction, 2026-07-11.

D11's exact extinction theorem is valid for the executable packet. Its
pre-review interpretation was incomplete because the packet omitted older
SHARD structures that directly govern continuation.

## Corrections

1. **Primitive type.** V6's primitive record is a sealed finite diamond with
   lower/upper screens, eventless collar, internal transports, a retained and
   eventless-repair comparison, and a whole-history law. D11 reduced this to a
   live qubit port plus a root-frame coordinate.
2. **Seal semantics.** D8 Rule 4 is `seal and birth`: the committed outcome is
   durable and the normalized state is retained on the rule's output collar.
   D11 instead introduced a generic `TERMINAL_SEAL: 1 -> 0` rewrite.
3. **Clock semantics.** V6/V7's exponential is survival in accumulated local
   RN/KL evidence. D11 used equal activity in a global enabled-token race.
   These are not the same law.
4. **History semantics.** V6's complete closed-holonomy object is a compatible
   family of whole-diamond history laws. D11 was Markov on an augmented current
   history data structure.
5. **Interaction semantics.** D8 licenses a multileg interaction when a prior
   committed connected collar already owns all legs. D11 allowed only direct
   sibling recombination.
6. **Construction gauge.** D8's target quotients auxiliary linearizations of
   concurrent local firings. D11 checked one selected schedule cell under a
   globally normalized sequential presentation.

## Correct interpretation

D11 proves:

> If terminal observation is promoted to an ordinary physical death token and
> raced globally at equal activity against SPLIT and sibling-MERGE, the open
> population becomes extinct almost surely.

It does not refute sealed-diamond SHARD, V7's local evidence click law, or
D8's seal-and-birth SCIR architecture. It is retained as a negative-control
ablation.

## Consequence

`SEAL -> COMMIT` is not invented from nothing. Continuing output was already
part of D8's rule type. What remains open is the actual between-diamond output
collar law: its support, number and types of ports, ownership, coupling, and
whole-history probabilities.

