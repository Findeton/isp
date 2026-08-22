# Paper 22 v3 construction note

Date: 2026-08-22

Disposition: **CONSTRUCTION COMPLETE — SUBMITTED FOR THREE-SEAT DELTA REVIEW**

This note binds the construction to its frozen pin and records coverage,
provenance, and discipline. It is not an adjudication.

## 1. Frozen inputs

| object | ordinary SHA-256 |
|---|---|
| v3 pin (frozen before construction) | `703784ecaa02f78262b188a7cfdede5c9f9d52d3be13d203bc88f972ce2ad69a` |
| v3 candidate (this construction) | `4064f66b8bcf8750a7a7a908e76ccbca840e3c3c30c42a14352e478077fd7963` |
| Paper 13D law | `3b91766fe269e8145766f4622f99e9009c3270530670119735e6045a473de5c9` |
| Paper 21 interferometer | `ca0f709b00906971c6aac2b25b12fea11f168411ab2f440ccc49d982aab4ba80` |
| v1 pin | `de32c02ee1be613eef4a867dadf9bc1c84fc8ed492b764f7545bb54fb91a5ae4` |
| v1 candidate | `6d75a072fb3c51c5c267448fd329895f94cd4f9ee4ba4d96ea9660be80c1c6b7` |
| v1 adjudication | `c261520aa142bf07a489f87cd0364628f094794c7523c03d8ba3dde05d824a07` |
| v2 pin | `a4c1c2ecd10edad73ed64b12f699c09d7cfd169d4cd264939990589554693627` |
| v2 candidate | `30340295ccd5f8371a9020cb76c0a93cc24ab14cbbf78f05c01a85ca5ce86468` |
| v2 adjudication | `31c0d7ca973ad62c188e946b2d10433705c9c6644ab1bd0ea8579a963e706c04` |

The v2 adjudication is the authorization source; the v3 pin is the committed
freeze it demanded. The pin was frozen, hashed, and recorded in the working
tree before the candidate file existed.

## 2. The two repairs, and nothing else

**Repair 1 — apparatus restoration (candidate Section 5).** The seed space
`Xi_X=[25]^{P_X}`, uniform product law `mu_X=25^{-|P_X|}`, purified state
`|Omega_X> = 5^{-|P_X|} sum |xi>`, Householder preparation
`S_X = I - 2|v_X><v_X|`, fine-seed witness computations
`C_{T,X}`, `C_{F,X}`, controlled query `U_{Q,X}`, kickback identity (13),
and exact closure (11) are the v1 candidate Sections 5.1–5.3 at printed
content, placed on the v2 homogeneous domain. New relative to both
predecessors: only Theorem 4 (seed-preparation naturality on the bound
apparatus), which the restoration's covariance claim requires.

**Repair 2 — partial visibility (candidate Section 7).** Theorem 7 states
and proves law (V) with `q_phi = Re(gamma e^{i phi})` via the explicit
residual-environment Born calculation with first-lift route amplitudes
`(3/5,4/5)` and `(-4/5,3/5)`. Corollaries 7.1–7.4 discharge all four
pin-registered consequences: the `gamma=i`, `phi=pi/2` control (`I_2`),
the endpoint laws, the visibility audit `(288/337)|gamma|` / `|gamma|`
(diagonal row / off-diagonal row), and the `gamma=1` scope of `K_phi`.

Everything else is inherited: Sections 2–4 are the v2 Sections 2–4;
Sections 8–14 are the v2 Sections 7–14 renumbered. No third change exists.
In particular there is no coarse binning, no seed bias, no carrier change,
no reader-statistic change, no phase reconvention, and no fitted parameter.

## 3. Coverage against the pin

Pin Section 7 required fourteen theorem slots:

1. Domain decidability/refusal — Prop 1 + source controls (v2 verbatim).
2. Total typed child pair — Thm 1 (v2 verbatim).
3. Reversible-erasure obstruction and no-hiding — Thms 2–3 (v2 verbatim).
4. Seed preparation naturality — **Thm 4 (new, restored content)**.
5. Exact query closure — **Thm 5 (restored, fine seeds)**.
6. Phase-kickback identity — Eq. (13) in Section 5.4 (restored).
7. Minimal calibrated lift — Thm 6 first part (anchor, gauge statement).
8. Coherent probe law `C_phi` — Eq. (15) (anchor).
9. **General partial-visibility law — Thm 7 + Cors 7.1–7.4 (repaired)**.
10. Commit isometry/joint law/recovery/no dormant child — Thms 8–10.
11. Complete-instrument naturality including seeds — Thm 11 (item 2 names
    seed space/law/purification; item 6 names the overlap functional).
12. Restriction laws — Thms 12–13.
13. External tensor composition — Thm 14.
14. Plurality and noninheritance — Thms 15–16.

All present. Pin Section 8 hostile controls: the matrix in candidate
Section 13 contains all inherited controls plus five new rows naming the
exact v2 failure modes (biased carrier, coarse bond bit, `[25]`
repartition, `Re(v)` sentences, seed traced at recombination) and their
dispositions.

## 4. Independent arithmetic verification

Exact rational arithmetic for every printed number was checked
independently of the drafting process (floating-point harness over 10^5
admissible `(gamma, phi)` pairs, exact at the sampled points):

- law (V) equals the direct residual-environment Born rule for both input
  columns at every admissible `gamma`;
- columns sum to one and all entries lie in `[0,1]` for every admissible
  `gamma`;
- `gamma=1` reproduces `C_phi`; `gamma=0` reproduces `B^2`;
  `C_{pi/2,i}=I_2`;
- visibilities `(288/337)|gamma|` (diagonal row) and `|gamma|`
  (off-diagonal row);
- `K_phi` entrywise positivity endpoints `-7/32`, `7/18` reproduce exactly
  (`(63+288c)^2-(112-288c)^2 = 175(576c-49)`).

Two drafting errors were caught by this harness and corrected **before**
this note froze: a wrong control value in an early pin draft
(`diag(1,0)` instead of `I_2`) and a wrong compact form
(`|R diag(1,gamma e^{iphi})R|^2`, valid only at `|gamma|=1`, replaced by
the correct interference-scaling derivation). The frozen pin contains the
correct values.

## 5. Discipline statements

- No code, evaluator, fixture, or generated number is part of the object;
  the verification harness above was audit scaffolding only and is not
  evidence of any constructed coordinate.
- No downstream artifacts were consulted during construction; Paper 23's
  preparation pin was read only as a bound consumer.
- Construction-stage writes were scoped to
  `v16/paper-22-reversible-structural-instrument-v3.md` and this note.
- Line counts at freeze: pin 379 LF; candidate 1024 LF.
  Forward-only chronology correction (post-adjudication): the ordered
  bounded prose repair (#306) moved the candidate to 1030 LF / new
  ordinary SHA-256 `be0822c81d58eee487925191b3156e22172bcc372012fd6cfc4f23b2ca890349`.
  Four replacement sentences only; no number, definition, control, or
  scope wall moved. The pre-repair bytes remain recoverable from hash
  `4064f66b8bcf8750a7a7a908e76ccbca840e3c3c30c42a14352e478077fd7963`.

## 6. Review request

Three-seat blind delta review per pin Section 12, repo read-only, each seat
rebuilding from published prose. Mandatory regressions: the two repairs and
the `gamma=i` control. Verdicts ACCEPT / ACCEPT-WITH-FIXES / REJECT,
findings most-severe-first, replacement sentences verbatim.
