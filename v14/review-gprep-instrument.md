# Γ-PREP (paper-11) — HOSTILE REVIEW, LENS K5 (THE INSTRUMENT)

**Reviewer lens:** K5 — the CLI audit first at the #82 contract
minimum; then gates-vs-mutants coverage at #34, the waiver census,
verbatim anchors at #62, comparator independence at the #82-strengthened
standard, the feed-forward surface, the three-way sweep and
byte-identity.

**Grade: ACCEPT-WITH-FIXES** — 7 MAJOR, 9 MINOR. The science is not
impeached by this lens: every number the paper states traces to the
receipt (114 of 114), the byte/path anchor layer genuinely bites and
blocks the write, and two plain runs are byte-identical under a varied
hash seed. What fails is the instrument's **description of itself**.
Three statements the delivered paper makes about its own instrument are
false as written, one gate label is false as demonstrated, the
registered CLI repair item is unaddressed and reproduces exactly, and
four of nine injections survive — two of them corrupting the delivered
verdict's content with 44/44 gates green.

**Executions:** 9 full-program runs (all on scratch copies, never in the
repo). **Independent recomputations / verifications:** 670 (breakdown
in §10).

**Object verified before any work.** All six pinned hashes reproduce:
paper `09482eb080cc`, code `9a4f0529b840`, output `097c08a0229d`,
receipt `dd86ad1a80d7`, pin `42ce06e6be8a`, protocol `b00a0be5c1ce`.
Repo HEAD `d9f39a2`, working tree clean at start.

---

## 1. THE CLI AUDIT — the registered disease is UNREPAIRED

### 1.1 What the file declares

Lines 17–31 of `v14/code/gprep_foundation_exact.py`, verbatim:

```
  17	CLI CONTRACT
  18	  /opt/homebrew/bin/python3.13 v14/code/gprep_foundation_exact.py
  19	      A plain run.  Runs everything: anchors, ARM A, ARM B, every
  20	      declared injection-falsifier, the never-falsified census, the
  21	      compliance sweep, and the composed verdict.  WRITES
  22	      v14/code/gprep_foundation_output.txt and
  23	      v14/code/gprep_foundation_receipt.json (paths derived from this
  24	      file's own location).  Exit 0 whatever the science says; exit 1
  25	      ONLY on an anchor failure or a dead falsifier.  Two plain runs
  26	      are byte-identical: every wall-clock number goes to stderr and
  27	      never to the receipt.
  28	  ... --no-write
  29	      Identical measurement, no files written (diagnostic).
  30	  ... --list-gates | --list-mutants
  31	      Print the gate / falsifier registries and exit 0.
```

### 1.2 What the file actually parses

The entire argv handler is four lines. There is no other reference to
`sys.argv` or to `ARGV` anywhere in the 3,251-line file:

```
    54	ARGV = set(sys.argv[1:])
  2816	if '--list-gates' in ARGV:
  2820	if '--list-mutants' in ARGV:
  3237	if '--no-write' not in ARGV:
```

`ARGV` is a **set membership test three times over**. There is no
whitelist, no residue computation, no `argparse`, no error branch. The
six `sys.exit` sites in the file are: L394 (anchor failure, exit 1),
L2819 / L2823 (the two registry flags, exit 0), L3251 (exit 1 iff a
falsifier is dead). **Exit 2 does not exist in this program.**

### 1.3 The #82 contract minimum, scored

| # | contract minimum | present? | evidence |
|---|---|---|---|
| 1 | unknown flags rejected, exit 2 | **NO** | no residue test; `exit 2` absent from the source |
| 2 | a real `--selftest` (corrupts one anchor, exits 1, writes nothing) | **NO** | the token `selftest` does not occur in the file |
| 3 | a `--mutant NAME` harness | **NO** | a strong *internal* mutant engine exists (118 falsifiers) but is not CLI-addressable; `--mutant` is not parsed |
| 4 | flags do what the contract says | **PARTIAL** | the three real flags work; everything else is a silent no-op |

### 1.4 Demonstrated (execution #3, scratch tree `cli/`)

```
python3.13 v14/code/gprep_foundation_exact.py \
    --selftest --mutant BLOCKING-FACT-ERASED --no-writ --list-gate -x --utterly-bogus
```

- **exit code 0**
- **zero** occurrences of `unknown` / `unrecognized` / `usage:` /
  `invalid` on stdout or stderr
- the full plain delivery ran: `44 PASS / 0 FAIL over 44 gates; 118
  falsifiers, 0 dead`
- **both artifacts were (re)written**
- the resulting `gprep_foundation_output.txt` is **byte-identical**
  (`a10cc832350a`) to the plain run in the same environment

This is the #66 correction of record reproduced verbatim: a `--selftest`
invocation runs a plain delivery and reports success. **The registered
repair item has not been applied.**

Two aggravations found beyond the registered item:

- **`--no-writ` wrote both files.** A one-character typo of the safety
  flag silently disables the safety. In-repo this would overwrite the
  committed artifacts.
- **Exit 1 on a dead falsifier still writes.** The write at L3237
  precedes the exit at L3251. Injection INJ-2b exited 1 *and* left
  rewritten `output.txt` and `receipt.json` on disk. Only the anchor
  precheck (L394) is a write-blocking failure — confirmed by INJ-5,
  which exited 1 with **no artifacts written**.

### 1.5 The two registry flags silently under-report

Verified statically (no execution needed), because both flags exit
before the remaining registrations run:

- `--list-gates` (L2816) prints the **40** gates registered before that
  line. Four substantive gates — `C-THEOREMCENSUS` (L2925),
  `C-COMPLIANCE` (L3026), `C-WAIVERS` (L3033), `C-VERDICTFALSIFIERS`
  (L3041) — are registered afterwards. The delivered census is **44**.
- `--list-mutants` (L2820) prints **112**. `MUTANTS.extend(PHASE2)`
  at L3074 adds six more. The delivered census is **118**
  (`mutants_total: 118`).

The `--list-gates` number is especially misleading: 40 is also the
substantive-gate count, so the listing looks self-consistent — but the
40 rows it prints are 36 substantive + 3 theorem-pass + 1 disclosure,
i.e. neither all gates nor the substantive ones.

### 1.6 The CLI verdict, in the #82 contract's terms

