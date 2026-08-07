# HOSTILE REVIEW R1 — OPERATOR / ALGEBRAIC LENS

## O4 DISCRIMINATOR (v13), against the frozen protocol `v13/note-o4-hostile-protocol.md`

**Reviewer lens:** operator/algebraic. **Primary weight:** K1 (the obstruction),
K2 (like-for-like). K3–K5 at lower depth.

**Date:** 2026-08-07. **Method:** independent recomputation. The composite
model was rebuilt from its mathematical specification alone — the totally real
quartic field `Q(cos pi/8)` implemented from the minimal polynomial
`8c^4 - 8c^2 + 1 = 0` over `fractions.Fraction`, `U_prep`, `U_A(theta)`,
`U_B(theta)`, the two frames, the record layer (`h_corr` / `h_avail` / the
token value law), the declared permutation scopes and W5's divisibility
residual. No repo module was imported into any measurement. The delivered
script was executed exactly once, without `--falsification-selftest`, purely as
a determinism/integrity cross-check; its write path is guarded behind that
flag, and the frozen artifacts were re-hashed afterwards and are untouched.

**Recomputation count: 593.**

---

## 0. Object integrity

All four SHA-256 prefixes verified before reading:

| artifact | pinned | measured |
|---|---|---|
| `v13/paper-o4-discriminator.md` | `e45c090f226f` | `e45c090f226f` ✓ |
| `v13/code/o4_discriminator_exact.py` | `240a6e05dce7` | `240a6e05dce7` ✓ |
| `v13/code/o4_discriminator_output.txt` | `fd1cb9273951` | `fd1cb9273951` ✓ |
| `v13/code/o4_discriminator_receipt.json` | `b791ec7e2d30` | `b791ec7e2d30` ✓ |

A plain run of the frozen script reproduces the frozen `output.txt`
**byte-for-byte** except for the `O4-MUTANTS` gate block and the `MUTANT TABLE`
section, both of which are emitted only under `--falsification-selftest`. 27
anchors pass, 21 gates pass, 0 must-pass failures. Determinism as claimed.

---

## 1. K1 — THE OBSTRUCTION

### 1.1 The §6 table reproduces exactly

Rebuilt from the specification, all six rows, both frames, intersections and
unions:

| setting | F1 occupied (mine) | F2 occupied (mine) | ∩ | ∪ | delivered |
|---|---|---|---|---|---|
| SP-A | {12,24} | {1,2,10,11,19,20,28,29} | 0 | 10 | identical |
| SP-B | {12,24} | {1,2,10,11,19,20,28,29} | 0 | 10 | identical |
| SP-C | {3,6,12,15,21,24,30,33} | {1,2,10,11,19,20,28,29} | 0 | 16 | identical |
| SP-D | {3,6,12,15,21,24,30,33} | {1,2,10,11,19,20,28,29} | 0 | 16 | identical |
| SP-E | {12,24} | {11,19} | 0 | 4 | identical |
| SP-F | {3,6,12,15,21,24,30,33} | {1,2,10,11,19,20,28,29} | 0 | 16 | identical |

Every leg is exactly orthogonal in my rebuild (`U_prep` + 8 local operators, 9
certificates); the five half-angle Pythagorean identities close exactly.

### 1.2 The decisive attack: is disjointness frame-relative? — **NO. The paper wins.**

I swept, at all three matching levels, order-free, with and without the `j0`
filter:

- **S1** the declared base scope (72) and the declared extension (96);
- **S2** a **wide structural scope of 1728** elements — `(qa,qb,pa,pb) ↦
  (π(qa,qb), σ_a(pa), σ_b(pb))` for `π ∈ S4`, `σ_a,σ_b ∈ S3`, with and without
  the pointer-slot exchange — verified to **contain** both declared scopes;
- **S3** **every bijection of the 36 configurations**, by exact backtracking
  constraint search over the simultaneous-conjugation problem (36 searches, no
  scope restriction whatsoever).

Result, uniform across S1/S2/S3:

| setting | frame isos F2→F1 (j0-fixing), all 36! | of those, sharing occupancy | achieving occ. equality |
|---|---|---|---|
| SP-A/B | 1 | **0** | 0 |
| SP-C/D | 1 (exact,sign) / 2 (born) | **0** | 0 |
| SP-E | 9 | **0** | 0 |
| SP-F | 1 | **0** | 0 |

