# Paper 23d review — Seat C (category/structure)

Date: 2026-08-22

Disposition: **ACCEPT-WITH-FIXES** (one MAJOR, one MODERATE, one MINOR)

Blind delta review of the #333 construction (`699fe5b7…`, 182 LF)
against pin #332 (`112684d6…`), 13D `3b91766f…`. Lens: definitional
typing of Cpx/Σ_χ and the category-level steps.

## Findings

**F-C1 (MAJOR). Q1's restriction argument needs a functor, not a
"subcategory" gesture.** The singleton-diagram complexes do form a
full subcategory of (the groupoid quotient of) Cpx, but the printed
proof says "restrict to the singleton-diagram subcategory" without
noting that E's covariance on all of Cpx restricts to covariance on
the subcategory only because the subcategory is *full* and the
presentation groupoid acts within it. One sentence establishing
fullness closes it. As printed, the key universal step rests on an
unstated categorical fact.

**F-C2 (MODERATE). Definition 1.1's "realizable over that complex"
is ambiguous between two readings with different Lemma A content.**
Reading 1: decorations the complex could be paired with in some
enlarged law (all pairs — what Lemma A counts). Reading 2: decorations
recoverable from the complex's own history cells under Γ_D (none beyond
field-isomorphism classes — by rank-blindness there is exactly one).
The theorem needs Reading 1; the printed text permits Reading 2, under
which Lemma A is false for labeled-fiber complexes. Required repair:
define the fiber as decoration space *external* to the law — "pairs of
total orders on the carrier modulo transport+swap" — and say plainly
that Γ_D assigns no internal structure distinguishing them.

**F-C3 (MINOR). §6's citation "13D §7.1/§8" for the no-ordered-datum
claim should split:** §8 supplies the vertex-set-not-list fact; §7.1
supplies trace retention; the finite-set nature of occurrence data is
§3.1–3.2. Three citations, three clauses.

## What survived

The pinned σ-algebra (colimit of invariant finite restrictions) is
well-typed and the smuggling audit has real teeth — this seat
independently attempted a refined-σ-algebra smuggle (hiding orientation
in a non-invariant cylinder generator) and confirmed pin §2 bars it.
Scheduler independence correctly prevents staged-trace weighting from
masquerading as orientation supply while remaining a legal weight on
distinct points of Cpx (control 6 respected without conflating traces).
Q3's fiat-declaration branch is the right honest handling of the only
loophole. Control rows PASS. Outcome earned modulo repairs; none
structural.
