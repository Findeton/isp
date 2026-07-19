# D44e round 1 — hostile review: the per-type reception census

**Object:** LOG #359 (commit 2a289e5) — `v10/note-d44e-reception-census.md`
(pin §1–4 + amendments A1–A7), `v10/code/d44e_reception_census_exact.py`
(880 lines, 46 PASS / 0 FAIL), `v10/data/d44e_reception_census_exact.out`
(85 lines). Reviewed against the d42b4 R6 carried obligation
(`reviews/d42b4-round1-hostile-review.md` lines 499–503, 635–640), the
d43c F-C1 conviction class (`reviews/d43bc-round1-hostile-review.md`
line 364 ff.), the committed layer sources (d42b3, d42b2, d42b1), d43c,
and D25/D27.

## VERDICT: REVISE — 0 BLOCKER / 2 MAJOR / 4 minor / 3 nit

Every numerical headline survived independent recomputation: the 11-type
inventory re-derives from the two committed heads under a *different*
scanning method (AST, not regex); all 6,567 instances re-classify
identically under a referee-built strict full-shape classifier (zero
malformed, zero disagreements with the receipt's predicates); every
distinct-record count, key count, imprint-collision count (p 309 /
v.arb 17 / v.mrg 3 and the other six), the 4 multi-creator versions, the
strong (actor,base) census 0/1191, the A8-fake refusal, the 0.2599...
literal (= 1/√2 − 1/√5, matching the committed d42b4 80-digit value),
the RG3 memberships/Born, and the RG4 grain facts all check. Reruns are
byte-identical (unseeded, PYTHONHASHSEED 0/7, from `/`, and from a
path-relocated copy); exit-1-by-design fires at the right gate under all
four commissioned mutant classes plus a source-scan mutant. No
`check(True)`; one benign crash-mode assert (line 74).

The two MAJORs are not about the numbers. (M-1) RG2's 27 per-type gate
predicates are construction-tautologies — the copy map is unconditionally
isometric and both lossy controls fire unconditionally when they run — so
the per-type carrier-imprint content that makes the census "per type" is
carried entirely by unanchored prints: my constant-imprint mutant runs
**46/46 silent-green** while the r-type's delivered "INJECTIVE" print
silently flips to "253 colliding pairs". (M-2) Amendment A5's
"(identical text, declared)" is **false**: the d42b2-embedded transport
head is the *pre-#300* d42b1 semantics whose merge-denominator rule
d42b1's own round-1 F1 convicted as a BLOCKER and repaired; the two
layers diverge **on this unit's own gated anchor point** (the D2H merge:
1/16 embedded vs 1/24 under terminal d42b1). Both fixes are
prose/anchoring repairs; no delivered number changes.

---

## Findings

### M-1 — MAJOR: RG2's per-type gates cannot fail for the object under
### test; the per-type content is print-anchored, and a corrupted
### imprint reader runs silent-green

`d44e_reception_census_exact.py` lines 600–689 (`run_type`): the
reception map `V: e_i -> e_i ⊗ e_{sh(i)}` (lines 612–616) is an isometry
for **every** function `sh` — the gate `dev < TOL` (line 649) tests a
mathematical triviality of the copy template, not a property of the
layer. The diagonal control (lines 654–660) evaluates the same fixed
2-dim geometry for every type (violation ≡ 1/√2 − 1/√5; the printed
"per-type" value is type-independent by construction), and the shadow
control (lines 661–687) yields violation exactly 1.0 whenever any
collision exists — `okC` and `okS` are unconditionally true on every
execution path. Consequence: of the banner's pre-registered outcomes
(lines 86–88, "a failed reception gate would be a DELIVERED finding"),
the reception-gate-failure outcome is **unreachable** — only a corrupted
receipt (my MUT-D) can fail these lines, never the layer.

