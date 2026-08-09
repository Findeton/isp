# TOP — HOSTILE REVIEW R1 (OPERATOR / ALGEBRAIC LENS)

**Reviewer:** R1, operator/algebraic lens.
**Object under review (SHA-256, first 12), each verified before reading:**

| artifact | pinned | measured | |
|---|---|---|---|
| `v13/paper-top-topology.md` | `ab09d091ed1d` | `ab09d091ed1d` | OK |
| `v13/code/top_topology_exact.py` | `e2d0200e4a06` | `e2d0200e4a06` | OK |
| `v13/code/top_topology_output.txt` | `bd213b18d1b1` | `bd213b18d1b1` | OK |
| `v13/code/top_topology_receipt.json` | `0fb290cf4bfd` | `0fb290cf4bfd` | OK |

Foundation: `v13/code/tb3_third_base_receipt.json` measured at
`c9bc956fe75129bdf411e4d1c1ce082d5866e7e63f12712e56f6f231dcf5a9a7`, equal to the
value pinned in the instrument's source. Protocol read as frozen at
`v13/note-top-hostile-protocol.md`; pin at `v13/note-top-topology-pin.md`;
RUNBOOK §13–§15 and all addenda read.

**Method.** I rebuilt TB3's three-wing base, its 36-chart atlas, its drawn-link
table and the coordinate-resolved complex on my own instrument, written from
TB3's §2 declaration and TOP's §2.3 declaration only, with deliberate
implementation differences (row-major operators instead of column dicts; chart
conjugation by index relabelling instead of two sparse matrix products; Born
keys of conjugated legs recomputed from the conjugated operator instead of
push-forwarded; admission clauses evaluated in a different order; F₂ rank by
lowest-bit pivot with rows consumed in a deterministic LCG-shuffled order and no
rank cap; components by BFS colouring instead of union-find; cycle rank from
Euler rather than from a forest count). The K4 census was recomputed with no
physics at all — pure permutation group theory on the eight labels. Scripts in
`/private/tmp/claude-501/-Users-felixrobles-workspace/82d34949-326c-4269-8dd0-587362126fa5/scratchpad/`
(`r1_atlas.py`, `r1_top.py`, `r1_rest.py`, `r1_extra.py`, `r1_2wing.py`,
`r1_k4.py`, `r1_k4b.py`, `r1_blockthm.py`, `r1_probe.py`). I also copied the
frozen instrument and the pinned TB3 receipt into scratch and ran the full
delivery there twice, so that nothing in the repository was written.

**Headline.** Every number in the delivery reproduced. I found **one hard
numerical error in the frozen paper** (a candidate-table cell that contradicts
the frozen output, the frozen receipt, and my independent census), one
consequential prose error that follows from it, one further misdescription of
the same table, and three structural findings about what the delivery's
headline quantities actually measure. No verdict is overturned.

---

## 0. Recomputation count

590 independently recomputed quantities, by block:

| block | count |
|---|---|
| artifact + foundation hashes | 5 |
| base rebuild (carrier, wing group, frames, checkpoints, admitted group, rule-selected Q) | 6 |
| ordered admitted chart pairs, per coordinate cell, 5 instances × 10 cells | 50 |
| per-cell block partitions + block-completeness, 5 × 10 | 50 |
| chart counts, 1-cell counts, 2-cell counts, coherent counts, 5 instances | 20 |
| per-checkpoint geometric 2-cells, 5 × 5 | 25 |
| N invariants (V,E,F,b₀,cycle rank,rank ∂₂,b₁,b₂,χ), 5 instances | 45 |
| N_coh invariants, 5 instances | 45 |
| per-checkpoint sub-nerve (E,F,b₀,b₁,b₂,χ), 25 | 100 |
| gluing formula + H₂-additivity, N and N_coh, 5 instances | 20 |
| block-incidence closed form (b₀,b₁), 25 checkpoint instances | 50 |
| estimator profiles (dimprofile, star, link) + split rows | 19 |
| simplicial nerve (maximal faces, χ), 5 | 10 |
| declared manifold controls, 3 × 8 | 24 |
| wing action (hom, free, equivariance, conjugation) | 4 |
| fixed-cell census, 6 group elements × 3 dimensions | 18 |
| orbit counts, direct and Burnside | 6 |
| quotient complex V,E,F,b₀,cycle rank,b₁,b₂,χ | 8 |
| orbit size distributions | 4 |
| three-wing transport graphs, 4 × 4 | 16 |
| two-wing control (Q, nodes, links, id links, cycle rank) × 2 + atlas 8 | 18 |
| ordered triangle defect multiset (6 entries + total) | 7 |
| GL(3,2) order by two routes + element-order spectrum | 7 |
| defect-order distribution at P* | 6 |
| locus size, K=GL, K⊆GL, on-locus, distinct generator sets | 5 |
| K = GL(3,2) by defect order | 6 |
| \|K\| distributions, family and locus | 16 |
| the 13-candidate table, 5 columns each | 65 |
| four-target comparison, 5 rows | 5 |
| lex-first completions at 6 orders + the transvection identity | 7 |
| five rule-selected rungs × 4 | 20 |
| P*-dependence sweep, 5 symmetries × 4 | 20 |
| extensional-duplicate and containment tests | 6 |
| coherence conjugacy-pattern census | 3 |
| OR-vs-XOR boundary reconstruction | 6 |
| scrambled-control arithmetic | 5 |
| anchor tally reconstruction, provenance split | 3 |
| full delivery rerun: artifacts byte-compared | 2 |
| **total** | **590** |

