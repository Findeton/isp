# Paper 14 stable-happenings and premetric-order hostile adjudication

Date: 2026-08-20

Status: **TERMINAL ADJUDICATION / FULL CEILING REJECTED / STRUCTURAL SUBSTRATE SURVIVES**

## 1. Terminal head

```text
P14-POINT-FREE-HISTORY-LAW-FAILS;
P14-GRAMMAR-STABLE-RECORD-THEOREM-SURVIVES;
P14-COMPLETE-FRONTIERS-AND-NATIVE-NONDIVISION-SURVIVE;
P14-LOCALLY-FINITE-BUNDLE-POSET-PLUS-UNIT-MEASURE-SURVIVES;
P14-INTRINSIC-GAMMA-ATOMIC-WEIGHT-FAILS;
P14-PREMETRIC-ORDER-AND-INTERVAL-MEASURE-NOT-EARNED
```

The official `ELIGIBLE-GREEN-UNREVIEWED` ceiling is rejected. Two blind seats
found independent exact mathematical defects; both are reproduced below. A
third seat found no scientific counterexample and supplied useful bounded
wording observations, but its acceptance does not survive the cross-seat
countermodels.

This is terminal for the frozen Paper 14 candidate. No source or paper repair
is authorized or required. Paper 13 remains closed.

## 2. Frozen authority

The adjudication binds:

| object | path / commit | SHA-256 |
|---|---|---|
| pin commit | `9687d59c2faa29efd53993643deb92b3f5c5a025` | — |
| source commit | `dda7a01e80a17883a039bd0e33a3453b0601af3f` | — |
| official-result commit | `44c23725559dda2d00f6dc482088d8a97e5b6964` | — |
| hostile protocol commit | `ed258111d2ff604de97816266be2184fd1d06c63` | — |
| referent report commit | `735bf74` | — |
| probability report commit | `f074d12` | — |
| order/measure report commit | `23e4735` | — |
| referent report | `v16/review-paper14-premetric-referent.md` | `b8d7e244425dbb044f5e71b5929a3a27d3d3d525d4cab8a399a944fa5c4724ac` |
| probability report | `v16/review-paper14-premetric-probability.md` | `29fe49d6bc9db3094e87a99e87f5d2a55e6e4972af54e484d10cf6127df2f9e4` |
| order/measure report | `v16/review-paper14-premetric-order-measure.md` | `c7e851badb6f89d77be043ceb4c4f288f5f8fa392aa2696728a124ed96739c41` |

All three reports were frozen mutually blind and committed separately before
adjudication. Their normalized self-hashes are respectively
`af8dac38a543c4362c01f93b4771aa576d90a95a5282b1bbe8754304410cc5c1`,
`ebdf6a2883ed4535b485b9643041610ca8101e8deff47ac6fe298c12db3a5188`,
and `d34a8287a935fa402e4919b88bc68c031682175316ea5dcc9894024aa89d0971`.

The adjudicator read all reports and reconstructed both decisive objects in a
separate exact script:

```text
/private/tmp/p14_hostile_adjudication_reconstruction.py
SHA-256 10fb658f3ebebfad4093bb4f16728b9938075c1e2bfea17fa667f161fac559c5

/private/tmp/p14_hostile_adjudication_reconstruction.json
SHA-256 35617655da8d342c4d9db3a91703445f138e8581c856d11b3e526ed5cd3fa286
```

## 3. Adjudication of H4: sector swap, not erasure

Seat P is correct and Seats R/O are overruled on H4.

The submitted changed operation is

$$
E=X\otimes I_2.
$$

The implementation tests only the same-coordinate equations
$P_rE=EP_r$. Those fail because $E$ exchanges the two record sectors. But the
paper's actual typed condition permits transported output projectors:

$$
P_r^{\rm out}F=FP_r^{\rm in}.
$$

Set

$$
Q_r=EP_rE^\dagger.
$$

Then

$$
Q_0=P_1,qquad Q_1=P_0,qquad Q_rE=EP_r,qquad E^\dagger E=I_4.
$$

For the writer branches,

$$
(EV_0)^\dagger(EV_1)=V_0^\dagger V_1=0.
$$

Thus the record remains perfectly distinguishable and readable after a
known relabeling of its sectors. This is a required transport non-kill, not an
eraser or reconvergence. The published H4 disposition, the check
`ERASER-OUTSIDE-GRAMMAR`, and `all_registered_attacks_killed=true` are false.

This failure does **not** refute the positive sealed-word theorem. Every one
of the six licensed generators still shares the correct projector family, so
induction proves perfect record persistence for every finite word. What fails
is the submitted negative discriminator and therefore the global promotion
that required all 26 attacks.

A genuine eraser would have to destroy the semantic record algebra—for
example by a noninjective merge or an exact coherent unwrite into a carrier
where no transported record event remains. The frozen candidate does not
construct such an object.

## 4. Adjudication of O6: the law does not descend to its quotient

