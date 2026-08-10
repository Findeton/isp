# Γ-PREP (paper-11, the transport foundation) — OPERATOR-LENS HOSTILE REVIEW

**Reviewer lens:** the from-scratch rebuild. Nothing imported from the
unit's code. Protocol: `v14/note-gprep-hostile-protocol.md`
`b00a0be5c1ce`. Object reviewed at the shas the protocol names, all
verified before use.

## GRADE: **ACCEPT-WITH-FIXES**

**164 independent recomputations** — 118 receipt-level quantities
rebuilt end-to-end and reconciled (expanding to **553** individually
compared exact values, counted by machine, not typed), 15 quantities
the unit does not compute at all, 17 source-artifact sha
verifications, 2 full plain runs, 12 targeted checks.

**Zero false numbers.** Every measured quantity in the paper, the
output and the receipt reproduces exactly under a rebuild that shares
no data structure, no traversal order and no derivation route with the
unit. Four apparent mismatches in the machine reconciliation were all
pure representation differences (class *labels* under relabelling,
tuple-vs-list nesting, multiplicity-vs-repetition encoding), each
resolved by hand to identity.

**The headline survives.** I attacked
`GPREP-MINORIZATION-BLOCKED-AT-THE-MONOTONE-HOLDINGS-LADDER` from three
directions the unit did not run, and it held on two of them and needs a
qualifier on the third (MAJOR-4). The Birkhoff death is airtight. The
δ\* = 1 atoms are real.

The fixes below are disclosure, scope and discipline defects, not
science defects. Five are MAJOR because they touch what the receipt
*claims about itself* — the compliance sweep, the theorem-pass census,
the block coverage, the verdict's scope qualifiers, and one runtime
input that can silently degrade a paper headline to `None`.

---

## 1. What I rebuilt, and how it differs from the unit's route

| | the unit | this review |
|---|---|---|
| layer extraction | string index on `_ls.index('print("[d42b1')` → 16,129-char prefix | **AST surgery**: parse the layer, keep the module-body prefix of `Import`/`FunctionDef`/`ClassDef`/`Assign`/docstring nodes, stop at the first other node, recompile |
| family | `dict` keyed by tuples of event tuples, DFS with a list frontier | **integer-indexed forest**: `parent[] / ev[] / wt[] / depth[] / kids[] / menu[]`, breadth-first level by level |
| delivery-free partner | drop the `d` branch, add 1/4 to the transport idle weight | **re-evaluate the layer's own idle clause** with the delivery indicator forced false: `1 − ¼·[prop options] − ¼·[merge pairs or arb ckeys]`, through the layer's view predicates |
| potentials | recursive over the tuple-keyed cache | backward DP over integer ids, level by level |
| holdings / superseded / live | the layer's `View` object | **hand-rolled from the raw act list** — my own `vname`/`value_of`/`base_of`/`regs_of`/poset; `View` never constructed for the reduced predicate |
| partition refinement | `relabel` over `SK`-sorted dicts | my own total order `K`, my own signature dictionary, independent `relabel` |
| δ\* | `nstep_law` over tuple-keyed frontiers | measure propagation over integer ids with a separately memoised kernel table |
| ordering key | `SK` | `K` (different tag scheme, different tuple shape) |

**Cross-check earned by the difference:** my AST cut lands at source
line 422 — byte-for-byte the same prefix boundary the unit's string
index produces. Two unrelated methods agree on what "the pre-print
slice" is. Likewise the delivery-free census
`[1, 6, 32, 176, 976, 5280, 27904]` / 34,375 comes out identical from
the idle-clause route and the +¼ shortcut, so the unit's shortcut is
now independently licensed rather than merely asserted.

**Byte-identity.** Two plain runs on scratch copies. Run 2, with git
resolvable, regenerates `gprep_foundation_output.txt` = `097c08a0229d`
and `gprep_foundation_receipt.json` = `dd86ad1a80d7` — **exactly the
committed shas**. Run 1, in a scratch tree with no git object store,
differs in **exactly one key** (see MAJOR-2). Repo hashes unchanged
after all work; the unit was never run inside the repo.

**Provenance.** All 17 pinned source artifacts reproduce their pinned
sha256-12. The gate expectations are genuine pinned rows, not
re-declarations: I located the transport census, the per-level
breakdown, both potential columns, both ratio columns, R-SIG
5161 / R-MENU 1365 / 3796 / 0, the 4^n column, the (3/2)^n column, the
0.7705 mass, the delivery-free census and 34,375 in the committed
`v10/data/d70_horizon_limit_exact.out`, `…d44b…out`, `…d46b…out`,
`note-d70`, `paper31` and `paper32` bytes. Arm A is a recomputation
gated against pinned values, exactly as it says.

