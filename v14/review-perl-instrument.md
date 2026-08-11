# PER-L (paper 28) — K3 INSTRUMENT REVIEW

*Seat: INSTRUMENT-LENS (K3), protocol v14 ledger #218, launched #220.
Object at commit `9fcc081`.  Era note honoured: PER-L is the first unit
built entirely after E-22/E-23/E-24 were engraved, and nothing below is
excused by birth date.*

**GRADE: AWF** (accept with fixes) — at the heavy end of AWF.

Zero false computed numbers survive in the delivered artifacts.  Every
number I recomputed independently matched, including one the instrument
never computed at all.  The unit is byte-reproducible twice off-tree and
git-less, its seal manifest is total, its anchors have no phantom
consumers, real post-seal edits of sealed objects die, and its fenced-block
multiset gate is the strongest the campaign has shipped.

Against that, **six injections survive at exit 0** — one of them a full
delivery run that published and sealed two false numbers — and a set of
the unit's own statements about its instrument are false as written.
None of the findings moves a physics number; all ten MAJORs are liftable.

---

## 0. HASH DISCIPLINE

| object | declared (#218) | at start | at end |
|---|---|---|---|
| `v14/paper-28-perl.md` | `bd0298e2a482` | `bd0298e2a482` | `bd0298e2a482` |
| `v14/code/perl_exact.py` | `976d5b9e4ac8` | `976d5b9e4ac8` | `976d5b9e4ac8` |
| `v14/code/perl_output.txt` | `e4ff37a7a13e` | `e4ff37a7a13e` | `e4ff37a7a13e` |
| `v14/code/perl_receipt.json` | `54ec5a9e9b72` | `54ec5a9e9b72` | `54ec5a9e9b72` |
| `v14/note-perl-pin.md` (pin) | `973b160d52ed` | `973b160d52ed` | `973b160d52ed` |

All work in `scratchpad/perl-in/` on copied trees; git read-only.
Concurrent siblings' files (`paper-25-gdl.md`, `paper-27-smu.md`,
`gdl_*`, `smu_*`, and the live edits to `r4c_multi_exact.py`,
`r4dec_exact.py`, `paper-21-r4dec.md`, `paper-22-multi.md`) are
disclaimed — I touched none.  One repo write: this file.

`HEAD` moved under me during the review (`37523c6` → `7d63958`, sibling
commits by the orchestrator).  **All five PER-L objects are byte-identical
at the end of my work**, so every result below is measured against one
frozen object set; nothing was mixed.  I made no commits.

**Executions: 118.  Independent recomputations: ~360.**

---

## 1. WHAT HOLDS

**Byte-reproduction ×2, off-tree and git-less.**  Two provisioned trees
outside the repository with no `.git` anywhere, at `PYTHONHASHSEED=0`
and `PYTHONHASHSEED=12345`.  Both exit 0; **both artifacts byte-identical
to the committed objects** — transcript `e4ff37a7a13e`, payload
`54ec5a9e9b72`, 10407 + 133569 bytes, 41 sealed objects.  #91 and the
v10-layer hash-seed concern are discharged empirically.

