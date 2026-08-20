# Paper 13B mathematical hostile review — probability and intervention

Date: 2026-08-20

Status: **COMPLETE INDEPENDENT SEMANTIC REPORT / FROZEN ON DELIVERY**

Lens: probability, intervention, readers, records, divisions, and native
nondivision.

Verdict: **ACCEPT**

## 1. Corpus authentication and independence

I read the frozen review protocol before inspecting the scientific corpus.
Its SHA-256 was

```text
034fbe56a79a91860812bfbe4322e635a4a579f79f2b9b135877db2536e6a409
```

The three reviewed files authenticated byte-for-byte as follows:

| artifact | commit resolved during review | required and observed SHA-256 |
|---|---|---|
| physics pin | `f35c28fcb7a39775ffe47af352d563f9a37d0d44` | `df2c60be816e2aaf5261f954d6e1d12142ad528f572f7c77c1ff5a91464b4f47` |
| mathematical paper | `2ef0f26f32cbf5f15d1a304221b17e9eb4ed9c9c` | `5f55d1249e68e9b019790dda52254f819b68917637752cc32f0580ea07f7ff18` |
| construction note | `2ef0f26f32cbf5f15d1a304221b17e9eb4ed9c9c` | `ad13c0ba07110f608047a48a7b3cf921dac66c4beb4e857b000dc7d127c8f9f7` |

I did not read, inspect, search, diff, or otherwise use either sibling review.
I imported no earlier Paper 13/14 law, evaluator, receipt, review, or candidate
law. The derivations below are from the three authenticated artifacts. I used
no repository evaluator and performed no implementation audit.

## 2. Executive result and first decisive counterexample

**First decisive semantic counterexample: none.**

I tried all assigned attacks H12--H24, reconstructed every common item in
protocol section 5, and added six explicit mathematical countermodels. The
countermodels kill the forbidden weakened constructions but not the frozen
one. The probability mass function is normalized on every labeled finite
size and on the countable orbit space; the intervention contrasts are
truncated evaluations of the one fixed factor law rather than observational
conditionals; the response tensors have the stated entries; the record and
division examples fill all four cases; and invertibility of the declared
one-step carrier forces a unique restart candidate with negative entries.

The verdict is therefore `ACCEPT`, not `ACCEPT-WITH-FIXES`: I found no
mathematical probability, definition, parameter, outcome, or promoted
coordinate that must move.

## 3. Exact seed reconstruction

Squaring the declared rotation gives

$$
R^2=
\frac1{25}
\begin{pmatrix}
-7&-24\\
24&-7
\end{pmatrix}.
$$

Entrywise squared moduli therefore give

$$
B=\frac1{25}
\begin{pmatrix}
9&16\\
16&9
\end{pmatrix},
\qquad
C=\frac1{625}
\begin{pmatrix}
49&576\\
576&49
\end{pmatrix}.
$$

Direct multiplication gives

$$
B^2=\frac1{625}
\begin{pmatrix}
337&288\\
288&337
\end{pmatrix}.
$$

The determinant of $B$ is $-7/25$, so

$$
B^{-1}=\frac17
\begin{pmatrix}
-9&16\\
16&-9
\end{pmatrix}.
$$

Finally,

$$
CB^{-1}=\frac1{175}
\begin{pmatrix}
351&-176\\
-176&351
\end{pmatrix}.
$$

Every column of $B,C,$ and $B^2$ sums to one. Every column of $CB^{-1}$
also sums to one, but each has a negative entry. Thus the obstruction is
positivity, not normalization.

## 4. Reconstruction of the complete finite law

Let

$$
s(0)=\frac{16}{25},\qquad s(1)=\frac9{25}.
$$

The primitive source tuple is

$$
(q_0,h,c,e,\eta_X,\eta_Y,w),
$$

with the first four bits fair, the two noises independently distributed by
$s$, and $w$ uniform on $\{U,R,D\}$. The Boolean outputs are fixed functions:

$$
x=c\oplus\eta_X,\quad y=c\oplus\eta_Y,
$$

$$
x'=x\oplus e,\quad y'=y\oplus e,\quad
e'=e\oplus x\oplus y,
$$

