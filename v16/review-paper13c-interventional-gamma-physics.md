# Paper 13C physics/ontology mathematical review

Date: 2026-08-20

Seat: **physics/ontology, intervention identity, response, and scope**

Verdict: **REJECT**

Scope: semantic mathematics only. No implementation, evaluator, fixture, or
prospective Rust issue was inspected or used.

## 1. Corpus authentication and blindness

I authenticated the complete frozen corpus before review.

| artifact | commit | SHA-256 | authenticated size |
|---|---:|---|---:|
| physics pin | `9acac0c` | `6f6acdfdc3065e7376eabb118adcf9c9b09cc89770f3616d31927366e7ab4c4f` | 464 LF lines / 15,629 bytes |
| mathematical paper | `562f623` | `51c16c5bf85bb7dd0db44e3477233a6f331a0efe01f306600379165fcf932bed` | 946 LF lines / 31,376 bytes |
| construction note | `562f623` | `c93e0ca95ba3bf75601a7dd1d258167f545fb60c733cdff6ad1d7e1b5ffc2a7f` | 104 LF lines / 3,858 bytes |
| review protocol | `6bae696` | `392a6d3497e3ea2b6e7116d462da35cbec8c8445f210e7943785d01e114eea64` | 285 LF lines / 11,396 bytes |

I did not inspect or communicate with either sibling Paper 13C review. I did
not inspect a Paper 13B review or import a Paper 13B evaluator or experiment
packet.

## 2. Result in one paragraph

The frozen executable map substantially solves the Paper 13B intervention
identity problem: its mechanism programs are primitive inputs, two maps with
the same observational identity can be distinguished as different executable
laws, the query is not a supposed revelation of a value hidden in the
unqueried path, and the displayed response controls can be reconstructed from
the global evaluator. The native $B_1$ obstruction is also genuinely
cut-relative. The packet nevertheless fails terminal acceptance because its
claimed stable-future grammar is not a typed action on its declared histories.
The generator $F_t$ toggles $t$ while the boundary grammar requires $t=h$;
hence it sends an admitted recorded history outside `CompleteHist`. A second
problem is that the many-to-one reset is called an admitted eraser control but
is not a generator of either the experiment category or a separately typed
future category on which $\mathbf\Gamma$ is evaluated. The advertised stable
record theorem therefore is not a theorem of the frozen packet. Repair would
change a future generator, a boundary type, or the experiment catalogue, so it
is not an allowed proof/prose fix and Rust remains unauthorized.

## 3. First decisive semantic counterexample

Take $n=1$ and any positive-probability recorded history of
$R_c\circ Q^r$ with

$$
h=0,\qquad t=h=0.
$$

Choose either positive record sector. Section 3 declares that every legal
$2_1^r$ boundary value satisfies $t=h$. Section 14 declares $F_t$ to toggle
$t$ and calls it an exact bijection in the entire licensed future grammar. It
does not toggle or transport $h$. Consequently

$$
F_t:(h,t)=(0,0)\longmapsto(0,1),
$$

and the image is not a legal $2_1^r$ value. It is not a history of any other
declared boundary type either. Thus $F_t$ is not an endomorphism, bijection,
or typed future morphism on the claimed history space. Products containing
$F_t$ and the displayed projector intertwining equation are undefined.

The failure is not an ownership, mutability, serialization, or programming
defect. Possible repairs include toggling $h$ and every historical copy with
$t$, removing $F_t$, weakening $t=h$, or adding a new future boundary type.
Each changes frozen mathematical data. The protocol therefore requires
rejection of the stable-record coordinate rather than reviewer repair.

There is an additional boundary-specific ambiguity. At $1_n^r$ the grammar
requires $r=m$. If $F_r$ is meant to act on that recorded boundary, toggling
$r$ without $m$ again leaves the declared value set. If it is meant only at
$2_n^r$, that restricted source and target were not stated. This does not
replace the decisive $F_t$ counterexample; it independently confirms that
`Fut` lacks exact typing.