Dropping the `j0` filter entirely widens the iso set to 9/18/81; some of those
share occupied configurations (4/8/18) but **none** achieves set equality, and
every one of them moves the initial configuration, so none is a co-reference
map. **Verdict on K1's fork: DISCRIMINATED, not BLOCKED-AT-FRAME-CHOICE.** The
obstruction is robust against every frame pair, relabelling and matching level
the base admits, and against every bijection whatsoever. This is the paper's
strongest result and it survives the hardest test I could construct.

One qualification the paper should carry. Disjointness of the *named*
propositions is **not** relabelling-invariant: in the wide scope, 672 maps
produce overlap and 96 produce set **equality** at SP-C/D/F (8 at SP-E) — e.g.
the pure wing exchange carries F2's SP-E support {11,19} exactly onto F1's
{12,24}. None of these is leg-compatible, which is precisely why the
obstruction holds. So §6's sentence *"no proposition of the form 'the
configuration between the division events is i' is true in both frames"* is a
statement relative to the base's declared common labelling; the
relabelling-invariant statement is the frame-isomorphism one. The paper relies
on the invariant statement in §5 but headlines the non-invariant one.

### 1.3 FINDING F2 (MAJOR) — the verdict turns on a free slice choice

§11.5 defines the intermediate time as *"after the declared division event 0
and before the final time"*. **t = 1 satisfies that definition.** The paper
reads t = 2, anchoring to W6's control 4. Measured at t = 1:

| | SP-A | SP-B | SP-C | SP-D | SP-E | SP-F |
|---|---|---|---|---|---|---|
| occ F1 = occ F2 at t=1 | {9,18} | {9,18} | {9,18} | {9,18} | {9,18} | {9,18} |
| F-CFG datum identical in both frames | yes | yes | yes | yes | yes | yes |
| C2 / C2X / C3 F-CFG transports at t=1 | **1** | **1** | **1** | **1** | **1** | **1** |
| the same rules at t=2 (delivered) | 0 | 0 | 0 | 0 | 0 | 0 |

At t = 1 the unrecorded-configuration class is **FORCED at every setting under
every corridor-bound candidate** — an `O4-RULE-EXISTS`-shaped result, from the
same charts, the same rules, the same scopes.

The obvious defence — that t = 1 is itself a division event and so not
"between" — **fails on the paper's own instrument**. W5's residual computed at
t = 1 is `(0,0,16,16,0,16)` in both frames, *identical to t = 2*. So at SP-C,
SP-D and SP-F, t = 1 is exactly as much a non-division-event intermediate time
as t = 2 — and those are precisely the settings where the paper's own LTP
forcing lemma fires. The suite's `support-lax` mutant covers the final time
t = 3; **nothing in the 23 mutants covers t = 1.**

*Repair:* declare the read time as a coordinate, run t ∈ {1,2}, publish the
per-slice verdict table, and rescope §6/§9 to the slice at which each result was
measured.

### 1.4 FINDING F3 (MAJOR) — the obstruction is carried by the record coordinates

Splitting the t = 2 datum into the pointer coordinates (which the declared
record tokens' values read: `VALS[k] = POINTER3[k % 3]`) and the qubit
coordinates:

| setting | record (pointer) marginal ∩ | system (qubit) marginal ∩ | system marginals identical? |
|---|---|---|---|
| SP-A | **0** — F1 {(+,r),(−,r)} vs F2 {(r,+),(r,−)} | 2 | no |
| SP-B | **0** — same | 2 | no |
| SP-C | **0** — same | 4 | no |
| SP-D | **0** — same | 4 | no |
| SP-E | **0** — same | 2 | **yes** |
| SP-F | **0** — same | 4 | **yes** |

The pointer marginal is disjoint at all six settings and is **the same pair of
sets at all six**. The qubit marginal is **never** disjoint. Running the
paper's own rules on the system-marginal datum gives transports
`[0,0,0,0,1,1]` under C2 and C3 — the identical profile the paper attributes to
C4's realized restriction.

Moreover the disjointness is a **theorem, not a six-setting measurement**:
`U_X(θ)` shifts the measured wing's pointer by 1 or 2 under a 3-cycle, never by
0, so at t = 2 frame F1 always has `pA ≠ r, pB = r` and frame F2 always has
`pA = r, pB ≠ r`. I verified nonempty overlap is impossible at **all 16** angle
pairs in {0°,45°,90°,135°}², not just the six committed. The six rows of §6
carry one bit, not six.

The consequence for the charter: what §6 exhibits is that at F1's t = 2 wing
A's record has been written and B's has not, and conversely in F2. That is a
statement about *which record exists*, not about unrecorded actuality.

*Repair:* state the structural theorem in one line, publish the record/system
marginal split, and withdraw the implication that the six settings independently
measure the obstruction.

### 1.5 FINDING F6 (MODERATE) — §6's prose is contradicted by §5's own table

§6: *"That is the object on which every F-CFG transport count in §5 is measured
to die."* C4's F-CFG count is **1 at SP-E and SP-F** (delivered table; my
recomputation agrees). The same sentence is embedded verbatim in the
`O4-OBSTRUCTION-NAMED` gate's claim string in the receipt.

