# WRC Paper 8 pin addendum — one anchor-hash transcription repair

Date: 2026-08-18  
Scope: provenance only; no physics, fixture, gate, comparator, outcome, or
claim changes  
Parent pin: `v16/note-wrc-pin.md`, SHA-256
`956d26e22515471c49ed95a43b2956d8f73e8bcd662eeacc82215d9527c00f99`  
Parent base commit: `0611966f8b6b5f8e60d8b87e0d5f042278404f91`

## Defect

The parent pin's anchor table transcribes the SHA-256 for
`v16/QUESTIONS.md` as
`91ae5d440d9e28df0a459b0ba73f493a756638b0e4d92c5501755466e9bf19b`.
That string is not the file's digest.

## Exact correction

At the parent pin's own base commit, and still in the worktree at discovery,
the exact SHA-256 of `v16/QUESTIONS.md` is
`91ae5d440d9e28df0a459b0ba73ad2f6bba85a3b9395e8a73f493a756638b0e4`.
`git diff --exit-code` between the parent base and the discovery worktree is
empty for that path. The defect is therefore a pin transcription error, not a
post-pin source movement.

The corrected digest replaces only that one table cell for every WRC runtime
anchor and verification. All tokens, clauses, questions, frozen outcome
words, gates, mutants, chronology, and scope walls in the parent pin remain
unchanged. In particular, this addendum does not authorize reading any
in-flight or completed Paper 3–7 hostile report during WRC scoring.

## Refusal rule

WRC must continue to refuse without writes if `v16/QUESTIONS.md` differs from
the corrected digest above, or if either this addendum or the parent pin is
missing from the committed provenance chain.
