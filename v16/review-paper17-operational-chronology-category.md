# Paper 17 review — category, experiments, onset, and operational precedence

Date: 2026-08-20

Status: **INDEPENDENT BLIND SEMANTIC REVIEW / REVISE**

## 1. Corpus authentication and independence

I authenticated the frozen corpus before review.

| artifact | commit or authority | SHA-256 | size |
|---|---|---|---:|
| Paper 17 pin | `f729d95` | `90a3dac7a1a7cf9eec063ae67475da908d9298d961635c3eb53d9152ad4b34bb` | 490 LF lines / 21,247 bytes |
| Paper 17 mathematical construction | `9433fb2` | `d90a20dc475a19834c1b0bcb9e33354aae987052a5e59ea229e26b5364c18a24` | 500 LF lines / 21,396 bytes |
| Paper 17 construction note | `9433fb2` | `667195be58a2ea1079f1b3bac6cd4ae5a5e9541c57c0135ea118ba78d9a9621f` | 145 LF lines / 5,931 bytes |
| Paper 17 review protocol | `b3a344e` | `51695ccb348c73649367f892455ca067c76f302741deab486e9480b8550d5949` | 167 LF lines / 7,871 bytes |
| accepted Paper 13D law | `a8cc45e` authority | `3b91766fe269e8145766f4622f99e9009c3270530670119735e6045a473de5c9` | 1,285 LF lines / 42,928 bytes |
| Paper 13D adjudication | `a8cc45e` | `ae2c4ef066335c39a0b8057c897c947b06e4270be67d1ed3ec59bf8d6d0a00c9` | 230 LF lines / 10,395 bytes |

I read the Paper 17 pin, construction, construction note, and protocol
completely and reconstructed the accepted Paper 13D interfaces from their
mathematical law and terminal scope clauses. I did not inspect or contact a
sibling Paper 17 report and did not use Paper 15/16 drafts, preparation notes,
an implementation, generated cases, or an expected-answer table.

## 2. Verdict and first semantic counterexample

```text
REVISE
```

The accepted Paper 13D law does not need to change. Two Paper 17 conclusions
do.

First, the onset quotient does not yet preserve occurrence multiplicity under
automorphisms. Let

$$
f=u\boxtimes u
$$

be two identically prepared independent copies of one atomic generator and let
$H=(h,h)$ be a positive-mass symmetric tensor history. The tensor braiding is
in the stabilizer of the reader-free experiment and fixes $H$ while exchanging
the two generator vertices $v_1,v_2$. If $G_k$ is the onset germ at $v_k$, then

$$
[G_1]=[G_2]
$$

under the frozen definition “a primitive transition occurrence is its
diagonal orbit.” Thus the set of onset orbits contains one element although
the accepted trace has two generator vertices and the product law contains
two physical occurrences. The construction asserts that symmetry does not
fuse them, but supplies no multiset, orbit multiplicity, or groupoid-valued
finite family that retains the number two. This is a reproducible failure of
the pin's multiplicity gate and affects the quotient and co-onset coordinates.

Second, the chronology stopping statement is too strong. The missing reverse
localized intervention must remain `UNTESTED`; it is not a tested zero.
Nevertheless, the accepted trace-valued composition law proves an independent
prefix-invariance theorem at every complete division. When combined with a
nonzero complete response in a field newly written by a later generator, it
is sufficient for a scoped **Gamma-relative operational precedence**. It does
not require pretending that the absent reverse localized mark was tested.

This earns a partial precedence relation, not a complete locally finite
chronology. The chronology-valued ensemble and dimension battery remain
closed.

`REVISE` is the protocol-appropriate verdict: the Paper 17 result statement
and onset constructor need revision, but no accepted Paper 13D boundary,
generator, hom-set, probability, reader, or experiment changes.

## 3. Independent reconstruction

### 3.1 Exact accepted experiment classes

The accepted Paper 13D law has four distinct kinds of experimental variation.

