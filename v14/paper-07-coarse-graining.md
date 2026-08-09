# CR-C — THE COARSE-GRAINING SEMIGROUP

**Status:** `GREEN-UNREVIEWED` — delivered against the CR-batch pin.
**Pin:** the CR-C section of `v14/note-cr-batch-pins.md` (frozen 2026-08-09, v14 ledger
#30, sha256-12 `1cfee4fc0891`).
**Sources, hash-verified and path-value anchored at run time:** I7 —
`v13/code/ha_successor_receipt.json` (`542b8735daf0`); the HA paper
`v13/paper-ha-successor.md` (`f286ba10d2d9`) and the HA instrument
`v13/code/ha_successor_exact.py` (`d44cb72f8ee9`); and, **for the additivity dual and
the consistency control only**, the R6a receipt
`v14/code/r6a_refinement_receipt.json`, whose status is **DELIVERED-UNDER-PANEL**
(committed v14 #26, adjudicator-verified #27, hostile protocol frozen #28) and is
carried at every citation below. That status is not decorative here: **R6a's receipt
moved from 022c3f488a93 to 94adec72ab11 while this unit was built, and all 12 of the
values this unit reads from it by path are unchanged.** Both hashes are declared in
the instrument, the drift is disclosed at `X-R6A-BYTES-MOVED`, and the load-bearing
check is `G-R6A-VALUES-STABLE-UNDER-DRIFT` (§13.1). Nothing is imported; every object
is rebuilt here.
**Verdict:** **`CRC-MERGE-CHOICE-AT`** — canonical on the two count registers,
choice-bearing at the matter register, with the commutation segment carried. The
full emitted string is §12.
**Deliverables:** this note; `v14/code/crc_coarsegrain_exact.py`,
`crc_coarsegrain_output.txt`, `crc_coarsegrain_receipt.json`.

---

## Scope box

Everything below is at declared finite arenas. The pinned base is I7's own
$X=(\mathbb Z_L)^d$ with $L=3$; because a 2:1 block-merge needs an even axis, this
unit **builds** three arenas of the same class — $A4=(\mathbb Z_4)^2$,
$A6=(\mathbb Z_6)^2$, $A4X=(\mathbb Z_4)^3$ — and records I7's own $L=3$ arena as
non-mergeable rather than skipping it. No continuum limit is taken, no scaling limit
is claimed, no invariant trajectory is measured, and nothing here bears on Einstein
dynamics. The geometry sector is frozen under $H_a[N]$ exactly as I7 declares
(deviation 7 of the HA paper); the merge acts on the record, and the dynamics
comparison is posed on the front and the address register.

---

## 1. The direction the grammar licenses

R6a asked whether the pinned grammar admits a motivated interval **subdivision**, and
answered `R6A-NO-MOTIVATED-SPLIT`: the forced half held exactly, and four freedoms
were measured genuinely free. Its semantic anchor, quoted verbatim from its own pin,
is the equation

> n(x,y) + n(y, x+ℓ) = n(x, x+ℓ) (events in the whole = events in the
> parts) — this is semantics, not a choice

read left to right. This unit reads it **right to left**. That is the whole
difference, and it changes the answer on two of the three registers.

The reason it changes the answer is not rhetorical. Splitting must **invent** a
number: given a coarse count it must choose how to divide it. Merging must only
**read** numbers it already has. The pin puts it in one sentence — *Merging is the
direction the grammar licenses* — and this unit measures how far that goes and
exactly where it stops.

It stops at the matter register, and the stopping point is sharp.

---

## 2. The arenas, declared as data

| coordinate | value |
|---|---|
| pinned base | $X=(\mathbb Z_3)^2$, I7's own arena — **non-mergeable** |
| built arenas | `A4` $=(\mathbb Z_4)^2$ (16 sites), `A6` $=(\mathbb Z_6)^2$ (36 sites), `A4X` $=(\mathbb Z_4)^3$ (64 sites) |
| links | I7's declared set: the $d$ axis links and the $\binom d2$ positive diagonals |
| geometry record | $s$: $n_\ell(x)\in\mathbb Z_{>0}$, division events in the record interval between $x$ and $x+\ell$ |
| front | $n:X\to\mathbb Z$, events already committed **at** site $x$ |
| matter record | $m:X\to\mathbb Q^d$, the address register |
| readout | $q_{ij}e_\ell^ie_\ell^j=n_\ell(x)$, $I_a(g)=q^{-1}(\det q)^w$ at $w=0$ |
| records | I7's 9 declared $d=2$ count vectors as homogeneous records **plus** its two declared inhomogeneous site rules `G-CURVED` and `G-CURVOFF`; 9 of 11 admissible, identically at `A4` and `A6` |
| fronts | `F-ZERO`, `F-SYM` ($n=x_0x_1$), `F-RAMP` ($n=x_0$) |
| lapses | I7's declared family, rebuilt at each arena: the $\lvert X\rvert$ site deltas, the constant profile, the $d$ chart ramps |
| drag rules | I7's 11 declared rules at `A4`; I7's **own** declared $d=3$ subfamily at `A6` (anchored, and disclosed as a narrowing) |
| enlargements | `E-HOM` (I7's count box), `E-PARITY` (parity-class records), `E-AFFINE` (a declared parameter box) |

**The L = 3 arena I7 declares does not merge: 3 is odd, and all 11 of its declared
records are recorded non-mergeable.** The reason is measured, not asserted: the block
partition $\{2i,2i+1\}$ of $\mathbb Z_3$ is not a partition — site 2 would pair with
site 0, which already sits in block 0 — so the block map is undefined. Every one of
the eleven records carries that row in the receipt.

---

## 3. The merge moves

Write $\beta_i\in\{1,2\}$ for the block vector, $\iota(x)_i=\beta_ix_i$ for the
block's base corner, and $\tilde\ell_i=\beta_i\ell_i$ for the lift of a coarse link.

- **`M-DYADIC`** — every axis halved, block $2^d$, $2L\to L$.
- **`M-AXIS-0`, `M-AXIS-1`** — one declared axis halved, block $2$.
- **`C-PROJECT`** — the negative control: read the coarse count off the base-corner
  link, merging no interval.

A move is **admissible** when every coarse lift has a *unique* minimal realisation by
declared links, **blocked** when some lift has two or more, **foreign** when it merges
no interval.

**M-DYADIC's incidence is forced: 3 of 3 coarse lifts have a unique minimal
realisation.** $2e_j$ is two $e_j$ steps and nothing else; $2(e_1{+}e_2)$ is two
diagonal steps and nothing else.

**M-AXIS carries 2 candidate realisations of the diagonal lift, and the block is real:
the two readings disagree at 26 of 1404 cells, on 1 of 9 records.** Under a
single-axis merge the diagonal lift is $(2,1)$, which decomposes as $e_0$-then-diagonal
or diagonal-then-$e_0$. This is the *same named grammar fact* R6a's HYPERPLANE branch
blocked at — `DIAGONAL-INTERVAL-INCIDENCE`, two candidates — reached here from the
opposite direction and anchored against R6a's own receipt row. The block is measured
real rather than assumed: the two readings agree on every homogeneous record and on
the separable inhomogeneous one, and disagree only on `G-CURVOFF`, whose cross term is
site-dependent. The axis merges are therefore reported as BLOCKED at the named fact,
with the disagreement census printed.

The control behaves as a control must: `C-PROJECT` forces 0 additivity constraints and
discards 180 recorded division events over the 27 coarse intervals of `A6` — measured
FOREIGN by the same audit that passes `M-DYADIC`.

---

## 4. The forced part: the additivity dual, on **two** registers

The counting semantics that forces the split's additivity forces the merge's
composition, and it does so **twice**, because I7 declares two count registers:
$n_\ell$ counts events *in an interval*, $n(x)$ counts events *at a site*.

$$n^c_\ell(x)=n^f_\ell(\iota(x))+n^f_\ell(\iota(x)+\ell),\qquad
n^c(x)=\sum_{\delta\in\{0,1\}^d}n^f(\iota(x)+\delta).$$

**Count additivity holds at 591 of 591 checked cells and the front sums at 314 of
314.** Both are class-(i) freedoms with fiber 1: the incidence is forced by the
declared link set, and the composition is forced by the semantics.

The alternative composition is not left unmeasured. The declared alternative
`ALT-INTERIOR` — the sub-interval sum *plus* the interior site's front value — is the
Boolean-connective boundary of this construction, and it carries its death certificate
as a measured delta: **The declared alternative composition differs at 877 cells.** It
is excluded because the two registers are distinct; adding one to the other is a
category error, and it also destroys the split-then-merge identity of §9.

---

## 5. The transformation law

$q^c$ is the pinned readout applied to $n^c$. That is the whole law, and it is
forced. What is *not* a single statement is "$q$ adds componentwise", because the
three links sample three **different** second points: the $q_{jj}$ block reads
$\iota(x)+e_j$ while the cross term reads $\iota(x)+(e_1{+}e_2)$.

$$q^c_{jj}(x)=q^f_{jj}(\iota)+q^f_{jj}(\iota+e_j)\ \ \text{always};\qquad
q^c_{12}(x)=q^f_{12}(\iota)+q^f_{12}(\iota+\ell_{\mathrm{diag}})
\ \Longleftrightarrow\ \mathcal T(x),$$

$$\mathcal T(x):\quad n_{e_0}(\iota+\ell_{\mathrm{diag}})+n_{e_1}(\iota+\ell_{\mathrm{diag}})
\;=\;n_{e_0}(\iota+e_0)+n_{e_1}(\iota+e_1).$$

**The diagonal components of q are additive at 234 of 234 cells; the cross component
at 117 of 117.** The iff is checked cell by cell — 117 of 117 agreements between the
additivity outcome and $\mathcal T$ — and it has teeth in both directions: a declared
negative-control parity record `NC-PARITY` violates $\mathcal T$ and its cross term is
measured **not** to add. Over the parity enlargement the two outcomes are both
realised at scale (§7).

**Merge-covariant:** the interval counts $n_\ell$, the front $n$, and the $q_{jj}$
block. **Not merge-covariant:** the cross term $q_{12}$ (covariant only under
$\mathcal T$), $\det q$, and $I_a(g)=q^{-1}$. The record is what transforms; the
metric is what is read afterwards, and I7's record-IS-metric re-encoding commutes with
the merge only where the sampling points agree.

---

## 6. The merge choice inventory

R6a's classification rule, applied to the merge direction: **(i)** forced by a named
pinned declaration with fiber 1; **(ii)** fixed by a measured stabiliser; **(iii)**
genuinely free, fiber counted exactly.

| freedom | register | fiber | class | forced by / obstruction |
|---|---|---|---|---|
| `MERGE-LOCUS` | — | 1 | (i) | the move-class declaration |
| `MERGE-INCIDENCE` | $s$ | 1 | (i) | `[P-I7-LINKS2]` — every dyadic lift has a unique minimal realisation |
| `INTERVAL-COUNT-COMPOSITION` | $s$ | 1 | (i) | `[T-COUNTS-SEMANTIC]` — the R6a dual |
| `FRONT-COMPOSITION` | $n$ | 1 | (i) | `[T-FRONT]` — the merged site IS the block |
| `THE-MATTER-RULE` | $m$ | **INFINITE** | (iii) | no pinned declaration; **no stabiliser** |
| `THE-LAPSE-RESTRICTION` | dynamics | 2 | (iii) | declared, not derived |
| `THE-FRONT-MERGE-PAIR` | $n\times$dynamics | 2 | (iii) | declared, not derived |

**The inventory closes at FORCED 4, STABILIZER 0, FREE 3.**

The matter register is where the merge stops being canonical, and the mechanism is
measured. Addresses do not add — I7's own declaration calls $m$ *the recorded
tangential address of the matter carrier at $x$*, not a count — so a merge must choose
a rule $m^c(x)=\sum_\delta c_\delta\,m^f(\iota(x)+\delta)$. Two pinned constraints cut
that space and no more:

- **$D$-equivariance.** $D_a[v]$ shifts the register by a constant $v$; a merge that
  commutes with it needs $\sum_\delta c_\delta=1$.
- **Chart equivariance.** The surviving direction relabelling forces
  $c_{(1,0)}=c_{(0,1)}$.

**The matter-merge fiber is an affine Q-space of dimension 2; over the declared
coefficient box 35 of 625 members are D-equivariant and 9 are also
relabelling-equivariant.** No stabiliser can do better, and the reason is structural:
**The merge breaks the chart translations to the block-preserving subgroup: 9 of 36
survive at A6, of index 4.** The survivors are the *even* translations, which permute
blocks and fix every offset — **no pinned symmetry acts within a block at all**. A
class-(ii) classification of the matter rule is therefore not merely unproved, it is
unavailable.

That is the verdict's head: `CRC-MERGE-CHOICE-AT`, at the register $m$, with the
inventory above.

---

## 7. The fixed-point census

A record is **merge-self-similar** when its image is $\lambda$ times itself for one
rational $\lambda$. The declared enlargement `E-AFFINE` makes the question finite:
$n_{e_j}(x)=a_j+b_jx_j$ and $n_{\mathrm{diag}}=n_{e_0}+n_{e_1}+2g$, on which the merge
acts by

$$(a_j,\;b_j,\;g)\ \longmapsto\ (2a_j+b_j,\;4b_j,\;2g).$$

**Over the declared affine box of 1125 parameter points, 775 are admissible and 35 are
merge-self-similar, with rescalings 31 at lambda = 2 and 4 at lambda = 4.** The census
is identical at `A4` and `A6` — measured, not assumed. Two families, and the second
one is the interesting one:

- **$\lambda=2$** — the locus $b_j=0$: the homogeneous records, any cross term.
- **$\lambda=4$** — the locus $b_j=2a_j$, and it is **forced into HA's diagonal
  sector**: a graded axis count rescales by 4 while the cross term rescales by 2, so a
  common $\lambda$ exists only at $g=0$. Measured over the whole box, not argued.

The parity enlargement gives the flow. **E-HOM carries 361 records and E-PARITY
16983563041; the merge sends every parity record to a homogeneous one in a single
step, with 16855671371 of them landing on an admissible image.** Within `E-PARITY` the
fixed points are therefore exactly the 361 homogeneous records: one relevant
direction, the overall scale, and everything else killed in one step.

And the sector question, at scale: **Of the 1679616 diagonal parity records, the merge
preserves diagonality at 189216.** On the declared record family HA's closure sector is
merge-stable at 10 of 10 diagonal records; on the enlargement it is not, and the exact
criterion separating the two cases is $\mathcal T$ again. Both counts are printed;
neither is generalised.

---

## 8. The semigroup

**The two axis merges commute at 702 of 702 cells, while their composite equals the
dyadic merge at 598 of 702.** The failure is not noise and not a tie-breaking
artefact — it is the same measurement under both declared tie rules — and it is an
**iff**, verified record by record: the composite equals the dyadic merge exactly on
the records whose readout is diagonal, and on no other. The arithmetic is the same
arithmetic that makes HA's link-local rule close on the diagonal sector: there the
diagonal count is the sum of the axis counts, so stepping through the block corner and
stepping along the block diagonal read the same total.

So the coarse-graining semigroup does **not** factor through the axis merges off the
diagonal sector. It is generated by `M-DYADIC`, and it terminates: `A4` admits one
dyadic step to $L=2$ and `A6` one to $L=3$, and $L=1$ is REFUSED with the measured
reason — at a single site every declared link maps the site to itself, so "the interval
between $x$ and $x+\ell$" is a self-loop and the count register loses its referent.

---

## 9. Merge-dynamics compatibility

Coarsen-then-advance against advance-then-coarsen, over both drag architectures, all
declared rules, the full declared lapse family at each arena, three declared fronts,
the $2\times2$ grid of (front merge, lapse restriction) rules and three declared
matter rules.

**The front sector.** $C_n(n+N)=C_n(n)+C_n(N)$, so the front commutes precisely when
the lapse restriction is the *same* rule as the front merge. **The front sector
commutes at 1044 of 1044 matched cells and at 234 of 1044 mixed ones.** The mixed
survivors are exactly the block-corner deltas, where the two coarsenings coincide.
This reproduces, from the merge side, the 2-of-4 structure R6a measured on its lift
grid.

**The register sector.** The defect has an exact closed form,

$$D^i(x)=\sum_\delta c_\delta\,N^f(y_\delta)\sum_j\Lambda^f(y_\delta)^{ij}
\bigl(n(y_\delta+e_j)-n(y_\delta)\bigr)
-N^c(x)\sum_j\Lambda^c(x)^{ij}\bigl(n^c(x+e_j)-n^c(x)\bigr),
\qquad y_\delta=\iota(x)+\delta,$$

and it is two-sided: **The register defect is nonzero at 61780 of 118260 censused
cells and identically zero at 56480.** The matter record cancels between the two
orders, so the defect is a pure drag comparison and is independent of $m$. It is
characterised rather than merely reported — support by block parity class, per-rule,
per-record and per-grid profiles are all in the receipt, cell-complete.

The sharpest measurement in the section is that the defect cannot be merged away.
Because $D$ is linear in the coefficients $c_\delta$, "is there a matter-merge rule
that makes the register commute?" is an exact linear system, and it is solved exactly.
**The joint linear system for a defect-killing matter rule is unsolvable at 540 of 540
cells.** The positive control is carried in the same gate: a constructed solution is
planted and the same solver recovers it, so the verdict is a measurement and not a
solver artefact.

> **The merge's one genuinely free register is free in a way the dynamics cannot fix.**
> The matter rule is not forced by the grammar, not fixed by a symmetry, and not
> selectable by demanding that the merge commute with $H_a[N]$ — the demand has no
> solution at any censused cell.

**Two routes and an independent comparator.** **The closed form and the literal
composition agree at 67716 of 67716 compared cells, and the independent weight route at
2880 of 2880.** The two defect routes share `drag()`; that shared part is policed by
the second, independently written weight route (diagonal rules assembled directly,
inserted rules by the adjugate/determinant formula), by the positive control above, and
by the mutants `order-swap` and `coarsen-skew`, which move one route only.

---

## 10. The consistency control

R6a's dyadic split run backwards must reproduce the merge on its overlap.

**Split-then-merge is the identity at 2971 of 2971 checks, and this unit's independent
rebuild reproduces R6a's split fibers at 9 of 9 records.** The check is
fiber-exhaustive, not sampled: the split fiber factorises over coarse sites and the
merge is site-local, so a per-site exhaustive sweep *is* a sweep of the whole fiber —
including `G-ANISO2`'s fiber of $1{,}257{,}565{,}061{,}957{,}837{,}936{,}381$ — and
the factorisation itself is gated.

**The count lattice reproduces at 361 admissible vectors and 261 splittable ones.**
The unique-admissible-split witness is $(2,2,2)$ — R6a's numbers, rebuilt here from
the readout and the Sylvester criterion alone.

On the other two registers the control says something the split alone could not.
Under the forced block-sum front rule, split-then-merge is the identity on the front
**exactly when** R6a's class-(iii) `NEW-FRONT-VALUES` vanish — measured in both
directions. The merge direction therefore cuts an infinite R6a fiber to a single
point. That is a consequence of a demand this unit *states* — that the round trip be
the identity — not a derivation from the pinned grammar alone, and it is carried as a
disclosure rather than as a result. On the matter register the identity is
unconditional under the corner rule and conditional under every other member of the
fiber.

---

## 11. The dimension extension, and where the asymmetry is sharpest

**At d = 3 the dyadic blocks cover 64 of 64 sites and 6 of 6 lifts are unique, while
R6a measured 27 sites unreached by the split at the same arena.** R6a's own reading of
that number is that at $d=3$ the declared link set has no body diagonal, so one parity
class of refined sites lies on no coarse interval: the split is site-incomplete. The
merge has no such gap — blocks partition, and every coarse lift is $2\ell$ for a
declared $\ell$.

This is the pin's thesis at its most measurable. The split leaves 27 sites with no
coarse referent and 54 of 108 links free; the merge leaves nothing free on the count
registers at all.

---

## 12. The verdict, as emitted

```
CRC-MERGE-CHOICE-AT<ARENAS=I7-BASE-L3-NON-MERGEABLE-11-RECORDS|BUILT-A4-A6-A4X|MOVES=DYADIC:ADMISSIBLE-INCIDENCE-3-OF-3-UNIQUE|AXIS:BLOCKED-AT-DIAGONAL-INTERVAL-INCIDENCE-2-CANDIDATES|PROJECT:FOREIGN-ADDITIVITY-0-EVENTS-DISCARDED-180|BLOCK-REAL=DISAGREEING-26-OF-1404-ON-1-OF-9-RECORDS|CANONICAL=S-ADDITIVITY-591-OF-591|N-FRONT-SUM-FORCED-314-OF-314|ALT-INTERIOR-DELTA-877|CHOICE=REGISTER-M-FIBER-AFFINE-DIM-2-BOX-9-OF-625-NAMED-3|INVENTORY=FORCED:4|STABILIZER:0|FREE:3|OBSTRUCTION=THE-MATTER-RULE+THE-LAPSE-RESTRICTION+THE-FRONT-MERGE-PAIR|TRANSFORM=Q-DIAGONAL-BLOCK-ADDITIVE-234-OF-234|CROSS-IFF-TRANSVERSALITY-117-OF-117|COVARIANT=COUNTS-n_l+FRONT-n+Q-DIAGONAL-BLOCK|FIXED-POINTS=AFFINE-35-OF-775-ADMISSIBLE-OF-1125-BOX|LAMBDA-2-31|LAMBDA-4-4-DIAGONAL-FORCED-YES|HOM-361-ALL-LAMBDA-2|PARITY-16983563041-FIXED-361|SEMIGROUP=AXIS-COMMUTE-702-OF-702|COMPOSITE-EQUALS-DYADIC-598-OF-702-IFF-DIAGONAL-YES|CHAIN-A4-1-A6-1-FLOOR-L1-REFUSED|COMMUTATION=FRONT-GRID-2-OF-4-UNIVERSAL-MIXED-234-OF-1044|REGISTER-DEFECT-NONZERO-61780-OF-118260-ZERO-56480|IRREDUCIBLE-540-OF-540-UNSOLVABLE|SUPPORT-(0, 0):31845-OF-269892|(0, 1):23851-OF-168804|(1, 0):24082-OF-168804|(1, 1):19644-OF-118260|CONSISTENCY=SPLIT-MERGE-IDENTITY-2971-OF-2971|R6A-FIBERS-REPRODUCED-9-OF-9|SPLITTABLE-6-UNSPLITTABLE-3|FRONT-IDENTITY-IFF-NEW-FRONTS-ZERO-MEASURED|D3=MERGE-SITE-COMPLETE-64-OF-64-INCIDENCE-6-OF-6-UNIQUE-VS-R6A-SPLIT-UNREACHED-27>
```

The head is computed in-gate from the inventory's class counts: no genuinely free
freedom would emit `CRC-MERGE-CANONICAL-ON`, and both heads are demonstrated reachable
by synthetic probes. The complete string is compared for equality against a rebuild
produced from the receipt object by a comparator sharing no code and no input with the
builder; five injection classes and a head-pinning mutant die there.

---

## 13. The receipt

`v14/code/crc_coarsegrain_exact.py` emits `crc_coarsegrain_output.txt` and
`crc_coarsegrain_receipt.json`. Interpreter `/opt/homebrew/bin/python3.13`. Exact
arithmetic throughout: `int` and `fractions.Fraction` only; the AST float guard is
validated by synthetic injections it must flag, and the receipt is scanned for float
values.

### 13.1 A live source, and how the citation survived it

R6a is under panel and its receipt is a live file. It was repaired mid-build — its
gate count went 48 to 71, its mutant count 34 to 78, and a MECHANISM segment was added
to its verdict string — so the file-bytes anchor this unit's pin names stopped
matching, and every run aborted at it, loudly, which is what an anchor is for.

The resolution is the one LOG #4 engraved for pins, applied at run time: a unit
reading a tree that is still moving must anchor the **values**, not only the bytes,
and must say so. Both hashes are declared in the instrument; the twelve `(path,
value)` pairs this unit reads are gated unchanged across the drift; a hash outside the
declared pair still kills the run, and a drifted value dies at
`G-R6A-VALUES-STABLE-UNDER-DRIFT`. R6a's head, its 27 coarse intervals, its 972
additivity checks with 0 violations, its 361/261 count lattice, its
`DIAGONAL-INTERVAL-INCIDENCE` block with 2 candidates, its 54 free links, its 27
unreached $d=3$ sites, its splittable and unsplittable record lists and its whole
split-fiber table are all bit-for-bit what they were at pin time.

### 13.2 Totals

| item | value |
|---|---|
| anchors (exit-1-only) | 44 — 6 file-bytes, 27 path-value, 11 verbatim-text |
| gates | 55, all must-pass |
| disclosures | 7 (`X-UNDER-PANEL`, `X-R6A-BYTES-MOVED`, `X-NOTRANSPORT`, `X-FRONT-IFF-CONDITIONAL`, `X-SECTOR-SCOPE`, `X-ROUTES-SHARE-DRAG`, `X-EXTENSION-RULE-SET`) |
| mutants | 44, 0 survivors |
| runs | two full runs, byte-identical output and receipt |

---

## 14. Deviations and declared choices

1. **The arenas are BUILT, not inherited.** I7 declares $L=3$; a 2:1 merge needs an
   even axis. `A4`, `A6` and `A4X` are constructed from I7's declaration schema —
   same site group family, same link set, same readout, same lapse family rule, same
   record rules — and the base arena is recorded non-mergeable rather than dropped.
2. **The `A6` commutation census runs I7's own declared $d=3$ rule subfamily**, the
   same narrowing I7 used for its own extension, anchored at `P-I7-RULES-EXT`. The
   `A4` census carries all eleven rules. Every count is printed with its scope.
3. **`A-insert` and `A-notransport` supply the same weight at a single $H_a[N]$
   step**, so the one-step commutation census cannot separate them; the frozen-front
   behaviour is a property of the composition, which this unit does not form. The
   duplicate row is disclosed, not claimed as an independent measurement.
4. **The R6a receipt is cited as DELIVERED-UNDER-PANEL** at every use, and every
   number read from it is also independently rebuilt here. The panel moved the
   receipt's bytes during this build; the anchors failed loudly rather than silently
   agreeing, and the resolution is §13.1 — two declared hashes, twelve gated
   `(path, value)` pairs, and a disclosure.
5. **The front-forcing statement is conditional** on demanding that split-then-merge be
   the identity (§10, disclosure `X-FRONT-IFF-CONDITIONAL`).
6. **The matter-rule fiber is counted two ways** — as an affine $\mathbb Q$-space of
   measured dimension, and exactly over a declared finite coefficient box. Neither is
   presented as the other.
7. **The fixed-point census is at a declared parameter box**, and its
   $L$-independence across `A4` and `A6` is measured rather than assumed.

---

## 15. Non-claims

- No continuum limit, no scaling limit, no refinement family, no invariant trajectory.
- No claim about general $d$, general $L$, general records, general lapses, general
  weights. The verdict is at the declared arenas.
- No claim that the merge is canonical on the full record: it is canonical on $s$ and
  $n$ and choice-bearing on $m$, and the verdict says so.
- No claim that the $\lambda=4$ fixed-point family is a physical fixed point of
  anything. It is a fixed point of a declared move on a declared parameter box, and
  its containment in HA's diagonal sector is an arithmetic consequence measured over
  that box.
- No claim that HA's diagonal sector is merge-stable in general — it is measured stable
  on the declared record family and measurably unstable on the declared enlargement.
- No claim that the register defect is irremovable by any means: what is measured is
  that no **linear** matter-merge rule removes it, over the declared lapse family, at
  every censused cell.
- No Einstein-dynamics claim of any kind; no geometry-update law is constructed.
- Nothing here is citable before an external hostile round confers TERMINAL.

---

## 16. Opens

1. **The $p$-adic direction.** Only the 2:1 block was constructed. Whether a $k$:1
   merge for odd $k$ (which I7's $L=3$ arena would admit) carries the same forced
   structure on $s$ and $n$, and whether its incidence is unique, is untouched.
2. **A non-linear matter rule.** §9 measures that no linear $c_\delta$ removes the
   register defect. Whether some non-linear, record-dependent matter-merge rule does
   is open, and it is the natural successor question.
3. **The cross-chart merge.** The merge is defined with respect to a declared block
   origin. Whether two block origins related by an odd translation give the same
   coarse record is a question this unit poses but does not answer; the surviving
   subgroup measurement (§6) is what makes it well-posed.
4. **The sector criterion at general $d$.** $\mathcal T$ is a $d=2$ statement. Its
   $d\ge3$ analogue, and whether the $\lambda$-spectrum stays $\{2,4\}$, are open.
5. **R6b's question, from this side.** If a refinement family does not exist inside
   the pinned grammar (R6a) but a coarsening semigroup does, the continuum question may
   be posable only as a limit *of* coarse-grainings rather than a limit of refinements.
   This unit supplies the semigroup; it does not take the limit.