Seat O is correct and Seat R is overruled on the point-free law and intrinsic
weight coordinates.

The paper declares complete physical histories to be isomorphism classes of
their incidence-and-value structures and explicitly permits exchange of the
two incomparable root bundles $A$ and $B$. On one reciprocal cell this acts
as

$$
\tau(a,b,g,y)=(b,a,g,y).
$$

The labeled law is

$$
\Gamma(a,b,g,y)=\frac14 B_{g\mid a\oplus b}B_{y\mid g}.
$$

It has 16 positive labeled rows and is invariant under $\tau$. But its
whole-history quotient has only

$$
8+\frac82=12
$$

classes: eight fixed histories with $a=b$ and four two-element orbits with
$a\ne b$.

There is no interpretation that is simultaneously the printed law, normalized
on physical history classes, and factorized by the advertised intrinsic atom
weights:

1. Assigning each class its representative's printed probability gives total
   mass $3/4$.
2. Pushing labeled probability forward gives total mass one, but doubles each
   off-diagonal orbit. In particular,

   $$
   \Gamma(0,1,0,0)=\frac{36}{625}
   \quad\longmapsto\quad
   \Gamma([0,1,0,0])=\frac{72}{625}.
   $$

Already at the root pair the physical unordered masses are

$$
\frac14,\quad\frac12,\quad\frac14.
$$

The equal-pair rows force putative independent root factors
$q(0)=q(1)=1/2$, whose mixed product is $1/4$, not $1/2$. The missing
$\log2$ term is orbit multiplicity attached to the whole history, not an
intrinsic weight of either root occurrence.

Therefore:

- `P14-DECLARED-POINT-FREE-HISTORY-LAW` is not earned;
- the printed `16^n` is a labeled-presentation history count, not the physical
  quotient count (`12` already at one reciprocal cell);
- strong diamonds in a chosen labeled representative do not establish
  intrinsic atomic-weight descent through the groupoid; and
- the point-free intrinsic `Gamma` valuation and the proposed full premetric
  ceiling fail.

This is not node-orbit counting. The quotient history still contains both
root occurrence nodes and unit occurrence measure remains two. What changes
is the probability assigned to the complete unlabeled decorated history.

## 5. Exact surviving mathematics

The rejected global outcome does not erase independent lower results.

### 5.1 Stable-record theorem

The exact writer identities survive:

$$
\sum_rV_r^\dagger V_r=I,
\qquad
P_rV_s=\delta_{rs}V_s.
$$

All six sealed generators preserve the record projectors. Therefore every
finite licensed word preserves the two record sectors and their orthogonality.
This is a grammar-stable record theorem on the declared presentation-bound
carrier. It is not an actualization theorem and, after O6, is not a complete
point-free probabilistic happening construction.

### 5.2 Division and nondivision

The recorded two-step law is

$$
B^2=\frac1{625}
\begin{pmatrix}337&288\\288&337\end{pmatrix},
$$

and direct versus cut evaluation agrees for every input/output row. The full
root-pair and root-pair-plus-$g$ frontiers remain sufficient for the declared
future grammar. The marked one-root projection remains insufficient because
the omitted other root changes the $g=1$ profile from $16/25$ to $9/25$.

For the unrecorded coherent law,

$$
C=|R^2|^2=\frac1{625}
\begin{pmatrix}49&576\\576&49\end{pmatrix}.
$$

The unique native restart candidate is

$$
CB^{-1}=\frac1{175}
\begin{pmatrix}351&-176\\-176&351\end{pmatrix},
$$

not $B^{-1}=\frac17\begin{pmatrix}-9&16\\16&-9\end{pmatrix}$.
It has negative entries, so no positive source-independent restart exists on
the declared two-state carrier. This says nothing about configuration
unreality or enlarged-history Markovizations.

### 5.3 Dependency order and unit measure

The structural incidence construction survives independently of the failed
probability descent:

```text
bundles: ({a,b},{c},{d})
order:   {a,b} < {d}, {c} < {d}, {a,b} || {c}
states:  5
words:   7
traces:  5
```

Mutual-dependence quotienting removes false orientations while preserving
occurrence multiplicity. In the uniform recursive structural family,
dependency depth strictly increases and finite branching bounds every closed
interval. Therefore

```text
P14-LOCALLY-FINITE-BUNDLE-POSET
```

survives as a theorem of the declared structural family.

Unit measure counts bundle occurrences, not labels, raw record components,
history rows, or automorphism orbits. It remains additive on disjoint bundle
regions and interval finite. Therefore

```text
P14-UNIT-COUNTING-MEASURE
```

also survives. The stronger `P14-INTRINSIC-GAMMA-ATOMIC-WEIGHT` and
`P14-INTERVAL-FINITE-ATOMIC-MEASURE` do not.

### 5.4 Reciprocal response

