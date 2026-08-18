# WRC terminal verification — bounded repair replayed off tree

**Date:** 2026-08-18

**Verified commit:** `acd4b3896d71461c5c9e83028c37b0345c3c6d78`

**Terminal result:**

```text
WRC-WALK-REPRESENTABLE-MODULO-CELL-HIT-INSTRUMENT
```

## 1. Frozen bytes

| object | SHA-256 |
|---|---|
| generic core | `94c74731179c1302254a3b7424dcb66d1154518bcf936c5531b05a52f42fa6b3` |
| physical fixture | `4ced0a163d645072ded79c51c92cf6f847576f062f35091df67db6d6f8a971c8` |
| repaired scorer | `d5bab9601763c86556482ab0e83f32956b1b1bb2cd9a2cfeba0901de346a7ecd` |
| transcript | `dcc7be5eda5d47e619bc0c2c77dfccb07b2b088535af0a9d83938d6462ec7979` |
| receipt | `9cc0b4740c87b1541260e313e4caa1da0ccfa3afed56d74721b86016712a67af` |
| paper | `2be4c85b5b09eeb2cde6a055204520b5bb4fff921b562ff4b59260db3bd71f60` |
| repair note | `62fb4eaad7bf271740866b7a1b7282d929dd173cee6ecaf06c3597f925e084ab` |

The receipt payload digest is
`1a7f5ebc76dbe167dfdbb781e7d1793e308c2c559675cc3afedbbe7eb5266332`.

## 2. Clean and off-tree replay

The committed scorer was run from the repository and regenerated its three
artifacts twice with byte-identical results.  A `git archive HEAD` was then
expanded into a fresh directory containing no `.git` directory and no
untracked worktree files.  From an alien working directory, the archived
scorer regenerated transcript, receipt, and paper byte-identically to the
committed artifacts.

The generic core and physical fixture stayed byte-identical to the hostile
panel inputs.  The off-tree replay read only tracked committed ancestors.  The
untracked v15 SCOUT-T files were neither archived nor read.

## 3. Post-commit falsifier replay

The clean receipt reports 37 passing gates.  Every one of its 37 named
mutants was then invoked in a fresh process after commit.  All 37 exited with
`WRC REFUSAL`; zero survived.  The new load-bearing deaths were:

| mutant | refusing gate |
|---|---|
| `record-feedback` | `WRC-RECORD-FEEDBACK-DISCRIMINATOR` |
| `alternative-completion` | `WRC-ALTERNATIVE-COMPLETION-SINGLE-FIT` |
| `two-input-completion` | `WRC-TWO-PREPARATION-COMPLETION-DISCRIMINATOR` |
| `q8-scientific-leak` | `WRC-QUALIFIERS` |
| `primary-comparator` | `WRC-PRIMARY-COMPARATOR` |

All inherited provenance, transport, regression, beable, covariance,
instrument, recurrence, scope, rendering, exactness, and seal mutants also
refused at their named gates.

## 4. Terminal scope

The coordinate vector remains

```text
(true, true, true, true, false, true).
```

The terminal physical reading is restricted to one finite fixed carrier:

```text
FIXED-CARRIER WALK PACKET RECONSTRUCTED;
LITERAL CELL-HIT OPERATION IS NOT AN AFFINE QUANTUM INSTRUMENT;
STATE-RECORD FEEDBACK IS NON-INERT;
DYNAMIC RELATIONAL GEOMETRY AND GEOMETRY IRREDUCIBILITY ARE UNBUILT.
```

The full rank-one affine-completion theorem, alternative single-continuation
fit, and two-preparation impossibility witness are terminal at that scope.
The pure-ray branch remains a coherent law class with mixtures represented as
measures over rays, but steering/no-signalling is untested.  Actualization,
genuine division boundaries, record permanence, carrier growth, relation
rewrite, geometry, gravity, continuum/Lorentz structure, QFT/GR, species,
Hamiltonian selection, constants, and deviations remain open.