1. **Localized marked intervention.** At a $B_0(I)$-source generator vertex
   $v$ of type $U_J,Q_J^0,$ or $Q_J^r$, the address is

   $$
   (v,i,F),\qquad F\in\{X,Y,E,E'\}.
   $$

   $X,Y,E$ are source-stage writes and $E'$ is a mediator-stage write. The
   point-free contrast is an aligned ordered pair of reader-free experiments
   with a common context and intersection stabilizer.

2. **Whole-boundary preparation.** For an accepted later-source arrow
   $g:D\to T$, every exact legal $y\in D$ closes a valid experiment
   $\Gamma_g(y)$. A pair $y_0,y_1$ therefore gives two accepted conditional
   experiments. It changes the complete source argument, has no marked local
   address, and does not share a prior trace unless a separate causal-break
   theorem is supplied.

3. **Operation choice.** If $g_0,g_1:D\to T$ are distinct accepted same-typed
   arrows and $f:S\to D$ is a shared prefix, then

   $$
   g_0\circ f,qquad g_1\circ f
   $$

   are two accepted whole-law experiments. This is not a `set` contrast inside
   either $g_k$, but it is a genuine choice between operations after the same
   complete boundary.

4. **Context and reader choice.** A source cylinder changes the declared
   context before evaluation. An equivariant reader is applied after the
   physical quotient and changes only a pushforward, never the history cells
   or their masses.

These classes must not be conflated. In particular, whole-boundary preparation
is not silently upgraded to a localized intervention, while operation choice
is not absent merely because it is not a program address.

### 3.2 Concrete later-preparation experiment

Fix a legal relational packet $a$ and $h$ at $B_1^0$. The exact preparations

$$
y_0=(m=0,h,a),
\qquad
y_1=(m=1,h,a)
$$

are accepted sources for $D:B_1^0\to B_2^0$. Their new $q_2$ laws are the two
columns of $B$ and therefore differ. This proves conditional sensitivity of
the continuation kernel to its complete boundary argument.

It does not test `set` at the continuation occurrence: the complete source
was replaced, there is no shared prefix, and no local continuation address is
marked. It consequently cannot be used as the missing reverse localized
fusion intervention.

### 3.3 Concrete same-typed operation-choice experiment

Let

$$
f=R_c\circ Q_J^r:B_0(I)\longrightarrow B_2^r(I)
$$

and choose nonempty $A\subseteq I$. The accepted arrows

$$
g_0=\iota,
\qquad
g_1=F_q^A\circ\iota
$$

have the same source $B_2^r(I)$ and target $B_3^r(I)$. Hence
$g_0\circ f$ and $g_1\circ f$ are an accepted nontrivial operation-choice
pair after one shared prefix. The second choice toggles the later $q^+$ field,
but neither choice changes the distribution of the complete $B_2^r$ prefix.

The same construction can be placed after recorded fusion:

$$
g_0=\iota\circ\Phi_{B_2^r},
\qquad
g_1=F_q^A\circ\iota\circ\Phi_{B_2^r},
$$

with common tensor source and common $B_3^r$ target. This supplies an accepted
operation-choice class even though it does not create a localized mark inside
the fusion vertex.

### 3.4 Prefix/no-backwards theorem at a complete division

Let $f:S\to D$ be a prefix whose target $D$ is a certified complete division,
and let $g_\lambda:D\to T$ be any accepted normalized continuation or
same-typed operation choice. For a complete prefix trace $H_f$ ending at
$y\in D$, Paper 13D's trace composition gives

$$
\Gamma_{g_\lambda\circ f}(x)
(H_f\star_y H_g)
=\Gamma_f(x)(H_f)\Gamma_{g_\lambda}(y)(H_g).
$$

Marginalizing the entire continuation trace,

$$
\begin{aligned}
P_\lambda(H_f)
&=\sum_{H_g}
\Gamma_f(x)(H_f)\Gamma_{g_\lambda}(y)(H_g)\\
&=\Gamma_f(x)(H_f),
\end{aligned}
$$

because every accepted continuation kernel is normalized. Therefore every
complete or coarse reader on the prefix has exactly the same law for every
post-$D$ operation choice. Averaging over one common source cylinder preserves
the equality.

This theorem is independent of a missing reverse localized intervention. It
does not assign that absent contrast the value zero. It proves instead that
no accepted choice made wholly in the continuation of a certified complete
division changes the already retained prefix law.

The complete-division qualification matters. At the primitive unqueried
native $B_1$ candidate cut there is no traversed complete frontier and no
positive restart kernel, so this calculation cannot be inserted there.

### 3.5 Why this is not merely category direction renamed time

The theorem uses the accepted directed composition syntax, but the proposed
precedence is not the set of all directed arrows. Define a scoped relation on
distinct onset occurrences by requiring all three conditions:

1. a certified complete division separates a prefix occurrence $A$ from a
   continuation occurrence $B$;
2. an accepted localized operation at $A$ changes a complete-reader coordinate
   in a field first written at $B$; and
3. the prefix theorem holds against every accepted post-division operation
   choice.

Call this $A\triangleleft_\Gamma B$. Typed order alone is insufficient:
identities, stable transport without new response, and zero-response tensor
components acquire no relation. Braiding and reparenthesization preserve it,
and no string-diagram drawing height, generator-list position, or loop index
appears. A native nondivision cut supplies no relation merely from its diagram.

Thus $\triangleleft_\Gamma$ is an operational precedence relative to the
accepted Gamma experiment category. It is not a derivation of an independent
spacetime time direction, and it need not compare every onset pair.

### 3.6 Fusion witness

Take two singleton components whose relational packets have already been
written, and fuse their complete target boundary at a certified tensor
frontier. The only new physical field is the cross bond. At fixed other
endpoint color,

$$
P(\ell_{ij}=1\mid d_i\ne d_j)=\frac{16}{25},
\qquad
P(\ell_{ij}=1\mid d_i=d_j)=\frac9{25}.
$$

An accepted source intervention that toggles $X_i$ at fixed $Y_i,E_i$ toggles
$d_i=e'_i$ and moves the complete bond law by magnitude $7/25$. The bond is
first written at the fusion occurrence. No generator occurrence lies between
the carried component color and that fusion write.

Consequently the component operation has a nonzero Gamma-native signal into
the fusion onset. The reverse localized fusion intervention remains absent and
its contrast remains `UNTESTED`. The prefix theorem, rather than an invented
zero, supplies the no-backwards half needed for the scoped relation
$A\triangleleft_\Gamma\Phi$.

This is at least a total inter-onset response. Calling it mechanistically
direct depends on whether the carried $d_i$ wire is counted as a mediator; the
frozen construction does not need that stronger label to earn precedence.

## 4. Onset minimality and descent

### 4.1 What atomicity proves

A Paper 13D generator vertex is atomic in the free typed execution category.
Even when its stochastic kernel algebraically factorizes, splitting it into
two physical transitions would require new typed arrows, a new intermediate
boundary, and a longer retained trace. An equality of endpoint marginals is
not an equality of trace-valued arrows.

Therefore one generator vertex supports a **Gamma-atomic onset bundle**. It
does not prove absolute metaphysical nonfactorizability under every possible
successor law. This scoped minimality is sufficient for Paper 17 if stated
categorically.

### 4.2 Multiplicity failure

The orbit of a germ is a valid presentation-independent *onset type*, but a
set of such orbits is not a valid occurrence family when a stabilizer exchanges
two equal vertices. The two-factor counterexample in Section 2 also defeats
the construction's tensor-incomparability statement on its claimed onset set:
the two factor responses are distinct at the tensor diagram level but their
onset-orbit elements coincide.

A correction would need an orbit-valued finite multiset, action-groupoid
family, or equivalent multiplicity-preserving constructor. This review does
not choose or implement one. Any such change is Paper 17 mathematics and must
be frozen and reviewed; it does not alter Paper 13D.

## 5. Mandatory semantic questions

| question | result | evidence |
|---|---|---|
| 1. generator germ descent | **PASS WITH DEFECT** | the germ transports under category equations, but taking a set of its orbits loses symmetric multiplicity |
| 2. one generator is minimal | **PASS WITH SCOPE** | it is atomic in accepted typed syntax; an algebraic kernel factorization alone cannot add a physical trace boundary |
| 3. automorphism multiplicity | **FAIL** | the symmetric tensor counterexample collapses two exchanged vertices to one orbit element |
| 4. braiding/reassociation | **PASS for germs** | they transport vertices; the remaining failure is multiplicity, not dependence on parenthesization |
| 5. experiment class | **PASS after reconstruction** | localized marks, preparations, operation choices, contexts, and readers are distinct as in §3.1 |
| 6. later preparations | **PASS WITH SCOPE** | accepted conditional experiments exist, but are whole-boundary replacements rather than accepted local causal breaks |
| 7. same-typed operation choices | **OMITTED BY CONSTRUCTION / CONSTRUCTED HERE** | $\iota$ versus $F_q^A\circ\iota$ after a common prefix is an exact accepted pair |
| 8. reverse experiment search | **UNTESTED** | no localized fusion/continuation/future/eraser intervention exists; operation choice does not fabricate one |
| 9. prefix independence | **INDEPENDENT THEOREM** | normalized trace convolution proves identical complete prefix marginals for every continuation choice at a division |
| 10. internal response | **PASS** | $X/Y/E/E'$ Boolean response and $E'$ mediation rows reconstruct from the accepted evaluator |
| 11. tensor zero | **PASS** | product semantics give every complete cross-factor coordinate zero in both directions and every common context |
| 12. singleton fusion | **PASS** | the unique fresh cross-bond probability moves by signed magnitude $7/25$ after quotient |
| 13. fusion classification | **TOTAL; DIRECTNESS SCOPED** | the response ends in a newly written bond; the carried $d$ wire may be called a mediator, but no intervening generator occurs |
| 14. carried packet | **PASS** | registered controls do not change $m$, so continuation $q_2$ has zero new-write response while the carried packet remains readable |
| 15. records/divisions | **PASS** | stable transport, erasure, complete division, and native nondivision remain distinct from influence |
| 16. bidirectional census necessity | **REFUTED AS NECESSARY FOR PARTIAL PRECEDENCE** | positive complete signaling plus the independent prefix theorem orients a Gamma-relative partial relation without assigning a reverse zero |
| 17. weaker influence relation | **PASS** | $\triangleleft_\Gamma$ is safely partial and scoped to complete divisions and accepted operations |
| 18. empty chronology | **PASS as a hostile rejection** | it is vacuous and discards the unresolved positive fusion signal |
| 19. hidden order | **PASS for $\triangleleft_\Gamma$** | the predicate uses point-free division, new-write response, and a universal marginal theorem, not phases, drawing height, or serialization |
| 20. dimension stop | **PASS** | partial precedence plus unresolved onset multiplicity is not a locally finite chronology-valued ensemble |

## 6. Fresh countermodels and controls

### 6.1 Factorizing kernel inside one atomic arrow

For a multi-occurrence $Q_J^0$, independent occurrence coins make parts of
the endpoint kernel factorize. The accepted arrow is nevertheless one atomic
vertex from $B_0(I)$ to $B_1^0(I)$ and its trace has no intermediate boundary.
Replacing a probability factorization by two onset vertices changes the typed
history law. This control prevents algebraic factorization alone from splitting
one Gamma-atomic onset.

### 6.2 Same endpoint marginal, different retained histories

For three components, simultaneous n-ary fusion and a staged pair of binary
fusions can expose the same final independent cross-bond law. Their histories
differ: the staged execution retains an intermediate fused boundary and two
fusion vertices, while the simultaneous execution retains one fusion vertex.
Endpoint equality therefore does not identify onset structure.

### 6.3 Later preparation is not a local mark

The $y_0,y_1$ pair of §3.2 changes $m$ and hence the $D$ continuation law. It
has no shared prefix and no intervention address at $D$. Treating this pair as
a localized reverse experiment would silently extend the contrast object.

### 6.4 Same-typed operations after a shared prefix

$\iota$ and $F_q^A\circ\iota$ are different accepted arrows with identical
source and target. Their choices change the later $q^+$ value but, by exact
normalization, leave every prefix reader unchanged. This is a nonvacuous
operation-choice witness for the prefix theorem.

### 6.5 Positive forward response without target-side local mark

The singleton fusion bond moves by $7/25$ under a component $X$ intervention,
while the fusion vertex has no program address. This keeps the reverse local
contrast `UNTESTED` but does not erase the positive forward signal or the
universal prefix theorem.

### 6.6 Symmetric tensor occurrence multiplicity

Two identical tensor factors under the braiding stabilizer produce two
generator vertices but one onset-germ orbit. This is the first decisive
counterexample and shows why orbit mass for histories does not automatically
supply multiplicity for an extracted set of local occurrences.

### 6.7 Mediation, cancellation, and common cause

The accepted Boolean packet supplies three distinct controls: holding $E'$
fixed kills the $X\to z_Y$ residual; the parity reader cancels the nonzero
complete $E\to(x',y')$ response; and observational
$P(y=1\mid x=1)=337/625$ differs from the intervention value $1/2$. None may
be converted into an inter-onset edge merely from a scalar association.

### 6.8 Record and division cross-controls

The record-only restriction is stable but omits $h,a$ and is not future
sufficient. Conversely, the complete $B_1^0$ queried frontier is a positive
division with no record register. Thus neither durability nor restartability
supplies chronology or a new onset by itself.

## 7. Full product vector

The revised product supported by this seat is:

```text
input       P17-INPUT-P13D-TERMINAL-GAMMA-BOUND
quotient    P17-POINT-FREE-RESPONSE-DESCENT-CONSTRUCTED;
            P17-ONSET-OCCURRENCE-MULTIPLICITY-UNCONSTRUCTED
experiment  P17-BIDIRECTIONAL-EXPERIMENT-CENSUS-INCOMPLETE
response    P17-COMPLETE-ACCEPTED-RESPONSE-ATLAS-CONSTRUCTED
co-onset    P17-PRIMITIVE-GENERATOR-ONSET-BUNDLES-UNPROVEN
chronology  P17-GAMMA-RELATIVE-OPERATIONAL-PRECEDENCE-PARTIAL
ensemble    P17-CHRONOLOGY-VALUED-ENSEMBLE-NONE
dimension   P17-DIMENSION-NONE-CHRONOLOGY-GATE-UNPASSED
signature   P17-SIGNATURE-UNCONSTRUCTED
metric      P17-METRIC-UNCONSTRUCTED
actuality   P17-ACTUALIZATION-UNCONSTRUCTED
```

The `experiment` coordinate remains incomplete because no localized reverse
fusion intervention was added or inferred. `PARTIAL` chronology means only
the scoped Gamma-relative precedence theorem of §3.5. It is not the pin's
target locally finite operational chronology.

The quotient demotion is localized: Paper 13D's physical history and response
quotients remain accepted. The defect is only Paper 17's extraction of a set
of onset occurrences from symmetric traces.

## 8. Semantic classification and scope walls

Both findings are semantic, not code-related. The multiplicity counterexample
concerns the mathematical quotient of generator germs. The precedence
correction follows from the exact accepted trace kernel and changes the Paper
17 scientific product. Neither has anything to do with ownership, mutation,
serialization, runtime, Python, Rust, or performance.

The partial precedence is relative to the accepted Gamma execution and
operation class. It does not establish that every physical influence has been
made manipulable, that the reverse localized fusion response is zero, or that
the primitive execution direction is already spacetime time. It supplies no
complete chronology, local-finiteness theorem on a multiplicity-correct onset
family, chronology-valued ensemble, or dimension estimator input.

No actualization, Lorentzian signature, topology, volume, duration, scale,
clock, metric, curvature, gravity, continuum physics, QFT, particles, or
phenomenology is promoted. The dimension gate remains closed exactly.

## 9. Disposition

The strongest honest correction is:

> A missing reverse localized intervention remains untested. At a certified
> complete division, however, normalized trace composition independently
> proves that every accepted continuation operation leaves the prefix law
> unchanged. A nonzero complete response in a field first written by a later
> onset can therefore define a Gamma-relative partial operational precedence.

Paper 17 must not call this a complete chronology. It must also repair and
review its multiplicity-preserving onset object before any chronology-valued
ensemble exists. No implementation or dimension work is authorized by this
review.

The ordinary full-file SHA-256, LF line count, and byte count are returned to
the adjudicator after the final byte is written. The report is intentionally
left unstaged and uncommitted.
