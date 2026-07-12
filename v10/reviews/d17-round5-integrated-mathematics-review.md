# D17 final focused round-5 integrated mathematics review

**Date:** 2026-07-12  
**Verdict:** **PASS AT THE INTEGRATED FINITE CONDITIONAL SCOPE**

## Decision

The final embedding and boundary-key repairs are correct. Declared extension
edges now use one joint canonical marked-edge key, so parent and child cannot
be independently canonicalized in a way that forgets which child element is
new. Typed past/future boundary metadata is included in the presentation key.

A consistently relabeled declared embedding admits. An abstractly isomorphic
chain with an undeclared new-minimum embedding rejects, and forged boundary
metadata cannot reuse the edge. All earlier owner, collar, memory, D14 carrier,
isometry, CPTP, projectivity, action and orbit checks remain intact.

## Reproduction

```text
source    5fffa4d676da38a64e61cdd3b01c031d6fa74d2e1119f72c35369ad7be40be57
packet    a9c08c3b5702dce8726f2b2b355b98398f227085ced61eedda98207d3018fa00
receipt   2b43af4909a7e8400c7c582cccd9cf780ea945e3d1d4bf7e9b7c5e64d85fecc6
ledger    cb2030af4f2c91ab30443801c5b16ded66eb4ccf6e985fdaecb387e88f10f841
stdout    b8593b3aa3f012243455904f407a2822b3e866b4ddf9a8554b6a0dc752df8398
checks    40/40 normal and optimized
```

Normal and optimized stdout are byte-identical.

## Joint canonical marked-edge key

The canonicalizer relabels the parent and child jointly while preserving the
old-element embedding into the child. Its serialized presentations include:

```text
relations;
past and future `(element,kind,owner)` boundary tuples;
element-owner tuples;
the marked old/new embedding.
```

Minimizing these joint presentations removes label gauge without quotienting
different extension embeddings. This is exactly the distinction missing from
the prior separately canonicalized keys.

The positive relabeling test and negative new-minimum-chain test exercise both
directions. The foreign boundary-port control additionally shows that an
order with the same raw relation cannot collide after its typed boundary data
changes.

## Regression audit

The final source retains all earlier exact identities:

```text
every cylinder edge is an induced one-element causal extension;
undeclared, nonowner and unentitled joins reject;
the fixed action is evaluated on every node;
three positive kernels are projective and inequivalent;
causal-node collars equal successive D14 network carriers;
V^dagger V = I for the full record network;
sum K_i^dagger K_i = I for reset;
record probabilities match equal, envelope and orbit kernels;
reset changes 000/101 to 000/100;
labeled orbit counting gives 2/3,1/3.
```

The nonselection theorem is unchanged: the same action and supplied grammar
admit inequivalent kernels. The repairs constrain representation and admission;
they do not make the action choose the grammar, kernel, commit or memory.

## Final verdict

**PASS AT THE INTEGRATED FINITE CONDITIONAL SCOPE.** All 40 checks and frozen
hashes reproduce with no regression. The broader ceiling remains supplied
extension grammar, kernels and record instrument; no continuum, geometry,
unit or fundamental-selection claim follows.