> **CLI-CONTRACT-FAILED — 0 of 4 minima met.** The program has no flag
> whitelist and cannot emit exit 2; it has no `--selftest` and no
> `--mutant NAME`; its declared "CLI CONTRACT" docstring is a comment
> that nothing enforces; and its two diagnostic flags under-report their
> own registries (40/44 and 112/118). This is the second recorded
> occurrence of the silent-flag-ignoring disease on this unit.

---

## 2. COVERAGE AT #34 — the honest denominators

### 2.1 What the unit reports

44 gates (40 substantive / 3 theorem-pass / 1 disclosure), 0 failures;
118 falsifiers, 0 dead; 3 never-falsified, all waived; 0 keys
read-but-unconstrained. The theorem-pass census is printed with its
count and the paper says "the pass count is not a test count" — that is
correct practice and I credit it.

### 2.2 The denominators the unit does not print

**(a) 82 of 189 delivered receipt keys carry no falsifier at all
(43.4%).** The falsifier generator (L2768–2775) harvests read-keys from
`KIND_SUB` gates only; every key outside that harvest, and outside the
14 named mutants, is delivered ungated. Computed key-by-key over the
receipt: 107 of 189 flat keys are covered, 82 are not. The ungated set
is not peripheral — it includes numbers the paper states as results:

| ungated key | the paper claim it carries |
|---|---|
| `t5_ledger_number` | §3 "terminal at v10 ledger #495" — the pin's *explicit* order |
| `rsig_profiles` | §7 the profile decomposition `{(1,1):1365,(2,2):3788,(2,3):4,(3,2):4}` — "ARM B rides on it" |
| `mono_pairs`, `mono_shrinking`, `nsup_shrinking` | §7 the monotonicity theorem's numbers |
| `escape_control_classes` | §8.2 "76 escaping transitions into 32 above-window classes" |
| `escape_witness_{depth,kind,q,target}` | §8.1 the exhibited escape witness |
| `root_menu`, `root_conditional`, `root_orbits_per_kind` | §10 the root-symmetry theorem's distribution |
| `B2_full_rows`, `B2_homo_rows`, `B2_profile_rows` | §11.4 / §11.5 — both δ* tables entire |
| `B3_dist_by_depth`, `B3_block_reentries` | §11.6(ii) the distance table; the re-entry census |
| `pool3_*`, `depth7_projection` | §11.1 the infeasibility projections |
| `mass_census_d6`, `ratio_transport`, `ratio_deliveryfree` | §4 the one-level extension; §5 "ratio for ratio" |

**(b) 12 of 118 falsifiers only bite after escalation, and this is never
censused.** The harness escalates drift → poison → erase (L2707–2760)
and records the level in the mutant's *name*, but no line of the output
or the paper aggregates it. Measured from the receipt: 91 die at L1
drift, **10 need L2 POISON**, **2 need L3 ERASE**. A gate that only dies
when its input is *erased* is a gate that constrains existence, not
value. The two are:

- `DRIFT[B2_grain_split]+ERASE` → `B2-GRAIN`, whose predicate is
  `len(f['B2_grain_split']) > 0` (L2274) — a pure non-emptiness test.
  Its label claims "at least one profile block is an atom at the primary
  grain and is NOT at the control grain", and the paper elevates this to
  a headline control ("the grain bites", §11.4; controls table §13;
  inheritance item 4 §15). Any wrong content — wrong profiles, wrong N,
  wrong δ*, the inequality in the wrong direction — passes. Only total
  deletion is detected.
- `DRIFT[budget_arbmerge]+ERASE` → `A1-BUDGETS`, whose arb-merge
  conjunct is `len(f['budget_arbmerge']) > 0` (L657). The other two
  conjuncts are real set equalities; this one is not.

**(c) Phase-1 falsifiers were scored against 40 gates, not 44.** `RES`
at L2703 predates the four `C-*` registrations; phase-1 mutants are
compared against that partial set and are never re-scored against the
full one. This direction is conservative (it can only under-report
kills), so it is a disclosure gap, not a defect.

### 2.3 Tautological and weak predicates (static scan of all 44)

| gate | kind | weakness |
|---|---|---|
| `B2-GRAIN` | SUB | non-emptiness only (above) |
| `A1-BUDGETS` | SUB | third conjunct is non-emptiness only |
| `C-WAIVERS` | SUB | second conjunct `len(f['waivers']) > 0` is non-emptiness only |
| `V-SEVEN` | SUB | **containment**, on a **typed literal shared with the builder** (§5) |

No gate predicate is a constant. No gate predicate references a mutant's
identity — the L2992 self-check for that is weak (it tests only for
`"MUTANT` with a double quote and for `mutant_name`; the same reference
written with single quotes would pass) but the property it checks is in
fact satisfied. I credit the read-tracking `Facts` class and the
blind-evaluation design: these are the right mechanisms.

---

## 3. WAIVER CENSUS AT #34 — the loop closes on the declaration

Every waiver in this unit is issued by this code (L2890–2904, repeated
L3085–3099):

```python
    if kind == KIND_THM:
        w = ("THEOREM-PASS: analytically forced by the construction; "
             "the forcing is machine-checked by the disclosure printed "
             "at its section, ...")
    elif kind == KIND_DIS:
        w = ("DISCLOSURE: this clause is true by algebra for every "
             "input ...")
    else:
        w = "NO VERIFIED WAIVER — this is a defect"
```

The "VERIFIED" waiver is `if kind == KIND_THM`. No machine check of the
forcing exists anywhere; the waiver text asserts one that is not there.
And the loop is closed in the wrong direction:

1. a gate declared `KIND_THM`/`KIND_DIS` is **excluded from the
   falsifier generator** (L2770 `if kind != KIND_SUB: continue`);
2. having no falsifier, it can only die by accidental key overlap with a
   substantive gate;
3. dying nowhere, it lands in the never-falsified census;
4. where it is **automatically waived by the very declaration that
   excluded it**.

Measured, the loop runs to completion for three of the four THM/DIS
gates. `A3-KERNEL` (THM) escapes only by accident: `proper_rows` happens
also to be read by `V-VERDICT`, so `DRIFT[proper_rows]` kills it. The
other three are never named in any kill sample:
`A3-CUTADD`, `A4-MONO`, `A7-ROOTTHEOREM` — exactly `never_falsified`.

Worse, all three waived predicates **are measurements**:

- `A4-MONO`: `mono_shrinking == 0 and mono_pairs == mono_expect and
  nsup_shrinking > 0` — a census over 30,728 transitions that could have
  come out otherwise, plus a strict positivity claim.
- `A7-ROOTTHEOREM`: `root_one_orbit_per_kind and
  root_conditional_constant` — a measured constancy across r = 1…7.
- `A3-CUTADD`: `raw_cut_masses[0] == '2' and raw_cut_masses[-1] ==
  '2168717/16384'` — typed-literal comparisons against measured values.

So the classification that removes them from the substantive count of 40
**and** from falsification **and** grants their waiver is the author's
declaration alone. The gate `C-WAIVERS` is falsifiable (PHASE2's
`WAIVER-UNVERIFIED` kills it), but what it gates is the *bookkeeping*,
never the *classification*.

**Waiver census result: 3 waivers, 0 backed by a gate that could fail on
the question the waiver answers.**

---

## 4. VERBATIM ANCHORS AT #62 — they bind existence, not meaning

### 4.1 One anchor names a gate that does not exist

`v14/code/gprep_foundation_exact.py` L217 binds the T4 window to
consumer gate `B0-SUCCESSOR-NAMED`. The string `B0-SUCCESSOR-NAMED`
occurs **exactly once in the file** — at that line. It is not among the
44 registered gates (checked against every `gate(...)` call and against
the receipt's `_gates`; the B-series is `B1-TREE, B2-ATOM, B2-FULLZERO,
B2-GRAIN, B3-HITTING, B3-RSIG-RETURN, B3-DISTANCE, B3-MONOTONE`).

The window it anchors is the single most load-bearing quotation in the
unit — d70's *"No operator-level minorization … has been attempted
anywhere"* — the sentence that licenses ARM B's existence and the
paper's claim to be running "the one construction the predecessor named
and did not run" (§11). Its declared consumer is a gate that is not
there, and nothing notices: no referential-integrity check exists
between the consumer field and `GATES`.

The paper repeats the claim as a delivered result (§16): "verbatim-context
anchors | 12 windows, evaluated first, **each bound to a named consumer
gate**". That statement is false as written.

### 4.2 The consumer binding is decorative

`VB` rows are `(tag, path, consumer, ok, chars)`. The `consumer` field
is used at L372–374 (printing), L420 (`F['verbatim_ok']`) and L3216–3218
(the receipt). It is never matched against a gate id, and no gate reads
`verbatim_ok` or `verbatim_n` at all — grep returns only the two
assignment lines. The anchors are enforced by the L391 precheck
(`ctx in txt`, else exit 1), which is real; the *binding to a consumer*
is a printed string.

### 4.3 The drift falsifier is tautological for 10 of 12 windows

The perturbation rule (L2675) is:

```python
    drifted = ctx.replace('68', '69') if '68' in ctx else ctx + "!"
```

Only two of the twelve windows contain `68` (T2's and T3's escape
quotations). For the other **ten**, the "perturbation by one character"
is *appending an exclamation mark to a multi-line technical quotation* —
a test that cannot plausibly fail. `M-VERBATIMDRIFT` reports
"drifted windows still found: 0 of 12" and its label claims the windows
"bind meaning to use, not mere existence".

### 4.4 Demonstrated (execution #8, INJ-6)

I replaced T7's 41-character window
`objects k_r(e|h) = q G(h+e, r-1)/G(h, r).`
with the 4-character string `"the "` — a substring appearing on 95
lines of the source note and carrying no content whatever. Result:

```
  [OK ] T7  v10/note-d46b-martin-at-transport.md  -> consumer gate A3-KERNEL  (4 chars of context)
  [PASS] M-VERBATIMDRIFT — ... the windows bind meaning to use, not mere existence
        (drifted windows still found: 0 of 12)
```

`44 PASS / 0 FAIL`, 118 falsifiers, 0 dead, exit 0, artifacts written.
**The gate whose label asserts that the windows bind meaning passed
while certifying a 4-character generic string as a verbatim-context
anchor.**

### 4.5 What does work — credited

The **byte anchors and path-value anchors are real and they bite.**
Injection INJ-5 changed one pinned artifact path (T5's `d74` `.out` to
`d70`'s, keeping the pinned sha). The run printed `ANCHOR FAILURE — exit
1` at the precheck, exited 1, and **wrote no artifacts**. This is the
one place in the instrument where a failure is caught *before* the
delivery is produced, and it is correctly built.

---

## 5. COMPARATOR INDEPENDENCE AT THE #82-STRENGTHENED STANDARD

### 5.1 The verdict comparator IS its builder

```
  2631	VERDICT = build_verdict(F)
  2632	F['verdict'] = VERDICT
  2633	gate("V-VERDICT", KIND_SUB,
  2634	     "THE VERDICT IS DERIVED INSIDE A GATE FROM THE MEASURED COUNTS: "
  2635	     "the emitted string is compared for COMPLETE-STRING EQUALITY "
  2636	     "against a string rebuilt segment-by-segment from the gated "
  2637	     "object (never containment, never a prefix), and a verdict-flip "
  2638	     "falsifier proves the derivation can fail",
  2639	     lambda f: f['verdict'] == build_verdict(f),
```

The #82 engraving prohibits a verdict comparator sharing **code, inputs,
or typed literals** with its builder. This comparator shares **all
three**: it is the identical function `build_verdict`, applied to the
identical object `f`. It is not "the same concatenation written twice"
(the previously measured failure mode) — it is the same concatenation
*called* twice. There is no second rebuild anywhere in the file.

What the gate can therefore detect is exactly one thing: direct
corruption of the stored string `f['verdict']` after it was built (which
is what all five `VERDICT-*` falsifiers do, and they do kill it), or
corruption of a key that `build_verdict` reads. What it **cannot**
detect is any fault *inside `build_verdict` itself* — because both sides
of the comparison commit the same fault.

### 5.2 Demonstrated, twice, on the delivered headline

**INJ-1** (execution #4) — one token changed in the builder:
`f['escape_primary']` → `f['escape_control']` in the ESCAPE clause.
Delivered verdict:

```
ESCAPE 76 transitions into 5 above-window classes at the DECLARED-PRIMARY 13-class grain and 76 at the 113-class control grain
                                      (committed: ESCAPE 68 ... 13-class grain and 76 ...)
```

`44 PASS / 0 FAIL`, 118 falsifiers, 0 dead, exit 0, artifacts written.
The delivered verdict now reports the **control-grain** escape count
*under the declared-primary grain label* — precisely the arena artefact
the unit's own §8.2 and §15(4) forbid ("A verdict taken at one grain and
read at the other would be an arena artefact"). The unit's central
methodological safeguard is defeated by a one-token builder edit,
undetected.

**INJ-2** (execution #5) — `f['B3_profile_decreases']` →
`f['B3_profile_pairs']` in the BLOCKED clause. Delivered verdict:

```
the holdings profile decreases at 30728 of 30728 transitions, so the atoms
form a ladder the process climbs and never descends
```

A self-contradicting headline — the blocking fact asserted while its own
number denies it. `44 PASS / 0 FAIL`, exit 0, artifacts written.

### 5.3 The one protection is a coincidence, not a design

**INJ-2b** (execution #9) flipped the segment name in the builder:
`"GPREP-MINORIZATION-BLOCKED-AT-"` → `"GPREP-MINORIZATION-FOUND-AT-THE-"`.
This **was** caught — exit 1, `41 PASS / 3 FAIL`, three dead falsifiers
— but **not by V-VERDICT, which passed**. The catch came from
`VERDICT-TYPED-SEGMENT`, whose body is
`f['verdict'].replace('BLOCKED-AT-', 'FOUND-AT-')`: once the builder
stopped emitting the literal `BLOCKED-AT-`, that falsifier became a
no-op, went dead, and cascaded into `COMPLIANCE-FALSE` and
`VERDICT-FALSIFIER-CENSUS-DROP` also dying. `C-COMPLIANCE`, `C-WAIVERS`
and `C-VERDICTFALSIFIERS` then failed.

So the only thing standing between this unit and a delivered
`GPREP-MINORIZATION-FOUND-AT-THE-` headline is a **string literal
duplicated between a mutant body and the builder** — the exact coupling
the #82 engraving names, here load-bearing in the protective direction.
It protects the segment *name* only: INJ-2 preserved the literal and
corrupted the segment's *content* with impunity. And the run still
overwrote both artifacts before exiting 1.

### 5.4 What does work — credited

`A4-MASS` (L1296) is a **genuinely independent comparator** and the
COMPLY rule describing it is true. The two routes are structurally
different computations:

- `renewal_depth5_measured` = `ret_k[5]`, a depth-5 chained
  kernel-weight recursion summed over the R-MENU points (L1160–1185);
- `renewal_depth5_closed` = `(3/2)**5 * GT[ROOT][1] / GT[ROOT][6]`, a
  three-term rational expression in the root potentials.

They share only the potentials. This is what #82 asks for, and it proves
the unit knows how to build such a comparator — and did not do it for
the verdict.

---

## 6. THE FEED-FORWARD SURFACE — what R-GM-9's swallowed probe should have read

### 6.1 The receipt's real key structure

`gprep_foundation_receipt.json` is written by
`json.dump(RECEIPT, fh, indent=1, sort_keys=True)` (L3241) where
`RECEIPT` is built by copying **every key of the gated object `F`
verbatim to the top level** (L3203–3205), then attaching seven
underscore-prefixed blocks. It is therefore **flat**, with:

- **189 flat keys** (no `facts`, no `F`, no `results`, no nesting), and
- **7 nested keys, all underscore-prefixed**:
  `_anchors_bytes`, `_anchors_verbatim`, `_caps`, `_compliance`,
  `_gates`, `_mutants`, `_pedigrees`.

A probe that looked for `receipt['gates']`, `receipt['facts'][...]`,
`receipt['results'][...]` or any nested container finds nothing — and
because the JSON is otherwise well-formed, an unguarded `.get()` chain
returns `None` and the probe reports success on an empty read. That is
the shape of a silent swallow.

**A correct probe reads, by their real names:**

| what Γ-main wants | the real key | shape |
|---|---|---|
| the verdict string | `receipt['verdict']` | `str`, top level |
| the census | `receipt['t_total']` = `243769` | `int` |
| the ports | `receipt['rsig_count']` = `5161`, `receipt['rmenu_count']` = `1365` | `int` |
| the potentials | `receipt['G_transport']`, `receipt['G_deliveryfree']` | **list of `str`** |
| the kernels | `receipt['proper_rows']`, `receipt['positivity_violations']` | list / int |
| the escape | `receipt['escape_primary']`, `receipt['escape_control']`, `receipt['grain_primary_classes']`, `receipt['grain_control_classes']` | `int` |
| the atoms | `receipt['B2_atoms']`, `receipt['B2_best_delta']`, `receipt['B2_nu_profile']` | list / **`str`** / **`str`** |
| the blocking fact | `receipt['B3_profile_decreases']`, `receipt['B3_profile_pairs']` | `int` |
| gate status | `receipt['_gates']` — a **list** of `{id, kind, ok, label, detail}` | list, **not a dict keyed by id** |
| falsifiers | `receipt['_mutants']` — list of `{name, class, killed, sample}` | `sample` is **truncated to 4** |
| anchors | `receipt['_anchors_bytes']` (`{row, path, sha256_12, ok}`), `receipt['_anchors_verbatim']` (`{row, path, consumer, ok, chars}`) | list |
| caps | `receipt['_caps']` = `{CAP_T:6, CAP_DF:6, CAP_ESC:4, CAP_SYM:3, RMAX:7, NMAX:5, pool3_depth:3, pool3_depth5_conditional_arm:'NOT RUN'}` | dict |

**Three traps a consumer must be told about:**

1. **Every `Fraction` is a JSON string.** `json.dumps(..., default=str)`
   (L3205) means `G_transport` is `['2','4','257/32',…]`, `B2_best_delta`
   is `'1'`, `B3_rsig_inf_widest` is `'0'`. A numeric comparison against
   these silently fails or raises; `'0'` is truthy.
2. **Tuples became lists; tuple dict-keys became strings.** e.g.
   `B2_atoms` rows carry the profile as the string `'(1, 1)'`.
3. **`_mutants[i]['sample']` is truncated to the first four gates**
   (L3211), so a gate→killer map cannot be rebuilt from the receipt
   alone. Any coverage audit done *from the receipt* will under-count.

### 6.2 The receipt cannot identify the code that produced it

`RECEIPT` carries no sha of `gprep_foundation_exact.py`. The code digest
is emitted only into `gprep_foundation_output.txt` (L3234–3235). A
consumer reading the receipt — which is what Γ-main does — has **no way
to verify which code version produced the numbers it is consuming.**

### 6.3 Nothing gates the artifacts between the gated object and disk

**INJ-3** (execution #6): I mutated `RECEIPT` and `OUT_LINES` after the
gated object was final and before the write. Result — exit 0,
`44 PASS / 0 FAIL`, 118 falsifiers, 0 dead, and on disk:

```
  receipt verdict    = GPREP-MINORIZATION-FOUND-[delta = 1 uniform on R-SIG]
  receipt t_total    = 1
  receipt rsig_count = 9999
  output  line 1     = [GPREP - INJECTED LINE: not what the run computed]
```

Every gate reads `F`; no gate reads the serialized artifacts. **The
files Γ-main consumes are, structurally, ungated output.** This is the
feed-forward surface R-GM-9 was standing on.

---

## 7. THREE-WAY SWEEP, BYTE-IDENTITY, AND THE UNANCHORED INPUT

### 7.1 paper ↔ output ↔ receipt: clean

I extracted every numeric token in the paper greater than 12 or of the
form `a/b` (after normalising `{,}`, `\!`, `\tfrac`): **114 tokens.**
Every one appears verbatim in `gprep_foundation_output.txt` or
`gprep_foundation_receipt.json`. **Zero orphans.** Spot-verified by hand
against the receipt: `243769/243768/0` (columns), `5161/1365/3796/0`
(ports), `1365 = Σ4ⁿ`, `1044 of 3969`, `30728/0`, `31570/293121`,
`8988404357/9050056041`, `44/40/3/1`, `118/0`, `18 of 18`. The paper
does not invent numbers.

I also credit two disclosures the paper makes against itself: the
pin says the layer has "6 event kinds" and the measurement returns 5
(§4, disclosed as a derived-in-text mismatch), and the narrow-window
positive δ* row is printed rather than dropped (§11.5).

### 7.2 Determinism: holds

Execution #2 with `PYTHONHASHSEED=7` produced output `a10cc832350a` and
receipt `747c62e826b1` — **byte-identical** to execution #1's plain run.
The `SK()` stable-key discipline works. Credited.

### 7.3 Byte-identity against the committed artifacts: FAILS off-tree

My plain scratch run does **not** reproduce the committed hashes:

| artifact | committed | plain scratch run |
|---|---|---|
| `gprep_foundation_output.txt` | `097c08a0229d` | `a10cc832350a` |
| `gprep_foundation_receipt.json` | `dd86ad1a80d7` | `747c62e826b1` |

The entire diff is two lines, and one value:

```
< ... carries **(LEDGER #495)**. ... TERMINAL at v10 LOG #495.
> ... carries **(LEDGER #None)**. ... TERMINAL at v10 LOG #None.
```

### 7.4 The cause: an unanchored, ungated runtime input

```
   435	_gitlog = os.popen(
   436	    "cd " + REPO + " && git show HEAD:v10/LOG.md 2>/dev/null").read()
```

- `v10/LOG.md` is **not in the anchor table**. It has no byte anchor, no
  path-value anchor and no verbatim-context anchor. The banner at
  L280–284 claims "**every file this process opens is listed in the
  anchor table below with its sha256-12**". It is not.
- The value is read through a **shell subprocess at git HEAD** — a
  moving target. The delivered output is a function of the ambient
  repository, not of the pinned bytes. Any HEAD at which that ledger
  line differs changes the artifact hashes.
- `2>/dev/null` swallows every failure mode. Outside a git work tree the
  read returns empty, `_stamp` stays `None`, and the run prints
  `**(LEDGER #None)**` and `TERMINAL at v10 LOG #None`.
- **`t5_ledger_number` is read by no gate.** Grepped: it is assigned at
  L445 and appears only in emitted f-strings at L453, L456, L461. So the
  run above reported **`44 PASS / 0 FAIL over 44 gates; 118 falsifiers,
  0 dead`** and **exit 0** while delivering `#None` as the pin's
  explicitly ordered verification.

This is the pin's own T5 instruction — *"VERIFY the exact v10 ledger #
in-unit and print it"* — discharged by the single unanchored input in
the file and left as the single ungated number in the delivery.

### 7.5 The compliance sweep contradicts the paper, and itself

The receipt's `_compliance` carries, with status `true`:

> `"RUNBOOK 14 (#46) no unanchored runtime inputs"` — evidence: *"the
> only files read are the pinned artifacts and this file's own source;
> v14/LOG.md and /STATUS.md are not opened"*

The paper's §3 says the opposite, correctly:

> "The only files this process opens are the pinned artifacts, **the
> committed ledger object for the T5 verification**, and its own source."

The compliance evidence string is false as written, and its status is
**hard-coded `True`** (L2988).

### 7.6 Eight of eighteen compliance rules are asserted, under a header that says they are not

The sweep is printed under `[COMPLIANCE SWEEP — computed statuses, not
asserted ones]` (L3022), and the paper §16 reports "compliance | 18 of
18 engraved rules satisfied, **each computed**". Eight of the eighteen
are the literal `True`:

| line | rule |
|---|---|
| L2963 | RUNBOOK 13 (#10) render from the gated object |
| L2967 | RUNBOOK 13 (#20) prose renders from the receipt |
| L2971 | **RUNBOOK 14 (#20) compliance claims are gate claims** |
| L2987 | **RUNBOOK 14 (#46) no unanchored runtime inputs** (also false, §7.5) |
| L2995 | **RUNBOOK 14 (#219) comparators built independently** |
| L3000 | RUNBOOK 15 declared arena |
| L3005 | RUNBOOK 15 (#196) match every coordinate |
| L3010 | RUNBOOK 13 (#314) precheck may not name the verdict |

The three in bold are self-undermining: the rule asserting that
compliance claims are gate claims is not a gate claim; the rule
asserting comparators are built independently is asserted while the
verdict comparator is its own builder (§5); the rule asserting no
unanchored inputs is asserted while one exists (§7.4). `C-COMPLIANCE`
gates only the aggregate `compliance_all`, so a rule that is a constant
can never move it.

---

## 8. THE INJECTION TABLE

Nine full-program executions on scratch copies. "Caught" means the
program refused the delivery (exit 1) **or** a gate failed.

| # | injection | class | result | evidence |
|---|---|---|---|---|
| INJ-0a | plain run, unmodified | baseline | — | 44 PASS / 0 FAIL, exit 0; hashes differ from committed (§7.3) |
| INJ-0b | plain run, `PYTHONHASHSEED=7` | determinism | **byte-identical** | `a10cc832350a` / `747c62e826b1` = INJ-0a |
| INJ-CLI | `--selftest --mutant NAME --no-writ --list-gate -x --utterly-bogus` | CLI contract | **SURVIVED** | exit 0, no diagnostic, full delivery, artifacts written, output = plain run |
| INJ-1 | builder field swap: verdict's ESCAPE count reads the control grain | verdict content | **SURVIVED** | delivered "ESCAPE 76 … at the DECLARED-PRIMARY 13-class grain"; 44 PASS / 0 FAIL, exit 0 |
| INJ-2 | builder value swap: `B3_profile_decreases` → `B3_profile_pairs` | table value in verdict | **SURVIVED** | delivered "decreases at 30728 of 30728 transitions"; 44 PASS / 0 FAIL, exit 0 |
| INJ-2b | builder headline flip `BLOCKED-AT-` → `FOUND-AT-THE-` | verdict segment name | **caught** (accidentally) | exit 1, 41 PASS / 3 FAIL, 3 dead falsifiers — **V-VERDICT passed**; caught by literal coupling in a mutant body; artifacts still written |
| INJ-3 | receipt + output corrupted between the gated object and the write | render / feed-forward | **SURVIVED** | receipt on disk: `verdict = GPREP-MINORIZATION-FOUND-…`, `t_total = 1`, `rsig_count = 9999`; 44 PASS / 0 FAIL, exit 0 |
| INJ-5 | path drift on a pinned row (T5 `.out` → `d70`'s) | path-value anchor | **CAUGHT** | `ANCHOR FAILURE — exit 1`, **no artifacts written** |
| INJ-6 | quotation-meaning: T7's 41-char window → the 4-char string `"the "` | verbatim anchor | **SURVIVED** | `[OK ] … (4 chars of context)`, `M-VERBATIMDRIFT` PASS "0 of 12"; 44 PASS / 0 FAIL, exit 0 |

**4 survived, 1 caught by coincidence, 2 caught, 2 baselines.**
Of the four survivors, two corrupt the delivered verdict's content, one
corrupts the delivered receipt wholesale, and one defeats the
verbatim-anchor layer.

---

## 9. FINDINGS AND REPAIRS

Repairs are phrased to be lifted verbatim into repair orders.

### MAJOR-1 — the registered CLI repair item is unapplied; the disease reproduces exactly

Evidence §1. `ARGV` is three membership tests; `--selftest`,
`--mutant NAME`, `-x`, `--utterly-bogus`, `--list-gate` and `--no-writ`
are all silently ignored; exit 2 does not exist; the docstring's "CLI
CONTRACT" is unenforced; `--list-gates` reports 40 of 44 and
`--list-mutants` 112 of 118. This is the second recorded occurrence on
this unit (#66 → #82 engraving → here).

> **REPAIR MAJOR-1.** In `v14/code/gprep_foundation_exact.py`, replace
> the bare `ARGV = set(sys.argv[1:])` with a whitelist parse:
> (a) declare `KNOWN = {'--no-write', '--list-gates', '--list-mutants',
> '--selftest', '--mutant'}`; (b) compute the residue of `sys.argv[1:]`
> against `KNOWN` (treating `--mutant` as taking one value) and, if the
> residue is non-empty, print `usage:` with the accepted flags to stderr
> and `sys.exit(2)` **before any measurement runs**; (c) add
> `--selftest`, which corrupts exactly one anchor value in-process,
> asserts that the corresponding gate fails, prints the gate id it
> killed, **writes no files**, and exits 1; (d) add `--mutant NAME`,
> which runs the named falsifier from `MUTANTS`, prints the gates it
> killed, writes no files, and exits 1 if it killed nothing; (e) move
> the `--list-gates` / `--list-mutants` branches to **after** the final
> registrations (after L3074) so the registries printed are the
> registries delivered, or register all gates and mutants before the
> branches; (f) move the artifact write at L3237 to **after** the
> dead-falsifier test, so that `exit 1` never leaves a rewritten
> artifact on disk.

### MAJOR-2 — the verdict comparator is its own builder

Evidence §5. `VERDICT = build_verdict(F)` (L2631) and
`lambda f: f['verdict'] == build_verdict(f)` (L2639) share code, inputs
and typed literals. Demonstrated to pass INJ-1 and INJ-2, both of which
corrupt the delivered verdict's content with 44/44 green; and to pass
INJ-2b, where the headline itself flipped.

> **REPAIR MAJOR-2.** Build the verdict comparator independently of the
> verdict builder, at the #82-strengthened standard. Concretely: keep
> `build_verdict` as the emitter, and add a second function
> `check_verdict(f, s)` that does **not** call `build_verdict` and does
> not re-concatenate; instead it **parses the emitted string** and
> asserts, field by field against `f`, that each extracted number and
> each segment name equals the gated value — including that the ESCAPE
> clause's first number is `f['escape_primary']` and its second is
> `f['escape_control']`, and that the BLOCKED clause's first number is
> `f['B3_profile_decreases']`. No string literal may appear in both
> `build_verdict` and `check_verdict`: segment names must be read from a
> single shared constant table that both consult by key, and the gate
> must assert the *key*, not a re-typed literal. Re-point `V-VERDICT` at
> `check_verdict`. Add two falsifiers that reproduce INJ-1 and INJ-2 (a
> builder field swap and a builder value swap) and require both to kill
> `V-VERDICT`.

### MAJOR-3 — an unanchored, ungated runtime input; byte-identity fails off-tree

Evidence §7.3–7.5. `os.popen("cd … && git show HEAD:v10/LOG.md
2>/dev/null")` (L435) is outside the anchor table, is read at a moving
HEAD, has its failures swallowed, and its product `t5_ledger_number` is
read by no gate. A plain run outside the work tree delivers
`TERMINAL at v10 LOG #None` with 44 PASS / 0 FAIL and exit 0. The
banner's "every file this process opens is listed in the anchor table"
and the compliance rule at L2987 are both false as written; the paper's
§3 states the truth and contradicts them.

> **REPAIR MAJOR-3.** Either (a) **anchor it**: add `v10/LOG.md` to the
> anchor table as a pinned row with its own sha256-12 byte anchor and a
> verbatim-context anchor on the exact string
> `D74 ROUND 1 ADJUDICATED AND TERMINAL: TH-II WITH A FIND`, read it
> through the same `check_bytes`/`check_verbatim` path as every other
> row, drop the `2>/dev/null`, and gate `t5_ledger_number` with a
> substantive gate asserting `f['t5_ledger_number'] == 495` (with a
> falsifier); or (b) **freeze it**: replace the subprocess with the
> pinned integer as a declared constant carrying the ledger quotation
> verbatim, and gate that constant against the anchored quotation. Under
> either option, correct the L2987 compliance evidence string to name
> every file the process opens, and correct the L280–284 banner. Under
> (a), state in the paper that byte-identity of the delivered artifacts
> is conditional on the repository HEAD.

### MAJOR-4 — a verbatim anchor names a gate that does not exist

Evidence §4.1. `B0-SUCCESSOR-NAMED` (L217) is not among the 44 gates; it
occurs once in the file. It anchors the quotation that licenses ARM B.
The paper §16 claims all 12 windows are "each bound to a named consumer
gate".

> **REPAIR MAJOR-4.** Register the missing gate `B0-SUCCESSOR-NAMED` as
> a substantive gate asserting that the d70 quotation naming the
> unattempted successor engine was located and that ARM B was in fact
> run (e.g. that `f['birkhoff_tau']` and `f['B2_atom_found']` are
> populated) — **and**, independently of that choice, add a
> referential-integrity gate `M-CONSUMERBINDING` asserting that every
> `consumer` field in `VERBATIM` is a member of
> `{gid for gid, k, l, p, d in GATES}`, with a falsifier that renames
> one consumer to a non-existent id and must kill it. Correct paper §16
> once the gate exists.

### MAJOR-5 — eight of eighteen compliance rules are asserted under a header that says they are computed

Evidence §7.6. Including the rules asserting that compliance claims are
gate claims, that comparators are built independently, and that there
are no unanchored runtime inputs — the last of which is also false.

> **REPAIR MAJOR-5.** Replace every literal `True` in `COMPLY` with a
> measured predicate over `F`, or delete the rule. Specifically:
> "render from the gated object" → assert that the set of keys the
> receipt serialises equals the set of keys in `F`; "prose renders from
> the receipt" → delete (it is a claim about a different artifact and
> cannot be measured here); "compliance claims are gate claims" →
> assert `all(isinstance(ok, bool) for n, ok, d in COMPLY)` **and** that
> no entry's status expression is a constant, by an AST check over
> `COMPLY`'s own source region; "no unanchored runtime inputs" → assert
> that the set of paths opened equals the anchored set (instrument
> `open`/`os.popen` and compare); "comparators built independently" →
> assert that `check_verdict` (MAJOR-2) shares no string literal with
> `build_verdict`, by AST comparison; "declared arena", "match every
> coordinate", "precheck may not name the verdict" → replace with
> assertions over the arena keys actually emitted, or delete. Add a gate
> `C-NOCONSTANTRULES` asserting that zero `COMPLY` statuses are literal
> constants, with a falsifier that inserts one and must kill it. Correct
> paper §16's "each computed".

### MAJOR-6 — the waiver loop closes on the declaration

Evidence §3. `KIND_THM`/`KIND_DIS` gates are excluded from the falsifier
generator and are then auto-waived by the same declaration; the waiver
text claims a machine check of the forcing that does not exist; all
three waived predicates are in fact measurements.

> **REPAIR MAJOR-6.** (a) Change the falsifier generator at L2769–2772
> to harvest read-keys from **all** gates, not only `KIND_SUB`, so that
> theorem-pass and disclosure gates carry falsifiers like every other
> gate. (b) Replace the declaration-based waiver with a *verified* one:
> a `KIND_THM` waiver may be issued only if the gate's predicate is
> shown to be constant over the admitted input class — either by a
> printed proof obligation with its own gate, or by demonstrating that
> the predicate survives the poison and erase perturbations of all its
> read keys (in which case it is genuinely input-independent). Any gate
> that fails this test must be reclassified `KIND_SUB` and counted as a
> measurement. (c) Re-audit `A4-MONO`, `A7-ROOTTHEOREM` and `A3-CUTADD`
> under (b); on the evidence here all three are measurements and the
> substantive count of 40 is understated. (d) Delete the phrase "the
> forcing is machine-checked by the disclosure printed at its section"
> from the waiver text unless (b) is implemented.

### MAJOR-7 — 82 of 189 delivered receipt keys carry no falsifier, and the artifacts themselves are ungated

Evidence §2.2 and §6.3. The ungated set includes the profile
decomposition ARM B rides on, both δ* tables, the escape witness, the
root-symmetry distribution, the infeasibility projections and the pin's
ordered ledger number. Separately, INJ-3 shows that no gate reads the
serialized output or receipt at all.

> **REPAIR MAJOR-7.** (a) Print an explicit coverage census in the
> output and receipt: `keys_delivered`, `keys_with_falsifier`,
> `keys_without_falsifier` with the unconstrained key list, and gate it
> (`C-KEYCOVERAGE`) with a declared floor plus a named waiver for every
> key deliberately delivered ungated. (b) Add a post-serialisation gate:
> after writing, re-read `gprep_foundation_receipt.json` and
> `gprep_foundation_output.txt` from disk and assert that the receipt's
> flat keys and values equal `F` and that the output's line list equals
> `OUT_LINES`; exit 1 on mismatch. Add a falsifier reproducing INJ-3
> that must kill it. (c) Add the producing code's sha256-12 to the
> receipt as `_code_sha256_12` so a consumer can identify what produced
> the numbers it reads.

### MINOR-1 — `--no-writ` (a typo of the safety flag) writes both artifacts
> **REPAIR.** Subsumed by MAJOR-1(b): with a whitelist, `--no-writ`
> exits 2 before any measurement.

### MINOR-2 — `exit 1` on a dead falsifier still overwrites the artifacts
> **REPAIR.** Subsumed by MAJOR-1(f).

### MINOR-3 — `B2-GRAIN` is falsifiable only by total erasure
Its predicate is `len(f['B2_grain_split']) > 0` (L2274) while its label
and the paper's headline control claim a directional fact.
> **REPAIR.** Strengthen to assert the direction the label states:
> every row of `B2_grain_split` has primary `'1'` and control `'0'`, and
> the row count equals the value the paper reports (4 of 6). Add a
> falsifier that flips one row's direction and must kill it.

### MINOR-4 — `A1-BUDGETS`' arb-merge conjunct is non-emptiness only
> **REPAIR.** Assert `set(f['budget_arbmerge']) == {'1/2', '1/4'}`, the
> measured value set the paper reports, rather than `len(...) > 0`.

### MINOR-5 — ten of twelve verbatim drifts are "append `!`"
Only two windows contain `68`; for the other ten the "perturbation by
one character or one digit" cannot plausibly fail (§4.3).
> **REPAIR.** Replace the drift rule at L2675 with one that perturbs a
> **content-bearing token** of every window: change the first digit if
> the window has one, else swap two adjacent alphabetic words, else
> delete the window's longest word. Gate that every one of the twelve
> drifted windows differs from its original **and** is absent from its
> source, and print the perturbation applied per row.

### MINOR-6 — verbatim windows bind existence, not meaning
INJ-6: a 4-character generic substring passes as an anchor while
`M-VERBATIMDRIFT` asserts the opposite in its own label.
> **REPAIR.** Add to the verbatim check a minimum-specificity gate: each
> window must be at least N characters (declare N; the T5 window is 15,
> so N ≤ 15 or T5 must be lengthened) **and** must occur **exactly once**
> in its source file. Correct the `M-VERBATIMDRIFT` label so it claims
> only what it tests. Add a falsifier that shortens one window to a
> generic substring and must kill the gate.

### MINOR-7 — `V-SEVEN` uses containment on a literal shared with the builder
`'FOUNDATION-TERMINALIZED' in f['verdict']` (L2642) — the only
containment test among the 44 predicates, and the literal also occurs in
`build_verdict`.
> **REPAIR.** Subsumed by MAJOR-2's shared-constant table: assert the
> segment *key* is present in the parsed verdict, not a re-typed literal
> substring.

### MINOR-8 — the escalation ladder is recorded but never censused
10 falsifiers need POISON and 2 need ERASE; nothing aggregates this, and
the paper reports only "118 falsifiers, 0 dead".
> **REPAIR.** Emit and gate an escalation census (`drift / poison /
> erase` counts, with the erase-only gate ids named), and report it in
> paper §13 beside the falsifier count.

### MINOR-9 — the mutant-identity self-check is quote-style dependent
L2992 tests only for `"MUTANT` (double quote) and `mutant_name`.
> **REPAIR.** Replace the substring test with an AST check that no
> `gate()` predicate lambda contains a string constant equal to any
> registered mutant name.

---

## 10. COUNTS, DISCIPLINE, AND REPO STATE

**Full-program executions: 9** — all in
`/private/tmp/.../scratchpad/gprep-in/{isp,plain2,cli,inj1,inj2,inj3,inj5,inj6,inj8}/`,
each a structurally faithful tree (`isp/v14/code/` real, `isp/v10`
symlinked read-only to the repo). **The unit was never run inside the
repo.**

**Independent recomputations / verifications: 670**

| n | what |
|---|---|
| 6 | sha256-12 of the six frozen artifacts |
| 2 | sha256-12 of the scratch code copies before running |
| 8 | sha256-12 of run artifacts (baseline, plain2, cli, comparisons) |
| 114 | paper numeric tokens traced into output/receipt |
| 189 | receipt flat keys enumerated and classified against the falsifier set |
| 118 | mutant rows classified by escalation level and kill count |
| 88 | 44 gate records classified by kind + 44 predicates parsed and scanned |
| 55 | static registry counts (44 gate linenos, 11 mutant append sites) |
| 17 | byte-anchor rows confirmed in the receipt |
| 18 | compliance rules classified computed vs asserted |
| 12 | verbatim consumer names checked against the gate registry |
| 12 | verbatim windows classified by drift class |
| 10 | argv sites (4) and sys.exit sites (6) enumerated |
| 8 | INJ-6 window candidates pre-checked (4 × present/drifted) |
| 7 | injection result extractions (verdict clauses, anchor rows, receipt fields) |
| 4 | never-falsified gate predicates traced to their read keys |
| 2 | A4-MASS's two routes audited for independence |

**Discipline observed.** Read-only git (`rev-parse`, `log`, `show`,
`status`, `diff --stat` only). No imports of unit code. All mutation on
scratch copies. One repo write: this file.

**Repo state.** My four target files are byte-identical to HEAD
(`git diff --stat` empty). **Note for the adjudicator:** `git status
--porcelain` was empty when I began at 05:27 and shows
`M v14/code/gmain_exact.py` (modified 05:42, 1286 insertions / 2099
deletions) at the end. **That modification is not mine** — I never
opened, wrote or executed that file; it is Γ-main's instrument and
appeared during my session, presumably from a concurrent worker. My only
write is `v14/review-gprep-instrument.md`.

---

## 11. THE GRADE

**ACCEPT-WITH-FIXES**, with all seven MAJOR repairs blocking.

The unit's measurements survive this lens intact: 114 of 114 paper
numbers trace to the receipt, the anchor precheck genuinely refuses a
drifted delivery without writing, determinism holds under a varied hash
seed, the falsifier engine is real and well-built (118 live falsifiers,
a three-level escalation ladder, a read-but-unconstrained census, blind
predicate evaluation), and `A4-MASS` is a properly independent
comparator. I found **no false physics number.**

What fails is the instrument's account of itself, and it fails in ways
the corpus has already engraved. The registered CLI item is unrepaired
and reproduces exactly. The verdict comparator is its own builder, and
that is not a theoretical objection: two one-token edits put a
wrong-grain escape count and a self-contradicting blocking fact into the
delivered headline with every gate green. The receipt Γ-main consumes is
structurally ungated. A verbatim anchor points at a gate that does not
exist. And three sentences the delivered paper prints as results — "each
computed", "each bound to a named consumer gate", and the description of
V-VERDICT as a segment-by-segment rebuild — are false as written, as is
the `M-VERBATIMDRIFT` gate label.

Those three are corrections of record, not cosmetic edits; MAJOR-1 is a
second occurrence of an engraved minimum. If the adjudicator's standing
rule is that no false claim about the instrument may survive in a
delivered paper, this grade converts to REJECT on that rule alone — I
record the finding and leave the rule to the adjudicator.
