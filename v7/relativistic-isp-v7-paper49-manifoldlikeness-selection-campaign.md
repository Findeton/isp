# Relativistic ISP v7 - Paper XLIX

# Manifoldlikeness Selection From Record-History Defects

## 0. Purpose

Previous papers separated three facts:

1. order plus count can recover conformal and volume structure, but only once a
   manifoldlike causal set is available;
2. scalar/count laws are too weak to select manifoldlike orders;
3. finite atlas and continuum gates exist, but physical passage through those
   gates was not proven.

This paper attacks the remaining manifoldlikeness problem directly.

The target is not:

$$
\boxed{
\text{every admissible record history is manifoldlike.}
}
$$

That is false.

The target is:

$$
\boxed{
\text{the selected bounded-history law suppresses nonmanifold classes whenever
the bounded panel licenses a spacetime readout.}
}
$$

The campaign result is strong but scoped:

$$
\boxed{
\text{manifoldlikeness is proven as a record-conditioned selected-sector
property, not as an unconditional property of all possible histories.}
}
$$

## 1. Prior State

Paper XI gave the causal-set decomposition:

$$
\boxed{
\text{order}+\text{number}
\Rightarrow
\text{geometry up to scale}
}
$$

but only in the manifoldlike regime.

Paper XXII showed that:

$$
\boxed{
\text{scalar count laws and finite few-statistic tests are spoofable.}
}
$$

Paper XXXIX proved finite atlas existence and set-valued atlas stability when
the admissible nonlookup atlas class is nonempty.

Paper XLVIII proved:

$$
\boxed{
\sum_n\operatorname{ContDef}_n<\infty
\Rightarrow
\text{stable continuum readout}.
}
$$

What remained was the physical selection statement:

$$
\boxed{
\text{why should selected histories make }\operatorname{ContDef}_n\text{
summable?}
}
$$

## 2. Definitions

Let:

$$
\boxed{
\mathcal P_n=I_{GR}^{cl}(H_{B_n,k_n})
}
$$

be the selected finite spacetime packet at boundary size `B_n` and history
depth `k_n`.

Let:

$$
\boxed{
\mathcal CDef_n
=
\left(
D_n^{dim},
D_n^{dbl},
D_n^{atl},
D_n^{caus},
D_n^{sig},
D_n^{meas},
D_n^{curv},
D_n^{src},
D_n^{tail},
D_n^{proj}
\right)
}
$$

be Paper XLVIII's continuum defect vector.

Define the manifoldlikeness defect:

$$
\boxed{
\operatorname{MDef}_n
=
D_n^{dim}
+D_n^{dbl}
+D_n^{atl}
+D_n^{caus}
+D_n^{sig}
+D_n^{meas}
+D_n^{tail}
+D_n^{proj}.
}
$$

Curvature and source defects are omitted from `MDef` because a region can be
manifoldlike while having large matter or curvature.  They belong to Einstein
closure, not basic manifoldness.

## 3. Manifoldlike Tail

A selected packet sequence is manifoldlike on a scale window `\mathcal R` when:

$$
\boxed{
\sum_{n\ge n_0}\operatorname{MDef}_n<\infty.
}
$$

It is Lorentzian-manifoldlike when, in addition:

$$
\boxed{
\sum_{n\ge n_0}(D_n^{caus}+D_n^{sig})<\infty.
}
$$

It is smooth to order `q` when:

$$
\boxed{
\sum_{n\ge n_0}\operatorname{Reg}_n^{(q)}<\infty.
}
$$

Thus "manifoldlike" is not a single bit.  It is a tail statement about a
projective record packet sequence.

## 4. Immediate No-Go

### Theorem 1: Scalar Count Cannot Select Manifoldlikeness

Any law depending only on record count `N` cannot distinguish a manifoldlike
order from a nonmanifold order with the same `N`.

**Proof.**

Fix `N`.  There are manifoldlike sprinkling orders and nonmanifold KR-like,
chain, antichain, and layered orders with the same count.  A scalar count law
takes the same value on all of them.  It cannot select among them. `\square`

## 5. Few-Statistic No-Go

Let:

$$
\boxed{
\Xi_m(C_N)
=
(\xi_1(C_N),\ldots,\xi_m(C_N))
}
$$

be any finite list of order statistics such as Myrheim-Meyer dimension, height,
one interval-density moment, or finitely many Laplace samples of the interval
histogram.

### Theorem 2: Finite Few-Statistic Manifoldness Is Spoofable

