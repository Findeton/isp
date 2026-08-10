# Γ-ITERATION (paper-16) — HOSTILE REVIEW, THE OPERATOR LENS

**Reviewer:** operator lens (from-scratch rebuild, importing nothing).
**Protocol:** `v14/note-giter-hostile-protocol.md` (`9f54f1083f21`,
commit 128cb57), K1–K4 with K2 decisive and K4 shared with the effectus
lens.
**Object, hashes verified at commit 9e481db before any work:** paper
`fd2f25d40002`, code `fab2cdc1893e`, output `58ddd86a52f2`, receipt
`8d28b5f2f807`, pin `aa161f8f8e9d`.  Parents verified at their terminal
commits: Γ-main 4747b47 (`05f5dc7c7273` / `a47d622c7608` /
`d4fe2c64c082`), Γ-prep 2a859a1 (`0f92ab8a1af9` / `a28d8673a2cc`),
D74 9d61cf8 (`0180e21c7127` / `bb852161aced`, `.out` `b5a9d50f9573`).
All 13 declared sources re-verified against their pinned sha at 9e481db:
13 of 13 match.  Repo untouched apart from this one file; the concurrent
workers' files (`u4b_*`, `r5_*`, `paper-17`, `paper-18`) are disclaimed
and were never read from the working tree.

---

## GRADE: **AWF** — ACCEPT WITH FIXES

**Zero false numbers.**  Every delivered numerical result inside my
lens reproduces *exactly* under an independent rebuild — the carrier,
all six ruling properties, the square census, both holonomies, Γ, the
flow identity, Chapman–Kolmogorov, the readout, both legs and all three
readouts on them, the deviation identity, all eight [B3] cells with
their certificates, the whole atom/block battery, the anchor
measurements, the supply row, and (as a cross-check outside my share)
the eq.-22 census down to the four minima.  ~123 independent
recomputations, **0 disagreements**.  The plain run byte-reproduces at
my own hands, off-tree and with git absent.

The fixes are not arithmetic.  They are two places where a **gate's
statement, and a verdict segment, claim more than the predicate under
them decides**, and both have cheap exact repairs.

---

## WHAT I REBUILT DIFFERENTLY

Nothing was imported from `giter_exact.py`.  The only shared object is
the pinned **law** — `v10/code/d42b1_transport_exact.py`, exec'd from
its own bytes at `576275d55ecf` — because re-implementing the transport
grammar would be a different law, not an independent check of this one.
Everything above the law is mine:

| layer | the delivery | my rebuild |
|---|---|---|
| canonical keys | `sk()` — nested tuples of `repr` | `ck()` — a recursive canonical **string** |
| family construction | DFS over an explicit stack | BFS over a `deque` |
| potentials | descending-depth sweep | memoised recursion on `(h, r)` |
| partition refinement | dict-of-histories, signature `(class, sorted succ)` | Moore refinement over **integer node ids** with a precomputed successor array, plus an explicit *stability* check and a *monotone-splitting* check the delivery does not run |
| holonomy | union–find with edge potentials | BFS **spanning forest**, node potential φ, cycle value φ(u)·x/φ(v) |
| group rank | integer row reduction on prime valuations | exact **rational** Gaussian elimination on the same lattice |
| square enumeration | index pairs `i<j` over `CACHE[h]` | `itertools.combinations`, admissibility re-derived per square |
| feasibility LP | dense tableau phase-1, Bland | **revised** phase-1 with an explicit basis inverse and sparse pricing — and then every verdict re-proved from its certificate |
| leg scan | as delivered | own frontier, own weighting, own positional reduction |

Two independent structural checks of the carrier that the delivery does
not carry: the fixed point is verified **stable** (its own successor
signature induces no further split), and every refinement round is
verified to **refine** the previous one — which together prove the
result is the coarsest stable refinement of the menu partition, rather
than leaving that to the recipe's provenance.

---

## K1 — THE CARRIER: **CONFIRMED, 6 of 6, and the contrast at 2 of 6**

CONG-185 re-derived from the pinned layer by my own refinement:
**185 classes after 5 rounds**, per-round counts `162, 179, 184, 185,
185`, spanning-more-than-one-depth counts `17, 5, 1, 0, 0`, dims
`[1, 5, 17, 49, 113]` — all exact.  MENU dims `[1, 5, 13, 45, 113]`.
Fixed point stable: **True**.  Refines MENU: **True**.  Every round
refines its predecessor: **True**.

