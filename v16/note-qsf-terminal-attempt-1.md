# QSF terminal verification attempt 1 — refused at the paper-claim seal

**Date:** 2026-08-18

**Candidate commit:** `0adaf5994fad43f00f78794c2c459990bab8dffe`

## Result

Terminal promotion is refused. Post-commit clean generation passes `20/20`
scientific gates in `187.05` seconds and reproduces the committed output,
receipt, and paper byte-for-byte. Of the `28` registered mutants, `27` refuse
without writing any result artifact. The sole survivor is `paper-claim`.

The survivor is a seal implementation defect, not a scientific discrepancy.
The rendered sentence is split as

```text
does
**not** choose a fundamental law
```

while the mutant searched for the one-line string
`does **not** choose a fundamental law`. It therefore changed no byte, passed
the equality check, and wrote only to its isolated `/private/tmp` case
directory. The official candidate artifacts were never touched.

## Authorized repair

The only source change is to bind the contiguous rendered token
`**not** choose a fundamental law`. Core, fixture, equations, scientific gates,
measured values, renderer, primary, and all official artifacts are unchanged
at this freeze event. The repaired source must commit before any new candidate
generation. Terminal status remains withheld.