For every fixed finite statistic list that does not separate the full
interval/atlas response type, there exist nonmanifold families matching the
listed statistics to tolerance while failing some unlisted manifold defect.

**Proof.**

Paper XXII gives explicit instances: KR families spoof Myrheim-Meyer dimension;
bilayer-plus-chain families spoof dimension and height while failing interval
density; thin-middle families spoof dimension, height, and one calibrated
interval moment; finite multi-alpha interval profiles remain underdetermined
as a moment problem.  Any finite list with a nontrivial kernel admits hidden
mass or hidden structure in that kernel unless the list is response-separating.
`\square`

## 6. Required Object: Full Response-Separating Profile

The finite manifoldness detector must be a profile:

$$
\boxed{
\mathfrak M_B(C)
=
\left(
\mathcal I_B,\mathcal H_B,\mathcal L_B,\mathcal A_B,
\mathcal T_B,\mathcal C_B,\mathcal U_B
\right)
}
$$

where:

- `\mathcal I_B` is the interval-size generating object, not finitely many
  moments;
- `\mathcal H_B` is height/layer growth across windows;
- `\mathcal L_B` is link/null skeleton stability;
- `\mathcal A_B` is atlas/overlap gluing;
- `\mathcal T_B` is transport/cocycle structure;
- `\mathcal C_B` is cone/signature profile;
- `\mathcal U_B` is unresolved boundary/source tail.

The profile is admissible only if it is subraw, record-covariant, and
nonlookup.

## 7. Manifold Work

Define the manifold work:

$$
\boxed{
\mathcal A_B^{man}(H)
=
\sum_{n\ge n_0}
\left[
\operatorname{MDef}_n(H)
+\operatorname{Spoof}_n(H)
+\operatorname{RawAtlas}_n(H)
+\operatorname{Tail}_n(H)
\right].
}
$$

This is not an extra physical force.  It is the part of the already calibrated
boundary-history action that charges manifoldness failure:

$$
\boxed{
\mathcal A_B^{hist}
=
\mathcal A_B^{base}
+\mathcal A_B^{man}
+\mathcal A_B^{src}
+\mathcal A_B^{QFT}
+\cdots.
}
$$

## 8. Physical Manifold Selection Theorem

### Theorem 3: Summable Manifold Work Gives Manifoldlike Readout

If a selected bounded-history tail satisfies:

$$
\boxed{
\mathcal A_B^{man}(H^\star)<\infty
}
$$

and the packet comparison maps are coherent up to same-actual nulls, then the
selected packet sequence is manifoldlike on the represented scale window.

**Proof.**

Finite manifold work includes the summable tail of `MDef`, raw-atlas
exclusion, spoof exclusion, and unresolved-tail control.  The summability of
`MDef` is exactly the manifoldlike tail condition.  Coherent comparison maps
make the tail meaningful across `n`. `\square`

## 9. Converse: Manifoldlike Readout Forces Small Manifold Work

### Theorem 4: Stable Manifoldlike Readout Has No Above-Tolerance Manifold Work

If a bounded packet sequence has a stable nonlookup manifoldlike readout and
no hidden source/tail channel above tolerance, then:

$$
\boxed{
\mathcal A_B^{man}(H)<\infty.
}
$$

**Proof.**

Stable manifoldlike readout gives summable dimension, doubling, atlas, causal,
signature, measure, tail, and projective defects.  Nonlookup excludes raw atlas
cost.  No-silent closure excludes unprinted tail work.  Hence the sum defining
`\mathcal A_B^{man}` is finite. `\square`

## 10. Selection Against KR-Like Orders

KR-like orders fail manifoldness in at least one of:

1. height/layer growth;
2. interval histogram profile;
3. link/null skeleton stability;
4. atlas overlap gluing;
5. cone/signature profile;
6. transport coherence.

### Theorem 5: KR Suppression Under Response-Separating Manifold Work

If `\mathfrak M_B` is response-separating on KR-like alternatives and
`\mathcal A_B^{hist}` penalizes above-tolerance `\mathfrak M_B` defects by
calibrated barriers, then selected histories cannot be KR-like in a bounded
panel that licenses manifoldlike readout.

**Proof.**

A KR-like alternative either matches all licensed response channels or fails
one.  If it matches all, it is same-actual for the bounded target and not a
distinct obstruction.  If it fails one, response separation exposes the defect,
and the calibrated barrier raises its action above the selected manifoldlike
carrier. `\square`

## 11. Selection Against Thin-Middle Spoofs

Thin-middle constructions spoof low-order statistics by hiding structure in
unseen interval layers.