| # | property | @CONG-185 (mine) | @MENU-113 (mine) |
|---|---|---|---|
| 1 | descent by horizon, multi-valued classes | `0,0,0,0,0` over `185,72,23,6,1` classes tested | `0,0,4,0,0` over `113,45,13,5,1` — **4 of 13 at r = 2** |
| 2 | labelled edges / multi-weight / multi-target | 572 / 0 / **0** | 368 / 0 / **4** |
| 3 | defective squares closed | **44** of 88, symmetric difference vs MENU **0** | 44 of 88 |
| 4 | q-holonomy | primes `[2,3]`, rank 2, obstruction 44, loops `{1/2:26, 2/3:2, 3/2:6, 2:10}` | primes `[2,3]`, rank 2 |
| 5 | k-holonomy | primes `[2,3]`, rank 2, non-unit loops 44 | primes `[2,3,5,13]`, **rank 3**, non-unit loops 52 (`64/65:6, 65/64:2` added) |
| 6 | Chapman–Kolmogorov | **0 of 10** fail | 4 of 10, at `34, 112, 12, 12` cells |

Square census `{AB-only: 28, BA-only: 12, both-blocked: 142, closed:
1546}`, spectrum `{1/2:70, 2/3:2, 1:1458, 3/2:6, 2:10}`, 88 defective;
CONG closes 1362 of 1546, MENU 1402, REC 473 and 0 of the 88.

**No-mismatch-with-D74.**  I read D74's own `.out` at `9d61cf8`
(`b5a9d50f9573`) and every row it states for AB4 is reproduced by my
rebuild: `185 classes after 5 refinement rounds`; `menu closes 44 /
congruence closes 44`; carrier self-loop holonomy `{1/2: 26, 2: 10,
2/3: 2, 3/2: 6}`; off-loop graph `16 nodes, 134 independent cycles, 44
with holonomy ≠ 1, values {1/2: 22, 2: 22}`; menu-mass spectrum
`{2: 3757, 5/2: 212}`; the `(A,B) d ≤ 5` row `265 / 462 / 6 rounds`.
Zero mismatches.  Note that property 3 as delivered — the **set**
identity, symmetric difference 0 — is *stronger* than D74's own gate,
which compares counts (44 = 44); the strengthening is real and it holds.

**Size-matched scramble control, rebuilt:** 185 classes with the
identical class-size multiset loses descent at horizon 1 on **47 of
185** classes and carries **47** multi-weight and **251** multi-target
edges.  The control fires.

---

## K2 — THE TARGETS (decisive): **CONFIRMED numerically; two readings to fix**

**The step-normaliser.**  k₁ = q/M at **0 of 30728** kernel entries;
k₂ = q/M fails at **1340 of 3968**.  Both exact.

*The decisive ruling the protocol asks for — carrier-native or
inherited?  **Neither: it is LAW-NATIVE.***  I measured
`G(h,1) == M(h)` at all **3969** carrier histories: true, and it is
true by the potential recursion's terminal condition
`G(·,0) ≡ 1`, so `G(h,1) = Σ_e q(e|h)·1 = M(h)` for *every* history of
*every* arm under *any* partition.  Nothing in the identity touches
CONG-185; it is not inherited from Γ-main either — the unit re-derives
it in unit, which is what the pin demanded and what it did.  What is
genuinely carrier-dependent is only the side clause, that **M is
class-constant** — and that holds at *both* quotients (0 of 185, 0 of
113 multi-valued).  See MINOR-1.

I also ran the comparison at like scope, which the delivery does not:
k₁ restricted to the k₂ window is **0 of 3968** against k₂'s 1340 of
3968.  The claim survives the fair comparison.

**The law values, both legs, independently scanned.**

| readout | leg 1 (mine) | leg 2 (mine) | matches delivered |
|---|---|---|---|
| step-normalised q/M = k₁ | `(15/38, 5/19, 13/38)` | `(15/38, 5/19, 13/38)` | yes |
| raw price product | `(3/8, 1/4, 3/8)` | `(3/8, 1/4, 3/8)` | yes |
| counting measure | `(3/7, 1/7, 3/7)` | `(4/9, 1/9, 4/9)` | yes |

