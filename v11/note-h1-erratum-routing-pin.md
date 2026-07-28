# v11 H1 — ERRATUM ROUTING (housekeeping unit, PIN)

**Status:** PIN, STRICT, 2026-07-27.  **Binding specification:**
paper 0 §6.7 (the unrouted-erratum duty) + the catalog [V11-CAT]
§5's errata census.  A documentation unit: no new claims, only
routing corrections the corpus already owns to the places readers
will actually meet them.

## The two routings

1. **The BC/Cauchy-Schwarz erratum.**  The correction exists but is
   unrouted: readers of v6 paper 7 §12, paper 26, and v10 paper 18
   can still meet the uncorrected claim with no pointer.  Route it:
   - v6/v7 are FROZEN — no edits to frozen papers.  The routing
     lands in the status layer: `v6/ARCHIVE-STATUS.md` (or the
     archive-status file the corpus actually uses — worker locates
     it; if none covers the affected papers, create the minimal
     status note beside them) gains an erratum line per affected
     paper, quoting the correction and citing its committed source.
   - v10 paper 18 is LIVE-ERA: it gets a forward-only erratum
     footnote at the affected passage (v10's forward-correction
     convention, not a rewrite).
   - v8/LEDGER.md gets one entry recording the routing (the ledger
     is the corpus's correction spine — catalog §0.4).
2. **The v4 effective-GR descent erratum.**  The catalog found the
   v4 effective-GR descent claim was later corrected in substance
   but NEVER errata'd anywhere.  Same routing pattern: status-layer
   erratum line beside the v4 paper (frozen — no in-paper edit),
   citing the committed later correction; one v8/LEDGER.md entry.

## Gates

- Every erratum line QUOTES the correction from its committed
  source (file/line cited) — no new mathematical content authored
  in this unit; if the worker cannot locate a committed source for
  the v4 correction's substance, the erratum line states the claim
  is [DISPUTED-UNROUTED] and says so rather than inventing the fix.
- Frozen files untouched (v1–v7 papers, v6 corpus): verified by
  `git diff --stat` in the receipt — only status files, v10 paper
  18, v8/LEDGER.md, and v11 files may change.
- The catalog's third carried erratum (119→137) checked: if
  already routed, say where; if not, route it by the same pattern.

## Scope

Routing only.  The 1.82 downgrade is already carried in the
catalog's graded entries and needs no new routing unless the worker
finds an unpointed reader path — in which case same pattern.