The exact conditional residuals $7/25$, $7/25$, and $49/625$ remain valid in
the presentation-bound declared law. They show matter--relation--matter
sensitivity in that model. They do not change the underlying Hasse order and
are not geometry or gravity.

## 6. Terminal product coordinates

```text
law:
  P14-LAW-REFERENT-UNBOUND

record:
  P14-ONSET-GERMS-PRESENTATION-ONLY
  plus an exact grammar-stable record theorem on the declared carrier

actuality:
  POSTULATED-NOT-DERIVED

dependency:
  P14-LOCALLY-FINITE-BUNDLE-POSET
  (structural-family scope; not yet chronological order)

frontiers:
  full root pair       P14-COMPLETE-DIVISION-FRONTIER
  full root pair + g   P14-COMPLETE-DIVISION-FRONTIER
  marked one-root cut  P14-FRONTIER-INCOMPLETE
  (all declared presentation-bound-law scope)

valuation:
  P14-UNIT-COUNTING-MEASURE
  intrinsic Gamma atomic weight FAILS

geometry:
  P14-NO-METRIC
  proposed P14-PREMETRIC-ORDER-AND-INTERVAL-MEASURE NOT EARNED as a physical
  law-relative product
```

The surviving bundle order plus unit measure is a genuine premetric
**structural substrate**, but not yet a network of point-free actual stable
happenings governed by a normalized point-free law. This distinction is
load-bearing for every successor.

## 7. Report-quality findings

Seat R's three terminology/certificate clarifications are sensible but no
repair is ordered because the candidate is terminally adjudicated at lower
coordinates.

Seat P also identifies a receipt shortfall: the official receipt seals only
four parity/output cut rows rather than the complete all-input frontier
objects, and omits the native nondivision object. The mathematical frontier
and nondivision claims were nevertheless independently reconstructed by all
seats. This remains a promotive-evidence deficiency, not a reason to erase the
surviving mathematics.

Seat O transcribed the verification-note hash incorrectly in its
authentication table. The correct committed hash is
`c8aec2827778a0f31645a374eebfa03c82563da9a7395ef6b5af708c1ee9ae42`.
Its source/paper reconstruction and O6 countermodel are unaffected.

## 8. Permanent ontology walls

No branch is actualized by probability. `rho` remains an external postulate.
No law is selected. Stable records are not automatically complete division
frontiers. Dependency is not chronology or spacetime causality. Unit count is
not spatial volume or proper time. The construction supplies no topology,
dimension, signature, scale, metric, connection, curvature, stress-energy,
entropy, gravity, GR, continuum, QFT, particles, or phenomenology.

The Barandes-compatible scope remains only this: arbitrary cuts need not
admit positive restart kernels, while selected complete frontiers may admit
conditioning. Stable happenings, their quotient, and their use as a metric
substrate are ISP proposals, not results attributed to Barandes.

## 9. Paper 15 authorization

The user explicitly directs continuation toward Paper 15 after terminal
Paper 14 adjudication. That successor is now authorized **only as a new
result-neutral conditional reconstruction cycle** whose live input is the
surviving structural pair

$$
(\text{locally finite unlabeled bundle poset},\ 	ext{unit occurrence measure}).
$$

Paper 15 may ask whether this pair is compatible with, selects, or fails to
select dimension, Lorentzian order, volume, duration, topology, and metric
data. It may not import:

- the rejected point-free Paper 14 probability law;
- intrinsic `Gamma` atom weights;
- a derived actuality map;
- chronological interpretation of dependency;
- null coordinates, manifold dimension, Poisson sprinkling, density, scale,
  topology, signature, or continuum as established facts; or
- the earlier nonbinding Paper 15 calculations as authoritative evidence.

The Paper 15 pin must preregister at least:

1. exact order-isomorphism and multiplicity invariance;
2. chain/antichain and same-count/different-order controls;
3. conformal and scale nonidentifiability;
4. finite-sample manifold nonuniqueness;
5. dimension/signature/model-family hypotheses;
6. unit-weight versus inserted unequal-weight separation;
7. no hidden orientation, coordinate realizer, global clock, or density;
8. out-of-family and thinning/coarse-graining controls; and
9. a ceiling no stronger than conditional manifoldlike compatibility unless
   independent selection, calibration and convergence theorems pass.

This authorization opens only the Paper 15 result-neutral pin. It does not
pre-award a spacetime coordinate, and Paper 16 remains closed.

## 10. Final disposition

Paper 14 is terminally closed without repair. The proposed full point-free
stable-happening law and intrinsic weighted premetric ceiling are rejected.
The exact stable-word theorem, complete-frontier distinctions, native
nondivision, locally finite structural bundle poset, and unit occurrence
measure are retained with the scopes above.

The next authorized event is a Paper 15 result-neutral pin built on the
surviving structural order-plus-unit-measure pair. No Paper 13 or Paper 14
source work is authorized.

The ordinary SHA-256 of this adjudication is recorded after creation in the
ledger and status board; it is not self-embedded.
