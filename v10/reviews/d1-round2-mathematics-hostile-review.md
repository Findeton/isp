# D1 hostile review round 2 — exact mathematics and marked restriction

**Referee:** independent exact-mathematics hostile review

**Date:** 2026-07-11

**Artifacts reviewed:** the frozen round-2 versions identified by the hashes
below.

**Verdict:** **PASS WITH ONE REQUIRED SCOPED CORRECTION**. The two finite
nonselection results and the executed common-root projectivity result pass.
The general marked eligibility helper has one exact complete-screen false
positive that must be repaired before it is reused as a generic filter.

## 1. Reproduction record

Commands run from the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 \
  code/.venv/bin/python \
  v10/code/d1_no_silent_center_exact.py

PYTHONDONTWRITEBYTECODE=1 \
  python3 \
  v10/code/d1b_marked_support_restriction_exact.py
```

Results:

- D1A exited `0` with `ALL CHECKS PASS (45/45)`.
- D1B exited `0` with `RECEIPT: 20/20 exact checks passed`.
- Two independent output runs of D1A had the same SHA-256:
  `a265b73f93e2fe23d77aebc2763152cc398240dcc98599442af68899d43d78ea`.
- Two independent output runs of D1B had the same SHA-256:
  `7fd754dbc69a9883fa1a904b3c6e4efda9d73b4c687dbaa38f126500bc7abdcc`.

Frozen source hashes at review:

```text
1b6e4ef3339d65941445f1277dd0d0afe59f3ea29763854c078a1d33f79f078d  v10/code/d1_no_silent_center_exact.py
a36a51d1951dd881f827ddba1fa5a7ba2407910dce18e171f445bcb0683b9bb3  v10/code/d1b_marked_support_restriction_exact.py
3f56214ff6700842fc6eeb32ffba18dc5d1acaa8ee26aaec2723a13755f70f75  v10/note-d1-no-silent-support-birth.md
10e7b17eb0fd46d21eaee5d8060c3826355db5dc3bb2d594a511c3880b5b6370  v10/relativistic-isp-v10-paper2-no-silent-centers-do-not-select-support-birth.md
```

## 2. Independent reconstruction

I rebuilt the D1A partition census with a separate Ruby set-partition
implementation rather than calling the production functions. It reproduced
the complete/minimal counts and blocks for S0--S7. In particular, the repaired
S5 witness has exactly three complete partitions: atomic lookup and the two
incomparable minima

```text
0 | 12 | 3
0 | 1 | 23
```

Every S5 atomic matrix is strictly positive, rank one, and has mass `25`.
The aggregate is

$$
\begin{pmatrix}22&18\\23&37\end{pmatrix},
\qquad \det=400,
$$

and both minima have cell-mass multiset `25,25,50`. Thus block count and
cell-mass entropy cannot select between them. All refinements of either
minimum remain complete because every atomic cell is rank one. This removes
the Simpson/refinement sensitivity of the round-1 witness.

Independent `BigDecimal`/`BigMath` evaluation reproduced the load-bearing
CMI reports. Examples are

```text
S5   = 0.013479848236960145570727598777808585645473681948043558408625...
AC|B = 0.1004082738565493933433188441379196669559065436702020657774...
BC|A = 0.074758407616630037918565984718225693152977752662268092047838...
```

The production code uses integer minors, not these transcendental values, as
the equality oracle. The refinement direction is correct: `refines(p,q)` in
the minimality loop means that `q` is a coarsening of `p`, so a reported
minimum has no strictly coarser complete partition above the visible screen.

For D1B I independently inspected the restriction algebra. Lineage and port
filtering, carrier intersection, the idempotent `projected` flag, support
intersection, and marginalization of the joint count law are associative on
nested retained sets. The receipt now checks every nonempty subset of
`{A,B,C}`, every nested nonempty restriction path, and projection versus
recomputation of the full eligible-support family. These checks pass exactly.

## 3. Round-1 openings

The round-1 openings were resolved honestly.

1. Target marginalization, change of visible screen, and typed history
   restriction are now distinct operations. The old G7c is explicitly called
   a screen/grain change, not a restriction counterexample.
2. The paper no longer claims that target marginalization refutes record
   projectivity. Typed projectivity is reported only for the executed
   common-root family and is left open universally.
3. S5 was replaced by the stronger strictly positive, refinement-stable,
   tied-complexity witness above.
4. O1 is now a cutwise over-eligibility theorem, not a claim that a three-pair
   birth history and one hyperedge birth history are dynamically equivalent.
5. One joint three-variable law supplies every pair marginal and all three
   triple bipartitions.
6. Boundary occupancy, all minimal-center CMI checks, separate X/Z
   relabelings, and the stated covariance coverage are now executable.
7. D1B makes parents, output ports, field carriers, existing supports,
   structural connectivity, and restriction maps operational. In particular,
   removing `C`'s output port removes every `C`-bearing candidate.

The covariance claim is correctly scoped. D1A executes every boundary
permutation for cells of at most four atoms and representative reversal/cycle
tests at eight atoms. General finite reindexing covariance follows directly
because partition enumeration, cell aggregation, rank, refinement, and
minimality are transported by a bijection. This is not a continuum or
profinite covariance theorem.

## 4. Required finding

### [Required correction] A complete marked screen is counted as an eligible support

`admissible_centers` permits selecting zero center fields. If the marked
screen is already complete, it therefore returns the screen partition with an
empty field-name tuple. `cut_center_status` retains that partition whenever
it is nonlookup, and `support_is_eligible` checks only that exactly one status
survives. The result is an exact false promotion: an already complete screen
is called an eligible support even though D1's rule says that no additional
center is identified.

I reproduced the opening by taking the common-root history and changing its
existing `H` field from kind `ancestor` to kind `screen`, without changing the
law. For the `A|B` cut the exact output is

```text
screen_complete_AB True
AB_status ((((0, 1), (2, 3)), ()),)
eligible_supports (AB, AC, BC, ABC)
```

The empty tuple in `AB_status` means that no center field was selected. This
should be a no-promotion verdict, not unique-center eligibility.

Required repair: distinguish “screen already complete” from “one nonempty
marked center algebra closes an incomplete screen.” For example,
`support_is_eligible` should require exact failure at the screen-only
partition and exactly one nonlookup minimal completion using at least one
center field. Add marked factorized and complete-screen refusal controls.

This defect does **not** change the executed common-root results: their
constant screen is exactly incomplete and `H` is a required nonempty center.
It also does not weaken either negative theorem. It blocks promotion of D1B's
current helper as a generic marked filter until repaired.

## 5. Minor finding

### [Minor] Same-partition fields with distinct provenance are silently collapsed

`admissible_centers` keys generated candidates only by boundary partition and
retains the shortest/lexicographically earliest field-name tuple. Adding a
second field `H2` with the same values and carrier as `H` but different stable
provenance returns only

```text
((((0, 1), (2, 3)), ('H',)),)
```

This is valid only if identical induced field algebras are explicitly
quotiented as center gauge and provenance is declared irrelevant to center
identity for the current cut. Otherwise the routine has hidden a marked
nonuniqueness with a lexical selector. The paper should state that quotient,
or the receipt should preserve all provenance-distinct generators of one
partition. The S5 theorem is unaffected because `R` and `C` induce different
partitions.

## 6. Findings that pass

- The exact conditional-independence criterion is correct for the occupied
  finite cells.
- Partition enumeration and the coarsening/minimality direction are correct.
- S0/S1 refusals and S2/S3 existence witnesses reproduce.
- S5 proves finite center nonuniqueness even under strict positivity, atomic
  rank-one stability, equal cell count, and equal cell-mass entropy.
- S6 is lookup-only and S7 has no boundary-definable closing partition.
- All six O1 cuts are strictly positive and have the same unique `H` center.
- Statistical dependence alone does not cross D1B's explicitly supplied
  structural-component boundary.
- Candidate generation remains an axiom; the receipt does not pretend to
  derive it from conditional independence.
- Typed restriction and support-family recomputation agree on the complete
  nonempty subset lattice of the tested common-root family.
- The paper correctly refuses a firing rate, outcome law, transfer law,
  universal projectivity, component-birth law, and profinite theorem.

## 7. Verdict and claim ceiling

The load-bearing paper result survives hostile reconstruction:

$$
\boxed{
\text{no-silent closure can identify centers inside supplied cuts, but it
does not generate or uniquely select record-support birth.}
}
$$

After the complete-screen eligibility repair, the accepted claim ceiling is:

1. an exact finite center census and refusal classifier on supplied seams;
2. a finite strictly positive center-nonselection theorem;
3. cutwise support over-eligibility for one supplied marked common-root family;
4. locality only relative to an explicitly supplied ancestry/support/field
   seam axiom;
5. typed projectivity only on the executed finite common-root restriction
   family.

No claim is accepted for a universal support-birth law, a unique marked center
modulo provenance, genuinely new component joining, a click intensity,
quantum dynamics, or a profinite/continuum extension.
