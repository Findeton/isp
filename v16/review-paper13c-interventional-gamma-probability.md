# Independent probability review of Paper 13C

Date: 2026-08-20

Seat: probability, global evaluation, query/division, and nondivision

Status: **REJECT / SEMANTIC TYPE DEFECT / NO IMPLEMENTATION REVIEWED**

## 1. Frozen corpus authentication and blindness

I reviewed only the following frozen mathematical corpus and the governing
protocol. I did not inspect a sibling Paper 13C report, a Paper 13B review, a
repository evaluator, a fixture, or prospective Rust source.

| artifact | commit | independently reproduced SHA-256 |
|---|---|---|
| physics pin | `9acac0c` | `6f6acdfdc3065e7376eabb118adcf9c9b09cc89770f3616d31927366e7ab4c4f` |
| mathematical paper | `562f623` | `51c16c5bf85bb7dd0db44e3477233a6f331a0efe01f306600379165fcf932bed` |
| construction note | `562f623` | `c93e0ca95ba3bf75601a7dd1d258167f545fb60c733cdff6ad1d7e1b5ffc2a7f` |
| hostile-review protocol | `6bae696` | `392a6d3497e3ea2b6e7116d462da35cbec8c8445f210e7943785d01e114eea64` |

The authenticated sizes were respectively 464 LF lines / 15,629 bytes, 946
LF lines / 31,376 bytes, 104 LF lines / 3,858 bytes, and 285 LF lines /
11,396 bytes.

## 2. Verdict and first decisive counterexample

**Verdict: REJECT.**

The probability evaluator, native-cut obstruction, and positive queried
divisions reconstruct. The first decisive semantic counterexample is instead
inside the mathematical object used to claim record stability.

For one occurrence, take a legal recorded endpoint value with

$$
h=0,\qquad t=0.
$$

Section 3 defines every legal value of $2_n^r$ to obey $t_i=h_i$ and says that
no other field is legal on the boundary. Section 14 nevertheless declares
$F_t$ to toggle $t$ while leaving the record unchanged and calls it an exact
bijection in the licensed future grammar. It sends the legal value above to

$$
h=0,\qquad t=1,
$$

which is not a value of $2_1^r$. Therefore $F_t$ is not a typed bijection on
the declared recorded target space. Its projector equation is not a
well-typed equation between the frozen boundary spaces, and words containing
$F_t$ do not establish the claimed stability theorem.

This is not an implementation defect. Repair requires changing either a
boundary value set or a future generator, both of which the no-retuning rule
identifies as changes to the mathematics.

There is a second independent interface defect. The many-to-one map $E_r$ is
called an “admitted eraser control,” but it is not an arrow of $mathsf P_n$ or
$\mathsf{Exec}_n$, not a mechanism generator, and not an experiment evaluated
by $\mathbf\Gamma$. It has no declared source/target boundary packet, reader
transport, or executable probability law. Thus the frozen packet does not
contain the pinned true eraser/reset **experiment**. Adding one would again
change the experiment category.

The first defect alone rejects the stable-record coordinate. The second also
prevents the advertised experiment interface from being complete relative to
the pin. Neither finding changes the sound probability results recorded below.

## 3. Exact probability reconstruction

### 3.1 Threshold kernels

For $\beta$, 9 of the 25 seeds retain the input and 16 flip it. With columns
indexed by input and rows by output,

$$
B=\frac1{25}
\begin{pmatrix}9&16\\16&9\end{pmatrix}.
$$

For $\kappa$, the integer $25u_1+u_2$ ranges uniformly over $[625]$; 49
values retain the input and 576 flip it. Hence

$$
C=\frac1{625}
\begin{pmatrix}49&576\\576&49\end{pmatrix}.
$$

Two independent $\beta$ steps retain by either two retentions or two flips,
so

