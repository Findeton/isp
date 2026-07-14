# Paper 24 round 2 — note cemetery-consistency delta

**Base:** commit `63ea1863bde134923bb04a5644ae4f10024e9012`
**Reviewed object:** the single current working-tree hunk in
`note-d35-timeless-local-next-click-law.md`, section 4
**Lane:** positive conditioning mass, absent-successor convention and
Paper-24/D35-note consistency
**Verdict:** **PASS — THE NOTE NOW MATCHES THE ACCEPTED PAPER 24 GENERIC
REACH CONDITIONAL EXACTLY, WITH NO CHANGE TO THE D35 EXECUTABLE SCOPE OR
PROBABILITIES.**

**Count:** **0 blockers / 0 majors / 0 minors / 0 nits.**

## 1. Frozen hunk and hygiene

The reviewed note blob has SHA-256

```text
ab8506281161c6add0c7d2e2aae3034bb1f0ce958f2fcbfad145daf7fdccebfe.
```

The complete note delta is one hunk:

```text
1 file changed, 7 insertions, 4 deletions
```

`git diff --check -- v10/note-d35-timeless-local-next-click-law.md` is clean.
No note section outside the generic CAP cylinder formula changes.

## 2. Mathematical consistency — pass

The prior note divided by the mass of the completion cylinder without stating
that it was positive and evaluated `A2(H)` even on a completion where A had no
strict successor.  The hunk now supplies both missing domain clauses:

```text
[H0]          cylinder of completions of the present finite history;
mu([H0]) > 0  positive conditioning mass;
A2 = bottom   cemetery value when A has no strict successor;
reach          false on the cemetery value.
```

The resulting note formula is

```text
P(e reaches A2 | H0)
 = mu({H in [H0]: A2 != bottom and
                   e in NewPast_A(A1,A2(H)) by a licensed path})
   / mu([H0]).
```

This is the same event and convention as Paper 24 section 3.4:

```text
P(e reaches A2 | H0)
 = mu({H in [H0]: A2 != bottom and
                   e enters A2 through a licensed path})
   / mu([H0]).
```

The two phrasings are equivalent because the note's CAP immediately defines
acquisition as membership in `NewPast_A(A1,A2)` connected to A2 by a finite
licensed transfer chain.  Neither version conditions away the no-successor
histories; those histories remain in the denominator and contribute false to
the reach event.

## 3. Scope preservation — pass

The hunk changes only a generic completed-history conditional.  It does not:

- add a duration, rate, proper-time variable or global opportunity order;
- alter CAP's distinction between structural ancestry and operational
  intervention;
- change the rooted local menu, Q1/Q2 parameters or branch weights;
- change the `1/16` and `3/40` D-reach probabilities;
- change the 16/408 projectivity result or Ionescu--Tulcea completion; or
- claim that the rooted family supplies a root-free overlap law.

For the executable D35 family, every selected root call terminates and seals
A2, so the cemetery event has probability zero.  Adding the cemetery value
therefore makes the wider formula total without changing any registered D35
probability or receipt.  No executable rerun is required for this
definition-only consistency hunk.

## 4. Final tally

```text
B  blockers  0
M  majors    0
m  minors    0
n  nits      0
```

**Final recommendation:** accept the one-hunk note cleanup.  The terminal D35
note and revised Paper 24 now use the same positive-cylinder and absent-A2
convention, and no scientific scope has moved.