Finally, $E_r:(r_i)_i\mapsto(0)_i$ is named an admitted eraser control but is
absent from $\mathsf P_n$, $\mathsf{Exec}_n$, the mechanism-generator list,
and the licensed future grammar. The paper gives no closed experiment packet
or $\mathbf\Gamma(E_r)$ evaluation. As an external map it demonstrates what
an eraser would do, but it is not the true eraser/reset experiment required by
the pin.

## 4. Independent common reconstruction

### 4.1 Threshold laws

For fixed input bit $a$, exactly $9$ of the $25$ values of $u$ leave $a$
unchanged and $16$ flip it. For $s=25u_1+u_2$, exactly $49$ of $625$ pairs
leave $a$ unchanged and $576$ flip it. Hence

$$
B=\frac1{25}\begin{pmatrix}9&16\\16&9\end{pmatrix},
\qquad
C=\frac1{625}\begin{pmatrix}49&576\\576&49\end{pmatrix}.
$$

Independent successive $\beta$ steps give

$$
B^2=\frac1{625}
\begin{pmatrix}
9^2+16^2&2(9)(16)\\
2(9)(16)&9^2+16^2
\end{pmatrix}
=\frac1{625}\begin{pmatrix}337&288\\288&337\end{pmatrix}.
$$

Since $\det\begin{pmatrix}9&16\\16&9\end{pmatrix}=-175$,

$$
B^{-1}=\frac17\begin{pmatrix}-9&16\\16&-9\end{pmatrix},
$$

and direct multiplication gives

$$
CB^{-1}=\frac1{175}
\begin{pmatrix}351&-176\\-176&351\end{pmatrix}.
$$

The columns sum to one but the off-diagonal entries are negative.

### 4.2 Boundary fields and path-history types

The reconstructed legal fields are:

| boundary | complete value |
|---|---|
| $0_n$ | $((q_{0i},h_i,c_i,e_i^0))_i$ |
| $1_n^0$ | $((m_i,h_i,a_i))_i$ |
| $1_n^r$ | $((m_i,r_i,h_i,a_i))_i$, with $r_i=m_i$ |
| $2_n^0$ | $((q_{2i},t_i,a_i))_i,(\ell_{ij})_{i<j}$, with $t_i=h_i$ |
| $2_n^r$ | the $2_n^0$ value plus $(r_i)_i$, with $t_i=h_i$ |

Here