Demonstration (MUT-F, scratch copy): replace `shadow_of` (lines 587–594)
by the constant `'X'`. Result: **exit 0, 46 PASS / 0 FAIL**. The .out
drifts only in unanchored detail strings — p's collisions 309→780, and
RG2-r's "shadow imprint INJECTIVE on the realized basis (0 collisions)"
becomes "253 colliding pairs" — i.e. the LOG-#359 delivered facts "r and
ka have INJECTIVE realized imprints" and the seven collision counts are
protected by **zero gates**. The same holds for the finding gate at line
715: `len(multi_cr) >= 1` — the delivered "4" is print-only. (Mitigant,
acknowledged: the corpus's byte-diff-vs-committed-.out convention makes
the drift *visible at review time*; MUT-F is not a blocker for that
reason. But this unit's whole claim is the per-type structure, and the
receipt's own anchoring discipline — RG0b-i anchors 1191/4502 in-gate —
is not applied to it.)

This also bears on wording: the verdict line (877–880) "no shared-form
shortcut" and LOG #359's "The d42b4 R6 carried obligation is DISCHARGED
at fixture scope" are true only under the second-arm reading of R6 (the
census obligation). The first arm — "implement the four types' actual
reception maps on their actual registers (delivery on the {s,r} joint
register with chain transport; merge with supersession update)" — is
*not* delivered: all nine maps are one copy-form template instantiated
per type (record identity ⊗ carrier-footprint label; no register
dynamics, no chain transport, no supersession update). The .out disloses
the template inline on every line (honest), and the pin licensed it
("probe pairs from the enumerated instances"; "the d42b4 convention"),
so this is not the d43c F-C1 fabrication class — the objects exist and
are load-bearing per MUT-D — but the discharge sentence should say
*which* reading is discharged.

**Fix (prescribed):** (i) anchor in-gate: per-type basis sizes
(40/23/3/4/3/3/3/3/1/20/3), the collision vector (p 309, r 0, d 1, m 1,
ko 1, kc 1, ka 0, v.arb 17, v.mrg 3), the r/ka injectivity booleans, and
`len(multi_cr) == 4`; (ii) add one clause to the verdict + LOG forward
note: "per-type = the type's own realized basis + its own carrier
imprint under the shared d42b4 copy-form template; the isometry gate is
existence/demonstration, its falsifiable content is the probe-sanity +
control-fire + (newly anchored) imprint structure"; (iii) scope the R6
discharge to the second arm explicitly, naming the first arm
(layer-semantic reception dynamics) as an open successor.

### M-2 — MAJOR: A5's "identical text" is false; the transport pricing
### this census rides on is the pricing d42b1's own round CONVICTED,
### and the divergence hits this unit's gated anchor point

