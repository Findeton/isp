# XBA — HOSTILE REVIEW R3 (INSTRUMENT LENS)

**Reviewer:** R3, the instrument lens. **Date:** 2026-08-08.
**Protocol:** `v13/note-xba-hostile-protocol.md` (K1–K5 binding), frozen
before dispatch. **Primary weight:** K5, with K1 and K2 at lower depth.
**Repository access:** read-only. No git. No child agents. One file written.

## 0. The frozen object, verified

| artifact | sha256-12 | verified |
|---|---|---|
| `v13/paper-xba-crossbase.md` | `284a51e88e6f` | yes |
| `v13/code/xba_crossbase_exact.py` | `91677df8bbc7` | yes |
| `v13/code/xba_crossbase_output.txt` | `603a6eab18cf` | yes |
| `v13/code/xba_crossbase_receipt.json` | `1945dbb12eb1` | yes |

All four verified at the start of the review and re-verified at the end,
unchanged. No repository file was modified; every experiment ran on a scratch
copy of the tree.

**Recomputations: 114.** Counted below in §6.

**Method.** I read the RUNBOOK §13–§15 and all five addenda, the pin, the
frozen protocol, the paper, the instrument (2,217 lines) and the receipt. I
then built an *independent* rebuild of the whole combinatorial layer from the
paper's prose alone, on a deliberately different route — **no spanning tree and
no cotree**: a connection is six Klein values on the declared cycle basis, and
each walk's class is solved into that basis over $\mathbb{F}_2$ from its
13-link parity vector. Every headline number was recomputed there before I
looked at how the instrument computes it. I then attacked the instrument
itself with file-level pin corruption, four declared-mutant re-runs, two
from-prose mutant reconstructions, three probes of my own design, and a
200-fold randomisation of the cycle coordinates.

---

## 1. Findings, ranked

### MAJOR-1 — The printed verdict has no computational falsifier; the derivation sits outside the gate

