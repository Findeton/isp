# D1 hostile review, round 3: independent rebuild and final adversary audit

**Referee:** independent hostile reconstruction

**Date:** 2026-07-11

**Verdict:** **PASS at the stated finite scope**

The round-2 blockers have been repaired and promoted into exact gates. I
independently rebuilt the center arithmetic, one-joint-law cut census,
direct-carrier generator, complete-screen refusals, stronger S5 witness, and
parity/synergy adversary. Both production receipts are deterministic and pass.

I found one additional provenance-serialization adversary during round 3. It
was repaired before this frozen review by replacing delimiter-concatenated
strings with typed `(name, provenance)` identities and adding the adversary to
the receipt. No remaining exact counterexample invalidates the paper's scoped
claims.

This is not approval of a record-birth law. It is approval of the paper's
negative boundary: no-silent completion is an exact finite diagnostic/filter
on supplied candidate supports, not the missing law that generates those
supports.

## 1. Frozen artifacts and hashes

```text
523c84ae2c431cc8a7a533732f85e77c804a670fcd8e4fd50675375a39780962  v10/note-d1-no-silent-support-birth.md
2270c7b0115260b8c296687644271a89b44aa23bec0d66bb8540d8928696bf23  v10/relativistic-isp-v10-paper2-no-silent-centers-do-not-select-support-birth.md
51b3a6460ccf3ddcac7efc0448c770cfa76187a7560ce7bcbb63adf3fb735947  v10/code/d1_no_silent_center_exact.py
276e7919d88878ae9447dbb9a6619f4914b906d4816c8addc8f71b41c3883703  v10/code/d1b_marked_support_restriction_exact.py
```

The production commands were:

```bash
PYTHONDONTWRITEBYTECODE=1 \
  /opt/miniconda3/envs/tbp.monty/bin/python \
  v10/code/d1_no_silent_center_exact.py

PYTHONDONTWRITEBYTECODE=1 \
  python3 v10/code/d1b_marked_support_restriction_exact.py
```

Each command was run twice. All four executions exited zero. The two runs of
each receipt were byte-identical:

```text
e89d84ff77c910d49e0303df12a4bea7c3fc20612699ae5052d6ee1569a28b1a  D1A output, both runs
e589cfb7b5690a246cb8cf3adba68f374c9c2ce61525e7f9448fbb82ce22e799  D1B output, both runs
```

D1A reports **45/45** checks. D1B reports **28/28** checks.

## 2. Independent implementation

I used a separate Ruby reconstruction which imports no production code. Its
round-3 SHA-256 was
`c9894b7896769ac791aebf13f63eec5ba3610365c1c0c481069ca8bbef490583`.
It independently implements:

1. canonical finite partition enumeration;
2. exact integer rank-one tests via all minors;
3. refinement order and coarsest-complete selection;
4. marginalization from one joint `ABC` law;
5. all pair and triple cut tables;
6. direct structural-carrier support generation;
7. output-port intervention;
8. direct versus successive restriction;
9. the robust S5 census; and
10. the `ARZ` parity/synergy construction.

The relevant independent output was:

```text
CUT A|B   screen incomplete; H complete; unique minimum H
CUT A|C   screen incomplete; H complete; unique minimum H
CUT B|C   screen incomplete; H complete; unique minimum H
CUT AB|C  screen incomplete; H complete; unique minimum H
CUT AC|B  screen incomplete; H complete; unique minimum H
CUT BC|A  screen incomplete; H complete; unique minimum H

direct ABC->A law = successive ABC->AB->A law
full-port candidates = AB, AC, BC, ABC
after removing C output port = AB

overlapping direct carriers AB and BC produce only AB and BC
connected factorized constant screen is exactly complete

PARITY A|R   screen complete; H complete
PARITY A|Z   screen complete; H complete
PARITY R|Z   screen complete; H complete
PARITY AR|Z  screen incomplete; H complete
PARITY AZ|R  screen incomplete; H complete
PARITY RZ|A  screen incomplete; H complete
```

These results independently reproduce the intended ontology distinctions. In
particular, the parity theorem is not an artifact of calling six separately
fitted tables: every cut is obtained from one positive integer joint law.

## 3. Complete-screen and factorized refusals — pass

The repaired `support_is_eligible` now requires, on every relevant cut:

1. an incomplete visible screen;
2. exactly one minimal finite-nonlookup completion;
3. a completion strictly finer than the screen; and
4. a nonempty marked generator selection.

This closes the round-2 false positive.

### Connected factorized control

The marked control has `A,B` as direct siblings with output ports, so `AB` is
a legitimate supplied candidate. Its positive count table is constant and
factorized on every boundary atom. Exact aggregation gives a rank-one constant
screen. The candidate remains structurally present but the eligible family is
empty.

### Visible complete-screen control

In the common-root law, relabeling `H` as a visible screen makes every pair and
triple cut conditionally rank one in each `H` cell. The direct structural
candidate family remains `AB,AC,BC,ABC`, while the eligible family becomes
empty. Thus the refusal is caused by screen completeness rather than removal
of the candidates.

Both controls implement the campaign's required distinction between
“candidate seam exists” and “no missing center is needed.”

## 4. Direct-carrier locality — pass at its explicit scope

The candidate generator no longer takes every subset of a transitive graph
component. It first constructs primitive structural hyperedges from:

- one direct sibling group with a common recorded parent;
- one existing support; or
- one marked ancestor/joint-boundary carrier.

It generates output-port-bearing subsets inside each such direct carrier. It
does not close overlapping carriers transitively.

The exact `AB-BC` chain has one connected graph component but candidate family

```text
AB, BC
```

with neither `AC` nor `ABC`. Independent reconstruction agrees.