$$
z_X=e\oplus y,\quad z_Y=e\oplus x,\quad
u_X=x\oplus c,\quad u_Y=y\oplus c,
$$

and $t=h$. With deterministic consistency indicators suppressed, the three
mode-specific atom masses are

$$
\widetilde\mu_U(a)=
\frac1{48}s(\eta_X)s(\eta_Y)C_{q_2q_0},
$$

$$
\widetilde\mu_R(a)=
\frac1{48}s(\eta_X)s(\eta_Y)
B_{mq_0}B_{q_2m}\,\mathbf1\{r=m\},
$$

$$
\widetilde\mu_D(a)=
\frac1{48}s(\eta_X)s(\eta_Y)
B_{mq_0}B_{q_2m}.
$$

Here the typed disjoint union matters: $m,r$ are absent in $U$, $r$ is
present and equals $m$ in $R$, and $m$ is present but $r$ absent in $D$.
There are 128 positive labeled atoms in mode $U$ and 256 in each of modes
$R,D$, hence 640 positive labeled atoms in the typed disjoint union. These
counts are consequences, not normalization assumptions.

### 4.1 Explicit local normalization at fixed source context

Fix $q_0,h,c,e$.

For mode $U$,

$$
\sum_{\eta_X,\eta_Y,q_2}
s(\eta_X)s(\eta_Y)C_{q_2q_0}
=1\cdot1\cdot1=1.
$$

For mode $R$,

$$
\sum_{\eta_X,\eta_Y,m,q_2,r}
s(\eta_X)s(\eta_Y)B_{mq_0}B_{q_2m}
\mathbf1\{r=m\}=1.
$$

For mode $D$, the same calculation without the $r$ sum gives one. Restoring
the four fair source bits gives total one conditional on each mode; restoring
the mode factor gives mass $1/3$ per mode and total local mass one. This also
shows that the modes are values of one normalized sampled field, not three
post-inspection laws.

### 4.2 Boolean invertibility and internal-swap invariance

The advertised inverse is correct:

$$
e=e'\oplus x'\oplus y',\qquad
x=x'\oplus e,\qquad y=y'\oplus e.
$$

Substitution recovers each input, so the core is bijective. Exchanging
$X\leftrightarrow Y$ swaps the two identically distributed noise variables
and every ordered pair of $X/Y$-typed fields, while fixing $e,e'$ and every
process field. All primitive masses and all deterministic equations are
unchanged. Thus $\widetilde\mu(a)=\widetilde\mu(\tau a)$.

An atom is fixed by $\tau$ exactly when $\eta_X=\eta_Y$ (equivalently
$x=y$, after which all derived paired fields agree). Such a singleton orbit
has mass $\widetilde\mu(a)$. If $\eta_X\ne\eta_Y$, its two-element orbit has
mass $2\widetilde\mu(a)$. It is incorrect to double the fixed point or to use
only one member of the paired orbit.

### 4.3 Bond law and exact two-atom normalization

The endpoint color $d=e'$ is $X/Y$-swap invariant. For one bond,

| endpoint relation | $P(\ell=0)$ | $P(\ell=1)$ | sum |
|---|---:|---:|---:|
| $d_i=d_j$ | $16/25$ | $9/25$ | $1$ |
| $d_i\ne d_j$ | $9/25$ | $16/25$ | $1$ |

Thus the bond kernel is normalized for each fixed endpoint pair, not merely
after averaging colors. Since $e$ is fair, each $d=e\oplus x\oplus y$ is
also fair and the unconditional one-bond success probability is $1/2$; this
last marginal is not used in the conditional proof.

For fixed $n$, summing every bond bit first yields one for every atom tuple,
then summing the iid atom tuple yields one. Explicitly:

| $n$ | bonds | labeled normalization |
|---:|---:|---|
| 0 | 0 | the empty product is $1$ |
| 1 | 0 | $\sum_a\widetilde\mu(a)=1$ |
| 2 | 1 | $\sum_{a,b}\widetilde\mu(a)\widetilde\mu(b)[(1-p_{ab})+p_{ab}]=1$ |
| 3 | 3 | each of the three conditional bond sums is $1$, then $(\sum_a\widetilde\mu(a))^3=1$ |

