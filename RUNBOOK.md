# ISP PROGRAMME RUNBOOK

How this project is run and validated. Written 2026-07-29, at the v12 halt
(LOG #42), distilled from the practices that produced the W-batch, W6, W7,
and paper 1. **Any agent working in this repository follows this document.**
Where a rule cites a ledger entry (e.g. #36), that entry records the failure
that made the rule.

---

## 0. Authority and standing constraints

- **The user owns:** the publication route (never act on it, never prepare
  submissions unbidden), unit ordering and go/no-go, paper splits/merges
  (paper 1 is NEVER to be split — user order), reopening anything frozen.
- **Frozen, do not touch:** `v11/` (halted at its LOG #24), `bc/` (halted at
  its LOG #4), the v9 review (never reopen — user order, v8/LEDGER.md #128).
  Commit `25a959e`'s additions (v11 U1c + bc partials) are UNREVIEWED and not
  citable.
- **HALT discipline:** when a batch closes, STOP. Report, then do nothing
  further without the user's word. Do not start units, papers, or reviews
  on your own initiative.
- **Live state pointer:** read both `v12/LOG.md` and `v13/LOG.md` from their
  last entries backwards.  Paper 2 is terminal at v12 #46.  The user's
  binding order is: GW2 regional-descent census → RQ0 regional causal arena
  → RQ1a scalar → RQ1b Dirac → GR1 backreaction; Maxwell may accompany
  early GR1 but precedes any general-matter universality claim.  GW2 is
  GREEN-UNREVIEWED at v13 #9 with `GW2-BLOCKED-AT-1`: v10's regions belong to
  the old supplied classical record carrier, while the live Barandes/W3–W6
  lineage exports charts but no derived finite spacetime-region object.  No
  descent equation was posed.  The next possible unit is a pinned Barandes
  regionalization/RQ0a construction; it awaits the user's word.  No
  RQ0/RQ1/GR1 construction may begin without its own committed pin and the
  preceding gate.

## 1. The unit cycle

Every research unit moves through exactly these stages, each one committed:

```
PIN (frozen) → CONSTRUCT (worker) → ADJUDICATOR VERIFY → COMMIT green
→ HOSTILE ROUND (external) → ADJUDICATE → REPAIR (worker) → VERIFY
→ COMMIT → TERMINAL (ledger confers it)
```

- Nothing is citable until TERMINAL. GREEN-UNREVIEWED means "exists,
  verified to run, not yet attacked."
- Internal audits (a worker's own, or the adjudicator's) can force repairs
  but only an EXTERNAL hostile round can confer terminal (#40).
- Treat every positive headline as provisional until it survives its round.
  House history: early positive headlines died 9-for-9; what survives are
  numbers; what dies are sentences. Write accordingly.

## 2. Pins

A pin is frozen and committed BEFORE any construction starts. It contains:

1. The question, one box.
2. The operationalized steps, in order, with the FIRST step being a
   referent/instrument census whenever the unit builds on claimed
   instruments (GW1 precedent: `BLOCKED-AT-⟨referent⟩` is a first-class
   outcome, not a failure).
3. **Pre-registered outcomes only** — including the honest negatives. The
   worker may not invent a verdict name.
4. Kill conditions, explicit.
5. The anchor list: which committed numbers/files the unit must reproduce.
6. Receipt rules (see §4), runtime cap, file whitelist.
7. Scope engravings (what the unit does NOT decide).

**The four-gate rule** for every newly introduced object (paper 0 §5):
Referent (definable from committed primitives, or labelled a postulate) /
Necessity (which measured obstruction requires it) / No-smuggling (the
definition must not contain what it is meant to explain) / Discriminator
(what would distinguish it from alternatives). Apply it IN WRITING.

## 3. Workers and dispatches

- Workers run in the background (Opus-class), one unit per worker, bound to
  the frozen pin by commit hash.
- Every dispatch includes: the read-list (pin first), the file whitelist
  ("you may create/modify ONLY these paths"), the house-rules block (§4),
  the stall doctrine (no silent command > 8 min; progress prints; total
  compute cap), the report format, and: **no git mutations — the
  adjudicator commits.**
- `cd /Users/felixrobles/workspace/isp` at the start of EVERY shell command
  (CWD resets between calls). Interpreter: `/opt/homebrew/bin/python3.13`
  (bare `python3.13` is not on PATH). Exact-arithmetic units must not need
  numpy; if a diagnostic truly does, `code/.venv/bin/python3.13`.
- **FREEZE-ON-DELIVERY** (#36): the worker's final run IS the delivery;
  zero edits after it; workers do NOT launch their own child audits — the
  W6 worker edited its unit three times while its self-launched audit ran,
  poisoning the audit's line numbers.
- If a worker dies on a server error (500/529), resume the SAME agent with
  a message: state what the working tree preserves, order an
  applied/partial/remaining inventory of its own fixes before it touches
  anything, then continue. After repeated deaths, the adjudicator completes
  mechanical remainders directly (#41) — never re-derive physics by hand,
  only verify, rerun, and account.

## 4. Receipt and code discipline (the heart of validation)

- **Exact arithmetic only** in substantive paths: `fractions.Fraction`,
  cyclotomics as integer coefficient tuples reduced mod Φ_n (tuple equality
  IS field equality), exact real subfields with sign oracles where order
  matters. No floats, no tolerances, ever. A float sweep (grep + AST) is
  part of every review.
- **Anchors are exit-1-only:** every committed number a unit reuses gets an
  assertion that kills the run loudly on mismatch. Substantive negative
  results exit 0 with the negative printed.
- **Counts must be computed, never typed** (#24: a hard-coded 6561 survived
  a unit AND its hostile round; the true value was 729).
- **Every gate must be a measurement that could have come out otherwise**
  (#36). The W6 circularity catalogue is the checklist of sins: a gate that
  restates its own constructor arguments; a comparison of an object with
  itself; a hard-coded Φ set; a search whose filter reduces the advertised
  scope from 72 to 2 without saying so; a "second" gate that recomputes the
  first; a branch that never executes with no positive control; a claim
  whose table cell has no gate at all.
- **Controls, both directions:** every mechanism needs a positive control
  (it fires when it should) and a negative control (it fails when it must).
  A zero without a positive control is not a result (#36, M5).
- **Falsification self-test:** deliberately break one anchor → the receipt
  must exit 1 visibly. Run it; report it.
- **Determinism:** two full runs, identical modulo timing stamps.
- **Declared scope everywhere:** strides, caps, sample vs exhaustive, which
  dimension, which support class — printed in the receipt AND stated at
  every claim in the note ("exhaustive n ≤ 4; sampled at n = 5; general n
  open" is the model sentence).
- Receipt truncation must not hide flagship values (#40 F12).

## 5. Adjudicator verification (before ANY commit of a delivery)

1. `git status --short` — ONLY the whitelisted files changed. If a worker
   is mid-flight, its working-tree edits are never committed (the v11-era
   directory-sweep incident is why staging is explicit paths, never `git
   add <dir>/`).
2. Independent full rerun; diff against the delivered receipt modulo
   timings (strip `[N.Ns]` stamps).
3. md5-pin the delivered files whenever any audit will cite line numbers;
   confirm the audit's pin matches disk before acting on its findings.
4. Spot-read the load-bearing repaired/new passages (grep the fix markers).
5. When an audit arrives against a flawed delivery: **commit the flawed
   state AS-IS first** so the findings have a permanent referent, with the
   ledger entry saying exactly that (#35+#36). Then repair on top.

## 6. Hostile rounds

- External reviewer, background, repo READ-ONLY, own code in the session
  scratchpad, **independence**: rebuild from the published prose, import
  nothing from the unit.
- The dispatch enumerates the attack surface: proofs line-by-line;
  quantifier scopes; an independent numbers table (claimed vs. mine, every
  load-bearing quantity); witnesses reconstructed from specification;
  source-quote verification against the FETCHED originals (arXiv), page and
  equation numbers included; attribution boundaries (antecedent vs.
  contribution); the note's sentences (any claim broader than its gate);
  stress attacks of the reviewer's own design.
- Verdict vocabulary: ACCEPT / ACCEPT-WITH-FIXES / REJECT, findings ranked
  most-severe-first with severities (FATAL/MAJOR/MINOR/NOTE) and
  replacement sentences supplied verbatim.
- Rounds may CONTRIBUTE constructions (the φ-criterion, #23); repairs gate
  them natively with inline credit ("the hostile round's construction").
- Repair workers apply ALL fixes; numbers may not move unless the round
  proved them wrong; the adjudicator re-verifies and only then confers
  terminal in the ledger. The note's Status line is then set TERMINAL with
  the full provenance chain (delivered #, round #, repair #, terminal #).

## 7. The ledger (each version's LOG.md)

- Append-only, numbered entries, one per event. NEVER rewrite an entry.
- **Forward-only corrections:** errors — including the adjudicator's own —
  are corrected by NAME in a later entry (#21's wrong denominator fixed in
  #23; #38's "independently rebuilt" phrase fixed in #40). Owning errors is
  mandatory; silently smoothing them is the cardinal sin.
- **Dispatches are recorded only AFTER they occur** (#11/#15: two entries
  once said "dispatched" before it happened).
- Every commit maps to a ledger entry; the commit message names it
  (`v12 #NN: ...`).

## 8. Git

- `git commit --no-gpg-sign`, trailer:
  `Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>`.
- Stage EXPLICIT paths only. Never sweep a directory.
- Commit granularity = ledger granularity. Pins are committed before
  dispatch (frozen means committed).

## 9. Papers

- **Single-threaded** (user rule): papers state results; no correction
  narrative, no process story, no review history — that lives in the LOG.
  Internal reviews are authorship.
- **Paper 0** (per version) is the programme charter: amended by DATED
  passes (v2.2, v2.3, ...), each pass one ledger entry; it carries the
  ontology, the unit registry with outcome headers, non-claims, and the
  four-gate rule. Results papers never ontologize; the charter's ontology
  section is scoped by postulate labels and NOT-lists.
- **Paper 1 standard (self-contained, publishable):**
  - Citations to EXTERNAL literature only; a mechanical FORBIDDEN-TOKEN
    audit (unit labels W1–W7/GW/BC/U#/T#, corpus versions, LOG/ledger/pin/
    hostile/terminal/green-unreviewed/ISP/SHARD, note filenames) must
    return zero.
  - Every theorem proved in-paper or externally cited with the paper's
    delta delimited; every witness model RECONSTRUCTED in-paper with fresh
    bundle code; definitions must DETERMINE their objects (the paper-round
    F1: a definition that fixes only one column of a matrix does not define
    the model — print the matrix).
  - A code bundle (`paper1_code/` pattern) regenerating EVERY number, exact
    arithmetic, self-anchors exit-1-only, master runner + receipts table +
    RUN.txt. One declared unanchored number is a disclosure, not a secret.
  - **Rendering rules (markdown/KaTeX):** structured math (matrices,
    aligned, multi-relation) in `$$` display blocks only; `pmatrix`, never
    `psmallmatrix`; no `\\` or `&` inside inline `$...$`; NO text-mode
    LaTeX in prose (`\emph`, `\textbf`, `\cite`, `\ref` are defects —
    markdown only; a backslash outside a math span is a defect); escape
    pipes in table cells (`$\lvert$` not `$|$`).
  - References journal-grade: every entry has author/title/venue/year;
    every entry cited in the body; every bracket resolves; load-bearing
    clauses have pinned sources.
  - Scope tags on every contribution and every numbered result; consecutive
    numbering; cross-reference validation (zero dangling).
  - The paper gets its OWN hostile round (self-containment gate, number
    sweep, proof audit, attribution audit, quote verification, register)
    before "publishable" is claimed.

## 10. Verdict and status vocabulary

- File status ladder: `PIN` → `GREEN-UNREVIEWED` →
  (`GREEN-UNREVIEWED-REPAIRED`) → `TERMINAL` (set only by the adjudicator,
  with the ledger chain in the status line).
- Unit verdicts: pre-registered names only, of the form
  `UNIT-OUTCOME(-QUALIFIER)`; combinable when the pin says so; the terminal
  entry states which earned conditions hold and at what scope.
- Discriminator-style vocabularies (W6's |Φ|: ABSENT / FORCED /
  UNDERDETERMINED / VACUOUS / NO-INSTRUMENT) must be used consistently:
  a table cell may not editorialize against its own measured value.

## 11. External reviews from the user

The user periodically delivers external reviews ([REV], [REV2], ...).
Protocol: adjudicate each claim (verify the mathematics YOURSELF before
adopting — hand-check constructions, run the counterexamples), adopt with
attribution in the ledger, fold paper-level items into running rounds as
amendments, and record what was adopted vs. corrected. External reviews
outrank internal enthusiasm and have killed two founding formulations
(v1's H¹; the Bargmann mistyping); expect casualties and record them.

## 12. Memory vs. repository

The adjudicator's persistent memory files are session infrastructure, NOT
project ground truth. The repository is the ground truth: LOGs, pins,
notes, receipts, papers, this runbook. Another agent needs nothing outside
the repo except this rule.

---

## Appendix: the failure catalogue (why each rule exists)

| Ledger | Failure | Rule it made |
|---|---|---|
| v11-era | `git add v11/` swept another worker's file into a commit | explicit paths only |
| #11, #15 | "dispatched" written before the dispatch | record dispatches after they occur |
| #21→#23 | adjudicator summed denominators (10,064 vs 10,050) | forward-correction by name |
| #24 | hard-coded 6561 (true 729) survived unit + round | counts computed, never typed |
| #35–#36 | worker edited while its own audit ran; audit line numbers stale | freeze-on-delivery; no child audits |
| #36 | 22 circular/vacuous gates carried a table | every gate falsifiable; positive+negative controls |
| #38→#40 | "independently rebuilt" — the rebuild was gated EQUAL | describe mechanisms as measured, not as intended |
| #40 F1/F2 | descent measured at one setting, stated unscoped | scope tags at the claim, not just the receipt |
| paper F1 | a definition fixing one column of V "defined" a model | definitions must determine their objects |
| #41 | 3× server-killed worker | resume-with-inventory; adjudicator finishes mechanics |