**T5's ledger number is right.** Reading the committed
`v10/LOG.md`, the entry *"D74 ROUND 1 ADJUDICATED AND TERMINAL: TH-II
WITH A FIND"* carries **(LEDGER #495)**; #494 is *"D74 DELIVERED
(GREEN-UNREVIEWED)"* and #492 is *"D74 PINNED"* — so the emitted
sentence's "green delivery immediately preceding" and "pin freeze" are
both true. The citability gap is real and is correctly closed.

---

## 2. K1 — THE SEVEN FACTS

All seven rebuilt from the pinned sources. **Zero mismatches**, and
every one is a genuine recomputation.

| fact | quantities rebuilt | result |
|---|---|---|
| F1 grammar | 5 kinds; kind counts; per-actor budgets `{1/4}`,`{1/4}`,`{1/2,1/4}`; mass census at d≤4/5/6; merge depths 5:72 6:2672; 72 merge-bearing histories; 350 re-deliveries; root menu | identical |
| F2 census + potentials | per level, cumulative, 243,769; partner 34,375; G₁..G₇ both scopes; both ratio columns; sign; first separation D=4 | identical |
| F3 kernels | 279,067 (history,horizon) pairs; 0 properness violations; 0 non-positive kernel entries; 0 non-positive potentials; raw cut masses; mis-normalised control 69/69 | identical |
| F4 ports | 5161/1365/1365/3796/0/3796; 4^n; (3/2)^n; completed masses; 1671053/2168717; closed form 497664/2168717 by both routes; 30,728 transitions, 0 shrinking, 4,340 nsup-shrinking; profiles | identical |
| F5 escape | 13 and 113 classes; growth and |Pₜ| tables both grains; 68 into 5 of 6; 76 into 32 of 17; factorisation 2/9 → 0/6; aggregate operator agrees | identical |
| F6 reopening | 1,044 diverged; 124 pairs; 84 prefixes; 4 minimal 3-chains at 1/256; 4 df shapes, 0 with `d`; 0 of 3,969 | identical |
| F7 symmetry | 521/0/0/0 × 3; one orbit per kind; `{d:1/2, n:1/2, p:1/4}` constant over r=1..7 | identical |

Two claims I checked beyond the receipt:

* **The escape witness is real.** §8.1 exhibits a depth-2 parent taking
  an `r` event at exactly 1/4 into a class whose shallowest member has
  length 3. I confirm such a transition exists (16 of the 68 are
  `r`@1/4 from depth 2), and further that **all five** escaping target
  classes have shallowest member length exactly 3 — the "strictly
  deeper than the window" clause holds for every escape, not just the
  exhibited one. The escape decomposes as
  `p@1/8: 16, d@1/8: 8, d@1/4: 12, r@1/4: 16, r@1/8: 16`, all from
  depth-2 parents.
* **§7's "exactly" is true as a set identity.** The 3,796
  non-menu-exact R-SIG points and the 3,796 re-entered ones are the
  *same set* (symmetric difference empty), not merely equinumerous.
  The gate is weaker than the prose — see MINOR-4.

---

## 3. K2 — ARM B, THE ATOMS (decisive)

### 3.1 The Birkhoff route's death — scope and airtightness

**Verdict: the proof is correct and the scope is correctly stated, but
it is a theorem of the representation, and two of its receipt keys are
typed rather than computed.**

The measurement `columns_single_parent = 243,768 of 243,768` is, as the
source comment honestly says, a measurement of the *multiplicity of a
history's last event in its parent's menu* — a history determines its
own prefix, so no other row can be a candidate. I recomputed the same
content from the other side: **the number of duplicated menu entries
anywhere in the family is 0** (over all 243,769 menus). That is the
only way the column census could have failed. The 2×2 minor
`[[1/4,0],[0,1/4]]` reproduces exactly.

The inference chain — off-diagonal zeros ⇒ infinite cross-ratio ⇒
Δ = ∞ ⇒ tanh(Δ/4) = 1, and disjoint descendant supports ⇒ δ = 0 for
every N — is mathematically airtight and correctly scoped to the
history level. It genuinely is "a theorem, not a cap", and §15.2 says
so. But see MAJOR-5 and MINOR-1.