Note lines 92–95 (A5): "transport d/m semantics sourced from the
d42b2-embedded d42b1-verbatim head (identical text, declared)."
Referee diff of `d42b1_transport_exact.py` vs the d42b2 head: `vname`,
`mname`, `value_of`, `event_poset`, `canon`, the `d`-branch and
`regs_of`'s d/m lines are textually identical, **but** `admissible`'s
`n`- and `m`-branches differ materially: terminal d42b1 (post-#300)
computes the idle `has_am` bit and the merge denominator via
`admissible_arb_ckeys(acts, a, actors)` (lines 252–280 — "the C1
repair: ...the admission relation, probed, not the own-view component
list"), while the d42b2 embedding uses `arb_components_in_view(view, a)`
— the own-view component rule that LOG #299's **F1 BLOCKER** convicted
("the merge denominator count[s] OWN-VIEW components unfiltered by
admission — the d42a conviction class") and #300 repaired. Chronology:
d42b2 went TERMINAL at #298 ("4,012 functional comparisons, 0
mismatches") *against pre-repair d42b1*; d42b1 then changed at #300;
no post-#300 reconciliation of the embedding exists anywhere in the LOG
or notes (grepped). d44e's A5 is the first committed sentence to assert
identity — *after* the divergence arose.

Extensional check on this unit's own corpus (all 66 non-click fixture
events, both layers): 63 agree; 2 are d42b1 crashes on click-bearing
prefixes (expected — clicks are d42b2's extension); **1 real price
divergence: FXC2m's merge `mB1` after D2H — d42b2-embedded 1/16,
terminal d42b1 1/24** (admissible_arb_ckeys finds 2 arb ckeys —
{t1A,t1B} and B's own singleton {t1B} — + 1 merge pair ⇒ D = 3).
The 1/16 is exactly the "merge@D2 = 1/16" anchor that RG0b-iv (receipt
lines 355–380) re-gates and that d42b2's committed M4 line carries. The
citation *to d42b2* is accurate; the A5 provenance chain *to d42b1* is
not. Form-level census content (admissibility bits, regs_of, record
shapes) is unaffected — the divergence is a price — but the RG2-m
weighted probe's "exact layer mass" (W_FIX, receipt line 344) includes
the disputed 1/16, and the unit's story ("the transport types censused
at the SIG-chain grain") silently means "at the d42b2-frozen,
pre-conviction pricing".

**Fix (prescribed):** (i) forward-correct A5 (the #304/#316 mechanism):
"verbatim at embedding time (#298); d42b1's #300 C1 repair postdates the
embedding; d/m *form* semantics identical, merge/idle *pricing*
divergent — exhibited at D2H: 1/16 (embedded) vs 1/24 (terminal)";
(ii) add a printed scope line to the receipt (or the round-1 forward
note) stating the transport prices cited here are the d42b2-committed
ones; (iii) route to the board as a carried question: which transport
pricing is canonical at the SIG grain — the corpus currently carries two
committed receipts whose pricing rules disagree at a gated record point,
and the convicted rule is the one downstream units keep citing.

### m-1 — minor: headline census numbers are print-only where the
### receipt's own discipline anchors elsewhere

Gated: 1191, [1,7,39,215,1191], 4502, p+r+n *sum* = 4502, v0 = 1191,
v.arb = (r count), zero unclassified/multi/multibase, 0/1191, the M4
anchors, 11/11 realized. Print-only (no gate): the per-type family split
2128/748/1626 (receipt line 236 anchors only the sum; LOG #359 quotes
the split), the fixture totals 90 + 36, N_ALL = 6567 (line 397 —
detail-string only; the verdict interpolates it), every RG1 distinct
count, key count, and carrier signature, and the RG2 collision counts
(see M-1). All verified correct by recomputation — but a split-drifting
bug would run green. **Fix:** anchor the split (2128/748/1626), the
fixture totals (90/36), and N_ALL == 6567 in the RG0b-ii/RG0 predicates.

### m-2 — minor: the layers' kind dispatch is open at the r/else branch
### — "derived from the grammar" is generator-scoped, not
### checker-scoped

Both committed `admissible` functions fall through to the arb branch for
*any* unknown tag: referee probe `('z','A',CK,{tA})` after [pA0,pB1] is
**admissible at 1/8 in both layers**, and `regs_of` treats it as an r
(writes a created vname into the registers). The 8-kind inventory is
sound for the *generated* corpus (d42b3's `candidates_for` emits only
p/r/n; the fixtures are committed lists; RG0's zero-unclassified gate
would catch an alien instance), but RG0a-iii's "completeness by
construction" silently assumes a closed dispatch the checker does not
enforce, and the kind-scan (receipt lines 91–104) derives 'r' from
`View`'s classification lines alone (the admission branch never names
'r'). **Fix:** one scope sentence in the note ("kind-closure holds at
the generator, not the admission checker — alien tags alias to r
semantics"), or an added refusal gate in a successor layer touch.

### m-3 — minor: "WIRE-MEDIATED" (A7-ii, LOG #359) overstates what the
### mwire does

Verified: the created mname is absent from `regs_of(m)` (= {actor,
('mw', actor, pk)}), and it enters views via `View.created` — the
receipt's RG1 line says exactly this, honestly. But the referee census
also shows the `('mw', ...)` register is written **only by the m event
itself and never touched by any other realized record** (and no other
kind's `regs_of` can produce one): the wire mediates nothing downstream;
the causal linkage of the created version runs through the initiator's
actor register and the derived created-map. "Wire-mediated creation"
suggests transport along the wire. **Fix:** reword to "created
OFF-REGISTER (the mname is not written into any creation register; the
mwire is a write-once pricing carrier; visibility enters via
View.created)".

### m-4 — minor: the grain list under-describes the unrealized
### post-merge stratum

RG4-b prints "realized merge pairs containing an mname = False". The
stronger referee fact: **no realized record of any type contains an
mname anywhere** — p bases are {V0, v1, vc}, d payloads {v1, vC, vc},
all ckeys sit on V0/v1/vc, merge pairs are vname-only. So the entire
post-merge stratum (p/d/clicks/arbs *on* merge-created bases) is
unrealized, and v.mrg records are gated only as *outputs*, never as
inputs to any reception. This is implicitly inside RG4-c's transport-
depth grain but is checkable and worth its own printed line — A6's
"three grains" is a coarser slicing than the census itself supports.
**Fix:** add the printed fact "mname occurs in zero realized input
slots" to RG4-b or -c.

### n-1 — nit: "re-run verbatim" (RG2-0) is a faithful
### re-implementation, and the literal is a truncation

The d42b4 NSE block (d42b4 lines 271–298) is matrix-based; d44e's RG2-0
is list-based with identical probes/map/control (verified equivalent;
the control value equals 1/√2 − 1/√5 exactly). `LIT2599` (lines 559–560)
is the committed 80-digit value with the last digit dropped (truncated,
not rounded) — immaterial at dps 50 / 1e-40, but "verbatim" and the
literal's provenance deserve one honest word.

### n-2 — nit: LOG #359 "the committed literal matched at 1e-40" reads
### wider than the gate

The literal match is gated once, at RG2-0 (3-dim anchor). The nine
per-type diagonal controls are gated at > 1/100 only; their printed
digits coincide because the construction is the same 2-dim geometry
(see M-1). One clause in the forward note fixes the reading.

### n-3 — nit: unguarded empty/thin-basis paths behind the gates

MUT-A (dist_all['m'] emptied) crashes at the RG1 table line 511
(`max(ars)` on empty) *after* RG0 correctly FAILs; `run_type` would
IndexError at n < 2 (u2[1], line 623). Exit is 1 on both paths, so gates
are not maskable — but the failure mode is a traceback, not a verdict.
Cheap hardening if touched again.

---

## Independent-recomputation inventory (referee-built, scratchpad)

Script: `scratchpad/d44e/referee_verify.py` — 32/32 after fixing a
py3.8 AST quirk in *my* scanner (receipt unaffected). Confirmed:

1. **Kind scan, different method** (AST Compare-node harvest incl. `!=`,
   list/set containers, kind-var aliasing): d42b3 head {n,p,r}; d42b2
   head {d,ka,kc,ko,m,n,p,r}; **full-file** scans add nothing.
2. **Version constructors:** V0 2-tuple; vname 5-tuple ('v', base≠'m');
   mname 5-tuple ('v','m',...) — disjoint, jointly exhaustive on
   realized versions.
3. **Family** (layer's own enumerate_family): 1191; per-depth
   [1,6,32,176,976]; 4502 events; strict full-shape classifier: p/r/n =
   2128/748/1626, zero malformed; v0 1191 + v.arb 748 under the declared
   convention; zero multibase ckeys.
4. **Fixtures:** 90 events (p33/r14/n2/d13/m4/ko8/kc8/ka8) + 36 versions
   (v0 10 / v.arb 22 = 8 ka-written + 14 created / v.mrg 4); every
   non-click event independently re-admitted in place; grand total 6567.
5. **Distinct counts:** 40/23/3/4/3/3/3/3/1/20/3 — all match.
6. **Receipt-PREDS vs strict classifier:** zero disagreements on all
   realized records; over-broad tag-only acceptance demonstrated on
   synthetics (('p','A'), 6-tuple 'd', ('v','v0',...)-5-tuple → v.arb) —
   none realizable by the generators (documented, no gate impact).
7. **Collisions (full basis):** p 309, r 0, d 1, m 1, ko 1, kc 1, ka 0,
   v.arb 17, v.mrg 3; **key counts** 21/8/3/2/1/2/2/2/1/9/1.
8. **Strong census:** 0/1191; A8-fake `[('p',A,V0,0),('p',A,V0,1)]`
   refused by the layer.
9. **Findings:** exactly 4 multi-creator versions — ('v',V0,(x),(I),I)
   for x∈{0,1}, I∈{A,B} (self-arb {I,v} vs pair-arb {A,B,v} imprints);
   count invariant when creators are collected over *all* r positions,
   not only cut positions. mname ∉ regs_of(m); mwire written only by m.
10. **0.2599... :** 1/√2 − 1/√5 at dps 85 equals the committed d42b4
    80-digit literal; receipt literal = its 79-digit truncation.
11. **RG3:** K1 from ns3.PK1 = {1/2,1/2}/{1}; V_pair/V_sing/Acols match
    the committed d43c construction (read from source); all V-side
    records members of the census sets and strict-classified
    p/ko/kc/r/ka/v.arb; zero out-of-census forms.
12. **RG4 facts:** max realized |ckey| = 2; no mname inside any merge
    pair (nor any realized input slot — m-4); n records bare 2-tuples,
    regs {actor}, singleton fibers.
13. **M4 anchors:** 1/8, 1/16, 1/16; both-branch 1/4 with named-winner
    refusal; click canons distinct.
14. **d42b1 vs d42b2-embedded** on all fixture events: 63 agree / 2
    d42b1-crashes on click prefixes / **1 price divergence** (M-2).
15. **Plumbing:** rerun byte-identical to committed .out (unseeded,
    PYTHONHASHSEED 0 and 7, cwd = repo and `/`); scratch-relocated copy
    byte-identical (path-independence of the __file__ anchoring); 46
    PASS / 0 FAIL / 85 lines confirmed; ~1.4 s; no check(True); single
    crash-mode assert line 74.

## Mutation table (scratch copies only; committed files untouched)

| Mutant | Change | Gate that fires | Exit |
|---|---|---|---|
| MUT-A | `PREDS['d']` also matches 'm' (multi-match) | RG0 COMPLETE FAILs (multi>0); downstream RG1 crash after the gate (n-3) | 1 |
| MUT-B | 'kc' dropped from EVK (type dropped) | RG0a-iii + RG0b-ii + RG0 FAIL | 1 |
| MUT-C | LIT2599 4th decimal 8→9 (literal tilt) | RG2-0 FAIL, 45/1 | 1 |
| MUT-D | V maps records 0,1 to one cell (isometry entry broken) | all nine RG2-\* RECEPTION ISOMETRY FAIL | 1 |
| MUT-E | fake ninth kind `'q'` added to the scanned d42b2 head (scratch layer copy) | RG0a-i + RG0a-iii FAIL — the source scan is live, not a dressed-up list | 1 |
| MUT-F | `shadow_of` → constant `'X'` (imprint reader corrupted) | **none — 46/46 SILENT GREEN**; only unanchored prints drift (evidence for M-1) | 0 |

All four commissioned mutant classes die at the right gates; MUT-F is
the referee's additional diagnostic and is graded MAJOR (not BLOCKER)
because the byte-diff-vs-committed-.out convention exposes the drift.

## Reproduction appendix

```
cd /Users/felixrobles/workspace/isp
python3 v10/code/d44e_reception_census_exact.py          # 46/46, exit 0
PYTHONHASHSEED=0 python3 v10/code/d44e_reception_census_exact.py  # byte-identical
PYTHONHASHSEED=7 python3 v10/code/d44e_reception_census_exact.py  # byte-identical
(cd / && python3 /Users/felixrobles/workspace/isp/v10/code/d44e_reception_census_exact.py)  # cwd-robust
```
Referee artifacts (scratchpad, session-local):
`scratchpad/d44e/referee_verify.py` (32 checks; AST scan, strict
classifier, censuses, collisions, findings, RG3, anchors);
`scratchpad/d44e/mut/` (receipt + both layer copies; baseline
byte-identical; mutA–mutF as in the table; layer restored and re-run
green after MUT-E). Key one-off probes reproduced in-line above:
alien-tag admission `('z','A',CK,{tA})` → (True, 1/8) in both layers;
`admissible_arb_ckeys(D2H,'B')` = {{t1A,t1B},{t1B}} ⇒ terminal-d42b1
merge price 1/24 vs embedded 1/16; d42b1-vs-d42b2 function-text diff
(regs_of/View/own_view/admissible differ; d-branch identical).

## Disposition

The census itself — the deliverable — is real, exact, and fully
reproduced: this referee found no false number anywhere in the .out,
the note, or LOG #359's quantitative claims. REVISE is carried by
prose-and-anchoring repairs: forward-correct A5 (M-2), scope the R6
discharge and "no shared-form shortcut" to the copy-form template
actually gated (M-1), anchor the print-carried per-type structure
(M-1/m-1), and route the d42b1/d42b2 transport-pricing divergence to
the board as a named corpus-level carried question. With those applied,
the unit is PASS-grade at its pinned scope.
