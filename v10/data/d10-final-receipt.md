# D10 final receipt — many clocks, few factors in SCIR

**Finalized:** 2026-07-11 after three hostile review rounds.

## Verdict

```text
CONDITIONAL-COMPLEX-QUBIT/LORENTZ-CONE-ISOMORPHISM
+ FOUR-FACTOR-DIRECTIONAL-POSITIVE-EVALUATIONS
+ FINITE-OUTER-CONE-APPROXIMATIONS
+ FINITE-ALPHABET/FINITE-DEPTH-PROJECTOR-REFINEMENT
+ CHOSEN-PACKET-SEAL/SCHEDULE/FOREST-INTERVENTION-TESTS
+ SUPPLIED-SU2-CONNECTION-GAUGE-COVARIANCE
- COMPLEX/LOCAL-TOMOGRAPHY-SELECTION-NOT-DERIVED
- NORMALIZED-QUBIT-TIME/SCALE-MAP-NOT-DERIVED
- PHYSICAL-LINK/SEAL/CAPACITY-NOT-DERIVED
- FULL-SL2C-BORN-GAUGE-OPEN
- JOINING/ORDER/SPACETIME-INFLUENCE-LINK-OPEN
= KINEMATICS-ONLY
```

## Reproduction

```bash
python3 v10/code/d10_bloch_lorentz_exact.py
python3 -O v10/code/d10_bloch_lorentz_exact.py
python3 v10/code/d10_finite_clock_convergence.py
python3 -O v10/code/d10_finite_clock_convergence.py
python3 v10/code/d10_relational_scir_packet.py
python3 -O v10/code/d10_relational_scir_packet.py
python3 v10/code/d10_reproducibility_audit.py
python3 v10/code/v10_self_containment_audit.py
```

Final audit output:

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

Self-containment passes 4/4: every D10 executable resides in `v10/code`, no
duplicate investigation source exists outside it, D10 exact/core code uses
only the Python standard library, and no `pyc` artifact exists under `v10`.

## Exact results

### Ordered-space algebra — 109/109

- `Herm_2(C)_+` is the `1+3` future Lorentz cone;
- normalized rank-one rays are `CP^1=S^2`;
- directional positive functionals are `Tr(P_uX)=t+u.x`;
- R/C/H/O rank-two determinant forms give `1+2`, `1+3`, `1+5`, `1+9`;
- generic spin factors prove nonselection of three-space;
- supplied `SU(2)` link/path/loop covariance passes;
- an exact nonunitary `SL(2,C)` boost preserves determinant but changes trace.

### Finite geometry — 99/99 at 90 decimals

- finite clock-shadow cones are outer polyhedral approximations;
- Platonic support minima and radial excesses reproduce;
- span and origin-interiority hypotheses certify triple-normal completeness;
- infinite convergence is conditional on a dense nested union, with the
  compactness lemma stated in Paper 11;
- the external 120,000-direction Fibonacci probe is diagnostic only.

### Finite packet — 43/43

- exact `H/T` words generate 113 distinct projectors through depth 12;
- generation uses no external sphere oracle; the 50,000-direction Fibonacci
  sphere is explicitly a diagnostic;
- projective `SEAL` is complete, Born-normalized, and repeat-durable;
- actual disjoint complex-tensor schedules agree and an overlap control does
  not;
- a bounded-forest source intervention changes exactly nodes `{1,3,4}` and
  leaves the other branch/disconnected component unchanged;
- per-record evidence capacity, joining sectors, physical links, and
  spacetime influence remain open.

## Hostile review trajectory

Round 1: all three streams returned `MAJOR REVISION` while independently
reproducing the central theorem and numbers. Every opening is retained in the
review files and disposed in `note-d10-round1-opening-repairs.md`.

Round 2: all substantive repairs passed. Reviewers found only two textual
blockers: the `SL/PSL` covering sentence and a surviving finite-information
overstatement.

Round 3: all three streams returned PASS:

```text
2e832c3fdc61d89b211e7341f8659763cbafdd4f470edf36ce9fac5ccc4f890b  d10-round3-mathematics-hostile-review.md
c720a67420065b1aee348ad194a426b254de8ba4781a97ced2ac962ff95064f0  d10-round3-ontology-locality-hostile-review.md
a85b913afee6328e65349e6e327119a4664b8c4716f493afe1bc7919965e5e3d  d10-round3-independent-rebuild-hostile-review.md
```

Accepted scope: **PASS at the repaired finite conditional
`KINEMATICS-ONLY` scope.**

## Final artifact hashes

