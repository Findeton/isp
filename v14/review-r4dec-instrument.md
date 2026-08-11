# PAPER-21 (THE R = 4 ARENA) — K3 INSTRUMENT REVIEW

**Seat:** K3 INSTRUMENT, panel protocol v14 ledger #203.
**Object at f45b3a1:** `v14/paper-21-r4dec.md` `f54dad8d51b8`;
`v14/code/r4dec_exact.py` `e387674bfcdd`; `v14/code/r4dec_output.txt`
`27ed73ded234`; `v14/code/r4dec_receipt.json` `e1f148dd6a0e`; pin
`v14/note-r4dec-pin.md` `f50630ced3be`. **All five verified at the start and
at the end of this review; unchanged.** The three untracked siblings
(`v14/code/perl_exact.py`, `v14/code/smu_exact.py`, `v14/paper-28-perl.md`)
belong to other units in flight and are disclaimed.

**Grade: ACCEPT-WITH-FIXES (AWF).**

**Executions: 165 instrument invocations** — 2 off-tree delivery runs at two
`PYTHONHASHSEED` values; 27 hostile argv forms; 3 registry listings; 1
`--selftest`; 36 `--break-anchor` (18 names × 2 passes, the first pass voided by
my own shell bug, §7); 2 bare-copy; 8 CLI `--mutant` runs; 50 in-process mutant
runs; 12 + 9 in-process `full_run` invocations driving the two paper-injection
batteries; 7 in-process `full_run` invocations driving the shadow mutants; 1
driver session of 372 schedule drives; plus 13 direct evaluations of the #125
needle matcher. **Seven independent reviewer programs** written from scratch in
`…/scratchpad/r4d-in/` (`probe_equality`, `sweep50`, `seal_audit`, `anchors`,
`clean`, `e24`, `inject`/`inject2`/`shadow`).

**Recomputations: 653, mismatches against a delivered number: 0.** By source:
48 combinatorial columns rebuilt clean-room; 372 driven-vs-combinatorial field
comparisons outside the window; 63 anchor checks (21 matches + 21 perturbations
+ 21 consumer bindings); 56 seal recomputations and corruption probes; 50 mutant
outcomes recomputed and diffed against the delivered sweep; 49 coverage /
allow-list measurements; 9 window-arithmetic identities; 6 E-24 measure counts.

**Headline:** nothing this unit measured is wrong. Every combinatorial column
reproduces exactly under a clean-room rebuild that shares no code with the
instrument — including the 100,080, recounted by meet-in-the-middle instead of
branch-and-bound. The W4 window license is *under*-claimed, not over-claimed:
it generalises to 372 schedules the window never touched. The seal, the
provenance, the CLI and the mutant sweep are all sound at the era's standard.
**The defects are entirely on the paper-facing perimeter and in two false
sentences.** Of nineteen corruptions of the paper executed against the delivered
instrument, **eleven pass at exit 0** — including a headline-reversing forgery of
the verdict block a reader will quote — seven die at a named gate, and one is
withdrawn as mis-built by me.

---

## 1. ROW 1 — THE W4 WINDOW LICENSE

### 1.1 What the equality gate actually compares

`G-DRIVEN-EQUALS-COMBINATORIAL` (source L1735–L1746) does exactly this, for
each of the 600 driven window records:

```
driven_f = link_field_of(rec["footprints"])      # from the layer's own regs_of
comb     = unpack_field(packed_of_schedule(sch)) # from the groupings alone
any(driven_f[c] != comb[c] for c in CELLS)
```

- **The object compared** is the induced 27-cell link field, and nothing else:
  not the event list, not the initiators, not the event order, not the
  footprints as sets.
- **The alphabet** is `CELLS = SITES × I7_LINKS` — the nine sites and the
  **three declared** directions `(1,0), (0,1), (1,1)`. Values live in 0..4
  (four bits per cell, and four rounds cannot overflow a nibble — verified).
- **The blind spot, named:** AG(2,3)'s fourth parallel class `(1,2)` is
  invisible to *both* sides. A driven/combinatorial divergence confined to the
  undeclared direction cannot be seen by this gate. It is seen elsewhere — the
  R4-ONE-ANT control counts its 9 foreign pairs and dies STRUCT-DEAD — but that
  is a different gate on a different object, and §2.3's sentence should not be
  read as covering it.

The gate is a per-object predicate over 600 × 27 = 16,200 cells, not an
aggregate. **#87-compliant.**

### 1.2 Could a divergence OUTSIDE the 600 hide? Measured: no.

I drove schedules the window never contains and compared the two routes myself
(`probe_equality.py`, seed 20260811):

| probe | drives | mismatches | maxhits values |
|---|---|---|---|
| uniformly random grouping quadruples + random seedings, **all outside W4 and outside its 520 grouping quadruples** | **300** | **0** | {1} |
| the 276 G-FLAT quadruples at **non-canonical** seed transversals (every 23rd quadruple × 6 random seedings) | **72** | **0** | {1} |

The 72 non-canonical-seed drives produced **exactly one distinct driven link
field**, equal to I7's committed G-FLAT row. This is stronger than what the
paper claims:

- **Deviation 1** (the window) — the equality holds on 372 further records the
  window does not contain.
- **Deviation 2** (one canonical transversal per round) — the paper says the
  seed-axis invariance is "measured on the fan rather than assumed", i.e. at one
  grouping quadruple. It in fact holds at 12 further grouping quadruples with
  randomly chosen non-canonical seeds.
