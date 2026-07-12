# D11 hostile mathematics review — round 3 closure

**Date:** 2026-07-11  
**Verdict:** **MINOR REVISION**

The sole round-2 mathematical blocker is fixed in the constructors. SPLIT now
stores `K_g^dagger K_g=I_2/2`; sibling-MERGE stores the correct input-domain
`J_b^dagger J_b`, a `4 x 4` operator; terminal-SEAL continues to store `P_b`.
The repaired outcomes are dimensionally and mathematically correct.

Final PASS is withheld only because the stated frozen stdout hash does not
match the reviewed executable.

## 1. Effect repair

Source inspection confirms:

```text
SPLIT          effect = K_g^dagger K_g = I_2/2
TERMINAL_SEAL  effect = P_b
SIBLING_MERGE  effect = J_b^dagger J_b
```

The executable also verifies that these effects reconstruct the registered
Born weights for the SPLIT, MERGE, and SEAL witnesses. Thus the previous
dimension/type blocker is closed and no dynamics or extinction result changes.

The new general gate checks the SPLIT effect exactly, terminal effects by
membership in `{P0,P1}`, and MERGE effects by dimension; the following check
reconstructs the witness Born weights. For future hardening, it should directly
pair each durable string value `b` with its own stored effect (`P_b` or
`J_b^dagger J_b`) rather than merely checking membership/dimension. The current
constructors do make the correct pairing, so this is not a surviving
mathematical blocker.

## 2. Reproduction inconsistency

The current executable completes successfully with 73 checks and semantic
receipt

```text
c45eea0b4d50ec1644627a722bfa6f010f238ae581f66391eba7aeff4c32b62e
```

Normal and optimized Python are byte-identical. However, their complete stdout
SHA-256 is

```text
639154ac73e65adb1b528a2bc1d5f6fa1dc4ffc1bc8a1e94bb643742891021f4
```

not the frozen `b1d380...` value supplied for this review. I reproduced
`639154...` repeatedly after the internal receipt gate was corrected. No file
in the reviewed D11 tree records `b1d380...`.

This is a receipt/freeze inconsistency, not a theorem failure. It requires
either freezing the actual `639154...` output or restoring the exact artifact
whose output was `b1d380...` and reviewing that artifact.

## 3. Scope check

The narrowed adjudication remains intact:

- `canonical_projective_pushforward=OPEN`;
- `decentralized_local_click_law=OPEN`;
- dual `SL(2,C)` covariance remains a non-integrated template;
- the globally raced finite-prefix kernel and exact instrument calculations
  remain passed;
- the almost-sure extinction proof is unchanged;
- the primary verdict remains `INCOMPLETE-PACKET`.

No stronger projectivity, locality, gauge, bridge-birth, or spacetime claim was
introduced by the effect correction.

## 4. Verdict

**MINOR REVISION.** The round-2 mathematics blocker is substantively closed.
Update or reconcile the frozen complete-stdout hash; after that receipt-only
repair, this D11 mathematics package is eligible for PASS without another
substantive theorem review.
