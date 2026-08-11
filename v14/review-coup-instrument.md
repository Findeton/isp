# K3 INSTRUMENT — hostile review of paper-20 (the coupling unit)

**Seat:** K3 INSTRUMENT, panel protocol frozen at v14 ledger #180.
**Object at 9b1860e**, hashes verified at the start of this review and again
at the end, unchanged in both places:

| object | sha256-12 |
|---|---|
| `v14/paper-20-coupling.md` | `b328a8278fac` |
| `v14/code/coupling_exact.py` | `9e71cf511ab3` |
| `v14/code/coupling_output.txt` | `3e3d04222782` |
| `v14/code/coupling_receipt.json` | `3ca0308b6c19` |
| `v14/note-coupling-pin.md` (pin) | `7c6e9e44fc2c` |

The blob at `9b1860e` and at `HEAD` (`2c00e29`) are the same object for all
four artifacts. Concurrent workers' uncommitted files (`cra_*`,
`r4c_*`, `r4dec_*`, `r5m_*`, `paper-22`, `paper-23`) are disclaimed and were
never read. My single repo write is this file.

---

## GRADE: **AWF** — accept with fixes

Four MAJOR findings, eleven MINOR. **Within the domain this seat tests — the
paper against the receipt and the transcript, and the receipt against itself —
no false computed number was found**: every table in the paper recomputes
exactly from the receipt, the delivery is byte-reproducible off-tree across two
`PYTHONHASHSEED` values, and all 44 declared falsifiers die at the gate they
name when run cold, one OS process each, outside the harness. Nothing *I* found
overturns the headline or any measured quantity, and every repair below is
local and touches no measurement.

**Scope note, recorded because it cuts against an unqualified reading of the
line above.** This seat does not re-derive the physics: the composition
census, the two §3 theorems (the monomial-only scalar shape and the
S_3-covariant coin scan), the transport identity, the battery semantics and
the ladder are K1's and K2's rows, and I took their values as given except
where I recomputed them *from the receipt* to check the paper against it. That
check cannot detect a census that is internally consistent and wrong. The K2
effectus review, landed at #182 while this seat was running, reports exactly
such a case (the coin-forcing solution count). My "no false computed number"
claim is therefore a statement about paper↔artifact consistency and
reproducibility, **not** about the correctness of the underlying censuses.

The unit is the strongest instrument of the era on almost every axis I
attacked. The four MAJORs are: one genuine hole in the terminal seal that the
#119-totality discipline exists to close and does not close here; one
paper-perimeter gap that lets three corruptions of the *delivered* paper ship
with exit 0; one battery row that measures a different quantity from the one
it pre-registers and duplicates its neighbour; and three declared falsifiers
whose published `what_it_does` is not what they do — the same disease the
worker self-found, one layer further down.

---

## WHAT I RAN

**132 process executions**, all off-tree in
`scratchpad/coup-in/` on provisioned git-less mirrors; **≈367 independent
recomputations**. Breakdown of the recomputations: 16 pinned-source
sha256-12 re-verified from the bytes; 5 object hashes ×2 (start and end);
4 byte-identity comparisons; 11 verbatim anchors located + 44 of my own
perturbations + 44 of my own re-wrappings; 5 `paper_coverage` fields
recomputed; 46 distinct paper numerals checked against the receipt;
5 consistency per-class rows + their sum; 5 law-transport counts; 24 ensemble
branch/leaf counts; 8 K6/K7 battery cells; 12 head-reconstruction identities;
3 fenced-block multiset identities; 11 registry cardinalities; 27 sealed-path
population orderings; 44 mutant declared-vs-observed gates; 16 break-anchor
falsifiers; 20 AST probe fields; and the remainder in gate-set differences and
static audits.

---

## 1. THE SEAL MECHANISM — verdict

### 1.1 The snapshot is 50+2, not 49+3

The protocol's "49+3" is a mis-statement of the object, and the object itself
publishes **three different gate cardinalities without distinguishing them**:

- `GATE_REGISTRY` / `--list-gates` / `coverage.gates` / `coverage.declared_registry` = **52**
- `len(R["gates"])`, the *sealed snapshot* = **50**
- `totals.gates` and G-PAPER-COVERAGE-FINAL's *"the payload closes: 49 gates evaluated, all passed"* = **49**

`R["gates"] = [dict(g) for g in LD.rows]` (L3280) is taken after
G-PAPER-COVERAGE-FINAL, so the snapshot holds 50 rows; `R["totals"]` is built
at L3251, one gate earlier, so it holds 49. **Exactly two gates are outside
the snapshot**: `G-SEAL-COMPLETE` and `G-ARTIFACT-INTEGRITY` (verified:
`set(--list-gates) − {g["gate"] for g in R["gates"]}` = exactly those two;
the reverse difference is empty).

### 1.2 The post-snapshot gates: what actually guards them

I built the injection the protocol asked for — drop / rename / weaken each
post-snapshot gate — and ran all four variants as full deliveries. The result
is sharper than "the hole exists":

