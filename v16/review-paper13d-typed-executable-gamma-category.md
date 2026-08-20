# Paper 13D review — category, groupoid, readers, tensor, and fusion

Date: 2026-08-20

Status: **INDEPENDENT BLIND SEMANTIC REVIEW / ACCEPT**

## 1. Corpus authentication

I authenticated the complete frozen corpus before scientific inspection.

| artifact | commit | SHA-256 | size |
|---|---|---|---:|
| physics pin | `a20c52a` | `722dc3bfe528fc3a52f2d2f5afcaba2c7858250e63d24439e43d0a17ab5c049e` | 459 LF lines / 14,240 bytes |
| candidate law | `efe9d97` | `3b91766fe269e8145766f4622f99e9009c3270530670119735e6045a473de5c9` | 1,285 LF lines / 42,928 bytes |
| construction note | `efe9d97` | `93f1e84444d60365fe729d73058dae1f3dede63a87bf1663d4865511255b50bb` | 203 LF lines / 9,792 bytes |
| review protocol | `04f503e` | `4754f89b01c7975ef79de2d9465e54304bbcf2d6e02b942f9957062a63c9eba3` | 301 LF lines / 13,009 bytes |

I read all four files completely. I did not inspect or contact either sibling
Paper 13D report. I used no implementation, evaluator, fixture, generated
case, or prior report as evidence.

## 2. Verdict and first decisive counterexample

```text
ACCEPT
```

No decisive mathematical or physical-semantic counterexample was found in
Seat C's assigned domain. In particular, the three Paper 13C category kills
do not recur:

- source and mediator writes now live at different control objects, so a
  reverse-stage concatenation meets an empty hom-set;
- the physical stabilizer is fixed from the reader-free experiment before a
  diagnostic reader is selected; and
- formal tensor boundaries and tensor arrows are objects and morphisms of the
  declared domain, while fusion is a separate n-ary generator.

The fresh countermodels in Section 5 include nontrivial automorphisms,
alternative-dependent stabilizers, an unanchored oriented coordinate, nested
tensor/fusion, and deletion of an entire component. Each is either refused by
an exact type or transported by an exact constructor.

This report is evidentiary rather than terminal. Acceptance by this seat does
not bind the other seats and does not authorize implementation.

## 3. Independent reconstruction summary

### 3.1 Finite-set species and groupoid

An object presentation uses an arbitrary finite occurrence set $I$. A
presentation arrow $g=(\sigma,\tau):I\to J$ consists of a bijection
$\sigma:I\to J$ and local port exchanges $\tau:I\to C_2$. If
$h=(\rho,\upsilon):J\to K$, the reconstructed composition is

$$
h\circ g=
\left(\rho\circ\sigma,
i\longmapsto\tau(i)+\upsilon(\sigma(i))\right),
$$

with addition in $C_2$. This is the standard action-groupoid composition and
has the evident inverse.

The atomic boundary species carry exactly:

| object | fields and invariants |
|---|---|
| $B_0(I)$ | $(q_0,h,c,e^0)_i$ |
| $B_1^0(I)$ | $(m,h,a)_i$ |
| $B_1^r(I)$ | $(m,r,h,a)_i$ with $r=m$ |
| $B_2^0(I)$ | $(q_2,h,t,a)_i,L$ with $t=h$ |
| $B_2^r(I)$ | $(q_2,h,t,a,r)_i,L$ with $t=h$ |
| $B_3^r(I)$ | $(q^+,h,t^+,a,r)_i,L$ |
| $B_3^e(I)$ | $(q^+,h,t^+,a)_i,L$ |

The packet $a$ has the eleven frozen binary fields and satisfies $d=e'$.
The local swap exchanges every paired $X/Y$ field and fixes scalar fields;
occurrence bijections transport unordered bond endpoints. Consequently all
three invariants $r=m$, $t=h$, and $d=e'$ are preserved on the boundary sorts
where they are declared. No later $t^+$ operation mutates the earlier $t=h$
boundary fact.

