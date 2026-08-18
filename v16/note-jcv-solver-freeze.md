# JCV generic solver freeze

Status: **INSTRUMENT-FROZEN-BEFORE-PHYSICAL-FIXTURE**.

Pin commit: `a51f9493e5be78f090aa7d387afa9a1eecfc6a4c`.  The physical JCV fixture, scorer, output, receipt,
and paper paths were absent throughout this freeze.  This artifact reports
public calibration behavior only and carries no JCV physical verdict.

## Public exact calibration table

| model | nonempty gauge sectors | Krull dimensions |
|---|---:|---|
| EMPTY | 0 | [] |
| POINT | 1 | [0] |
| POSITIVE_DIMENSIONAL | 1 | [1] |
| REDUCIBLE | 1 | [1] |
| GAUGE_SECTOR | 1 | [0] |

The backend uses rational multivariate polynomials, exact Buchberger reduction,
an independently checked S-pair remainder criterion, leading-monomial-ideal
dimension, exact sign-sector substitution, and saturation by an inverse
variable for nonzero-locus questions.

The frozen public battery has 15 gates and 11 named
falsifiers.  It reads 9 committed source anchors.
Every number in this note is rendered from the measurement object sealed in
`v16/code/jcv_public_receipt.json`.

## Non-claims

No physical comparison map, weight law, gauge quotient, solution dimension,
interference witness, backreaction, geometry, particle, constant, or QFT/GR
claim is made.  The next authorized event is the separate freeze of one
physical fixture and its verdict-neutral scorer, followed by one official run.
