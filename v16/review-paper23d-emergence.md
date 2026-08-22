# Paper 23d review — Seat Q (quantum/emergence)

Date: 2026-08-22

Disposition: **ACCEPT-WITH-FIXES** (one MAJOR, one MODERATE, one MINOR)

Blind delta review of the #333 construction (`699fe5b7…`, 182 LF)
against pin #332 (`112684d6…`), 13D `3b91766f…`. Lens: emergence-gate
discipline — what the negative result licenses, quantifier honesty,
scope walls.

## Findings

**F-Q1 (MAJOR). Theorem C's conclusion overstates one clause: "the
orientation observable is not … made unique by any state weight" is
proved only for extractors well-defined on the pinned joint space.**
The fiat-declaration branch shows output laws coincide across P —
uniqueness fails *relative to the pinned σ-algebra*. A weight that is
not a function on Cpx (e.g., a genuinely history-dependent selection,
explicitly excluded by #308 control 5 as physics-retuning) is outside
the theorem by construction, and §5's ledger says so; Theorem C's own
sentence should carry the same qualifier rather than a stronger bare
reading. One-clause repair in the theorem statement.

**F-Q2 (MODERATE). §6's second attribution ("even a fiber-varying
weight over histories could not read an order out of H") reaches
beyond what is proved here.** That claim concerns hypothetical weights
on the history side — outside this unit's pinned spaces — and rests on
13D rank-blindness applied to *fields*; a hostile reader could note
that a history-side selector might condition on trace-level structure
(fields plus generator arrangement) not covered by Lemma C as printed.
Either scope the sentence to "no admissible observable of the pinned
joint space", or cite precisely which 13D clauses bar trace-arrangement
readability (§7.1 retains traces but §9.1 quotients by stabilizer, and
§8 bars serialization). Scope it; the citation route belongs to a
future unit.

**F-Q3 (MINOR). §4 outcome block prints `-NOT-SELECTED` as "superseded"
— pre-registered outcome names should be earned or explicitly marked
NOT EARNED, never superseded.** Use the pin's own convention: list it
under not-earned with the reason.

## What survived

This is the correct deep form of the negative: not "no Π works" but
"*no measurable copy of orientation exists in the typed joint space*",
which is exactly the failure attribution pin §7 demanded and exactly
what makes the result robust to richer weight families. The door
distinction from synthesis §3 is respected — the paper does not claim
anything about law-level symmetry breaking, root states outside Cpx,
or non-scalar extensions beyond flagging them as out-of-scope. Paper 17
and dimension stay correctly closed; the conditional-state-induced
positive branch was correctly NOT claimed since no positive case
exists. Control rows PASS. Outcome earned modulo repairs; none
structural.