### 3.2 The R-SIG holdings-profile block decomposition and δ\* = 1

Rebuilt independently. Every row of §11.4 and §11.5 reproduces exactly,
including the two long rationals
`3916670725604/3948076132837` and `290707648979/291881114879`, the
ν masses `1/4` and `3/4` on two Ψ-classes summing to 1, the block
windows, the depth supports, and the 4-of-6 grain split.

I also proved and machine-checked a lemma the unit does not state, and
which is what makes its two-grain measurement *decisive* rather than
two data points:

> **Coarsening lemma.** If Ψ′ coarsens Ψ then δ\*(C,N,Ψ′) ≥ δ\*(C,N,Ψ),
> because min\_x Σ\_{s∈S′} P^N(x,s) ≥ Σ\_{s∈S′} min\_x P^N(x,s).

The event×weight grain refines the kind×weight grain (the event
determines its kind), so the unit's control is strictly finer than its
primary. Checked on all four blocks: `event113 ≤ kind13 ≤
profile-unordered`, true on every row. **This is a free strengthening:
the atoms' δ\* = 1 at the 13-class grain implies δ\* = 1 at every
coarsening of it, and the full class's δ\* = 0 at 13 classes implies
δ\* = 0 at every refinement, including all six of T5's committed
abstractions** (each of which is finer than a 13-class menu partition
on this family). The unit's result is more robust than it claims.

### 3.3 Is `BLOCKED-AT-THE-MONOTONE-HOLDINGS-LADDER` the honest head?

I ran three attacks the unit did not.

**(a) Does any pinned fact unblock the ladder? No.** T5 supplies six
committed abstractions (SEQ 3969 / REC 2477 / MULT 578 / STATE 125 /
PORT 65 / MENU 113). All are refinements of, or finer than, the
13-class primary grain on this family, so by the coarsening lemma each
can only *lower* δ\*. The pinned inheritance strengthens the block; it
does not relieve it. The unit's decision to carry T5 "as an anchor, not
interpreted" costs it nothing here.

**(b) Does the obstruction coordinate itself unblock it, used as the
grain? No — and this is the strongest confirmation in the review.**
I ran δ\* on the full R-SIG class at Ψ = the holdings profile (ordered)
and at Ψ = the holdings profile (unordered) — both *coarser than or
incomparable to* the declared grains, and both the most natural
candidates given the unit's own diagnosis:

| N | points | kind13 | event113 | profile | profile-unordered | R-SIG indicator |
|---|---|---|---|---|---|---|
| 1 | 5161 | 0 / 0 | 0 / 0 | **0 / 0** | **0 / 0** | 5531/5564 / **1** |
| 2 | 689 | 0 / 0 | 0 / 0 | **0 / 0** | **0 / 0** | 34359971/34588859 / **1** |
| 3 | 105 | 12420/2168717 / 3/514 | 0 / 0 | 12420/2168717 / 3/514 | 12420/2168717 / 3/514 | 744372383/748207365 / 1541/1542 |

(H7 / MATCHED.) On the two widest windows δ\* = 0 at **four** grains,
three of which the unit never tested. The head is robust.

**(c) But it is not grain-free, and the verdict does not say so.**
At Ψ = the R-SIG indicator — a legitimate declared abstraction, and the
obvious one for a regeneration argument *about R-SIG* — the full class
has δ\* = **1** at matched horizon on both widest windows. This is not
an artefact: the one-step matched kernel is the sector-normalised menu,
and the R-SIG-preserving mass is `3/2` out of total menu mass `2` at
*every* R-SIG point, menu-exact or not, because the two idles carry 1
and the deliveries (of the non-superseded token, or of a superseded
remainder, which changes neither `nsup` nor its equality) carry 1/2.
So P¹(x, R-SIG) = 3/4 identically. See MAJOR-4.

**(d) Is "blocked" about the corpus or about this construction?**
About **this construction**, correctly: two actors, depth ≤ 6, N ≤ 5,
the two declared menu grains, the four declared blocks. §14 and the
abstract's "what is deliberately not claimed" paragraph say this
plainly and well. The verdict string, however, states the δ\* = 0
clause without its grain (MAJOR-4) and the block clauses with the
universal "every block" (MAJOR-3).

**(e) The mechanism holds at 8× the coverage the unit measured.** The
unit censuses the monotone index over 30,728 transitions (those out of
depth < 5). I ran it over **every transition of the family**:

