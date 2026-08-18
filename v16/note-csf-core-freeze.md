# CSF generic exact core freeze

Status: **GENERIC CORE FROZEN BEFORE PHYSICAL FIXTURE**.

Ledger event: v16 #61. Immutable pin commit: `c4579b9`.

The following generic public artifacts are frozen before any CSF recurring-
context physical fixture, scorer, official output, receipt, or Paper 6 path
exists:

| artifact | SHA-256 |
|---|---|
| `v16/code/csf_core.py` | `93a093d6ce72be4167d277719daf37aa7df7704510819f3b2e264546a14362b4` |
| `v16/code/csf_public_output.txt` | `4e9a88aa4842ad7511b984c25fb4ce2289d20e4ede1eca3fd29ec1ddbf936b82` |
| `v16/code/csf_public_receipt.json` | `8f452d2f5498291d453237cc633b005df0646108905b84b79661ce5909f3230a` |

The core is exact over `Q(i)` and contains no float literal. It implements:

- exact Gaussian-rational matrix algebra;
- `M=C^dagger C`, all-input completeness through `L_V(M)`, and the
  independently indexed unconditioned channel `Phi_M`;
- Hermitian-coordinate affine systems, exact ranks/nullspaces, stacked
  recurring-context intersections, and symmetry constraints;
- exact PSD checks by all principal minors at the explicitly small public
  matrices;
- calibrated port-resolved outputs and unconditioned channel signatures;
- the tangent-support extremality criterion, with optional affine symmetry;
- exact flag tensoring and direct unitary/nonnormal operator constraints;
- deterministic JSON/text rendering, gate-time payload seals, strict CLI,
  selftest, and public mutants.

The eleven constructor-stated public gates pass. They reconstruct the two JCV
factorizations with common `M=diag(16/25,9/25)`, common unconditioned channel,
and calibrated first-port probabilities `0` and `49/625`; reconstruct the
third `M=diag(25/169,144/169)` and channel movement; measure affine dimensions
`3,2,1` for scalar/two-phase/rich-spectrum two-history contexts; reduce the
three-context public intersection from dimension `1` to `0` under exchange
symmetry; separate extreme endpoint, nonextreme midpoint, and exchange-fixed
midpoint by tangent nullities `0,1,0`; separate partial-flag two-phase
completeness from rich-phase failure; and reject a non-PSD affine control.

These values are public calibrations, not the CSF physical result. In
particular, no physical recurrence dictionary, selected matrix, held-out
context, primary outcome, or Paper 6 claim has been constructed.

Two ordinary runs are byte-identical. A copied source run from alien CWD
`/private/tmp` reproduces both public artifacts byte-for-byte. `--selftest`
and all three public mutants exit `1` without artifact writes; an unknown
option exits `2`. Static parsing finds zero float literals.

At this freeze the following paths are absent:

```text
v16/code/csf_fixture.json
v16/code/csf_score.py
v16/note-csf-fixture-freeze.md
v16/code/csf_output.txt
v16/code/csf_receipt.json
v16/paper-06-completeness-spectrahedra-record-fibers.md
```

The next authorized stage is one data-only recurring-context fixture and a
verdict-neutral scorer, both frozen before first official execution. The
generic core may not change after this commit.