The same factorization proves normalization for every finite $n$.

## 5. Orbit pushforward, automorphisms, and varying size

Here are two explicit orbit calculations. Define the non-fixed $U$ atom $a$
by

```text
q0=h=c=e=0, eta_X=0, eta_Y=1, w=U, q2=0.
```

Its derived tuple has $x=0,y=1,e'=1$, and

$$
\widetilde\mu(a)=\frac{147}{390625}
=\widetilde\mu(\tau a).
$$

Let $H_{\rm aut}$ consist of two copies of $a$ with their bond equal to one.
The group $G_1^2\rtimes S_2$ has order eight. Atom interchange fixes this
repeated-atom bonded history, while neither internal swap fixes $a$; hence
the stabilizer has order two and the orbit has four distinct labeled
members. Its pushforward mass is

$$
\Gamma_2([H_{\rm aut}])
=4\left(\frac{147}{390625}\right)^2\frac9{25}.
$$

The two atom occurrences remain present even though atom interchange is an
automorphism.

For a trivial-stabilizer example, let $b$ have the same primitive relational
fields as $a$ but mode $D$, with $m=q_2=0$. Then

$$
\widetilde\mu(b)=\frac{243}{390625}.
$$

The modes prevent an atom interchange from identifying $a$ with $b$, and
neither atom is internally fixed. Thus the bonded history
$H_{\rm free}=(a,b;\ell=1)$ has trivial stabilizer and orbit size eight:

$$
\Gamma_2([H_{\rm free}])
=8\frac{147}{390625}\frac{243}{390625}\frac9{25}.
$$

These computations verify both stabilizer-sensitive pushforward cases
without replacing an orbit sum by a group-order multiplier.

For each $n$, the orbits partition the labeled sample space, so their masses
sum to one. The all-size total is then

$$
\sum_{n\ge0}2^{-(n+1)}\sum_{[H]:|H|=n}\Gamma_n([H])
=\sum_{n\ge0}2^{-(n+1)}=1.
$$

Uniform deletion is exact before quotient: deleting any uniformly selected
index from iid atoms leaves $n-1$ iid atoms, and removing incident bonds
leaves precisely the same endpoint-conditioned factors on surviving pairs.
For an orbit $O$, invariance makes every labeled representative have mass
$\Gamma_n(O)/|O|$. Consequently sampling $O$, lifting uniformly, deleting a
uniform occurrence, and requotienting is exactly the pushforward of labeled
deletion and has law $\Gamma_{n-1}$. The geometric prior is also memoryless:
conditional on $N>0$, $N-1$ again has mass $2^{-(k+1)}$ at $k$.

## 6. A marked intervention at a symmetric history

Choose the fixed atom

```text
q0=h=c=e=0, eta_X=eta_Y=0, w=U, q2=0.
```

It is fixed by $X\leftrightarrow Y$. Mark $X$, intervene with value one,
hold the other matter value and $e$ at zero, and read the complete binary
$e'$ field. The packet has a two-element marked orbit: its transported member
marks $Y$ and transports the context and reader. Both packets make $e'=1$
with probability one. The naked strings `do(X=1)` and `do(Y=1)` are not
separately functions of the unmarked history orbit; the complete marked
packet is. This is exactly the covariance the paper claims.

## 7. Full response-tensor reconstruction

The convention in this section is always `do(1)` minus `do(0)`. Outcome
orders are printed explicitly, so no total-variation scalar substitutes for
the signed tensor.

### 7.1 Matter to local relation

Put $k=e\oplus y$. Since $e'=x\oplus k$, for outcome order $(0,1)$,

