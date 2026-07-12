# D1 hostile review round 3 — final exact-mathematics audit

**Referee:** independent exact-mathematics hostile review

**Date:** 2026-07-11

**Verdict:** **PASS WITH MINOR CORRECTIONS**. No major mathematical opening
remains in the scoped finite results. The repaired complete-screen,
provenance, direct-carrier, parity/synergy, and typed-restriction claims all
survive exact reconstruction. Two identity/scope wording corrections remain;
neither changes an executed theorem.

## 1. Frozen artifacts and reproduction

Source hashes reviewed:

```text
51b3a6460ccf3ddcac7efc0448c770cfa76187a7560ce7bcbb63adf3fb735947  v10/code/d1_no_silent_center_exact.py
d0944fbf99ac0b9e7f5d94c90feb1d8ae88be21a47bd52bb9461edee4dd978eb  v10/code/d1b_marked_support_restriction_exact.py
f0dad6ce77932cd1bf60980009e999dc455153c84733876a716f7aebecd6fa61  v10/note-d1-no-silent-support-birth.md
67619bb7fe3d49b07260cf887f483ab5a1244963b9acb31e68846b274b0851cb  v10/relativistic-isp-v10-paper2-no-silent-centers-do-not-select-support-birth.md
```

Commands:

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
- D1B exited `0` with `RECEIPT: 28/28 exact checks passed`.
- Two independent D1A output runs had SHA-256
  `e89d84ff77c910d49e0303df12a4bea7c3fc20612699ae5052d6ee1569a28b1a`.
- Two independent D1B output runs had SHA-256
  `e589cfb7b5690a246cb8cf3adba68f374c9c2ce61525e7f9448fbb82ce22e799`.

D1A's probability tables and mathematics are unchanged from the independently
reconstructed round-2 version; its legacy S4 diagnostic was correctly renamed
from a “genuine crossing” to a common-root three-variable cell. Its full
partition census, exact refinement direction, robust S5 witness, and
high-precision CMI reports retain the prior PASS.

## 2. Complete-screen refusal

The round-2 false-positive path is repaired in `support_is_eligible`.
Eligibility now requires, for every cut:

1. the visible screen itself fails exact conditional independence;
2. exactly one nonlookup minimal completion survives;
3. that completion differs from the screen;
4. at least one non-screen marked generator is used.

The new controls are load-bearing.

- A connected, structurally licensed but factorized `AB` history remains a
  candidate and is refused because the constant screen is complete.
- Retyping the common-root `H` field as a visible screen preserves all four
  structural candidates but makes every one ineligible.

I reran the earlier hostile construction. Its exact result is now

```text
candidate supports = (AB, AC, BC, ABC)
eligible supports  = ()
```

This fully closes the required round-2 opening.

## 3. Provenance-preserving center census

The marked census no longer maps one partition to one lexically preferred
field tuple. It records all generator selections, first minimizes the induced
partitions, and then removes only generator selections containing a strict
redundant subset on the same partition.

For `H@root:H` and `Hcopy@root:H-copy`, which induce the same atom partition,
the exact status contains two one-generator marked centers. The pair is
therefore refused as nonunique. The robust fields `R@AB:R` and `C@AB:C` still
produce the two distinct incomparable S5 partitions.

This proves the paper's stated marked rule: provenance-distinct generators
are not silently quotiented. It does not prove that provenance must be
physical in a future ontology; the paper correctly says an explicit record
gauge could later identify them.

## 4. Direct-carrier locality

Candidate supports are no longer generated from an entire transitive graph
component. The primitive carrier family consists of:

- a sibling set sharing one recorded parent;
- an existing support hyperedge;
- a marked ancestor or joint-boundary carrier.

Candidate supports are subsets of one such direct carrier and require exposed
output ports. In the exact `AB`--`BC` overlap control, the connectivity graph
has one component `{A,B,C}`, but the candidate family is exactly `{AB,BC}`.
Neither `AC` nor `ABC` is generated. Removing `C`'s output port from the
common-root history likewise removes every `C`-bearing candidate.

