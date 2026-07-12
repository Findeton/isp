# D17 hostile round-4 opening ledger

**Round-4 verdict:** finite nonselection passes; integrated `Ext(C)` still had
two exact keying bypasses.  
**Repair status:** submitted to focused round 5, 2026-07-11.

| Opening | Exact repair |
|---|---|
| Parent and child were canonicalized separately, forgetting the extension embedding | Declaration now uses one joint canonical marked-edge key; an abstractly isomorphic chain child with undeclared new-minimum embedding rejects |
| D16 past/future `BoundaryPort` metadata was omitted | Typed presentation keys include relabeled past and future `(element,kind,owner)` tuples; a foreign boundary port rejects |
| “Construction-order gauge” exceeded the proof | Claim narrowed to compatible element-label covariance within one supplied filtration; alternate filtrations remain an open quotient/sewing problem |

This repair does not change the finite action/kernel nonselection result or
promote the supplied filtration into a physical growth law.
