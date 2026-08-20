# Paper 13B point-free Gamma: hostile physics/ontology review

Date: 2026-08-20

Seat: physics and ontology; owner of H23--H26

Verdict: **REJECT**

Status: **FROZEN ON DELIVERY / MATHEMATICS AND PHYSICS SEMANTICS ONLY**

## 1. Independence and corpus authentication

I read the frozen protocol before the scientific corpus. I did not read either
sibling review, any prior Paper 13/14 evaluator or review, or another agent's
reconstruction. I used no repository implementation or evaluator. All
arithmetic below was reconstructed from the frozen prose.

The protocol authenticated as follows:

| artifact | observed SHA-256 | lines | bytes |
|---|---|---:|---:|
| `v16/note-paper13b-pointfree-gamma-math-review-protocol.md` | `034fbe56a79a91860812bfbe4322e635a4a579f79f2b9b135877db2536e6a409` | 326 | 12563 |

The review corpus authenticated byte-for-byte both in the working tree and at
the named commits:

| artifact | commit (resolved) | required and observed SHA-256 | lines | bytes |
|---|---|---|---:|---:|
| physics pin, `v16/note-paper13b-pointfree-gamma-physics-pin.md` | `f35c28fcb7a39775ffe47af352d563f9a37d0d44` | `df2c60be816e2aaf5261f954d6e1d12142ad528f572f7c77c1ff5a91464b4f47` | 463 | 18935 |
| paper, `v16/paper-13b-pointfree-whole-history-gamma.md` | `2ef0f26f32cbf5f15d1a304221b17e9eb4ed9c9c` | `5f55d1249e68e9b019790dda52254f819b68917637752cc32f0580ea07f7ff18` | 680 | 20602 |
| construction note, `v16/note-paper13b-pointfree-gamma-mathematical-construction.md` | `2ef0f26f32cbf5f15d1a304221b17e9eb4ed9c9c` | `ad13c0ba07110f608047a48a7b3cf921dac66c4beb4e857b000dc7d127c8f9f7` | 118 | 4261 |

## 2. Result in one paragraph

The frozen bytes do construct an exact normalized exchangeable probability
law on finite typed-history orbits. The orbit arithmetic, all-size mixture,
uniform-deletion result, displayed response arithmetic, and record
intertwining checks survive. They do not construct the advertised physical
packet at the frozen scope. The first decisive counterexample is that the
same static whole-history law admits a different directed factorization with
different `do` probabilities. Thus the paper must either treat its displayed
structural arrows as physical/operational extra structure--contrary to the
pin's no-causal-order rule and the paper's claim that factorization is mere
representation--or concede that its experiment law is not determined. In
addition, the experiment/read/context classes are named but not determined,
and the claimed native nondivision carrier is absent from mode $U$ itself.
Those are semantic defects, not implementation defects. They defeat promoted
coordinates and require more than bounded prose repair.

## 3. Independent reconstruction

### 3.1 Numerical core

Direct multiplication gives

$$
R^2=\frac1{25}
\begin{pmatrix}
-7&-24\\
24&-7
\end{pmatrix},
\qquad
B=\frac1{25}
\begin{pmatrix}
9&16\\
16&9
\end{pmatrix},
$$

$$
C=|R^2|^2=\frac1{625}
\begin{pmatrix}
49&576\\
576&49
\end{pmatrix},
\qquad
B^2=\frac1{625}
\begin{pmatrix}
337&288\\
288&337
\end{pmatrix}.
$$

Also

$$
B^{-1}=\frac17
\begin{pmatrix}
-9&16\\
16&-9
\end{pmatrix},
\qquad
CB^{-1}=\frac1{175}
\begin{pmatrix}
351&-176\\
-176&351
\end{pmatrix}.
$$

Every column of $B,C,B^2$ sums to one. The determinant of $B$ is
$-7/25$, so the candidate in the last display is the unique $K$ satisfying
$C=KB$.

### 3.2 Local normalization and Boolean core