```text
26e61c146b328b5eae14994594f79bb70421a275a35de464b4245e482dc42a46  v10/note-d10-bloch-celestial-selection-protocol.md
9e8bb52ebc7d4732eb4d88b82e2cbca958ce649b1b006b4442e7c7218560afe6  v10/note-d10-bloch-celestial-investigation.md
055df5b4d0e5523df67e62737b056ac5525efc0d8aacd0bf2e9ee6f29578aeed  v10/note-d10-literature-audit-bloch-celestial.md
fe91dfeb1e95d04b813f59b59c47443df246b8e74ad579ef263796df511ff494  v10/note-d10-round1-opening-repairs.md
0b9040cc8e6d6608b169ed5ff11c290b32768ebbce1fb964c0fb694956a36c88  v10/code/d10_bloch_lorentz_exact.py
595ca56dce92052f0db0ecc3fe28252e2b467dd1eb28b55aead26aa0848650d3  v10/code/d10_finite_clock_convergence.py
435cea33e9d6f57dca114567828544bc04c0add597d8a87534f6301bda481b5f  v10/code/d10_relational_scir_packet.py
ed9cf8089f61dc777be4dc436f5df41a30cd4f764e0617a975a0d2e667439d90  v10/code/d10_reproducibility_audit.py
743b8d93c3baad99981db20e3133cdf36b4fe58486584161205609b4ec5381db  v10/code/v10_self_containment_audit.py
152b3f5dac8e6bf208374ae3ac8893fe07d06973947886ba092c2357c3cdb49a  v10/data/v10-self-containment-receipt.md
b8af6242554f321ad6c6a6b8d4596377b94dc3401acb300ab15c972ca871c6c6  v10/relativistic-isp-v10-paper11-many-clocks-few-factors-is-an-exact-kinematic-bridge.md
ed9340af3900c32110084d76e34719923fcafb8cdae8e9693bcd922366b70d1e  v10/data/d10-pre-review-receipt.md
b5ee4792718745285c830c39148882fd7eaebe47015469234798ddde51a031c0  v10/data/d10-round1-repair-receipt.md
a93d1f461087e908c9adc242900e5d5ed500a05a18a86c09b37f0c65cb8d316d  v10/data/d10-round2-textual-closure-receipt.md
9f494342cde8dd803282e0ffb4551699fe29aaa34a619a0752880b94eb517301  v10/reviews/d10-round1-mathematics-hostile-review.md
74eb63c65c609213db3d3a858b470b42999d6d70c7d083f2425445fc0fcc90dd  v10/reviews/d10-round1-ontology-locality-hostile-review.md
35dc1d09c06f94ab87a69863c7c29dbda0d9843f79d7de6f9e45998bdd26de8a  v10/reviews/d10-round1-independent-rebuild-hostile-review.md
bb3ead3cf267d2565178a569be4899512cf1c478f1a7237c1a4147194ceb6a6d  v10/reviews/d10-round2-mathematics-hostile-review.md
fd9e7e6f2ac48b92485c73d81824befea25d19335d3dc1c4ba0ba14e082cbf66  v10/reviews/d10-round2-ontology-locality-hostile-review.md
e73bbcc414279a6ac5c1d2a541e42910d148a2aa951d7786fe8ae4e3538a8684  v10/reviews/d10-round2-independent-rebuild-hostile-review.md
2e832c3fdc61d89b211e7341f8659763cbafdd4f470edf36ce9fac5ccc4f890b  v10/reviews/d10-round3-mathematics-hostile-review.md
c720a67420065b1aee348ad194a426b254de8ba4781a97ced2ac962ff95064f0  v10/reviews/d10-round3-ontology-locality-hostile-review.md
a85b913afee6328e65349e6e327119a4664b8c4716f493afe1bc7919965e5e3d  v10/reviews/d10-round3-independent-rebuild-hostile-review.md
4bf6b5c8d362c6dc82448e9441347f91355f82e477b448a6fbf394051588586d  v10/README.md
fd2b4ef38a76390ff23d3302c74f610e03be067d62cea57df4ca99bd815291c2  v10/PLAN.md
d2f5e811625a9afe6d49ba0d525af99b846943972de73c3d4f41c2259ed5f675  v10/LOG.md
```

## Next decisive investigation

Construct an unnormalized SCIR event/effect packet with dual `SL(2,C)`
transport, invariant Born ratios, typed link birth/ownership, and sealed
diamond data. Then compare a paired-history marked continuation-measure
influence front with the algebraic cone. In parallel, run the
real/complex/quaternionic/spin-factor selection tournament; if no owned record
principle distinguishes them, the complex operational factor must be declared
primitive rather than derived.