Leg 1: 16 renewal-1 bases, **152672** raw continuations unpruned,
**3584** legs, patterns `{(n,p,p,r):512, (d,p,p,r):1024, (p,n,p,r):512,
(p,p,n,r):512, (p,p,d,r):1024}`.  Leg 2: **256** bases, **796672**
expansions, **73728** legs.  Leg-independent: yes.  Left–right
asymmetric `15/38 ≠ 13/38`: yes.  Shadow leg-dependent: yes.

**The prune gate, re-run at ten times the delivered coverage.**  The
delivery gates the leg-2 prune on 3 of 256 bases.  I ran the unpruned
scan on **32 spread bases** (every 8th of the sorted 256): **645248**
continuations, **9216** legs, and the pruned and unpruned leg sets are
**identical, leg for leg and weight for weight, at both weights**.  The
delivered subsample numbers are corroborated exactly by rate:
645248/32 = **20164** per base = 60492/3, and 9216/32 = **288** per base
= 864/3.

**The census-shadow token scan: 0 hits, and the #82 disease is provably
absent — with room to spare.**  I re-ran the scan over the 2744-character
target region with the 9 declared tokens (0 hits) *and* with 22 further
tokens of my own — `MENU`, `REC`, `TARGET`, `SHADOW`, the literals
`15/38`, `5/19`, `13/38`, `3/7`, `4/9`, and `W[`, `G[`, `kern(`,
`PRICE`, `MU[`, `MASS`, `IDX_`, `GAM`, `DIMS`, `READ`, `CLOSES`,
`EDGES`, `CARRIER`.  **0 hits on all 31.**  The only object the region
shares with the rest of the run is `CACHE`, the layer's own enumeration.
The measurement that reproduces the shadow consults nothing the family
constructs.  This is the strongest form of the #82 lesson and it holds.

---

## K3 — HOLONOMY: **AGREES, and it is the honest head — with one dependence to disclose**

| measured | mine | delivered |
|---|---|---|
| deviation identity `r_k = r_q·G(h e_A e_B, r−2)/G(h e_B e_A, r−2)` | **0 violations of 1546** | 1546 of 1546 |
| correction-factor spectrum | `{1: 1538, 64/65: 6, 65/64: 2}` | same |
| non-unit factors, base depths | 8, all at depth **0** | same |
| non-unit factors on carrier-closing squares | **0** @CONG, **8** @MENU | same |
| `r_k = r_q` on squares that close | **1362 of 1362** @CONG (0 deviations); 1394 of 1402 @MENU (8) | same |
| the 40 squares CONG declines that MENU closes | 40, of which **8** non-unit and **0** defective | same |
| REC control | obstruction 0, non-unit self-loops 0, 473 closing, both readings | same |

**Is AGREES honest given the pre-registered expectation?**  Yes — and
better than honest, because the pin's "operator's theorem" is a real
theorem and I verified its hypothesis independently: if a square closes
in the carrier then `h e_A e_B` and `h e_B e_A` lie in the *same* class,
and ruling property 1 (descent at horizon `r−2`, which the delivery
tests over exactly the histories of depth `d+2` these squares reach)
forces the two potentials equal, hence factor 1, hence `r_k = r_q`.  So
the head is not a lucky confirmation of a pre-registration; it is a
proved consequence, machine-confirmed.  **That is also the disclosure
owed** — see MINOR-3: conjunct (iii) of `G-HOLONOMY-HEAD` is *entailed*
by `G-CONG-DESCENT` and conjunct (ii), so the four conjuncts are not
four independent pieces of evidence.

**The gate's two-way demonstration works.**  `MUT-DEVIATION-PLANTED`
turns the vanishing conjunct false by planting a non-unit factor on a
CONG-closing square; `MUT-HOLONOMY-HEAD` turns it false by evaluating
the same predicate at MENU-113, where 8 deviations sit.  A deviation
would have looked exactly like the MENU reading: 8 squares carrying
`64/65` or `65/64`, k-primes enlarging to `[2,3,5,13]` at rank 3.  I
reproduced that enlargement independently, so the head can fail and the
instrument can see it fail.

---

## K4 — THE OPERATOR SHARE

### The [B3] LP: **every verdict independently re-proved**

I solved all 8 cells with my own revised simplex **and** verified every
certificate in exact arithmetic — a primal point checked against
`x ≥ 0, Ax = b`, or a Farkas vector checked against `yᵀA ≤ 0, yᵀb > 0`.
The verdicts therefore do not rest on either solver.