For each fixed mode, the independent fair variables $q_0,h,c,e$ each
normalize, each noise row sums as $16/25+9/25=1$, and all displayed Boolean
outputs are deterministic. Mode $U$ contributes a normalized column of $C$.
Modes $R$ and $D$ each contribute

$$
\sum_m B_{m q_0}\sum_{q_2}B_{q_2m}=1.
$$

Multiplication by $P(w)=1/3$ and summation over the three values gives one.
Thus the local labeled law is normalized, including separately at every fixed
source context.

The Boolean relational core is invertible because

$$
e=e'\oplus x'\oplus y',\qquad
x=x'\oplus e,\qquad y=y'\oplus e.
$$

Exchanging $X$ and $Y$ swaps all five displayed ordered pairs, fixes $e,e'$,
and leaves every primitive factor unchanged because the two noise variables
have the same law. Hence the local law is $G_1$-invariant.

### 3.3 Local orbits, bonds, and labeled sizes

A local atom is fixed by the internal swap precisely when
$\eta_X=\eta_Y$ (the other exchanged fields then agree as consequences).
The total fixed mass is

$$
\left(\frac{16}{25}\right)^2+
\left(\frac9{25}\right)^2=\frac{337}{625};
$$

the paired-orbit mass is $288/625$. Fixed atoms contribute once and paired
atoms contribute the sum of two equal labeled masses.

For fixed endpoint colors the bond row normalizes as $p+(1-p)=1$, with
$p=9/25$ for equal colors and $p=16/25$ for unequal colors. Therefore the
labeled partition sums are, without invoking a theorem label,

$$
Z_0=1,
$$

$$
Z_1=\sum_{a_1}\widetilde\mu(a_1)=1,
$$

$$
Z_2=\sum_{a_1,a_2}\widetilde\mu(a_1)\widetilde\mu(a_2)
\sum_{\ell_{12}}P(\ell_{12}\mid a_1,a_2)=1,
$$

and

$$
Z_3=\sum_{a_1,a_2,a_3}\prod_i\widetilde\mu(a_i)
\prod_{i<j}\sum_{\ell_{ij}}P(\ell_{ij}\mid a_i,a_j)=1.
$$

The same factorization proves $Z_n=1$ for every finite $n$.

For an explicit nontrivial-automorphism case, take three identical
$\tau$-fixed atoms with a path bond graph. In
$G_1^3\rtimes S_3$ the eight internal swaps and the path's endpoint exchange
stabilize the history, so the stabilizer has size $16$, the orbit has size
$48/16=3$, and the pushforward is the sum of those three distinct labeled
path placements. The physical multiplicity remains $N=3$; the automorphism
does not collapse three occurrences to two. For a history with three
pairwise-distinct local orbit types, nonfixed local presentations, and no
typed graph symmetry, the stabilizer is trivial and the orbit has all $48$
elements. In both cases the orbit pushforward is exactly the sum of distinct
labeled masses, not group order times one representative.

The geometric mixture normalizes because
$\sum_{n\geq0}2^{-(n+1)}=1$. Deleting a uniformly marked atom from the iid
atom law removes exactly its incident bond factors; all surviving atom and
bond factors are unchanged. Equivariance then makes quotient-after-deletion
equal deletion-after-uniform-lift. This proves the stated projectivity. It
does not make deletion a physical time evolution.

### 3.4 Symmetric marked intervention

Choose a local history with $c=e=0$ and
$\eta_X=\eta_Y=0$, hence $x=y=0$; choose all other swap-fixed fields
arbitrarily. The underlying history is fixed by $\tau$. The packet marked
`do(X=1)` is carried by $\tau$ to the packet marked `do(Y=1)`, with the
corresponding outcome slots and reader transported. A naked `do(X=1)` is not
invariant on the unmarked history orbit. The paper handles this particular
symmetry correctly by requiring the complete packet orbit.

### 3.5 Complete signed tensors

I use outcome order $(0,1)$ for binary readers and the convention
`do(first) - do(second)`.