| census | unit's scope | full scope (this review) |
|---|---|---|
| transitions | 30,728 | **243,768** |
| holdings-shrinking | 0 | **0** |
| profile-decreasing | 0 | **0** |
| non-superseded-shrinking | 4,340 | **29,980** |

So the abstract's "zero transitions of the family" is **true**, and now
measured at the scope its wording claims. See MINOR-3.

---

## 4. K3 — THE FEED-FORWARD BINDING

**A hash-drift finding first, for the record.** At the start of this
review `v14/code/gmain_exact.py` in the worktree hashed to
`51c3b4cf3f3c`, the sha the protocol names. During the review it
changed twice (`4d3527957ae2`, then `d302c16a0072`) — a Γ-main repair
pass is in flight. `git show HEAD:v14/code/gmain_exact.py` still hashes
to `51c3b4cf3f3c`, and **all K3 findings below are taken at that
committed sha**, per the protocol's instruction. HEAD itself moved
(`d9f39a2` → `95c3b77`) during the review; all Γ-prep artifacts were
re-verified unchanged at the end.

### What Γ-main consumes from this unit, and whether consumed = delivered

| Γ-main row | what it reads | delivered here | verdict |
|---|---|---|---|
| `S-GPP/S-GPC/S-GPO/S-GPR` | the four artifacts' sha256-12 at commit `0f5d57eef77f` | `09482eb080cc`, `9a4f0529b840`, `097c08a0229d`, `dd86ad1a80d7` | **matches** |
| `G-PATH-VALUE-STABILITY` | 3 upstream paths read at both `SHA_TREE` and `SHA_GPREP` | pinned rows T1, T5 | consistent |
| `A-CENSUS-LEVEL` `[1,8,60,452,3448,26760]` | rebuilt in-unit, anchored to a typed literal | `t_per_level[:6]` | **matches** |
| `A-CENSUS-CUM` `[1,9,69,521,3969,30729]` | rebuilt in-unit | `t_cumulative[:6]` | **matches** |
| `A-CARRIER-SIZE` `3969` | rebuilt in-unit | `t_cumulative[4]` | **matches** |
| `A-RSIG` `5161`, `A-RMENU` `1365` | rebuilt in-unit | `rsig_count`, `rmenu_count` | **matches** |
| `A-BLOCKS` `{(1,1):1365,(2,2):3788,(2,3):4,(3,2):4}` | rebuilt in-unit, labelled "Γ-prep's committed B2 holdings-profile blocks" | `rsig_profiles` | **matches at depth ≤ 5** — but see MAJOR-3 |
| `V-LADDER` verbatim anchor into `S-GPP` | the paper sentence *"The holdings profile decreases at\n**zero** transitions of the family: it is a monotone non-decreasing"*, consumer gate `T8-ATOMS` | — | see below |
| `PV-GPREP-DELTA` | `armB/atoms/0/delta_matched_primary`, `want=None` | — | **does not resolve; swallowed** |

Every value Γ-main consumes agrees with what this unit delivers. No
row is read that this unit does not pin **except one**, and it is the
verbatim anchor:

> **Γ-main's load-bearing quotation from this unit is a paper sentence
> whose receipt-backed form is scoped, and the unscoped universal is
> not pinned anywhere in the receipt.** `V-LADDER` binds "zero
> transitions of **the family**"; the receipt pins
> `B3_profile_decreases = 0` over `B3_profile_pairs = 30728`, i.e.
> transitions out of depth < 5 only — 12.6% of the family's 243,768
> transitions. The claim is true (I measured 0 of 243,768), but Γ-main
> is currently anchored to prose that outruns its own receipt key.
> Repair: MINOR-3 below fixes this at the source, after which
> `V-LADDER` binds a sentence the receipt backs.

### What R-GM-9's swallowed probe SHOULD have read

Γ-prep's receipt is a **flat dict of 196 keys**; there is no `armB`
key, no nesting, no list of atom records with named fields. The δ\* = 1
datum the Γ-main pin names as inherited lives at:

| what the probe wanted | the actual key | value | type |
|---|---|---|---|
| `armB/atoms/0/delta_matched_primary` | **`B2_best_delta`** | `"1"` | **string** |
| the same datum row-wise | **`B2_profile_rows/0/5`** | `"1"` | **string** (row 0 = block `(1,1)`, N=1; index 4 = H7 primary, 5 = MATCHED primary, 6 = MATCHED control) |
| the atom's existence | `B2_atom_found` | `true` | bool |
| the atom's block window | `B2_nu_block_size` | `1365` | int |
| the atom list | `B2_atoms/0` | `["(1, 1)", 1, 1365]` | list — **carries no δ\* field at all** |

