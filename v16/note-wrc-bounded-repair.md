# WRC bounded repair — panel corrections implemented without moving the walk

**Date:** 2026-08-18

**Authority:** `v16/note-wrc-adjudication.md`, ordered repair 1–9.

**Status:** repaired candidate; terminal promotion awaits the post-commit
off-tree/no-git replay.

## 1. Frozen scientific inputs did not move

The repair leaves the generic core and physical fixture byte-identical:

| object | SHA-256 |
|---|---|
| `v16/code/wrc_core.py` | `94c74731179c1302254a3b7424dcb66d1154518bcf936c5531b05a52f42fa6b3` |
| `v16/code/wrc_fixture.json` | `4ced0a163d645072ded79c51c92cf6f847576f062f35091df67db6d6f8a971c8` |

The exact branch ladder, nine observable families, coordinate vector, and
primary are unchanged:

```text
(referent, transport, cuts, observables, instrument, beable-readout)
= (true, true, true, true, false, true)

WRC-WALK-REPRESENTABLE-MODULO-CELL-HIT-INSTRUMENT
```

## 2. Repaired artifacts

| object | SHA-256 |
|---|---|
| `v16/code/wrc_score.py` | `d5bab9601763c86556482ab0e83f32956b1b1bb2cd9a2cfeba0901de346a7ecd` |
| `v16/code/wrc_output.txt` | `dcc7be5eda5d47e619bc0c2c77dfccb07b2b088535af0a9d83938d6462ec7979` |
| `v16/code/wrc_receipt.json` | `9cc0b4740c87b1541260e313e4caa1da0ccfa3afed56d74721b86016712a67af` |
| `v16/paper-08-walk-reconstruction.md` | `2be4c85b5b09eeb2cde6a055204520b5bb4fff921b562ff4b59260db3bd71f60` |

The receipt is schema `wrc-result-v2`, has payload digest
`1a7f5ebc76dbe167dfdbb781e7d1793e308c2c559675cc3afedbbe7eb5266332`,
and seals 37 passing gates.

## 3. Scientific repair

The rank-one CELL-HIT effect is now used to construct and gate the complete
affine-CP classification:

```text
J_c(rho) = Tr(E_c rho) sigma_c.
```

The generated alternative instrument is complete and matches the single
registered conditioned continuation exactly.  A two-preparation witness then
shows that the displayed projective completion fits the effect eigenstate but
not the coherent preparation, while the generated alternative fits the
coherent preparation but not the effect eigenstate.  Both probabilities are
nonzero and the literal rule demands distinct output rays.  Therefore no one
fixed-output affine completion reproduces the literal noncollapse successor
on both preparations or on all inputs.

The displayed projective comparison is consequently named as one comparison,
not *the* repair.  Its conditioned-state inequality and six-cell later-screen
movement are gated directly.

The pure-state branch is typed as stochastic dynamics on projective pure rays
times count records.  Mixtures are probability measures over rays, not merely
density matrices.  Steering and no-signalling remain open.

The emission-history/count readout and zero-violation predicate are gated
directly.  Recurrence is retyped as four repeated numeric local record
signatures under one imported rule; the declared coin fiber is measured and
unselected.  Editorial Q8 status is absent from the primary, coordinates,
scientific qualifiers, and measured claims.

The fixed-carrier coupled/frozen discriminator is now a direct scorer result:
at tick three the site screen moves by total variation `1024/19683`.  This
earns non-inert **record feedback**, not geometry rewrite.

## 4. Process repair

The primary comparator is a separate semantic decision tree; it neither calls
the builder nor indexes its word table.  Direct gates now bind:

- zero history-to-count violations;
- coupled/frozen record-feedback movement;
- displayed-projective conditioned-ray and later-screen movement;
- the rank-one affine-completion normal form;
- the alternative single-continuation fit;
- the two-preparation all-input discriminator; and
- exclusion of editorial Q8 status from scientific qualifiers.

All 37 registered mutants refuse without artifacts.  The new mutants kill the
record-feedback control, the alternative single-fit, the two-preparation
discriminator, and a Q8 scientific-evidence leak.  The clean run was repeated
twice with byte-identical paper, transcript, and receipt.

## 5. Binding physical reading

```text
FIXED-CARRIER WALK PACKET RECONSTRUCTED;
LITERAL CELL-HIT OPERATION IS NOT AN AFFINE QUANTUM INSTRUMENT;
STATE-RECORD FEEDBACK IS NON-INERT;
DYNAMIC RELATIONAL GEOMETRY AND GEOMETRY IRREDUCIBILITY ARE UNBUILT.
```

The successor must apply the frozen relational-sufficiency method, including
JS predictive sufficiency/minimality, matched graph interventions, a
graph-generated later probe, erasure/reconstruction, resource-parity
adversaries, and held-out family scaling.  This repair does not pre-answer
that experiment.