| control | complete signed entries |
|---|---|
| $X:1-0\to e'$, fixed $e,y$ | $(-1,+1)$ if $e\oplus y=0$; $(+1,-1)$ if $e\oplus y=1$ |
| $E:1-0\to(x',y')$, fixed $x,y$ | $-1$ at $(x,y)$, $+1$ at $(1-x,1-y)$, zero at the other two outcomes |
| total $X:1-0\to z_Y$, fixed $e$ | $(-1,+1)$ if $e=0$; $(+1,-1)$ if $e=1$ |
| direct residual $X\to z_Y$ with $e'$ independently fixed | $(0,0)$ |
| common-cause intervention $X:1-0\to Y$ | $(0,0)$ |
| $E:1-0\to x'\oplus y'$ | $(0,0)$ |
| $X:1-0\to u_X$ at $c=0$ | $(-1,+1)$ |
| $X:1-0\to u_X$ at $c=1$ | $(+1,-1)$ |
| $q_0\to e'$ | $(0,0)$ |
| incident bond $X:1-0\to\ell$, when $d(x=0)=d_j$ | $(-7/25,+7/25)$ |
| incident bond $X:1-0\to\ell$, when $d(x=0)\ne d_j$ | $(+7/25,-7/25)$ |

All rows sum to zero. The exact common-cause calculation is

$$
P(y=1\mid x=1)=\frac{337}{625},\qquad
P(y=1\mid\operatorname{do}(x=1))=\frac12,
$$

so the observational excess is $49/1250$. The mediation, cancellation,
context reversal, spectator, and bond-orientation controls all have the
claimed arithmetic. Their physical promotion nevertheless depends on a
well-defined intervention object; Findings 1 and 2 address that dependency.

### 3.6 Stable records and four division cases

For $F_Q,F_T,F_{XY}$ the record sector is fixed, and for $F_R$ it is swapped
together with the output projector. Thus
$P_r^{\rm out}F=FP_r^{\rm in}$ generator by generator, and composition proves
the equality for every finite licensed word. A noninjective reset maps both
input sectors to one output and admits no transported inverse reader; a
reversible swap does. The record theorem is correct exactly relative to this
licensed grammar, not as an absolute durability theorem.

The three well-referred cases are:

- in $R$, $Z_R$ carries $m,r,h$ and all declared relational data; $B$ is a
  positive normalized continuation and $t=h$;
- the $r$-only restriction stays readable but histories with the same $r$
  and opposite $h$ give opposite deterministic $t$, so it is not
  future-sufficient; and
- in $D$, $Z_D$ carries $m,h$ and the declared relational data and supports
  the same positive $B$ continuation without a new $r$ register.

The proposed fourth case has the correct matrix calculation but not the
claimed native physical referent; see Finding 3.

## 4. Findings, most severe first

### FATAL-1 — the experiment law contains an undeclared directed causal order

The paper calls the factorization notation a representation, but defines
intervention by replacing one structural assignment and retaining its other
factors. Those two claims are incompatible: `do` distributions are not
functions of a static joint distribution.

Here is the decisive countermodel. Let $P_0$ be the paper's joint law on the
source and relational variables. Its $(x,y)$ marginal is

$$
P_0(x)=\frac12,\qquad
P_0(y=x\mid x)=\frac{337}{625},\qquad
P_0(y\ne x\mid x)=\frac{288}{625}.
$$

Factor exactly the same full joint law instead as

$$
P_0(x)P_0(y\mid x)P_0(c,\eta_X,\eta_Y\mid x,y),
$$

leaving $e$, all process variables, deterministic relational outputs, bonds,
and all other factors unchanged. This is identically $P_0$ by the chain rule,
so it gives the same labeled and physical whole-history probabilities. Under
truncated evaluation of this factorization,

$$
P_0(y=1\mid\operatorname{do}(x=1))=\frac{337}{625},
$$

whereas truncated evaluation of the paper's displayed common-source
factorization gives $1/2$. The same $\Gamma_*$ therefore has two different
experiment laws unless the directed structural assignments are additional
physical/operational data.