| carrier | triple | row problems | infeasible | certified | coupled | certified |
|---|---|---|---|---|---|---|
| CONG-185 | (1,2,3) | 49 | 0 | 49 | FEASIBLE | yes |
| CONG-185 | (1,2,4) | 113 | 0 | 113 | FEASIBLE | yes |
| CONG-185 | (1,3,4) | 113 | 0 | 113 | FEASIBLE | yes |
| CONG-185 | (2,3,4) | 113 | 0 | 113 | FEASIBLE | yes |
| MENU-113 | (1,2,3) | 45 | 0 | 45 | **INFEASIBLE** | yes |
| MENU-113 | (1,2,4) | 113 | 0 | 113 | **FEASIBLE** | yes |
| MENU-113 | (1,3,4) | 113 | 0 | 113 | **INFEASIBLE** | yes |
| MENU-113 | (2,3,4) | 113 | 0 | 113 | **INFEASIBLE** | yes |

**772 row problems, 0 infeasible, 772 certified**; orphan columns 0 and
empty rows 0 in every cell.  The support reduction is exact as stated
and I re-derived it: `allow[i] = {j : supp P1[j] ⊆ supp P2[i]}` is
forced because every term of the sum is non-negative, and the equations
dropped outside `supp P2[i]` are satisfied identically by the allowed
columns.