The locality result is conditional on this supplied carrier axiom. The paper
does not misattribute the carrier rule to conditional independence and does
not claim a law for creating a new carrier.

## 5. Independent parity/synergy reconstruction

I rebuilt the parity cell independently in Ruby from its integer weight
vectors, without importing D1B.

Let `U,V` be uniform latent bits, duplicate every `(U,V)` state with a nuisance
bit, and let

$$
A\leftarrow U,\qquad R\leftarrow U\oplus V,\qquad Z\leftarrow V
$$

through the positive channels `(3,1)/(1,3)`, `(4,1)/(1,4)`, and
`(5,1)/(1,5)`. Every one of the eight boundary atoms has mass `120`; total
mass is `960`.

The independently aggregated pair tables are all

$$
\begin{pmatrix}240&240\\240&240\end{pmatrix},
$$

so `A|R`, `A|Z`, and `R|Z` are exactly independent at the constant screen.
For each of `AR|Z`, `AZ|R`, and `RZ|A`, the constant-screen table is

$$
\begin{pmatrix}
144&96\\
96&144\\
96&144\\
144&96
\end{pmatrix}.
$$

Its first `2x2` minor is `11520`, so every triple bipartition is exactly
dependent. Conditioning on each of the four `H=(U,V)` cells makes every cut
rank one. The four-cell center is nonlookup because the nuisance duplication
leaves eight occupied boundary atoms.

Therefore the exact marked eligibility family is

$$
\operatorname{Eligible}(ARZ)=\{ARZ\},
$$

while every pair restriction has empty eligibility. In particular,

$$
\operatorname{project}_{AZ}\{ARZ\}=\{AZ\}
\ne
\operatorname{Eligible}(AZ)=\varnothing.
$$

This is a genuine restriction of one marked history, not target
marginalization or a screen change.

## 6. Data functoriality versus eligibility non-naturality

The paper now makes the necessary distinction correctly.

The underlying marked data restriction is path-independent: lineage and port
filtering, carrier intersection, the idempotent projection flag, support
intersection, parent-entry filtering, and marginalization of the count law
compose on nested retained sets. D1B executes every nested nonempty subset path
in both the common-root and parity families.

The derived eligibility operation is nonlinear. It first tests screen
incompleteness and then minimizes exact center completions cut by cut.
Marginalization can erase a purely synergistic dependence, so this derived
family need not commute with support projection. The parity witness proves
that failure exactly.

Accordingly, the following statements pass together:

- marked history data restrict path-independently in the two executed finite
  families;
- the eligible-support family is not a natural transformation for the stated
  support-intersection projection;
- universal/projective support birth is refused, not repaired.

## 7. Minor findings

### [Minor 1] Clarify whether marked identity is provenance or `(name, provenance)`

The delimiter-collision repair is correct: generator identities are now typed
`(name, provenance)` pairs rather than concatenated strings, and the exact
`("A@B","C")` versus `("A","B@C")` adversary remains distinct. The D1B
docstring, however, says generator identity is stable provenance, while the
implemented identity contains both name and provenance. Adding a second alias
with the same provenance and induced partition but a different `name` still
produces two marked centers:

```text
Alias@root:H
H@root:H
```

If provenance alone is the stable physical identity, this is artificial
nonuniqueness under a display-label change. If `(name, provenance)` is the
intended physical identity, the implementation is correct and only the
docstring needs clarification. The executed M8 witness uses two distinct typed
identities and is unaffected.

### [Minor 2] The note's unmarked and marked equivalence rules need separate scope

Section 4 of the note says two D1 centers are physically the same exactly when
they induce the same boundary partition. O4/G9 later says
provenance-distinct marked fields inducing that same partition must remain
distinct. These are consistent only when the first statement is labeled the
unmarked D1A equivalence and the second the marked D1B equivalence. The paper
already makes this distinction; the note should do so explicitly.