The full profile defeats them only when:

$$
\boxed{
\mathcal I_B
\text{ contains enough interval generating data to expose hidden layer mass.}
}
$$

### Theorem 6: Full Interval Profile Blocks Moment Spoofs

If two finite orders agree on the full interval-size generating object
`\mathcal I_B` and on height/link/atlas channels at tolerance, then any
remaining thin-middle spoof is same-actual for the bounded manifold target.
If it disagrees, it pays manifold work.

**Proof.**

The thin-middle spoof mechanism uses the kernel left by finite moment samples.
The full interval generating object removes that kernel for the bounded
interval profile.  Remaining disagreements occur in height, link, atlas, or
transport channels and are charged separately. `\square`

## 12. Atlas Nonlookup Requirement

The finite atlas theorem from Paper XXXIX assumes a nonempty admissible atlas
class.  This paper turns that into a selector condition:

$$
\boxed{
\operatorname{RawAtlas}_n(H)=0
\quad\Longleftrightarrow\quad
\text{a subraw center-visible atlas exists.}
}
$$

If no subraw center-visible atlas exists, the packet is not manifoldlike at
that tolerance even if raw reconstruction could draw a manifold over it.

## 13. The Main Conditional Equivalence

### Theorem 7: Manifoldlikeness Selection Equivalence

For a completed no-silent bounded panel with selected history `H^\star`, the
following are equivalent up to tolerance:

1. `H^\star` has finite manifold work;
2. the selected finite packet tail has summable manifold defects;
3. the bounded panel licenses a nonlookup manifoldlike readout;
4. every nonmanifold competitor is either same-actual, below tolerance, or
   pays calibrated spoof/raw/tail work.

**Proof.**

`1 -> 2` is Theorem 3.  `2 -> 3` is Paper XLVIII's continuum Cauchy gate
restricted to manifold defects.  `3 -> 1` is Theorem 4.  Condition 4 is the
competition form of the same selector: any nonmanifold alternative must either
preserve all readouts, fail below tolerance, or trigger a charged defect.
`\square`

## 14. What This Proves

This proves:

$$
\boxed{
\text{manifoldlikeness is not an extra assumption once the selected bounded
history has finite manifold work.}
}
$$

It also proves:

$$
\boxed{
\text{scalar/count and finite few-statistic laws cannot be enough.}
}
$$

The selector must see a response-separating interval/atlas/cone/tail profile.

## 15. What This Does Not Prove

It does not prove:

$$
\boxed{
\text{all possible pre-geometric seeds become manifoldlike.}
}
$$

It does not prove:

$$
\boxed{
\text{the actual universe globally has no nonmanifold regions.}
}
$$

It proves a bounded operational statement:

$$
\boxed{
\text{where selected histories have finite manifold work, the continuum
readout is manifoldlike; where they do not, manifoldness is not licensed.}
}
$$

## 16. Relation To Newton's `G`

`G` is not used to prove manifoldlikeness.

The order is scale-free.  Count gives volume only up to `l_step`.  `G` can
calibrate that absolute scale after a manifoldlike sector exists.

Thus the correct order is:

$$
\boxed{
\text{record history}
\to
\text{manifoldlike packet}
\to
\text{scale anchors}
\to
G_B\text{ or }G_\infty.
}
$$

Using `G` to select the manifoldlike scale would smuggle in the continuum.

## 17. Local Failure And Critical Regions

Manifoldlikeness can fail locally without invalidating the record law.

If:

$$
\boxed{
\operatorname{MDef}_n>\epsilon_M
}
$$

in a bounded region, then that region is not licensed as smooth continuum
spacetime at the requested tolerance.  It may be:

1. pre-spacetime;
2. critical/topology-changing;
3. horizon/singularity-like;
4. source-boundary incomplete;
5. nonmanifold but record-law valid.

## 18. Hostile Review Round I

### Review 1: "The theorem assumes finite manifold work."

Accepted.  That is the exact physical selection burden.  The paper proves what
finite manifold work buys and why weaker scalar/few-statistic laws fail.

### Review 2: "This is just the continuum gate again."

Rejected.  Paper XLVIII gave the gate.  This paper isolates the selector part:
which action terms suppress KR/spoof/raw nonmanifold competitors.

### Review 3: "Full interval profiles may be raw."

Accepted unless the profile is compressed, subraw, and response-separating at
the target tolerance.  Raw full histograms are inadmissible.

### Review 4: "A nonmanifold code could reproduce all observations."

Then it is same-actual for that bounded panel.  The law cannot distinguish two
descriptions with identical licensed record predictions.

