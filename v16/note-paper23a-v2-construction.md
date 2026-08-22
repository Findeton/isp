# Paper 23a v2 construction note

Date: 2026-08-22

Disposition: **CONSTRUCTION COMPLETE — SUBMITTED FOR THREE-SEAT BLIND
REVIEW**

## 1. Frozen inputs

All hashes verified on disk; the v2 pin was frozen at ledger #315
before the candidate existed.

| object | ordinary SHA-256 |
|---|---|
| P23a v2 pin (#315) | `26587fb58f4f30eb52f9daff725d547ba1d7547ead6f1255ce2ae2a83d0b5dd7` |
| P23a v2 candidate (this construction) | `c4503bd309bcc54f0c20de2d8f1a28b4b4742c02c5f9eb7d7b2918deb5889209` |
| Paper 13D law | `3b91766fe269e8145766f4622f99e9009c3270530670119735e6045a473de5c9` |
| Paper 13D math adjudication | `ae2c4ef066335c39a0b8057c897c947b06e4270be67d1ed3ec59bf8d6d0a00c9` |
| v1 pin (#309) | `aafb35591bcc5e87417b8d2ee91e13d42935f9f75e9191a0e9dff60cd9d16b0c` |
| v1 candidate (#310, salvage source, not accepted physics) | `9cab8d2e78ee5365b0facc86ff059074f482091bbb3621cfd328939b9e247a5a` |
| v1 construction note | `cc157c793cca620b680dca1d93b83a6726dee1e3b7e044647a9cffde889ea10c` |
| Seat C (#311) | `8af0942fa88519363c62ddfd06fe7d81fd05e001d12698576c61ca8252b80372` |
| Seat P (#312) | `0c6c470fe50eaacd4cc9096c54e6175b91b9a3fb7596c0257a0131b8040eb8f4` |
| Seat F (#313) | `705a47aeac07b6c774fd0aeae695cefc658da19442ee37e5a5f86879f128e9da` |
| #314 adjudication (repair authority) | `68a10261fa0bbc71cf4b19d61acf5c97a2b9a53a26094a94786e7bf3e6b443f1` |

## 2. Authorization compliance

Each binding constraint from the user's authorization, and where it
is discharged:

- trace-sensitive classes retained unless complete readers prove
  equivalence: Definition 2.1 (#314 form) + Proposition B;
- stages 1–2 repaired exactly as adjudicated: all six §3 replacements
  of the pin applied verbatim in candidate §2/§3;
- stage 3 rebuilt honestly: §4 proves/refutes each clause separately
  — no associativity, duals, semiring, fusion ring, or FP character
  assumed anywhere;
- finite-closure failure by carrier monotonicity: Lemma E + Theorem F;
- explicit FP-route closure for present Gamma_D: §4.2 with engraved
  scope;
- no code: prose and exact rational scaffolding only;
- no new physical postulate: every object is built from the census of
  terminal Paper 13D alone;
- no rescue quotient: Proposition C/H keep bracketing-distinct
  classes distinct even though doing so destroys associativity;
- no automatic v3: none exists regardless of review outcome.

## 3. Coverage against pin Section 4

Steps 1–5 executed in order; no stage blocked. Pre-registered
outcomes earned exactly as listed in candidate §4.3; the five
not-earned names are recorded there too. No outcome name was renamed,
split, or merged.

## 4. Control coverage against pin Section 6

Candidate §5 disposes all eighteen carried controls and the four new
controls (19–22), each with a concrete disposition. Mandatory review
regressions: 3, 14, 15, 16, 17, 19, 20, 21, 22.

## 5. Independent arithmetic verification

Exact rational arithmetic (`fractions.Fraction`), run before this
note froze:

- v1 fixture tables reproduced elementwise (U(1): 96 cells / 64 fixed
  / six masses; D∘Q⁰(1): 192 / 128 / eight masses; endpoint
  conditional B² entrywise; bond marginal ½; three-pair pattern
  uniform);
- frontier-support lists for left/right bracketing computed and shown
  non-isomorphic (({1},{2}),({1,2},{3}) vs ({2},{3}),({1},{2,3}));
- primitive-vs-fusion trace-shape separation re-derived (empty vs
  singleton frontier list);
- carrier additivity |x⊗y|=|x|+|y| checked symbolically over sizes
  0–4.

The harness is audit scaffolding only and enters no proof. One
checker bug (an exploratory dead branch in the swap-walk) was removed
before the final clean run; no printed value changed.

## 6. Discipline statements

- Construction-stage writes scoped to
  `v16/paper-23a-v2-trace-sensitive-sector-algebra.md` and this note.
- Line counts at freeze: pin 184 LF; candidate 387 LF; this note as
  hashed below.
- Scope walls restated: no channel odds, opportunity/activity/root,
  Pi_phys, Gamma_struct, chronology, dimension, metric, gravity,
  actuality; Paper 17 gate CLOSED; disintegration-typing correction
  (#308) inherited unused.

## 7. Review request

Three-seat blind review per pin Section 10 — category seat,
probability/multiplicity seat, algebra seat — repo read-only,
rebuilding from published prose, reports frozen separately before
joint adjudication. Mandatory regressions: controls 3, 14, 15, 16,
17, 19, 20, 21, 22. Verdicts ACCEPT / ACCEPT-WITH-FIXES / REJECT,
findings most-severe-first with replacement sentences verbatim.
Adjudication confers or refuses terminal per house rules; no
automatic v3 exists.