$$
B^2=\frac1{625}
\begin{pmatrix}
9^2+16^2&2(9)(16)\\
2(9)(16)&9^2+16^2
\end{pmatrix}
=\frac1{625}
\begin{pmatrix}337&288\\288&337\end{pmatrix}.
$$

Since $\det B=-7/25$,

$$
B^{-1}=\frac17
\begin{pmatrix}-9&16\\16&-9\end{pmatrix},
$$

and direct multiplication gives

$$
CB^{-1}=\frac1{175}
\begin{pmatrix}351&-176\\-176&351\end{pmatrix}.
$$

The columns of the last matrix sum to one, but it is not positive.

### 3.2 Boundary fields and path laws

The reconstructed boundary carriers are:

- $0_n$: $((q_{0i},h_i,c_i,e_i^0))_i$;
- $1_n^0$: $((m_i,h_i,a_i))_i$;
- $1_n^r$: $((m_i,r_i,h_i,a_i))_i$, with $r_i=m_i$ on the generated path;
- $2_n^0$: $((q_{2i},t_i,a_i))_i$ and every generated $\ell_{ij}$, with
  $t_i=h_i$;
- $2_n^r$: the preceding endpoint fields plus $(r_i)_i$.

The relational packet is the frozen 11-tuple
$a_i=(x_i,y_i,\epsilon_i,x'_i,y'_i,e'_i,z_{Xi},z_{Yi},u_{Xi},u_{Yi},d_i)$
with $d_i=e'_i$. A complete path history contains only its genuinely traversed
boundaries. In particular, $U$ has no $B_1$ value.

The nonidentity path normal forms are exactly

$$
U,\ Q^0,\ Q^r,\ D,\ R_c,\ D\circ Q^0,\ R_c\circ Q^r,
$$

with the typed identities. A mechanism normal form is the pair of partial
maps $(J_0,J_1)$, source writes preceding mediator writes, distinct slots
commuting, and repeated writes reduced to the last value. Boundary mismatch,
an unavailable stage, a reversed-stage word, a generic mode write, and an
unlisted slot have no normal form and refuse.

For a fixed source process bit $q_0$ the direct laws are:

$$
U:\ q_2\sim C(\cdot\mid q_0),
$$

$$
Q^0:\ m\sim B(\cdot\mid q_0),
\qquad
Q^r:\ (m,r)\text{ with }m\sim B(\cdot\mid q_0),\ r=m,
$$

and at an exact supplied $B_1$ value,

$$
D:\ q_2\sim B(\cdot\mid m),
\qquad
R_c:\ q_2\sim B(\cdot\mid m),\ r\text{ carried}.
$$

The composites therefore have joint law

$$
P(m,q_2\mid q_0)=B_{mq_0}B_{q_2m},
$$

with $r=m$ added in the recording case.

### 3.3 Context and global normalization

Every consistent source cylinder fixes some subset of finitely many fair public
bits. Its mass is a positive power of $1/2$, so conditional normalization is
unique. All unfixed public bits retain their normalized conditional product
law. The $\eta$ coins have masses $16/25,9/25$; all transition and pair coins
are uniform finite laws. Later-boundary packets instead supply an exact legal
boundary value and draw only the declared fresh coins. Thus every actually
defined evaluator case is a deterministic pushforward of a normalized finite
law.

Stabilizer orbits partition each experiment fiber, so summing labeled masses
over those cells preserves fixed-$n$ normalization. Finally

$$
\sum_{n=0}^{\infty}2^{-(n+1)}=1,
$$

which proves grand observational normalization.

As an orbit check, at $n=1$ the unmarked discrete-reader experiment is fixed
by the $X/Y$ swap. A history whose complete $X$- and $Y$-typed fields agree is
a one-element stabilizer orbit; an otherwise legal asymmetric history has a
two-element orbit and receives the sum of both equal labeled masses. By
contrast, a fully transported marked-$X$ experiment has trivial stabilizer
when no additional symmetry fixes its mark, so its representative-fiber
outcome orbit is a singleton. These examples reproduce both nontrivial and
trivial stabilizer cases without representative-mass substitution.

Deleting one occurrence and its public/private occurrence factors, every
traversed field, and all incident pair seeds leaves exactly the size-$(n-1)$
product law. Two auxiliary extension orders generate the same set of iid
occurrence seeds and unordered pair seeds. This reconstructs the stated
unmarked projectivity and extension-order agreement. It does not turn
cardinality into time or volume.

## 4. Complete direct/cut reconstruction

Fix a complete source value and a common exterior context. Let $\mu(a\mid z_0)$
be the relational-packet law generated before the process query. For the
nonrecording queried composite, direct evaluation gives

$$
\mu(a\mid z_0)B_{mq_0}B_{q_2m}
\mathbf 1_{a_{\rm out}=a}\mathbf 1_{t=h}
\prod_{i<j}P(\ell_{ij}\mid d_i,d_j).
$$

The $Q^0$ kernel produces the first three factors through the frontier, and
the standalone $D$ kernel copies $(h,a)$ and uses fresh independent $u_2$ and
$v_{ij}$ for precisely the remaining factors. Summing over the exact
$1_n^0$ values therefore reproduces every complete target-history mass, not
only the $q_2$ marginal. The $Q^r/R_c$ calculation is identical with the
additional indicators $r=m$ and exact record transport. This establishes the
two positive division claims independently of a factorization of $U$.

Conversely, for $U$ the relational distribution is independent of $q_0$ once
the common public exterior is fixed. Even if a proposed positive continuation
were allowed to inspect the entire relational packet at $B_1$, averaging that
continuation over its $q_0$-independent distribution would yield a positive
two-state kernel $\bar K(q_2\mid m)$ satisfying $C=\bar K B$. The unique
candidate is the negative matrix above. Thus no more elaborate complete
continuation can evade the marginal obstruction.

For $n>0$, $B^{\otimes n}$ is invertible and the only candidate after the same
averaging is

$$
K_n=C^{\otimes n}(B^{\otimes n})^{-1}
=(CB^{-1})^{\otimes n}.
$$

It has a negative entry obtained from one $-176/175$ factor and positive
$351/175$ factors on all other coordinates. This proves nondivision for every
nonempty size. The proof explicitly does not exclude $C=CI=IC$, the $n=0$
unit, or a positive restart on an enlarged carrier.

## 5. Mandatory attacks H18--H30

| attack | result | reconstruction |
|---|---|---|
| H18 input-history smuggling | PASS | Carrying $(m,q_0)$, a seed, or a path identifier changes the declared carrier. A positive restart then says nothing about the frozen $m$ cut. |
| H19 cut-relative nondivision | PASS | The exact unique candidates are $CB^{-1}$ and $(CB^{-1})^{\otimes n}$; each nonempty case is nonpositive. Identity carriers, $n=0$, and enlargement remain nonkills. |
| H20 exterior averaging | PASS | Conditioning on any common assignment of $h,c,e^0$ changes neither $B$ nor $C$ because the transition seeds are private and independent. The relational-packet average also remains independent of $q_0$. |
| H21 query/unqueried confusion | PASS | $U$ bypasses $B_1$ and gives $C$; both completed query paths give $B^2$. No generated $m$ belongs to a $U$ history. |
| H22 marginal-only division | PASS | Section 4 above reconstructs equality on copied relational packets and $h$, deterministic $t$, carried records, and every endpoint bond. |
| H23 record implies division | PASS as an insufficiency test; record premise not earned | Same $r$ with $h=0$ and $h=1$ gives different deterministic $t$. Omitting relational data additionally changes future bond profiles. The record-only frontier is not sufficient. The frozen grammar defect prevents certifying its stability. |
| H24 division implies record | PASS | Exact $(m,h,a)$ is sufficient for all fresh $u_2,v$ futures on $D\circ Q^0$ and contains no record register. |
| H25 reversible swap versus erasure | **FAIL** | The record-label swap itself preserves transported sectors, and a total reset would erase them. But $F_t$ is not a typed future bijection, and $E_r$ is not an admitted executable experiment. The advertised exact grammar/control packet is therefore not constructed. |
| H26 conditioning as intervention | PASS | The explicit calculation in Section 6 gives $337/625$ observationally and $1/2$ under `set(X,1)`. |
| H27 reader cancellation | PASS | Changing $E$ complements both $(x',y')$ while preserving their parity. The parity partition is blind, whereas the discrete pair reader separates the outcomes. |
| H28 mediation/directness | PASS | Without override, $z_Y=\epsilon\oplus x$ and the total $X$ response is one at fixed $E$. With $E'$ held fixed, $z_Y=y\oplus E'$ and the residual is zero. The first is not renamed a direct effect. |
| H29 context reversal | PASS | For `set(X,1)` minus `set(X,0)`, the $u_X=1$ coordinate is $+1$ at $c=0$ and $-1$ at $c=1$. The tensor retains both. |
| H30 bond response sign | PASS with a prose qualification | At fixed neighbor color, toggling $d_i$ takes equal to unequal or vice versa, giving respectively $+7/25$ and $-7/25$. An unconditioned bond marginal need not have magnitude $7/25$; the full reader/context tensor still contains the stated response. |

## 6. Response and reader reconstruction

At least the following complete-reader coordinates were independently checked.

1. At fixed $Y,E$, changing $X$ complements
   $e'=E\oplus X\oplus Y$. The discrete $e'$ reader has total-variation
   response one.
2. At fixed $X,Y$, changing $E$ complements both
   $(x',y')=(X\oplus E,Y\oplus E)$. The discrete pair reader has response one,
   whereas its parity coarsening has response zero.
3. At fixed $E$, $z_Y=E\oplus X$ without a mediator override, giving total
   response one. Under a fixed `set(E',a)`, $z_Y=y\oplus a$ and the residual
   response to $X$ is zero.
4. The complete $u_X$ reader gives signed responses $+1$ and $-1$ in the two
   declared $c$ contexts.
5. With a neighbor endpoint color fixed by the base program, the joint
   color--bond reader gives signed bond responses $\pm7/25$.

The common-cause control follows directly from

$$
P(y=x)=\left(\frac{16}{25}\right)^2
       +\left(\frac9{25}\right)^2
=\frac{337}{625}.
$$

Because $x$ is fair, this is $P(y=1\mid x=1)$. Under `set(X,1)`, the untouched
$Y=c\oplus\eta_Y$ remains fair, so its corresponding probability is $1/2$.
This confirms that observational postselection is not the mechanism
intervention.

The sentence in §15.1 that “every incident bond probability changes” by
$7/25$ is too broad if “bond probability” means the unconditional bond
marginal. For example, a fair unobserved neighboring color makes equality and
inequality equiprobable and the marginal response vanishes. The exact
$\pm7/25$ statement holds conditional on/fixed at the neighbor color or in the
appropriate joint complete-reader coordinates. Narrowing that sentence would
be a permitted prose correction because the frozen evaluator and full tensor
do not move.

## 7. Independent mathematical countermodels

These countermodels were constructed independently from the frozen evaluator;
none defines or repairs the law.

### C1 — incomplete exterior masquerading as a frontier

Retain only $m$ (or only $r$) at the cut and omit $h,a$. Choose two
positive-probability pasts with the same retained bit, opposite $h$, and, if
desired, different endpoint colors. The future deterministic field $t=h$ and
the bond profile distinguish the pasts. The reduced frontier is not
future-sufficient even though it can be normalized.

### C2 — normalized erasing reset

On a binary record define

$$
E=\begin{pmatrix}1&1\\0&0\end{pmatrix}.
$$

It is positive and column-normalized, but both input sectors have the same
output, so no transported reader recovers them. Normalization is not record
stability. This also shows why the missing typed $E_r$ experiment cannot be
replaced by a verbal reference to an erasing map.

### C3 — postselection posed as an intervention

Define a counterfeit `set(X,1)` by restricting the observational measure to
$X=1$. It predicts $P(Y=1)=337/625$. The frozen mechanism write predicts
$1/2$. The two normalized measures differ, so postselection cannot supply the
executable law.

### C4 — positive enlarged-state restart

Enlarge the native carrier from $m$ to $(m,q_0)$ and set

$$
K_+(q_2\mid m,q_0)=C_{q_2q_0}.
$$

This is positive and normalized and exactly reconstructs $C$ after the first
leg, but only because the input was retained. It is a clean enlarged-carrier
nonkill, not a factorization through the frozen $B_1$ process field.

### C5 — coarse-reader false spectator

Use the parity partition of $(x',y')$. The $E$ intervention has exactly zero
pushforward response although the discrete reader has disjoint outcomes. A
single coarse zero cannot be promoted to absence of physical response.

### C6 — bond marginal cancellation

Let the unobserved neighbor color be fair and independent of the toggled
endpoint. Equal and unequal colors each occur with probability $1/2$, so the
bond marginal is $(9+16)/50=1/2$ before and after the toggle. The joint
color--bond law still changes with conditional signs $\pm7/25$. This is a
countermodel to scalarizing the complete response tensor, not to the frozen
response constructor.

## 8. Record/division square and future sufficiency

The two **division** statements reconstruct:

- complete $1_n^0$ on $D\circ Q^0$ is a positive sufficient frontier without
  a record; and
- complete $1_n^r$ on $R_c\circ Q^r$ is a positive sufficient frontier with a
  carried record field.

The two **nondivision** statements also reconstruct:

- the record-only projection is future-insufficient; and
- $U$ cannot divide through the native nonempty $B_1$ query carrier.

However, the rows labelled “stable record = yes” are not established by the
frozen theorem because the licensed future grammar is not a category of typed
bijections. Hence the advertised four-cell *stable-record/complete-division*
square is not earned even though its division axis is mathematically sound.

## 9. Product vector and permanent walls

The full reviewed product vector is:

```text
referent    P13C-POINT-FREE-EXECUTABLE-GAMMA-CONSTRUCTED
law         NO POSITIVE PREREGISTERED RUNG EARNED:
            normalized executable sublaw, but the pinned eraser experiment is absent
experiment  P13C-EXPERIMENT-CATEGORY-UNDEFINED
nondivision P13C-NATIVE-B1-CUT-NONDIVISIBLE
record      P13C-STABLE-RECORD-UNCONSTRUCTED
division    P13C-COMPLETE-DIVISION-FRONTIERS-CONSTRUCTED
size        P13C-VARYING-SIZE-COVARIANT-FAMILY-CONSTRUCTED
response    P13C-RECIPROCAL-RELATIONAL-RESPONSE-CONSTRUCTED
actuality   P13C-ACTUALIZATION-UNCONSTRUCTED
```

The experiment demotion is narrow: the closed evaluator is total and
normalized on the experiment packets it actually defines, but the paper also
calls an untyped, unevaluated reset “admitted.” The pin makes completeness of
that interface part of the coordinate, so the positive category/law rungs
cannot be awarded on these frozen bytes.

Nothing reviewed here supplies an actual history, chronology, causal order,
signal cone, dimension, signature, topology, volume, duration, scale, metric,
connection, curvature, stress tensor, energy, entropy, gravity, GR, continuum
limit, QFT, particle ontology, or phenomenology. The response result that
survives is relational and operational only.

## 10. Final disposition

The decisive findings are semantic and occur before Rust. They do not concern
Python mutability, ownership, serialization, or any other implementation
choice. The native indivisibility and queried-division physics are not attacked
by them. Nevertheless, terminal mathematical acceptance of the full Paper 13C
packet is not justified because its stable-future/eraser interface is not the
typed executable object it claims to be.
