# JCV first official run — infrastructure failure

Status: **HISTORICAL FAILURE RECORD — CHRONOLOGY CORRECTED AFTER HOSTILE REVIEW**.

Frozen fixture/scorer commit:
`ee8e414c2e354b5447af57efedbe234ae12af111`.

Command:

`/opt/homebrew/bin/python3.13 v16/code/jcv_score.py`

Exit code: `1`.

No physical output, receipt, or paper path exists.  The fixture and scorer are
byte-unchanged from their freeze.

## Failure

The clean core reached the predeclared mutation survey.  Its
`FIXTURE_DROP_CUT` falsifier moved a dictionary whose values are Python sets.
The move-proof digest called the scorer's canonical serializer, which handles
fractions, quadratic-field numbers, tuples, lists, and dictionaries but not
sets.  `json.dumps` therefore raised:

`TypeError: Object of type set is not JSON serializable`

The traceback terminates at `jcv_score.py` in `Mutator.move -> digest ->
canonical -> json.dumps`, called from `fixture_semantics` during
`mutation_survey`.  No classifier word or physical numeral was printed,
written, serialized, promoted, or committed.

## Post-panel chronology correction

The original status phrase `FAILED-BEFORE-VERDICT` was too broad if `verdict`
includes an internal value.  Source-order reconstruction by all three hostile
seats shows that `run_core()` had solved and classified the clean fixture and
the renderer had formed a paper string in memory before `mutation_survey()`
encountered the set serializer.  The exception exposed none of those values.

The exact chronology is therefore:

`FAILED AFTER INTERNAL CLASSIFICATION, BEFORE RESULT EXPOSURE, SERIALIZATION,
OR PROMOTION`.

This correction changes no physical rule and does not imply result leakage.
The evidence for chronology is the committed source order, traceback, git
history, and absent result paths—not the original scorer's hard-coded
`P-CHRONOLOGY=True` row.

## Disposition

This is an instrument defect, not `JCV-EMPTY` and not any other registered
physical outcome.  The failed run is committed before repair.  The only
authorized repair is to make canonical serialization total on the already-used
set type, then re-freeze the scorer under a new hash before another official
attempt.  The fixture equations, classifier, solver, witnesses, gates, and
paper renderer must not move.
