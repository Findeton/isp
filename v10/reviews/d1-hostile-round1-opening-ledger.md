# D1 hostile review round 1 — opening and disposition ledger

**Date:** 2026-07-11  
**Status:** every concrete opening was investigated before hostile round 2.  
**Purpose:** this is the primary author's disposition ledger, not a substitute
for the independent referee reports.

## 1. Exact mathematics referee

The referee independently ran the original 36/36 receipt twice, obtained
SHA-256
`f0ee8bbe3c6bbff8c46e6915ebba42f52246d9644fc4dcc315f228f543696f9a`,
and rebuilt the partition census in Ruby with independent high-precision CMI
reports.

### Openings

1. G7c changed the visible screen on the same table; it was not a restriction.
2. G7b was a target marginalization and could not establish failure of typed
   record projectivity.
3. Executable covariance coverage was too small for the prose.
4. “Irreducible” and “force promotion” exceeded the receipt.
5. Occupied boundary support and every minimal-center CMI needed explicit
   checks.

### Disposition

- D1A now classifies target marginalization and screen/grain change separately.
- D1B defines and executes a typed record-history restriction.
- All boundary permutations are executed for cells with at most four atoms;
  reversal/cycle representatives are executed for the eight-atom cell; `X`
  and `Z` relabelings are separate.
- The paper says “identify a center inside a supplied cut,” not “force birth.”
- Every boundary atom is required to have positive mass in the production
  cells, and exact/CMI agreement is checked for every reported minimum.

## 2. Independent reconstruction/adversary referee

The referee independently reconstructed the core census in Ruby and supplied a
stronger strictly positive witness:

$$
M_0=\begin{pmatrix}16&4\\4&1\end{pmatrix},\quad
M_1=\begin{pmatrix}3&2\\12&8\end{pmatrix},\quad
M_2=\begin{pmatrix}1&4\\4&16\end{pmatrix},\quad
M_3=\begin{pmatrix}2&8\\3&12\end{pmatrix}.
$$

Every atom has rank one, positive entries, and mass 25. The aggregate has
determinant 400. Exactly three partitions are complete: atomic lookup and two
incomparable minimal three-cell partitions. Both minima have cell masses
`25,50,25`.

### Disposition

- The original S5 was replaced by this witness.
- D1A checks strict positivity, atomic rank one, exact completeness census,
  incomparability, equal block count, and equal cell masses.
- D1B represents the two minima by actual marked fields rather than arbitrary
  partitions.
- All three pair cuts and all three bipartitions of the triple are tested.

## 3. Ontology/locality referee

The referee accepted the exact probability calculation but graded the record
claim MAJOR REVISION.

### Openings

1. Support and parent labels were inert annotations.
2. The O1 receipt established cutwise over-eligibility, not equivalence of a
   pair-event history and a hyperedge history.
3. Target marginalization, boundary coarse-graining, screen deletion, and
   record restriction were conflated.
4. Center identification was described as event promotion.
5. Statistical factorization was described as record disconnection without a
   structural support/ancestry graph.

### Disposition

- D1B adds named lineages and ports, a parent map, marked fields with carriers
  and stable provenance, support marks, a structural graph, a seam generator,
  and a typed restriction map.
- Removing a lineage's output port removes all candidates containing it.
- Common parentage affects connectivity; marked fields affect the center
  algebra; existing supports affect connectivity; every object is projected
  by restriction.
- A statistically dependent but structurally disconnected cell generates no
  cross-component candidate seam.
- The theorem is now “no selection from a supplied candidate family.” No
  equivalence of generative decompositions is claimed.
- Typed restriction passes the tested common-root family; universal
  projectivity is recorded as open, not refuted or proved.

## 4. Repaired receipts before round 2

- `d1_no_silent_center_exact.py`: 45/45.
- `d1b_marked_support_restriction_exact.py`: 20/20.

The repairs change the headline. No-silent closure is an exact boundary
accounting/filtering rule. It does not generate the local seam, choose one
support, or supply a click rate.