**The correction to Γ-main's 4-of-4 stands and is located.**
Convention-free the refutation holds at **3 of 4** triples, not 4.
**The one interpolant cell is `(d, md, dd) = (1, 2, 4)`** — feasible
with a verified primal point in 413 variables and 258 equations.  The
paper never names it (§8.1 "feasible at the fourth", §14 "one of the
four triples"), although the receipt does
(`b3.coupled["MENU-113|(1, 2, 4)"].feasible = true`).  See MINOR-6.

**The exhibited witness at CONG-185 IS a stochastic interpolant.**  I
rebuilt the process's own two-cut conditional `Γ(dd←md)` and verified,
at all four triples: `Wit · Γ(md←d) == Γ(dd←d)` exactly, **0** negative
entries, every column summing to **1**.  At MENU-113 the same object
fails to reproduce the target at **4 of 4** — so the witness discriminates
and the swap-mutant is a real falsifier.

### The atom, the block, and the (1,1) split: **exact, row for row**

R-SIG at `d ≤ 5`: **5161** points, **1365** menu-exact, blocks
`{(1,1): 1365, (2,2): 3788, (2,3): 4, (3,2): 4}`; the (1,1) block **is**
R-MENU.  Over the **30728** transitions out of depth `< 5`, entries from
outside: `(1,1): 0`, `(2,2): 1700`, `(2,3): 4`, `(3,2): 4`.

Block ∩ `d ≤ 4`: **341** points at depths 0–4; **one** MENU class,
block-pure; **five** CONG classes of sizes **256, 64, 16, 4, 1**, all
block-pure, exactly one per depth stratum.

| δ\* row | @CONG-185 (mine) | @MENU-113 (mine) |
|---|---|---|
| `(1,1) ∩ d ≤ 3`, N = 1, matched | **0** | **1** |
| `(1,1) ∩ d ≤ 3`, N = 1, H4 | **0** | **1373/1380** |
| `(1,1) ∩ d ≤ 2`, N = 2, matched | **0** | **1** |
| `(1,1) ∩ d ≤ 2`, N = 2, H4 | **0** | **5629529/5674560** |

Every depth stratum of the block has δ\* = 1 at N = 1; **0 of the 72**
testable carrier classes fails δ\* = 1.  The atom dies and the language
is vacuous on the classes, exactly as delivered.

### The anchor measurements

Depth purity: **0 of 185** CONG classes occur at more than one cut, root
class at depth `[0]` alone; **45 of 113** MENU classes recur, root class
at `[0,1,2,3,4]`.  Prefix-class returns: **0** @CONG against **1900**
@MENU.  Labels shared between a triple's cuts: `[0,0,0,0]` @CONG against
`[13,13,45,45]` @MENU.  Supply row `d ≤ 5`: **265** menu classes,
**462** congruence classes, **6** rounds.  All exact.

### The mechanism's own gate — **I built it, and the news is mixed**

Cross-check outside my share, run because the mechanism leans on it:
eq. 22 reproduces exactly — @MENU-113 identity and cyclic **speak** with
negatives **36, 104, 108, 164**, minima **−1/97, −5/97, −1/18, −1/128**,
column sums 1; uniform and marginal singular with duplicate columns
`(0,1)`; @CONG-185 **all 16 cells silent**.

The mechanism claim itself is **MAJOR-1** below.

---

## FINDINGS

### MAJOR-1 — `G-CARRIER-RELATIVE`: the statement is strictly stronger than the predicate, and the stated *reason* is refutable

The gate's statement says the relativity is "**MECHANISED** — the whole
non-Markov signature at MENU-113 is carried by that quotient's
multi-TARGET labelled edges, and refining to the coarsest congruence
removes them and the signature together."  Its predicate `_carrier_rel`
is only:

```
CKFAIL[MENU] > 0  and  CKFAIL[CONG] == 0
and EDGES[MENU].multitarget > 0  and  EDGES[CONG].multitarget == 0
```

That is a **four-way co-occurrence**.  Nothing in it links the edges to
the failures, and neither falsifier
(`MUT-CARRIER-RELATIVE-FLAT`, `MUT-MULTITARGET-BLIND`) tests the link
either — both attack the co-occurrence.  The claim then travels
unqualified into the abstract ("the whole signature is carried by the 4
multi-target labelled edges") and into the verdict string
(`MECHANISM=THE-SIGNATURE-IS-CARRIED-BY-THE-MULTI-TARGET-EDGES-…`).

**So I built the gate.**  Two new measurements:

1. **Localisation.**  The CK-failing cells at MENU-113 are carried by
   **5** distinct source classes, not 4.  The 4 multi-target sources are
   a strict subset; a fifth class carries failing cells at cuts 1 and 2
   and is the source of no multi-target edge.
2. **The minimal repair.**  Split **only** the 4 offending source
   classes, and only by the target of their offending label, changing
   nothing else: **113 → 121 classes**, leaving **36** multi-target
   edges standing (so the result is *not* a congruence and *not* a
   probabilistic bisimulation) — and Chapman–Kolmogorov holds at
   **0 of 10** failing triples.  The signature dies.

So the causal claim is **TRUE**, and the delivery is entitled to it —
but it never measured it.  And the *reason* the paper gives for it is
refuted as an explanation: §7 argues "a quotient with a single-valued
labelled target is a probabilistic bisimulation and its class process is
Markov by construction; a quotient without one need not be, and is not."
Single-valuedness is **sufficient, not necessary**, and the gap is
large: the 121-class minimal repair (36 bad edges) is Markov, and so is
the round-1 partition (**162** classes, **132** multi-target edges,
CK 0 of 10).  "Refining to the coarsest congruence removes them and the
signature together" is true but not explanatory — removing *those four*
is what removes the signature; removing all of them is incidental.

**Exact repair.**  Replace the predicate with the measurement, and
narrow the localisation clause:

```python
MIN = {}                                   # the minimal repair
for h in CARRIER:
    c = MENU[h]
    if c in _mt_src and len(h) < CAP:
        MIN[h] = (c, tuple(sorted((evsk(e), MENU[h + (e,)])
                                  for e, q in CACHE[h]
                                  if (c, evsk(e)) in _mt_bad)))
    else:
        MIN[h] = c
_, _, GAM_MIN = gamma_family(MIN, W)
_mech = (len(CKFAIL['MENU-113']) > 0
         and len([r for r in ck_rows(GAM_MIN) if not r['interpolates']]) == 0)
```

and gate on `_carrier_rel and _mech`, with the detail printing the
121/36/0-of-10 row and the 5-vs-4 localisation.  Add a falsifier that
splits **four other** MENU classes of the same sizes and shows CK still
fails, so the repair is shown to be the offending edges' and not any
refinement's.  Cost: ~15 lines, ~60 s of runtime.  In the paper, replace
"the whole signature is carried by" with the measured statement, and
delete or qualify "a quotient without one … is not" — it is true of
MENU-113 and false as a general reason.

### MAJOR-2 — the `TARGETS` segment is **carrier-free**, and the head does not say so

The unit's own token scan proves it, and my widened 31-token scan
confirms it: the region that computes the leg ensembles and all three
readouts touches **no** object of the constructed family and **neither
quotient**.  The legs live at depths **3 … 10**, outside the carrier cap
of 4.  `(15/38, 5/19, 13/38)` is therefore a value of the transport law
on renewal-cut ensembles — a genuine reproduction of Γ-main's number at
a proved readout — and it is **not a fact about CONG-185**.

Under the candidate-readings rule this matters, because the head reads
`GITER-LAW-CONFIRMED-<CARRIER=CONG-185-… -- LAW=… -- TARGETS=HIT-AT-THE-
LAW-VALUES-…>`.  A reader takes the third segment as "the law *on the
ruled carrier* hit its targets."  It did not; nothing in that segment
was measured on the ruled carrier.  The disclosure exists but lives four
segments away, inside `SCOPE=…|LEGS=RENEWAL-CUT-ENSEMBLES-AT-DEPTHS-
3..10-OUTSIDE-THE-CARRIER-CAP`.

**Exact repair.**  One token in the segment that carries the claim:

```
TARGETS=HIT-AT-THE-LAW-VALUES-AT-CARRIER-FREE-SCOPE-(15/38, 5/19, 13/38)-AT-BOTH-LEGS-…
```

and one clause in §5 and the abstract: "the targets are values of the
transport law at renewal-cut scope, measured outside the carrier cap and
independent of which quotient is used — which the token scan measures
rather than asserts."  Nothing else moves; the fact is unchanged and the
instrument that proves it is already in the delivery.

### MINOR-1 — "re-proved on **this carrier**" attributes a law-level identity to the carrier

`G(h,1) = M(h)` holds by the terminal condition of the potential
recursion, at every history, on every arm, under any partition — I
verified it at all 3969 carrier histories and it uses nothing about
CONG-185.  The paper's §5 heading ("The readout is re-proved on *this*
carrier, not assumed"), the abstract ("re-proved on *this* carrier"), and
the verdict token `STEP-NORMALISER-RE-PROVED-ON-THIS-CARRIER` all imply
carrier-specificity there is none of.  The pin's demand — re-derived in
unit rather than assumed — is fully met; only the attribution is loose.

**Repair.**  "The readout's normalisation is re-derived in unit rather
than imported: `q/M` is exactly `k₁` because `G(h,1) = M(h)` by the
terminal condition — a law-level identity, checked here at 0 of 30728
entries.  What the carrier supplies is only that `M` is class-constant,
which is descent at horizon 1 and which both quotients satisfy."
Verdict token → `STEP-NORMALISER-RE-DERIVED-IN-UNIT-…`.

### MINOR-2 — two of the five descent horizons are vacuous

`G(·,0) ≡ 1`, so "0 multi-valued classes at r = 0" is true of *any*
partition, including REC and the scramble; at r = 4 exactly **1** class
is tested (the root).  The tested populations are `185, 72, 23, 6, 1`.
The content of ruling property 1 is at r = 1, 2, 3.  **Repair:** print
the per-horizon population beside the count (the code already computes
it) and say in §4 that r = 0 is definitional.

### MINOR-3 — the holonomy head's conjuncts are not independent

Conjunct (iii) (`0` non-unit factors on carrier-closing squares, hence
`r_k = r_q` at 1362 of 1362) is **entailed** by ruling property 1 plus
conjunct (ii), by the pin's own operator theorem.  The paper states the
theorem in §6 and then presents the count as one of four measured
conjuncts.  **Repair:** label conjunct (iii) "machine confirmation of
the operator's theorem, given property 1" — which strengthens the
section rather than weakening it.

### MINOR-4 — the flow identity's positive half is an algebraic identity

`w(h)·k_{4−|h|}(e|h) = w(h+e)` follows by substituting
`w = μ·G(·,4−|h|)/G(root,4)` and `k_r = q·G(h+e,r−1)/G(h,r)`; it holds
for any price law and any carrier, so `3968 of 3968` cannot fail.  The
content is the off-horizon `352 of 596`, which the paper does carry.
**Repair:** one clause — "the identity at the matched horizon is
definitional; what is measured is that it fails at every other."

### MINOR-5 — `G-VERIFY-PAPER` is a membership sweep, and the abstract oversells it

The sweep tests `{t ∈ paper tokens : t ∉ explained}` = ∅.  Transposing
two numerals that both occur in the paper preserves the token multiset
exactly, so the residue stays empty and the gate cannot fire — e.g.
swapping `1362` and `1402` in §6 passes.  `MUT-PROSE-NUMBER` only tests
an *alien* token (`918273`).  The instrument is sound for what it does
(750 tokens, 111 distinct, 0 unexplained — I reproduced the counts), but
the abstract's "Every number below renders from the receipt" claims a
rendering pipeline that does not exist.
**Repair:** reword to "every numeral of the paper is matched against a
value this run computed"; optionally add the placement-bound sweep the
*verdict* audit already implements (value bound to the segment that
carries it, by occurrence count) and a `MUT-PROSE-TRANSPOSE` that
documents the known blind spot.

### MINOR-6 — the one [B3] cell that speaks is never named

It is `(1, 2, 4)` at MENU-113.  The receipt has it; the paper says "the
fourth" and §14 poses "what distinguishes it" as an open without
identifying which cell is open.  **Repair:** name it in §8.1 and §14.

### MINOR-7 — the prune gate's subsample is 3 of 256 (1.2 %)

The prune is a *set* claim about all 256 bases; the gate exhibits it on
a 1.2 % prefix.  I ran 32 spread bases (12.5 %) and it holds exactly.
**Repair:** either raise the declared subsample to a spread sample (cost
~5 min) or state the coverage fraction in §5 beside the "3 of the 256".

### MINOR-8 — the k₁/k₂ comparison is stated across different windows

`0 of 30728` against `1340 of 3968`.  The like-for-like number is
`0 of 3968`, which I measured.  **Repair:** print it.

---

## PROSE AUDIT AGAINST THE RECEIPT

I extracted all **750** numeric tokens (**111** distinct — matching
`paper_sweep`) and audited them semantically, not by membership.  Every
load-bearing number in §§4–9, §13 and the verdict string was checked
against my own measurement.  Verified independently and exactly:
`1,8,60,452,3448,26760` / `1,9,69,521,3969,30729`; `113`, `185`, `2477`,
`5`, `162,179,184,185,185`, `17,5,1,0,0`; `[1,5,17,49,113]`,
`[1,5,13,45,113]`; `572`, `368`, `4`, `44`, `88`, `0` symdiff; `1546`,
`28`, `12`, `142`, `1458`, `70`, `2`, `6`, `10`; `1362`, `1402`, `473`,
`40`, `8`; `1538`, `64/65`, `65/64`; `102`, `3968`, `352`, `596`, `1`;
`30728`, `1340`, `3757`, `212`, `5/2`; `16`, `152672`, `3584`, `256`,
`796672`, `73728`, `60492`, `864`; `15/38, 5/19, 13/38`, `3/8, 1/4,
3/8`, `3/7, 1/7, 3/7`, `4/9, 1/9, 4/9`; `34,112,12,12`; `36,104,108,164`
and `1/97, 5/97, 1/18, 1/128`; `13,13,45,45` and `0,0,0,0`; `45`, `1900`,
`0`; `772`, `0`; `341`, `256,64,16,4,1`, `72`; `1373/1380`,
`5629529/5674560`; `5161`, `1365`, `3788`, `4`, `4`, `1700`, `30728`;
`265`, `462`, `6`; `19`, `11`, `13`, `1`.  `243768`/`243769`/`424` are
pinned citations, probe-resolved against `gprep_foundation_receipt.json`
and consistent with my own `d ≤ 5` census (which contains no `(3,3)`
block at all, as "all at depth 6" requires).  `60492` and `864` are the
one pair I could not reproduce base-for-base (the delivery's subsample is
the first 3 under *its* sort key, mine under mine) — both are confirmed
by rate: my per-base counts are exactly `20164` and `288`.

**No prose number is wrong.  No number moved.**

---

## BYTE-IDENTITY, AT MY OWN HANDS

I rebuilt a minimal tree at `<scratch>/tree/` containing only the 15
files the run reads or writes, every one extracted at commit 9e481db and
sha-verified, and ran the plain delivery **off-tree**, under `env -i`,
with `PATH` stripped to a directory containing nothing but the
interpreter (**git absent**), and `PYTHONHASHSEED=12345`.  Exit 0,
1162.8 s, `files written: 2`, `artifact integrity: output True, receipt
True`, `paper sweep: 750 numeric tokens, 0 unexplained`, `58 gates
against the published 58, 54 falsifiers against the published 54`.

```
giter_output.txt   58ddd86a52f2   BYTE-IDENTICAL to the committed artifact
giter_receipt.json 8d28b5f2f807   BYTE-IDENTICAL to the committed artifact
```

The `#91` off-tree / git-less byte-reproduction leg is confirmed by a
second party.  The repo's four unit files and the two notes are
unchanged at review end.

---

## CANDIDATE-READING RULINGS

| segment | ruling |
|---|---|
| `GITER-LAW-CONFIRMED` head | **licensed** — the carrier is re-derived and gated at 6 of 6, Γ is exact and column-stochastic, and every conjunct under it reproduces |
| `CARRIER=CONG-185-RE-DERIVED-IN-UNIT…SIX-RULING-PROPERTIES=6-OF-6` | **licensed as stated**, with MINOR-2's disclosure on the two vacuous horizons |
| `LAW=COLUMN-STOCHASTIC-EXACT…FLOW-IDENTITY…` | **licensed**, with MINOR-4's disclosure that the matched-horizon half is definitional |
| `TARGETS=HIT-AT-THE-LAW-VALUES…` | **licensed only with the carrier-free stamp** — MAJOR-2 |
| `STEP-NORMALISER-RE-PROVED-ON-THIS-CARRIER` | **not licensed as worded** — MINOR-1; the identity is law-native |
| `CENSUS-SHADOW=…DECLARED-EXTERNAL-CONTROL-NEVER-A-TARGET-TOKEN-SCAN-0-HITS` | **licensed, and stronger than claimed** — 0 hits on 31 tokens, not 9 |
| `HOLONOMY=AGREES-AT-REPRODUCED-AND-LOCATED…` | **licensed**, with MINOR-3's disclosure of conjunct dependence |
| `QUANTUM=CARRIER-RELATIVE-CONFIRMED-BY-MEASUREMENT` | **licensed** — measured at both carriers on four claims, all reproduced |
| `MECHANISM=THE-SIGNATURE-IS-CARRIED-BY-THE-MULTI-TARGET-EDGES-AND-THE-45-…` | **true but ungated as delivered** — MAJOR-1; licensed once the minimal-repair measurement is carried, and the 45-classes clause is correlational, not mechanical |
| `B3=…COUPLED=@CONG-185-FEASIBLE-4-OF-4-WITNESS-EXHIBITED;@MENU-113-INFEASIBLE-3-OF-4-FARKAS-CERTIFIED` | **licensed** — re-proved cell by cell from certificates, and the exceptional cell identified as (1,2,4) |
| `ATOM…delta*=0-AT-CONG-185…THE-BLOCK-SPLITS-INTO-5-CLASSES-ONE-PER-DEPTH` | **licensed** — every row reproduced exactly |
| `ANCHOR=SEDIMENTARY<…THE-GRADING-IS-CAP-DRIVEN-PURITY-AT-REFINEMENT-ROUND-4-OF-5>` | **licensed** on my share (the negatives reproduce and the cap-driven stamp is carried inside the segment); the cap-scope audit proper is the effectus lens's row |

---

## RECOMPUTATIONS

**123 independent recomputations, 0 disagreements.**  Honestly counted
as distinct measured quantities, not as gate invocations: 15 in the
family/carrier construction; 18 in the six ruling properties and the
square census; 5 in the two holonomies at three quotients; 13 in Γ, the
flow identity and CK; 6 in the readout; 7 in the deviation battery; 14
in the leg ensembles and the prune; 25 across the eight [B3] cells and
their certificates; 23 in R-SIG, the block and δ\*; 8 in the anchor and
supply measurements; 4 in the mechanism gate I built; 32 eq.-22 cells
(counted as 4, one per carrier × speaking/silent class); 2 token scans;
1 byte-identity leg.  Of these, **11 are measurements the delivery does
not carry** — the stability and monotone-splitting proofs of the fixed
point, `G(h,1) = M(h)` as an identity, k₁ at the k₂ window, the widened
token scan, the 32-base prune check, the identification of the (1,2,4)
cell, the CK-failure localisation, the minimal repair, the round-1
counterexample, the round-by-round CK ladder, and the like-for-like
scramble descent census.

---

## WHAT WOULD CHANGE THE GRADE TO A

Both MAJOR repairs, and MINOR-1's three tokens.  Nothing in the
arithmetic needs to move, no measurement needs to be redone, and no
delivered number is at risk.  The unit is, on my lens, the most
completely reproducible object I have audited in this programme: an
independent rebuild with different primitives at every layer above the
pinned law agrees with it on every one of the ~123 quantities I could
compute, and its artifacts are byte-identical off-tree with git absent.