This establishes locality only relative to the supplied carrier ontology. A
single parent or joint field may itself have an arbitrarily large carrier, and
the receipt does not derive a metric radius, bounded-degree rule, or physical
diamond adjacency. The paper now keeps that stronger question open.

## 5. Provenance identity — pass after live round-3 repair

Round 2 correctly required distinct marked realizations of one induced
partition to remain distinct. The first repair encoded identity by the string

```text
name@provenance
```

which admits delimiter collisions. For example,

```text
(name="A@B", provenance="C")
(name="A",   provenance="B@C")
```

are different typed identities but serialize to the same string.

The frozen receipt uses typed pairs `(name, provenance)` throughout generator
sets and irredundancy comparisons. Its adversarial duplicate fields induce one
atom partition but remain the two selections

```text
(("A@B", "C"),)
(("A", "B@C"),)
```

Consequently the center is ambiguous and `AB` is not called uniquely
eligible. The implementation now matches the stated ontology.

## 6. Stronger S5 — independently passes again

For

$$
M_0=\begin{pmatrix}16&4\\4&1\end{pmatrix},\quad
M_1=\begin{pmatrix}3&2\\12&8\end{pmatrix},
$$

$$
M_2=\begin{pmatrix}1&4\\4&16\end{pmatrix},\quad
M_3=\begin{pmatrix}2&8\\3&12\end{pmatrix},
$$

every entry is positive, every atomic determinant is zero, and every atom has
mass 25. The total has determinant 400. Exhaustion of all 15 partitions gives
exactly three complete partitions: the two incomparable minima

$$
\{\{0\},\{1,2\},\{3\}\},
\qquad
\{\{0\},\{1\},\{2,3\}\},
$$

and atomic lookup. Both minima have cell-mass multiset `(25,25,50)` and remain
complete under every refinement. The center-nonuniqueness theorem is therefore
not a structural-zero, entropy, cardinality, or Simpson-refinement artifact.

## 7. Exact parity/synergy projectivity counterexample — pass

Let `H=(u,v)` with four states, duplicated by nuisance `N`. Conditional on
`H`, define positive product weights so that

$$
A\leftarrow u,
\qquad
Z\leftarrow v,
\qquad
R\leftarrow u\oplus v.
$$

Exact independent aggregation verifies:

- `A,R`, `A,Z`, and `R,Z` are each independent at the constant screen;
- every bipartition of `ARZ` is dependent at that screen;
- the four-state `H` field closes every triple cut;
- duplicated nuisance makes `H` finite nonlookup.

Thus the full eligible family is `{ARZ}`, whereas every pair restriction has
an empty eligible family. Under the implemented intersection projection,

$$
\operatorname{project}_{AZ}\{ARZ\}=\{AZ\}
\ne
\operatorname{Eligible}(H|_{AZ})=\varnothing.
$$

The marked history object itself remains path-independent on every nested
nonempty subset path. The failure belongs to the nonlinear eligible-support
operation, not the data restriction functor.

The paper now scopes this theorem to the implemented intersection support
projection. It does not claim that every conceivable lax, relational, or
provenance-carrying projection must fail.

## 8. Search for another exact counterexample

I attacked the frozen claims with:

1. a connected but exactly factorized candidate;
2. a visible complete screen with unchanged structural candidates;
3. statistically dependent disconnected lineages;
4. an overlapping `AB-BC` carrier chain;
5. removal of one output port;
6. identical partitions with distinct provenance;
7. delimiter-adversarial provenance strings;
8. direct and successive restrictions over the full tested subset lattices;
9. robust tied competing centers; and
10. pairwise-independent but jointly dependent parity/synergy.

All are now either passed as positive controls or promoted as exact refusal
theorems. I found no remaining exact counterexample to the claims as currently
scoped.

There remain many counterexamples to stronger statements, but the paper does
not make those statements. In particular, D1 does not derive primitive
carriers, does not select a universal center, does not select one support, and
does not provide a natural eligible family under its implemented projection.

## 9. Remaining openings, not review defects

1. **Carrier origin:** parents, existing supports, and joint fields are input
   data. The rule for creating a genuinely new direct carrier remains absent.
2. **Physical locality:** direct-carrier locality is combinatorial. No bounded
   causal neighborhood, diamond pushout, or emergent-distance theorem is
   supplied.
3. **Projection repair:** the exact parity theorem blocks the implemented
   intersection projection. A lax/set-valued alternative has not been derived.
4. **Center selection:** S5 leaves a genuine antichain of marked centers.
5. **Support selection:** the common-root law leaves all pair and triple
   candidates eligible.
6. **Dynamics:** no firing intensity, outcome kernel, transfer law, or shared
   evidence allocation is derived.
7. **Global mathematics:** there is no marked profinite, nonexplosion,
   continuum, geometry, or initial-record theorem.

These openings are accurately presented as future work.

## 10. Final claim ceiling

The evidence supports exactly the following:

> For supplied finite rational boundary laws and supplied marked candidate
> carriers, no-silent completion is an exact conditional-independence census.
> It may identify one finite-nonlookup marked center, several incomparable
> centers, lookup only, or no boundary center. It does not select one support
> from a supplied family. Marked history data restrict path-independently in
> the two executed finite families, while the derived eligible-support family
> fails naturality on an exact parity/synergy history under intersection
> support projection.

It does **not** support:

- a final interacting record law;
- spontaneous record or support birth;
- joining of previously unlicensed components;
- intrinsic physical locality;
- universal projectivity;
- a positive click rate or outcome/transfer kernel;
- a marked profinite extension; or
- spacetime dimension, scale, or cone claims.

At that ceiling the round-3 verdict is **PASS**.