**Zero disagreements** between my instrument and the delivery's artifacts. The
one disagreement I found is between the delivery's **paper** and its own frozen
output/receipt.

---

## 1. K1 — the complex, and whether the invariants reproduce

### 1.1 What reproduced

I rebuilt the atlas from TB3's §2 declaration on my own instrument. The
rule-selected completion came out `(0,3,2,1,4,5,6,7)`, the atlas has 36 charts
over 6 seeds, and the ordered admitted-pair table matches **TB3's own committed
receipt cell by cell at all five instances** (all 50 cells), independently of
TOP:

```
reference   1260 1260 1260 1260  396 1260  396 1260 1260 1260   (= TB3 edges_per_cell)
partial     1260  396 1260  396  396  396  396  396 1260  396
asymmetric  1260  180 1260  180  396  180  396  180 1260  180
W-class     1260  396 1260  396  396  396  396  396 1260  396
equivariant    0   30    0   30    0   30    0   30    0   30
```

Every coordinate cell's overlap graph is a disjoint union of **complete** blocks
(measured, all 50 cells). At the reference eight cells give one block of 36 and
two — `(checkpoint 2, FULL)` and `(checkpoint 3, FULL)` — give three blocks of
twelve, which is exactly the paper's attribution.

The complete invariant table reproduced, by routes that share no code with the
delivery's:

| instance | 1-cells | 2-cells | b₀ | cyc | rank ∂₂ | b₁ | b₂ | χ |
|---|---|---|---|---|---|---|---|---|
| reference | 5,436 | 204,384 | 1 | 5,401 | 5,261 | **140** | 199,123 | 198,984 |
| equivariant | 75 | 100 | 1 | 70 | 50 | 20 | 50 | 31 |
| partially symmetric | 3,276 | 57,216 | 1 | 3,241 | 3,101 | 140 | 54,115 | 53,976 |
| asymmetric | 2,736 | 36,120 | 1 | 2,701 | 2,565 | **136** | 33,555 | 33,420 |
| W-class | 3,276 | 57,216 | 1 | 3,241 | 3,101 | 140 | 54,115 | 53,976 |

Coherent sub-nerve: 84,720 / 204,384 at the reference with b₁ = **161**,
b₂ = 79,480, χ = 79,320; 41,520 / 57,216 with b₁ = 151 at the two 3,276-cell
instances; 36,120 / 36,120 with b₁ = 136 at the asymmetric setting; 100/100 at
the equivariant control. Per-checkpoint: exactly the delivery's table, all five
b₁ = 0 at the reference, with Σb₀ = 5, Σb₁ = 0, Σb₂ = 199,123 = b₂ (H₂
additivity measured, not assumed — confirmed at all five instances and for the
coherent sub-nerve). Σb₁ = 21 for the coherent per-checkpoint decomposition, so
161 = 1 + 144 + 21 − 5.