$$
\Delta_{X\to E'}=
\begin{cases}
(-1,+1),&k=0,\\
(+1,-1),&k=1.
\end{cases}
$$

The entries sum to zero and total variation is one.

### 7.2 Relation to matter

For fixed $(x,y)=(0,0)$, `do(e=1)` produces $(x',y')=(1,1)$ and
`do(e=0)` produces $(0,0)$. In outcome order $(00,01,10,11)$,

$$
\Delta_{E\to(X',Y')}=(-1,0,0,+1).
$$

For general fixed $(x,y)$, the entry at $(x,y)$ is $-1$, the entry at
$(1-x,1-y)$ is $+1$, and the other two entries vanish.

### 7.3 Mediation and the direct residual

At $e=0$, $z_Y=x$, so for outcome order $(0,1)$,

$$
\Delta^{\rm total}_{X\to Z_Y}=(-1,+1).
$$

At fixed mediator $e'=s$, $z_Y=y\oplus s$ no longer depends on $x$, hence

$$
\Delta^{\rm hold\ E'}_{X\to Z_Y}=(0,0).
$$

The first is total response and the second is the direct residual. Calling
the first direct would fail H14; the paper does not do so.

### 7.4 Common cause: Bayes row versus intervention row

Bayes' rule gives the complete observational rows

$$
P(Y=(0,1)\mid X=1)=\left(\frac{288}{625},\frac{337}{625}\right),
$$

$$
P(Y=(0,1)\mid X=0)=\left(\frac{337}{625},\frac{288}{625}\right).
$$

Indeed, given $x=1$, the posterior weights of $c=1,0$ are $16/25,9/25$,
so

$$
P(y=1\mid x=1)=
\left(\frac{16}{25}\right)^2+
\left(\frac9{25}\right)^2=\frac{337}{625}.
$$

Surgical intervention on $x$ leaves the source of $y$ untouched, hence

$$
P(Y=(0,1)\mid\operatorname{do}(X=1))
=P(Y=(0,1)\mid\operatorname{do}(X=0))
=\left(\frac12,\frac12\right).
$$

Thus the intervention response tensor is $(0,0)$, while the observational
row contrast is $(-49/625,+49/625)$. The single-row observational excess
over the fair interventional value is

$$
\frac{337}{625}-\frac12=\frac{49}{1250}.
$$

### 7.5 Reader cancellation

The parity outcome is $s=x'\oplus y'=x\oplus y$, independent of $e$. For
outcome order $(s=0,s=1)$,

$$
\Delta_{E\to s}=(0,0),
$$

even though the complete pair tensor in section 7.2 is nonzero. The reader,
not the law, creates the false zero.

### 7.6 Context reversal

For $u_X=x\oplus c$, in outcome order $(0,1)$,

$$
\Delta_{X\to U_X}[c=0]=(-1,+1),
\qquad
\Delta_{X\to U_X}[c=1]=(+1,-1).
$$

Averaging the complete tensors over a fair, forgotten $c$ gives $(0,0)$.
The paper retains the exterior context and therefore retains the reversal.

### 7.7 Typed spectator

The process input $q_0$ occurs in no defining expression for $e'$. At every
fixed complete relational exterior context, for outcome order $(e'=0,e'=1)$,

$$
\Delta_{Q_0\to E'}=(0,0).
$$

This is a same-law negative control, not a separately chosen null model.

### 7.8 Incident-bond response and orientation

Fix $k=e\oplus y$ and the other endpoint color $d_j$. Under `do(x=1)` the
marked endpoint color is $1\oplus k$; under `do(x=0)` it is $k$.

If the endpoints are unequal after `do(x=1)`, then in outcome order
$(\ell=0,\ell=1)$,

$$
\Delta_{X\to\ell}=\left(-\frac7{25},+\frac7{25}\right).
$$

If they are equal after `do(x=1)`, the complete signed tensor reverses:

$$
\Delta_{X\to\ell}=\left(+\frac7{25},-\frac7{25}\right).
$$

Thus both endpoint-color cases have magnitude $7/25$ and opposite
orientation, and both tensors sum to zero.

## 8. Owned hostile attacks H12--H24

### H12 — conditioning as intervention: survives

The two Bayes rows and the two interventional rows in section 7.4 differ
exactly. In particular $337/625\ne1/2$. Postselection cannot be substituted
for `do`.

### H13 — incomplete reader false zero: survives

Parity returns $(0,0)$ while the complete four-outcome pair reader returns
the nonzero tensor $(-1,0,0,+1)$ in the displayed context.

### H14 — mediator deletion: survives

The total $X\to Z_Y$ tensor is $(-1,+1)$ at $e=0$; the residual with $e'$
independently held is $(0,0)$. The paper labels the route mediated, not
direct.

### H15 — context aggregation: survives

The two context tensors are exact negatives and average to zero. The paper
retains $c$ and the signed outcome tensor.

### H16 — bond-response orientation: survives

The two complete bond tensors are $(-7/25,+7/25)$ and its negative. The
paper's magnitude $7/25$ is correct in both endpoint-color cases.

### H17 — reversible swap miscalled erasure: survives

In the ordered record basis let

$$
S=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
P_0=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
P_1=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
$$

With $P_r^{\rm out}=P_{1-r}^{\rm in}$, direct multiplication gives
$P_r^{\rm out}S=SP_r^{\rm in}$ for both $r$. A transported reader recovers
the input record. The paper correctly classifies the swap as reversible.

### H18 — true eraser admitted: survives

The reset matrix

$$
T=\begin{pmatrix}1&1\\0&0\end{pmatrix}
$$

is column-stochastic but maps both record sectors to the same output. No
two-sector transported reader can recover the input, and $T$ is not in the
licensed grammar. The stable-record theorem therefore does not admit it.

### H19 — record implies division: survives

Take two positive-mass mode-$R$ histories with the same $m=r=0$ and all
fields equal except $h=0$ versus $h=1$. At the restricted frontier $r=0$
their future outcome distributions in order $(t=0,t=1)$ are respectively
$(1,0)$ and $(0,1)$. The stable record alone is not future-sufficient.

### H20 — division implies record: survives

At mode $D$ and frontier $Z_D$, the continuation kernel is

$$
K_D(q_2,t\mid m,h)=B_{q_2m}\mathbf1\{t=h\}.
$$

It is positive and normalized for every $(m,h)$, while the type contains no
new record register. Thus the positive frontier does not imply a record.

### H21 — native cut Markovization: survives

For the declared two-state upstream carrier, $C=KB$ forces
$K=CB^{-1}$. Its two off-diagonal entries are $-176/175$. No positive
normalized kernel exists on that carrier.

### H22 — enlargement after failure: survives

Carrying an intermediate branch and record changes the typed history and
gives the distinct recorded law $B^2$. It is a positive enlarged-carrier
control; it is not presented as a factorization of native $C$.

### H23 — mode as law menu: survives

The law first samples one typed variable $w$ with mass $1/3$ and then uses
its fixed conditional kernel. All three pieces were normalized together in
section 4.1. No theorem conditions the mode weight on a favorable later
outcome or changes it after inspection.

### H24 — parameter retuning: survives

The rotation, source priors, mode weights, endpoint probabilities, and
cardinality law occur in the definition before the outcomes. The paper
explicitly says altering any of them produces a different candidate. No
later coordinate feeds back into their selection.

## 9. Direct/cut equality, records, divisions, and uniqueness

For both modes $R$ and $D$, the process-only direct two-step conditional is

$$
P(q_2=b,t=t_0\mid q_0=a,h)=
\mathbf1\{t_0=h\}(B^2)_{ba}.
$$

Cut evaluation gives

$$
\sum_m
B_{bm}B_{ma}\mathbf1\{t_0=h\}
=\mathbf1\{t_0=h\}(B^2)_{ba}.
$$

For $R$, $r=m$ is carried as an additional deterministic frontier field; for
$D$, no $r$ field exists. The full relational and incident-bond factors are
already included in the complete frontier and therefore agree term by term
as well. This establishes direct/cut equality at both $Z_R$ and $Z_D$.

The stable-word theorem follows by composing
$P_r^{\rm out}F=FP_r^{\rm in}$ for each typed generator; the reversible swap
calculation above checks the only nontrivial transport of record labels. The
two-history $h$ witness in H19 supplies the required failure of the
record-only frontier.

The four cases are consequently exact:

| stable record | complete division | witness | calculation |
|---|---|---|---|
| yes | yes | mode $R$, $Z_R$ | record intertwining and positive $B$ continuation |
| yes | no | mode $R$, frontier $r$ only | same stable record; $h=0,1$ give disjoint $t$ profiles |
| no | yes | mode $D$, $Z_D$ | positive $B$ continuation; no $r$ type |
| no | no | mode $U$, declared $B$ carrier | no record; unique restart has negative entries |

Uniqueness in the last row is not a search result: multiplying $C=KB$ on the
right by the already computed $B^{-1}$ proves that every candidate equals
$CB^{-1}$. The negative candidate is therefore decisive on the native
two-state carrier.

## 10. Additional hostile countermodels

These are new attacks constructed for this review. Each deliberately weakens
or changes one frozen ingredient. None is silently identified with the
reviewed law.

### N1 — incomplete exterior context erases a real signed response

Discard $c$ before retaining the $X\to U_X$ tensor. Fair aggregation gives

$$
\frac12(-1,+1)+\frac12(+1,-1)=(0,0).
$$

This incomplete-context model falsely reports no response. It confirms that
the frozen tensor must retain $c$, as it does.

### N2 — a three-outcome reader merges just the responsive pair

For fixed $(x,y)=(0,1)$, toggling $e$ exchanges complete outcomes $01$ and
$10$. Define a reader with outcomes $A,B,C$ by

$$
M(01)=M(10)=A,\qquad M(00)=B,\qquad M(11)=C.
$$

Its tensor in outcome order $(A,B,C)$ is $(0,0,0)$ although the complete pair
tensor has one $-1$ and one $+1$. This is a different merge from a complete
reader and independently confirms the reader-separation requirement.

### N3 — two-sided postselection masquerading as `do`

Replace the intervention rows by the observed rows at $x=1$ and $x=0$.
Their signed contrast is

$$
\left(-\frac{49}{625},+\frac{49}{625}\right),
$$

whereas the true interventional contrast is $(0,0)$. This countermodel is
normalized and superficially uses the same variables, but changes the
experiment from truncation to postselection. The frozen definition excludes
it.

### N4 — normalized stochastic record reset with no recovery

Let

$$
Q=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix}.
$$

Both columns are probability vectors, so failure is not normalization. The
two input record sectors have identical output laws; $Q$ has rank one and no
decoder can recover $r$. This stochastic eraser is not one of the licensed
bijective generators and does not satisfy the stable-record conclusion.

### N5 — carrier-relative control for the native no-restart result

Keep the same normalized whole transition $C$ but replace the declared
upstream carrier map $B$ by the identity. Then $C=CI$ is a positive restart.
This does not refute the paper: it changes the cut interface. It demonstrates
why the earned nondivision coordinate is exactly carrier-relative and why
state/interface enlargement or replacement cannot erase the $C=KB$ result
on the frozen $B$ carrier.

### N6 — posterior mode selection after inspecting the future

Let $S$ be the event $q_2=q_0$. Its likelihood is $49/625$ in mode $U$ and
$337/625$ in each of modes $R,D$. Although the prior mode weights are all
$1/3$, postselection gives

$$
P(U\mid S)=\frac{49}{723},\qquad
P(R\mid S)=P(D\mid S)=\frac{337}{723}.
$$

Reporting these posterior weights as the law's mode weights would be a
mode-after-inspection menu. The paper keeps the primitive $1/3$ weights and
does not make this substitution.

## 11. Remaining common hostile controls

Although H12--H24 are this seat's owned attacks, the probability
reconstruction also exposes the consequences of the other common controls:

- **H1:** on the local quotient, fixed atoms have total labeled probability
  $337/625$ and non-fixed atoms $288/625$. Choosing one representative of
  every two-element orbit would give only
  $337/625+144/625=481/625$, not one. Orbit pushforward avoids this failure.
- **H2:** $H_{\rm aut}$ has two physical occurrences, stabilizer size two,
  and orbit size four. Neither one-representative collapse nor multiplication
  by all eight group elements gives its correct mass.
- **H3:** fixed atoms contribute once; paired atoms contribute the sum of two
  equal masses, as reconstructed in section 4.2.
- **H4:** the symmetric marked experiment in section 6 has a two-element
  packet orbit; neither naked marked slot descends alone.
- **H5:** failing to transport context or reader breaks the equality in
  section 6 and can produce the N1/N2 false zeros.
- **H6:** permuting tuple positions merely permutes equal iid atom factors and
  endpoint-indexed bond factors. The product and orbit mass are unchanged.
- **H7:** moving a bond without its unordered endpoint pair changes the typed
  incidence relation and is not an action of the declared group.
- **H8:** if, only at $n=4$, the equal-color bond probability is changed from
  $9/25$ to $8/25$, deletion of an unrelated atom leaves a surviving
  equal-color bond with probability $8/25$, not the $n=3$ law. Projectivity
  detects the per-size replacement.
- **H9:** labeled deletion and quotient commute by the equivariance argument
  in section 5, so the exact lower-cardinality law is recovered.
- **H10:** a pair probability keyed to the first tuple index changes under a
  transposition and therefore fails covariance. No such index occurs in the
  endpoint rule.
- **H11:** a fixed dormant carrier would add inactive labels and their
  isomorphisms to the sample space. The frozen sample space contains exactly
  $N$ occurrences and no such field.
- **H25:** no dimension, coordinate, metric, lattice, scaling target, or
  desired spacetime output occurs in any probability definition or parameter
  choice in the authenticated corpus.
- **H26:** the law normalizes possibilities only. The paper explicitly leaves
  actualization unconstructed and never promotes its examples to actuality.

## 12. Coordinate-by-coordinate prerequisite audit

| coordinate | actual prerequisites checked | result |
|---|---|---|
| point-free history referent | finite typed atoms; complete bond incidence; invariant wreath action; stabilizer-sensitive orbit sum | passes |
| one whole-history Gamma | local normalization; conditional bond normalization; orbit partition; geometric size sum | passes |
| experiment action | complete packet transport; symmetric marked-slot test; same-factor truncation; transported reader/context | passes |
| grammar-stable record | typed generator intertwiners; swap transport; finite-word composition; eraser excluded by discriminator | passes |
| complete divisions | positive normalized $B$ continuation; $h$ and relational fields included; direct/cut equality at $Z_R,Z_D$ | passes |
| native indivisible cut | declared $B$ carrier; $B$ invertible; unique $CB^{-1}$; negative entries; normalized $C$ | passes |
| varying-size family | one endpoint rule for all $n$; $n=0,1,2,3$ and general normalization; uniform-deletion projectivity; no dormant carrier | passes |
| reciprocal relational response | complete signed tensors in both directions; mediation; common cause; reader merge; context reversal; spectator; bonds | passes |
| actuality | normalization only; no selection rule or promoted sample | remains unconstructed as claimed |

No coordinate relies on actuality, chronology, dimension, geometry, metric,
or a post-review choice of a primitive probability.

## 13. Findings and full product outcome vector

### Severity-ranked findings

There is no `FATAL`, `MAJOR`, or `MINOR` semantic finding. The hostile
countermodels above are passed controls, not defects in the frozen law. No
replacement sentence is required because no claim needs narrowing or repair.

### Product outcome vector

```text
referent    P13B-POINT-FREE-HISTORY-REFERENT-CONSTRUCTED
law         P13B-ONE-WHOLE-HISTORY-GAMMA-CONSTRUCTED
experiment  P13B-POINT-FREE-EXPERIMENT-ACTION-CONSTRUCTED
record      P13B-GRAMMAR-STABLE-RECORD-CONSTRUCTED
division    P13B-COMPLETE-DIVISION-FRONTIERS-CONSTRUCTED
nondivision P13B-NATIVE-INDIVISIBLE-CUT-CONSTRUCTED
size        P13B-VARYING-SIZE-COVARIANT-FAMILY-CONSTRUCTED
response    P13B-RECIPROCAL-RELATIONAL-RESPONSE-CONSTRUCTED
actuality   P13B-ACTUALIZATION-UNCONSTRUCTED
```

## 14. Final verdict

**ACCEPT**

At the exact frozen scope, the corpus constructs one normalized discrete law
on all finite complete-history orbits, one covariant marked-experiment
semantics, the claimed response tensors, all four record/division cases, and
one native carrier with no positive restart. This acceptance does not enlarge
the paper's scope to actuality, chronology, geometry, dimension, gravity, or
uniqueness of the primitive law.

The report's ordinary SHA-256, line count, and byte count are intentionally
reported at delivery rather than embedded self-referentially in these bytes.