### [Minor 3] Opening count typo

The O4 introduction says hostile round 2 found “four” load-bearing failures,
but the immediately following list has five numbered requirements. Replace
“four” with “five.”

## 8. Theorems and wording that pass

- Theorem 4.1 is an exact finite positive center-nonselection theorem with the
  stated strict-positivity and tied elementary-complexity conditions.
- Theorem 7.1 is correctly limited to cutwise nonselection inside one supplied
  candidate family; it claims no equivalence of pair-event and hyperedge
  generative histories.
- Theorem 9.1 correctly separates path-independent marked histories from a
  non-natural eligible-support family.
- Complete screens, factorized candidates, lookup-only closure, and absent
  boundary closure are distinct refusal modes.
- Direct-carrier locality is identified as an additional seam axiom, not a
  consequence of the statistical law.
- The receipt counts `45/45` and `28/28` match execution.
- All CMI values remain reports; integer minors are the equality authority.
- No continuum, profinite, quantum, geometric, firing-rate, transfer, root
  creation, or final interacting-law claim is made.

## 9. Final verdict and claim ceiling

**Final mathematical grade: PASS WITH MINOR CORRECTIONS.** The minor findings
above concern marked identity wording and one count typo. They do not alter
the finite witnesses or any theorem stated in Paper 2.

Accepted claim ceiling:

1. exact finite center identification/refusal inside already supplied cuts;
2. finite center nonuniqueness despite strict positivity and tied elementary
   complexity;
3. support over-eligibility inside one supplied common-root candidate family;
4. locality only relative to a supplied direct-carrier/output-port axiom;
5. path-independent marked-history restriction on the two executed finite
   subset lattices;
6. exact failure of eligible-family naturality on the parity/synergy history.

Not accepted:

- derivation of candidate carriers or newly joining components;
- a unique center across arbitrary marked histories;
- a projective support-birth rule;
- a firing probability, outcome law, transfer kernel, or initial-root law;
- a profinite, continuum, spacetime, or quantum extension.

## 10. Final correction addendum

The authors repaired all three minor findings after the round-3 report. I
verified the corrections in the final artifacts.

1. D1B now explicitly defines marked generator identity as the typed pair
   `(field name, stable provenance)`. The implementation uses exactly that
   pair, so name sensitivity is a frozen ontology choice rather than an
   accidental display-label dependence. A later quotient would require an
   explicit record-gauge law.
2. The note now scopes same-partition gauge equivalence to the unmarked D1A
   census and separately states D1B's typed marked identity.
3. O4 now correctly says round 2 found five load-bearing failures, matching its
   five-item list.

Final source hashes:

```text
51b3a6460ccf3ddcac7efc0448c770cfa76187a7560ce7bcbb63adf3fb735947  v10/code/d1_no_silent_center_exact.py
276e7919d88878ae9447dbb9a6619f4914b906d4816c8addc8f71b41c3883703  v10/code/d1b_marked_support_restriction_exact.py
523c84ae2c431cc8a7a533732f85e77c804a670fcd8e4fd50675375a39780962  v10/note-d1-no-silent-support-birth.md
2270c7b0115260b8c296687644271a89b44aa23bec0d66bb8540d8928696bf23  v10/relativistic-isp-v10-paper2-no-silent-centers-do-not-select-support-birth.md
```

Final executions remain `45/45` and `28/28`. Their deterministic output
SHA-256 values are respectively
`e89d84ff77c910d49e0303df12a4bea7c3fc20612699ae5052d6ee1569a28b1a`
and
`e589cfb7b5690a246cb8cf3adba68f374c9c2ce61525e7f9448fbb82ce22e799`.

**Final verdict after correction: PASS at the claim ceiling in Section 9.**
There are no outstanding mathematical corrections from this referee.
