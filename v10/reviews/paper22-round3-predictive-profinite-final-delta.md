# Paper 22 round 3 — predictive/profinite final delta

**Frozen target:** commit `a074608ebbc012ac6bd564d51757c6e009688124`

**Compared against:** commit `8e820cc2464eeefeabafe49ed64246e98d51ce4a`
and `paper22-round2-predictive-profinite-closing-delta.md`.

**Verdict:** **PAPER DELTA SCIENTIFICALLY CLEAN; ONE REPOSITORY-WHITESPACE NIT
— 0 blockers / 0 majors / 0 minors / 1 nit.**

The exact Paper 22 repair closes the sole round-2 minor.  Both bibliography
entries are now correct, the claim-local citations remain explicitly
background rather than SHARD theorem attribution, and the new validator
ceiling sentence accurately narrows only the validator—not the typed-union
theorem on genuine regional projections.  No unrelated Paper 22 content
changed.

The only nonzero count is mechanical: whole-commit `git diff --check` reports
two trailing-whitespace lines in the newly added round-2 predictive review.
Paper 22 itself passes `git diff --check`.

## 1. Exact paper identity

Both the working-tree file and the blob read directly from commit `a074608`
have SHA-256

```text
e33c0ad9294ff1411f49e7d32dc640c9047d3a7603e954219703f23031bf8576.
```

The Paper 22 diff is exactly `11 insertions / 6 deletions`.  Independent
inspection finds only three intended change groups:

1. the status advances from round-1 repair pending to narrow bibliography
   delta pending;
2. the validator/composition paragraph records the completed scientific delta
   and states the validator ceiling precisely;
3. references [3] and [4] receive the corrected metadata.

No theorem, equation, probability, receipt count, artifact hash, outcome row,
profinite ceiling, quantum refusal or open problem changed.

## 2. Bibliography repair — pass

Reference [3] now gives Shalizi and Crutchfield as:

```text
Journal of Statistical Physics 104, 817–879 (2001)
DOI 10.1023/A:1010388907793.
```

Reference [4] now gives Geiger and Temmel as:

```text
Journal of Applied Probability 51(4), 1114–1132 (2014)
DOI 10.1239/jap/1421763331.
```

These are the exact repairs required by round 2.

The three inline uses remain claim-local background:

- [3] contextualizes the computational-mechanics predictive-state
  distinction and immediately says the record-native carrier theorem is the
  D34e-specific question;
- [4] contextualizes strong Markov lumpability versus weaker law-relative
  aggregation;
- [5] names the process-tensor operational quantum criterion reserved for the
  still-missing controlled lift.

The reference annotations continue to deny attribution of SHARD locality or a
timed D34b-D34c construction to those sources.  No citation has been promoted
into evidence for an unproved SHARD claim.

## 3. Validator ceiling versus typed-union theorem — pass

The new sentence says:

```text
The validator certifies these declared invariants on the composition
interface; it is not a complete recognizer for whether an arbitrary fabricated
history is reachable under D34b.  The composition theorem is the typed-union
identity on genuine regional projections.
```

This is the correct logical separation.  The executable's nine malformed-
message attacks establish the listed interface and owned-history checks; they
do not prove that the validator decides reachability of every fabricated
history.  The composition theorem never required that stronger recognizer.
For genuine regional projections, typed set union still reconstructs the
direct projection, and the receipt's `159,734` registered compositions remain
unchanged.  The clarification therefore neither weakens the theorem nor
overstates the validator.

## 4. Diff checks

The relevant commands and results are:

```text
git rev-parse HEAD
    a074608ebbc012ac6bd564d51757c6e009688124

git show a074608:<paper> | shasum -a 256
    e33c0ad9294ff1411f49e7d32dc640c9047d3a7603e954219703f23031bf8576

git diff --numstat 8e820cc..a074608 -- <paper>
    11  6  <paper>

git diff --check 8e820cc..a074608 -- <paper>
    clean
```

Whole-commit `git diff --check 8e820cc..a074608` is not clean.  It reports:

```text
v10/reviews/paper22-round2-predictive-profinite-closing-delta.md:3:
    trailing whitespace
v10/reviews/paper22-round2-predictive-profinite-closing-delta.md:5:
    trailing whitespace
```

Those are Markdown hard-break spaces in review metadata, not Paper 22 content.
They do not alter any scientific result, but the requested repository-wide
check cannot be recorded as clean at this exact commit.

## 5. Final recommendation

Remove the two trailing-space sequences from the round-2 predictive review and
run `git diff --check` once more.  No Paper 22, note, code or output change is
required.  After that mechanical repair, this stream recommends terminal
acceptance at `0B / 0M / 0m / 0n`.

At exact commit `a074608`, the count is:

**0B / 0M / 0m / 1n.**