### Review 5: "The universe might contain nonmanifold regions."

Accepted.  The theorem is local/bounded and scale-windowed.

## 19. Opening A: Can Full Profile Be Subraw?

The remaining mathematical pressure point is:

$$
\boxed{
\text{prove }\mathfrak M_B\text{ is subraw for physical bounded panels.}
}
$$

A sufficient condition is a finite carrier decomposition:

$$
\boxed{
\mathfrak M_B
=
\mathfrak M_B^{interval}
\oplus
\mathfrak M_B^{atlas}
\oplus
\mathfrak M_B^{cone}
\oplus
\mathfrak M_B^{tail}
}
$$

with each carrier family growing subrawly and with only subrawly many admitted
types at tolerance.

### Theorem 8: Subraw Carrier Decomposition Gives Subraw Manifold Profile

If each component carrier is subraw and the number of admitted carrier types
is subraw, then `\mathfrak M_B` is subraw.

**Proof.**

A finite direct sum of subraw carriers indexed by a subraw type family remains
subraw. `\square`

## 20. Opening B: Can Selection Produce Summability?

Suppose the calibrated selector has a strict margin:

$$
\boxed{
\mathcal A_B^{hist}(H_{\rm nonman})
\ge
\mathcal A_B^{hist}(H_{\rm man})+\delta_n
}
$$

for every nonmanifold competitor at scale `n`.

If:

$$
\boxed{
\sum_n e^{-\delta_n}<\infty,
}
$$

then nonmanifold leakage is summable.

### Theorem 9: Barrier Margins Give Summable Nonmanifold Leakage

Under the displayed margin and quotient multiplicity bound `M_n`, if:

$$
\boxed{
\sum_n M_n e^{-\delta_n}<\infty,
}
$$

then the projected nonmanifold mass is summable along the tail.

**Proof.**

At scale `n`, nonmanifold mass is bounded by `M_n e^{-\delta_n}` relative to
the manifoldlike carrier.  Summing gives the claim. `\square`

## 21. Opening C: Does The Present Spacetime Panel Force It?

Paper XLVIII issue 8 proves that a spacetime-containing bounded panel projects
backward to onset-compatible seeds.

It does not by itself prove manifoldness for all larger panels.

But it does imply:

$$
\boxed{
\text{given a present panel whose continuum gates pass, compatible histories
charge manifoldlike onset branches.}
}
$$

Thus present spacetime records supply conditional support, not unconditional
cosmological inevitability.

## 22. Final Theorem

### Theorem 10: Manifoldlikeness Selection Closure

In the current v7 framework, manifoldlikeness is closed in the following
finite operational sense:

1. scalar/count-only laws cannot select it;
2. finite few-statistic laws are spoofable;
3. a response-separating, subraw manifold profile is necessary;
4. finite manifold work is equivalent to summable manifold defects;
5. summable manifold defects license manifoldlike continuum readout;
6. nonmanifold competitors are rejected only when they differ in a licensed
   profile channel above tolerance;
7. `G` calibrates scale after manifoldlikeness and does not prove it.

**Proof.**

Items 1 and 2 are Theorems 1 and 2.  Item 3 is the no-go consequence of those
theorems.  Items 4 and 5 are Theorem 7 and Paper XLVIII's continuum gate.  Item
6 is Theorems 5 and 6.  Item 7 is the scale-ordering argument of Section 16.
`\square`

## 23. Campaign Result

The manifoldlikeness problem is not "forgotten" anymore.

It has been converted into one exact physical theorem target:

$$
\boxed{
\text{prove selected physical bounded panels have subraw response-separating
manifold profiles with summable manifold work.}
}
$$

If this holds, manifoldlikeness is selected.

If it fails, the record law still exists, but smooth spacetime is only a
special phase and not a universal output.

## 24. References

- Paper XI: order plus number, `l_step`, and manifoldlikeness gate.
- Paper XXII: finite-order manifoldlikeness stress tests.
- Paper XXXIX: finite atlas and packet campaign.
- Paper XLVIII: finite continuum convergence gate and eight-issue closure.
- Bombelli, Lee, Meyer, Sorkin, "Space-time as a causal set", Phys. Rev. Lett.
  59, 521 (1987).
- Malament, "The class of continuous timelike curves determines the topology
  of spacetime", J. Math. Phys. 18, 1399 (1977).
- Kleitman and Rothschild, "Asymptotic enumeration of partial orders on a
  finite set", Trans. Amer. Math. Soc. 205, 205 (1975).