Note that `B2_atoms` rows are `(profile, N, window)` triples filtered
to δ\*=1, so there is *no* exact analogue of the probe's intended path;
`B2_profile_rows/0/5` is the nearest true one.

> **Advisory to the Γ-main repair now in flight (observed in the
> worktree at `4d3527957ae2`, may already be superseded):** the
> repaired `PV_DECL` declares `('PV-GPREP-DELTA', 'GPREP', GPR,
> 'B2_best_delta', 1)` with the Python **int** `1`, while the receipt
> holds the **string** `"1"`. `anchor()` compares with `==`, so
> `1 == '1'` is `False`, `ANCHOR_FAIL` fires and the run takes
> `finish(1)`. The probe must expect `'1'`. `PV-GPREP-ATOM` (`True`)
> and `PV-GPREP-NUBLOCK` (`1365`) are correctly typed. I verified this
> by resolving all three paths against the receipt at
> `0f5d57eef77f`.

---

## 5. FINDINGS

### MAJOR-1 — the compliance sweep asserts 8 of its 18 rows, and the one substantively violated rule is among them

The output banner reads `[COMPLIANCE SWEEP — computed statuses, not
asserted ones]` and paper §16 reads *"compliance | 18 of 18 engraved
rules satisfied, **each computed**"*. By AST census of `COMPLY`,
**8 of the 18 statuses are the typed literal `True`**:

`RUNBOOK 13 (#10) render from the gated object`,
`RUNBOOK 13 (#20) prose renders from the receipt`,
`RUNBOOK 14 (#20) compliance claims are gate claims`,
**`RUNBOOK 14 (#46) no unanchored runtime inputs`**,
`RUNBOOK 14 (#219) comparators built independently`,
`RUNBOOK 15 declared arena`,
`RUNBOOK 15 (#196) match every coordinate`,
`RUNBOOK 13 (#314) precheck may not name the verdict`.

`C-COMPLIANCE` gates `compliance_all = all(ok ...)`, so it cannot
detect a violation of any of those eight. And the #46 row's evidence
string is **factually false**: *"the only files read are the pinned
artifacts and this file's own source; v14/LOG.md and /STATUS.md are not
opened"* — the process also reads `v10/LOG.md` through
`git show HEAD:`, as the paper's own §3 states ("the committed ledger
object for the T5 verification"). The receipt contradicts the paper it
renders.

Two of the remaining ten are proxies rather than tests of their rule:
`RUNBOOK 4 counts computed, never typed` is discharged by
`t_total == 243769 and rsig_count == 5161`, which tests two censuses,
not the rule (and the rule is in fact violated — MINOR-1).

**Repair.** (i) Replace each typed `True` with a computed predicate, or
demote the row to a `DISCLOSURE` kind that the sweep counts separately
and the paper reports as asserted. (ii) Correct the #46 evidence string
to name the ledger read, and make its status computed —
e.g. `all(p in PINNED_PATHS or p == SELF or p == LEDGER_OBJECT for p in
OPENED)` with `OPENED` accumulated by a wrapper around every read.
(iii) Change §16's "each computed" to the computed split
(`n_computed`/`n_asserted`) and render it from the receipt.

### MAJOR-2 — `t5_ledger_number` is an ungated, unanchored, mutable-ref runtime input that degrades silently to `None`

`os.popen("cd REPO && git show HEAD:v10/LOG.md")` at line 436. Three
defects compose:

1. **Unanchored.** `HEAD` is a moving ref, not a hash pin. HEAD moved
   from `d9f39a2` to `95c3b77` during this review alone. The unit's own
   §3 presents "committed rather than working tree" as the anchor;
   committed-at-a-moving-ref is not a pin. (Γ-main's own engraved #62
   standard, at `51c3b4cf3f3c`, states the rule this violates verbatim:
   *"Worktree bytes and `git show HEAD:` are mutable state and are read
   for NO source."*)
2. **Ungated.** No gate anywhere reads `t5_ledger_number`. Grep
   confirms: the key is written once and consumed only by three
   f-strings.
3. **Silent failure.** With git unavailable, `_stamp` stays `None`.
   I ran exactly this: run 1, in a scratch tree with no git object
   store, produced a receipt differing from the committed one in
   **exactly one key** — `t5_ledger_number: null` — while emitting
   *"carries **(LEDGER #None)**"* and *"TERMINAL at v10 LOG #None"*,
   passing all 44 gates, and **exiting 0**. The pin's explicit order
   ("VERIFY the exact v10 ledger # in-unit and print it") is therefore
   dischargeable by a run that verified nothing.

**Repair.** Pin the ledger by blob sha, not by `HEAD`: read
`git show <declared-commit>:v10/LOG.md`, byte-anchor its sha256-12 like
every other row, and add a gate
`t5_ledger_number == 495 and t5_ledger_number is not None` whose
failure exits 1. Register a falsifier that sets it to `None` and
confirm the gate dies.

### MAJOR-3 — a fifth holdings-profile block exists and is never declared, tested, or disclosed; the universals "each block"/"every block"/"one per holdings profile" are false

`PROFS` is taken from `F['rsig_profiles']`, the **depth ≤ 5**
decomposition, and then applied to `RS`, the **depth ≤ 6** R-SIG set.
I censused R-SIG over the whole family:

| profile | points | by depth |
|---|---|---|
| (1,1) | 5,461 | 0:1 1:4 2:16 3:64 4:256 5:1024 6:4096 |
| (2,2) | 33,260 | 3:20 4:328 5:3440 6:29472 |
| (2,3) | 108 | 5:4 6:104 |
| (3,2) | 108 | 5:4 6:104 |
| **(3,3)** | **424** | **6:424** |
| total | **39,361** | |

The four declared blocks cover **38,937 of 39,361** R-SIG points. The
**(3,3) block, 424 points, is never named**. Consequences:

* §11.6(iii) heading *"THE RETURN INTO EACH PROFILE BLOCK"* — false.
* the §11.6 box *"exact atoms — **one per holdings profile**"* — false;
  (3,3) was never tested for atomicity.
* `B3-HITTING`'s label *"into **each** ATOM (each holdings-profile
  block)"* — false.
* the verdict's *"the hitting infimum into **every** block is 0"* —
  4 of 5.

**This does not reverse the head.** I ran the missing measurements:
the N = 1 hitting probability into (3,3) is exactly 0 at 30,545 of
30,729 histories, **infimum 0**; its re-entry census is 424 of 424; and
its δ\* is not computable at this cap at all (every point sits at depth
6, so no window with `dep + N ≤ 6` exists). The fifth rung *confirms*
the ladder. But the universals must go or the block must be carried.

**Repair.** Build `PROFS` from `RS` (all depths), print the full
profile census with its depth support, mark (3,3) `EXCLUDED-BY-CAP` for
δ\* with the reason ("depth-6-only; no N ≥ 1 window"), carry its
hitting row (`N=1: 30729 tested, 30545 zeros, inf 0`), and gate
`sum(len(PROFBLK[p]) for p in PROFS) == len(RS)` so a future
undeclared block cannot recur.

### MAJOR-4 — the BLOCKED verdict states its δ\* = 0 clause with no grain qualifier, while the FOUND verdict carries one — and δ\* is grain-relative on exactly that clause