- The **maxhits == 1 immunity** the v10-layer tie-break addendum (v14 #160)
  demands is not merely stated: it held at all 372 out-of-window drives too.

The mechanism is structural and the unit names it (§3.5): at this generator a
division event's footprint **is** its conflict group, so the driven field is a
function of the groupings alone. I could construct no counterexample.

### 1.3 Does every column claimed exhaustive rest on the theorem, or on the window?

I audited this column by column.

| column | rests on | verdict |
|---|---|---|
| 276 of 1,679,616 = 276 of 6,146,560,000; 12 multisets; 11 non-collinear | **the budget theorem** — and additionally **all 276 are inside the window and driven** | exhaustive on BOTH readings |
| 100,080 cover = posdef = I7-STRICT; 20,988/79,092; det spectrum; 900,720 cells | enumeration of an exhaustively defined finite set | exhaustive; the window caps nothing |
| 54 / 105 reachable site codes; the 3 breaking codes; 0 occurrences | enumeration | exhaustive |
| back-validation 72 of 21,952,000; 252 / 747 of 78,400 | enumeration | exhaustive |
| FORCED 600 of 600; the record-length spectrum; the 356-schedule arena identity; fibers 36/3/1; base-map spreads | **the window** | window-bound, and **disclosed** in the head (`@WINDOW-600-OF-3,266,533,992,960,000`) and in Deviation 1 |

**No column claimed exhaustive rests on the window.** The budget theorem is a
theorem and I verified it as one: (i) the per-round incidence ceiling is 9,
measured exhaustively over all 280 partitions (spectrum 1@0, 27@4, 54@6, 162@7,
36@9 — recomputed clean-room, sums to 280); (ii) I7's G-FLAT needs
(1+1+2)×9 = 36 incidences in total; (iii) 4 × 9 = 36, so equality forces every
round to saturate; (iv) therefore a G-FLAT-inducing quadruple can only be a
quadruple of saturating partitions, and 36⁴ = 1,679,616 is exhaustive over
280⁴ = 6,146,560,000 for this predicate. Sound.

**MINOR-10 (one sentence).** §2.3 attributes the license in the wrong
direction: "Every other column below is exhaustive over an object the window
does not cap … **What licenses that is the same equality** paper-19 used." The
exhaustive columns are exhaustive because they *enumerate*; the equality
licenses reading a combinatorial column as a statement about **driven** records.
Repair: "…the window does not cap. The equality below is what lets those
combinatorial columns be read as statements about driven records."

---

## 2. ROW 2 — THE 50-MUTANT SWEEP OUTSIDE THE HARNESS, AND E-23

### 2.1 The sweep

Driven by me, in a third off-tree mirror, with the four repo artifacts hashed
before and after every single mutant (`sweep50.py`; 8 of the 50 additionally
run as separate `--mutant NAME` CLI processes before I converged for time under
a machine load average of 140).

```
sweep rows 50; killed 50; on target 50; artifacts unchanged 50
survivors: none        off-target: none
disagreements with the DELIVERED receipt's own 50 sweep rows: none
```

The delivery run's `G-MUTANTS-ON-TARGET` and `G-SWEEP-BOUND` rows are therefore
**earned, not asserted**. `--mutant` writes nothing in every case. The raising
gate parses: `--list-mutants` prints 50 rows = `MUTANTS` = `receipt.mutants` =
`receipt.mutant_sweep` = `receipt.reachability`; `--list-gates` prints 60 rows =
`GATE_REGISTRY` = `coverage.gates_evaluated`, with `registry_drift` measured
empty. 48 gates carry a mutant, 12 carry a waiver, 0 uncovered.

### 2.2 MAJOR-4 (E-23) — seven of the fifty falsifiers are synthetic, and their published descriptions invert their code

Seven mutants do not corrupt any measured value. They append a constant `False`
to the gate's conjunction via `pick("MUT-X", True, False)`:

| mutant | gate | the gate's REAL conjuncts, which no mutant touches |
|---|---|---|
| `MUT-DRIVER-ANCHOR` | G-DRIVER-ANCHOR | `same_events`, `committed_row == grid34` |
| `MUT-MEMO` | G-MENU-PURE | `all(memo_rows)` |
| `MUT-WINDOW` | G-WINDOW-DISCLOSED | `flat_groupings <= wgroupings`, `len(W)==len(set(W))` |
| `MUT-DECLARED` | G-DECLARED-RECORD | `hits == ["G-FLAT"]` |
| `MUT-RSQ` | G-RSQ-THEOREM | `not linkconst`, `boxconst`, `fib1==1`, `fib>1` |
| `MUT-HOLE` | G-KERNEL-HOLE | `in_hole == 27`, `"G-FLAT" in unrefinable` |
| `MUT-HEAD` | G-VERDICT-RECONSTRUCTED | `rebuilt == R["verdict"]["segments"]` |

Two consequences, and E-23 names both:

1. **The falsifier cannot fail.** A constant-`False` conjunct is killed by
   construction; it demonstrates that the conjunct is in the expression and
   nothing else. The gate's actual discrimination is untested by its own
   declared falsifier.
2. **The published description is inverted.** All seven descriptions state a
   *false-positive* corruption — "declares the generalized driver anchored when
   it is not", "declares the memo gated without re-driving anything", "declares
   the window to contain the primary object without checking", "declares the
   induced record one of the eleven without comparing orbits", "declares the
   standard-versus-list theorem without its two measurements", "declares the
   kernel hole without counting the record's own intervals", "declares the head
   reconstructed without comparing the strings". A mutant that made a gate
   *pass* would SURVIVE, which is the failure outcome. The code performs the
   opposite corruption. E-23: "a description-inverted mutant is a false waiver
   wearing a green badge", and "a falsifier's published description is part of
   the sealed surface" — these seven descriptions are sealed under
   `SEAL-MUTANTS`.

**The gates themselves are alive.** I built shadow mutants that corrupt the
*object* rather than the boolean and confirmed each fires:

| shadow | what it corrupts (the object, not the boolean) | outcome |
|---|---|---|
| S1 | `read_d66_row`'s parsed committed row, +1 on each field | **DIED at G-DRIVER-ANCHOR** |
| S2 | the no-cache builder's record, truncated by one event | **DIED at G-MENU-PURE** |
| S3 | one W4-FLAT quadruple dropped from `window_schedules` | **DIED at G-WINDOW-DISCLOSED** |
| S4 | `chart_orbit` perturbed so no declared record is hit | **DIED at G-DECLARED-RECORD** |
| S7 | the comparator's own output, one character appended | **DIED at G-VERDICT-RECONSTRUCTED** |

with a pristine control before (`clean`) and a pristine post-check after
(`clean`), so the patches were fully undone. **Five for five.** So this is an
honesty defect in the sealed falsifier surface, not a hole in the gate wall —
which is exactly what E-23 is about. (The remaining two, `MUT-RSQ` and
`MUT-HOLE`, guard conjunctions whose inputs are read straight from I7's and
R6b′'s pinned receipts; corrupting them means corrupting a pinned source, which
dies at G-PROVENANCE first — so their gates are source-forced even though their
declared falsifiers are not.)

**Repair R-K3-4 (liftable, seven small edits).** Replace each constant with a
corruption of the object and rewrite the description to match:
`MUT-DRIVER-ANCHOR` → perturb `read_d66_row`'s parsed row; `MUT-MEMO` → truncate
the no-cache builder's record; `MUT-WINDOW` → drop one W4-FLAT quadruple from
`window_schedules`; `MUT-DECLARED` → perturb `chart_orbit`; `MUT-RSQ` → flip one
entry of `linkconst`; `MUT-HOLE` → move one interval out of the hole;
`MUT-HEAD` → perturb one character of the comparator's own output.

### 2.3 The twelve waivers, audited one by one

| waiver | class | forcing sound? |
|---|---|---|
| G-PROVENANCE | FALSIFIED-BY-A-FLAG | **yes** — I ran all 18 `--break-anchor` names: 18/18 exit 1 at G-PROVENANCE, artifacts unchanged |
| G-READS-DECLARED | STRUCTURAL | **NO — see MINOR-1** |
| G-EXACT-ARITHMETIC | SELF-SCANNING | yes (the gate parses this file; scope is this file, and the receipt type-scan covers the output) |
| G-NO-SUBPROCESS | SELF-SCANNING | yes, at the declared scope (this file's imports) |
| G-SLICE-EXIT-FREE | SOURCE-FORCED | yes — the property is read off pinned bytes; corrupting it dies at G-PROVENANCE, which I confirmed for A-D42B1 |
| G-I7-READOUT | READ-ANCHORED | yes — MUT-ANCHORS falsifies the same anchor class, and `detM` is a genuine recomputation |
| G-COVERAGE | SELF-REFERENTIAL | yes |
| G-REACHABILITY | SELF-REFERENTIAL | yes |
| G-MUTANTS-ON-TARGET | SELF-REFERENTIAL | yes |
| G-ARTIFACT-INTEGRITY | EXERCISED-IN-RUN | yes — the corrupted probe is built and shown detected before the real comparison (`probe_caught` in the evidence) |
| G-SWEEP-BOUND | DELIVERY-ONLY | yes — `sweep_ok = (not swept) or …`, and the same conjunction is re-taken at G-ARTIFACT-INTEGRITY |
| G-PAPER-COVERAGE-FINAL | AGGREGATE | yes |

**MINOR-1 — G-READS-DECLARED's forcing is not sound, and its statement is
false.** The forcing reads "the read list is appended by the only reader in the
file; a mutant could only add a read the gate would then catch." There are two
readers. `read_bytes` appends to `READS`; **`read_text` does not**, and
`read_text` is what opens the paper under test (`main`, `--verify-paper`) and
the module itself (`read_text(SELF)`). So the run opens 20 files while the gate
sees 18, and the gate's own statement — "Nothing outside the %d pinned sources
is opened" — is literally false. The *substance* of #91 survives: both extra
reads are gate-consumed (the paper by the four paper gates, `SELF` by
G-EXACT-ARITHMETIC and G-NO-SUBPROCESS), and the module's docstring does
disclose the paper as a second category. But the forcing as written would not
catch a `read_text` of anything else. Repair: give `read_text` a category
argument, record all three categories (SOURCE / OBJECT-UNDER-TEST / SELF), and
gate each against its declared list.

---

## 3. ROW 3 — COVERAGE UNDER E-22, AND THE INJECTIONS

### 3.1 What the scanner does, measured

| property | measured |
|---|---|
| numerals scanned in the paper | **1,068** (I recount 1,068) |
| of which inside fenced blocks | **296** (I recount 296) |
| fenced blocks | **8** — four distinct verdict segments, **each appearing exactly twice** (head §0 and §9) |
| inline code spans outside fences | **51**, carrying **31** numerals |
| unbacked numerals | **0** |
| allow-list size | **200** |

**E-22's inline-span half is satisfied, and the code says why.** The scanner's
body is `text` — the whole paper, nothing stripped — with an explicit comment
naming the defect this era fixed. Backticked numerals *are* scanned. Confirmed
by measurement, not by reading: the 31 in-span numerals appear in the scan
count.

**E-22's blocks-by-multiset half is NOT implemented**, and the paper is in
exactly the configuration E-22 was bought on.

### 3.2 The injections

Nineteen corruptions executed across two rounds, each run exactly as
`--verify-paper PATH` runs it (`full_run(paper_text=…)` then
`finish(write=False)`), against a pristine control that returns exit 0 with
1,068 / 296 / 8 / 0. **Eleven survive at exit 0, seven die at a named gate, one
(INJ-18) is withdrawn as mis-built by me.**

| # | injection | outcome | ruling |
|---|---|---|---|
| INJ-01b | UNBACKED numeral `4242` inside an **inline code span** | **DIED at G-PAPER-COVERAGE** | control for the scanner — E-22's inline-span half is live |
| INJ-02 | `[[1, 0], [0, 1]]` → `[[1, 1], [1, 1]]` inside the §3.3 inline span (backed numerals only) | **SURVIVED, exit 0** | MAJOR-2 / MAJOR-5 |
| INJ-03 | **duplicate-and-corrupt**: forge the **§9 copy** of the weld fence — `FIBERS=36/3/1` → `1/1/1`, `2-FREE-ITEMS=UNMOTIVATED` → `0-FREE-ITEMS=MOTIVATED` | **SURVIVED, exit 0** | **MAJOR-1** |
| INJ-04 | forge the **head copy** of the same fence instead | **SURVIVED, exit 0** | **MAJOR-1** |
| INJ-05 | §4.5 weld-fiber **table row swap** (`I-SITE-ASSIGNMENT` 36↔`I-ORIENT` 1) | **SURVIVED, exit 0** | **MAJOR-2** |
| INJ-06 | §6.1 price **table** denominator 6,146,560,000 → 21,952,000 | **SURVIVED, exit 0** | **MAJOR-2** |
| INJ-07 | §4.4 census **table** fate R4-FLAT UNMOTIVATED → FOUND at both readings | **SURVIVED, exit 0** | **MAJOR-2** |
| INJ-08 | §6.3 homogeneous-record **table**, G-FLAT 276 → 20,160 | **SURVIVED, exit 0** | **MAJOR-2** |
| INJ-09 | prose "**12** grouping multisets" → "**13**" (contradicting its own head's `12 MULTISETS`) | **SURVIVED, exit 0** | **MAJOR-3** |
| INJ-10 | **delete** the §9 copy of the price fence | **SURVIVED, exit 0** | MAJOR-1 |
| INJ-11 | **append a forged third copy** of the split fence claiming `SPLIT FIBER 1 AT 27 OF 27 INTERVALS` | **SURVIVED, exit 0** | **MAJOR-1** |
| INJ-12 | the Lorentz naming sentence inverted ("it **is** a signature… **is** a metric on any continuum") | **DIED at G-WALL-LORENTZ-NAMED** | wall holds |
| INJ-09b | UNBACKED numeral in plain prose | **DIED at G-PAPER-COVERAGE** | control |
| INJ-13 | UNBACKED numeral in a **table cell** | **DIED at G-PAPER-COVERAGE** | control — tables *are* scanned for numerals |
| INJ-14 | UNBACKED numeral in **both** fenced copies | **DIED at G-PAPER-COVERAGE** | control |
| INJ-15 | **both** copies of the weld fence forged, backed numerals only | **DIED at G-PAPER-HEAD-VERBATIM** | **the gate is alive** — it is the two-copy containment that defeats it |
| INJ-16 | the head's four fenced blocks **deleted entirely** | **SURVIVED, exit 0** | **MAJOR-1** — a paper with no verdict block at the top passes |
| INJ-17 | a **rendered claim** sentence corrupted (18 → 12 in the splittable claim) | **DIED at G-PAPER-CLAIMS** | control — the 15 rendered claims are live |
| INJ-18 | the retracted L-1 sentence, mid-word-wrapped + blockquoted | **SURVIVED — but the injection was MIS-BUILT by me; see §3.7** | not a finding |

### 3.3 MAJOR-1 — the fenced-block gate is containment, and every fence is carried twice

```python
headok = all(canon(seg) in canon(ptext) for seg in R["verdict"]["segments"])
```

E-22, verbatim: *"Fenced blocks are gated by MULTISET EQUALITY, not containment
— the object carried two copies of its verdict fence and the clean copy
satisfied a containment gate while its twin was forged."* This paper carries
**two copies of each of its four verdict fences**. Forging either copy leaves
the other to satisfy containment (INJ-03, INJ-04). Deleting one leaves the other
(INJ-10). *Adding* a forged third copy is not even looked at (INJ-11). The
forged text in INJ-03 reverses the unit's own second headline from
UNMOTIVATED-at-the-free-assignment to MOTIVATED with zero free items — the
sentence the effectus seat is adjudicating — and the delivered instrument
returns exit 0 with 0 unbacked numerals.

The two supporting predicates in `G-PAPER-COVERAGE` are cardinalities, not
per-object predicates: `cov["fenced_blocks_scanned"] >= len(segments)` (8 ≥ 4)
and `cov["fenced_numerals_scanned"] > 0`. **#87** says gates bind objects, not
counts.

**Repair R-K3-1 (liftable).** Declare the copy multiplicity and gate the
multiset:

```python
FENCE_COPIES = 2            # head and section 9, declared
want = Counter({canon(seg): FENCE_COPIES for seg in R["verdict"]["segments"]})
got  = Counter(canon(b) for b in FENCE.findall(ptext))
headok = (got == want)
```

and add `MUT-PAPER-FENCE-MULTISET`, which forges one of the copies, targeting
`G-PAPER-HEAD-VERBATIM`. This kills INJ-03, INJ-04, INJ-10 and INJ-11 at one
gate.

### 3.4 MAJOR-2 — tables are not claims

E-22, verbatim: *"Tables render as claims."* The unit renders **15** prose
claims from the receipt (`paper_claims`) and **0** table rows. Five distinct
table forgeries survive at exit 0 (INJ-05 through INJ-08 and INJ-02), including
the §4.4 census table asserting the weld FOUND where the run measured
UNMOTIVATED, and the §4.5 fiber table asserting a site-assignment fiber of 1
where the run measured 36. In each case the prose claim elsewhere in the section
still matches, so `G-PAPER-CLAIMS` is silent; every numeral involved is
receipt-backed, so `G-PAPER-COVERAGE` is silent; the fenced heads are untouched,
so `G-PAPER-HEAD-VERBATIM` is silent.

**Repair R-K3-2 (liftable).** Render the six published tables row by row from
the receipt and match each row with `match_needle` — §3.3 (unit-grade), §3.4
(fates), §4.4 (the twelve census cells with their reading stamps), §4.5 (the
three fibers at both arenas), §5.1 (the split table), §6.1 (the price sequence)
and §6.3 (the four homogeneous records). Add `MUT-PAPER-TABLE`.

### 3.5 MAJOR-3 — the coverage gate's own statement is false: there is a third, hand-typed allow list

The sealed gate statement says every numeral is *"allow-listed **only** against
the receipt's own registered numbers and this run's own verdict strings."* The
code unions in a **42-element hand-typed literal tuple**. I measured what it
does:

- **11 of the 42 are dead** — they never occur in the paper at all (`-1/2`,
  `2,2,4`, `1,1,4`, `08`, `3.13`, `125`, `20`, `91`, `119`, `148`, `46`, `87`,
  `34`; the comma/decimal splitting in `NUMTOK` makes several unreachable by
  construction).
- **7 fire and are backed by nothing else**, covering 13 numeral occurrences:
  `1/2` (×2), `21` (×2), `15` (×1), `1,1,2` (×1), `1,1,1` (×3), `2,3` (×3),
  `82` (×1). The comment justifies two classes (AG(2,3)'s name; RUNBOOK
  engraving numbers) but the sealed statement does not mention the list at all.
- The consequence is measured: **INJ-09** changes §3.2's "**12** grouping
  multisets" to "**13**" — directly contradicting the paper's own head, which
  reads `12 MULTISETS, 11 NON-COLLINEAR` — and survives at exit 0 **because
  `13` is on the hand list**.

For calibration I measured the allow list's discrimination: it accepts 10/10
one-digit numerals, 44/90 two-digit, 31/900 three-digit, 10/9,000 four-digit,
18/90,000 five-digit. The gate is strong exactly where the unit's big numbers
live and weak on small ones — which is inherent, and worth stating in the paper
rather than leaving to a reader.

**Repair R-K3-3 (liftable).** Publish the exemption list as a receipt key with
a per-literal reason; gate that (i) every exemption FIRES (a dead exemption is
rejected), (ii) no exemption is a numeral the receipt could have supplied, and
(iii) the gate statement names all three lists.

**The separation is clean and worth stating precisely.** `G-PAPER-HEAD-VERBATIM`
is *not* dead: forging **both** copies kills it (INJ-15). Forging **either one**
does not (INJ-03, INJ-04). Deleting one does not (INJ-10, INJ-16 — and INJ-16
removes all four head blocks). Appending a forged copy does not (INJ-11). This is
E-22's diagnosis reproduced verbatim on a second object.

### 3.6 MINOR-2 — spelled-out numerals are unscanned

`NUMTOK = \d[\d,]*(?:/\d+)?` requires a leading digit. The paper carries **173**
spelled-out number-words (one ×79, three ×23, two ×20, four ×13, nine ×13,
twelve ×7, eleven ×6, twice ×5, eight ×4, six, twenty, hundred), several
load-bearing: "**one** of I7's **eleven** declared records", "**nine** sites",
"twelve grouping multisets", "one hundred and twenty degrees". Under E-22's own
rationale — a backticked numeral is a claim like any other — a spelled-out one
is too. Repair: a word→value table in the scan, each word required backed or
whitelisted with a reason.

### 3.7 The #125 wall: I mis-built INJ-18, and the gate is sound

My INJ-18 wrapped the retracted L-1 sentence **mid-word** (`…and precise / ly
the form…`), which no author and no renderer produces; the injection survived
for that reason and is **withdrawn as a finding**. I then tested `match_needle`
against the banned sentence directly — the gate is literally
`hit = match_needle(ptext, BANNED_L1)` — over thirteen realistic evasions:

```
plain one line ............................ CAUGHT     bulleted + wrapped ......... CAUGHT
house-style wrap at a space (w=60) ........ CAUGHT     nested blockquote '> >' .... CAUGHT
house-style wrap at a space (w=40) ........ CAUGHT     curly apostrophe ........... CAUGHT
blockquoted + wrapped at a space .......... CAUGHT     **emphasised** ............. CAUGHT
numbered-list + wrapped ................... CAUGHT     inside a code fence ........ CAUGHT
double-spaced ............................. CAUGHT     inline `span` .............. CAUGHT
tab-separated ............................. CAUGHT
```

**13 of 13 caught**, including the exact house-style line-wrap that bought the
#125 engraving at U4. **#125: PASS.** The single residual is the mid-word break.
**MINOR-11**, one line: also compare a whitespace-stripped form of both sides.

---

## 4. ROW 4 — E-24, PER FRACTION CLASS

The paper stamps nothing `COUNTING-ONLY` and declares no measure. I classified
every X-of-Y form (50 occurrences, 24 distinct):

| class | instances | E-24 status |
|---|---|---|
| **exhaustive-census counts over an enumerated configuration space** — 276/1,679,616; 276/6,146,560,000; **100,080/6,146,560,000**; 72/21,952,000; 0/78,400; 252/78,400; 20,988/100,080 | 7 distinct | **COUNTING-ONLY in substance, unstamped in form.** Every one is the cardinality of a subset of a fully enumerated finite set; none is converted to a rate; no typicality claim rests on any of them |
| **per-object saturation tallies** — 27/27 cells, 9/9 sites, 9/27 and 0/27 intervals, 600/600 | 5 distinct | outside E-24's reach: these are per-object counts, not fractions over a configuration space |
| **the declared window** — 600 of 3,266,533,992,960,000; 520 of 6,146,560,000 | 2 | correctly handled: the head carries the scope and Deviation 1 prices it; never read as a coverage probability |
| **parent-owned** — 79/201 and 60 of R6b′'s censused intervals; 3 of 9 unrefinable; 0 of 9 link-constant | 4 | attributed to their sources; the one probability word in the paper ("the kernel assigns them probability zero") is R6b′'s own declared first-return law, correctly attributed |

**The 100,080/6,146,560,000 row specifically: counting-only.** §6.1 states it as
"100,080 of the 6,146,560,000 ordered grouping quadruples cover all 27 cells",
the head stamps it `EXHAUSTIVE`, and nothing downstream reads it as a
likelihood.

**The one measure-relative word in the paper is "mostly"** — §6.3 and §9: "R = 4
is the first budget whose covering class is **mostly** inhomogeneous"
(79,092 of 100,080). A majority claim over a configuration space is
measure-relative by E-24's definition. **I measured it under three invariant
measures on the same set:**

| measure on the covering class | homogeneous | inhomogeneous |
|---|---|---|
| uniform on **ordered grouping quadruples** (the paper's) | 20,988 (20.97%) | **79,092 (79.03%)** |
| uniform on **grouping multisets** (the quotient by round order) | 876 (20.92%) | **3,312 (79.08%)** of 4,188 |
| uniform on **distinct induced fields** | 4 (1.43%) | **276 (98.57%)** of 280 |

**The headline is measure-stable and, under two of the three measures, stronger
than published.** E-24 is satisfied in substance; only the stamp is missing.

**Birth-date ruling.** E-24 was engraved at v14 #192; this unit's pin was frozen
at #174 declaring "the full era per HANDOFF-PROMPT.md §4 (all 21 engravings)",
and the ledger records no mid-flight relay to the r4dec worker. **E-24 was not
binding at construction.** MINOR-7, liftable in one line: append
`(counting-only; no measure declared)` to the price row and to "mostly", or cite
the measurement above.

---

## 5. ROW 5 — ANCHORS, SEALS, POST-WRITE CORRUPTION

### 5.1 The 21 verbatim anchors, perturbed

Recomputed outside the instrument (`anchors.py`). For every anchor: does the
needle occur in the source it names; is it above the #62 floor; does an
eight-character perturbation break the match (i.e. is the match non-vacuous);
is its named consumer gate both **registered** and **actually evaluated**?

```
21 of 21 found in their named source
21 of 21 above the 30-character canonical floor (shortest 57, longest 200)
21 of 21 broken by an 8-character perturbation  -- no vacuous needle
21 of 21 consumers registered AND present in this run's evaluated ledger
defects: none
```

Needles per source: A-PIN 3, A-P19 4, A-P04 4, A-R3WEFF 2, A-HA 2, A-P09 2,
A-CAT 2, A-P06 1, A-L1 1. The nine sources with no verbatim anchor are the JSON
receipts and the three Python layers — read as *data* (parsed / AST-extracted),
where a prose needle is the wrong instrument; they are held by the provenance
sha and by the numeric anchors instead. Honest.

### 5.2 The 4 numeric anchors

`N-I7-BOX` (361, recomputed 361) and `N-READOUT-DET` (2, recomputed 2 from a
typed 3×3 matrix) are recomputed in-run. `N-P19-R4-REGISTER` (276) and
`N-D66-GRID34` ([66, 12, 18]) publish `computed: null` and are **carried as the
committed side of a later gate** — G-276 and G-DRIVER-ANCHOR respectively. I
confirmed both are genuinely consumed there. The gate statement says exactly
this ("either RECOMPUTED here or carried as the committed side of a later
gate"), so there is no false claim. `MUT-ANCHORS` falsifies the recomputed
class; `--break-anchor` covers the read side for all 18 sources.

### 5.3 The 27 seals, the manifest, and post-write corruption

Recomputed from the **delivered bytes**, outside the instrument
(`seal_audit.py`):

```
seal rows 27 = declared_seals 27
27 of 27 seal digests recompute exactly from the delivered receipt
receipt keys 31; covered by a seal or DECLARED-UNSEALED 31; uncovered: none
payload_sha256_12 published 366620c0fe4f, recomputed 366620c0fe4f  -> MATCH
post-write corruption of one leaf under each sealed key: 27 of 27 CAUGHT
```

The four `DECLARED-UNSEALED` keys are `arithmetic`, `python`, `seal_manifest`,
`payload_sha256_12`: none carries a measurement, the list is frozen by content
**and** by length, and `unsealed_clean` is machine-checked against
`SEALED_PATHS ∪ MEASURED_KEYS`. The manifest-vs-declared-set comparison is the
#148 form, not the weaker seals-that-happened-to-be-taken form. The write is
staged and `os.replace`d only after `G-ARTIFACT-INTEGRITY` passes, and the
corrupted probe is exercised before the real comparison. **#119 + totality +
vouching: PASS, at the strongest form in the corpus.**

Two small notes. **MINOR-4:** `--selftest` proves "artifacts unchanged" by
`(path, exists, st_mtime)` rather than by digest — weaker than the #119 standard
it sits beside. I verified the bytes independently and they are unchanged;
repair is a two-line switch to sha256. **MINOR-5:** a delivery run that fails
`G-ARTIFACT-INTEGRITY` leaves `r4dec_receipt.json.tmp` and `r4dec_output.txt.tmp`
behind; the delivered artifacts are untouched, as the gate statement says, but
the staged files are not removed.

---

## 6. ROW 6 — THE SEAL-VS-VOUCHING PERIMETER

The seal protects the **receipt's own bytes** and, per #148 and the U4b
vouching lesson, it protects the vouching layer too: `schema`, `provenance`,
`paper_claims`, `paper_coverage`, `polarity`, `coverage`, `reachability`,
`waiver_ledger`, `mutants`, `mutant_sweep`, `gates`, `closing_gates`, `totals`
and `transcript_head` are all sealed. That is the strongest perimeter this
corpus has built and it holds under every corruption I could construct.

**The paper is on the other side of it.** The seal cannot see the paper; only
the four paper gates can, and §3 shows eight of twelve corruptions walk past
them. So the honest statement of the perimeter is: **the receipt is sealed; the
paper is *vouched*, and the vouching is 15 prose claims + 4 fenced segments
matched by containment + an allow-list numeral scan + 5 polarity probes.**
MAJOR-1/2/3 are all failures of the vouching side, not of the seal.

One more asymmetry worth a row. The seal's own root is inside the artifact:
`seal_manifest` and `payload_sha256_12` are both DECLARED-UNSEALED, necessarily.
The receipt therefore authenticates only against the **external** pin — the
ledger's `e1f148dd6a0e`, which I verified. That is the corpus's standing answer
and it is fine, but the paper's §11 sentence "the terminal integrity gate
compares the bytes on disk against the gate-time seal" should not be read as
self-authentication after the process exits.

---

## 7. ROW 7 — THE CLI

`parse_args` read in source first (L3759), never from the docstring.

**27 hostile argv forms, all exit 2, all artifacts unchanged:**

`--bogus` · `-h` · `--help` · `""` · `--no-write --numbers` ·
`--numbers --no-write` · `--list-gates --list-mutants` · `--mutant` (missing
NAME) · `--mutant NOPE` · `--mutant MUT-276 --no-write` · `--break-anchor`
(missing NAME) · `--break-anchor NOPE` · `--break-anchor A-PIN extra` ·
`--verify-paper /nonexistent/x.md` · `--verify-paper v14` (**a directory**) ·
`--selftest --selftest` · **trailing arity on every mode flag** (`--list-gates
trailing`, `--list-mutants trailing`, `--numbers trailing`, `--no-write
trailing`, `--selftest trailing`) · `--mutant MUT-276 MUT-276` ·
`--verify-paper --numbers` · `--VERIFY-PAPER` (case) · `---no-write` ·
`"--no-write "` (trailing space) · `--no-write=1`.

**Exit-code semantics:** `--selftest` → exit 1, dies at G-PROVENANCE, artifacts
byte-unchanged (verified by sha, not by the gate's own mtime check).
`--break-anchor <each of the 18>` → exit 1 at G-PROVENANCE, artifacts unchanged,
18 for 18. `--mutant <each of 50>` → exit 1, artifacts unchanged, 50 for 50.
`--list-gates` → 60 rows, exit 0. `--list-mutants` → 50 rows, exit 0.

*(A note against myself: my first `--break-anchor` battery reported rc=0 for all
18. That was my own shell bug — `$?` after a pipe captures `tail`. Re-run
without the pipe: 18/18 rc=1. Recorded because a reviewer's own instrument is
part of the review.)*

**#24 / registry consistency:** `--list-gates` (60) = `GATE_REGISTRY` (60) =
`coverage.gates_evaluated` (60) with `registry_drift` measured empty;
`--list-mutants` (50) = `MUTANTS` = `receipt.mutants` = `receipt.mutant_sweep` =
`receipt.reachability` (50 each). **MINOR-6:** `totals.gates` publishes **57**
while `receipt.gates` holds **58** rows and coverage counts **60** — three
correct numbers at three different snapshot instants, of which
`closing_gates.warrant` explains only the 58-vs-60 step. Repair: name the
snapshot instant in `totals`.

---

## 8. ROW 8 — BYTE REPRODUCTION AND BARE-COPY DEATH

Two mirrors provisioned off-tree from the pinned bytes, **with no `.git`
anywhere**, holding exactly the 18 sources + the paper + the instrument:

| run | artifacts |
|---|---|
| `PYTHONHASHSEED=1234` | `r4dec_output.txt` **27ed73ded234** · `r4dec_receipt.json` **e1f148dd6a0e** |
| `PYTHONHASHSEED=0` | `r4dec_output.txt` **27ed73ded234** · `r4dec_receipt.json` **e1f148dd6a0e** |
| committed | `27ed73ded234` · `e1f148dd6a0e` |

**Byte-identical, twice, across two hash seeds, off-tree and git-less.** Payload
`366620c0fe4f`, 60 gates, 50 mutants in both. The v10-layer tie-break exposure
(#160) is real — d60's `pick` breaks ties with `sorted(key=repr)` over a
frozenset — and the unit's immunity is *measured*: every window schedule is
fully specified so `maxhits == 1`, the branching control deliberately stops
after one under-specified pick and reports only the count, and §3.4 states the
reason. I extended the check: 372 further drives, all `maxhits == 1`.

**Bare copy** (the instrument alone, no sources, no git): dies at the first read
with `FileNotFoundError`, exit 1, **writes nothing** — the directory still
contains exactly one file afterwards. `--list-gates` still works, correctly (it
reads nothing). **MINOR-9, cosmetic:** the death is an uncaught traceback rather
than a gate failure or a clean `[CLI]` message.

---

## 9. ROW 9 — THE FULL NUMERAL SWEEP, AND THE CHECKER ITSELF

**Recount, outside the instrument:** 1,068 numerals in the paper, 296 of them
inside the 8 fenced blocks, 51 inline spans outside fences carrying 31
numerals, 0 unbacked. **The delivered figures reproduce exactly.**

**The checker itself, audited per E-22's inline-span rule:** the scan body is
the unmodified paper — no fence stripping, no span stripping — and
`MUT-COVERAGE-SCAN` falsifies exactly the fence-stripping regression, on target.
That half is sound. The three defects are §3.5 (the undeclared third allow
list), §3.6 (digit-only tokenisation) and the fact that coverage is an
*allow-list* gate and not a *position* gate: a numeral that appears anywhere in
the receipt may appear anywhere in the paper. That is #20's design, not a
defect, but it is the reason MAJOR-1/2 matter — coverage cannot be the backstop
for a forged table or a forged fence, so those need their own gates.

### 9.1 Clean-room recomputation of every combinatorial column

Written from scratch (`clean.py`), sharing no code with the instrument: its own
grid, its own partition generator, its own link field, and — for stage 4 — a
**meet-in-the-middle over 39,340 distinct pair fields** instead of the unit's
branch-and-bound.

| delivered | recomputed | |
|---|---|---|
| partitions per round 280; closed form 280 | 280 / 280 | ✓ |
| incidence spectrum 1@0, 27@4, 54@6, 162@7, 36@9; max 9; 36 saturating | identical | ✓ |
| 36⁴ = 1,679,616; 280⁴ = 6,146,560,000; (280·27)⁴ = 3,266,533,992,960,000 | identical | ✓ |
| G-FLAT quadruples **276**; **12** multisets; orbit sizes 12(×1), 24(×11) | identical | ✓ |
| **COVER-27 = POSDEF-9 = I7-STRICT = 100,080** | 100,080 / 100,080 / 100,080 | ✓ |
| homogeneous 20,988 over 4 records — (1,1,1) 20,160, (1,1,2) 276, (1,2,1) 276, (2,1,1) 276; inhomogeneous 79,092 | identical | ✓ |
| determinant spectrum over 900,720 cells — 3/4 @437,184, 1 @386,640, 7/4 @76,896 | identical | ✓ |
| reachable site codes 54 (R=3) / 105 (R=4); breaking codes (1,1,4), (1,4,1), (4,1,1) | identical | ✓ |
| back-validation: R=3 I7-STRICT 72 of 21,952,000; R=2 ceiling 3 at 252, 747 non-degenerate of 78,400 | identical | ✓ |
| 276² = 76,176 concatenation witnesses | 76,176 | ✓ |

**Zero discrepancies.** The branch-and-bound's exhaustiveness is independently
confirmed by an algorithm that prunes nothing.

Window arithmetic also checks: 256 + 276 + 81 + 1 = 614, less 12 flat quadruples
already in the class stratum, less the committed R=4 point (a class quadruple),
less the seed fan's canonical member = **600**; distinct grouping quadruples
256 + 276 − 12 = **520**; driven G-FLAT schedules 276 + 81 − 1 = **356**; new
flat 264; new seedfan 80; class multisets C(7,4) = 35.

---

## 10. MAJOR-5 — THE COMPARATOR SHARES TYPED LITERALS WITH THE BUILDER

RUNBOOK §14: *"the comparator shares NOTHING with its builder — neither code,
nor inputs, nor typed literals; 'the same concatenation written twice' and 'the
same literal in both paths' are the measured failure modes (Γ-main's
G-VERDICT-EQUALITY; R4's MAJOR-6)."* This is inside the unit's own 21, and this
is its third recurrence.

The paper asserts (§11) and the sealed gate statement repeats: *"a comparator
that shares neither code nor input nor **typed literal** with the builder."*
Measured — `verdict_segments` and `reconstruct_from_serialized` type the same
constants in at least fourteen places:

`at 27 of 27 CELLS` · `at 9 of 9; POSDEF 9 of 9` · **`q=[[1, 0], [0, 1]]`** ·
`ONE-OF-I7'S-ELEVEN-DECLARED-RECORDS` · `AGAINST-INVARIANT-1/1/1-AT-R=3` ·
`d66'S-OWN-GRID(3,4)` · `ARITY-DEAD-AT-THE-DECLARED-8-ACTOR-PROBE` ·
`-OF-3-NON-EMPTY` · `FIBER 1|ORBITS 1|SIMPLEX-DIM 0=n-2|PINNED-TRANSITIVE` ·
`SUPPORT HOLE g(1)=g(2)=0` · `COVER-27 = POSDEF-9 = I7-STRICT` · `0 BREAKING` ·
`ALL AT det=0` · and the shared arithmetic offset `declared_family_size - 2`.

The comparator *is* genuinely independent in structure — %-formatting against
string concatenation, reading the serialized dict, and re-deriving the outcome
word from the fate rows with its own predicate chain plus a fate-multiset
cross-check. That part earns its keep. But for those fourteen fragments it
provides **zero** independent verification: whatever is typed wrong is typed
wrong twice and compares equal.

I then checked whether each shared fragment is nailed down elsewhere:

- `27 of 27` and `9 of 9` — **yes**, `G-UNIT-GRADE` binds `cells_at_target ==
  27`, `nposdef == 9` and `all(per_site[x] == FLAT)` per object.
- `0 BREAKING`, `ALL AT det=0` — **yes**, `G-SITEWISE-BREAK`.
- `ELEVEN` — **no**, but self-revealing: the same segment prints
  `declared_family_size - 2` = 9 from the receipt, so a change would show up as
  an inconsistency inside one string.
- **`q=[[1, 0], [0, 1]]` — NO.** The receipt publishes
  `i7.target_q = [["1","0"],["0","1"]]` and **no gate compares the head's
  literal against it.** The same matrix is typed a third time inside
  `LORENTZ_NAMED`, the mandatory naming sentence the wall gate matches into the
  paper. So the unit's most resonant object — the induced form the entire
  Lorentzian wall is written about — is a **typed string in three places and
  derived in none**. INJ-02 confirms the paper's own §3.3 table can carry a
  different matrix at exit 0.

**Repair R-K3-5 (liftable).** Derive `q` in the builder from
`R["i7"]["target_q"]` and in the comparator from the serialized receipt; build
`LORENTZ_NAMED` from the same value; replace `ELEVEN` with
`declared_family_size`, `-OF-3-` with the law count, `27 of 27` / `9 of 9` with
`len(CELLS)` / `len(SITES)`; then either delete the "nor typed literal" sentence
from §11 and from the gate statement, or make it true and *gate* it with an AST
scan for string constants shared between the two functions.

---

## 11. THE ERA-COMPLIANCE TABLE, PER ENGRAVING

| engraving | verdict | evidence / finding |
|---|---|---|
| **#82** CLI contract | **PASS** | 27/27 hostile argv → 2; real `--selftest` → 1 writing nothing; 50 named mutants on target; 18/18 `--break-anchor` |
| **#82** comparator independence (§14 clause) | **FAIL** | **MAJOR-5** — 14 shared typed literals; the "nor typed literal" sentence is false; `q` derived nowhere |
| **#87** gates bind objects, not cardinalities | **MOSTLY PASS** | unit-grade, forced, split-fiber, sitewise, equality all per object; two cardinality predicates in `G-PAPER-COVERAGE` (folded into R-K3-1) |
| **#91** no moving refs / off-tree / git-less | **PASS** | byte ×2 across two hash seeds, git-less; no subprocess; bare copy writes nothing |
| **#91** v10-layer tie-break (v14 #160) | **PASS, strengthened** | `maxhits == 1` stated as a gate *and* measured at 372 further out-of-window drives |
| **#119 + #148 totality + vouching** | **PASS (strongest form)** | 27/27 seals recompute from delivered bytes; 31/31 keys covered; payload sha reproduces; 27/27 corruptions caught; staged `os.replace`; probe exercised. **MINOR-4** (selftest mtime), **MINOR-5** (`.tmp` litter) |
| **#125** text gates as written | **PASS** | 13 of 13 realistic evasions of the banned L-1 sentence caught, incl. the house-style wrap that bought the engraving (§3.7); MINOR-11 residual |
| **#20** coverage incl. fenced blocks | **PARTIAL** | fences and inline spans *are* scanned (296 + 31) — credit; but **MAJOR-3** (undeclared third allow list), **MINOR-2** (digit-only) |
| **#34** honest denominators + reachability | **PARTIAL** | 0 uncovered, 0 registry drift, 50/50 reachable, 12 waivers audited — but **MAJOR-4** (7 synthetic falsifiers) and **MINOR-1** (one unsound forcing) |
| **§15** declared arena as data | **PASS** | arena declared in §2; window in the head; 14-item choice inventory with fibers; 7 deviations priced |
| **candidate readings** | **PASS** | stated at line 25 |
| **single-threaded / no correction narrative** | **PASS** | no correction narrative anywhere |
| **counts computed, never typed** | **PARTIAL** | see MAJOR-5 |
| **heads derived + string-equal into the paper** | **PARTIAL** | derived twice, but matched by **containment** — **MAJOR-1** |
| **no silent caps** | **PASS** | the window is in the verdict string and in Deviation 1 |
| **E-22** inline spans | **PASS** | the scan body is the whole paper; the code names the defect it fixed |
| **E-22** blocks by multiset | **FAIL** | **MAJOR-1** — containment, and every fence carried twice |
| **E-22** tables as claims | **FAIL** | **MAJOR-2** — 0 table rows rendered; 5 forgeries survive |
| **E-23** falsifier honesty | **FAIL** | **MAJOR-4** — 7 synthetic, 7 descriptions inverted |
| **E-24** measure-relativity | **PARTIAL (form only)** | **MINOR-7** — no stamp; but I measured the sharpest fraction under three measures and it is **stable** |

### Birth-date ruling

E-22 and E-23 were engraved at v14 **#187**, E-24 at **#192**. This unit's pin
was frozen at **#174** with "the full era per HANDOFF-PROMPT.md §4 (all 21
engravings)", and the ledger records no mid-flight relay to the r4dec worker.
Therefore:

- **E-22's inline-span half is credited, not owed** — the unit implemented it
  anyway, and its own comment shows it knew the #20 defect this era fixed.
- **E-22's multiset and tables halves, E-23 and E-24 were not binding at
  construction.** MAJOR-1, MAJOR-2 and MAJOR-4 nevertheless stand as MAJOR
  because their consequences are *demonstrated* (a headline-reversing forgery at
  exit 0) and because most of the obligation already sits inside the unit's own
  21: #20 requires coverage of every numeral with polarity, and #34 requires
  every falsifier to reach its gate and every waiver to be a machine-checked
  forcing. MINOR-7 is fully birth-date-excused.
- **MAJOR-3 and MAJOR-5 are NOT birth-date-excused.** #20's own gate statement
  and RUNBOOK §14's typed-literal clause are both inside the 21, and §14 names
  two prior demonstrations of exactly this failure.

---

## 12. FINDINGS, ORDERED

| # | severity | finding | repair |
|---|---|---|---|
| MAJOR-1 | MAJOR | fenced-block gate is containment; all four verdict fences are carried twice; forging either copy, deleting one, or appending a forged third all pass at exit 0 (INJ-03/04/10/11) | R-K3-1: multiset equality against a declared copy count + `MUT-PAPER-FENCE-MULTISET` |
| MAJOR-2 | MAJOR | tables are not rendered as claims; 5 table/inline forgeries survive, incl. the census table asserting FOUND where the run measured UNMOTIVATED (INJ-02/05/06/07/08) | R-K3-2: render the six published tables row by row + `MUT-PAPER-TABLE` |
| MAJOR-3 | MAJOR | `G-PAPER-COVERAGE`'s sealed statement says "only against the receipt … and this run's verdict strings"; a 42-literal hand list is also unioned in — 7 fire on 13 occurrences, 11 are dead; INJ-09 exploits it to contradict the paper's own head at exit 0 | R-K3-3: publish + gate the exemptions (must fire, must be unsupplied by the receipt); amend the statement |
| MAJOR-4 | MAJOR | E-23: 7 of 50 falsifiers are constant-`False` conjuncts, none corrupts a measured value, and all 7 published descriptions invert their code | R-K3-4: seven object-level corruptions + seven rewritten descriptions |
| MAJOR-5 | MAJOR | §14 comparator independence: ≥14 typed literals shared between builder and comparator; the "nor typed literal" sentence is false in the paper and in the sealed gate; `q=[[1, 0], [0, 1]]` is typed three times and derived nowhere | R-K3-5: derive the shared constants; gate the no-shared-literal property or delete the claim |
| MINOR-1 | MINOR | `G-READS-DECLARED`'s forcing is unsound and its statement false — `read_text` opens files without recording them (the paper, and the module itself) | categorise reads (SOURCE / OBJECT-UNDER-TEST / SELF) and gate all three |
| MINOR-2 | MINOR | 173 spelled-out numerals are unscanned, several load-bearing | word→value table in the coverage scan |
| MINOR-3 | MINOR | `NUMTOK` splits decimals and drops signs; several allow-list literals are unreachable in consequence | tokenise `-?\d[\d,]*(?:\.\d+)?(?:/\d+)?` |
| MINOR-4 | MINOR | `--selftest` proves "artifacts unchanged" by mtime, not by digest | compare sha256 |
| MINOR-5 | MINOR | a failing delivery run leaves `.tmp` staged files behind | `os.unlink` the stages on failure |
| MINOR-6 | MINOR | `totals.gates` 57 vs `gates` array 58 vs `coverage` 60, with only one step explained | name the snapshot instant in `totals` |
| MINOR-7 | MINOR (birth-date excused) | no fraction carries a measure or a COUNTING-ONLY stamp | one clause on the price row and on "mostly" — or cite §4's three-measure table |
| MINOR-8 | MINOR | the abstention scan's surface excludes `provenance`, `verbatim_anchors`, `mutants`, `walls` and the wall gates' own rows; five of these carry wall terms. The **gate statement scopes itself accurately** ("every measured receipt key…"); the **paper's** §7 phrase "this run's whole measurement layer" reads wider than the code | align §7's phrase with the gate's scope |
| MINOR-9 | MINOR | bare-copy death is an uncaught traceback, not a gate failure | catch and print `[CLI] missing source …` |
| MINOR-10 | MINOR | §2.3 attributes the exhaustiveness license to the equality; the equality licenses the *driven reading*, not the exhaustiveness | one-sentence rewrite (§1.3 above) |
| MINOR-11 | MINOR | the #125 normaliser is defeated only by a **mid-word** line break (not house style; 13/13 realistic evasions caught) | also compare a whitespace-stripped form of both sides |

**Withdrawn by me:** INJ-18 was mis-built (mid-word wrap) and is not a finding;
my first `--break-anchor` battery reported rc=0 on a shell pipe bug. Both are
recorded above rather than deleted.

**No finding moves a delivered number.** Every quantity in the four verdict
segments survived recomputation.

---

## 13. WHAT I COULD NOT BREAK

Recorded because a hostile review that reports only defects is not a
measurement.

1. **Byte reproduction.** Two hash seeds, two mirrors, no git, no sources
   outside the pinned 18 — both artifacts byte-identical to the committed ones,
   twice.
2. **The mutant sweep.** 50/50 killed, 50/50 on target, artifacts unchanged at
   every step, zero disagreement with the delivered rows.
3. **The seal.** 27/27 recompute from delivered bytes, 31/31 keys covered,
   27/27 corruptions caught, payload sha reproduces, DECLARED-UNSEALED
   measurement-free and frozen.
4. **The anchors.** 21/21 found, 21/21 non-vacuous under perturbation, 21/21
   consumers registered and evaluated; 18/18 `--break-anchor` deaths.
5. **The CLI.** 27/27 hostile argv forms exit 2 with artifacts untouched,
   including trailing arity on every mode flag and a directory passed to
   `--verify-paper`.
6. **The W4 license.** 372 drives the window never contains: 0 mismatches, 0
   branching, one driven field on every G-FLAT quadruple. The two priced
   deviations are under-claimed.
7. **The budget theorem.** Verified as a theorem and recomputed clean-room; the
   exhaustive columns rest on it, not on the window.
8. **Every combinatorial column.** Reproduced exactly by a clean-room program
   that shares no code with the instrument, with stage 4 recounted by a
   different algorithm.
9. **The E-24 headline.** "Mostly inhomogeneous" is stable across three
   invariant measures on the covering class.
10. **The gate wall.** Five shadow mutants that corrupt the *object* behind the
    seven synthetic falsifiers all died at their own gates, with a clean
    pristine control on both sides. MAJOR-4 is an honesty defect, not a hole.
11. **The #125 normaliser.** 13 of 13 realistic evasions of the banned L-1
    sentence caught, including the house-style wrap that bought the engraving.
12. **The walls.** The retracted L-1 sentence and the mandatory naming sentence
    are both defended by falsifiers that edit the *paper*, not a boolean; the
    naming-sentence inversion dies (INJ-12), and the three abstention walls scan
    a real surface.

---

## 14. THE SEAM RULING

The seam of this unit is **the paper**, not the receipt. Everything inside the
process — provenance, arithmetic, gates, seal, artifacts, mutants, CLI,
reproduction — is at or above the era's strongest standard, and I could not move
any of it. Everything the process says *about the document a reader will quote*
is one gate weaker than the era now requires: the fences are matched by
containment where E-22 demands a multiset, the tables are unrendered where E-22
says tables are claims, and the numeral allow list has a third component its own
sealed statement denies. Eleven of nineteen corruptions of the paper — including
one that reverses the second headline, and one that deletes the head's four
verdict blocks outright — pass at exit 0.

That is a repairable perimeter, not a false result. **AWF.**

---

**Objects re-verified at close:** `f54dad8d51b8` / `e387674bfcdd` /
`27ed73ded234` / `e1f148dd6a0e`; pin `f50630ced3be`. **Unchanged.** One repo
write made by this seat: this file.