**§13 addendum (2026-08-08, v13 #234), first clause, verbatim:** *"the printed
verdict string must be derived inside a gate from the measured counts, and a
verdict-flip mutant must prove that derivation can fail — an ungated verdict is
a typo away from fiction."*

The unit was built before that addendum (#234 precedes the XBA protocol freeze
at #238 by hours). Judged as the addendum asks — does it *happen* to comply —
**it does not.**

**Evidence.** Source lines 1561–1574. `verdict` is assigned by an
`if named: / elif partial: / else:` chain over the measured lists and *then*
handed to a gate whose predicate is membership in a three-string tuple:

```
gate("XBA-VOCABULARY", verdict in PREREGISTERED
     or verdict.startswith("XBA-BLOCKED-AT-"), "must-pass", {...})
```

The derivation is never gated. I ran the verdict-flip probe the addendum asks
for: in a scratch copy I swapped the two branch strings
(`if named: verdict = "XBA-PARTIAL"` / `elif partial: verdict =
"XBA-SHARED-STRUCTURE-IDENTIFIED"`). The run printed
`>>> XBA-PARTIAL`, exited **0**, and reported **"must-pass failures 0"**. No
gate fired. The receipt would have carried `findings.unit_verdict:
"XBA-PARTIAL"` under an otherwise clean instrument.

The declared `verdict-lax` mutant is a **waiver** that overwrites the verdict
with an out-of-vocabulary string (`"XBA-EVERYTHING-IS-FINE"`). It tests the
vocabulary predicate, not the derivation — and the frozen census confirms it:
`XBA-VOCABULARY` is one of the four gates in `falsified_only_by_a_waiver`.

**Severity.** Major as an instrument defect. It does *not* touch the result:
on my own independent recomputation the derivation's inputs are right (C4 and
C5 are exactly the candidates both bases satisfy that force, and both subsets
are proper), so the printed verdict is the correct one. The defect is that
nothing in the instrument would have caught it if it were not.

**Repair (no re-derivation needed).** Gate the derivation itself, e.g.
`(verdict == "XBA-SHARED-STRUCTURE-IDENTIFIED") == bool(named)` and
`(verdict == "XBA-PARTIAL") == (not named and bool(partial))`; add a
*computation* mutant that empties `named` (force
`forces_the_multiset_profile` False for C4/C5) and dies at that gate. Re-run
the census.

---

### MAJOR-2 — The "second spanning tree" is not a second route: its census numbers are algebraically forced, and its cell set is not gated complete

**§13 addendum (v13 #234), second clause, verbatim:** *"two independent routes
for a census must be genuinely independent computations; a pair related by an
algebraic identity is one route, and a cell-completeness gate must catch a
dropped cell."*

The paper §9 calls the flip-test "an independent comparator" whose "three
census numbers are gated against the first tree's own computed values", and
§12 lists it under "Independent comparators". Four measurements say otherwise.

**(a) One of the three numbers does not depend on the tree at all.** Line 2110:

```
order4_2 = sum(1 for p in ALLPHI if len(generated_group(p)) == 4)
```

`coord2` does not appear. This is the same expression as the first tree's
`order4`, evaluated twice.

**(b) The other two are invariant under *any* invertible change of cycle
coordinates.** I recomputed the census under **200 arbitrary invertible
$\mathbb{F}_2$ changes of the six cycle coordinates**. All 200 returned
exactly `(89, 96, 3906)`. A second spanning tree induces one such change, and
`cycle_coords` always assigns distinct powers of two to cotree links, so the
change is always invertible. `census_identical` therefore cannot fail in any
run that has passed `XBA-CYCLE-RANK`. It is a tautology, not a comparator —
and a shared bug in `cycle_coords`, `walk_class` or `make_profiler` would
corrupt both "routes" identically.

**(c) A dropped cell is not caught.** Line 2128:

```
subsets_ok = all(sizes1[n] == sizes2[n] for n in sizes2)
```

The loop runs over `sizes2`'s own keys. Probe: I set `sizes2 = {}` — every
compared cell dropped. Result: `subsets_identical True`, exit **0**,
**"must-pass failures 0"**. There is no cell-completeness gate; `all()` over
an empty set carried the gate.

**(d) Even undropped, the comparison covers 9 of 12 candidates.** The frozen
receipt's `tree_flip_test.candidate_sizes_second_tree` has **9** keys against
the first tree's **12**: the filter `if not n.startswith("C2")` drops C2a, C2b
and C2c, and `declare_candidates` is called with `[], []` for the two
automorphism actions in tree 2, which would make all three vacuously true
anyway. The paper §9's "and every candidate's subset size identical" is an
overclaim by three cells.

**(e) Consistent with all of the above,** the frozen census records
`XBA-TREE-FLIP-TEST` as falsified only by the `flip-lax` waiver, which
overwrites `flip["census_identical"] = False`. No computation can kill it.

**Repair.** Either demote `XBA-TREE-FLIP-TEST` to a disclosure — which is what
§9 already, correctly, does for the two other analytically-forced clauses — or
replace it with a route that is genuinely independent (e.g. recompute the
profile histogram from a separately enumerated walk set, or recompute a sample
of connections' class counts by the raw matrix product). Add
`set(sizes1) == set(sizes2)` and `len(sizes2) == len(CAND)` to the predicate.
State the C2 exclusion at the claim in §9.

---

### MAJOR-3 — All four "waiver-only" must-pass gates are analytically forced once earlier gates pass

The paper §12 names the four gates that only a waiver falsifies — the positive
control, the spanning-tree flip-test, the freeze order and the verdict
vocabulary — and says, honestly, that a waiver "measures that the predicate
carries the exit code — not that the gate would catch a computational defect,
and the two are not claimed to be the same thing." What it does not say is
*why* no computation mutant falsifies them. In all four cases the reason is
the same and is stronger than "unreached": **the predicate cannot fail.**

- **`XBA-POSITIVE-CONTROL`** (line 1437): `pos_ok = all(PROF[phis[tag]] ==
  TARGET for tag in phis) and len(phis) == len(realized) == 4`. Gate 7
  (`XBA-THE-TWO-BASES-SHARE-ONE-CONNECTION`) already requires
  `len(distinct_phi) == 1` and `len(phis) == len(realized)`, and `TARGET` is
  *defined* as `PROF[PHI_R]` at line 1255. So whenever gate 7 passes, every
  `phis[tag]` **is** `PHI_R` and the predicate is true by definition;
  `len(realized)` is 4 unconditionally (four fixed dict entries). The two
  gates fail together or not at all.
- **`XBA-TREE-FLIP-TEST`** — MAJOR-2.
- **`XBA-FREEZE-ORDER`** (line 1548): gates are appended in execution order,
  and the four named calls textually follow the declaration gate. Measured
  indices 11, 12, 13, 18 against a declaration index of 10. Forced by source
  order.
- **`XBA-VOCABULARY`** — MAJOR-1.

**§14 addendum (v13 #208):** *"Analytically-forced clauses (true by algebra for
every input) are disclosures, not must-pass gates."*

**Consequence for the headline.** "The set of must-pass gates that no mutant
falsifies is EMPTY, at denominator 23" is **true as printed**, and both
denominators (23 falsified by some mutant, 19 by a computation mutant) *are*
printed — which is to the paper's credit and is exactly the discipline §13
asks for. The honest reading, which the paper does not supply, is that 19 of
23 are computationally falsifiable and the remaining 4 are tautologies with
waivers attached.

**Repair.** Reclassify the four as disclosures (giving must-pass 20 including
the census, disclosures 8), or replace each with a falsifiable predicate. In
either case state the forcing argument for each in §12, so the reader is not
left to infer that a waiver-only gate is merely one the mutants failed to
reach.

---

### MODERATE-1 — A fail-closed path is claimed exercised and is not

**§12 claims:** *"Two prerequisites refuse every downstream measurement rather
than crashing: if the declared cycle basis is measured not to be a basis, and
if no base yields a readable connection. **Both paths are exercised** — by the
`basis-lax` and `base1-angle` mutants respectively — and both exit 1 with the
failed gate named."*

I ran both.

- `basis-lax` **does** take its path: it prints `FAILED: XBA-BASIS-INDEPENDENT,
  XBA-BASIS-INVERTIBLE` followed by *"the declared cycle basis is not a basis;
  every downstream measurement is refused"*, exit 1. Correct as claimed.
- `base1-angle` **does not**. It perturbs only base 1 @ SP-E, so base 1 @ SP-F,
  base G @ GP-E and base G @ GP-F still yield readable connections,
  `distinct_phi` is non-empty, and the refusal branch at lines 1168–1174 never
  runs. The run continues to the direct comparator and dies at anchor **A36**,
  having already failed `XBA-DIRECT-COMPARATOR` — gate index 8, which is
  *downstream* of the refusal branch. **The frozen receipt contains its own
  disproof**: `per_mutant["base1-angle"].falsified` lists
  `XBA-DIRECT-COMPARATOR`.

The second fail-closed branch is untested code and the coverage claim is false
as written.

**Repair.** Add a mutant that makes all four readings unreadable (e.g. read
*every* base at an asymmetric setting), or correct §12 to record that the
second path is declared but not exercised.

---

### MODERATE-2 — The cache self-test: the refusal is real, but "returned on a second visit" is not measured and one gate clause is an identity

This is the §14 disease the protocol singles out, so I separate what holds
from what does not.

**What holds — and it holds well.** The refusal mechanism is genuine, and the
gate is not the vacuous "zero hits of zero lookups" of §14-addendum (#219).
`XBA-GAUGE-SELFTEST-HAS-TEETH` requires `cache_hits == 0` **and**
`cache_misses > 0` **and** `refused_lookups > 0` **and** `primed > 0`. I
reconstructed the violation the protocol asks for by running `memo-lax`, which
flips the sweep onto the cache path: it reports `cache hits 442368, fresh
evaluations 0, refused lookups 0` and dies at that gate. I independently
confirm the arithmetic: **27** distinct walk masks × **16,384** gauge elements
= **442,368**, matching `refused_lookups` and `fresh_evaluations` exactly. The
read path exists, is reachable, and is measured shut.

One honest observation in the instrument's favour and one against. In favour:
even under `memo-lax` the sweep still reports `deviations 0`, so a cache-fed
sweep would have looked perfect — which is precisely why the hit count must be
gated, and it is. Against, in the sense of what carries the weight: the
refusal is therefore *not* what gives the invariance measurement its teeth.
The teeth are the mis-convention control at **12,288 of 16,384**, which I
reproduce independently. The paper says exactly this in §9. Good.

**What does not hold.** Line 2042:

```
CACHE_STATS["reserved_returns"] = sum(1 for m in masks if ("selftest", m) in HOLCACHE)
```

This counts key **presence**. It never reads `HOLCACHE[key]` back and compares
it to what was stored. And since `primed` is incremented once per `mask_bits`
entry while the keys are exactly those masks, `reserved_returns == primed` is
true for **every possible input** — a second tautology inside a must-pass gate.

Probe: I primed the cache with a deliberately **wrong** value (`x ^ 1`).
Result: exit **0**, zero must-pass failures, `reserved_returns` still 27 =
`primed`. So the paper §9's *"The priming pass is measured to return its
stored values"* and its table row *"entries primed before the sweep, **and
returned on a second visit** | 27 / 27"* describe a measurement the instrument
does not make.

**Related, and worth one sentence in the paper.** `HOLCACHE` occurs **only**
inside `gauge_selftest` (lines 2033–2065). The instrument has no memoiser
anywhere else — `PROF` is a fully materialised dict built by direct
evaluation. So "**the** value cache" (§9, definite article) is a prop the
self-test erects for the self-test, not a live component. That is stronger
than nothing and the paper half-concedes it ("exactly how a naive memoiser
*would* key a holonomy"), but the definite article plus the "returned on a
second visit" row read as a report on a component that exists.

**Repair.** Read one primed key back and gate that the returned value equals
the stored one — that is the claim as written. Demote
`reserved_returns == primed` to a disclosure. Drop the definite article in §9.

---

### MODERATE-3 — The freeze counter is instrumented on one code path, and a class-count profile is computed before the declaration point on another

`PROFILE_EVALS` is incremented only inside `make_profiler`'s closure (line
792). The direct comparator (lines 1190–1207) computes, for base 1 @ SP-E and
base G @ GP-E, the class counts of all 364 walks by the raw-matrix route. That
is a class-count profile, and the **frozen receipt carries it** at gate index
**8** as `{"1": 82, "D": 90, "W": 86, "WD": 106}` for both bases — while
`XBA-CANDIDATE-FREEZE` at gate index **9** reports
`profiles_computed_before_the_declaration: 0`.

So §2's *"The instrument gates the freeze with the profile-evaluation counter
measured at zero at the declaration point"* is a statement about calls to one
function, not about profiles.

**Mitigating, and material to the severity.** The realized profile is a
**pinned input**: anchors A32/A33 read 82 / 86 / 90 / 106 out of the two
terminal receipts before any candidate is declared. No blindness was available
to lose here, and §11.5 and D1 already concede the substantive residual (the
realized labels were computed first, because membership needs them). The
freeze's real content is "the 4,096-census had not been run", which is true.

**Repair.** Rename the evidence key to
`census_profile_evaluations_before_the_declaration`, and add one sentence to
§2/D1 recording that the realized class counts are an anchored input and are
recomputed by the comparator before the declaration point.

---

### MINOR-1 — The census records anchor kills as truncated fragments, not names

`run_mutant_census` extracts `ln.split()[-1]` from each `ANCHOR FAILURE` line
(line 2175). The recorded kill is therefore the last whitespace token of the
anchor's name. In the frozen receipt:

| mutants | recorded "kill" |
|---|---|
| `anchor-nt-hash`, `anchor-gen-hash`, `anchor-review-hash` | `"sha256"` (all three identical) |
| `field-lax`, `wingswap-lax` | `"points"` (both identical) |
| `graph-drop-real2`, `graph-add-full2`, `reduce-lax` | `"setting"` |
| `rot-lax` / `completion-lax` / `anchor-census` / `anchor-classcounts` / `lmax-lax` | `"R1"` / `"V"` / `"profiles"` / `"counts"` / `"walks"` |

Thirteen of 35 mutants have no named kill in the record, and three pairs/triples
are indistinguishable. §12's "each measured to exit 1 and to falsify at least
one **named** gate or anchor" is unsupported for those thirteen.

The headline is not corrupted: `never_falsified` is computed over gate names,
which all begin `XBA-` and never collide with these fragments — I checked the
collision explicitly. I recovered the true attributions by re-running
(`base1-angle` → A36; my from-prose reconstruction of `graph-drop-real2` → A11
+ `XBA-WALK-AUDIT`; the three hash mutants → A02 / A03 / A04, confirmed
independently by corrupting the actual files).

**Repair.** `why.append(ln[len("ANCHOR FAILURE  "):].strip())`.

---

### MINOR-2 — The stated mechanism for C2a's vacuity is wrong

§2: *"The rule-preserving group is generated by the frame swap, **which
carries every link to itself** and therefore acts trivially on cycles."*

Measured: the frame swap moves **all six leg links** (LEG_F1_$i$ ↔ LEG_F2_$i$);
only the seven identification links are fixed. I computed the moved set
directly: six links.

The **conclusion is correct** and I confirm it independently — the
rule-preserving group has order 2 and induces exactly one action on the cycle
space, the identity — but for a different reason: each *declared cycle's edge
set* is symmetric under the frame swap, not each link. Only the reason given
is false. This is the failure-catalogue class "describe mechanisms as
measured, not as intended" (#38→#40), and it sits on one of the pin's own
three candidate answers.

**Repair.** "…generated by the frame swap, which exchanges the two frames'
legs and fixes every identification link, and therefore carries each declared
cycle to itself."

---

### MINOR-3 — `XBA-NO-MUTANT-EXEMPTION` measures a lexical property that a one-line hoist satisfies

I re-ran the sweep independently: **64** gate/anchor call sites, **0** reaching
`MUTANT` — and also 0 reaching `M_ON`, though the sweep does not look for
`M_ON`, which is the other way the mutant flag is read.

More to the point: **eight** mutant checks sit within four lines *above* a gate
call and assign to the very variable the gate tests — `chain-lax`→`cons`,
`control-lax`→`pos_ok`, `flip-lax`→`flip["census_identical"]`,
`order-lax`→`order_ok`, `verdict-lax`→`verdict`,
`float-lax`/`exempt-lax`→`floats`/`mutant_ne`. All are in the *falsifying*
direction, so none exempts a falsifier and §14-addendum (#208) is not violated
in substance. But the gate as written would equally pass
`if MUTANT == "x": ok = True` placed one line above the gate — which is
precisely the prohibited pattern.

**Repair.** Extend the sweep to `M_ON`, and to the assignment chain of each
gate's predicate variable within the enclosing block.

---

## 2. What I could not break

I tried hard and moved nothing. Every number in the paper reproduces on a
route that shares no bookkeeping with the instrument's.

**The arena and the census** (my rebuild: declared cycle basis used directly as
coordinates, each walk solved into it over $\mathbb{F}_2$; no spanning tree, no
cotree): 13 links, 8 nodes, cycle rank 6; **16,168** reduced walks / **2,820**
closed / **364** based / **27** distinct cycle classes; **8** full-leg-only and
**18** realized-rule-only closed walks; the realized profile **82 / 86 / 90 /
106**; **89** distinct profiles, **96** multiset hits, **16** element-wise hits,
**3,906** order-4 connections with **96** of those hitting; most common profile
**[78, 90, 94, 102]** at **384**.

**K1 — the chain, recomputed with my own predicates.** 4,096 → **3,072** →
**768** → **192** → **12** → **6**, with the profile-hit column 96 / 96 / 24 /
12 / **6** / **6**. The last two steps the protocol names — **192 → 12 → 6** —
reproduce exactly. All six survivors carry the sorted profile, and I confirm
they are one relabelling orbit: their six element-wise profiles are the six
distinct permutations fixing 82.

**The candidates.** All nine non-C2 subset sizes (42, 1,728, 1, 6, 1,024,
1,024, 256, 2,304, 3,906), all nine in-subset hit counts, and all nine
violator-census counts (90 of 4,054; 0 of 2,368; 95 of 4,095; 90 of 4,090; 72
of 3,072; 72 of 3,072; 72 of 3,840; 48 of 1,792; 0 of 190) reproduce. The
automorphism layer reproduces too: |Aut| **2** rule-preserving and **16** full,
**1** and **8** distinct induced actions, C2a **4,096**, C2b **64**, C2c
**136**, with 0 hits for the latter two.

**The 11 declared violators (K5).** I rebuilt the lex-first, seed-free
construction independently — the lexicographically first single-coordinate
edit of the realized connection, in declared-basis order — and reproduced all
nine non-C2 violators, their profiles and their break verdicts, including the
one that is not obvious: **C3's is `SQ_FULL_1 := WD`**, and I confirm that
`:= W` and `:= D` genuinely fail to violate C3, so WD is the true lex-first.
Every declared violator breaks the profile. **C2a's missing violator is
legitimate**, not a gap the instrument could have filled: its subset is
provably the whole space (the rule-preserving group acts trivially on the
cycle space), so nothing violates it — and the paper names this twice, in §8
and in D7, rather than skipping it. Judged legitimate.

**The gauge layer.** 16,384 elements swept, **0** deviations, mis-convention
control moving the profile at **12,288** of 16,384, **27** masks, **442,368**
fresh evaluations. All independently reproduced.

**K2 at lower depth — the third instance re-run from its declaration.** I drove
the declared third instance (integer quaternion (5,1,2,3), rank-2
exchange-invariant preparation, transposition (1,5)) through **my own** directed
walk enumeration and **my own** raw matrix products, with my own permutation
extraction: **D fixes 45 of 81**, **4** distinct holonomies over 364 walks,
class counts **82 / 86 / 90 / 106** and element-wise 1:82, W:86, D:90, WD:106.
The exchange-equivariant control gives **D = I**, 81/81 fixed, **2** distinct
holonomies, **172 / 192**. I also verified D4's own arithmetic: $\psi_S$ has
Schmidt rank **2** and $\psi_G$ rank **3**, and $\psi_S$ is exchange-invariant.
Base G through the same independent route also returns 82 / 86 / 90 / 106.

**The hash pins (K5).** All pins fire on a **one-byte, semantically null**
change to the pinned file — a trailing space, which leaves the JSON valid JSON
and the Markdown valid Markdown. Each exits **1**, names the failed anchor,
prints got/want, and refuses every downstream measurement:

| pin | file corrupted | anchor that fired | exit |
|---|---|---|---|
| A01 | `v13/note-xba-crossbase-pin.md` | A01 pin sha256 | 1 |
| A02 | `v13/code/nt_transport_receipt.json` | A02 NT terminal receipt sha256 | 1 |
| A03 | `v13/code/gen_generality_receipt.json` | A03 GEN terminal receipt sha256 | 1 |
| A04 | `v13/review-gen-operator.md` | A04 frozen operator review sha256 | 1 |

Note the count: there are **four** hash-pinned sources, not three. The
protocol's K5 says "THREE hash pins", which counts the three carrying declared
mutants; A01 has no mutant, and I confirmed it live by file corruption. The
anchor mechanism is exit-1-only by construction (`anchor` calls
`_flush_and_exit(1)` inline) and I demonstrated it 4/4 empirically.

**Determinism and reproduction.** A fresh run of the instrument in a scratch
tree is byte-identical to the frozen `xba_crossbase_output.txt` apart from the
census block I suppressed for time. All 36 anchors traced to source; 28 gates
(24 must-pass, 4 disclosures) confirmed against the receipt's own gate list;
`never_falsified` EMPTY at denominator 23 with both denominators printed (23
and 19), as claimed; 35/35 mutants died. The exactness claim holds — I re-ran
the AST sweep: no float literal, no `float(` call.

**Three mutants reconstructed from prose (K5).** Written by me from the
paper's one-line descriptions, not invoked through `--mutant`:
`species-lax` ("drops one species clause from the derivation") → dies at
`XBA-CLAUSE-CHAIN` + `XBA-CANDIDATE-CHAIN-CONSISTENCY`;
`graph-drop-real2` ("drops the t=2 realized-rule link") → dies at A11 +
`XBA-WALK-AUDIT` (12 links, rank 5);
`violator-lax` ("builds a violator that does not violate") → confirmed by
direct reading that `viol_ok = not rec["pred"](PHI_R)` is False for every
candidate both bases satisfy, so `neg_ok` is False and
`XBA-NEGATIVE-CONTROLS` fires. Each lands on the gate the paper names.

**On K1's honesty question**, which the protocol asks me to check for scoping
rather than to adjudicate: the size-one triviality of C4's forcing is stated at
the claim in four separate places — §5 ("As a statement about subsets, forcing
at size one is trivial, and this paper says so rather than trading on it"),
§10, §11.4 and D2 — and the verdict is stated at C5, the naming-closed form
with six members. The scoping is carried everywhere I looked.

---

## 3. Assessment against the K5 checklist

| K5 item | verdict |
|---|---|
| 36 anchors traced | yes, all 36 located in source and matched to the receipt |
| three hash pins fire on corruption | yes — and a fourth (A01) that K5 does not count |
| exit-1-only, by deliberate breakage | yes, demonstrated 4/4 |
| 35 mutants audited, right gates, named kills | 35/35 died at the right gates; **named** kills fail for 13 (MINOR-1) |
| ≥3 mutants reconstructed from prose | yes, three; all land where the paper says |
| the 4 waiver-only gates legitimate | **no** — all four are analytically forced (MAJOR-3) |
| `never_falsified` EMPTY at 23, both denominators | yes, correct as printed |
| the cache refusal is real, not a never-consulted cache | **yes** — refusal genuine, gated, and I reconstructed the violation; but one clause is an identity and one prose claim is unmeasured (MODERATE-2) |
| 11 declared violators, lex-first, seed-free | yes, all reproduced independently |
| C2a's missing violator | legitimate, and named twice |
| verdict derived inside a gate + verdict-flip probe | **no** (MAJOR-1) |
| census routes genuinely independent; dropped-cell probe | **no** (MAJOR-2) |
| D8 both profile conventions printed and consistent | yes — multiset (96) and element-wise (16) both measured for every candidate, both in the receipt, and both reproduce independently |

---

## 4. Summary judgement

The **science reproduces completely.** I rebuilt the entire combinatorial layer
on an independent route and could not move a single number; K1's chain,
including the last two steps 192 → 12 → 6, and K2's third instance both
reproduce through machinery I wrote myself. The verdict
`XBA-SHARED-STRUCTURE-IDENTIFIED` is, on my own recomputation, the correct one.
No false number, no unsupported count, no unstated sampling; the paper's
scoping of the size-one triviality and of the admission-table residual is
carried at every claim I checked.

The **instrument, however, fails both clauses of the newest §13 addendum** — the
verdict is derived outside its gate with no computational falsifier (MAJOR-1),
and the "second route" is an algebraic identity with no cell-completeness gate
(MAJOR-2) — and four of its 23 must-pass gates are tautologies (MAJOR-3). Three
claims *about the instrument* are false as written: "both paths are exercised"
(§12), "returned on a second visit" (§9), and "every candidate's subset size
identical" (§9). One stated mechanism is wrong while its conclusion is right
(MINOR-2).

None of that changes a result. All of it is repairable in the instrument and
the prose; only the added mutants require a census re-run.

---

## 5. Repair list, ordered

1. Gate the verdict derivation from the measured counts; add a computation
   verdict-flip mutant. (MAJOR-1)
2. Demote `XBA-TREE-FLIP-TEST` to a disclosure or replace it with a genuinely
   independent route; add `set(sizes1) == set(sizes2)` and
   `len(sizes2) == len(CAND)`; disclose the C2 exclusion at the claim in §9.
   (MAJOR-2)
3. Reclassify the four forced gates as disclosures, or make them falsifiable;
   state the forcing argument for each in §12. (MAJOR-3)
4. Add a mutant that makes all four readings unreadable, or correct §12's
   "both paths are exercised". (MODERATE-1)
5. Read one primed cache key back and gate the returned value; demote
   `reserved_returns == primed`; drop the definite article in §9. (MODERATE-2)
6. Rename the freeze evidence key to
   `census_profile_evaluations_before_the_declaration` and add the one-sentence
   disclosure to §2/D1. (MODERATE-3)
7. Capture full anchor names in the census kill record. (MINOR-1)
8. Correct §2's frame-swap sentence. (MINOR-2)
9. Extend the mutant-exemption sweep to `M_ON` and to hoisted assignments.
   (MINOR-3)

---

## 6. Recomputation count

**114 independent recomputations**, itemised:

- **5** — the four frozen sha256 (verified twice) and a full byte-comparison
  re-run of the instrument in a scratch tree.
- **4** — the four hash pins, each fired by corrupting the pinned file.
- **16** — arena and census from my own rebuild: links, nodes, cycle rank,
  16,168, 2,820, 364, 27, 8, 18, the realized profile, 89, 96, 16, 3,906, 96,
  most-common-at-384.
- **14** — K1: six chain survivor counts, six chain hit counts, the
  all-survivors-carry check, the relabelling-orbit check.
- **36** — nine candidate subset sizes, nine in-subset hit counts, nine
  violator-census counts, nine lex-first violator constructions with profiles
  and break verdicts.
- **14** — the automorphism and gauge layers: |Aut| ×2, induced actions ×2,
  C2a/C2b/C2c subsets and their hits, the printed 13 labels → β, 27 masks,
  16,384 elements, 0 deviations, 12,288 mis-convention moves, 442,368
  evaluations.
- **12** — K2: my directed walk count, ψ exchange-invariance, two Schmidt
  ranks, and eight measured coordinates across the third instance, the
  equivariant control and the base-G cross-check.
- **9** — instrument probes and mutant re-runs: verdict-flip, dropped-cell,
  cache-garbage, two from-prose reconstructions, `memo-lax`, `gauge-head`,
  `basis-lax`, `base1-angle`.
- **4** — the 200-fold coordinate randomisation (one experiment), the AST
  call-site audit, the gate index/kind audit, the flip-test key-count audit.

---

# GRADE: ACCEPT-WITH-FIXES

The result stands. I attacked it on an independent route with 114
recomputations and moved nothing: the chain, the census, the candidates, the
violators, the gauge sweep and the third instance all reproduce exactly, and
the verdict is the one the measurements support. The pins are live, the
mutants all die, `never_falsified` is genuinely empty, and the cache refusal —
the item most likely to have been theatre — is real, gated, and survives the
violation I reconstructed against it.

What does not stand is the instrument's account of itself. The unit fails both
clauses of the §13 addendum it was built alongside: an ungated verdict with no
computational falsifier, and a "second route" that is one route wearing two
hats with no cell-completeness gate behind it. Four of its must-pass gates
cannot fail. Three sentences describe measurements the code does not make.
These are defects of the apparatus and of the prose, not of the physics, and
the repair list is nine items long and touches no result.

`ACCEPT-WITH-FIXES`, with items 1–3 required before the unit is called
terminal.