They plainly are used as such: the paper designates sources, input,
intermediate, final, downstream, later, and future variables; it truncates
upstream assignments while retaining downstream ones; and it defines
$q_0\to m\to q_2$, $c\to(x,y)$, $(x,y,e)\to(x',y',e')$, and
$h\to t$. That is a local directed causal/chronological partial order even
though it is not a metric time coordinate or an inter-atom chronology. The
pin says no field of the packet may contain causal order, while the paper says
factorization is representation and permanently disclaims causal order. The
experiment and response claims consume that very order.

This is the first decisive semantic counterexample. Treating the arrows as
mere representation makes the experiment law nonunique; treating them as
part of the experiment packet violates the frozen ontology firewall. Repair
would change or explicitly enlarge the experiment interface and is therefore
not a bounded prose correction.

Required replacement sentence, if the result is demoted rather than rebuilt:

> The normalized static law does not by itself determine the displayed `do`
> distributions; these additionally use a directed structural-order
> postulate, which is outside the no-causal-order scope of this paper.

### MAJOR-2 — `Exp`, `Read`, exterior context, and admissibility are named but not determined

The packet $(H,Z,A,a,R,E)$ is given only through phrases such as “relevant
endpoint and bond fields,” “complete reader,” “declared future fields,” and
“complete exterior context.” The paper never defines the set of admissible
slots, the descendant/fixed-context rule for every slot, the future field set
for every experiment, the complete partitions, or the object and morphism
sets of `Exp` and `Read`. Its examples cover $X,E,E'$ and selected readers,
but the quantified covariance theorem ranges over an unconstructed class.
Including a complete already-realized $H$ in the packet while computing
probabilities conditional only on $E$ also leaves the role of $H$ unstated.

The finite presentation action transports any fully specified example
correctly. It does not turn the placeholders into the complete experiment
action groupoid required by the pin. This is a referent failure for the
promoted experiment coordinate and blocks unconditional promotion of the
response coordinate.

Required replacement sentence:

> Only the explicitly displayed marked interventions and readers are defined;
> a total point-free experiment/reader action groupoid is not constructed.

### MAJOR-3 — the negative-kernel calculation is not a native nondivision frontier

Mode $U$ explicitly has no intermediate state or record random variable. The
later nondivision argument nevertheless inserts a “proposed $B$ intermediate
carrier.” No $Z_U$, native boundary variable, or first-leg experiment whose
marginal is $B$ exists in the $U$ history. The calculation correctly proves
only that the stipulated external first leg $B$ cannot be followed by a
positive $K$ to obtain $C$.

It does not prove that the normalized transition $C$ is indivisible through a
two-state carrier. For example, it has the positive normalized
factorizations

$$
C=C I=I C.
$$

Those are different proposed cuts, not refutations of the $B$-specific
matrix calculation. They show why the absent native carrier matters: the
whole law does not select $B$ as an intermediate $U$ frontier. The appeal to
$R$ as a coherent two-step representation cannot supply a native physical
carrier while the paper simultaneously says amplitude/factorization notation
adds no ontology.

Consequently `P13B-NATIVE-INDIVISIBLE-CUT-CONSTRUCTED` is not earned and the
NO/NO cell of Theorem 6 lacks the required frontier referent.

Required replacement sentence:

> The calculation proves only that $C\ne KB$ for every positive stochastic
> $K$ with the stipulated first leg $B$; mode $U$ contains no native
> intermediate frontier, so native nondivision remains unproven.

### MINOR-4 — the measurable structure is implicit rather than declared

The paper defines a countable orbit set and point masses but never states
$\Sigma$. Taking the full power set supplies the standard discrete measurable
space and moves no probability. This omission does not cause the rejection.

Required replacement sentence:

> The physical sigma algebra is the full power set of the countable set of
> finite typed-history orbits.

## 5. Mandatory hostile attacks H1--H26

### H1--H11: quotient, multiplicity, and size

| attack | result |
|---|---|
| H1 representative mass | Fails as it must. At $n=1$, representative-only mass would be $337/625+(288/625)/2=481/625$, not one. |
| H2 automorphism multiplicity | Pass. The repeated-atom path example has stabilizer $16$, orbit size $3$, and still three physical occurrences. |
| H3 internal fixed point | Pass. Fixed mass $337/625$ is counted once; paired mass $288/625$ is summed by two-element orbits. |
| H4 naked symmetric intervention | Pass for the displayed packet action. `do(X=1)` and transported `do(Y=1)` are one packet orbit, not separate invariant naked commands. |
| H5 history-only quotient | Rejected by the paper's packet rule; leaving slot, reader, or context behind breaks covariance. |
| H6 enumeration order | Pass. Permutations only reorder equal atom and endpoint-conditioned bond factors. |
| H7 endpoint sever | Correctly not the same orbit; a bond transports with its unordered endpoints. |
| H8 per-size replacement | A replacement at one $n$ preserves that table's normalization but destroys the uniform-rule theorem and generally H9. |
| H9 deletion | Pass for the frozen rule: surviving bond factors are exactly the lower-size factors. |
| H10 hidden order | Any tuple-index-dependent bond probability changes under an $S_n$ permutation and fails covariance. No such dependence occurs. |
| H11 dormant carrier | A fixed inactive carrier adds label/inactivity structure and a different sample space. The paper uses exactly $N$ realized occurrences. |

### H12--H22: intervention, records, division

| attack | result |
|---|---|
| H12 conditioning as intervention | Pass arithmetically: $337/625\ne1/2$. The deeper factorization dependence is FATAL-1. |
| H13 incomplete reader | Pass: parity gives the zero vector while the complete pair reader has two entries $-1,+1$. |
| H14 mediator deletion | Pass: total $X\to Z_Y$ has TV one; fixing $e'$ makes the residual zero. |
| H15 context aggregation | Pass: the $c=0$ and $c=1$ tensors are negatives and average to zero. |
| H16 bond orientation | Pass: the vectors reverse between equal and unequal endpoint colors with magnitude $7/25$. |
| H17 reversible swap | Pass: transported projectors retain exact readability. |
| H18 true eraser | Pass: the reset is normalized as a map but noninjective and nonrecoverable, hence excluded. |
| H19 record implies division | Refuted correctly: equal $r$ and different $h$ give different $t$. |
| H20 division implies record | Pass at the declared $D$ process frontier: $B$ is positive and normalized and no $r$ field is written. |
| H21 native cut | The matrix candidate is uniquely negative, but its native-frontier interpretation fails by Finding 3. |
| H22 enlargement | The recorded $B^2$ control is a distinct enlarged history and does not change the $B$-specific negative matrix. It also cannot create the missing native $U$ frontier retroactively. |

### H23--H26: owned physics/ontology attacks

**H23, mode-as-law menu.** Pass. Formally the local atom space is a typed
disjoint union over $w\in\{U,R,D\}$, with fixed mass $1/3$ on each sector and
fixed conditional kernels. No theorem changes $P(w)$ after inspecting an
outcome. Conditioning on a sector to exhibit a control is not selection of a
new law. Postselecting $w=R$ to force a record would be a different law, and
the paper does not do it.

**H24, parameter retuning.** Pass. The rotation seed, fair priors, equal mode
weights, bond rule, and geometric cardinality law are fixed by stipulation.
Changing any physically inequivalent value changes $\widetilde\mu$,
$\Gamma_n$, or the $N$ mixture and is correctly recognized as a new candidate.
Sign/orientation variants that disappear after entrywise squaring are only
representational variants. No result-dependent retuning occurs. The values
are not uniquely derived, and the paper says so.

**H25, dimension leakage.** No spatial dimension, metric, coordinate, lattice,
target scaling law, or desired spacetime behavior is used to choose the law.
The all-pairs bond domain is a binary relational signature, not declared
spatial adjacency, and $N$ is not thereby volume. This part passes. The
broader no-clock/no-chronology firewall fails: the directed structural and
future order identified in FATAL-1 is already inside each atom. It is local
partial chronology rather than a global clock, but it is still causal-order
data forbidden by the pin. A later dimension failure must reject that later
coordinate and cannot authorize retuning here; the paper states this
correctly.

**H26, actuality smuggling.** Pass. “Sample,” “generate,” and “choose $N$” are
probability-space construction language. The paper explicitly distinguishes
possible histories from an actual selected history, and it conditions stable
records on a realized branch without claiming that a branch is selected.
Actualization remains unconstructed.

## 6. New countermodels

The following are independent of the protocol's supplied attacks. The first
four are the physics-seat mandatory contrasts; the next four stress their
boundaries.

1. **Same relational graph, different typed atoms.** At $n=2$, keep the same
   endpoint colors and the same bond bit, but flip $q_0$ or $h$ in one atom.
   The graph is identical and both histories have positive mass, yet the
   complete typed-history orbits are different. This confirms that a coarse
   graph is not the physical history referent.
2. **Same count, different graph.** At $n=3$ with equal endpoint colors, the
   empty graph and triangle have the same $N$ and positive conditional factors
   $(16/25)^3$ and $(9/25)^3$, respectively. Thus cardinality is multiplicity,
   not graph structure, topology, or volume.
3. **Same graph, different law.** Keep the identical atom and graph sample
   space but replace both endpoint bond probabilities by $1/2$. An equal-color
   occupied edge changes factor from $9/25$ to $1/2$. Graph ontology does not
   select its probability law; the frozen probabilities are additional
   stipulated law data.
4. **Identical stable record, different complete frontier sufficiency.** In
   mode $R$, fix the same $m=r$ and all other restricted-frontier data but take
   $h=0$ and $h=1$. The record reader returns the same $r$ in both histories,
   while the complete future reader of $t$ returns $0$ and $1$. Record
   stability does not imply division.
5. **Same whole-history law, different `do`.** The chain-rule refactorization
   in FATAL-1 leaves every observational history probability fixed but changes
   $P(y\mid\operatorname{do}x)$. It is the decisive chronology/representation
   countermodel.
6. **Same $C$, positive alternative cut.** The normalized $C$ factors as
   $CI$ and $IC$. This does not rescue the paper's $B$-specific restart, but it
   disproves any carrier-independent reading of “two-state indivisible.”
7. **Same conditional family, different multiplicity law.** Replacing
   $2^{-(n+1)}$ by, for example, $1/[(n+1)(n+2)]$ preserves every
   $\Gamma_n$ and uniform-deletion theorem and still normalizes over all
   $n$, but changes the physical $N$ distribution. Hence projectivity does not
   derive the cardinality prior; the paper correctly treats it as primitive.
8. **Same record alphabet, normalized stochastic loss.** Apply the stochastic
   channel with both rows $(1/2,1/2)$ to the record bit. It is normalized and
   leaves a fair output but makes the input sectors unrecoverable. Stability
   therefore requires recoverability, not normalization or persistence of the
   alphabet alone.

## 7. Physics/ontology questions

| question | answer |
|---|---|
| One fixed candidate or uniquely derived? | One fixed candidate by stipulation. It is not uniquely derived, and no uniqueness is earned. |
| Are atom and bond referents distinguished? | Yes mathematically: an atom is a complete typed local-history occurrence; a bond is an endpoint-typed unordered inter-atom bit. Neither is spatial by itself. |
| Is the record referent distinguished? | Yes, but only relative to the frozen four-generator grammar and transported reader. It is not absolute durability. |
| Is division distinguished from record? | Yes for the $R$ complete/restricted and $D$ controls. Future sufficiency, not the presence of $r$, makes the distinction. |
| Is the experiment referent distinguished? | No at the promoted scope. Specific examples transport, but the admissible packet/context/reader classes are not determined, and their `do` semantics consumes an undeclared directed order. |
| Does the atom-and-bond ensemble already contain chronology? | Yes locally. The source/intermediate/final, downstream, late, and future roles plus truncated structural intervention define a directed partial order. No inter-atom or metric chronology is derived. |
| Is $N$ physical multiplicity but not time or volume? | Yes. It counts occurrences; neither the law nor projectivity supplies a clock or volume calibration. |
| Is reciprocal response relational rather than geometric? | The displayed algebra is relational and contains no metric or geometry. Its unconditional physical promotion fails with the experiment referent; it is not backreaction or gravity. |
| Does amplitude notation add ontology? | Not by itself. $R$ is only a recipe for $B$ and $C$. It cannot, consistently with that statement, supply the missing native $U$ carrier. |
| Is actuality constructed? | No. The honest outcome is unconstructed. |
| May later dimension failure retune this law? | No. It rejects the later coordinate; changing a frozen seed or prior creates a new law requiring new authority. |

## 8. Theorem-by-theorem physical audit

1. **Theorem 1:** mathematically sound. It constructs a normalized discrete
   orbit law. “Physical” means the declared typed-history orbit, not an actual
   history and not a uniquely selected law.
2. **Theorem 2:** mathematically sound. Uniform deletion is sampling
   consistency, not dynamics, duration, causal growth, or a physical erasure
   operation.
3. **Theorem 3:** sound for any fully specified displayed packet under the
   wreath-product action, but not established over a determined complete
   experiment object. Its intervention probabilities also require the hidden
   directed structure of FATAL-1.
4. **Theorem 4:** every displayed signed arithmetic control is correct under
   that structural model. The response is neither geometry nor gravity. The
   promoted physical coordinate is blocked because the complete experiment
   referent is not constructed at the frozen no-causal-order scope.
5. **Theorem 5:** sound exactly for the licensed finite-word grammar. It is a
   relative stable-record theorem; excluding the eraser is part of its scope,
   not a theorem that all physical futures preserve records.
6. **Theorem 6:** the first three cells are supported. The NO/NO cell is not:
   its $B$ carrier is proposed after mode $U$ was defined to contain no
   intermediate variable. Therefore the full independence-square theorem and
   native-nondivision coordinate do not survive.

## 9. Product outcome vector and prerequisite audit

```text
referent    P13B-POINT-FREE-HISTORY-REFERENT-CONSTRUCTED
law         P13B-ONE-WHOLE-HISTORY-GAMMA-CONSTRUCTED
experiment  P13B-EXPERIMENT-PRESENTATION-ONLY
record      P13B-GRAMMAR-STABLE-RECORD-CONSTRUCTED
division    P13B-COMPLETE-DIVISION-FRONTIERS-CONSTRUCTED
nondivision P13B-NONDIVISION-UNPROVEN
size        P13B-VARYING-SIZE-COVARIANT-FAMILY-CONSTRUCTED
response    P13B-RECIPROCAL-RESPONSE-UNCONSTRUCTED
actuality   P13B-ACTUALIZATION-UNCONSTRUCTED
```

Prerequisite accounting:

- the history referent consumes the complete typed atom grammar, bond
  endpoints, wreath action, and orbit pushforward; those survive;
- the law consumes local, bond, orbit, and cardinality normalization; those
  survive;
- the experiment coordinate requires determined `Exp`/`Read` objects,
  complete contexts, and representation-independent same-law intervention;
  those fail Findings 1--2;
- the record coordinate consumes only the typed sectors and all words in the
  explicitly licensed grammar; those survive at that relative scope;
- the positive division coordinate consumes complete $R/D$ boundary data,
  future sufficiency, and positive normalized $B$ continuation; those survive
  independently of the failed $U$ cut;
- native nondivision consumes a native incomplete frontier plus uniqueness
  and nonpositivity of its restart candidate; only the last two survive;
- varying size consumes the one uniform endpoint rule, finite normalization,
  covariance, and uniform deletion; those survive;
- reciprocal physical response consumes both the signed arithmetic and the
  complete experiment referent; the arithmetic survives but the referent does
  not, so the positive coordinate is not earned; and
- actuality has no positive prerequisites because the paper honestly leaves
  selection unconstructed.

## 10. Final disposition

**REJECT.** The exact normalized orbit law is a real surviving mathematical
result, but the frozen paper does not answer its own physical review question.
Its `do` semantics either imports local causal chronology or is
representation-dependent; its complete experiment action is not determined;
and its negative matrix is attached to a non-native proposed carrier. These
defects move promoted experiment, response, nondivision, and independence-
square outcomes. They cannot be repaired by a clarification that leaves the
experiment interface and physical ontology unchanged.

This report is complete, implementation-blind, and sibling-blind. It is
frozen on delivery. No repository path other than this report was edited.