`GPREP-MINORIZATION-FOUND-[…; scope = 2 actors, transport depth <= 6,
MATCHED horizon, **primary grain** …]` — correctly qualified.
`GPREP-MINORIZATION-BLOCKED-AT-[… the full R-SIG class has delta\* = 0
on both of its widest windows (N = [1, 2]) …]` — **no grain**. Yet
`B2_full_rows` is computed with `psi_kind_of` only, `B2-GRAIN` is the
unit's own gate establishing that δ\* is grain-relative, and §11.4 says
so in words ("the minorization is grain-relative, and the grain is
declared"). §12's "Scope qualifiers, mandatory and attached" lists the
horizon, the caps and the windows for Arm B — **not the grain**.

That the omission bites is shown in §3.3(c) above: on the same two
widest windows, at Ψ = the R-SIG indicator, the same class has
δ\* = **1** (MATCHED) — provably, since P¹(x, R-SIG) = 3/4 for every
R-SIG point.

**Repair.** (i) Add `at the DECLARED-PRIMARY 13-class grain` to the
BLOCKED verdict's δ\* clause and to §12's scope qualifiers, exactly as
the escape clause in the TERMINALIZED verdict already does. (ii) Adopt
the coarsening lemma (§3.2 above) and state the strengthened form the
measurement actually licenses: *δ\* = 0 on the two widest windows at
the 13-class grain and hence at every refinement of it, including all
six of T5's committed abstractions.* (iii) Add one row disclosing that
coarsenings incomparable to the menu grains are not covered, with the
R-SIG-indicator row as the printed witness.

### MAJOR-5 — the theorem-pass census undercounts: two SUBSTANTIVE gates cannot return False on any input the construction admits

§13 and the receipt state *"of the 44 gates, 40 are substantive — **they
could have returned False on this family**"*. Two cannot:

* **`B1-TREE`.** Unique parenthood is a property of the *representation*
  (a history is its event sequence, so `h = g + (e,)` forces
  `g = h[:-1]`). Its only failure mode is a duplicated menu entry — I
  measured 0 across all 243,769 menus. This is logically identical to
  `A3-KERNEL`, which the unit correctly classifies `THEOREM-PASS`
  precisely because "only a menu/potential mismatch could break it". Two
  gates of the same status, two classifications. The paper itself calls
  it a theorem: *"Unique parenthood is the defining property of a
  history tree"* (§11.2), *"at the history level it is dead by unique
  parenthood — that is a theorem, not a cap"* (§15.2).
* **`A4-PRED`.** The reduction is forced, not measured: `live = {}` ⇒
  `components() = {}` (components are built from live proposals), and
  `|nsup(a)| = 1` ⇒ `merge_pairs(a) = ∅` (the held-created-unsuperseded
  set is contained in `nsup(a)`). §7 states both implications as
  arguments. No input the layer admits can make the two predicates
  disagree; I confirmed 0 disagreements over 30,729 histories by my own
  implementation of both.

The corrected census is **38 substantive / 5 theorem-pass / 1
disclosure**. `C-THEOREMCENSUS` guards `n_theorem >= 3`, so the
reclassification passes it unchanged.

**Repair.** Reclassify `B1-TREE` and `A4-PRED` as `KIND_THM` with the
forcing named at each gate (as `A3-KERNEL` and `A4-MONO` already do),
update §13 and §16, and let the waiver machinery pick them up.

---

### MINOR-1 — `birkhoff_tau` and `birkhoff_diameter_finite` are typed literals feeding an abstract headline

Lines 1980–1981: `F['birkhoff_diameter_finite'] = False`,
`F['birkhoff_tau'] = '1'`. Neither is computed. `B1-TREE` then checks
`f['birkhoff_diameter_finite'] is False` — a typed literal compared to
itself, a tautological conjunct. The abstract's *"the Birkhoff
contraction coefficient is 1 at every level"* and the verdict's *"the
Birkhoff coefficient is 1"* both render from a declaration. The
*inference* is correct and the witness minor **is** measured; only the
bookkeeping is wrong, and it violates `RUNBOOK 4 counts computed, never
typed` — the rule the compliance sweep marks OK.
**Repair.** Derive them: `tau = '1' if (m12 == 0 or m21 == 0) else
str(...)`; `diameter_finite = not (m12 == 0 or m21 == 0)`. Then the
gate's conjunct is a real one and MAJOR-1's proxy row becomes true.

### MINOR-2 — `A1-KINDS`' label says "six declared event kinds" and lists five

`"the committed layer generates exactly the six declared event kinds
(p, r, m, d, n) and no others"` — five names, and the predicate checks a
five-element set. The paper §4 *does* own the discrepancy (the pin's T1
row summarises the layer as six kinds; the measurement is five), which
is exactly right; but the gate label, printed verbatim at
`gprep_foundation_output.txt:331`, is internally contradictory.
**Repair.** *"generates exactly the five kinds the layer defines
(p, r, m, d, n) — the pin's T1 summary column says six; this is the
measurement."* Fix the pin's T1 "supplies" cell in the same pass.

### MINOR-3 — the abstract's "zero transitions of the family" is measured over 12.6% of the family

`B3_profile_decreases = 0` over `B3_profile_pairs = 30728` (transitions
out of depth < 5). The family has **243,768** transitions. The verdict
prints the denominator; the abstract, §11.6's prose and the §11.6 box
do not, and Γ-main's `V-LADDER` anchors precisely the unscoped
sentence (§4 above). The claim is **true** — I measured 0 of 243,768,
and 0 of 243,768 holdings-shrinking transitions with it.
**Repair.** Run the census at full scope (it costs nothing — the state
scan already covers the whole family) and print `0 of 243,768`. The
narrowed 4,340 non-superseded-shrinking figure becomes **29,980** at
full scope; carry both with their scopes named, since §7's
absorbing-complement argument uses the narrowed one.

### MINOR-4 — `A4-PORTS` gates cardinality where the paper claims set identity

The paper: *"The R-SIG points that are not menu-exact are **exactly**
the re-entered ones."* The gate:
`f['rsig_reentries'] == f['rsig_menu_not_exact']` — two counts. I
verified the set identity holds (symmetric difference empty), so the
prose is true and the gate is merely weaker than it.
**Repair.** Carry the two sets and gate
`NOT_MENU_EXACT_SET == REENTERED_SET`, with a falsifier that swaps one
element between them.

### MINOR-5 — an output-file sentence is contradicted by the table printed four lines above it

`gprep_foundation_output.txt:249`: *"the maximum finite return distance
**rises with depth** over the measured rows."* The table at lines
219–226 gives maxima `0, 2, 2, 2, 2, 1, 0` by depth — it rises once,
is flat across depths 1–4, and falls. The paper does not repeat the
sentence (§11.6 says only "the largest return distance actually
attained is 2"), so no paper number is affected.
**Repair.** Delete the clause or replace it with the computed one:
*"the attained maximum is 2 on every informative row."*

### MINOR-6 — "roughly eight times this run's depth-6 build"

§11.1. The projection 1,696,040 is 7.96× **level 6** (213,040) but
6.96× **the depth-6 build** (243,769). Both numbers are in the receipt.
**Repair.** *"roughly eight times this run's level-6 layer"* — or print
the computed ratio.

### MINOR-7 — `#494` and `#492` are typed literals in the emitted prose

Line 454. Both are true (I checked them against the committed ledger:
#494 = "D74 DELIVERED (GREEN-UNREVIEWED)", #492 = "D74 PINNED"), but
they are asserted facts about the ledger printed beside a computed one.
**Repair.** Parse them out of the same ledger read that yields #495, or
drop them.

### MINOR-8 — the registered CLI disease is still present (the #66 correction of record)

`ARGV = set(sys.argv[1:])`; only `--list-gates`, `--list-mutants` and
`--no-write` are consulted. **Unknown flags are silently ignored** and
the run proceeds as a plain delivery — which is exactly how #65's
`--selftest` verification became vacuous. There is no `--selftest` and
no `--mutant NAME` harness, and the docstring's "CLI CONTRACT" section
does not mention rejection.
**Repair** (the #82 contract minimum): parse argv against a whitelist;
exit 2 on an unknown flag; add `--selftest` that corrupts exactly one
byte anchor, asserts exactly one anchor failure, writes **nothing**, and
exits 1; add `--mutant NAME` that applies one registered falsifier and
prints the gates it kills. Gate the whitelist itself
(`unknown_flag_exit_code == 2`) so the repair cannot silently regress.
*(K5's lens owns this item; recorded here because the operator lens is
the one that reproduces runs.)*

---

## 6. Prose ↔ receipt sweep

Every number in `paper-11-transport-foundation.md` was checked against
the receipt and against my rebuild. **All render from the receipt**;
none is unsupported. The three verdict segments appear in §12
character-for-character identical to `receipt['verdict']`.

Numbers I verified as derivations rather than receipt reads, each
marked at its site in the paper as the era requires: the five-vs-six
kind count (§4, marked *"Derived in text"*), and §11.1's branching
projections (both operands in the receipt). The only prose arithmetic
that does not land is MINOR-6's "eight times".

Items where the paper is **more** careful than the receipt, and should
stay that way: §3's "the only files this process opens are the pinned
artifacts, **the committed ledger object for the T5 verification**, and
its own source" — correct, where the receipt's #46 compliance row is
not (MAJOR-1).

## 7. Why ACCEPT-WITH-FIXES and not ACCEPT

Two things stop this being a clean ACCEPT. First, MAJOR-3: a fifth
block of the very object Arm B is about was never declared, and four
universals in the paper, the gate labels and the verdict are false as
written — even though the missing measurements, once run, confirm the
head. Second, MAJOR-1 and MAJOR-2 together: the receipt's self-audit
asserts eight rules it does not test, one of them the rule that the
run's only mutable-ref input violates, and that input can degrade a
paper headline to `None` on a green exit. Those are precisely the
self-report failures this era's standards exist to catch, and they are
in the receipt rather than the science.

Nothing here touches the seven facts, the atoms, the ν, the Birkhoff
death or the blocking mechanism. All eight repairs are mechanical, and
five of them (MAJOR-3's census, MAJOR-4's lemma, MINOR-3's full-scope
census) come with the replacement numbers already computed above.