For a finite component set $A$, the formal tensor boundary
$\boxtimes_{\alpha\in A}B_{s_\alpha}(I_\alpha)$ is a Cartesian product with
component tags retained and no cross-component bonds. Component permutations,
componentwise occurrence bijections, and local swaps supply its groupoid
action. The empty family is the unit.

### 3.2 The complete control category

Let $M_0$ and $M_1$ be right-biased partial-assignment monoids on
$I\times\{X,Y,E\}$ and $I\times\{E'\}$ respectively. Pointwise, a finite
sequence retains the last defined value, hence

$$
(p\triangleright q)\triangleright r
=p\triangleright(q\triangleright r).
$$

The exact hom-table is

| source $\backslash$ target | $\mathsf S$ | $\mathsf M$ | $\mathsf C$ |
|---|---|---|---|
| $\mathsf S$ | $M_0$ | $M_0\times M_1$ | $M_0\times M_1$ |
| $\mathsf M$ | $\varnothing$ | $M_1$ | $M_1$ |
| $\mathsf C$ | $\varnothing$ | $\varnothing$ | $\{1\}$ |

All compositions act by override in the adjacent component. For an
$\mathsf S\to\mathsf M$ pair, source precomposition changes its $M_0$
component and mediator postcomposition changes its $M_1$ component. The
$\mathsf M\to\mathsf C$ arrow acts similarly. Every composable triple reduces
componentwise to associativity of $\triangleright$; the empty partial maps are
the identities.

The unique write-free phase arrows are

$$
\alpha=(\varnothing,\varnothing):\mathsf S\to\mathsf M,
\qquad
\omega=\varnothing:\mathsf M\to\mathsf C.
$$

A legal complete word $J_0;\alpha;J_1;\omega$ has the unique
$\mathsf S\to\mathsf C$ normal form $(J_0,J_1)$. A mediator endomorphism ends
at $\mathsf M$, while a source write begins at $\mathsf S$; therefore
mediator-write then source-write is not composable. No word-order exception
or reordering convention is needed.

The control objects and write-free arrows occur only in type validation.
They are not boundary species, physical traces, division frontiers, or
chronology candidates.

### 3.3 Execution syntax, traces, and addresses

$\mathsf{Exec}_D$ is the free symmetric-monoidal category on the typed atomic
process, fusion, stable-future, and eraser generators, modulo only symmetric-
monoidal coherence, finite-set covariance, and permutation invariance of one
n-ary fusion. Its hom-sets are equivalence classes of finite well-typed string
diagrams. Thus:

- composition exists exactly at equal boundary objects;
- tensor association, unit, and braiding are structural isomorphisms;
- a boundary mismatch has an empty hom-set; and
- identities and associativity follow from free categorical syntax.

Histories are recursively glued physical boundary traces. Tensor histories
are component-indexed families and a fusion history retains its tensor source
and fused target. Control phases, program words, readers, seeds, and
serialization positions are absent.

The intervention vertices $V_0(f)$ are intrinsic vertices of the string
diagram. Their addresses are

$$
\bigsqcup_{v\in V_0(f)}\{v\}\times
\bigl(I_v\times\{X,Y,E,E'\}\bigr),
$$

with the stage sort retained by the disjoint source/mediator constructors.
Association and braiding transport vertices and addresses rather than
renumbering them. $M_{\rm int}$ is exactly the support of nonempty program
entries.

Probe addresses are exactly the occurrence fields, relational subfields,
unordered bonds, and component-tagged tensor probes enumerated by the target
sort. Arbitrary strings, integer positions, names, and unlisted fields are
not addresses.

### 3.4 Reader-independent quotient

The reader-free experiment is

$$
\widehat e=(\mathcal H_S,f,K,M_{\rm int},M_{\rm land}).
$$

Its physical history cells are $\mathcal G_{\widehat e}$-orbits and have mass

$$
\Gamma_D([\widehat e])([H]_{\widehat e})
=\sum_{H'\in\mathcal G_{\widehat e}H}
\widetilde\Gamma(\widehat e)(H').
$$

No diagnostic reader enters $\mathcal G_{\widehat e}$. Changing only a reader
therefore cannot change the orbit partition or these masses.

If $p$ is not fixed by the stabilizer, the naked value $H(p)$ is not constant
on a physical cell. The exact admissible replacement is the addressed orbit
profile

$$
\left[(q,H(q))_{q\in\mathcal G_{\widehat e}p}
\right]_{\mathcal G_{\widehat e}}.
$$

If a singleton physical landmark $\{p\}$ is included in $M_{\rm land}$, every
experiment stabilizer element fixes $p$, and its oriented field value becomes
well defined. The reader remains outside the stabilizer; it is the physical
landmark, not a diagnostic function name, that breaks the symmetry.

For an ordered alternative contrast, the common physical comparison uses

$$
\mathcal G_\chi=
\mathcal G_{\widehat e_a}\cap\mathcal G_{\widehat e_b}.
$$

This remains exact when one alternative has an accidental automorphism absent
from the other. Both laws push to the common refinement, and diagonal
transport conjugates the complete ordered pair and its intersection
stabilizer.

### 3.5 Independent tensor and simultaneous fusion

Tensor boundaries, tensor arrows, product histories, product readers, the
braiding, and the empty unit are all internal to $\mathsf{Exec}_D$. Structural
recursion assigns their exact product law.

For a finite component family of one atomic sort, simultaneous fusion is the
single generator

$$
\Phi_s^{\{I_\alpha\}}:
\boxtimes_\alpha B_s(I_\alpha)
\longrightarrow B_s\!\left(\bigsqcup_\alpha I_\alpha\right).
$$

It forgets component tags, carries all within-component fields and bonds, and
draws exactly one fresh coin for each unordered cross-component pair. The
family is unordered, so component permutation reindexes the same target
occurrences and seed set. For zero components it is the deterministic arrow
from the tensor unit to the unique empty atomic boundary value; for one it
forgets the trivial component partition and draws no cross coin; for two or
more it draws the entire cross-pair set simultaneously.

A nested sequence of physical fusion generators is a different string diagram
and retains additional intermediate boundaries. It need not be identified
with a single n-ary fusion even when its final marginal happens to agree.

### 3.6 Deletion and fusion naturality

Deleting $i\in I$ restricts every traversed boundary, bond set, seed family,
program, and intrinsic address. The operation is equivariant because
deleting $i$ and then applying $g$ equals applying $g$ and deleting
$g(i)$. On a fusion family, restriction removes every cross pair incident on
$i$; if a component becomes empty, the declared empty-component removal gives
the fusion of the remaining restricted family. Both sides retain the same
occurrences, internal bonds, and surviving cross-pair seeds. The auxiliary
order in which those independent factors are exposed is absent from the
execution diagram.

## 4. Registered attacks C1--C18

| attack | result | evidence |
|---|---|---|
| C1 all $\mathsf{Ctrl}$ hom-sets | **PASS** | §3.2 reconstructs the nine hom-sets, all nonempty compositions, units, and componentwise associativity |
| C2 mediator then source | **PASS** | it requests an arrow in $\operatorname{Hom}(\mathsf M,\mathsf S)=\varnothing$ and never reaches normalization |
| C3 equal normal forms | **PASS** | equal pairs arise only from within-stage override associativity, same-slot last-write, disjoint-address commutation, and the declared write-free arrows |
| C4 phase arrows physicalized | **PASS** | $\mathsf S,\mathsf M,\mathsf C,\alpha,\omega$ occur in no boundary or trace constructor |
| C5 execution hom-sets | **PASS** | free typed symmetric-monoidal string diagrams supply identity, associator, braiding, composition, and exact empty hom-sets on mismatch |
| C6 vertex under coherence | **PASS** | association and braiding preserve the intrinsic vertex and transport its address; no integer enumeration enters $V_0(f)$ |
| C7 boundary invariants | **PASS** | occurrence bijections and local swaps preserve $r=m$, $t=h$, $d=e'$, scalar fields, and unordered bond endpoints |
| C8 reader-only change | **PASS** | the stabilizer is defined from $\widehat e$ before $R$; reader changes only pushforward |
| C9 nonfixed coordinate | **PASS** | a naked value fails on a nontrivial address orbit, while the complete addressed orbit-profile is representative independent |
| C10 singleton landmark | **PASS** | a stabilizer preserving the singleton set $\{p\}$ fixes $p$, so an oriented field reader is defined without adding $R$ to the stabilizer |
| C11 accidental automorphism | **PASS** | the ordered contrast uses the exact intersection stabilizer and common refinement; §5.2 gives an explicit example |
| C12 representative mass | **PASS** | §5.1 gives fixed and size-eight orbits; orbit-sum mass counts both correctly while representative mass undercounts a nontrivial orbit |
| C13 tensor domain | **PASS** | formal tensor objects/arrows, product histories/readers, braiding, and empty unit all occur in the declared SMC and evaluator |
| C14 n-ary fusion | **PASS** | zero-, one-, two-, permuted-, and nested-family cases follow one unordered-family constructor with simultaneous cross-pair seeds |
| C15 staged versus simultaneous | **PASS** | staged fusion is a distinct composite trace with an extra boundary; no equation gauges it to one n-ary vertex |
| C16 tensor/fusion action | **PASS** | component tags, target disjoint unions, intrinsic marks, local ports, and cross-pair endpoints all transport functorially |
| C17 deletion naturality | **PASS** | deletion transports $i$ to $g(i)$, restricts intrinsic addresses, and restricts one n-ary fusion to the surviving family after empty-component removal |
| C18 unlisted syntax | **PASS** | addresses arise only from finite constructors; field strings, reader names, program metadata, and serialization positions have no type |

## 5. Fresh countermodels

### 5.1 Nontrivial automorphism and representative mass

Let $I=\{1,2\}$ in the unmarked observational experiment. Choose two equal
occurrence traces, each internally $X/Y$-fixed, and a fixed bond value. The
two local swaps and occurrence transposition generate a stabilizer of order
8, so this history has orbit size 1. A positive-mass generic history with
distinct occurrence data and no local swap symmetry has trivial stabilizer
and orbit size 8. The exact formula

$$
|\mathcal G_{\widehat e}H|
=\frac{|\mathcal G_{\widehat e}|}
{|\mathcal G_{\widehat e,H}|}
$$

handles both. Assigning one representative mass to each orbit undercounts the
generic cell by a factor of 8. The frozen orbit pushforward passes.

### 5.2 Alternative-dependent stabilizer

Take two otherwise symmetric occurrences with source-stage $X$ writes at both.
Fix the first value to zero and use the second as the contrast address. In the
zero-versus-zero alternative, occurrence exchange is an accidental symmetry;
in the zero-versus-one alternative, it is not. Quotienting the two experiments
separately and subtracting cells would be ill aligned. Their intersection
stabilizer removes the accidental exchange and gives one common comparison
fiber. The ordered contrast constructor passes.

### 5.3 Unanchored orientation versus a physical landmark

For one swap-symmetric occurrence without landmarks, $H(X)$ and $H(Y)$ are
exchanged inside one physical cell whenever they differ. A reader returning
the naked $X$ value is therefore not well defined. The orbit profile of the
addressed pair is well defined. Adding the singleton landmark $\{X\}$ to the
reader-free experiment reduces the stabilizer to elements fixing $X$, after
which the oriented $X$ reader is exact. Merely naming that reader without the
landmark remains refused.

### 5.4 Three-component tensor/fusion nesting

For nonempty components $A,B,C$, compare the single generator
$\Phi_{A,B,C}$ with

$$
\Phi_{A\sqcup B,C}\circ
(\Phi_{A,B}\boxtimes 1_C).
$$

Both can have the same final distribution because they ultimately expose the
same independent bond coins. They are not the same physical history law: the
second trace contains the intermediate boundary $B_s(A\sqcup B)$. The free
execution syntax distinguishes them, while permutations of the inputs of the
single first generator are identified only through braiding and n-ary
permutation invariance. No fold order enters the simultaneous generator.

### 5.5 Deletion of a whole component

Fuse a singleton component $A=\{a\}$ with nonempty $B$. Delete $a$. Every
cross bond incident on $a$ disappears, the restricted $A$ component is empty,
and empty-component removal leaves the one-component fusion of $B$. Deleting
after target fusion leaves the same $B$ occurrence fields and internal bonds.
Relabelling first merely replaces $a$ by its image. This passes the combined
address, fusion, and covariance attack without a hidden insertion index.

### 5.6 Same control result from different typed words

Let $p,q,r$ be source-stage writes, with $p,q$ writing the same address and
$r$ a disjoint address. The legal words

$$
(p;q);r,
\qquad p;(q;r)
$$

both retain $q$ on the repeated address and $r$ on the disjoint address. Their
equality follows from right-biased override and associativity. By contrast,
moving a mediator endomorphism ahead of any source endomorphism is not another
word with that normal form: it is untyped at the attempted join. Thus the
declared equations identify exactly the intended pairs.

## 6. Full product vector

Seat C found no semantic counterexample demoting any registered coordinate.
The full vector is therefore:

```text
referent    P13D-POINT-FREE-EXECUTABLE-GAMMA-CONSTRUCTED
law         P13D-ONE-TYPED-EXECUTABLE-GAMMA-CONSTRUCTED
experiment  P13D-TYPED-EXPERIMENT-CATEGORY-CONSTRUCTED
nondivision P13D-NATIVE-B1-CUT-NONDIVISIBLE
record      P13D-TYPED-STABLE-FUTURE-CATEGORY-CONSTRUCTED
eraser      P13D-EXECUTABLE-ERASER-CONTROL-CONSTRUCTED
division    P13D-COMPLETE-DIVISION-FRONTIERS-CONSTRUCTED
size        P13D-VARYING-SIZE-COVARIANT-FAMILY-CONSTRUCTED
response    P13D-RECIPROCAL-RELATIONAL-RESPONSE-CONSTRUCTED
actuality   P13D-ACTUALIZATION-UNCONSTRUCTED
```

Coordinates outside Seat C remain subject to the independent probability and
physics reports and terminal adjudication.

## 7. Semantic-versus-code classification

Every attack above concerns mathematical objects: hom-sets, trace types,
finite-set actions, stabilizers, reader descent, tensor/fusion syntax, and
deletion naturality. No ownership, mutability, serialization, lifetime,
transaction, memory, performance, CLI, or prospective implementation property
was used. No code-only defect was observed because no code is authorized or
part of the corpus.

Had reverse-stage composition normalized, readers changed the stabilizer, or
the tensor lived outside $\mathsf{Exec}_D$, each would have been semantic and
would have required a new law. The frozen 13D constructions prevent those
counterexamples mathematically.

## 8. Scope and ontology walls

The control objects are operational typing phases, not physical instants.
String-diagram composition and deliberately staged fusion are execution
syntax, not a derived chronology. Simultaneous fusion's absence of an input
order prevents a serialization index from becoming a clock, but does not
derive spacelike simultaneity.

Occurrence cardinality is neither event number nor volume. Fusion bonds are
not spatial adjacency. Stabilizer orbits are presentation classes, not actual
events. Readers are diagnostics, not actualization maps. Relational response
does not establish causal direction, backreaction, energy transfer, or
gravity.

No actuality, chronology, causal order, signal cone, dimension, signature,
topology, measure, duration, scale, metric, connection, curvature, stress
tensor, energy, entropy, gravity, GR, continuum limit, QFT, particle content,
or phenomenology is constructed.

## 9. Bounded wording observations

No mathematical repair is required by this seat. Two optional explanatory
additions could make later implementation specifications easier without
moving any object or probability:

1. print the semidirect groupoid composition formula reconstructed in §3.1
   instead of calling it “evident”; and
2. print the zero- and one-component fusion clauses and the empty-component
   deletion convention as explicit equations.

Both are already uniquely fixed by the finite-family, empty-unit, and
restriction definitions. They are wording expansions only and are not
conditions on this acceptance.

## 10. Artifact accounting

The ordinary SHA-256, LF line count, and byte count apply to the complete
frozen report bytes and are computed after the final byte is written. They are
returned with this report to the adjudicator; embedding a full-file digest in
the file it hashes would change that digest. The report is intentionally left
unstaged and uncommitted for independent freezing.