$$
a_i=(x_i,y_i,\epsilon_i,x'_i,y'_i,e'_i,z_{Xi},z_{Yi},u_{Xi},u_{Yi},d_i),
\qquad d_i=e'_i.
$$

$U$ histories traverse $0_n\to2_n^0$ and contain no $B_1$ field.
$Q^0$ and $Q^r$ terminate at their respective $1$ boundaries. The two
composites contain source, corresponding $1$ value, and endpoint. Standalone
$D$ and $R_c$ start from a supplied exact $1$ value. Identity paths copy the
supplied value and draw no coin.

### 4.3 Program normal forms, composition, and refusal

Process paths have the identities, five generators

$$
U,Q^0,Q^r,D,R_c,
$$

and only the nonidentity composites $D\circ Q^0$ and
$R_c\circ Q^r$. Every source/target mismatch refuses.

A mechanism word reduces uniquely to $(J_0,J_1)$: $J_0$ is a finite partial
map on the binary slots $X_i,Y_i,E_i$, and $J_1$ is a finite partial map on
$E'_i$. Source-stage writes precede mediator-stage writes, disjoint slots
commute, and the final same-slot write wins. The empty pair is identity.
Concatenation followed by normalization is associative. `set(W,a)`, a
mediator-then-source word, a generic mode write, and a mechanism write from a
later-boundary source all refuse.

Closed source conditioning is attached only after program composition.
Positive reader-cell postselection is a derived normalized restriction, not
program composition. Independently tagged tensoring has no cross-bond field;
physical fusion at size $n+m$ creates fresh cross-bond seeds and is not the
tensor product measure.

### 4.4 Seed laws and direct evaluations

At source boundaries, $q_0,h,c,e^0$ are independent fair bits;
$P(\eta_J=0)=16/25$, $P(\eta_J=1)=9/25$; every $u$ and $v$ is uniform on
$[25]$. A consistent source cylinder fixes some public bits and leaves a
finite normalized conditional product law because each cylinder atom has
positive mass. At $1$ boundaries only fresh $u_2$ and endpoint bond seeds are
drawn; endpoint identities draw none.

The path shadows for one occurrence are:

| path | stochastic process value |
|---|---|
| $U$ | $q_2=\kappa(q_0,u_1,u_2)$, kernel $C$ |
| $Q^0$ | $m=\beta(q_0,u_1)$, kernel $B$, no record |
| $Q^r$ | same $m$, with $r=m$ |
| $D$ | $q_2=\beta(m,u_2)$ from a supplied $1^0$ value |
| $R_c$ | same continuation from $1^r$, carrying $r$ |
| $D\circ Q^0$ | joint $B_{mq_0}B_{q_2m}$, endpoint $B^2$ |
| $R_c\circ Q^r$ | same joint law plus $r=m$, endpoint $B^2$ |

The direct and cut evaluations of either composite agree on complete target
histories, not only $q_2$: $h$ and $a$ are copied in the supplied complete
frontier, $t=h$, $u_2$ is fresh, and all endpoint unordered-pair seeds are
fresh with the same law. The recording continuation also copies $r$.

The relational evaluator is deterministic after source bits and noises:

$$
x=c\oplus\eta_X,\quad y=c\oplus\eta_Y,\quad
x'=x\oplus\epsilon,\quad y'=y\oplus\epsilon,
$$

unless a listed mechanism replacement applies, and

$$
e'=\epsilon\oplus x\oplus y,
\quad z_X=x\oplus e',
\quad z_Y=y\oplus e',
\quad u_X=x\oplus c,
\quad u_Y=y\oplus c.
$$

An $E'$ write replaces $e'$ before the four downstream fields are computed.
Endpoint bonds are Bernoulli $16/25$ for unequal $d=e'$ colors and $9/25$
for equal colors.

### 4.5 Covariance and two stabilizer controls

An internal $C_2$ swap exchanges $X/Y$, their noises, fields, slots, marks,
reader coordinates, and downstream typed ports, while it fixes $e'$ and the
bond color. $S_n$ transports occurrences and unordered bond endpoints.
Contexts and the whole contrast are transported with these data. Every
evaluator formula commutes with this action and the product seed law is
exchangeable.

For a nontrivial stabilizer, take $n=1$, the unmarked observational packet,
and a positive history with $x=y$, $x'=y'$, $z_X=z_Y$, and $u_X=u_Y$. The
internal swap fixes both experiment and history, so the diagonal pair has a
$C_2$ stabilizer and its orbit is not to be assigned two representative
masses. For a trivial stabilizer, mark `set(X,0)` and retain a reader probing
the $X$-typed target coordinate. The internal swap transports it to the
distinct `set(Y,0)` presentation, so the representative experiment fiber has
trivial stabilizer. These examples also show why the experiment and history
must be quotiented diagonally.

At $n=2$, an unmarked history with identical occurrence data has an $S_2$
automorphism (with its unordered bond fixed). The stabilizer-orbit sum counts
that mass once; representative multiplication by the full group order would
double count it.

### 4.6 Normalization, size, deletion, and extension order

Every fixed-size labeled law is a deterministic pushforward of a normalized
finite seed law. Stabilizer orbits partition its outcome fiber, so orbit
pushforward preserves total mass. The grand mass is normalized because

$$
\sum_{n=0}^{\infty}2^{-(n+1)}=1.
$$

For the unmarked observational family, deletion of one occurrence removes
exactly its iid occurrence factor, every traversed field, and all incident
unordered-pair factors. The surviving law is the size-$(n-1)$ law. The
restriction is equivariant, so deletion before or after quotient agrees.
Adding two labeled auxiliary occurrences in either order generates the same
two occurrence factors and the same unordered collection of old--new and
new--new pair seeds. Hence the two extension orders agree. This is an
unbounded finite-size family, not a fixed dormant carrier.

### 4.7 Native cut and record/division cells

For every fixed exterior value $(h,c,e^0)$, private process coins remain
independent. Thus the native query shadows are $B$ and the unqueried endpoint
shadow is $C$ without exterior averaging. In nonempty size $n$, $B^{\otimes
n}$ is invertible and the only proposed continuation is

$$
K_n=(CB^{-1})^{\otimes n}.
$$

An entry with exactly one off-diagonal factor and all other factors diagonal
is negative. The empty size, $C=CI=IC$, and the enlarged carrier $(m,q_0)$
are valid nonkills because they are different cuts.

The future-sufficiency/division calculations themselves give:

| frontier | record field | complete cut calculation |
|---|---:|---:|
| complete $1^r$ in $R_c\circ Q^r$ | yes | positive $B$ continuation |
| record-only restriction | yes | fails; omitted $h$ changes $t$ |
| complete $1^0$ in $D\circ Q^0$ | no | positive $B$ continuation |
| proposed native $B_1$ in $U$ | no | fails by $CB^{-1}$ negativity |

This reconstructs the division column and establishes that record content is
neither necessary nor sufficient for division. It does **not** establish the
stable-record column, because the frozen future grammar is not a typed action
as shown in Section 3 of this report.

### 4.8 Signed response reconstruction

The law-defined coordinate is the difference of two globally evaluated
target-reader probabilities in one transported frame, indexed by every path,
base program, public context, mark set, alternative pair, reader partition,
and cell. It is not a scalar selected after inspection.

Writing $e_a=e[J;S\leftarrow a]$ and
$e_b=e[J;S\leftarrow b]$, the reconstructed complete constructor is

$$
\Delta^{p,J,K,M,\Pi}_{S;a,b}(A)
=\widetilde{\mathbf\Gamma}(e_a)
  (\operatorname{target}\in A)
-\widetilde{\mathbf\Gamma}(e_b)
  (\operatorname{target}\in A),
$$

for every legal $p,J,K,M,\Pi,S,a,b$ and every cell $A\in\Pi$, with $J$
not already writing $S$. The presentation action transports the two packets
and $A$ together. The family, including the discrete reader, is the response
object.

The displayed controls reconstruct as follows.

1. With $Y$ and $E$ fixed, toggling $X$ toggles
   $e'=\epsilon\oplus X\oplus Y$. A discrete $E'$ reader distinguishes the
   two outputs with total variation one.
2. With $X,Y$ fixed, toggling $E$ flips the complete pair $(x',y')$ and its
   discrete reader has total variation one.
3. Without an $E'$ override, $z_Y=\epsilon\oplus X$. At fixed $\epsilon$,
   the $X\to z_Y$ response is one. With $E'$ fixed by $J_1$,
   $z_Y=Y\oplus E'$ and the residual $X$ response is zero.
4. In the identity law, $x=y$ precisely when $\eta_X=\eta_Y$, so
   $P(y=1\mid x=1)=(16^2+9^2)/625=337/625$. Under `set(X,1)`, $c$ remains
   fair and therefore $P(y=1)=1/2$.
5. Toggling $E$ flips $(x',y')$ but leaves
   $x'\oplus y'=x\oplus y$. The parity reader has zero response while the
   discrete pair reader detects it.
6. For the event $u_X=1$, `set(X,1)` minus `set(X,0)` is $+1$ at $c=0$ and
   $-1$ at $c=1$. Averaging the contexts produces zero but is not a spectator
   conclusion. $q_0$ is a genuine spectator for relational outputs.
7. With the neighboring color fixed, toggling one $d_i$ changes an incident
   bond from equal to unequal or conversely, giving signed change
   $\pm(16-9)/25=\pm7/25$.

The common-cause, mediation, reader-cancellation, context-reversal, spectator,
matter-to-relation, relation-to-matter, and conditional bond controls are
therefore present in the primitive executable law.

Two sentences in the paper require nonmathematical narrowing if the packet
were otherwise accepted. Section 15.3's “total response one” holds at fixed
$E$ (or fixed $e^0$), not under every admitted context: under the tautological
context the fair $\epsilon$ averages both `set(X)` distributions to fair
$z_Y$. Likewise, Section 15.1's statement that every incident bond probability
changes by $7/25$ requires a fixed neighboring color. If the neighbor color
is fair, the marginal bond response is zero. The full tensor itself contains
both facts, so these are prose-scope overclaims rather than changes to
$\mathbf\Gamma$.

## 5. Owned mandatory attacks

### H1 — static-law refactorization: PASS

Define $\mathbf\Gamma^{\rm comp}$ to use the identical seed law, boundary
grammar, and evaluator when $J$ is empty, but to interpret every written bit
$a$ as $1-a$. Apply this covariantly to $X/Y$ and to the relation slots. It is
a normalized presentation-covariant executable map with

$$
\mathbf\Gamma^{\rm comp}(\mathbb1_{\rm obs})
=\mathbf\Gamma(\mathbb1_{\rm obs}),
$$

but its `set(X,0)` law equals the frozen law's `set(X,1)` law and is detected
by the complete $X$ or $E'$ reader in a fixed context. The two maps are
different executable laws. The frozen packet does not identify them merely
because their observational identities agree. This is the precise sense in
which making the executable interface primitive resolves, rather than
derives away, intervention nonidentifiability.

### H21 — query/unqueried confusion: PASS

$U$ evaluates $\kappa$ and its history has no $m$. $Q^0,Q^r$ evaluate
$\beta$ and introduce a typed $m$; their continuations use the second
$\beta$. Therefore query endpoint $B^2$ is a changed experiment, not a
revelation of a pre-existing intermediate value in the $C$ history.

### H22 — marginal-only division: PASS

For both queried composites, the complete frontier includes $m,h,a$ and,
when present, $r$. Conditioning on it leaves exactly fresh $u_2$ and bond
seeds. Relational packets and $h$ are copied, $t=h$, records are carried, and
bonds use the same endpoint-color rule. Thus direct/cut equality holds for
every complete target history and hence every reader, not merely for $q_2$.

### H23 — record implies division: PASS AS AN ATTACK

At $n=1$, two positive histories can have the same $r=m$ and opposite $h$;
$R_c$ then gives opposite deterministic $t=h$. At $n=2$, keep $r,h$ fixed
but change an omitted relational color $d_1$ while fixing $d_2$; the future
bond probability changes between $9/25$ and $16/25$. A record-only frontier
is therefore insufficient even before the stable-grammar defect is reached.

### H24 — division implies record: PASS

The complete $1_n^0$ value contains every copied relational and matter field
needed by $D$. Fresh coins are independent and give a normalized positive
continuation. Direct/cut equality holds, although no $r$ exists.

### H25 — reversible swap versus erasure: FAILS THE FROZEN RECORD CLAIM

Restricted to a legal $2_n^r$ record coordinate, a bijective label swap with
transported projectors preserves recoverability, while a many-to-one reset
merges the two sectors. Those algebraic controls are correct. But the claimed
*entire* future grammar contains the ill-typed $F_t$ counterexample in Section
3, and $E_r$ is not an admitted experiment morphism. Therefore the frozen
packet has not constructed the exact `Fut` and eraser experiment required for
the stable-record theorem.

### H26 — observational conditioning as intervention: PASS

The exact values are

$$
P(y=1\mid x=1)=337/625,
\qquad
P(y=1\mid\operatorname{set}(X,1))=1/2.
$$

The second is evaluated from the mechanism map. No selected chain rule enters.

### H27 — incomplete-reader cancellation: PASS

The $E$ contrast flips both $x'$ and $y'$. Its parity pushforward is identical
under both alternatives, while a discrete reader distinguishes them. The
paper retains the discrete reader and does not promote the parity zero.

### H28 — mediation and directness: PASS WITH PROSE NARROWING

At fixed $E$, the total $X\to z_Y$ response is one. Holding $E'$ fixed makes
the residual zero. The paper does not call total response direct response.
The unqualified sentence must be read contextually as explained in Section
4.8; the complete tensor itself is correct.

### H29 — context reversal and scalar averaging: PASS

The two fixed-$c$ coordinates are $+1$ and $-1$. Their fair average is zero,
but neither conditional coordinate is zero, so this is not a spectator.

### H30 — bond response sign: PASS WITH PROSE NARROWING

For fixed neighbor color, the equal and unequal contexts give opposite signs
and exact magnitude $7/25$. A marginal over a fair neighbor gives zero; the
full tensor retains both. The law passes the attack, while “every incident
bond” must be narrowed to the held-color control.

### H31 — joint-stage overpromotion: PASS

The triple $(x',y',e')$ is generated in one declared operational stage, but
the paper explicitly refuses to call it a co-onset event, chronology edge,
spacetime event, or backreaction theorem.

### H32 — selection, geometry, and actuality: PASS

The constants, alternatives, size weights, seed laws, mechanisms, and readers
are frozen rather than selected by output. Cardinality is not promoted to
volume or time. No dimension, lattice, topology, metric, clock, signal cone,
or actual history enters the evaluator, and no future retuning permission is
reserved.

## 6. Additional independent mathematical countermodels

### CM-P1 — same observational law, different mechanism map

$\mathbf\Gamma$ and $\mathbf\Gamma^{\rm comp}$ in H1 have exactly the same
identity law but opposite written-bit semantics. A complete reader detects
the difference under `set(X,0)`. This shows both why the static law was
insufficient and why the complete executable map is the appropriate referent.

### CM-P2 — same record, different future profile

Two $1_1^r$ values with identical $r=m=0$ and opposite $h$ have disjoint
$t$ readers after $R_c$. At $n=2$, identical records and $h$ but different
relational colors have different bond readers. Stable record content is not a
restartable system state.

### CM-P3 — same count, different graph

At $n=3$ and fixed equal endpoint colors, every edge is independently present
with probability $9/25$. Both the empty graph and the triangle have strictly
positive probability at the same occurrence count. Count therefore does not
determine relational graph, order, dimension, or metric.

### CM-P4 — same graph law, different executable law

Keep the entire relational and bond evaluator fixed but replace the process
endpoint rule $\kappa$ by $q_2=q_0$. The generated bond graph distribution is
identical because bonds depend only on $e'$ colors, while the process kernel
changes from $C$ to the identity. Thus even a complete graph ensemble does
not determine the executable physical law. This is a countermodel only, not
a proposed retuning of the frozen packet.

### CM-P5 — same averaged zero, opposite contextual response

For $u_X$, the two $c$ strata have signed effects $+1$ and $-1$, while the
tautological-context effect is zero. This gives an exact countermodel to the
inference “zero scalar average implies no intervention response.”

### CM-P6 — same coarse reader, different complete outcomes

The two $E$ interventions have identical parity-reader laws but exchange
every discrete $(x',y')$ value. This gives an exact countermodel to the
inference “reader agreement implies physical-history agreement.”

## 7. Full product vector

The first seven positive coordinates below describe mathematical parts that
survive this seat's attacks; they do not override the terminal `REJECT`.
`record` is demoted because the frozen future action is ill-typed.

```text
referent    P13C-POINT-FREE-EXECUTABLE-GAMMA-CONSTRUCTED
law         P13C-ONE-INTERVENTIONALLY-COMPLETE-GAMMA-CONSTRUCTED
experiment  P13C-TYPED-EXPERIMENT-CATEGORY-CONSTRUCTED
nondivision P13C-NATIVE-B1-CUT-NONDIVISIBLE
record      P13C-STABLE-RECORD-UNCONSTRUCTED
division    P13C-COMPLETE-DIVISION-FRONTIERS-CONSTRUCTED
size        P13C-VARYING-SIZE-COVARIANT-FAMILY-CONSTRUCTED
response    P13C-RECIPROCAL-RELATIONAL-RESPONSE-CONSTRUCTED
actuality   P13C-ACTUALIZATION-UNCONSTRUCTED
```

The positive response coordinate means only that nonzero covariant response
tensors exist with the reconstructed controls. It does not mean actualization,
chronology, dimension, signature, topology, volume, duration, metric,
curvature, gravity, GR, continuum physics, or QFT.

## 8. Rust gate

**Closed.** The first required repair is mathematical: make `Fut` a typed
action on declared histories and type the eraser as an experiment or withdraw
that pinned claim. Neither can be performed as a code-only conformance repair.