The ordered triangle census is exactly 6× the geometric 2-cell count at every
instance, and the ordered defect multiset recomputes element by element to
TB3's committed multiset `{ABC:508320, ACB:151200, BAC:151200, BCA:132192,
CAB:132192, CBA:151200}`, whose identity entry is 6 × 84,720.

K₃₆ ⟹ contractible simplicial nerve: **verified**. The reference's unique
maximal face is the whole 36-chart set (a cone, hence contractible as a
homotopy statement), and the alternating binomial sum is 1. Both "routes" to
that χ are content-free — Σₖ₌₁ⁿ (−1)^{k+1} C(n,k) = 1 identically for every
n ≥ 1, and the cone argument says the same thing — but the paper says so
("predicted independently by the cone argument") and nothing rests on it.

All four committed three-wing transport graphs rebuilt on my instrument:
150/126/121, 99/75/70, 111/87/82, 75/51/46 — matching TB3's `a5_graph` and
`negative_controls` exactly.

### 1.2 FINDING F7 [MODERATE] — b₁ is a coordinate count, not a measurement of the atlas

Deriving the gluing identity myself: when every checkpoint sub-nerve is
connected and simply connected, the formula
b₁ = b₀ + (T−1)|V| + Σ(b₁ᵗ − b₀ᵗ) collapses to

$$b_1(N) \;=\; (T-1)\,(|V|-1).$$

Measured over the delivery's own objects:

| object | (T−1)(|V|−1) | measured b₁ |
|---|---|---|
| reference | 4 × 35 = 140 | 140 |
| partially symmetric | 140 | 140 |
| W-class | 140 | 140 |
| equivariant control | 4 × 5 = 20 | 20 |
| **the scrambled negative control** | 140 | **140** |
| asymmetric | 140 | 136 (Σb₀ᵗ = 9, not 5) |

Five of the six complexes the unit builds — including the scrambled atlas whose
identification data is destroyed — return b₁ = (T−1)(|V|−1) exactly. b₁ is
therefore a function of two integers, *five read times and thirty-six charts*;
the identification data enters only through the five per-checkpoint zeros.
§7.2 states this fact and then reasons past it ("b₀ and b₁ are exactly the
invariants the gluing formula pins to the checkpoint count and the chart
count"), but the abstract, the verdict string and §8's defended sentence all
still lead with b₁ = 140 as a *global-structure* datum.

By contrast b₂ **is** sensitive (199,123 → 81,748 under the scramble), and so
is χ. The honest headline is that the degree-2 invariant measures the atlas and
the degree-1 invariant measures the coordinate grid.

**Repair.** Present b₁ in its derived form (T−1)(|V|−1) in the verdict string
and abstract, and name the measured content as the five zeros — which is where
the information is (see F8). Nothing needs recomputing.

### 1.3 FINDING F15 [MODERATE] — the primary-complex choice: defensible, but "nerve" imports authority it does not have

The choice is declared (deviation 1) and the discarded object is computed and
reported, which is the right discipline. Two sharpenings:

(i) **N is not a nerve.** What licenses reading a nerve's homology as the
topology of the covered object is the nerve lemma; it applies to `N_simp` (which
is contractible and says nothing) and does not apply to `N`, which is a
presentation of the identification data indexed by (pair, checkpoint, rule).
§9 discloses part of this ("every other homology-like claim is an F₂ rank"), but
the abstract's "All of its topology is in the coordinates" and the verdict
string's "(b₀,b₁,b₂) = (1,140,199123)" read as invariants of the atlas.

(ii) **The convention is load-bearing and the delta is computable.** Collapse the
parallel 1-cells to one edge per pair — the simple overlap graph K₃₆ with all
7,140 triangles — and the same machinery gives b₀ = 1, b₁ = 0,
rank ∂₂ = 595, b₂ = 6,545. So the parallel-1-cell convention is what creates b₁
at all. Read with F7, the degree-1 statement is: 140 = (5−1)(36−1) counts
coordinate cells and charts.

I do **not** treat this as grounds for rejection: the pin's literal first
question is answered correctly and the deviation is declared. It is grounds for
qualifying the verdict string.

---

## 2. K2 — b₁ = the read times: both halves

### 2.1 Both halves verified

**Half one** — every checkpoint sub-nerve has vanishing first F₂-homology at the
reference: verified by my own elimination (b₁ = 0 at all five checkpoints), and
independently by the closed form below (no elimination at all).

**Half two** — the elimination-free formula 1 + 144 + 0 − 5 = 140: verified,
and the global elimination on my instrument returns 140 by a different pivot
rule, a different row order and no rank cap. Also verified at the other four
instances, including the two where the mechanism differs (partially symmetric
and W-class: Σb₀ = 7, Σb₁ = 2, 1 + 144 + 2 − 7 = 140; asymmetric: Σb₀ = 9,
Σb₁ = 0, 1 + 144 + 0 − 9 = 136).

**The coherent sub-nerve's b₁ = 161** coheres arithmetically with the temporal
reading and, read carefully, *contradicts* its content — which the delivery says
in §3.4: 161 = 1 + 144 + 21 − 5, so 21 of the coherent complex's cycles live
inside a single read time. See F16 below.

### 2.2 FINDING F8 [STRENGTHENING] — the five zeros have a closed form; the sentence is about partition nesting, not time

Independent third route, offered as a repair rather than a defect. Let a
checkpoint's two rules give partitions P (FULL) and R (REALIZED) of the charts
into complete blocks, and let every all-edges-drawn triple be a 2-cell. Then

> b₀(N_t) = b₀(I_t) and b₁(N_t) = cycle rank of I_t,

where I_t is the bipartite **block-incidence graph** whose vertices are the
blocks of P and the blocks of R and whose edges are the block pairs that share a
chart.

Proof sketch: within a complete block all triangles are 2-cells, so each block's
cycles die; a bigon on a pair drawn by both rules is the sum of two 2-cells
differing in one edge's rule; what survives is exactly the alternation between
blocks of the two partitions.

Tested at **all 25 (instance, checkpoint) pairs — 25/25 agreement**, including
both b₁ = 1 cases:

```
reference    ckpt 0,1,4 : I has V 2 E 1 -> (1,0)   ckpt 2,3 : V 4 E 3 -> (1,0)
partial      ckpt 0,1,4 : V 4 E 3 -> (1,0)         ckpt 2,3 : V 6 E 5 -> (2,1)
asymmetric   ckpt 0,1,4 : V 7 E 6 -> (1,0)         ckpt 2,3 : V 9 E 6 -> (3,0)
equivariant  every ckpt : V 7 E 6 -> (1,0)
```

So "every checkpoint sub-nerve has vanishing first homology" is exactly "at
every read time the FULL and REALIZED block partitions are nested (their
incidence graph is a forest)" — at the reference because one rule always draws a
single block; at the asymmetric setting because the 6×6 partition refines the
3×12 one; and it fails at the partially symmetric and W-class settings because
there neither partition refines the other, which is precisely the measured
b₁ = 1.

This makes the delivery's deepest sentence exact and shows where its content
actually sits. Recommended as a §3.3 addition.

### 2.3 FINDING F16 [MODERATE] — the defended sentence is false on the cocycle-respecting complex, and the paper contains the refutation

§8's defended sentence says "at the declared base the whole of that topology in
degree one is the comparison of read times." That is a statement about `N`,
whose 2-cells include 119,664 triangles whose three drawn maps do **not**
compose to the identity. On `N_coh` — which §2.3 itself introduces as "the
cocycle condition an atlas's transition maps **must** satisfy" — the statement
is false: Σb₁ᵗ = 21, so 21 of its 161 degree-one classes are intra-checkpoint. I
confirmed the 21 independently.

The paper reports the 21 in §3.4 and draws the right local conclusion. The
defect is that the sentence the unit says it "will defend" is asserted of the
complex where it happens to hold, without the qualifier that its neighbour
paragraph supplies.

**Repair.** Add "of N" and a clause: "on the coherent sub-nerve twenty-one of
the 161 classes are intrinsic to a single read time."

---

## 3. K4 — the dissolved exclusivity

Recomputed with no physics: labels = F₂³ with a = 4s_A + 2s_B + s_C, σ_P the
induced bit permutation, d_P(q) = σ_P⁻¹q⁻¹σ_Pq, K(q) = ⟨d_P(q)⟩, GL(3,2) the
F₂-linear label bijections.

### 3.1 What reproduced

|GL(3,2)| = 168 by two routes (brute force over the 8! label permutations, and
the invertible-3×3-over-F₂ count (8−1)(8−2)(8−4)); element orders exactly
{1,2,3,4,7}, spectrum {1:1, 2:21, 3:56, 4:42, 7:48}.

P* is the instrument's `[pi for pi in sp.PERMS if pi != sp.IDENT][0]` = the
transposition `ACB`. At that P*:

- ord d_{P*} distribution over the 5,040 completions: **48 / 384 / 1728 / 1152 /
  1152 / 576** — matches TB3's committed distribution.
- locus size **384**; K = GL(3,2) at **252**; K ⊆ GL(3,2) at **336**; on the
  locus **48**; distinct generator sets built **2,502** (the receipt's
  `distinct_defect_subgroups_built`).
- K = GL(3,2) by defect order: **{1:4, 2:48, 3:72, 4:128, 5:0, 6:0}**.
- |K| distributions over the family and over the locus: identical to the
  receipt, entry for entry.
- the five rule-selected rungs: (1, |K|=1, 1 linear, ≠GL), (2, 168, 168, **=GL**),
  (3, 12, 1, ≠GL), (6, 2520, 168, ≠GL), GHZ (3, 360, 24, ≠GL).
- the whole 13-candidate table, all five columns, **matches the frozen output
  exactly** — including the cell where the paper does not.
- the four-target comparison rows match exactly.

### 3.2 FINDING F1 [MAJOR — factual error in the frozen paper]

§5.2's candidate table prints, for **C7 (involutive profile), clause (c)**, the
value **0**. The frozen output line 136 prints **6**; the frozen receipt records
`"c_completions_with_a_non_linear_K": 6, "c_passes": false, "clauses_passed": 0`;
and my independent census gives **6**.

The consequential prose error is in the same section: "C4, C5, **C7**, C9 and
C10 predict linearity perfectly." C7 does not. With the correct value C7 passes
**zero** of the three clauses, not one, so the paper's own reading of the family
("splits cleanly into two halves") mis-sorts one of its thirteen members.

This is exactly the failure class the RUNBOOK appendix records at #24 —
a number in the prose that the instrument never produced. The instrument is
right; the paper is wrong.

**Severity.** Major as an error of record — it is a wrong number in a frozen
paper's primary table, and it survived delivery. It does **not** move the
verdict: no candidate passes all three clauses either way, and "the best reach
2 of 3" (C1 and C2) is unchanged.

**Repair.** `0` → `6` in the table; delete C7 from the linearity list; the
sentence then reads "C4, C5, C9 and C10 predict linearity perfectly."

### 3.3 FINDING F2 [MODERATE] — C8 is misdescribed in the same paragraph

"C1, C2 and **C8** hold on the locus and nowhere off it — and do not predict
linearity: 320 of the 384 order-2 completions have a K with a non-linear
element."

C8's clause (a) is **192/384**: it does not hold on the locus. The receipt
records `a_passes: false`, `clauses_passed: 1`. Only its clause (b) is zero.
The "320 of 384" figure belongs to C1/C2; C8's clause-(c) count is 128.

**Repair.** "C1 and C2 hold on the locus and nowhere off it; C8 holds nowhere
off it but on only half of it."

### 3.4 FINDING F3 [MAJOR — clause (c) has no measured content]

I tested, exhaustively over the 5,040, which candidates pass clause (c) and
why. The passers are exactly **{C4, C5, C9, C10}**, and every one of them is a
**subset of C4 = {q : K(q) ⊆ GL(3,2)}** (verified as sets, not counts):

- **C4** — disclosed by the paper: a group generated by F₂-linear maps is
  F₂-linear. Verified C4 = {q : K(q) ⊆ GL(3,2)} exactly (336 = 336).
- **C5** (q itself linear) — **not disclosed**. All six σ_P are measured
  F₂-linear, so d_P = σ_P⁻¹q⁻¹σ_Pq is linear whenever q is, so K is linear.
  C5 ⊂ C4 verified.
- **C10** (q a collineation of PG(2,2)) — **not disclosed**, and worse: over the
  prime field F₂ the collineation group of the Fano plane *is* GL(3,2), so
  **C10 ≡ C5 extensionally** (verified as sets; both hold at 168 with 126
  reaching GL(3,2)). This is an undisclosed extensional duplicate exactly
  parallel to the disclosed C1 ≡ C2.
- **C9** (q normalises the wing group) — **not disclosed**. Then
  d_P ∈ ⟨σ_P⟩, whose six elements are all F₂-linear, so K ⊆ wing ⊆ GL(3,2).
  Verified: all 12 completions satisfying C9 have K contained in the wing group.

The general statement, which the delivery never makes: clause (c)'s count for a
candidate C is **|C \ C4|**, so "clause (c) passes" is literally "C ⊆ C4" — a
set containment inside the declared family, not a measurement about the
geometry. Clause (c) therefore separates nothing that clauses (a) and (b) had
not already separated, and the paper's contrast — "the family splits cleanly
into two halves that fail in opposite directions… C4, C5, C7, C9 and C10 predict
linearity perfectly" — presents an algebraic tautology as a measurement in four
places (and, per F1, wrongly in a fifth).

Deviation 7 does the right thing for C4 and for C1≡C2; the same treatment is
owed to C5, C9, C10 and to C5≡C10.

**Repair.** State clause (c) as the containment C ⊆ C4; disclose the forcing for
all four passers; add C5 ≡ C10 to the disclosed duplicates. The verdict is
untouched — indeed it is *strengthened*, because clause (c) turns out to be
incapable of naming a selector on its own.

### 3.5 FINDING F4 [MODERATE] — P* is an undeclared arena coordinate

The census's two headline objects — "the order-2 **locus**" and the **defect
order** axis of the 252-table — are defined relative to a single wing symmetry
P*, which the paper never names and which the instrument picks by enumeration
order (`[pi for pi in sp.PERMS if pi != sp.IDENT][0]`, i.e. the transposition
`ACB`). I swept all five non-identity wing symmetries:

| P* | type | locus | ord distribution | K = GL by ord | on-locus |
|---|---|---|---|---|---|
| ACB, BAC, CBA | transposition | **384** | 48/384/1728/1152/1152/576 | {1:4, 2:48, 3:72, 4:128} | **48** |
| BCA, CAB | 3-cycle | **270** | 18/270/1080/1296/648/432/**1296 at order 7** | {3:72, 4:72, **7:108**} | **0** |

The 252 completions with K = GL(3,2) are P*-independent (K does not depend on
P*), but the locus and the order axis are not. At a 3-cycle P* the verdict
string's own sentence would read "the order-2 locus holds **270** completions of
which **0** reach GL(3,2)". RUNBOOK §15 requires arena coordinates declared as
data; §14 requires a self-test under the symmetry's own action. Neither is done
for P*, and P* is the coordinate the entire §5 hangs on.

**Repair.** Name P* in §2.2 and §5.1, and either report the measured invariance
across the three transpositions with the 3-cycle contrast, or scope the verdict
string's 384/48 to a transposition P*. Note this only strengthens NOT-FOUND.

### 3.6 FINDING F5 [MODERATE, mostly a strengthening] — "never at 5, 6" is a theorem, and the paper's argument is right

Verified in full. d_{P*}(q) is a generator of K(q), hence lies in it (checked at
all 5,040); GL(3,2)'s element orders are {1,2,3,4,7}; therefore
ord d_{P*}(q) ∈ {5,6} ⟹ K(q) ⊄ GL(3,2). Measured: **0 of the 1,728**
order-5/6 completions have K ⊆ GL(3,2). The paper's sentence is exactly
correct as an argument, not a coincidence.

Two things it does not say and should:

1. The two exclusions cost different amounts. Order 5 is **Lagrange-immediate**
   (5 ∤ 168). Order 6 is **not** (6 | 168) — it needs the actual element-order
   spectrum of GL(3,2) ≅ PSL(2,7), which has no element of order 6. "Exactly the
   orders GL(3,2) has no element of" flattens a divisibility fact and a
   classification fact into one.
2. **Converse status: strongly false.** 3,060 of the 3,312 completions with
   ord ∈ {1,2,3,4} have K ≠ GL(3,2). The condition is necessary and nowhere
   near sufficient. §5.3 says "not sufficient" in prose; the number is the
   sharper statement.

Incidental: at a transposition P* no completion realises an order-7 defect at
all (max order 6); at a 3-cycle P*, 1,296 do. Neither is recorded.

### 3.7 FINDING F6 [MODERATE] — §5.3's explanation under-determines its explanandum

"linearity of the completion, not the order of its defect, is what puts K
**inside** GL(3,2)" is a theorem — verified, all 168 linear completions have
K ⊆ GL(3,2). But what the ladder asserts at the ord-2 rung, and what §5.3 sets
out to explain, is the **exclusive visit**: K **equal to** GL(3,2). Linearity
gives containment only:

- of the 168 linear completions, **126** have K = GL(3,2) and 42 do not;
- the ord-1 target is the identity completion, which is linear and gives
  K = {1};
- on the locus, "q linear" and "K = GL(3,2)" are **different sets** (32 linear,
  of which 24 reach GL(3,2); a further 24 non-linear completions also reach it,
  making the 48).

So linearity separates {ord 1, ord 2} from {ord 3, ord 6} among the four A1
targets, and does not separate ord 2 from ord 1 — as the paper's own four-target
table shows (C5 holds at both). The attribution of the exclusivity to the
lex-first rule is correct and I verified its mechanism: the lex-first
order-2 completion is `(0,1,2,3,5,4,7,6)`, which is precisely the transvection
(s_A,s_B,s_C) ↦ (s_A,s_B,s_C⊕s_A), is F₂-linear, and gives K = GL(3,2). The
*explanation* of why it lands on equality, rather than mere containment, is
missing.

**Repair.** Scope the sentence to containment, and say plainly that what
supplies equality at this particular q is not measured here.

### 3.8 The freeze audit

The candidate family and the three clauses are declared in the source above
every measurement, and `_K_AT_DECLARATION == 0` is gated with `selfreeze-lax`
dying on it. That is an ordering fact **within one execution** only, which
TOP-DECLARATION-ORDER discloses in exactly those words. No in-run measurement
can do better, and the disclosure is correctly worded. I have no finding here
beyond noting that six of the thirteen candidates are labelled `"origin":
"worker"` in the receipt, which is the honest label.

---

## 4. K3 — uniformity ≠ manifoldhood (spot-verified)

All of §4 reproduced on my instrument:

- reference: **one** distinct estimator value across all 36 charts;
  dimprofile `(35,35,35,35,11,35,11,35,35,35)`, star `(302, 17032)`,
  link `(35, 17032, 1, 16998)`.
- the two 11-entries sit at `(2, FULL)` and `(3, FULL)`, the two cells whose
  overlap graph is three complete blocks of twelve — the paper's attribution is
  correct.
- partially symmetric and W-class: **two** values, split **24/12**, witnesses
  `ABC|ACB` and `ABC|BAC`; majority star `(182, 4828)` / link
  `(35,4828,1,4794)`, witness star `(182, 4648)` / link `(35,4648,1,4614)` —
  the 180-fewer-2-cells claim confirmed.
- the three declared controls: 2-sphere (χ 2, b₁ 0, b₂ 1, every link a circle),
  9-vertex torus (χ 0, b₁ 2, b₂ 1, every link a circle), pinch (χ 3, b₁ 0,
  b₂ 2, **not** a circle, witness vertex 0). Positive and negative in one
  family, on the same code path — confirmed.
- no link is a circle at the atlas: b₁(link) = 16,998 everywhere.

**On the verdict name.** The protocol asks whether `CONSISTENT` is honest when
the reading is instance-specific and non-manifold. My view: the *string*
carries its own qualifier — the emitted verdict is a 90-word sentence that says
"not a single number", "realising dimensions (11,35)", "a link is never a
circle", "the uniformity is NOT manifoldhood", and "INSTANCE-SPECIFIC, holding
at 3 of the 5 declared instances", naming the two failing instances. §9 repeats
all three qualifications. The pre-registered vocabulary in the pin is
`CONSISTENT | INCONSISTENT-⟨witness⟩`, so there was no third name available, and
the computed qualifier is where the honesty is required to live. I find this
**acceptable as delivered**, with one small note: a reader who quotes only the
head `TOP-MANIFOLD-READING-CONSISTENT` gets a false impression, and the paper's
§8 does quote it that way ("`TOP-MANIFOLD-READING-CONSISTENT` with its computed
qualifier"). A hyphenated head — `CONSISTENT-NOT-MANIFOLD` — would be within the
pin's family and would remove the risk. Low severity; a suggestion, not a fault.

One thing the paper does not print: at the **asymmetric** instance the reading
is `CONSISTENT` with dimprofile `(35,5,35,5,11,5,11,5,35,5)` — **three**
distinct local dimensions {5, 11, 35}. §4.2 gives only the distinct-value count
for that row. Printing it would make the "not one number" point harder.

---

## 5. K5 — instrument (at the protocol's lower depth)

### 5.1 What I verified

- **Determinism / provenance.** I copied the frozen instrument and the pinned
  TB3 receipt into scratch and ran the full delivery twice
  (`--falsification-selftest`, all 29 mutants each time; both exit 0). Both
  regenerated artifact pairs are **byte-identical** to the frozen ones — a
  three-way match at `bd213b18d1b1` and `0fb290cf4bfd`. Nothing in the
  repository was written; the four frozen artifacts still hash to their pinned
  values after my run. The frozen artifacts therefore provably come from the frozen source
  and the pinned foundation — and the C7 discrepancy in F1 is a paper-only
  error, now confirmed against a regenerated artifact.
- **Anchors.** 196, 0 failing; provenance split 172 external
  (171 `TB3 committed receipt` + 1 `this file, pinned SHA-256`) / 24
  declared-standard, reproducing the paper's §10 table. The declared sides of
  the 171 genuinely read from `tb3["tables"][...]` of the hash-pinned JSON, not
  typed. The anchor tally reconstructs exactly: 1 + 7 + (5 × 18) + 6 + 24 +
  (1 + 6 + 6 + 25) + (2 × 5 + 4) + 16 = 196.
- **Corrupt-and-fire on the pin.** `pin-hash` exits 1 falsifying
  TOP-PIN-TB3 / TOP-BASE / TOP-VERDICT.
- **Mutants.** All 29 exit 1; every must-pass gate falsified (`never_falsified`
  empty); 26 of 28 by a computation mutant; the two waiver-only gates named.
  Reproduced in my rerun.
- **Burnside vs enumeration.** Independently reproduced: (6, 996, 34,104) by
  direct orbit enumeration and by Burnside on my own fixed-cell census
  {ABC:5436, ACB:180, BAC:180, BCA:0, CAB:0, CBA:180} and
  {ABC:204384, ACB:0, BAC:0, BCA:120, CAB:120, CBA:0}. Orbit sizes 816×6 +
  180×3 and 34,044×6 + 60×2. Quotient (1, 25, 33,138), χ = 33,114,
  χ(N)/6 = 33,164, correction −90 + 40 = −50. The two routes are related by a
  theorem but are genuinely different traversals, and the theorem's hypothesis
  (that it is a group action) is separately gated and separately reproduced by
  me (homomorphism, free on charts, table preserved, maps conjugated, 2-cells
  permuted).
- **Cell-completeness.** Ordered census = exactly 6 × geometric at all five
  instances, verified on my instrument; the drop-one probe breaks it.
- **H₂-additivity is measured, not assumed** — confirmed, at all instances and
  for the coherent sub-nerve.
- **Two-wing positive control.** Rebuilt from scratch at NW = 2:
  Q = (0,1,2,3) and (0,1,3,2), nodes 8, links 11 / 13, id links 5 / 7,
  cycle rank 4 / 6 — matching TB3's committed two-wing graph. The two-wing
  atlas: 4 charts, 44 1-cells, 104 2-cells (56 coherent), b₀ 1, b₁ 9, b₂ 72,
  χ 64. So the F₂ homology machinery is genuinely anchored to a committed
  number (b₁ = 6), as claimed.

### 5.2 FINDING F9 [MODERATE] — the coherence "two independent routes" are one route plus an anchor

TOP-COHERENCE claims "THE COHERENT 2-CELLS ARE COUNTED TWICE, INDEPENDENTLY…
route 2 reads the ORDERED DEFECT MULTISET… and takes the entry at the identity."

Both are computed inside the same loop from the same three drawn maps, and the
three traversal defects are conjugate: d₂ = p₁d₁p₁⁻¹ and d₃ = (p₂p₁)d₁(p₂p₁)⁻¹.
I ran the pattern census at the reference: (d₁=id, d₂=id, d₃=id) takes exactly
two values — **(T,T,T) at 84,720 cells and (F,F,F) at 119,664** — never mixed.
So the multiset's identity entry is *identically* 6 × (coherent cells). That is
the pattern RUNBOOK §13's #234 addendum names by name: "a pair related by an
algebraic identity is one route."

What the second computation genuinely buys is different and better: the defect
multiset is anchored **exit-1 against TB3's committed receipt**, so the coherent
count is externally pinned. The `coh-lax` mutant does die on the gate. The claim
to fix is the word "independently", not the evidence.

**Repair.** Re-describe as "one route, externally anchored through TB3's
committed defect multiset", and note the conjugacy that makes the identity entry
6× the coherent count.

### 5.3 FINDING F10 [MINOR] — the OR-vs-XOR fix confirmed; no mutant covers the boundary assembly

I reconstructed the buggy assembly on the orbit complex, where a cell can meet a
face twice (240 of the 996 1-cell orbits have both endpoints in one vertex
orbit; 120 of the 34,104 2-cell orbits have a repeated edge orbit):

| assembly | rank ∂₁ | cycle rank | rank ∂₂ | b₁ | b₂ |
|---|---|---|---|---|---|
| XOR (as delivered) | 5 | 991 | 966 | **25** | 33,138 |
| OR (the bug) | 6 | 990 | 966 | **24** | 33,138 |

The 24 → 25 delta the protocol names is exactly reproduced. The bug **is**
caught — but only incidentally, by TOP-COMPONENTS (union-find would still say
b₀ = 1 while the rank route would say 0). Note ∂₂ is unaffected here, so an OR
regression confined to ∂₂ would move nothing and no gate would see it; and
TOP-QUOTIENT's only falsifier is the generic `rank-lax`, nothing
quotient-specific. §14's lesson applies ("a wholesale-replacement mutant does not
test that the RIGHT invariant is computed").

**Repair.** Add an `or-lax` mutant that assembles boundary rows with OR.

### 5.4 FINDING F11 [MINOR] — the chain-complex property is sampled where an argument exists

`Complex.invariants` checks ∂₁∂₂ = 0 on `self.tris[:2000]` only — 2,000 of
204,384 on the nerve, 2,000 of 34,104 on the quotient — and records it as a
disclosure. Both rank routes presuppose it: route 1 caps at `maxrank=cyc_rank`
(which would silently mask an image not contained in the cycle space) and route
2's cotree projection is rank-faithful only on cycles.

In fact ∂₁∂₂ = 0 holds identically for both complexes here (each 2-cell's three
1-cells are the three sides of a triangle; on the orbit complex the vertex-orbit
map is orbit-constant, so the same cancellation survives). Nothing is wrong.
The defect is that a guard is a 1% sample where a two-line argument is
available.

### 5.5 FINDING F12 [MINOR] — the pair table's symmetry is assumed, not gated

`nerve_edges` draws a 1-cell for `(a,b,cell)` only when the **ordered** pair
(a,b) with a < b appears in the admission table. If admission were not
symmetric the complex would depend on chart indexing. I measured the relation
symmetric at all 10 cells of all 5 instances, so nothing moves — but it is an
ungated assumption in a construction whose whole content is a 1-cell census.

### 5.6 FINDING F13 [TRIVIAL] — one anchor's provenance label

`A-PIN-TB3` is counted **external** (172 = 171 + 1), but its *declared* side is
the SHA-256 literal typed in the instrument; only its computed side comes from
outside. TOP-ANCHOR-PROVENANCE's own text defines an external anchor as one
whose "declared side comes from bytes outside this file". The 172/24 split is
printed in §10 as a provenance claim. Reclassify or footnote.

### 5.7 FINDING F14 [MINOR] — §7.2 explains a null result with an unmeasured reason

"a scramble that preserves per-checkpoint connectivity and simple-connectivity
cannot move them." The scrambled atlas's per-checkpoint b₀/b₁ appear nowhere in
the output or the receipt, and b₁ = 140 does **not** establish Σb₀ᵗ = 5,
Σb₁ᵗ = 0 — Σb₀ᵗ = 7 with Σb₁ᵗ = 2 also gives 140, which is exactly what happens
at the partially symmetric instance. The reason offered for the null is itself
unmeasured. Cheap to fix: print the scrambled atlas's per-checkpoint
decomposition.

---

## 6. What survives, and what must change

**Survives, fully verified on an independent instrument:** the completeness of
the overlap graph and the contractibility of the simplicial nerve; the entire
invariant table at all five instances; both halves of the b₁ claim; the coherent
sub-nerve and the 21; the dimension estimator and all three manifold controls;
the whole wing-action and quotient section including both orbit routes and the
−50; the two-wing and three-wing positive controls against TB3's committed
bytes; the ordered defect multiset; the whole GL(3,2) census, the 252/5,040
distribution, the "never at 5, 6" theorem, the lex-first attribution and the
transvection identification; determinism byte-for-byte.

**Must change (paper only, no recomputation needed):**

1. **F1** — §5.2 table, C7 clause (c): `0` → `6`; delete C7 from "predict
   linearity perfectly"; C7 passes zero clauses.
2. **F2** — §5.2: C8 does not hold on the locus (192/384); reword.
3. **F3** — disclose that clause (c) is the containment C ⊆ C4, and that all
   four of its passers are analytically forced; add C5 ≡ C10 to the disclosed
   extensional duplicates.
4. **F4** — name P*; report the transposition/3-cycle sweep or scope the
   verdict string's 384 and 48.
5. **F16** — qualify §8's defended sentence with the coherent sub-nerve's 21.
6. **F7 / F15** — carry b₁ = (T−1)(|V|−1) in the abstract and verdict string,
   and say that the degree-1 invariant is insensitive to the identification data
   (the unit's own scrambled control shows it), while b₂ is not.
7. **F5, F6** — sharpen the order-5-vs-order-6 argument and scope the
   §5.3 linearity sentence to containment.
8. **F9** — re-describe the coherence "two routes" as one route plus an external
   anchor.

**Should change (instrument, for the successor):** an `or-lax` mutant (F10); the
∂₁∂₂ argument in place of the 2,000-cell sample (F11); a symmetry gate on the
pair table (F12); the anchor-provenance label (F13); the scrambled atlas's
per-checkpoint census (F14).

None of the eight paper repairs changes a computed number in the instrument, and
none changes a pre-registered verdict:
`TOP-GLOBAL-STRUCTURE-⟨computed⟩`, `TOP-MANIFOLD-READING-CONSISTENT⟨…⟩` and
`TOP-FANO-SELECTOR-NOT-FOUND⟨…⟩` all stand as emitted. F3 and F4 in fact
strengthen NOT-FOUND.

I tried to break this unit at its arithmetic and could not: 590 recomputations,
zero disagreements with the instrument. The one disagreement is between the
paper and the instrument, and the instrument is right.

---

## GRADE

**ACCEPT-WITH-FIXES.**

A REJECT is not warranted: every computed quantity in the delivery reproduced on
an independently written instrument, the external anchors trace to TB3's
committed bytes, the artifacts regenerate byte-identically from the frozen
source, and all three verdicts stand. A plain ACCEPT is not warranted either:
the frozen paper contains a wrong number in a primary table (F1) together with
the prose error that follows from it, a second misdescription of the same table
(F2), a clause presented as a measurement that is a set containment forced by
algebra in every case where it passes (F3), and an arena coordinate on which the
whole selector census depends that is never declared (F4). Fixes 1–8 are
paper-level and mechanical; the instrument-level items are for the successor.