What actually kills C2/C2X/C3 is measured to be different: **full-leg matching
rigidifies the co-reference map to the identity** (exactly one j0-fixing
leg-compatible bijection at SP-A/B/E/F, two at SP-C/D, over every scope I
swept), and the identity cannot carry disjoint supports. Under C4's realized
legs the constraint loosens and a transport appears at the two symmetric
settings — which is why disjointness does not kill it there.

*Repair:* replace the sentence with the mechanism as measured (rigidity of the
leg constraint), per the RUNBOOK's #38→#40 rule.

---

## 2. K2 — LIKE-FOR-LIKE

### 2.1 The §5 transport table reproduces in full

All **90 cells** (5 candidates × 3 classes × 6 settings) reproduce from my
independent rebuild, including the F-REC positive control `1,1,1,1,1,1` under
C2/C2X/C3, F-CFG `0` throughout, F-CTRL `1` throughout, C4's
`0,0,0,0,1,1` for both F-REC and F-CFG, and C1's zeros. No numerical
discrepancy anywhere in this table.

### 2.2 FINDING F1 (FATAL to the headline verdict) — the classes are read at different times

The three fact-classes are not read at a common time index:

- **F-REC** — `datum_rec` reads at `upto = max(write_leg)+1 = 3` (the final time);
- **F-CFG** — `datum_cfg` reads at `upto = 2`;
- **F-CTRL** — same, `upto = 2`.

Holding the charts, the rules, the scopes and the levels fixed and varying only
the read time, for **both** classes (C2 shown; C3 identical):

| read time | F-REC | F-CFG |
|---|---|---|
| t = 1 | vacuous — no token written yet | **1,1,1,1,1,1** |
| t = 2 | **0,0,0,0,0,0** | **0,0,0,0,0,0** |
| t = 3 | **1,1,1,1,1,1** | **1,1,1,1,1,1** |

**At every time at which both classes have facts, they have the same profile.**
At t = 2 — F-CFG's read time — the *record* class is ABSENT at all six settings.
At t = 3 — F-REC's read time — the *configuration* class is FORCED at all six.

This is not a new measurement. It is **the paper's own anchor A13**, which is in
its receipt and passes exit-1: *"|Phi_A| and |Phi_B| at the intermediate slice,
per setting … committed ((1,1,1,1,1,1),(0,0,0,0,0,0))"*. I reproduced A13
independently (level A = 1 at all six, level B = 0 at all six, frame-isos = 0 at
all six). The disconfirming half of the discrimination is carried in the unit's
own anchor list and is never brought to bear on the comparison.

The CERT gate carries the same asymmetry into a hard pass/fail. `certify()`
computes the pair guard `dis` at each class's own read time:

| setting | `dis` at t=3 (F-REC's) | `dis` at t=2 (F-CFG's, F-CTRL's) |
|---|---|---|
| SP-A | **0** | 10 |
| SP-B | **0** | 10 |
| SP-C | **0** | 16 |
| SP-D | **0** | 16 |
| SP-E | **0** | 4 |
| SP-F | **0** | 16 |

`route_ext_pair` returns `DISAGREEMENT` iff `dis ≠ 0`. So F-REC's certificate
passes because it is evaluated where the two frames agree exactly, and
F-CFG's/F-CTRL's fail because they are evaluated where they do not. The
certificate never compares record data with configuration data at a common time.

**Consequence.** `O4-DISCRIMINATED-RECORD-ACTUALISM` as stated — *"the record
control is green … while the unrecorded class is obstructed at every coordinate
at which the record class is green"* — is not earned. There is no coordinate at
which the record class is green and the configuration class is measured at the
same time. The class variable is fully confounded with the read time, and at
matched read times the discrimination is null.

*Repair (required, not cosmetic):* run the full (class × read-time) grid as
declared coordinates and re-derive the verdict from the matched cells. Either
the outcome changes name, or the verdict is rescoped to an explicitly
time-indexed claim — *"record facts at the time all tokens are written descend;
configuration facts at the intermediate slice at which the two frames have
written different records do not"* — with the plain statement that no
class-versus-class discrimination at matched time is measured.

### 2.3 FINDING F7 (MODERATE) — the like-for-like gate is syntactic

`O4-LIKE-FOR-LIKE` measures (a) that each class's gate row carries every gate
key and (b) that the three transport functions share an argcount and their
first eight `co_varnames`. The `likeforlike-lax` mutant kills it by adding a
parameter. The gate is therefore live but cannot see any of the three real
per-class branches:

1. the read time (t = 3 vs t = 2), §2.2 above;
2. `certify()`'s three-way branch on `fid` — record values vs probability pairs
   vs `(str(i), str(i))`;
3. `class_gate_row` lines 963–964: `sa = NC if fid != "F-REC" else
   len(CHARTS[ka].live("available"))` — the five-valued discriminator is fed
   scope 36 for two classes and scope 2 for the third.

Only (3) is benign (it affects the VACUOUS branch alone). Branch (1) is the
fatal one and branch (2) implements it. This is precisely the RUNBOOK failure
mode #36/#40 — a gate that measures the intent rather than the property.

*Repair:* gate the semantic property. Declare the read time as class data and
assert its equality across classes, or gate that `certify()` takes the same
`upto` for all three.

Also note the FORCED gate is not type-matched: F-REC's Φ is a set of **token**
maps (at most 2), F-CFG's and F-CTRL's are sets of **configuration bijections**
(up to 96). Two distinct bijections inducing one token map count once for
F-REC and twice for F-CFG. It does not move any verdict here (F-CFG is 0), but
`|Φ| = 1` is not the same predicate across the three rows.

### 2.4 FINDING F8 (MODERATE) — the negative control has one tooth, exercised four times

F-CTRL fails TRI, GLUE, CERT and NAMEBLIND under C2/C3. All four trace to a
single fact — the datum is the configuration's name and the declared triple and
the relabelling change names — and CERT does not even do that:

`certify()` gives F-CTRL the reader `lambda i: (str(i), str(i))`. Both
coordinates are *identical by construction*, so ROUTE-EXT's value-preserving
bijection test is trivially satisfied; the only thing that can fail is the `dis`
pair guard, which is computed from the **t = 2 distributions** and is therefore
the *same number* as F-CFG's (10, 10, 16, 16, 4, 16). F-CTRL's certificate
failure carries no information about names whatsoever — it is the object's own
failure mode duplicated onto the control.

`transports_ctrl` admits `p` iff `p = identity`, and the identity is always
leg-compatible order-free, so F-CTRL passes EXIST/FORCED/INV automatically.
The control therefore distinguishes nothing on the first three gates and fails
the rest analytically. It is not weightless, but §5's presentation of four
independent failing gates overstates it.

### 2.5 C2X's BLOCKED-AT-COVAR — **verified**

Measured under the checkpoint-phase switchings: 60 tests per (candidate,class)
= 6 settings × (2 relabellings + 8 switchings). C2X shows **24 switching
failures of 48** on F-REC and 24 on F-CTRL, and 0 relabelling failures; C2 and
C3 show 0/0 everywhere. The level census agrees independently: `exact` not
switching-invariant (24 failures), `sign` and `born` invariant (0). The
BLOCKED-AT-COVAR verdict is carried by **non-vacuous** rows (F-REC base counts
are 1 at every setting), not by the vacuous F-CFG row. D5's all-classes reading
does real work here. This item passes.

### 2.6 FINDING F9 (MINOR) — vacuous passes rendered as passes

`O4-VACUITY-DISCLOSURE` records that F-CFG's covariance row is vacuous at
**every** coordinate for C1/C2/C2X/C3 and at four of six for C4. §5's table
prints `PASS` in those cells with no marker. D5 states the policy; the table
does not carry it.

---

## 3. K3 — THE LTP GATE

**The residual reproduces exactly.** My independent computation of
`D = Γ(3←0) − Γ(3←2)Γ(2←0)` on `p(0) = δ_{j0}` gives
`‖r‖₀ = (0,0,16,16,0,16)` in **both** frames — anchor A25 ✓. The per-column
census A26 = {16} ✓. The value censuses A27 reproduce exactly: SP-C 4 distinct
values, **0** of 16 rational; SP-F 6 distinct values, **8** of 16 rational,
rationality decided by the field's own test (components 2–4 vanishing), no
tolerance anywhere. The exhibited intermediate actuality is my §1.1 table. The
LTP-BARE finding at SP-F and LTP-BARE-UNWITNESSED at SP-E are correctly derived
from the residual and from `shared = 0`.

### FINDING F5 (MODERATE) — LTP-LAWFUL is unreachable, not measured-negative

§7 states: *"`LTP-LAWFUL` is reachable by the gate — it fires whenever a shared
record law conditions on the datum — and is measured never to obtain on this
base. That is a measured negative, not a stipulation."*

The branch fires iff `shared_record_at_intermediate(sp) > 0`, which counts token
pairs with the same partition. At t = 2, F1 has always written `R_A` (partition
`PARTA`) and F2 has always written `R_B` (partition `PARTB`), and
`same_partition(PARTA, PARTB) = False`. I measured `shared = 0` at all six
settings, and it is **structurally 0** — the two frames' second legs are on
different wings by construction, at every setting, under every switching and
every relabelling (the function does not even take an arena argument). No
mutant reaches the branch: `ltp-lax` empties `bare`, which yields
`LTP-BARE-UNWITNESSED`, not `LTP-LAWFUL`.

So the positive branch of the LTP gate cannot be emitted anywhere in the
declared arena, and the pin forbids building a fixture that would. This is
exactly the Q-OPT lesson the protocol names.

*Repair:* either exhibit a reachability witness (a declared variant in which
both frames have written the same partition by the intermediate time) or
downgrade the sentence to what is true — the branch is structurally unreachable
on this base and the negative is analytic, not measured.

---

## 4. K4 — THE ARENA TEST AND D3

**The numbers reproduce.** |arena| = 6 × 2 × 2 × 8 = **192** ✓. Under the
declared acting group, QA1 moves under setting/frame/relabelling with 4 distinct
values and orbit **2** at every one of the twelve charts; QA2 moves under
setting only, 2 distinct values, orbit **1** at every chart ✓. Neither moves
under the switchings ✓.

### FINDING F4 (MAJOR) — the discrimination is a representative artifact

QA1 is a **name-indexed** object (a 36-bit vector over configuration labels)
read at **t = 2**. QA2 is a **value-indexed** object (a set of record value
tuples) read at **t = 3**. Under a pure relabelling a name-indexed object must
move and a value-indexed one must not — by type, before any physics. Matching
the representatives (acting group = the admitted 2):

| quantity | moves under | distinct | orbit |
|---|---|---|---|
| QA1 — t=2, name-indexed (paper's object) | setting, frame, **relabelling** | 4 | **2** |
| QA2 — t=3, value-indexed (paper's control) | setting | 2 | **1** |
| **QA2′ — t=3, name-indexed** (matched to the object) | **relabelling** | 2 | **2** |
| **QA1′ — t=2, value-indexed** (matched to the control) | setting, frame | 3 | **1** |
| QA2″ — t=2, value-indexed (control at the object's time) | nothing | 1 | 1 |

Under the declared 8, QA2′'s orbit is **8** and QA1′'s is still **1**.

So §8's *"the record class's truth-values are invariant under the frame
coordinate and under the admitted relabellings … the unrecorded-configuration
class's truth-values move under both"* and §10's added clause are **false in the
relabelling coordinate** once the two classes are represented as the same kind
of object: the record class moves with orbit 2 (or 8), and the configuration
class does not move at all. The code already computes the name-indexed record
object (`datum_rec`'s `"read"` field) and `_truth_rec` uses `c.law` instead.

The frame coordinate survives type-matching (QA1′ still moves under frame), but
it is the same t=2/t=3 confound as F1; and QA2″'s frame-invariance at t = 2 is
degenerate — the two frames' t = 2 tokens are *different* tokens (R_A vs R_B)
whose marginals coincide at (1/2, 1/2), which A13 already says do not co-refer.

*Repair:* recompute the census with matched representatives in both directions
and report the 2 × 2; restrict `O4-ARENA-RELATIVE` to what survives.

### FINDING F10 (MINOR) — D3's shrinkage does hollow the orbit numbers

With |G| = 2 the only available orbit sizes are 1 and 2, so *"orbits of measured
size 2"* carries one bit: the wing exchange moves it. Under the declared 8,
QA1's orbits are {2, 4} — not constant — so the "orbit size 2 at every one of
the twelve charts" claim is a statement about the 2-element group only. D3
discloses the choice; the headline does not carry the dependence.

---

## 5. K5 — INSTRUMENT AND D1

### 5.1 D1 — **the 288 is right, and the diagnosis is constructively confirmed**

This was the protocol's hardest item and the paper is fully vindicated.

My independent build gives the matrix residual weight **288** at SP-C, SP-D and
SP-F in both frames — **18 differing columns, each differing in exactly 16
entries**. W5's committed 576 does not reproduce on this base.

I then tested the diagnosis constructively by sweeping orthogonal completions of
`U_prep` off the `j0` column (51 exactly-orthogonal completions: all signed
permutations of an orthonormal basis of the singlet's complement, plus the three
45° mixes):

| completion | matrix nnz | differing columns | per column | ‖r‖₀ on the j0 column |
|---|---|---|---|---|
| the committed one (and 47 others) | **288** | 18 | 16 | **16** |
| `mix45(0,2)` and one other | 432 | 27 | 16 | **16** |
| **`mix45(0,1)`** | **576** | **36** | 16 | **16** |

**W5's 576 is exactly reachable**, by exactly the mechanism the paper names — a
different orthogonal completion off the `j0` column. The `j0`-column weight is
**16 for every completion tested**, so A25 and A26 are completion-independent as
claimed, and "every column that differs at all differs in exactly 16 entries"
holds across the whole family. D1 is a right 288 and a genuine finding about
W5, decided conclusively.

### 5.2 The instrument

- **§14 fresh-eval:** `O4-ST-FRESH` records `value_cache_hits = 0`,
  `value_cache_misses = 1320`. `O4-ST-TEETH`: 600 instances tested, 480 with a
  nontrivial action. Cache-hit gating satisfied as the addendum requires.
- **Mutants:** 23, each exiting 1, each naming a kill. `never falsified []` at
  denominator 17; D6's accounting of the 18th (the vocabulary gate, killed by
  `verdict-lax`) is legitimate and correctly disclosed rather than hidden by
  reordering.
- **Anchors:** 27, all passing. I independently reproduced A13, A25, A26, A27
  and the §6 support data behind A16.
- **Coverage gap:** no mutant perturbs the **read time downward**. `support-lax`
  moves F-CFG's datum to t = 3 and dies at `O4-OBSTRUCTION-NAMED`; nothing tests
  t = 1, which is where the verdict flips (F2 above). The suite's own
  wrong-time mutant is therefore one-sided.
- **Exactness/determinism:** verified — no float in any path I exercised, and
  the reproduction run is byte-identical outside the mutant section.

### 5.3 FINDING F11 (MINOR) — §6's exhibit is a reused value

Anchor A16 (*"the two frames' time-2 occupied supports never coincide, per
setting"*) is already committed in `v12/note-w6-record-coreference.md` and
passes exit-1. §6's framing (*"The instrument's central negative is not a bare
zero. The obstructing object is exhibited as data"*) reads as a new
construction. The anchoring is honest; the prose should credit the base.

---

## 6. Summary of findings

| # | severity | finding |
|---|---|---|
| **F1** | **FATAL** | The three classes are read at different times (F-REC t=3, F-CFG/F-CTRL t=2). At matched read times the profiles are identical (t=2: both 0 at all six; t=3: both 1 at all six). The paper's own anchor A13 already records the record class's intermediate-slice zero. `O4-DISCRIMINATED-RECORD-ACTUALISM` is confounded. |
| **F2** | MAJOR | §11.5's definition of "the intermediate time" admits t=1 as well as t=2; at t=1 F-CFG is FORCED at all six settings under every corridor-bound rule, and W5's residual at t=1 is identical to t=2, so t=1 is not excludable as a division event at SP-C/D/F. No mutant covers it. |
| **F3** | MAJOR | The obstruction is carried entirely by the pointer (record) coordinates — disjoint at all six settings and identical across them — while the qubit (system) marginal is never disjoint and transports FORCED at SP-E/SP-F. Disjointness is a setting-blind theorem (verified at all 16 angle pairs), not six measurements. |
| **F4** | MAJOR | The arena discrimination is a representative artifact: QA1 name-indexed at t=2 vs QA2 value-indexed at t=3. Matched, the record class moves under relabelling (orbit 2, or 8) and the configuration class does not (orbit 1). |
| **F5** | MODERATE | `LTP-LAWFUL` is structurally unreachable (`shared` = 0 by construction at every coordinate); no mutant reaches it. §7's "measured negative, not a stipulation" is not established. |
| **F6** | MODERATE | §6's "every F-CFG transport count in §5 is measured to die" is contradicted by C4's 1 at SP-E/SP-F, in the paper's own table and in the `O4-OBSTRUCTION-NAMED` claim string. |
| **F7** | MODERATE | `O4-LIKE-FOR-LIKE` is a signature check; it cannot see the read-time branch, `certify()`'s class branch, or the discriminator-scope branch. FORCED is also not type-matched across classes. |
| **F8** | MODERATE | The negative control has one tooth exercised four times; its CERT failure is the object's own `dis` guard, carrying no information about names. |
| **F9** | MINOR | Vacuous COVAR passes rendered identically to substantive ones in §5. |
| **F10** | MINOR | With \|G\|=2 the orbit numbers carry one bit; under the declared 8 QA1's orbits are {2,4}, not constant. |
| **F11** | MINOR | §6's exhibit is W6's committed A16, presented as a new construction. |

**Verified against attack (no defect found):** the §6 occupied-set table (all
six rows); the entire §5 transport table (90 cells); **K1's central claim — the
obstruction is not frame-relative, under every scope up to and including all
36! bijections**; A13, A25, A26, A27; the LTP residual and its per-setting
verdicts; **D1, decided conclusively in the paper's favour, with W5's 576
constructed**; C2X's BLOCKED-AT-COVAR; the NOSLICE gate's bite on C1; the
§14 fresh-eval discipline; the mutant census and D6's accounting; exactness and
byte-level determinism. **Zero computed numbers were found to be wrong.**

---

## 7. Grade

The computational layer of this unit is clean. Every number I recomputed
reproduced — 593 recomputations, no numerical discrepancy anywhere. K1's own
kill-shot fails against the paper: I could not make the obstruction
frame-relative under any scope, including an exhaustive search over all
bijections of the carrier, and K5's hardest item (D1) resolves in the paper's
favour with W5's 576 constructed explicitly. Those are real results and they
should survive whatever happens to the verdict.

But the unit's headline is an inference, not a number, and the inference does
not hold. The discrimination between record facts and configuration facts is
fully confounded with the time at which each class is read; at matched read
times there is no discrimination at all, and the disconfirming measurement
(A13) is already in the paper's own anchor list, passing exit-1. The
like-for-like gate is syntactic and cannot see the branch that produces the
result. The second half of the unit verdict, `O4-ARENA-RELATIVE`, rests in its
relabelling coordinate on comparing a name-indexed object with a value-indexed
one; matched, that coordinate reverses. And the one intermediate slice the
paper does not test — t = 1, admitted by its own §11.5 — flips the object's
result to FORCED at every setting.

Both halves of `O4-DISCRIMINATED-RECORD-ACTUALISM + O4-ARENA-RELATIVE` require
re-derivation from matched coordinates, not correction in prose. The repair
path is concrete and the instrument mostly survives it: declare the read time
and the representative type as coordinates, run the (class × time) and
(class × representative) grids, and re-derive. I expect that re-derivation to
land on a different pre-registered outcome — plausibly
`O4-BLOCKED-AT-<the read-time coordinate>` — and that would be a real result
too.

# GRADE: REJECT
