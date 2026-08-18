# JCV candidate post-commit verification

Status: **GREEN-UNREVIEWED**.

Verified candidate commit:
`ab2102a0f452b5760674946cecf5e9b581986bde`.

## Frozen artifacts

- fixture: `ad887c213d14781838c6e70227b8f2c162f1392a08060de7c6e57829a8db012b`;
- scorer: `66b87bdf68f7210d959e13bfacae4c5957413e6d8f234647bfe3ad4a19619a03`;
- paper: `b54858c394fe22626ef1e233781737b7199cc56bf816f52e8aae063a99deaefc`;
- transcript: `b1d950c804c8b568514f1a0206853496b2f578650a3d98187e64c1c8a9b70d6d`;
- receipt: `a1b0baeee418d3f2c82e1ec6d07993cb51f69f3f51d63a9996dae9fb177fe3d1`.

## Verification

- `--replay` from the committed worktree returned zero and reported
  `byte-identical`; all three generated artifacts remained unchanged.
- The self-test returned zero by killing its anchor mutant.  Every one of the
  fifteen named mutants returned the registered death code at its registered
  gate.  Help and unknown-mutant modes returned the usage code.  A second
  official run was refused because all result artifacts already existed.
- All test modes left artifact hashes unchanged.
- A `git archive` of exactly the committed runtime/read set was extracted to
  `/private/tmp/jcv-physical-offtree.2Xi0T3`, which contained no `.git` path.
  `--replay` from alien CWD `/private/tmp` returned zero and reproduced the
  paper, transcript, and receipt byte-for-byte.
- An independent canonical-JSON verifier matched every sealed key and the
  paper, output, scorer, and receipt cross-hashes.
- A separate direct enumeration of the four holonomy bits reproduced every
  shared-law, active, dark, control, and control-only key, every reported
  dimension, and both rational calibrated-probability witnesses.

## Candidate result at verified scope

All twenty gates pass and all fifteen mutants die.  The frozen primary is
`JCV-STRATIFIED`.  On the full-rank internally interfering locus the word is
`JCV-PAIRING-SELECTED-WEIGHTS-FREE`: one coherent holonomy class survives, but
the active weight variety has dimension two and moves a calibrated
probability.  Six additional rank-deficient/dark holonomy sectors survive
because one complete history channel is silent.  The independent-triangle
control has two further mixed-handoff sectors, measuring the finite price of
declaring one shared law across the overlap.

This verifies the exact finite candidate only.  It does not turn the declared
real-isometric comparison doctrine into a derived record law; select the
weights; derive actualization; or construct geometry, backreaction, EPR on a
growing factorization, all-arity interactions, particles, constants, a
Hamiltonian, continuum physics, or QFT/GR deviations.

The next required event is a hostile protocol frozen against the artifact
hashes above, followed by three mutually independent reviews.