**The loud clean abort (#91), twice.**  A bare copy carrying only
`perl_exact.py` names all ten absent sources, prints "Nothing was
written", exits 1, and creates nothing.  A copy missing exactly one
source names that one and does the same.

**No subprocess, no git, stdlib only.**  Imports: `ast`, `hashlib`,
`json`, `os`, `re`, `sys`, `fractions`, `itertools`.  No `subprocess`,
`os.system`, `popen`, socket, or `git` anywhere in 3855 lines.

**The seal manifest is TOTAL (#148), verified independently.**  51
published keys, 40 sealed roots across 41 seal rows, 12 declared-unsealed
entries with reasons.  Recomputed from the source's `DECLARED_UNSEALED`
and the receipt's key set: **no published key is both unsealed and
undeclared**, and no declared-unsealed entry is dead.

**No phantom consumers (the paper-22 lesson).**  All 9 verbatim anchors
name a `consumer_gate` and **all 9 exist in the published ledger**; all
41 seal rows name a `sealed_at_gate` and **all 41 exist**.  The 60-char
verbatim floor is evaluated, and presence is tested with #125
normalisation on both sides.

**The seal is NOT inert against real pollution.**  Unlike paper-22's
cache gate, I edited *actual sealed objects* in place after their seals
were taken — `S["counts"]["arenas"] = 999` and
`S["band_law"]["parent_row"] = [9]`.  **Both die at `G-SEAL-COMPLETE`.**
The #119 gate-to-disk mechanism is sound.

**Anchor perturbation: 19/19 on target.**  4 byte anchors →
`G-SOURCES-PINNED`; 6 path-value → `G-PATH-VALUE-ANCHORS`; 9 verbatim →
`G-VERBATIM-ANCHORS`.  Artifacts unchanged.

**CLI contract (#82): 20/20.**  Unknown flags, `-h`, `--help`,
`--list`, `--list-mutants`, `--mutants`, bare positionals, case variants
and `--flag=value` forms all exit 2.  **Arity is real**: `--mutant` and
`--break-anchor` with no argument exit 2 ("needs a NAME");
`--mutant --selftest` is rejected as an unknown mutant name rather than
silently swallowing the flag; `--mutant ""` exits 2.  The no-list-flag
contract is usage-disclosed — the usage line enumerates exactly the five
accepted flags.  `--selftest` corrupts `A-R4-PAPER` in memory, dies at
`G-SOURCES-PINNED`, exits 1 and **writes nothing**, verified by hashing
both artifacts before and after the whole battery.

**E-22 fences by MULTISET — four ways, all die.**  The paper carries the
verdict fence twice.  Corrupting only the first copy dies; corrupting
only the second dies; appending a forged third dies; appending an *exact*
third dies.  A containment gate would have passed the first two.

**Independent recomputation of the physics** (my own code, no helper
shared with the instrument):

| object | result |
|---|---|
| §6 locality table, 9 rows × 5 fields | 9/9 match |
| §7 band table, 3 widths (admitted + predicted) | 3/3 match |
| §4 diameter and interior radii at L = 4, 6, 8 | 3/3 match |
| §8 persistence table: each verdict against its own three cells | 24/24 consistent |
| 1 952 424 maps = 3·(5·25³+25⁴) + 25³+7³+19³+25⁴+7⁴+19⁴ | exact |
| 2 940 axis-and-lag objects = 9·16 + 19·36 + 33·64 | exact |
| the DDS criterion at ord(a) = 2, 3, 4, 5 | "fails exactly at 2, 3, 4" confirmed |
| the 21 paper claims, verbatim under #125 normalisation | 21/21 present |
| the paper's numerals, by my own scanner | **83 — exactly the published count** |
| **the width-1 absence half**, exhaustive over all 512 subsets of the ball at every L in 2…14 | **TRUE at every size** |

That last row matters: it is the claim the instrument asserts but never
computes (MAJOR-1).  It is true.  It is simply not measured.

---

## 2. FINDINGS

### MAJOR-1 — the band's one *forced* half is never computed, and its window guard sits outside both ledgers

§7 says the absence half "is forced only at width 1, **where the
difference-doubled subset census over the nine-offset ball is exhaustive
over all of its subsets**".  §11 inventories the DECLARED-WINDOW as
covering "every arena declared here **and the radius-one ball**".  The
receipt's choice inventory says the census is exhaustive at |S| ≤ 12 "and
the absence half of the band law is **claimed only where it runs**".

`doubled_subsets()` is called at exactly one site — line 1798, the
18-arena loop, on offset sets of size 3 and 4.  **It is never called on
any ball, at any width.**  The band is computed entirely from
`doubled_pair()` (line 1189), which finds only difference-doubled subsets
of size 2 (pairs differing by an involution).  Difference-doubled subsets
of size ≥ 3 with no involution pair exist — the control rung's own
order-3 coset is one — so `doubled_pair` is not a decision procedure for
DDS-freeness.  `band_law` carries no ball-level census; its keys are
`rows`, `by_width`, `law`, `parent_row`, `one_sided_at_width_above_one`.

I ran the missing computation.  Over all 512 subsets of the nine-offset
ball at every L in 2…14, "a difference-doubled subset exists" and "an
involution pair exists" agree at every size — **the claim is true**.  It
is asserted, not measured; no gate binds it; and the receipt's sentence
about where the census runs is **false as written**.

Related: the window guard `G-DDS-WINDOW` is a real hard stop — lowering
`DDS_SUBSET_WINDOW` to 2 kills the run with that name (CI-08) — but it
appears in **neither the gate ledger (60 rows) nor the waiver ledger (62
rows)**.  `G-WAIVERS-VERIFIED`'s claim that the ledger "is built over
every gate the run will reach" is false for it: a named gate the run can
reach carries no row, no falsifier and no forcing.

*Repair R-PERL-K3-1:* run `doubled_subsets(ball(L, 1), L)` for every L in
`BAND_SIZES`; publish it under `band_law`; add
`G-BAND-ABSENCE-FORCED-AT-WIDTH-1` requiring, **per size** (#87), that
"no difference-doubled subset of the radius-1 ball" and "not admitted"
agree.  Add `G-DDS-WINDOW` to `REMAINING_GATES`/`FORCINGS` so the waiver
ledger covers it.  Reword the choice-inventory `why` to what runs.

### MAJOR-2 — a seal window publishes and seals two false numbers at exit 0

`S["totals"]` is complete at line 3312 and gated at `G-TOTALS-REDERIVED`
(3323), but `SEAL-TOTALS` is bound to `G-PAPER-COVERAGE-FINAL` (3722) —
**the last gate of the run**, ~400 lines and an entire 48-mutant sweep
later.  #148 is explicit: "seals taken at the final gate are
non-compliant."

Demonstrated (CI-09, a full delivery run): inserting
`S["totals"]["sources"] = 99` and `S["totals"]["path_value_anchors"] = 999`
*immediately after `G-TOTALS-REDERIVED` passes* gives —

```
EXIT=0
PUBLISHED totals: {"claims": 21, "gates": 61, "gates_in_receipt": 60,
 "mutants": 48, "numerals": 83, "path_value_anchors": 999, "seals": 41,
 "sources": 99, "verbatim_anchors": 9}
seal row: {"seal": "SEAL-TOTALS",
 "sealed_at_gate": "G-PAPER-COVERAGE-FINAL", "sha256_12": "f87a5ab9acf3"}
```

A clean run, both artifacts written, the corrupted values **sealed and
vouched** — the seal digested the corruption because it was taken after
it.  This is the #119/#148 failure mode in its pure form.

`G-TOTALS-REDERIVED` is also near-vacuous: its predicate is
`S["totals"]["mutants"] == len(MUTANTS) and S["totals"]["seals"] ==
len(SEALED_PATHS)`, comparing two dict entries to the expressions that
produced them three lines above.  Independently confirmed (CI-05):
replacing `"sources": len(SOURCES)` with the typed literal `9`
**survives at exit 0**.  The gate binds 2 of 9 totals keys, so its claim
— "the published totals are re-derived from the objects that produce them
rather than typed" — is false of seven.

*Repair R-PERL-K3-2:* move `SEAL-TOTALS` to `G-TOTALS-REDERIVED`, and
widen that gate to re-derive **every** totals key from its source with a
per-key predicate (#87).  The other wide windows are acceptable and
should be recorded as such: `SEAL-COUNTS` spans 664 lines with no
intervening write; `SEAL-GATES` and `SEAL-COVERAGE` are forced to the
final gate because their values only exist there.

### MAJOR-3 — "STRUCTURAL" is an unconditional `else`, and a gate that binds nothing passes

The waiver ledger's third bucket is a default branch: any gate that is
neither a mutant target nor a `FORCINGS` key is labelled STRUCTURAL and
handed a boilerplate forcing ("a rebuild identity: it compares two
independently computed objects…") **with no check that it is one**.

Demonstrated (CI-04): adding

```python
LD.gate("G-K3-INJECTED-VACUOUS",
        "a gate that binds nothing at all", True, "vacuous by construction")
```

**survives at exit 0.**  It is auto-classified STRUCTURAL,
`G-WAIVERS-VERIFIED` passes, and `G-GATES-CLOSED-AS-PREDICTED` passes
because the prediction `len(LD.rows) + 11` absorbs the extra row.

Auditing all 7 STRUCTURAL rows:

| gate | earned? |
|---|---|
| `G-DISPERSION-REPRODUCES-THE-PARENT` | **YES.** Compares this unit's rebuilt cells / moving / static / distinct against four independent path-value anchors from the parent's receipt. A genuine two-route identity. |
| `G-STAGES-DECLARED` | **NO — mislabelled.** Its predicate is the presence of `VB-PIN-STAGES`, a real binding falsifiable by `--break-anchor VB-PIN-STAGES` (fired; it dies). It belongs in WAIVED with that as its forcing, not in a bucket claiming a rebuild identity. |
| `G-ARENA-DECLARED` | **NO — redundant.** `list(LADDER) == [4,6,8]` is literal-vs-literal; the other conjuncts re-test PV-ALPHABET and PV-D, already bound at `G-PATH-VALUE-ANCHORS`. It never inspects `control_rung`, `link_set`, `widths`, `band_sizes` or the generalisation rule — the parts of the declaration that carry weight. |
| `G-NOT-EXECUTED-EMPTY` | **NO — unreachable.** The gate *is* reactive (CI-06 makes it fire), but `NOT_EXECUTED` is declared at line 320 and **appended to nowhere in 3855 lines**. No program input can fail it. |
| `G-WAIVERS-VERIFIED` | **NO — unreachable.** Reactive (CI-07 makes it fire), but `unguarded` filters for FALSIFIABLE rows lacking `falsifier` and WAIVED rows lacking `forcing`, and the loop three lines above sets both unconditionally. |
| `G-CHOICES-INVENTORIED` | **NO — unreachable.** `all("class" in c and "fibre" in c …)` and `any(class == "DECLARED-WINDOW")` over a literal list in which every entry has both keys and one has that class. |
| `G-TOTALS-REDERIVED` | **NO — see MAJOR-2** (CI-05 survives). |

1 of 7 earned; 2 mislabelled but binding; 4 unfailable on any input the
program can produce.

*Repair R-PERL-K3-3:* delete the `else` default.  A gate enters STRUCTURAL
only via an explicit registry naming its two independently computed sides.
Re-home `G-STAGES-DECLARED` to WAIVED with the break-anchor as its
forcing.  Delete `G-NOT-EXECUTED-EMPTY` or give `NOT_EXECUTED` a writer.

### MAJOR-4 — E-23 is implemented as switch *existence*, not description-vs-code

E-23: "A falsifier's published description … must be verified against its
code — a description-inverted mutant is a false waiver wearing a green
badge."  `falsifier_descriptions()` searches for the literal string
`mut("NAME")` and records `switch_present`; the recorded
`guarded_source_sha256_12` (a digest of the next 240 characters) is
**never compared to anything**.  Nothing relates description text to
branch behaviour.

Demonstrated (CI-03): inverting a published description — MUT-ALPHABET's
"drops one element from the rebuilt coefficient alphabet" → "**adds** one
element to…", leaving the code `A = A[:-1]` untouched — **survives at
exit 0**.

The self-reference is the sharpest part: `MUT-DESCRIPTION` is published as
"inverts one published mutant description relative to its code", and its
branch is `fd[0]["switch_present"] = False`.  It inverts no description.
The one mutant whose job is to prove E-23 is itself misdescribed, and the
gate it targets could not have caught it.

Manual audit of all 48 descriptions against their branches — five
mismatch, one imprecise:

| mutant | published description | what the branch does |
|---|---|---|
| `MUT-DESCRIPTION` | "inverts one published mutant description relative to its code" | sets `switch_present = False`; inverts nothing |
| `MUT-SEAL-BROKEN` | "edits a sealed object after its gate-time digest was taken" | sets `broken = ["SEAL-COUNTS"]`; edits no object. *(The gate itself is sound — CI-01/02 show real edits die — only the description overstates.)* |
| `MUT-ALT` | "breaks the alternating certificate **by moving one predicted order**" | sets `alternating_certified = False`; no order moves |
| `MUT-BAND` | "moves one admitted size **out of** the measured band" | sets `ok = True` at r = 2, L = 7 — it adds an inadmissible odd size *in* |
| `MUT-PAPER-SPAN` | "adds an unlicensed numeral **inside an inline code span**" | `sn = sn \| {"424242"}`; the paper is never touched |
| `MUT-EXTRA-READ` | "appends an undeclared path **to the runtime read list**" | appends to `extra`, the undeclared-reads list, not to `READS` |

The other 42 are accurate.

*Repair R-PERL-K3-4:* pin `guarded_source_sha256_12` in the frozen
`MUTANTS` table and require the live branch's digest to equal it, so that
editing code without editing the description (or the reverse) dies.
Reword the six rows.  Give `MUT-DESCRIPTION` a body that actually inverts
a description string.

### MAJOR-5 — the control rung is a fourth lattice size that the declared scope excludes and the paper never names

`CONTROL_RUNG = 3`.  546 174 of the 1 952 424 scanned maps — 28 % of the
unit's whole scan — are at L = 3, and the headline
"REGISTERED-54-REPRODUCED" comes from there.  The verdict's scope segment
reads `SCOPE=D=2;RUNGS=L-IN-{4,6,8};…`, which **excludes it**, and the
paper says "the control rung" seven times without ever stating that it is
L = 3.  §15 requires the declared arena to match every coordinate; a
reader cannot recover this one from the paper at all.

*Repair R-PERL-K3-5:* render the scope segment from `LADDER` and
`CONTROL_RUNG` instead of typing it —
`RUNGS=L-IN-{4,6,8}+CONTROL-RUNG-L-3` — and name L = 3 in §3.4's first
sentence and in §11's control-alphabet bullet.

### MAJOR-6 — the verdict's most contested segment is a typed literal, and the "independent comparator" binds one number by substring

`build_verdict` emits four segments with **no format specifier at all**:

- `SCALE=…WIDTH-1={4};WIDTH-2={6,8};WIDTH-3={8,10,12};PRESENCE-CONSTRUCTIVE-ABSENCE-FORCED-ONLY-AT-WIDTH-1` — the band, the paper's own nominated weak point, typed;
- `BREAKS=…INTEGER-VELOCITIES-FAIL-AT-L-6(SPEED-3/2-ON-AN-ORDER-2-AXIS);EIGENPHASE-LATTICE-TRANSFORMS-Z/lcm(8,L)` — typed;
- `GLOBAL-SUPPORT-IS-THE-VOLUME-16;36;64` inside FINGERPRINT — typed, while the *paper's* prose version of the same triple is rendered from `global_stencil`;
- `RUNGS=L-IN-{4,6,8}` inside SCOPE — typed (MAJOR-5).

One pseudo-derivation: "ALL-**64**-ANTIDIAGONAL-COINS" is computed as
`S["counts"]["coins"] // 10` — 640 // 10.  The antidiagonal sector count
lives at `coin_sectors["sectors"]["ANTIDIAGONAL"]` and is not consulted;
the two agree by coincidence.

`G-VERDICT-RECONSTRUCTED` claims "the head and **every segment key** …
are re-derived … by a comparator that shares no literal and no helper
with the builder".  Its predicate:

```python
ok = (rh == S["verdict"]["head"]
      and S["verdict"]["string"].startswith(rh + "<")
      and str(rparts[3]) in fp.get("CONTROL", "")
      and set(fp) == {ten typed segment names})
```

`reconstruct_verdict` computes seven parts; **six are discarded**.  The
single comparison is `"54" in fp["CONTROL"]` — a *substring* test, so
`154` or `540` would also satisfy it.  The remaining check compares ten
segment **key names** against a typed set: names, not values.  The
verdict body is bound at exactly one number.

Demonstrated (CI-10): widening `WIDTHS` to `(1, 2, 3, 4)` — which leaves
`G-BAND-LAW`'s per-width equality intact, since admitted = predicted =
`[10, 12, 14]` at r = 4 — **runs to exit 0** while the head continues to
assert a three-width band and the unmodified paper continues to verify.
A run that measured four widths publishes a head describing three.

*Repair R-PERL-K3-6:* render SCALE from `band_law["by_width"]`, BREAKS
from `velocity_census` and the eigenphase rows, the global-support triple
from `global_stencil`, the antidiagonal count from
`coin_sectors["sectors"]`, and SCOPE from `LADDER`/`CONTROL_RUNG`.  Make
the comparator compare **all seven** reconstructed parts against the
parsed segments by equality, not membership.

### MAJOR-7 — E-24: the fraction census is self-selected, and three published fractions are unstamped

`declared_fractions` is a hand-written two-row literal.
`G-FRACTIONS-STAMPED` checks that those two rows carry `COUNTING-ONLY`
and **never scans the paper or the verdict**, so it cannot discover an
unstamped fraction — only confirm the ones volunteered.  `MUT-FRACTION`
appends to the same self-selected list, testing the predicate and not the
denominator (#34).

Scanning the object for fraction-shaped constructions:

| construction | where | stamped? |
|---|---|---|
| `13 of 18` | §3.2, inline span | **yes**, and the paper says so |
| `13-OF-18-ARENAS-DDS-FREE` | verdict, LAW segment | yes (same row) |
| `18-OF-18-ARENAS` | **verdict head**, SIDON segment | **no** |
| `10 of them` (= 10 of the 18 arenas) | §3.2 | **no** |
| `0-OF-25` | verdict, CONTROL segment | **no** — and it is not a fraction: it means "0 non-monomial over the 25-element alphabet", but the hyphenation reads as a ratio |

`3 of 18` is declared but never appears in the paper (harmless
over-declaration).  §10's "the two fractions this unit publishes are
stamped COUNTING-ONLY" is inaccurate.

*Repair R-PERL-K3-7:* build `declared_fractions` by **scanning the
rendered paper text and the verdict string** for `\d+ of \d+`,
`\d+-OF-\d+` and `\d+ of them`; require every hit to be stamped or
measure-declared; gate the coverage (found = stamped).  Rewrite `0-OF-25`
as `0-NON-MONOMIAL-OVER-THE-25-ELEMENT-ALPHABET`.

### MAJOR-8 — the head's `18-OF-18` counts fifteen vacuous confirmations

`sufficiency_holds` is the material implication
`(not r["sidon"]) or r["monomial_only"]`.  At 15 of the 18 arenas the
antecedent is false, so it holds vacuously.  The prediction's sufficiency
direction is substantively tested at exactly **three** arenas — LINK at
L = 4, 6, 8 — which is what `counts["arenas_sidon"] = 3` records and what
§3.2's honest sentence already says ("at the anchored link stencil, which
is Sidon at every rung, the exhaustive scan finds no non-monomial unitary
at all").  The headline number is the vacuous one.

*Repair R-PERL-K3-8:* publish `sufficiency_substantive: 3` and
`sufficiency_vacuous: 15`; change the head to
`SUFFICIENCY-HOLDS-AT-3-OF-3-SIDON-ARENAS(VACUOUS-AT-THE-OTHER-15)`; add
the same clause to §3.2.

### MAJOR-9 — 27 of the paper's 69 table rows are unbound, including the band table

`paper_tables()` renders exactly two tables: the 24-row persistence table
and the 18-row arena table (42 rows, matching the published
`table_rows: 42`).  Unrendered: §3.4's control table (6 rows), §4's VMAX
table (3), §5's profile table (6), §6's locality table (9) and **§7's
band table (3)**.  §10 scopes the guarantee honestly to two tables, but
E-22 says "Tables render as claims", and the one table the paper itself
nominates for attack is outside the guarantee.

Demonstrated: forging `| 2 | [6, 8] | [6, 8] |` → `| 2 | [6, 8, 10] |
[6, 8] |` **survives at exit 0** (INJ-07), as does
`| 3 | [8, 10, 12] | [8, 10, 12] |` → `[8, 10, 14]` (INJ-08).  Both
inserted numerals are licensed — `10` by the 0–24 whitelist, `14` by
`band_sizes` — and no table gate covers the rows.

*Repair R-PERL-K3-9:* extend `paper_tables()` to render all five
remaining tables from `fourth_direction_control["control_rung_rows"]`,
`vmax_census` + `interior_radii`, `gauge_profile`, `locality_windows` and
`band_law["by_width"]`.

### MAJOR-10 — E-22 inline-span coverage is defeated by the 0–24 whitelist

E-22: "a backticked numeral is a claim like any other".  The spans *are*
scanned in their own right — but against the same licence set, whose
`STRUCTURAL` component admits **every integer 0–24** unconditionally.

Demonstrated (INJ-10): the paper's one inline span carrying a measured
value, `` `13 of 18` `` — the DDS-free count, and the unit's own
E-24 exhibit — forged to `` `14 of 18` `` **survives at exit 0**.
`14` is inside the whitelist; the span is not a rendered claim; nothing
else covers it.  INJ-11 (`` `v14/code/perl_exact.py` `` →
`perl_exact9.py`) also survives, showing the span gate is numeral-only
and never checks span content.

Overall, **24 of the paper's 83 numerals are licensed by range alone**,
independently of the receipt; only 5 (`23`, `91`, `119`, `125`, `148`)
need the whitelist for the reason its comment gives.  The honest coverage
denominator is 59/83.

*Repair R-PERL-K3-10:* restrict `STRUCTURAL` to numerals actually needed
— section and rung labels computed from the paper's heading lines, plus
the cited engraving numbers — rather than a typed 0–24 range; and render
`13 of 18` as a claim from `declared_fractions[1]["value"]`.

### MINOR-11 — post-write corruption is caught, but the artifact is left promoted

Verified with a real injection after `os.replace`: the post-write check
fires — `GATE FAILED: G-ARTIFACT-INTEGRITY :: the artifacts on disk
differ from the gate-time seal (the payload digest)`, exit 1 — so a
corrupt artifact can never be silently delivered.  But there is no
rollback: the receipt on disk went from `54ec5a9e9b72` to `c2b21e1eca6d`
(133 595 bytes) and **stayed there**.  §10's "The delivery run is the
only writer, and a failing run writes nothing at all" is false for this
path.  (Same class as paper-22's MINOR-5.)

*Repair:* copy the pre-existing artifacts aside before `os.replace` and
restore on post-write failure; or scope §10's sentence explicitly.

### MINOR-12 — one seal is taken outside the ledger mechanism

`Ledger.gate` carries the comment "a value is digested AT THE MOMENT ITS
GATE PASSES, **here and nowhere else.  Nothing is sealed in a late
take.**"  `finish_receipt` calls `SEAL.take("SEAL-MUTANTS", S)` directly.
In execution order the take follows `G-MUTANTS-ON-TARGET` by one line, so
the seal is tight and the manifest's `sealed_at_gate` is accurate — the
defect is the code's statement about itself, which a reader of the seal
mechanism would rely on.

### MINOR-13 — `--verify-paper` never reaches the final coverage gate

The declared paper harness exits 0 immediately after `build_receipt`, so
`G-PAPER-COVERAGE-FINAL` — the pass that exists to cover §10 itself —
runs only in the delivery run.  Its in-run twins carry the falsifiers, so
nothing is unguarded, but the flag a reviewer is invited to use is
strictly weaker than the delivery path.  Worth a sentence in §10.

### MINOR-14 — a signed velocity is published under the key `speed`

`velocity_census[1]["witness"]["speed"] = "-3/2"`, with a separate
`"direction": 1`.  The paper and verdict report `3/2`.  The magnitude is
right; the key name is not.  *Repair:* rename to `velocity`, or publish
`speed` as its absolute value alongside.

---

## 3. THE INJECTIONS

Artifacts hashed before and after every battery.  **Unchanged
throughout**, except the one battery designed to write (CI-PW / CI-09).

| # | injection | expected | result |
|---|---|---|---|
| INJ-01 | corrupt **only the first** of the two identical verdict fences | die | exit 1, `G-PAPER-FENCED-MULTISET` |
| INJ-02 | corrupt **only the second** fence | die | exit 1, `G-PAPER-FENCED-MULTISET` |
| INJ-03 | append a **forged third** copy of the fence | die | exit 1, `G-PAPER-FENCED-MULTISET` |
| INJ-04 | append an **exact third** copy (multiset 2→3) | die | exit 1, `G-PAPER-FENCED-MULTISET` |
| INJ-05 | persistence table: `VMAX 2 3 4` → `2 3 5` | die | exit 1, `G-PAPER-TABLES-AS-CLAIMS` |
| INJ-06 | persistence table: `interior radii … TRANSFORMS` → `PERSISTS` | die | exit 1, `G-PAPER-TABLES-AS-CLAIMS` |
| INJ-07 | **band table**: width-2 admitted `[6, 8]` → `[6, 8, 10]` | die | **SURVIVES exit 0 — MAJOR-9** |
| INJ-08 | **band table**: width-3 admitted `[8, 10, 12]` → `[8, 10, 14]` | die | **SURVIVES exit 0 — MAJOR-9** |
| INJ-09 | arena table: L=4 AXIS-0-1 non-monomial `48` → `47` | die | exit 1, `G-PAPER-TABLES-AS-CLAIMS` |
| INJ-10 | **inline span** `` `13 of 18` `` → `` `14 of 18` `` | die | **SURVIVES exit 0 — MAJOR-10** |
| INJ-11 | **inline span** `` `…/perl_exact.py` `` → `perl_exact9.py` | die | **SURVIVES exit 0 — MAJOR-10** |
| INJ-12 | prose numeral `1952424` → `1952425` | die | exit 1, `G-PAPER-CLAIMS` |
| INJ-13 | claim: "fails at 10 of them" → "fails at ten of them" | die | exit 1, `G-PAPER-CLAIMS` |
| INJ-14 | delete the TABLE segment from the verdict block | die | exit 1, `G-PAPER-FENCED-MULTISET` |
| CTRL | the pristine paper | pass | exit 0; 83 numerals, 21 claims, 15 spans, 2 fences, 42 table rows, 0 unlicensed, 0 polarity failures |
| CI-01 | **real** post-seal edit of `counts/arenas` → 999 | die | exit 1, `G-SEAL-COMPLETE` |
| CI-02 | **real** post-seal edit of `band_law/parent_row` | die | exit 1, `G-SEAL-COMPLETE` |
| CI-03 | invert a published falsifier description (MUT-ALPHABET) | die | **SURVIVES exit 0 — MAJOR-4** |
| CI-04 | add a gate that binds nothing | die | **SURVIVES exit 0 — MAJOR-3** |
| CI-05 | type a total: `"sources": len(SOURCES)` → `9` | die | **SURVIVES exit 0 — MAJOR-2** |
| CI-06 | `NOT_EXECUTED` non-empty (reactivity probe) | die | exit 1, `G-NOT-EXECUTED-EMPTY` — reactive, but no writer exists |
| CI-07 | a FALSIFIABLE waiver row with no `falsifier` | die | exit 1, `G-WAIVERS-VERIFIED` — reactive, but unreachable by construction |
| CI-08 | `DDS_SUBSET_WINDOW` 12 → 2 | die | exit 1, `G-DDS-WINDOW` — a hard stop, but in neither ledger |
| CI-09 | edit `totals` inside the seal window, **full delivery run** | die | **SURVIVES exit 0; false numbers PUBLISHED and SEALED — MAJOR-2** |
| CI-10 | widen `WIDTHS` to (1,2,3,4) — does the head follow? | head moves | **exit 0, head unmoved — MAJOR-6** |
| CI-PW | corrupt the receipt **after** `os.replace` | die, nothing left | exit 1 **but the corrupted file stays promoted — MINOR-11** |
| BARE | copy with only `perl_exact.py` | loud clean abort | exit 1, all 10 named, nothing written |
| PART | copy missing `r5_gauge_receipt.json` | loud clean abort | exit 1, that one named, nothing written |
| ANCH | `--break-anchor` × 19 (4 byte / 6 path-value / 9 verbatim) | die at class gate | **19/19 on target**, artifacts unchanged |
| CLI | 20 hostile argv forms + `--selftest` | exit 2 / exit 1 | **20/20 exit 2**; selftest exit 1 writing nothing |

---

## 4. THE 48-MUTANT SWEEP, OUTSIDE THE HARNESS

Each mutant run as a **separate process** (`--mutant NAME`) in a
provisioned off-tree copy; each exit code and dying gate compared against
the frozen `MUTANTS` registry parsed from source — never against the
in-run report.

**48 declared, 48 killed, 48 killed by their declared target, 0
survivors, 48 distinct gates hit — 48/48 ON TARGET.**  Every mutant
exits 1 with `MUTANT SURVIVED` absent from its transcript.  The 48
targets are 48 distinct gate ids, so no gate carries two falsifiers and
none is covered by a neighbour's.

**Artifacts hashed before and after the whole sweep: unchanged.**  The
in-run report (`mutants: 48 declared, 48 killed, 48 killed by their
declared target`) is therefore confirmed from outside the harness, which
is the point of running it there — the in-run sweep and its adjudicator
`G-MUTANTS-ON-TARGET` share the process, the state dict and the mutant
switch with the thing they are measuring.

Two qualifications the raw 48/48 does not carry, both developed above:

- Six of the 48 published *descriptions* do not match the branches they
  guard (MAJOR-4), so "killed by its declared target" certifies the
  wiring, not the meaning.  `MUT-SEAL-BROKEN` and `MUT-PAPER-SPAN` in
  particular fake their gate's *input* rather than perturbing the object
  the description names — for `MUT-SEAL-BROKEN` I re-ran the honest
  version by hand (CI-01/CI-02) and the gate holds; for
  `MUT-PAPER-SPAN` the honest version (INJ-10) **survives**.
- The sweep's denominator is the gates that have mutants.  62 gates are
  ledgered; 48 are FALSIFIABLE, 7 WAIVED, 7 STRUCTURAL — and four of the
  STRUCTURAL seven cannot fail on any input (MAJOR-3), while
  `G-DDS-WINDOW` is reachable with no ledger row at all (MAJOR-1).

---

## 5. ERA COMPLIANCE — FULL STANDARD, NO EXCUSES

| engraving | verdict |
|---|---|
| **E-22** inline spans | **FAIL.** Spans are scanned, but against a licence set that whitelists 0–24; the one span carrying a measured value is forgeable at exit 0 (MAJOR-10). |
| **E-22** blocks by MULTISET | **PASS — strongest in the campaign.** Four injections, all die; a containment gate would have passed two. |
| **E-22** tables render as claims | **PARTIAL.** 42 of 69 rows; the band table is unbound and two forged band rows survive (MAJOR-9). |
| **E-23** falsifier honesty | **FAIL.** Switch existence, not description-vs-code; an inverted description survives at exit 0; 5 of 48 descriptions mismatch their branches; the E-23 mutant is itself misdescribed (MAJOR-4). |
| **E-23** every row falsifiable or waived-with-forcing | **FAIL.** The third bucket is an unconditional `else`; a vacuous gate is auto-blessed (MAJOR-3); `G-DDS-WINDOW` has no row at all (MAJOR-1). |
| **E-24** measure-relativity | **PARTIAL.** Two fractions correctly stamped; the census is self-selected and three published fraction-shaped constructions are unstamped, two of them in the head (MAJOR-7). |
| **#119 / #148** gate-to-disk seal, total manifest | **PASS on the mechanism** (real edits die; manifest total, independently verified) **with one exploited non-compliant window** (MAJOR-2). |
| **#125** text gates as written | **PASS.** Whitespace and markdown-prefix normalisation both sides; 60-char floor evaluated. |
| **#91** no moving refs, off-tree, git-less | **PASS.** Byte ×2 across two hash seeds; no subprocess; loud clean abort twice. |
| **#82** CLI contract | **PASS.** 20/20 hostile argv, real arity, real selftest, mutant harness with artifacts unchanged. |
| **#87** gates bind objects | **MOSTLY PASS.** Per-object predicates throughout the physics gates; `G-CHOICES-INVENTORIED` and `G-TOTALS-REDERIVED` are aggregate-shaped and unfailable. |
| **#34** honest denominators | **FAIL twice.** `18-OF-18` counts 15 vacuous confirmations (MAJOR-8); the fraction census has no denominator (MAJOR-7). |
| **#20** paper coverage incl. fences | **PASS on fences**, see MAJOR-10 on the whitelist. |
| **§15** declared arena, match every coordinate | **FAIL.** The control rung L = 3 is measured, headlined, excluded from SCOPE and never named in the paper (MAJOR-5). |
| heads DERIVED, never typed | **FAIL.** Four verdict segments are pure literals; the comparator binds one number by substring; a run measuring four widths publishes a three-width head (MAJOR-6). |

---

## 6. THE SEAM RULING

The seam this seat rules on is between **what the instrument measures**
and **what the object says it measures**.

PER-L's measurements are sound.  Every number I recomputed independently
— 83 numerals, 21 claims, 9 locality rows, 3 band widths, 3 radii rows,
24 persistence verdicts, the totals 1 952 424 and 2 940, and even the
width-1 absence half the instrument never ran — came out exactly as
delivered.  The physics survives this seat intact, and so does every
headline.

What does not survive is a set of **self-descriptions**.  §11 says a
census covers the radius-one ball; it does not.  §10 says a failing run
writes nothing; one path writes and leaves the corruption promoted.  §10
says the two published fractions are stamped; five are published and
three are not.  §10 says falsifiers follow E-23; an inverted description
survives at exit 0.  `G-VERDICT-RECONSTRUCTED` says every segment key is
re-derived by an independent comparator; one number is, by substring.
`G-TOTALS-REDERIVED` says the totals are re-derived rather than typed;
seven of nine are not, and a typed one survives.  The STRUCTURAL forcing
says the gate compares two independently computed objects; four of seven
compare an object to itself.  `G-WAIVERS-VERIFIED` says the ledger covers
every gate the run will reach; one named gate has no row.

That is the seam: **PER-L measures honestly and describes its instrument
optimistically.**  The pattern is uniform — wherever the unit made a
claim *about its own machinery* rather than about the lattice, the claim
outran the code.  Six injections survive at exit 0 and every one of them
lives on that side of the seam; none touches a measurement.

On the era's own terms, with no birth-date excuse available, that is
AWF at the heavy end: ten liftable MAJORs, no false physics number, and
one repair pass — R-PERL-K3-1 through -10 — between this unit and A.

---

*K3 INSTRUMENT — PER-L (paper 28).  Objects verified unchanged at start
and end.  118 executions, ~360 independent recomputations.*
