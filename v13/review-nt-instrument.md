# NT — HOSTILE REVIEW R3 (INSTRUMENT LENS)

**Reviewer:** R3, instrument lens (K5/K4 primary, K1–K3 at depth).
**Date:** 2026-08-07.
**Protocol:** `v13/note-nt-hostile-protocol.md` (frozen, v13 #203).
**Object under review, SHA-256 verified before reading:**

| file | sha256-12 declared | measured | ok |
|---|---|---|---|
| `v13/paper-nt-nomological-transport.md` | `730679a896de` | `730679a896de…` | yes |
| `v13/code/nt_transport_exact.py` | `76fb081b124f` | `76fb081b124f…` | yes |
| `v13/code/nt_transport_output.txt` | `e0dca9e00d34` | `e0dca9e00d34…` | yes |
| `v13/code/nt_transport_receipt.json` | `b0f6482be448` | `b0f6482be448…` | yes |

**Method.** All work in the session scratchpad; no repository file was read for
anything but reading, and no repository file was written except this review.
The instrument was never executed in place: it was copied into a sandbox tree
with `v12/` symlinked read-only, so no delivery-mode run could touch
`v13/code/`. Independent recomputation was rebuilt from the paper's prose,
importing only the committed base (`model_composite`, and my own re-derivation
of `w6_coreference_exact`'s `build_perm` / `build_perm_tr` from their source
definitions). Nothing was imported from `nt_transport_exact.py`.

**Recomputation count: 63 independent recomputations** across eight scratch
programs, plus **38 sandboxed executions of the frozen instrument** (the full
21-mutant sweep, three pre-delivery-bug reruns, two name-test-removal
experiments, two deliberate-anchor-breakage runs, and one full delivery-mode
rerun).

---

## 0. The headline: what survives

I tried to break this unit and could not break its physics. Recording that
first, because the findings below are numerous and none of them touches a
headline number.

**Byte-identical reproduction.** Two full delivery-mode reruns of the frozen
instrument in my sandbox produced `nt_transport_output.txt` with sha256
`e0dca9e00d34…` and `nt_transport_receipt.json` with sha256 `b0f6482be448…` —
byte-identical to each other **and identical to the committed artifacts, byte
for byte**. The committed receipt is what the committed code produces, the
determinism claim in §10 holds under my own execution and not only the worker's,
and no wall-clock or path-dependent value reaches the artifacts.

**Everything I recomputed from scratch matched.** In particular, from my own
code with my own predicates:

- the path space: 9 / 13 links, 3 / 7 identification links, cycle rank 2 / 6,
  422 / 16,168 reduced paths, 56 / 2,820 closed paths, **34,024** total paths,
  **4,972,096** same-endpoint pairs — all reproduced;
- the full matched pair table, all twelve cells, computed by **brute-force
  pair enumeration** rather than the unit's closed-form multiplicity
  arithmetic, and agreeing exactly (T1 681,660 / 1,025,340 / 1,276,120 /
  1,988,976; T2 1,478,644 / 228,356 / 2,769,932 / 495,164; T3 434,744 /
  1,272,256 / 917,412 / 2,347,684). Obstructed = 0 everywhere, as claimed;
- the per-object totals 1,957,780 / 3,014,316; 4,248,576 / 723,520;
  1,352,156 / 3,619,940, and the distinct-value counts 223 / 5 / 186;
- **all eight K1 witnesses**: the canonical loop is exactly the identity at
  every setting; the aligned-prefix bigons at t ∈ {0,1,3} at SP-E and SP-F all
  carry the wing exchange; both prefix-crossing loops carry exactly the
  identity; the SP-F bigon at t=1 is the one cell where T2 fails to return;
- the twisted comparator: not a signed permutation at SP-A–SP-D, another
  permutation with sign orbit {−1,+1} at SP-E/SP-F;
- **all 22 anchors**, each traced to its named source and recomputed
  (details in §2 F12 for the three exceptions);
- **K3's weld**, directly and independently: the amplitude composition is exact
  at all 48 nodes and Δᴮ equals W5's declared-law residual **entry by entry at
  all 48 nodes**. Defect weights 0 / 288 and j₀-column weight 16 all reproduce;
- **K4's numbers**: 18/18 prefix agreement, 12/18 residual agreement, all six
  equal-residual / opposite-transport witnesses, and cell-by-cell equality of
  all three profiles with the committed O4 receipt;
- **D1's cause, verified by construction**: the declared one-step Born
  transition is column- and row-stochastic but is not orthogonal — BᵀB ≠ I for
  the first leg at every setting — so the transposed step does not invert the
  forward one. The minimal witness is two moves long: pushing T1 forward across
  leg 1 and back again already fails to return, at all six settings. T1's
  non-return is not an artifact of the reverse-leg *construction*; it is a
  property of the declared Born-level action, exactly as §8.1 says;
- **all 21 mutants** re-run in the sandbox: 21 exit 1, and every kill set
  matches the committed receipt exactly;
- **D8 reproduced**: reinstating the pre-delivery convention (waiver predicate
  set to `True`) makes all three waivers **survive at exit 0**; the delivered
  convention (`False`) makes all three die. The fix is correct and the episode
  is honestly recorded;
- **exit-1-only proven by deliberate breakage in a direction no declared mutant
  tests**: I perturbed the *committed* side of five anchors (A02, A04, A09,
  A11, A19) inside a sandboxed copy of the O4 receipt. The run exited 1 and
  named exactly those five;
- **the §14 sweep bookkeeping is as declared**: 512 complete at the four
  9-link settings, 8,192 with 512 swept at SP-E/SP-F, checkpoint subgroup 128
  complete everywhere (recomputed by my own node-sign enumeration), 10 loops
  swept × 640 instances = **6,400**, matching the fresh-eval miss count exactly
  and the cache-hit count of zero;
- an **independent AST sweep** finds no float literal, no `float()` call, and no
  numeric builtin that could introduce one; every `/` in the module is a
  `pathlib` join.

**I also settled K3's D2 attack in the unit's favour, and more strongly than the
unit does.** I swept the **full 8,192-element** switching group over the SP-E
aligned bigon: 1 distinct permutation part, 2 distinct sign orbits — identical
to the sampled result. The unswept 7,680 elements hide nothing. The reason is
structural and is stated in F7 below.

The unit verdict `NT-HOLONOMY-⟨T1⟩ + NT-HOLONOMY-⟨T2⟩ + NT-HOLONOMY-⟨T3⟩ +
NT-PREFIX-FLATNESS-REFUTED` is the verdict the measurement supports. No finding
below moves it.

---

## 1. Findings, ranked

### F1 — MAJOR. A hard-coded mutant kill: `reduce-lax` is killed by its own name, and the reduced-path condition has no gate at all.

`nt_transport_exact.py:2224`, inside `NT-PATH-SPACE-ENUMERATED`'s predicate:

```
         and ps["_total_paths"] > 0 and MUTANT != "reduce-lax",
```

The gate's other clauses cannot catch this mutant, and two of them cannot catch
anything:

- `ps[sp]["nodes"] == len(FRAMES) * len(CHECKPOINTS)` — `n_nodes` is assigned
  `len(NODES)`, which *is* that product. Tautology.
- `ps[sp]["cycle_rank"] == ps[sp]["links"] - ps[sp]["nodes"] + 1` — `cycle_rank`
  is **defined** as `len(links) - len(NODES) + 1` at `build_graph`
  (line 851). The gate recomputes its own constructor argument. This is item 1
  of the W6 circularity catalogue.
- `closed_paths > 0` and `_total_paths > 0` remain true with the reduced
  condition dropped.

**Evidence, decisive.** I removed the literal name test in a sandbox copy and
re-ran the mutant:

```
reduce-lax -> exit 0  KILL-JSON {"failed_anchors": [], "failed_gates": []}
```

The mutant **survives** with zero failed gates and zero failed anchors. It dies
in the delivered build only because the gate reads its name. The reduced-path
condition — a declared property of the path space that is load-bearing for
34,024, for 4,972,096, and hence for every number in the matched table — is
**untested**. (I confirmed the condition itself is real and consequential:
dropping it takes SP-A from 422 to 12,228 paths.)

The same construct appears at line 1699 for `path-collapse` inside
`NT-HYPOTHESIS-FROM-THE-TABLE`. There it is redundant: I removed it and
`path-collapse` still died, on the measured clause
`(twisted > 0) == bool(probe_tw)`. That one is a code smell, not a defect.

The gate does have one genuine falsifier — `id-lax` empties the identification
links, `closed_paths` goes to 0 and the gate fires on a measurement — so the
census headline is not affected. The defect is that the paper advertises a
coverage it does not have.

**Repair.** Delete both literal `MUTANT !=` tests from the two gate predicates.
Replace the two tautological clauses with a measurement that can move — the
natural one is a property of the enumerated rows themselves: gate that **no
enumerated path traverses the same link twice in immediate succession**, which
is exactly the declared condition, is checkable from `edges`, and is violated by
`reduce-lax`. §3.2's sentence "the `reduce-lax` mutant drops the condition and
dies" and §10's "The suite covers … the path space (`path-collapse`,
`reduce-lax`)" may not be restored until the gate measures the condition.

---

### F2 — MAJOR. §8.2's holonomy value set is **4**, not 3; the value set is already **closed**; and D5's stated premise is a labelling artefact.

§8.2 reads:

| SP-E, SP-F | **3** — the identity, **the wing exchange**, and one further permutation | **order 4**, computed by closure |

The receipt computes the value-set size from **name labels**, not permutations
(line 2249): `els.add(PERM_NAME.get(canon(...), "another permutation"))`.
`PERM_NAME` knows two permutations; every other permutation collapses to the
single string `"another permutation"`.

**Evidence.** Enumerating every closed path based at F1@t=0 of the committed
path space, at both settings:

```
SP-E  distinct PERMUTATION parts = 4   distinct raw signed matrices = 4
      the 'other' permutations are 2 and are distinct: True
        other perm: fixed points=18, order=2
        other perm: fixed points=12, order=2
      IS THE VALUE SET ALREADY CLOSED UNDER COMPOSITION? True
      generated group order: 4      value set == group ? True
SP-F  (identical)
```

The true value set is the **Klein four-group**: the identity, the wing exchange,
and **two** further involutions. It is already closed at the declared bound —
value set = group = order 4.

Three consequences:

1. §8.2's "3" and "one further permutation" are wrong. The number reaches the
   rendered output as well (`nt_transport_output.txt` lines 294, 296).
2. **D5's entire premise is void.** D5 explains a 3-vs-4 gap by "the value set is
   enumerated at the declared length bound and need not be closed under
   composition there". There is no gap. The apparent gap is the label collapse.
   A deviation that explains a measurement artefact as a scope caveat is worse
   than a missing deviation.
3. §8.3's "a two-element wing-exchange holonomy at the two symmetric settings"
   understates the earned structure and contradicts §8.2's own "order 4" cell.
   RUNBOOK §10: a table cell may not editorialize against its own measured
   value.

**Repair.** Count permutations, not labels: replace `els` with the set of
permutation tuples and derive the names from it. Then:

- §8.2 row, verbatim replacement: `| SP-E, SP-F | **4** — the identity, **the
  wing exchange**, and two further permutations, each of order two | **order
  4**; the value set is measured already closed at the declared bound |`
- D5, verbatim replacement: "**D5 — the holonomy value set is bounded, and is
  measured already closed.** The value set is enumerated over the closed paths
  of the committed path space, which is bounded at L_max = 8, so it need not be
  closed under composition; it is measured to be closed here, and the group
  computed separately by closure is the same four-element group. Both numbers
  are carried in the receipt, and the paper never calls the value-set size a
  group order."
- §8.3, verbatim replacement for the final clause: "The geometric structure the
  theory earns here is small and exactly named — a four-element holonomy group,
  generated by the base's own wing exchange, at the two symmetric settings —
  and it is earned at the coordinates where the base admits two certified
  co-reference rules at once, not at the coordinates where prefixes diverge."

---

### F3 — MAJOR. §6's mechanism sentence is false for T1, and it is stated unscoped. (K2, at the full-table level.)

§6: "The measurement locates the twist precisely: holonomy appears exactly where
the base admits **two different certified identifications at one coordinate** …"

K2 asks for this to be checked against the full path-pair table and for holonomy
to occur "there and only there". It does not.

**Evidence — per-setting disagreement breakdown, recomputed by brute force:**

| setting | id-multiplicity ≥ 2 anywhere? | T1 disagreeing pairs | T2 | T3 |
|---|---|---|---|---|
| SP-A | no | **460** | 0 | 0 |
| SP-B | no | **460** | 0 | 0 |
| SP-C | no | **672** | 0 | 0 |
| SP-D | no | **672** | 0 | 0 |
| SP-E | yes (t=0,1,3) | 1,134,244 | 0 | 1,809,970 |
| SP-F | yes (t=0,1,3) | 1,877,808 | **723,520** | 1,809,970 |

At SP-A through SP-D no coordinate admits two identifications, yet T1 is
path-dependent at all four. The mechanism sentence is true of T3 (and of T2's
single SP-F cell) and false of T1 — which the paper itself establishes one page
later in §8.1 ("path-dependent as soon as a reverse step is taken … at every
setting including the four where the frames' geometry is trivial"). §6 and §8.1
are in tension as written.

Two by-products worth recording, both confirming the paper where it is right:

- T2's 723,520 disagreements are **entirely** at SP-F, exactly as §8.1 claims;
  T3's are entirely at SP-E and SP-F.
- I verified the flat crossing's cause by construction: P_W·U_A·P_W = U_B holds
  **exactly at SP-E and SP-F and nowhere else** (the two settings with equal
  angles). So the crossing loop's identity is genuine, not forced by the link
  construction — K1's third attack is answered. I also built the **unbuilt**
  t=2↔t=3 crossing loop (the code `break`s after the first): it is also exactly
  the identity, so no counterexample was skipped.

**Repair.** Scope the sentence. Verbatim replacement for §6's opening of "What
the mechanism is instead": "**What the mechanism is instead.** At the amplitude
layer the measurement locates the twist precisely: T3 holonomy appears exactly
where the base admits **two different certified identifications at one
coordinate**, and the two differ by the base's own **wing exchange**; T2 moves
at the one coordinate where that element is admitted and the defect is not
wing-symmetric. T1's path-dependence has a different and weaker cause — the
declared Born-level action is not invertible (§8.1) — and is present at every
setting, including the four where no coordinate admits two identifications.
Prefix alignment governs *whether an identification exists*, which is O4's
finding and survives §2 intact."

---

### F4 — MAJOR. The read time is **not** a coordinate of every datum: T2 carries none, and T2 data read at different checkpoints do compare equal.

§3: "Every transported datum carries the checkpoint at which it was read, and
two data read at different checkpoints can never compare equal — the O4 lesson
(RUNBOOK §15 addendum) built into the type rather than checked afterwards."
§9.2 repeats it: "the read time is a coordinate carried inside every datum."
The pin makes it a clause: "read time a declared coordinate in **every cell**".

`structural_key` (line 857) attaches the read time only when the value is a dict
containing `"law"` — that is, only for T1. T2's datum is a bare matrix.

**Evidence.** Equal-across-checkpoint pairs of T2 data (frame F1):

```
SP-A  (0,1) (0,2) (0,3) (1,2) (1,3) (2,3)      <- all six
SP-B  (0,1) (0,2) (0,3) (1,2) (1,3) (2,3)
SP-C  (0,3) (1,2)
SP-D  (0,3) (1,2)
SP-E  (0,1) (0,2) (0,3) (1,2) (1,3) (2,3)
SP-F  (0,3) (1,2)
distinct T2 node data without the read time: 4    with the read time: 10
```

The claim is false for T2 at every setting. The guard mutant does not cover it
either: `readtime-conflate` perturbs `node_law` only, i.e. T1 only. There is no
mutant for T2's coordinate because there is no coordinate to perturb.

This does not move a verdict — the pair table matches both endpoints by
construction, so every compared pair is read at one coordinate — but it does
contaminate a reported number: T2's `distinct_transported_values` = 5 is
computed on read-time-blind keys, and so is the `loop_value_set` column (see
F11).

**Repair.** Either (a) tag T2's datum with its cut index in `t2_value` and
`structural_key`, add a `readtime-conflate-T2` mutant, and re-derive T2's
distinct-value count; or (b) restrict the claim. Verbatim replacement for §3's
sentence under (b): "**The read time is a coordinate of the node, and of T1's
datum.** T1 carries the checkpoint at which it was read, so two T1 data read at
different checkpoints can never compare equal — the O4 lesson (RUNBOOK §15
addendum) built into the type. T2's datum is the defect matrix at the node's own
cut and is not so tagged; every T2 comparison in this paper is nevertheless at
matched coordinates, because the matched table pairs only paths sharing both
endpoints. T3 is a path functional and has no read time." §9.2 must be corrected
in the same terms, and §10's "distinct transported values" for T2 flagged as
read-time-blind.

---

### F5 — MAJOR. The declared 96/8 extension scope is never searched, and at it four admissions change — one of them would delete the canonical loop at two settings.

§3's arena table declares "admitted isomorphisms | **2** of the declared
72-element scope after the j₀ filter; **8** of its declared 96-element
extension". §9.9: "The permutation scopes are declared and every negative is a
negative at the stated scope: 72 elements admitting 2 after the j₀ filter, 96
admitting 8."

`admits()` (line 653) iterates `SCOPE["admitted"]` — the **2**-element set —
and nothing else. `SCOPE["admitted_extension"]` is used only in the arena table
and in anchor A17. No negative in this paper is a negative at the 8-element
scope.

**Evidence.** Re-running the same four-clause predicate over the declared
8-element admitted extension:

```
cells where the extension changes the admission count:
  SP-C FULL t=0 : 1 -> 2      SP-C FULL t=1 : 1 -> 2
  SP-D FULL t=0 : 1 -> 2      SP-D FULL t=1 : 1 -> 2
  (the extra element is a pointer transposition with 12 fixed points)
```

Because admission is by **uniqueness** (`len(adm) != 1 → continue`), at the
declared wider scope those four links would **not be admitted**. SP-C and SP-D
would keep only the t=3 identification, dropping to 7 links and cycle rank 0 —
and the canonical loop, which needs the FULL identification at t=0, **would not
exist at SP-C or SP-D**. Conversely, multiplicity ≥ 2 — which §6 names as the
place holonomy lives — occurs at the extension scope at prefix-*aligned*
checkpoints at two settings the paper reports as flat.

Using the 2-element scope is a legitimate inheritance from O4. Presenting the
96/8 pair in the arena table and in §9.9 as though the negatives were taken at
it is not. And D3's disclosure of the admission criterion discusses FORCED vs
CERT while omitting that FORCED is **scope-dependent**.

**Repair.** Verbatim replacement for §9.9: "**The permutation scope is
declared, and it is the narrow one.** Every admission search in this unit runs
over the **2** elements of the declared 72-element scope that survive the j₀
filter; every negative is a negative at that scope. The declared 96-element
extension, which admits 8, is anchored but is not searched: measured at it, the
full-leg rule admits two permutations at t=0 and t=1 at SP-C and SP-D, so the
uniqueness criterion would refuse those links and the canonical loop would not
exist at those two settings. That measurement is reported here and is not folded
into any verdict." D3 should gain one sentence naming the scope-dependence of
FORCED.

---

### F6 — MAJOR. `never_falsified` is EMPTY, but one of the thirteen is carried by a waiver alone.

The exempt gate (K5's question) is **`NT-FALSIFICATION` itself**, excluded by an
explicit `x["id"] != "NT-FALSIFICATION"` at line 1859. I judge that exemption
**legitimate and correctly disclosed**: `run_mutant_table` is guarded by
`a.falsification_selftest and not a.mutant`, so the census gate does not exist
in a mutant run and cannot be falsified by the mutant mechanism at all. It
remains a measurement that can come out otherwise — it is exactly what caught
the D8 bug — it just cannot be tested by itself. 15 gates, 1 disclosure, 14
must-pass, denominator 13. That arithmetic is right.

What is not disclosed is the composition of the 13. Cross-tabulating the mutant
table (reproduced in my sandbox, kill sets identical):

| must-pass gate | falsified by a *computation* mutant | by a *waiver* |
|---|---|---|
| NT-T2-POSABILITY | `defect-order` | `posability-lax` |
| NT-POSITIVE-CONTROL | `orient-flip`, `id-lax` | `control-lax` |
| NT-FLIP-DIRECTION | `readtime-conflate`, `orient-flip` | `flip-lax` |
| **NT-VOCABULARY** | **none** | `verdict-lax` |
| (the other nine) | yes | — |

**`NT-VOCABULARY` has no computational falsifier.** Its only kill is
`verdict-lax`, which the unit itself declares a **waiver** and about which §10
says a waiver "measures that the predicate carries the exit code — not that the
gate would catch a computational defect, and the two are not claimed to be the
same thing." By the unit's own taxonomy, then, the honest census is *13
falsified by some mutant, 12 falsified by a computational one*. The gate is
close to unfalsifiable by computation in any case: every branch of
`run_verdicts` emits a string built from a pre-registered template.

The 17/4 split itself is correct as declared and I verified it from
`MUTANT_DECL`.

**Repair.** Report both denominators. Verbatim replacement for the census bullet
in §10: "**Mutants:** 21, each run to completion, **21 of 21 died** — each
measured to exit 1 and to falsify at least one named gate or anchor. **The set
of must-pass gates that no mutant falsifies is EMPTY**, at denominator 13; the
fourteenth must-pass gate is the census's own, which does not exist in a mutant
run and so cannot be falsified by this mechanism. Of the thirteen, **twelve are
falsified by a mutant that perturbs a computation** and one — the verdict
vocabulary — only by a waiver, because every branch that emits a verdict builds
it from a pre-registered template. Each mutant declares its kind and the split
is counted from the declaration: **17 perturb a computation and 4 are
waivers**. A waiver overwrites a gate's computed predicate after the fact, so
what it measures is that the predicate carries the exit code — not that the gate
would catch a computational defect, and the two are not claimed to be the same
thing."

---

### F7 — MAJOR. §7's "the invariant is fixed" clause is analytically forced; the sweep's real teeth are elsewhere. (K3-D2 is thereby settled in the unit's favour.)

§7: "the sweep is built so that a wrong invariant would show", and the first
bullet, "**The invariant is fixed.** The permutation part takes exactly one
value under every switching swept, at every declared loop and every setting."

A switching assigns ±1 per link. A closed loop's link product is therefore
multiplied by the **product of its signs — a global scalar ±1** — and a signed
permutation matrix and its negative have the *same* permutation part. The clause
`len(perms) != 1` can never fire. No mutant can make it fire.

**Evidence, three ways.** (i) The full 8,192-element sweep of the SP-E aligned
bigon gives 1 permutation part and 2 sign orbits — identical to the sampled
result. (ii) Under the `gauge-sign` perturbation the permutation-part count is
*still* 1; what moves is the checkpoint-subgroup sign count, 1 → 2. (iii) Every
row of the receipt's `gauge_selftest.per_loop` reports
`distinct_permutation_parts_under_the_full_group: 1`, at all ten loops.

So `gauge-sign` dies on the **checkpoint-subgroup sign** clause — the
telescoping property ∏ sw = ∏ (node sign)² = +1 around a closed loop — which is
a genuine measurement, as is the group-order arithmetic, as is
`NT-GAUGE-CONTROL-MOVES` (10 of 10 loops move their raw sign). The gate as a
whole has teeth. The *sentence* presents a tautology as a measurement, which is
RUNBOOK §4's prohibition and RUNBOOK §14's own lesson one level up.

The same argument **answers K3's D2 attack definitively**, and more strongly
than the paper does: the unswept 7,680 elements at SP-E/SP-F cannot hide
switching-variance of the permutation part, because there is none to hide.

**Repair.** Verbatim replacement for §7's first bullet and lead-in: "**The
declared invariant is fixed, and fixed structurally.** A switching multiplies a
closed loop's link product by the product of its signs — a global ±1 — so the
loop's permutation part is invariant under the whole switching group by
construction, and the sweep confirms this rather than testing it: exactly one
value at every declared loop, every setting, and (checked separately at the
aligned-prefix bigon) over the complete 8192-element group, not only the sampled
512. **The sweep's teeth are the other two clauses.** The loop's sign is
measured invariant under the whole 128-element checkpoint subgroup — a
telescoping property that a wrong sign convention breaks, and the `gauge-sign`
mutant, which drops the switching on a reversed traversal, dies exactly there —
and moves under the full link-sign group, which is what makes it an orbit datum
and not a result."

---

### F8 — MINOR. The `[SAMP]` sweep is not a spread sample: it is exactly the subgroup that never switches a realized-rule link.

D2 and §7 call it "a declared uniform stride sample of **512** of the 8192".
With 13 links and stride 8192/512 = 16, and `itertools.product` varying the last
coordinate fastest, `k % 16 == 0` selects precisely the elements whose **last
four** coordinates are +1. Those four are link indices 9–12, which I identified
in the graph:

```
   9  id  REAL t=0 (wing exchange)     11  id  REAL t=2 (wing exchange)
  10  id  REAL t=1 (wing exchange)     12  id  REAL t=3 (wing exchange)
```

The sample is the subgroup fixing all four **realized-rule** identifications —
the very links that carry every scrap of holonomy content — at +1. By F7 this
costs nothing, and I verified the full sweep gives the same answer. But
"uniform stride sample" describes the algorithm, not the object, and a reader
auditing D2 would be misled.

**Repair.** Verbatim replacement for D2's third sentence: "The sweep is
**complete** at the four 512-settings; at SP-E and SP-F it covers 512 of the
8192, marked `[SAMP]` with both sizes printed. Because `itertools.product`
varies the last index fastest, the stride-16 sample is exactly the subgroup
holding the four realized-rule identifications at +1; that is stated rather than
glossed, and it costs nothing, because a switching multiplies a closed loop's
product by a global sign and cannot move the declared invariant at all (§7)."
Better still, replace the stride with an explicit generating-set sweep so the
sample is spread.

Related, non-blocking: `gauge_group`'s docstring says the group is "one sign per
link of the corridor sub-graph … the 2·NLEGS declared legs of the two frames
together with the FULL rule's identifications" — the code uses **all** links.
The paper is right and the docstring is stale.

---

### F9 — MINOR. The rule-label flip-test compares a list with a copy of itself.

Lines 1547–1554:

```python
            a = admits(sp, t, ID_RULES[0])
            b = [p for p in a]                       # same declared predicate
            if canon([list(x) for x in a]) != canon([list(x) for x in b]):
                full_rules_agree = False
```

`b` is a shallow copy of `a`; the branch is unreachable and
`rule_label_flip_is_inert: True` is structurally forced. This is item 2 of the
W6 circularity catalogue ("a comparison of an object with itself") reproduced
verbatim in live code that emits a receipt value. It sits inside a `disclosure`
gate, so nothing depends on it, and the paper does not cite it — which is why
this is MINOR rather than MAJOR.

O4's corresponding measurement was real: it compared three full-leg rules
(C2, C2X, C3). NT declares only one, so there is nothing to compare.

**Repair.** Delete the clause and the receipt key, or replace the emitted value
with `"not applicable: one full-leg rule is declared"`.

---

### F10 — MINOR. §5 reading 5's leading sentence is false as written.

"Conjugating the composition defect by the wing exchange returns the same matrix
everywhere except **SP-F at t=1 and t=2**, where P_W Δᴮ P_W⁻¹ ≠ Δᴮ."

Measured, over all 24 (setting, checkpoint) cells of frame F1:

```
SP-C t=1 nonzero, P_W D P_W != D : True      SP-D t=1 : True      SP-F t=1 : True
SP-C t=2 nonzero, P_W D P_W != D : True      SP-D t=2 : True      SP-F t=2 : True
```

Conjugation moves the defect at SP-C and SP-D too. The paragraph's *next* clause
supplies the missing qualifier ("at SP-C and SP-D the wing exchange is not
admitted"), so the paragraph as a whole is sound and §8.1's conjunction is
correct — but the sentence that carries the claim omits its own scope, which is
exactly RUNBOOK #40 F1/F2.

**Repair.** Verbatim replacement for the first sentence of §5 reading 5:
"**T2 moves at exactly one coordinate of the transport, and it is the sharpest
cell in the table.** Wherever the base admits the wing exchange as an
identification, conjugating the composition defect by it returns the same matrix
except at **SP-F at t=1 and t=2**, where P_W Δᴮ P_W⁻¹ ≠ Δᴮ. (Conjugation also
moves the defect at SP-C and SP-D, but the wing exchange is not an admitted
identification there, so no transport carries it.)"

---

### F11 — MINOR. §8.1's "loop value set" column aggregates base points, and the mechanism the paper attributes to it is the one D4 rules out.

`loop_value_set_size_per_setting` (line 1636) counts distinct values over closed
paths from **all eight base points**, not the holonomy of a based loop. At SP-C
and SP-D the T2 column reads 2 — and the T2 disagreement count there is **0**.
The 2 is simply "the two distinct T2 node data", one at the division events and
one at the intermediate cuts:

```
SP-C  T2 loop-value-set(all base pts)=2  (based at F1@t0)=1  distinct NODE data=2
SP-D  T2 loop-value-set(all base pts)=2  (based at F1@t0)=1  distinct NODE data=2
```

§8.1 explains those cells as "the leg reason — the defect is a datum of the cut
and moving the cut moves it". But D4 states, correctly, that "T2's leg action
carries the matrix unchanged": **no leg move within a path moves T2**. The
variation is entirely across base points. The stated mechanism contradicts the
unit's own declaration.

The verdicts do not depend on the column (`NT-HOLONOMY-⟨obj⟩` is emitted iff the
disagreement count is positive, which I verified), so this is presentation.

**Repair.** Rename the column to "settings at which the closed-path values
differ across base points" and replace the explanatory sentence: "SP-C and SP-D
enter that column for the base-point reason — the defect is a datum of the cut,
and closed paths based at the division events and at the intermediate
checkpoints carry different cuts — and not because any move transports it: at
those two settings no pair of same-endpoint paths disagrees about T2 at all."

---

### F12 — MINOR. Three of the 22 anchors are not what §10 describes.

§10: "**Anchors:** 22, exit-1-only, against the committed O4 terminal receipt …
the committed W6 note and output, and the committed model's own orthogonality
and commutation measurements." Nineteen are exactly that, and I recomputed every
one. Three are not:

- **A12** types its committed side `(36, 36, 30, 30)` although the O4 receipt
  carries `pair_census` and A13 reads that same table programmatically. The
  value is correct — I recomputed 36/36 and 30/30 at t=2 and 0/36 at t=1, t=3 —
  but RUNBOOK §4's "computed, never typed" argues for reading it.
- **A22** compares `len(o4["anchors"])` with `sum(1 for x in o4["anchors"] if
  x["passed"])`. Both sides come from the same file; it anchors no NT quantity.
  It is a useful health check on the source artifact, but it is not an anchor of
  a reused number, and its `source` string ("v12/note-w6-record-coreference.md /
  O4 anchors A04–A07") does not name what it reads.
- **A18**'s `source` reads "the committed composite model" while its committed
  side is `o4["tables"]["declarations"]["final_declared_division_event"]`.

**Repair.** Read A12 from `o4["tables"]["pair_census"]`; relabel A22 as a source
health check with a correct `source` string (or move it out of the anchor list);
correct A18's `source`. Adjust §10's sentence to say that one of the 22 anchors
checks the source receipt's own integrity rather than a reused number.

---

### F13 — NOTE. Coverage disclosures that are true but incomplete.

- §8.4's direction flip-test says "every declared loop". The receipt covers **14
  of the 20** probe rows; the six twisted comparators are skipped because
  `loop["edges"] is None`. The negative control is never flip-tested.
- §10 says the §14 sweep's tested set is "one loop per declared probe role". It
  is one loop per role **that has an edge list**: 3 of the 4 declared roles are
  swept, the negative control again being skipped. 10 loops × 640 = 6,400,
  which is exactly the fresh-eval miss count — so the arithmetic is transparent
  once the exclusion is known.
- Only the **t=0** bigon is swept at each of SP-E/SP-F (the t=1 and t=3 bigons
  share its role and are deduped), and only the **t=1↔t=2** crossing loop is
  built (the `break` at line 1250). I checked the skipped t=2↔t=3 crossing loop
  independently: also exactly the identity. Nothing is hidden.

**Repair.** One clause in §8.4 and one in §10 naming the exclusion.

---

### F14 — NOTE. "18 of 18" has an effective sample of three.

The 18 cells are 3 read times × 6 settings, and the profiles are constant in the
setting at each read time (t=1 aligned/transports, t=2 divergent/does not,
t=3 aligned/transports). Six settings replicate one pattern. The same holds for
the 12/18: the six disagreements are t=1 at SP-C/D/F and t=2 at SP-A/B/E. The
convention is inherited from O4 and the numbers are right; a reader should
simply know that the denominator counts cells, not independent structures.
No repair required; a half-sentence would be generous.

---

### F15 — NOTE. K4's independence is algorithmic, not derivational — but the transport profile *is* independent, so the 18/18 is not circular.

I read both implementations. O4 (`o4_discriminator_exact.py:1961`) computes
`any(all(W6.leg_match(K, lb[x], la[sg[x]], "born")) for sg in permutations(...))`,
and `leg_match(..., "born")` reduces to `sp_born(X) == sp_born(Y)`. NT computes
multiset equality of canonical renderings of `born(L)`. **Multiset equality of
canonical keys *is* "there exists a bijection matching the keys"** — the same
predicate, computed by sorting instead of searching. I ran both routes over all
18 cells and they agree cell for cell, as they must. So the independence here is
implementation-level: it would catch a coding error in O4's search, not an error
in the *definition* of prefix alignment.

The paper is careful — §2 says "**The route** is different from O4's" and names
the two algorithms — but the abstract's "PREFIX-DECIDES is **re-derived here
independently**" carries more than the route does.

**The more important half of K4 passes cleanly.** The *transport* profile is
computed by a genuinely different predicate: NT's four-clause admissibility
search over the admitted scope, versus O4's candidate/matched-table machinery.
And it is not a restatement of the prefix profile: NT's leg clause compares the
**full** leg lists (which always match), so what separates t=2 from t=1 and t=3
is the occupied-set and exact-law clauses — a different measurement from
"do the first t legs match order-free". The 18/18 agreement is therefore a real
coincidence of two distinct computations, not a tautology. I confirm it.

**Repair.** Soften the abstract by one word: "**PREFIX-DECIDES is re-derived
here by an independent route**".

---

## 2. Kill-shot dispositions

**K1 — the refutation witnesses. PASSES.** All eight recomputed independently
and exactly: six twisted-corridor bigons (aligned prefix, t ∈ {0,1,3}, SP-E and
SP-F, holonomy = the wing exchange) and two flat crossings (t=1↔t=2, SP-E and
SP-F, holonomy = the identity). The bigons are genuine closed loops based at
F1@t — F1@t → F2@t by the FULL rule reversed, back by the REAL rule — with an
admitted-by-uniqueness identification at each end; I re-derived both admissions
myself, over my own enumeration of the declared scope. The wing-exchange
holonomy is gauge-invariant content, not a relabelled orbit: by F7 no switching
can touch a permutation part, and I confirmed it over the complete 8192-element
group. The flat crossing is genuine and not construction-forced: it is the
identity because P_W intertwines the two frames' second legs, which I verified
holds at SP-E and SP-F and at no other setting.

**K2 — the mechanism. FAILS AS STATED, for T1.** See F3. Multiplicity ≥ 2 occurs
exactly at SP-E/SP-F at t ∈ {0,1,3} (FULL identity + REAL wing exchange), and T3
holonomy occurs there and only there — the claim is correct for the amplitude
layer. It is false for T1, which is path-dependent at all six settings including
the four where multiplicity is never ≥ 2. D3's FORCED-not-CERT demotion is
disclosed honestly and I confirm the consequence (a CERT reading would empty the
loop space); what D3 omits is that FORCED is scope-dependent — F5.

**K3 — the holonomy computations. PASSES on T1 and T2; FAILS on T3's value-set
count.** T1: 223 distinct values, nontrivial at all six, and the cause verified
**by construction** (BᵀB ≠ I; a two-move minimal witness at every setting). T2:
5 values, and the weld verified directly against both sources — Δᴮ is W5's
declared-law residual entry by entry at all 48 nodes, with the amplitude
composition exact at all 48. T3: the value set is **4**, not 3, and it is the
Klein four-group, already closed at the bound (F2). The generated group order 4
is right. D2 is answered definitively and in the unit's favour (F7).

**K4 — PREFIX-DECIDES re-derivation. NUMBERS PASS; the independence claim is
one notch stronger than the fact.** 18/18, 12/18, all six witnesses, and all
three profiles cell by cell against the committed O4 receipt — reproduced from
my own code. See F15 for the scope of "independently".

**K5 — instrument. THE MOST FINDINGS LIVE HERE.**
D1: scoping the positive control to the amplitude layer is **legitimate**, and
T1's non-return is neither under-claimed nor an instrument defect. §8.1 states
it as a finding, §9.5 declares the action, and the cause is a property of the
declared Born-level step which I verified by construction — the reverse-leg
construction is faithful (a reverse traversal applies the exact transpose, and
`orient-flip`, which drops the transposition, dies on the positive control, as I
reconstructed independently). If anything the paper under-sells it: the minimal
witness is two moves long, which is a cleaner statement than "around a loop".
D8: the fix is **correct** and the account is **exact** — I reinstated the
pre-delivery convention and reproduced the survival (exit 0 for all three), then
confirmed the delivered convention kills all three. The 17/4 split is right. One
waiver does hide a gate that nothing else tests — F6.
`never_falsified` EMPTY at denominator 13: the exempt gate is `NT-FALSIFICATION`
and the exemption is **legitimate and disclosed**; the composition of the 13 is
not — F6.
Anchors, path-space counts, fresh-eval, and the §14 bookkeeping: all
reproduced (§0). Two mutants reconstructed from prose in my own code
(`orient-flip` breaks the canonical loop; `defect-order` matches W5's residual at
only 24 of 48 nodes and moves the residual profile from [0,0,16,16,0,16] to
[10,10,12,12,4,16]), plus a third (`reduce-lax`, 422 → 12,228) — and the third
is how F1 was found.

---

## 3. Summary of required repairs

Blocking (numbers or instrument integrity): **F1** (delete the hard-coded
mutant-name tests; give the reduced-path condition a real gate), **F2** (count
permutations not labels; correct §8.2, D5 and §8.3), **F5** (state the operating
scope and disclose the extension-scope measurement).

Blocking (claims broader than their gates): **F3** (scope §6's mechanism),
**F4** (scope or fix the read-time claim), **F6** (report both census
denominators), **F7** (stop presenting a tautology as a measurement).

Non-blocking but should ship: F8–F13. F14–F15 are observations.

No number in the pair table, the path space, the anchors, the probes, the weld
or the verdicts requires a change. **No mutant re-run is required except after
the F1 repair, which will change no receipt value** (`reduce-lax` already exits
1 today; after the repair it will exit 1 for a reason).

---

## 4. Grade

I make no claim to have exhausted this instrument. What I can say is that I
attacked it along the axes the protocol names, rebuilt every load-bearing
quantity from the published prose without importing a line of it, reproduced the
delivery byte for byte, and could not find a false physics number anywhere. The
four headline results survive intact and so does the unit verdict. What I did
find is a gate that reports a falsification it did not perform, a wrong count in
a headline table with a deviation built on top of it, a scope declared and not
used, and four sentences stated wider than their measurements — which is a
serious instrument bill, and an entirely repairable one.

> **ACCEPT-WITH-FIXES.**