**`G-SEAL-COMPLETE` is well guarded, and not by the seal.** Renaming it (I6)
and weakening its predicate to `True` (I7) both die at **`G-MUTANTS-ON-TARGET`**,
because three declared falsifiers (`MUT-SEAL-DROP`, `MUT-SEAL-BROKEN`,
`MUT-TRANSCRIPT-FLIP`) name it as their gate and the in-process sweep notices
they stopped landing there (I6: "on target 41 of 44"; I7: "MUT-SEAL-DROP died
at None"). **The mutant sweep, not the seal, is the guard on a post-snapshot
gate's identity and predicate.** That is a real and elegant property of this
design and it should be stated in the ledger, because it is what makes the
50+2 shape defensible at all.

**`G-ARTIFACT-INTEGRITY` is guarded by nothing** — and the reason is exactly
that it is the one post-snapshot gate with **no mutant**. It carries the
waiver `EXERCISED-IN-RUN`. The waiver is honest about *why* — a mutant on it
is unreachable, because `run_mutant` calls `finish(write=False)`, which
returns before the terminal gate ever runs — but the consequence is the hole:

> **MAJOR-1. Removing or renaming the terminal integrity gate produces
> artifacts that are byte-identical to the delivered ones.**

Verified twice, as full deliveries (I4, I5): exit 0, and `cmp` reports the
produced `coupling_receipt.json` **and** `coupling_output.txt` byte-identical
to the committed artifacts. This falsifies the warrant the unit prints in
`closing_gates.warrant` and seals:

> "that verdict is recorded instead by the artifacts themselves, since a run
> which fails any gate writes nothing and the staged bytes are moved into
> place only after it passes."

The artifacts record nothing of the kind: they are the same bytes whether or
not the gate ran. `late_ok` at L3353 checks names in the *live* ledger, but it
is computed inside the very gate whose existence is in question, so it cannot
attest to itself; `coverage.late_gates` and `closing_gates.names` are typed
constants (`list(LATE_GATES)`, `LATE_GATES[1:]`), not evidence of execution.

### 1.3 The seal catches everything it claims to catch, inside its perimeter

The modern playbook lands where it should. Post-gate head flip (I1) dies at
`G-SEAL-COMPLETE` with `seals broken at close ['SEAL-VERDICT']`. Census-row
move in the seal→disk window (I2) and post-write receipt corruption of a
sealed key (I3) both die at `G-ARTIFACT-INTEGRITY` with the broken seal named
(`SEAL-CONSISTENCY`, `SEAL-COUNTS`). All three: exit 1, `os.replace` never
reached, delivered artifacts untouched. The disk-vs-seal discipline is real.

**But the perimeter has two measured gaps**, both demonstrated:

> **MAJOR-2a. Only the first 40 lines of the transcript are covered.**
> `head_ok` compares `read_text(tmp_t).split("\n")[:40]` against the sealed
> `transcript_head`. The delivered transcript is 181 lines. I corrupted line
> 88 — a gate's own evidence line — between the staged write and the read-back
> (I3b): **exit 0, and the forged transcript shipped.** The delivered
> `coupling_output.txt` then reads `consistency violations 0 of 111111 checks`
> while the byte-identical-to-gold receipt says `948297`. The two published
> artifacts disagree and no gate noticed.

> **MAJOR-2b. The four `DECLARED_UNSEALED` receipt keys are outside the
> disk-vs-seal comparison — and one of them is the receipt's own digest.**
> I overwrote `python` and `payload_sha256_12` on the staged receipt before
> read-back (I3c): **exit 0, and the receipt shipped carrying
> `"python": "9.9.9-FORGED"` and `"payload_sha256_12": "deadbeefcafe"`**, every
> other key identical. A later reader who verifies the receipt by its own
> `payload_sha256_12` is verifying an unauthenticated field.

**Repairs (all local, none touches a measurement):**

1. **MAJOR-1** — seal the *shape of the writer*, which is measurable before the
   snapshot and therefore sealable without circularity. The file already
   AST-parses itself twice (L1819, L3522). Add, evaluated before
   `R["gates"]` is taken, a `G-WRITER-SHAPE` gate over

   ```
   fn = the finish() FunctionDef
   gate_names_in_finish            = [c.args[0].value for LD.gate(...) calls in fn]
   terminal_gate_present_exactly_once
   os_replace_calls                = count of .replace(...) calls in fn
   every_replace_after_the_terminal_gate = all(r.lineno > integ.lineno)
   ```

   published as a new receipt key and a new `SEALED_PATHS` row
   (`SEAL-WRITER-SHAPE`), with one mutant that drops the terminal name from
   the list. **I implemented and tested this probe.** On the delivered file it
   returns `gate_names_in_finish = ['G-COVERAGE', 'G-SWEEP-BOUND',
   'G-ANCHOR-CONSUMERS', 'G-REACHABILITY', 'G-PAPER-COVERAGE-FINAL',
   'G-SEAL-COMPLETE', 'G-ARTIFACT-INTEGRITY']`, `terminal_gate_present_exactly_once
   True`, `os_replace_calls 2`, `every_replace_after_the_terminal_gate True`;
   and it **differs from gold on the I4 drop, the I5 rename, and on moving an
   `os.replace` above the gate.** It does not differ on the I7 weakening — but
   I7 is already caught by the sweep, so the two mechanisms together close the
   loop.
2. **MAJOR-2a** — `Seal.close` already stores `payload_sha`; store
   `text_sha = digest(text)` beside it and add
   `digest(read_text(tmp_t)) == SEAL.text_sha` to the `G-ARTIFACT-INTEGRITY`
   conjunction. Three lines; keeps the receipt total (no new key).
3. **MAJOR-2b** — either move `payload_sha256_12` out of `DECLARED_UNSEALED`
   (it is assigned after the seal, so seal it over the *staged bytes* instead:
   compare `digest(read_text(tmp_j))` to a value fixed at close), or add
   `back["python"] == R["python"]` and
   `back["payload_sha256_12"] == SEAL.payload_sha` to the integrity
   conjunction. The second is two lines and needs no restructuring.
   `seal_manifest` should also be checked against `SEAL.rows` on read-back.

### 1.4 Seal-mechanism verdict, in one line

**The seal is total over the receipt's measured layer and honest about
disk-vs-seal; its identity guard on post-snapshot gates is carried by the
mutant sweep rather than by the seal, which works for `G-SEAL-COMPLETE` and
fails for the one gate that has no mutant; and its coverage of the second
artifact stops at line 40 of 181.**

---

## 2. THE INJECTION TABLE

Every row is an off-tree full run against a work dir seeded with the committed
artifacts, so "wrote nothing" means *those exact bytes did not move*.

| # | what | where | caught by | exit | wrote nothing |
|---|---|---|---|---|---|
| I1 | post-gate head flip: `R["verdict"]["gates"]` rewritten `NOT-REQUIRED`→`AND-REQUIRED-K9-SOURCING` after `SEAL-VERDICT` | `full_run`, after L2676 | **G-SEAL-COMPLETE** (`seals broken at close ['SEAL-VERDICT']`) | 1 | yes |
| I2 | census-row move: `R["consistency"]["violations"] = 7` in the seal→disk window | `finish`, before the staged write | **G-ARTIFACT-INTEGRITY** (`broken on disk ['SEAL-CONSISTENCY']`) | 1 | yes |
| I3 | post-write corruption of a **sealed** receipt key (`counts.horizon`→99), staged file rewritten before read-back | `finish`, before L3345 | **G-ARTIFACT-INTEGRITY** (`['SEAL-COUNTS']`) | 1 | yes |
| I3b | post-write corruption of the **transcript at line 88** (>40) | same window | **NOTHING** | **0** | **no — forged `coupling_output.txt` shipped** |
| I3c | post-write corruption of `python` and `payload_sha256_12` (DECLARED-UNSEALED) | same window | **NOTHING** | **0** | **no — forged `coupling_receipt.json` shipped** |
| I4 | **drop** the terminal gate (`LD.gate(...)` → no-op lambda) | `finish` L3358 | **NOTHING** | **0** | yes — *artifacts byte-identical to the delivered ones* |
| I5 | **rename** the terminal gate | `finish` L3358 | **NOTHING** | **0** | yes — *byte-identical* |
| I6 | **rename** `G-SEAL-COMPLETE` | `finish` L3315 | **G-MUTANTS-ON-TARGET** (41/44; the three seal falsifiers miss) | 1 | yes |
| I7 | **weaken** `G-SEAL-COMPLETE` to `True` **+** post-seal census corruption | `finish` L3325 + L3337 | **G-MUTANTS-ON-TARGET** (`MUT-SEAL-DROP died at None`) | 1 | yes |
| I8 | **no-op falsifier**: `pick("MUT-KERNEL", kviol, kviol)` | L2193 | **G-MUTANTS-ON-TARGET** (`MUT-KERNEL died at None`) | 1 | yes |
| I9 | writer added **lexically inside** `finish` | `finish`, before L3345 | **G-SELFTEST-WRITES-NOTHING** (the AST guard is live) | 1 | yes |
| P1 | paper: claim numeral `948,297`→`948,298` in §6 | object under test | **G-PAPER-CLAIMS** | 1 | yes |
| P2 | paper: §6 table row `\| norm \| 45,157 \|` → `406,413` | object under test | **NOTHING** | **0** | yes |
| P3 | paper: §8.1 `K6-BLOCH` row frozen/coupled **swapped** | object under test | **NOTHING** | **0** | yes |
| P4 | paper: **one of the two copies** of the arena verdict fence, `27 OF 27`→`22 OF 27` (§12's copy) | object under test | **NOTHING** | **0** | yes |
| P5 | paper: mandatory Lorentz naming sentence deleted | object under test | **G-WALL-LORENTZ-NAMED** | 1 | yes |
| P6 | paper: retracted L-1 sentence injected | object under test | **G-WALL-L1** | 1 | yes |
| P7 | paper: polarity flip, "the coin register is forced"→"is a declared choice" | object under test | **G-PAPER-CLAIM-POLARITY** | 1 | yes |
| P8 | paper: `2,455`→`2,456` in §8.3 prose | object under test | **G-PAPER-NUMERAL-COVERAGE** | 1 | yes |
| P9 | control under label: `--verify-paper` pointed at paper-19 | object under test | **G-WALL-LORENTZ-NAMED** | 1 | yes |
| P10 | #125 probe: the §6 claim re-wrapped, blockquoted **and** list-prefixed | object under test | (by design: still located) | 0 | yes |
| — | seal-then-edit-source: `d66_arbitration_crystal_exact.py` appended on disk | pinned source | **G-PROVENANCE** (`mismatched anchors: ['A-D66']`) | 1 | yes |
| — | paper appended on disk with a foreign numeral `999999999` | object under test | **G-PAPER-NUMERAL-COVERAGE** | 1 | yes |
| — | bare copy of the driver alone, no repo around it | off-tree | `FileNotFoundError` at the first pinned read | 1 | yes (only the `.py` in the dir) |

**Fifteen injections are caught by a NAMED gate** with exit ≠ 0 and nothing
written (I1, I2, I3, I6, I7, I8, I9, P1, P5, P6, P7, P8, P9, the on-disk
source drift, and the on-disk paper append); a sixteenth — the bare copy — is
refused by a loud abort that is not a gate, also writing nothing.
**Seven survive**: I3b, I3c, I4, I5 (MAJOR-1 and MAJOR-2) and P2, P3, P4
(MAJOR-3). P10 survives by design and is the #125 control.

---

## 3. MAJOR FINDINGS

### MAJOR-1 — the terminal gate is byte-invisible

Stated and repaired in §1.2 above. Severity: it is the one place where the
#119 chain does not terminate in something the artifacts witness, and the unit
prints a sealed warrant claiming that it does.

### MAJOR-2 — the disk-vs-seal perimeter has two holes

Stated and repaired in §1.3 above (transcript beyond line 40; the four
declared-unsealed keys, including the payload digest).

### MAJOR-3 — the paper is only partly inside the vouched perimeter

The CR-A instrument found paper corruption surviving. This unit's era
machinery catches far more of it — six of my nine paper injections die at a
named gate, including the wrong-paper substitution and an on-disk append. But
three survive, and they are not obscure:

- **P2**: `| norm | 45,157 | 0 |` → `| norm | 406,413 | 0 |` in §6. That table
  is the decomposition of the headline 948,297 (I verified the five rows sum
  to exactly 948,297); after the edit it does not, and §6's own bolded claim
  still says 948,297. Exit 0.
- **P3**: §8.1's `K6-BLOCH` row swapped to `**fails** | holds`. The paper then
  contradicts its own fenced head twenty lines earlier, which lists
  `K6-BLOCH` under `PASS-FROZEN-FAIL-COUPLED`. Exit 0.
- **P4**: the arena verdict fence appears **twice** (the head and §12). I
  corrupted §12's copy to `22 OF 27 CELLS`. `G-PAPER-HEAD-VERBATIM` tests
  `canon(seg) not in canon(ptext)` — containment — so the clean head copy
  satisfies it. Exit 0. *This is the block the corpus quotes.*

Measured cause, two parts. (i) The head gate is containment, not equality or
multiplicity. (ii) The numeral allowlist is `receipt_numbers(R)` — every
numeral anywhere in the 105 KB receipt — plus a 51-entry hand list. I measured
its strength: it admits **118 of the 1000 integers 0–999** and 17 of the 9000
four-digit integers, and, decisively, it admits *every other true measurement
of the same run* (which is why P2 passes). I also audited the hand list for a
#24 leak and found none — **no numeral in the delivered paper is admitted only
by `NUM_ALLOW`; all 46 distinct paper numerals occur in the receipt** — but 26
of the 51 entries are dead, and one of the dead ones (`22`) is what let P4
through.

**Repairs, both verified feasible against the delivered paper:**

1. Gate the fenced blocks by **multiset equality**, not containment. I
   measured it on the delivered paper: 6 fenced blocks, 3 distinct, each of
   the three derived segments appears **exactly twice**, and every fenced
   block *is* one of the three segments. So
   `Counter(canon(b) for b in blocks) == {canon(seg): 2 for seg in verdict}`
   holds today and would have failed P4. Publish the multiplicity as data.
2. Render §6's five class rows and §8.1's twenty battery cells as
   `paper_claims` entries. The mechanism is already there (`match_needle`
   against assembled sentences) and costs nine more claims of the same shape;
   it would have failed both P2 and P3.
3. Prune `NUM_ALLOW` to the entries actually consumed (25 of 51 today).

### MAJOR-4 — three declared falsifiers do not do what the receipt says they do

This is the disease the worker self-found (`R["mutants"]` unpopulated; two
no-op mutants), swept one layer down. **The worker's three repairs are
verified good** — see §5 — but the same family survives in three more places,
and `mutants[i].what_it_does` is published in the receipt as data:

- **`MUT-TRANSPORT-ASSUMED`** publishes *"declares the transport to hold
  without evaluating its own conjuncts"*. It does the opposite:
  `transport_ok = pick("MUT-TRANSPORT-ASSUMED", transport_ok, False)` (L2230)
  asserts the transport **fails**. A mutant that actually assumed the
  transport would *pass*. Worse, the row `G-LAW-TRANSPORT` advertises as *"its
  CONTENT — the row that could have failed"* is `mdviol`, the 187,155
  menu-mass-is-Born-mass checks — and **no falsifier anywhere in the file
  moves `mdviol`** (I grepped every site: L1224/1226 counts it, L2194-2195
  aggregates it, L2229/2239-2259 consume it; no `pick`). §4 of the paper is
  built on that row.
- **`MUT-FIBER-BLIND`** publishes *"reports a declared fiber as measured when
  its members were never run"*; `measured_members = pick(..., False)` (L2145)
  reports them as **not** measured. And the honest value is a tautology:
  `len({fibers["ORDER-GD"], fibers["ORDER-DG"]}) >= 1 and ...` (L2140-2144) is
  `True` whenever the keys exist, which they always do. The gate's
  execution leg **cannot fail**. (The members genuinely *are* run — `run_arm`
  at L1461/1481/1484 — so nothing published is false; the gate simply does not
  check it.)
- **`MUT-PRUNE`** publishes *"drops the lightest branch of the emission tree"*;
  `pruned = pick("MUT-PRUNE", 0, 1)` (L2286) flips a **hard-coded literal**.
  `"pruned_branches": 0` is published in the receipt as if measured. The
  source comment at L2276 announces *"#24, two routes: the branch count at
  each level, recomputed from the emission supports rather than read off the
  list that was built"* — that second route **is not implemented**; the loop
  below it only tests `lv["branches"] <= 0`, and `branches` is
  `len(frontier)`, one route (L1280).
  *Mitigating, and it should be said:* exhaustiveness **is** genuinely
  protected — by `G-BRANCH-MASS`, whose exact level-mass-equals-1 at all 20
  levels would break if any branch were dropped. It is the gate that *names*
  exhaustiveness that is weak, not the property.

**Repairs:** point each falsifier at the measured quantity —
`mdviol = pick("MUT-TRANSPORT-ASSUMED", mdviol, 4)` (and rename it, or add
`MUT-MASS-DENSITY`); replace `measured_members` with an explicit list of
fiber members actually executed, recorded by `raw_census`, gated by set
equality against the declared members, with the mutant dropping one id; and
implement the second branch-count route the comment already promises. Correct
the three `what_it_does` strings.

---

## 4. MINOR FINDINGS

1. **Three gate cardinalities, undistinguished** (§1.1): 52 / 50 / 49. The
   most quotable of them — the console banner `TOTALS: 16 sources, 11 verbatim
   anchors, 49 gates, 44 mutants, 27 seals, ...` — **is not in the archived
   transcript at all**: `emit_report` runs after `text` is frozen, so stdout is
   189 lines and `coupling_output.txt` is 181. Repair: move `emit_report`
   inside `finish` before `text` is built, and publish the three counts under
   three names (`gates_before_the_snapshot`, `gates_in_the_sealed_snapshot`,
   `gates_in_the_registry`).
2. **G-COVERAGE's enumeration does not add up.** "45 already closed, plus this
   gate and its twin (2), plus the sweep-binding and anchor-consumer gates (2),
   plus the 3 LATE gates, plus the sweep gate the delivery pipeline evaluates
   around it (1)" = 53, against a denominator of 52. `G-MUTANTS-ON-TARGET` is
   already inside the 45 — the output shows it passing immediately before
   G-COVERAGE. The computed numbers (52/45/40/12) are all right; only the
   English clause double-counts. Repair: delete "plus the sweep gate ...".
3. **Two waiver forcings overstate the code.** `G-ARTIFACT-INTEGRITY`'s says
   *"the run corrupts a written byte"*; the probe (L3346-3349) mutates an
   in-memory copy of the read-back object and exercises exactly **one** of the
   27 seal rows (`SEAL-COUNTS`). Repair: probe all 27 in turn and publish the
   count. `G-READS-DECLARED`'s says *"the read list is appended by the only
   reader in the file"*; `read_text` is a second, untracked reader used at five
   sites (L1819, L3345, L3351, L3522, L3621).
4. **The module docstring's `#46/#91` sentence is false as written.** *"Exactly
   16 files are read at run time as SOURCES ... plus exactly one file read as
   the OBJECT UNDER TEST ... No repository state outside them is read."* The
   run also reads **this file itself**, twice (L1819, L3522). Repair: say so,
   and gate the object-read set (`{SELF, paper_path}`) the way `READS` is
   gated.
5. **`G-NO-SUBPROCESS` is narrower than its sentence.** It scans the driver's
   own import names against `{subprocess, multiprocessing, socket, shutil}`.
   `os` is imported and `os.system/popen/exec*/spawn*` are not scanned; and
   the two `exec(compile(...))` calls (L688, L732) run pinned third-party
   source in a namespace explicitly handed `os` and `sys` (L728-730). Pinned shas
   make this theoretical, but the gate should scan attribute calls too, and
   scan the exec'd bodies.
6. **`G-SLICE-EXIT-FREE` is evaluated after the slice has already run.**
   `Grammar.__init__` execs the d42b1 slice at L688 and the extracted bodies at
   L732 (via `_extract`, called at L696 and L701), and only then computes
   `slice_exit_free` (L707) and `bodies_exit_free` (L709). A slice calling
   `sys.exit` would end the process
   before the gate could refuse it. Repair: compute both before the first
   `exec`.
7. **Two reduced horizons are undisclosed in the paper.** The
   staleness-blindness theorem is measured at `FIBER_T = 3`
   (`run_arm(FIBER_T, False, "A", n0=stale_field(), ...)`, L1494) and the
   terminal-condition falsifier at horizon 2 (L1496), but §8.3, §4, both gate
   statements and `battery.staleness_blindness` state neither — while §11 and
   §13.5 are scrupulous about disclosing horizon 3 for the fibers. (I verified
   the 2,455 figure: the eleven `staleness_blindness.checks` entries sum to
   exactly 2455.) Repair: add "at the reduced horizon 3" to §8.3 and to
   `G-STALENESS-BLIND`, and publish `staleness_blindness.horizon`.
8. **Two falsifiers are tautological rather than mechanical.**
   `MUT-SELFTEST-WRITES` is wired straight into its predicate
   (`st_ok and not mut(...)`, L3556) and never exercises `selftest_shape`;
   `MUT-CLI-PERMISSIVE` sets `bad = [["--nope"]]` (L3537) rather than routing
   `cli_selftest` through `parse_args_permissive`, which is what its
   `what_it_does` claims. Both underlying checks are independently live at my
   hands (I9 kills the AST guard; my 37-vector argv sweep exercises the
   whitelist), so this costs truth nothing and falsifier honesty something.
   `MUT-WALL-LORENTZ` / `MUT-WALL-HEX` likewise set `lz`/`hx` to `False`
   rather than deleting the sentence — my P5 shows the real deletion is caught.
9. **`--mutant NAME` exits 1 when the falsifier lands and 0 when it MISSES**
   (`return 1 if got == gate else 0`, L3628). A CI caller testing `exit == 0`
   reads a dead falsifier as success. The delivery's own
   `G-MUTANTS-ON-TARGET` does catch it (I8), so this is a CLI-contract nit;
   repair: exit 1 on the kill, 3 on a miss.
10. **The `NO-WITNESS` label is typed in both builder and comparator.**
    `"G-CONSISTENCY=PASS"`, `"G-NONTRIVIALITY=PASS"` and
    `"G-REQUIREMENT=NO-WITNESS("` are literals in `build_verdict` (L2832-2833)
    *and* in `reconstruct` (L2932-2943). The first two are forced (a failing
    gate raises before the head is built). The third is not: had a witness
    existed, `outcome_word` would return
    `COUPLING-CONSISTENT-AND-REQUIRED-<id>` while the same segment still read
    `G-REQUIREMENT=NO-WITNESS(1 CLOSURES ...)`. Latent, not live — the
    comparator's independence is textual duplication, so it catches value
    forgeries (its stated job, and `MUT-VERDICT-VALUE` demonstrates it) but
    cannot catch a template error duplicated on both sides. Repair: derive the
    label as `("NO-WITNESS" if not wits else "REQUIRED-%s" % wits[0])` in both.
11. **`G-ISOS-CITED`'s citation leg is weaker than it reads.** Its first
    pattern `r'"isos": 1296'` matches **zero** times in the weld receipt (that
    key is named otherwise), so `isos_found` reduces to a bare substring search
    for `1296` in 137 KB of JSON — 19 hits, which is what
    `occurrences_in_weld_receipt: 19` correctly reports, and the gate only
    needs `> 0`. `aut = 6*6*6*6` (L1973) is assigned and never used. Repair: locate the weld
    receipt's actual key and require the number under it.

Also noted, non-blocking: the comment at L2604-2607 says *"`--numbers` carries
no paper by contract"*, but `main` loads `paper_text` for every mode, so the
two naming walls **do** run under `--numbers` (the safe direction — I
confirmed 38 gates there, consistent with 52 − 10 skipped).

---

## 5. THE WORKER'S SELF-FOUND BUG — repairs verified, disease swept

**Repair 1 — `R["mutants"]` was an unpopulated sealed path.** Verified fixed:
`R["mutants"]` is assigned at L3173, `SEAL.take("SEAL-MUTANTS", R)` at L3194,
with the reasoning recorded in the comment at L3170-3172. **I swept all 27
sealed paths statically for the same ordering hazard** — for each, the earliest
assignment (or `setdefault`) line against the earliest `SEAL.take` line — and
**every one is populated first**; the sole apparent exception, `SEAL-SCHEMA`,
is populated by `R = {"schema": SCHEMA}` at L1777, before the first take at
L1816. In a delivery run `mutant_sweep` is populated at L3650 (in `main`)
before `finish`; the `setdefault` at L3199 keeps the manifest total in the
mutant sub-pipeline. No residual unpopulated sealed path.

**Repair 2 — the mid-word needle split.** Verified fixed and correctly
reasoned: `MUT-WALL-L1` cuts at `BANNED_L1.index(" ", 40)` (L2555) and rebuilds
across the newline, so `canon`'s whitespace collapse restores the needle. The
comment at L2552-2554 states exactly why a mid-word split would have made the
falsifier a no-op.

**Repair 3 — the substring absent from the claim.** Verified: `C01` contains
the literal `27 cells`, so `sent.replace("27 cells", "26 cells")` (L2691) is a
real corruption.

**Sweep for the same diseases:**

- *Every mutant needle present verbatim in its target*: I checked all
  `.replace`/slice-based hooks. `MUT-VERDICT-WORD`'s `NOT-REQUIRED` needle,
  `MUT-VERDICT-VALUE`'s `27 OF 27`, `MUT-PAPER-CLAIM`'s `27 cells`,
  `MUT-PAPER-HEAD`'s `seg[:-1]+"Z"`, and the three wall injections' needles
  (`boost`, `myrheim`, `cosmolog` — all lowercase, matching the lowercased
  measurement layer) are each present. **No dead needle.**
- *No-op falsifiers*: **none survive**, and the machinery detects the class —
  I injected one (I8) and the delivery died at `G-MUTANTS-ON-TARGET` with
  `MUT-KERNEL died at None`. What I did find is the weaker cousin: three
  falsifiers whose *published description* is not their mechanism
  (MAJOR-4) and two that are tautologically wired (MINOR-8).
- *Census-cache contamination*: `raw_census` memoizes into `RAW` and the 44
  in-process mutants share it. I checked every hook for in-place mutation of a
  cached object: all take copies (`list(raw["n_driven"])`, `set(raw["pairs"])`,
  `dict(raw["coin"])`, `dict(raw["conn"])`) or rebind locals. **No mutant
  writes into `RAW`.** My out-of-harness sweep is the independent cold-cache
  confirmation and it agrees 44/44.

---

## 6. THE 44-MUTANT SWEEP, OUTSIDE THE HARNESS

One OS process per falsifier (`--mutant NAME`), cold cache, six-way parallel,
on a provisioned git-less mirror, with the delivered artifacts hashed before
and after **every single run**:

```
rows 44   on-target 44   off-target 0
died at NONE: 0
exit codes: {1: 44}
artifacts untouched in every run: 44/44
distinct declared gates hit: 40   (matches coverage.gates_with_a_mutant = 40)
```

**Zero false waivers.** The 12 waived gates are exactly the 52 − 40 with no
mutant, and I audited each forcing:

| gate | class | forcing holds? |
|---|---|---|
| G-PROVENANCE | FALSIFIED-BY-A-FLAG | **yes, measured** — I ran `--break-anchor` on all **16** source ids; all 16 die at G-PROVENANCE, exit ≠ 0, artifacts untouched. Also confirmed by a real on-disk edit of `d66_arbitration_crystal_exact.py`. |
| G-EXACT-ARITHMETIC | SELF-SCANNING | yes — AST float-literal scan; I also checked the one `Div` node (L1362, `Fraction/int`) for a runtime float leak: none. |
| G-NO-SUBPROCESS | SELF-SCANNING | yes but narrow — see MINOR-5 |
| G-READS-DECLARED | STRUCTURAL | forcing wording wrong — see MINOR-3/4 |
| G-VERBATIM | SELF-FALSIFYING-PER-ROW | **yes, and I re-ran it myself** — see §7 |
| G-SLICE-EXIT-FREE | SOURCE-FORCED | yes (and see MINOR-6 on its ordering) |
| G-ANCHOR-CONSUMERS | STRUCTURAL | yes — 11 consumers, all registered and evaluated |
| G-COVERAGE / G-REACHABILITY / G-MUTANTS-ON-TARGET | SELF-REFERENTIAL | yes; G-MUTANTS-ON-TARGET's liveness demonstrated by I8 |
| G-ARTIFACT-INTEGRITY | EXERCISED-IN-RUN | **this waiver is MAJOR-1** — the forcing is about the gate's internal probe, not its existence, and the probe covers 1 of 27 seals |
| G-PAPER-COVERAGE-FINAL | AGGREGATE | yes |

`R["reachability"]["dead_falsifiers"]` is empty and I confirmed it
independently: every declared gate is in the registry, and every one is either
in the 50-row snapshot or is one of the two named post-snapshot gates.

---

## 7. WHAT I VERIFIED CLEAN

- **Byte reproducibility ×2, off-tree and git-less.** A provisioned mirror
  containing only the 16 pinned sources + the paper + the driver, no `.git`,
  run under `PYTHONHASHSEED=0` and `PYTHONHASHSEED=987654321`: both produce
  `coupling_output.txt` `3e3d04222782` and `coupling_receipt.json`
  `3ca0308b6c19` — **byte-identical to the committed artifacts**.
- **#91 at its own hands.** A bare copy of the driver with no repo around it
  dies with `FileNotFoundError` on the first pinned read, exit 1, and **writes
  nothing** (the directory afterwards contains only the `.py`). Designed
  behaviour, confirmed.
- **CLI, 37 hostile vectors, all exit 2, no writes.** Including every
  trailing-argument arity case the protocol flagged: `--selftest EXTRA`,
  `--list-gates EXTRA`, `--list-mutants EXTRA`, `--numbers EXTRA`,
  `--no-write EXTRA`, `--mutant MUT-KERNEL EXTRA`,
  `--break-anchor A-PIN EXTRA`, `--verify-paper x y`; plus `--mutant=X`,
  `--no-write=1`, `--no-w`, `--NO-WRITE`, `-h`, `--help`, `--`, `""`, `"  "`,
  and every second-mode composition. **No arity slop** — unlike CR-A, the
  whitelist test precedes every branch, so a trailing token can never be
  absorbed. `--verify-paper /nonexistent` → exit 2.
- **`--selftest`** corrupts `A-D42B1` in memory, dies at G-PROVENANCE, exits
  1, artifacts untouched.
- **#24 registry counts.** `--list-gates` prints 52 lines, 52 unique, equal to
  `coverage.declared_registry` and to `coverage.gates`; `--list-mutants`
  prints 44, equal to `totals.mutants`, to `len(R["mutants"])` and to
  `len(R["mutant_sweep"])`; 27 seals declared and 27 taken. `registry_drift`
  empty, independently confirmed both ways.
- **#20 with fenced-block polarity, in-run.** I recomputed `paper_coverage`
  offline against the committed receipt and got
  `scanned 341, allowed 341, fenced_blocks 6, fenced_numerals 118,
  unregistered []` — **exact match** with the receipt. All **46** distinct
  paper numerals occur in the receipt; none is admitted only by the hand list.
- **#125 on the prose gates, verified by me not by the run.** For each of the
  11 anchors I re-wrapped at every space, blockquoted every line, list-prefixed
  every line, and tab-substituted every space: **all 44 re-wrappings still
  locate**. And in the live run, P10 (a claim re-wrapped, blockquoted *and*
  list-prefixed simultaneously) still matched. The markdown-prefix
  normalisation is real.
- **The 11 verbatim anchors, perturbed by me.** All 11 present in their pinned
  source; all clear the 30-character floor (minimum 47 after canonicalisation);
  11 distinct consumer gates. I applied four perturbation kinds of my own to
  each: 43 of 44 flip. The one that does not (`V-CAT-KR` under my
  drop-a-word perturbation) is **not an instrument defect** — I checked, and
  `"must carry a Kleitman–Rothschild control"` is itself genuine text in
  `v11/note-v11p0a-reproduction-catalog.md`, so my perturbation happened to
  land on a real sentence. The unit's own per-row falsifier flips for all 11.
- **The head, reconstructed from the committed receipt.** All three segments:
  builder == comparator == `R["verdict"]` == the paper, and each appears
  **exactly twice** in the paper. `reconstruct` re-derives the outcome word
  from the receipt's own rows (`consistent=True inert=False witnesses=none`).
- **Every table in the paper recomputes exactly.** §6's five consistency
  classes (45,157 / 406,413 / 406,413 / 45,157 / 45,157) and their sum
  948,297; §4's law numbers (406,413 / 406,413 / 1,215,681 / 187,155 / 10);
  §5's four branch ladders and the leaf counts 284,078 / 212,382 / 314,928;
  §8.3's 2,455. **Zero false computed numbers.**
- **No silent caps, no sampling, no randomness.** `LADDER = (1,2,3,4,5)`,
  `HORIZON = 5`, `FIBER_T = 3`, `light=True` only drops the retained frontier.
  Branch expansion skips zero-weight cells only, and `G-BRANCH-MASS` proves
  the mass is exactly 1 at all 20 levels.
- **The seal's totality is real inside its perimeter**: 27 declared, 27 taken,
  no missing, no extra, no uncovered receipt key, `DECLARED_UNSEALED` frozen by
  content and length and measurement-free.

---

## 8. WHAT I DID NOT DO

I did not re-derive the physics — the census, the two coin theorems, the
transport identity, the battery semantics and the ladder are K1's and K2's
rows, and I took their numbers as given except where I recomputed them from
the receipt to check the paper against it. The K6/K7 duplication (MAJOR-4's
sibling, reported in §3) touches K2's licensure question and I flag it across:
**§8.2's "3 rows pass frozen and fail coupled" is 3 names but 2 distinct
conditions**, since `K6-BLOCH`'s coupled cell is
`Fraction(curvature_constant_probability) == 1` and `K7`'s is
`curvature_homogeneous`, which `horizon_stats` *defines* as `curv_const == 1`
(L1379) — the same predicate, identical on both readings — while `K6`'s frozen
cell is a typed `mf = True` (L1626). `K6`'s pre-registered statement is
translation covariance, and the instrument already computes the right quantity
for it (`count_field_translation_invariant` / `translation_invariant_probability`,
L1380-1381) and does not use it. The outcome word is unaffected (SYMMETRY-class
rows can never be witnesses). Repair: `mf`/`mc` from
`count_field_translation_invariant`, then re-check the pre-registered polarity.

---

## 9. SUMMARY FOR THE ADJUDICATOR

| row | verdict |
|---|---|
| the 50+2 gate-snapshot mechanism | **hole found and located exactly**: post-snapshot gates are guarded by the mutant sweep, not the seal; the one without a mutant (`G-ARTIFACT-INTEGRITY`) can be dropped or renamed with byte-identical output. Repair verified. |
| the total seal + vouching + chained ledger | **catches the whole modern playbook inside its perimeter**; perimeter stops at transcript line 40 and excludes the four declared-unsealed keys incl. the payload digest. Both demonstrated, both repaired in three lines each. |
| the worker's self-found bug | **all three repairs verified**; the disease swept clean (27/27 sealed paths ordered, no dead needle, no surviving no-op); a weaker cousin found in three mutants' published descriptions. |
| the 44-mutant sweep outside the harness | **44/44 on target, cold cache, exit 1 every time, artifacts untouched every time, zero false waivers**; 12 forcings audited, 16/16 break-anchors fire. |
| coverage: #20 fenced polarity, #34 reachability, #125 | **all three verified independently**, coverage recomputed exactly, 44/44 re-wrappings locate, 0 dead falsifiers. |
| CLI | **37/37 hostile vectors exit 2, no arity slop**; registry counts consistent 52/44/27. |
| byte ×2 off-tree | **exact**, two seeds, git-less mirror, bare copy dies writing nothing. |
| paper ↔ output ↔ receipt numerals | **clean** — 46/46 paper numerals in the receipt, every table recomputes, no #24 leak. Scope: consistency and reproducibility, not census correctness (see the scope note under the grade). |

**Grade: AWF.** The four MAJORs are repairs to the instrument, not to the
physics; none moves a number and none touches the verdict
`COUPLING-CONSISTENT-NOT-REQUIRED` **on this seat's evidence** — the
licensure of the §3 claims is K1/K2's row, and #182 has already moved one of
them.

Objects re-verified at the close of this review: `b328a8278fac` /
`9e71cf511ab3` / `3e3d04222782` / `3ca0308b6c19`, pin `7c6e9e44fc2c` — all
unchanged.
