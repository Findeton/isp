# JRH terminal verification

Date: 2026-08-17

Ledger target: v16 #16

Candidate commit: `e657b2069ec3e338e517d8763dd96158d6db8e96`

## Terminal disposition

The scoped terminal verdict is:

`BOUNDARY-INSTRUMENT-CONSISTENT-BUT-FUNDAMENTAL-DYNAMICS-UNSELECTED`.

This is not a claim that a quantum-gravity dynamics has been derived.  It is a
verified separation of three facts:

1. a finite fixed-boundary relational CP-instrument architecture exists and is
   internally consistent at the tested fixtures;
2. the delivered dynamic-geometry toy is exactly eliminable classical
   feed-forward and therefore does not demonstrate backreaction; and
3. a complex functional on joint matter–geometry histories is a coherently
   typed candidate architecture, but its weights, common-boundary refinement
   maps, all-input instrument completion, actualization rule, nonfactorizing
   backreaction, and selection principle have not been derived.

The paper's embedded status says that post-commit verification is pending
because the candidate artifacts were frozen before this note existed.  The
checks below discharge that pending condition without changing those bytes.

## Frozen bytes

- paper SHA-256:
  `98489edb6a83919199c11b14b92c423965d1a08ad7652a1c1915d5402f9e6003`;
- exact source SHA-256:
  `5b76a1f230c5bcea2cbebd6883b9d1db7debe0d99bea8e82602f421a7294aeb9`;
- transcript SHA-256:
  `1d54adebf950e3486669f2dedb770737e260048f74ebf1c41e8fe55e63af575d`;
- receipt SHA-256:
  `1da2e12dbb6f94a8b93c356e31cb8e00593dbcb083cdbba5d57fc7d49af572a9`.

## Verification performed

1. The exact program was run three times before commit.  All four hashes above
   were identical on every run.
2. After commit, a plain worktree run reproduced paper, transcript, and receipt
   byte-for-byte against `HEAD`.
3. A true off-tree copy was produced with `git archive` from the candidate
   commit.  It contained no `.git` directory, ran from an unrelated alien CWD,
   and reproduced the three generated artifacts byte-for-byte.
4. All `38/38` exact gates pass.  All `17/17` named mutants move their intended
   primitive datum and die at their predeclared gate.  The self-test exits zero;
   each explicit mutant exits three; invalid CLI forms exit two; none writes a
   candidate artifact.
5. An independent canonical-JSON seal verifier confirms all 19 receipt payload
   keys, the paper and transcript byte hashes, 13 frozen source anchors, 32
   classified consequence rows, and all 202 paper-numeral occurrences.  No
   paper numeral is unbound.
6. Independent AST inspection finds no floating-point literal in the exact
   source.  The arithmetic remains exact over rational Gaussian numbers.
7. `git diff --check` is clean.  The unrelated untracked v15 SCOUT-T paths were
   not read, edited, staged, cited, archived into the test copy, or committed.

## What is terminal and what is not

Terminal at this scope:

- existence of the tested fixed-boundary CP instrument;
- its preparation blindness, no-signalling at the fixed factorization, exact
  entanglement-breaking character, and idle-spectator extension;
- the feed-forward equivalence no-go for the original geometry toy;
- viability of a two-actor projective occurrence at the tested type;
- three actors as the first simple closed relational loop, not a demonstrated
  universal minimum interaction arity;
- the state-relative-decoherence versus all-input-instrument counterexample;
- infinite generator/logarithm ambiguity for the tested transfer;
- rival-law underdetermination and the resulting refusal to infer a forced
  QFT/GR deviation from mere microscopic disagreement.

Not terminal as physical constructions:

- a selected joint successor law on changing relational carriers;
- a nonfactorizing and calibrated matter–geometry backreaction;
- compatible stable record partitions and objective actualization;
- a coherent all-finite-arity extension;
- growing-factorization subsystem algebras and no-signalling;
- reconstruction of the committed ISP walk;
- a continuum/QFT/GR limit, Lorentz behavior, particles/species, scattering,
  the affine/cosmological constants, an absolute scale, or any dimensionless
  phenomenological deviation.

No successor unit is authorized by terminalization.  Any later unit must begin
with a new pin and may cite only the scoped results above.
