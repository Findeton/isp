# D10 hostile review, round 3: independent textual closure

**Referee:** independent clean-room reconstruction  
**Date:** 2026-07-11  
**Verdict:** **PASS — the round-2 textual openings are closed and the frozen executable receipts remain unchanged**

This review is intentionally narrow. I verified the three corrections frozen
in `v10/data/d10-round2-textual-closure-receipt.md`, recomputed their artifact
hashes, and reran the normal/optimized reproducibility audit after the
relational executable's docstring edit. All submitted hashes match. The
executable stdout is unchanged and still passes its frozen hash gates.

## 1. Closure-receipt integrity

The textual closure receipt has SHA-256:

```text
a93d1f461087e908c9adc242900e5d5ed500a05a18a86c09b37f0c65cb8d316d
```

The three corrected artifacts reproduce the frozen hashes exactly:

```text
435cea33e9d6f57dca114567828544bc04c0add597d8a87534f6301bda481b5f  v10/code/d10_relational_scir_packet.py
9e8bb52ebc7d4732eb4d88b82e2cbca958ce649b1b006b4442e7c7218560afe6  v10/note-d10-bloch-celestial-investigation.md
b8af6242554f321ad6c6a6b8d4596377b94dc3401acb300ab15c972ca871c6c6  v10/relativistic-isp-v10-paper11-many-clocks-few-factors-is-an-exact-kinematic-bridge.md
```

The unchanged executable/audit hashes also remain:

```text
0b9040cc8e6d6608b169ed5ff11c290b32768ebbce1fb964c0fb694956a36c88  v10/code/d10_bloch_lorentz_exact.py
595ca56dce92052f0db0ecc3fe28252e2b467dd1eb28b55aead26aa0848650d3  v10/code/d10_finite_clock_convergence.py
ed9cf8089f61dc777be4dc436f5df41a30cd4f764e0617a975a0d2e667439d90  v10/code/d10_reproducibility_audit.py
```

## 2. `SL(2,C)` / `PSL(2,C)` correction

Paper 11 now states:

```text
SL(2,C) is the two-to-one cover of the proper orthochronous Lorentz
group with kernel {+I,-I}, while PSL(2,C) is isomorphic to SO+(1,3).
```

This is correct. The congruence action of `SL(2,C)` on Hermitian two-by-two
matrices has kernel `{+I,-I}` and induces

$$
PSL(2,\mathbb C)
=SL(2,\mathbb C)/\{\pm I\}
\cong SO^+(1,3).
$$

The reversed cover/quotient sentence reported in round 2 is gone.

**Disposition:** closed.

## 3. Capacity wording correction

The investigation note no longer claims that finite Hilbert dimension solves
finite record capacity. It now makes the exact supported distinction:

- one finite-dimensional state and a finite instrument alphabet can answer
  many correlated directional questions without storing infinitely many
  independent classical clock scalars;
- this does not bound exact state-description length, accumulated provenance,
  evidence/KL content, or total per-record storage.

The later packet discussion and final conditional statement repeat that those
capacity notions remain open. Paper 11's abstract, finite-generation section,
verdict, and exclusions use the same ceiling.

**Disposition:** closed.

## 4. External-sampler wording correction

The relational executable docstring now says that the `H/T/SEAL` generator
uses no external `S^2` generation oracle while an external Fibonacci sphere is
used for the coverage diagnostic. This agrees with its frozen summary:

```text
generation_external_sphere_sampler=ABSENT
coverage_diagnostic_external_fibonacci_sampler=50000
```

Paper 11 and the investigation note make the same generator/diagnostic
distinction. The former unqualified “no external sampler” wording is gone.

**Disposition:** closed.

## 5. Frozen stdout after the docstring-only edit

I reran `v10/code/d10_reproducibility_audit.py`. It executed each production
script normally and with `python -O`, compared each pair byte-for-byte, and
checked each result against its frozen expected stdout hash:

```text
D10 REPRODUCIBILITY AUDIT
scripts=3
normal_optimized=BYTE_IDENTICAL
frozen_stdout_hashes=PASS
d10_bloch_lorentz_exact.py bytes=4750 stdout_sha256=a05b84aa0a94a4a3086c190045fc56e96eb0fde6a00c179073a23944bbebcd5f
d10_finite_clock_convergence.py bytes=7470 stdout_sha256=f2e8c45e1a224e4f84ebfdd5a11e9973266879723443508d9f04539fdaa3be27
d10_relational_scir_packet.py bytes=3294 stdout_sha256=b5827de1d703ab492563fb1b981a41da477a1627943215ffe4ce660d0feb65eb
audit_sha256=f8c409191f05ee830a6422428517860e1961311b98c6f3b6be1dc5c505e6b596
```

The docstring edit changes the source-file hash, as the closure receipt
records, but does not change the program's stdout or any of the `109/99/43`
frozen conditions.

## 6. Final determination

All round-2 textual openings assigned to this stream are closed:

| Opening | Result |
|---|---|
| `SL`/`PSL` cover statement reversed | corrected |
| finite Hilbert dimension overclaimed as record capacity | narrowed to independent-register objection; capacity remains open |
| external sampler absence unqualified | generator and diagnostic scopes separated |
| docstring edit might disturb frozen receipts | normal/`-O` stdout hashes unchanged and gated |

No new inconsistency was introduced by these edits. The final D10 ceiling
remains `KINEMATICS-ONLY`: a conditional complex-qubit/Lorentz-cone
isomorphism plus finite chosen-packet tests, not a selected, scaled, or
influence-wired spacetime dynamics.

**Round-3 independent-rebuild verdict: PASS.**
