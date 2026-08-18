# RFB result-neutral fixture freeze

**Frozen:** 2026-08-18, v16 ledger #132.

**Status:** DATA-ONLY PHYSICAL FIXTURE FROZEN — SCORER HAS NOT BEEN CREATED
OR RUN; NO RESULT OR PAPER 10 CANDIDATE EXISTS.

## 1. Frozen object

| object | SHA-256 |
|---|---|
| `v16/code/rfb_fixture.json` | `f3557b3400584d01984c6a4f38d40744c9e2cf2f0e36c7c4aa225b045e5bd362` |

The fixture is downstream of the committed public core event `a7b1051` and
binds all three public artifacts by hash. It also binds the RFB pin, terminal
QSF result and law-type correction, E-37 sufficiency method, JS-v2 predictive
obligation, v15 causality standard, and Paper 1 history architecture. The
untracked SCOUT-T files are explicitly outside the read set.

## 2. Registered rows without answers

The JSON contains:

- fourteen named assumption toggles, each with an impose reading and a drop
  control;
- eleven nontrivial assumption/freedom cells whose two directions the scorer
  must measure;
- the `q=2,3,4` dial rows;
- all-permutation writers, all edge-phase decorations, all pointer-indexed
  readers, and all writer-step/reader-charge pairs;
- classical, coherent, and exact `3/5` hybrid tags at one common final port
  type;
- a two-history, two-port, two-cut interference arena;
- equal-resource predictive rows and a held-out horizon;
- append-only, reset, and redundant-record recovery grammars; and
- fixed-factor local channels plus a trace-amplifying drop control.

The file declares the pin's allowed result vocabulary and scope walls as a
schema. It contains no selected word, expected count, primary, verdict,
survivor count, paper prose, or gate result. No scorer source or official RFB
output exists at this event.

## 3. Freeze checks

The file parses as canonical JSON input. All thirteen anchor digests match the
committed bytes; assumption identifiers are unique; every forcing cell names
only registered assumptions; the three dials and three record-mode rows are
total; and the three-output whitelist is exact. A pre-freeze absence check
confirms that `rfb_score.py`, `rfb_output.txt`, `rfb_receipt.json`, and
`paper-10-record-feedback-boundary.md` do not exist.

## 4. Next immutable event

The next event may freeze a scorer against this exact fixture and the #131
core. The scorer may be compiled and statically inspected, but it may not be
executed on this physical fixture until its own source hash has been committed.
Any fixture edit after this event requires a disclosed re-freeze before a
physical run.
