# Paper 13B hostile mathematical review — groupoid/referent seat

Date: 2026-08-20

Status: **COMPLETE INDEPENDENT HOSTILE REPORT / FROZEN ON DELIVERY**

Verdict: **REJECT**

## 1. Scope, independence, and authentication

This is the groupoid/referent report required by the frozen protocol. I read
the protocol before the scientific corpus, reconstructed the mathematics by
hand, used no repository evaluator or implementation, and did not inspect
either sibling report. I did not import an older Paper 13/14 evaluator,
receipt, review, candidate law, or another reviewer's reconstruction.

The protocol authenticated as:

```text
034fbe56a79a91860812bfbe4322e635a4a579f79f2b9b135877db2536e6a409
  v16/note-paper13b-pointfree-gamma-math-review-protocol.md
```

The immutable corpus authenticated byte-for-byte both in the working tree
and at the declared Git objects:

```text
f35c28fcb7a39775ffe47af352d563f9a37d0d44
df2c60be816e2aaf5261f954d6e1d12142ad528f572f7c77c1ff5a91464b4f47
  v16/note-paper13b-pointfree-gamma-physics-pin.md

2ef0f26f32cbf5f15d1a304221b17e9eb4ed9c9
5f55d1249e68e9b019790dda52254f819b68917637752cc32f0580ea07f7ff18
  v16/paper-13b-pointfree-whole-history-gamma.md

2ef0f26f32cbf5f15d1a304221b17e9eb4ed9c9
ad13c0ba07110f608047a48a7b3cf921dac66c4beb4e857b000dc7d127c8f9f7
  v16/note-paper13b-pointfree-gamma-mathematical-construction.md
```

The first line in each pair is the full commit and the second is the ordinary
SHA-256 of the exact artifact. The working-tree and `git show` bytes produced
the same three SHA-256 values.

## 2. Executive finding and first decisive counterexample

The complete-history quotient is mathematically sound. The local fixed-point
and paired orbits, the wreath-product stabilizers, the whole-orbit
pushforward, the all-size normalization, and the quotient/deletion kernel all
survive the assigned attacks. In particular, I found no representative-mass,
automorphism-multiplicity, hidden-order, dormant-carrier, or per-size-table
defect in the frozen history law.

The first decisive semantic counterexample instead defeats the promoted
*complete experiment interface*. The paper defines a packet using a marked
intervention slot but gives no admissible-slot set. It then says that an
intervention replaces “exactly one declared structural assignment,” with
three examples rather than a definition of the domain. The mode \(w\) is a
declared structural field, and section 10 expressly says its kernels are
fixed before the mode is “sampled or intervened upon.” Take a \(U\)-atom,
mark \(A=w\), and force \(a=R\).
The frozen atom types are dependent:

- in \(U\), neither \(m\) nor \(r\) is a random variable and
  \(q_2\mid q_0\) has kernel \(C\);
- in \(R\), a new \(m\) is sampled with \(B\), \(r=m\) is written, and the
  second \(B\) step samples \(q_2\).

“Replace one assignment and retain every other factor” does not determine
whether the intervention retypes the atom and creates \(m,r\), retains the
\(U\)-typed carrier, or is inadmissible. The first natural completion gives

\[
P(q_2=0\mid q_0=0,\operatorname{do}(w=R))=(B^2)_{00}=\frac{337}{625},
\]

and creates a record. Retaining the (U) branch gives

\[
P(q_2=0\mid q_0=0,\operatorname{do}(w=R))=C_{00}=\frac{49}{625},
\]

and has no record. Declaring the operation inadmissible requires a frozen
definition of admissible slots which the corpus does not contain. These are
different probabilities, sample types, and reader domains, not alternative
presentations of one experiment.

The same omission appears at the packet level: (H) is called a complete
valued history, while (Z), (R), and (E) are described only as “full,”
“complete,” or “declared”; the displayed probability does not specify which
histories are summed, which fields are excluded from the exterior context,
or the complete reader domain. The formal simultaneous transport of six
symbols is an action whenever a packet set is supplied, but it does not
construct the missing set or its intervention measure.

This violates the pin's requirement that
\(\mathsf{Exp}\), \(\mathsf{Read}\), and same-law semantics be
*determined, not merely named*. Repair requires fixing the experiment
interface or the dependent intervention semantics. The adjudication rule
forbids changing that interface. The experiment coordinate is therefore not
earned on the immutable corpus, and the terminal verdict is `REJECT`.

This failure does **not** alter the already defined history measure. Nor does
it erase the explicitly specified (X), (E), and (E') response examples;
those form a valid covariant subinterface and independently support the
narrow reciprocal-response coordinate recorded below.

## 3. Exact algebraic reconstruction

### 3.1 Rotation and stochastic matrices

Direct multiplication gives

\[
R^2=
\begin{pmatrix}
-7/25&-24/25\\
24/25&-7/25
\end{pmatrix}.
\]

Therefore entrywise squared moduli give

\[
B=\frac1{25}\begin{pmatrix}9&16\\16&9\end{pmatrix},\qquad
C=\frac1{625}\begin{pmatrix}49&576\\576&49\end{pmatrix}.
\]

Ordinary matrix multiplication gives

\[
B^2=\frac1{625}\begin{pmatrix}337&288\\288&337\end{pmatrix}.
\]

Since

\[
\det B=\frac{81-256}{625}=-\frac7{25},
\]

the process matrix \(B\) is invertible as a linear map, with

\[
B^{-1}=\frac17\begin{pmatrix}-9&16\\16&-9\end{pmatrix}.
\]

Consequently

\[
CB^{-1}=\frac1{175}
\begin{pmatrix}351&-176\\-176&351\end{pmatrix}.
\]

Every displayed column of (B,C,B^2) sums to one. The two negative entries
of (CB^{-1}) are exact.

### 3.2 Local normalization in (U,R,D)

For fixed (q_0,h,c,e), each deterministic relational assignment has one
output. Each noise law sums to

\[
\frac{16}{25}+\frac9{25}=1,
\]

so the joint noise sum is one. In mode (U),

\[
\sum_b C_{ba}=1.
\]

In each of modes (R,D),

\[
\sum_{m,b}B_{ma}B_{bm}
=\sum_m B_{ma}\sum_bB_{bm}=1.
\]

The \(R\)-record \(r=m\) is deterministic and adds no normalization factor.
Finally \(\sum_w 1/3=1\), and the four fair primitive bits each sum to
one. Hence \(\widetilde\mu\) is normalized in every fixed source context
and globally.

### 3.3 Boolean relational core and internal exchange

From

\[
(x',y',e')=(x\oplus e,y\oplus e,e\oplus x\oplus y)
\]

one recovers

\[
e=e'\oplus x'\oplus y',\quad x=x'\oplus e,\quad y=y'\oplus e.
\]

Thus the Boolean core is bijective.

Under \(X\leftrightarrow Y\), the identically distributed noises exchange,
\(x,y\) exchange, \(x',y'\), \(z_X,z_Y\), and \(u_X,u_Y\) exchange, while
\(e,e'\), all process fields, \(h,c,w,r\), and the weights are fixed. Hence
the atom law is invariant. In particular, the bond color \(d=e'\) is fixed.

### 3.4 Atom-conditioned bond law

For an endpoint pair, in outcome order \(\ell=0,1\),

\[
P(\ell\mid d_i=d_j)=\left(\frac{16}{25},\frac9{25}\right),\qquad
P(\ell\mid d_i\ne d_j)=\left(\frac9{25},\frac{16}{25}\right).
\]

Both rows sum to one. The law depends only on the two transported endpoint
colors, not on pair order or any atom index.

## 4. Local (G_1) orbit enumeration

Suppress all fields fixed by \(\tau\) and call their joint value
\(\beta\). It includes \(q_0,h,c,e,w\) and the appropriate process
outcomes. Since \(x=c\oplus\eta_X\) and \(y=c\oplus\eta_Y\), a labeled atom is
fixed by \(\tau\) exactly when
\(\eta_X=\eta_Y\). For every \(\beta\) there are precisely three
local orbit types:

| class | labeled noise values | orbit size | relative mass |
|---|---:|---:|---:|
| fixed (F_{00}(\beta)) | ((0,0)) | 1 | (256/625) |
| fixed (F_{11}(\beta)) | ((1,1)) | 1 | (81/625) |
| paired (P_{01}(\beta)) | ({(0,1),(1,0)}) | 2 | (288/625) |

The common omitted factor is the probability of \(\beta\). Thus each
\(\beta\)-fiber has total orbit mass
\((256+81+288)/625=1\).

There are 32 possible \(\beta\)-values in mode \(U\) and 64 in each
of modes \(R,D\). Hence \(\mathcal A\) has

\[
32\cdot4+64\cdot4+64\cdot4=640
\]

labeled atoms, split into 320 fixed singleton orbits and 160 two-element
orbits, for 480 local physical orbit types.

This also supplies the H3 fixed-point check: (F_{00}) and (F_{11}) are
each counted once, while (P_{01}) receives the sum of its two equal
representative masses.

## 5. Wreath-product action, stabilizers, and orbit pushforwards

### 5.1 Full bond-rule invariance

Write \(g=(\epsilon_1,\ldots,\epsilon_n;\pi)\in G_1^n\rtimes S_n\).
Internal swaps satisfy

\[
d(\epsilon_i a_i)=d(a_i),
\]

and the permutation transports

\[
\ell_{ij}\longmapsto\ell_{\pi(i)\pi(j)}.
\]

Therefore the equality predicate on endpoint colors, the Bernoulli parameter,
and the realized edge bit move together. The atom product is invariant under
every \(\epsilon_i\), and both the atom product and unordered-pair
product are invariant under \(\pi\). This proves invariance under the
full wreath-product action, not merely under (S_n) or (G_1^n) separately.

### 5.2 General stabilizer formula

For a representative (H), let (f(H)) be the number of vertices whose
local atom is \(\tau\)-fixed. Let
\(\operatorname{Aut}_{\rm typed}(H/G_1)\) be the automorphism group of
the bond graph decorated by complete local (G_1)-orbit types. Projection of
the wreath stabilizer to (S_n) has this typed automorphism group as image.
For every such permutation the required internal swap is unique at a paired
vertex and has two choices at a fixed vertex. Hence

\[
|\operatorname{Stab}_{\mathcal G_n}(H)|
=2^{f(H)}|\operatorname{Aut}_{\rm typed}(H/G_1)|,
\]

and

\[
|[H]|=
\frac{2^n n!}
{2^{f(H)}|\operatorname{Aut}_{\rm typed}(H/G_1)|}.
\]

The orbit mass is this number times any representative mass because the
frozen law is invariant.

### 5.3 Repeated-atom bonded history with automorphism

Take \(n=3\), the same \(\tau\)-fixed atom \(a\) at every vertex, and
the path graph with two present bonds. All endpoint colors are equal, so a
representative has mass

\[
q=\widetilde\mu(a)^3
\left(\frac9{25}\right)^2\frac{16}{25}.
\]

Here (f=3) and the typed path automorphism group has order two (exchange
the endpoints). Thus

\[
|\operatorname{Stab}|=2^3\cdot2=16,\qquad
|[H]|=\frac{2^3\,3!}{16}=3,
\]

and \(\Gamma_3([H])=3q\). The three is the number of distinct
placements of the missing edge. The endpoint automorphism does not delete any
of the three atom occurrences or the three pair occurrences: their physical
multiplicity remains in the powers of \(\widetilde\mu\), \(9/25\), and
\(16/25\).

### 5.4 History with no nontrivial automorphism

Take three paired local atoms in three distinct local orbit types, for
example one each in modes (U,R,D), and any bond pattern. No nonidentity atom
permutation preserves the complete decorations, and no internal swap fixes a
paired representative. Thus (f=0), the typed automorphism group is trivial,
the wreath stabilizer is trivial, and the orbit has size

\[
2^3 3!=48.
\]

The orbit pushforward is exactly 48 times the representative's atom-and-bond
mass. This and the preceding path give the required pushforwards for free and
non-free actions without trusting the paper's theorem label.

## 6. Normalization at fixed and varying size

At (n=0), the empty labeled history has mass one. At (n=1), summing
\(\widetilde\mu\) gives one. At \(n=2\),

\[
\sum_{a_1,a_2}\widetilde\mu(a_1)\widetilde\mu(a_2)
\sum_{\ell_{12}}P(\ell_{12}\mid d_1,d_2)=1.
\]

At (n=3), the three independent pair sums each equal one, so

\[
\sum_{a_1,a_2,a_3}\prod_i\widetilde\mu(a_i)
\prod_{i<j}\sum_{\ell_{ij}}P(\ell_{ij}\mid d_i,d_j)=1.
\]

The same product argument proves normalization for every finite (n). The
orbits partition the finite labeled set, so orbit pushforward preserves each
normalization. Finally

\[
\sum_{n=0}^\infty2^{-(n+1)}=1.
\]

Thus the history law is exactly normalized. On the resulting countable orbit
set, taking the power set as \(\Sigma\) completes the measure space. The
paper calls the set countable and later refers to its physical sigma algebra
but does not print this equality; that is a bounded expository omission, not
a probability counterexample.

## 7. Deletion before and after quotient

For \(n\ge1\), define the physical deletion kernel using any representative
(H) by

\[
D_n([H],[K])=\frac1n
\#\{i\in\{1,\ldots,n\}:[H\setminus i]=[K]\}.
\]

A different representative only permutes the (n) occurrences and applies
internal swaps, so the count is unchanged. Thus deletion *after quotient* is
a well-defined Markov kernel. It equals “choose a uniform labeled
representative, delete a uniform slot, quotient,” because each member of an
orbit has equal mass and an orbit of size (s) has pushforward mass (s)
times that member's mass.

Marginalizing the deleted iid atom gives one, and marginalizing every incident
bond gives one conditional on its endpoints. Every surviving atom factor and
pair factor is exactly the \(\widetilde\Gamma_{n-1}\) factor. Therefore

\[
\sum_{[H]}\Gamma_n([H])D_n([H],[K])=\Gamma_{n-1}([K]).
\]

This proves that quotient after uniform deletion and uniform deletion after
quotient agree as kernels. It is important that deletion is uniform over
physical occurrences, not a canonical-label deletion.

There is also an all-size check not stated in the paper. Conditional on
(N>0), deletion sends (N) to (N-1), and

\[
P(N-1=m\mid N>0)
=\frac{2^{-(m+2)}}{1-1/2}=2^{-(m+1)}.
\]

So the geometric cardinality law itself is stationary under one deletion
conditioned on nonemptiness.

## 8. Marked experiment groupoid: action proof and semantic failure

If \(\mathcal P_n\) is a specified set of complete well-typed packets,
the declared simultaneous transport defines

\[
g\cdot(H,Z,A,a,R,E)=(gH,gZ,gA,ga,gR,gE).
\]

Identity transport fixes every component, and
\(g_2\cdot(g_1\cdot p)=(g_2g_1)\cdot p\) because every component is
transported by the same presentation action. Hence
\(\mathcal G_n\ltimes\mathcal P_n\), with arrows
\((g,p):p\to g\cdot p\), is an action groupoid. Atom and bond factor
invariance bijects terms of equal mass, so any *defined* same-law intervention
whose rule is equivariant has the displayed covariance.

This proves the algebraic action conditional on \(\mathcal P_n\). It
does not cure the decisive defect in section 2: the frozen corpus never
defines \(\mathcal P_n\), the admissible slot alternatives, complete
contexts/readers, or a single intervention measure on dependent mode types.
An action on six metavariables is not yet the mandatory physical experiment
object.

### 8.1 Marked-slot stabilizer

Take two identical \(\tau\)-fixed atoms and either value of their one
bond. The unmarked history stabilizer has order
\(2^2\cdot2!=8\). Mark atom 1, port \(X\), its transported complete
reader, and a value. A stabilizer element can no longer exchange the atoms,
and \(\tau\) at the marked atom carries \(X\) to \(Y\); only the
internal swap at the unmarked fixed atom remains. The complete packet
stabilizer has order two and its packet orbit has size four. The four packets
mark (X) or (Y) in either occurrence. A naked marked-slot name would
discard this orbit.

At one fixed atom with \(c=e=0\) and
\(\eta_X=\eta_Y=0\), `do(X=1)` gives
\((x',y')=(1,0)\), while its transported packet `do(Y=1)` gives
\((0,1)\). Transporting the pair reader and outcome identifies the
two experiments. Leaving the reader or outcome labels behind does not.

## 9. Complete signed response reconstruction

All vectors below use the orientation `do(1) - do(0)`. These computations
apply to the explicitly defined \(X,E,E'\) subinterface and do not supply the
missing universal experiment domain.

### 9.1 Matter to local relation

Let \(s=e\oplus y\). Then \(e'=x\oplus s\), so for \(r\in\{0,1\}\),

\[
\Delta_{X\to e'}(r)
=\mathbf1_{r=1\oplus s}-\mathbf1_{r=s}.
\]

In outcome order \((0,1)\), this is \((-1,+1)\) for \(s=0\)
and \((+1,-1)\) for \(s=1\).

### 9.2 Relation to matter

For the complete outcome pair,

\[
\Delta_{E\to(X',Y')}
=\delta_{(1-x,1-y)}-\delta_{(x,y)}.
\]

Thus exactly one of the four entries is (+1), one is (-1), and the other
two vanish. Total variation is one.

### 9.3 Mediation

The total \(X\to Z_Y\) tensor is

\[
\Delta_{X\to Z_Y}(r)=\mathbf1_{r=1\oplus e}-\mathbf1_{r=e}.
\]

It is \((-1,+1)\) for \(e=0\) and
\((+1,-1)\) for \(e=1\). Holding \(e'=j\) independently fixed
makes \(z_Y=y\oplus j\), so the direct residual tensor is exactly
\((0,0)\).

### 9.4 Common cause versus intervention

The source gives

\[
P(y=1\mid x=1)=\frac{16^2+9^2}{25^2}=\frac{337}{625},
\]

while symmetry gives

\[
P(y=1\mid x=0)=\frac{288}{625}.
\]

The observational contrast \(x=1-x=0\), in outcome order
\(y=0,1\), is

\[
\left(-\frac{49}{625},\frac{49}{625}\right).
\]

The difference between conditioning on \(x=1\) and intervening to \(x=1\)
is

\[
\left(-\frac{49}{1250},\frac{49}{1250}\right),
\]

because the do-law leaves \(y\) fair. The actual \(X\to Y\) intervention
tensor is \((0,0)\).

### 9.5 Reader cancellation

The complete pair tensor is the four-entry tensor in section 9.2. The parity
reader is unchanged because
\(x'\oplus y'=x\oplus y\), and its two-entry tensor is
\((0,0)\). The zero belongs to the merged reader, not to the complete
future distribution.

### 9.6 Context reversal

For the outcome order \(u_X=0,1\),

\[
\Delta_{X\to U_X}[c=0]=(-1,+1),\qquad
\Delta_{X\to U_X}[c=1]=(+1,-1).
\]

Fairly averaging \(c\) before retaining it gives \((0,0)\), an exact
loss of context sign.

### 9.7 Spectator zero

No relational assignment depends on \(q_0\). Hence

\[
\Delta_{q_0\to e'}=(0,0).
\]

### 9.8 Incident-bond response

Let \(s=e\oplus y=d_i(\operatorname{do}x=0)\). Toggling \(x\) complements
\(d_i\). In bond-outcome order \((0,1)\),

\[
d_j=s:\quad
\Delta_{X\to\ell_{ij}}=
\left(-\frac7{25},\frac7{25}\right),
\]

\[
d_j\ne s:\quad
\Delta_{X\to\ell_{ij}}=
\left(\frac7{25},-\frac7{25}\right).
\]

The sign reverses between equal and unequal endpoint colors and the magnitude
remains (7/25). Every complete signed tensor above sums to zero.

## 10. Stable record, division, and nondivision reconstruction

For every licensed generator (F), the stated transported sectors obey
\(P_r^{\rm out}F=FP_r^{\rm in}\). If the equality holds for \(F\)
and (G), then

\[
P_r^{\rm out}(GF)=G(P_r^{\rm mid}F)=GF P_r^{\rm in}.
\]

Induction proves it for every finite word. The reversible sector swap remains
readable using the transported projector; the constant reset merges sectors
and has no inverse reader.

The four cases are exact:

1. **record yes / division yes:** In (R), (Z_R) contains (m,r,h) and
   all relational source and incident fields. The continuation is the
   positive normalized column (B_{q_2m}), (t=h), and deterministic or
   declared bond factors. Summing over (m) gives (B^2), so direct and cut
   laws agree.
2. **record yes / division no:** Keep (r=m) but omit (h). Two histories
   with the same (r) and (h=0,1) have future laws
   (P(t=0)=1) and (P(t=1)=1), respectively. The stable record alone is
   not future-sufficient.
3. **record no / division yes:** In (D), (Z_D) contains (m,h) and all
   relational data. The same positive (B) continuation and deterministic
   (t=h) give future sufficiency, although no record field exists.
4. **record no / division no:** In (U), invertibility of (B) makes
   (K=CB^{-1}) the unique candidate for (C=KB). Its entries
   (-176/175) exclude a positive normalized two-state restart. (C) itself
   remains bistochastic.

Adding a branch or record produces the different (B^2) law on an enlarged
carrier; it cannot factor the declared (C) law on the native two-state
carrier.

## 11. Owned hostile attacks H1--H11 and H23

### H1 — representative mass: attack succeeds against the mutant; paper passes

At (n=1), summing one representative per local orbit gives relative noise
mass

\[
\frac{256+81+144}{625}=\frac{481}{625},
\]

not one. The correct unequal-noise orbit contributes (288/625), not
(144/625). The paper uses the orbit sum and avoids this failure.

### H2 — automorphism multiplicity collapse: paper passes

The repeated-atom three-vertex path in section 5.3 has stabilizer 16, orbit
size three, and orbit mass (3q). Dividing by its graph automorphism or by
the full stabilizer would give the wrong physical mass. The paper sums
distinct labeled histories and retains the powers representing all physical
occurrences.

### H3 — internal fixed-point orbit: paper passes

The two fixed noise classes contribute (256/625) and (81/625) once each;
the paired class contributes (2(144/625)=288/625). No fixed class is
doubled.

### H4 — naked symmetric intervention: packet orbit required

The exact fixed-atom calculation in section 8.1 sends
`do(X=1)` with outcome \((1,0)\) to `do(Y=1)` with transported outcome
\((0,1)\). A naked slot is not a function on the history orbit. The
paper correctly states simultaneous packet transport, but its complete packet
domain fails for the independent reason in section 2.

### H5 — history-only quotient: rejected

Quotienting (H) while retaining an (X)-marked slot, an untransported pair
reader, or fixed coordinate outcome distinguishes the two presentations in
H4. Such a number is not physical. Only the complete transported packet can
descend.

### H6 — graph enumeration order: paper passes

The finite atom product and unordered-pair product commute. Any atom
permutation is a bijection on factors, and every pair bit follows its endpoint
set. Probabilities and the defined experiment profiles are unchanged.

### H7 — bond endpoint sever: rejected exactly

Take colors \((d_1,d_2,d_3)=(0,0,1)\) and only bond 12 present. The
bond factor is

\[
\frac9{25}\frac9{25}\frac9{25}=\frac{729}{15625}.
\]

Swap atoms 2 and 3 but improperly leave the present bit at pair 12. The factor
becomes

\[
\frac{16}{25}\frac{16}{25}\frac9{25}
=\frac{2304}{15625}.
\]

Properly transporting the present edge to pair 13 retains (729/15625).
The severed structure is not the same orbit, exactly as required.

### H8 — per-size table replacement: all-size theorem fails

Mutate only (n=4) bonds to fair Bernoulli variables while retaining all
smaller laws. For equal endpoint colors, deletion from (n=4) leaves an
(n=3) empty-graph probability (1/8), whereas the frozen (n=3) endpoint
law assigns

\[
\left(\frac{16}{25}\right)^3=\frac{4096}{15625}.
\]

The mutant remains normalized separately at each size but is not projective.
The paper uses one endpoint rule and passes.

### H9 — uniform deletion: paper passes

The physical kernel (D_n) in section 7 is representative-independent and
maps \(\Gamma_n\) exactly to \(\Gamma_{n-1}\). All deleted incident
bond factors marginalize to one. Quotient and uniform deletion commute.

### H10 — hidden order: rejected exactly

As a mutant, give the first enumerated equal-color pair probability (16/25)
and other equal-color pairs (9/25). On a three-vertex graph with one present
edge, a presentation in which that edge is first has factor
\(4096/15625\); a relabeling in which the first pair is absent has factor
\(1296/15625\). The same typed graph gets two masses. No such index
enters the frozen endpoint law.

### H11 — fixed dormant carrier: changes the sample space

A maximum carrier of size (M) deletes the positive tail
\(P(N>M)=2^{-(M+1)}\). A countably infinite dormant carrier has no
uniform finite (n)-subset and introduces dormant-point automorphisms or a
selection measure absent from \(\Gamma_*\). Either construction is a new
law. The frozen carrier is exactly the finite occurrence set and passes.

### H23 — modes are one field, not a result-selected menu

The frozen joint law samples \(w\) with prior \((1/3,1/3,1/3)\) before
its fixed conditional kernel. As an inspection-selection mutant, postselect
on (q_2=q_0). The posterior mode weights become

\[
P(U\mid q_2=q_0)=\frac{49}{723},\qquad
P(R\mid q_2=q_0)=P(D\mid q_2=q_0)=\frac{337}{723},
\]

not one third. That is a different postselected law. The paper makes no such
selection and passes H23.

## 12. Quotient audit of H12--H22 and H24--H26

| attack | exact result and quotient effect |
|---|---|
| H12 conditioning as intervention | (P(y=1\mid x=1)=337/625) but (P(y=1\mid\operatorname{do}x=1)=1/2). Swapping (X,Y) transports the whole comparison; quotienting cannot identify conditioning with do. Pass. |
| H13 incomplete reader | The complete pair tensor has entries \((+1,-1,0,0)\); parity has \((0,0)\). Parity is itself swap-invariant, but quotient invariance does not make it separating. Pass. |
| H14 mediator deletion | Total (X\to Z_Y) is the signed unit tensor; holding (e') fixed gives zero. Under \(\tau\), (X,Z_Y) transport to (Y,Z_X). No quotient turns total into direct. Pass. |
| H15 context aggregation | (c) is fixed by \(\tau\); its two signed tensors are opposites. Averaging (c) gives zero but is a coarse reader/context, not a physical quotient. Pass. |
| H16 bond orientation | The two endpoint cases give \((-7/25,+7/25)\) and its negative. Atom permutations transport endpoint, color, mark, and bond together. Pass. |
| H17 reversible swap | Transporting (P_r) through (F_R) recovers the input sector. (F_R) is a future bijection, not a presentation quotient or eraser. Pass. |
| H18 true eraser | The reset merges both record sectors. Quotienting presentations cannot restore an inverse reader, and the reset is outside the grammar. Pass. |
| H19 record implies division | The (h=0,1) histories are in different typed orbits because the presentation group fixes (h). Their deterministic (t) profiles remain distinct after quotient. Pass. |
| H20 division implies record | Mode (D) and (m,h) are transported atom fields, while no record field exists. Quotienting cannot manufacture one. The positive (B) continuation survives. Pass. |
| H21 native Markovization | Process bits are fixed by local port exchange and only transported between atoms. The unique (CB^{-1}) retains its negative entries in every presentation. Pass. |
| H22 enlargement after failure | A branch, history ID, phase, or cache must either be a new transported physical field, changing the orbit space, or gauge away, returning the same negative two-state kernel. It cannot repair the declared carrier. Pass. |
| H24 retuning | Changing (R), priors, mode weights, bond probabilities, or the geometric cardinality law changes invariant factors and therefore orbit masses. Quotienting does not identify different measures. The paper does not retune. Pass. |
| H25 dimension leakage | The finite-set cardinality and canonical unordered-pair set introduce neither a metric nor dimension. No dimension, coordinate, lattice, scaling target, or desired spacetime outcome selects the frozen law. Pass. |
| H26 actuality smuggling | Orbit pushforward normalizes possible alternatives only. No orbit is selected, and no groupoid operation supplies actualization. The paper states `UNCONSTRUCTED`. Pass. |

## 13. Additional mathematical countermodels

The following concrete countermodels are new to this report. They supplement,
rather than replace, the mandatory mutations.

### N1 — nontrivial typed graph automorphism

The repeated fixed-atom three-path in section 5.3 has graph automorphism
\(C_2\), wreath stabilizer 16, and orbit size three. It kills both naive
division by automorphism order and naive multiplication by all group elements.
Only the set-orbit pushforward gives \(3q\).

### N2 — disconnected component-exchange history

Take four identical fixed atoms with equal color and graph \(2K_2\), two
disjoint present edges. Its graph automorphism group has order
\(2^2\cdot2=8\): each edge can flip and the two components can
exchange. With \(f=4\),

\[
|\operatorname{Stab}|=2^4\cdot8=128,\qquad
|[H]|=\frac{2^4 4!}{128}=3.
\]

The three physical presentations are the three perfect matchings. Its orbit
mass is

\[
3\widetilde\mu(a)^4
\left(\frac9{25}\right)^2
\left(\frac{16}{25}\right)^4.
\]

Quotienting connected components independently and forgetting the component
exchange factor loses this exact multiplicity.

### N3 — marked-slot stabilizer reduction

The two-identical-atom packet of section 8.1 reduces the history stabilizer
from eight to a packet stabilizer of two and produces four marked packets.
Quotienting the history before adding the mark incorrectly leaves one naked
slot. This is a concrete stabilizer obstruction, not merely a naming warning.

### N4 — complete and empty fixed-point families

For every \(n\), put the same fixed atom \(a\) at every vertex and take either
\(K_n\) or the empty graph. The full wreath group fixes the complete typed
history, so the orbit is a singleton. Writing
\(M=\binom n2\) and \(p=9/25\), the correct masses are

\[
\widetilde\mu(a)^n p^M
\quad\hbox{and}\quad
\widetilde\mu(a)^n(1-p)^M.
\]

Multiplying by \(2^n n!\) overcounts; dividing by that stabilizer undercounts.
The powers still retain all \(n\) atom occurrences and \(M\) pair
occurrences. Uniform deletion maps each family to the corresponding
(n-1) family.

### N5 — coarse unlabeled graph is not a typed-history orbit

Take the same empty two-vertex graph and identical values of every field
except that one atom has (h=0) in (H_0) and (h=1) in (H_1). The coarse
unlabeled graph is identical, but (h) is fixed by (G_1) and transported by
(S_2), so the complete typed histories are not in one orbit. Their future
readouts include (t=0) versus (t=1). A quotient that erases atom fields
while retaining bonds destroys a measured future distinction and is not the
declared physical quotient.

### N6 — canonical-representative deletion

Take a two-atom orbit with distinct typed atoms (A,B). If a canonical
representative always orders (A) first and one deletes slot 1 rather than a
uniform physical occurrence, the output is always (B). Correct uniform
deletion gives \(\frac12\delta_A+\frac12\delta_B\). A deterministic
canonical deletion therefore fails projectivity even though the history
representative was canonical.

### N7 — dependent mode-slot intervention

The (U\to R) mode intervention in section 2 gives (49/625) or (337/625)
and changes record type according to equally compatible completions of the
frozen prose. This is the decisive semantic countermodel to the universal
experiment coordinate.

## 14. Provisional-coordinate prerequisite audit

| coordinate | actual prerequisites | result |
|---|---|---|
| point-free history referent | finite typed atoms, full incidence transport, wreath action, orbit pushforward | **passes** |
| one whole-history law | fixed primitives, normalized \(\widetilde\mu\), normalized bonds, orbit partition, geometric size law | **passes** |
| point-free experiment action | determined packet set, admissible typed slots, contexts, complete readers, same-law measure, simultaneous groupoid transport | **fails**: only the last transport clause is defined globally |
| grammar-stable record | typed projectors, all licensed generators, intertwining, finite-word induction, eraser controls | **passes** |
| complete division frontiers | full (Z_R,Z_D), future sufficiency, positive normalized kernels, direct/cut equality | **passes at the declared grammar** |
| native indivisible cut | fixed native carrier, invertible (B), unique (K), negative entry, normalized whole (C), no repair state | **passes** |
| varying-size family | all-(n) rule, fixed-size normalization, exact quotient, uniform-deletion kernel, local finiteness, order independence | **passes** |
| reciprocal relational response | one same-law explicitly specified (X/E/E') subinterface, complete outcome tensors, common-cause/mediation/cancellation/reversal/spectator controls, packet covariance | **passes narrowly**; it does not construct the missing universal experiment interface |
| actuality | an actualization postulate or derivation if claimed | correctly **unconstructed** |

The response coordinate is retained because the product rule forbids erasing
independent results: its concrete interventions, fixed contexts, complete
outcome readers, and transported tensors are explicitly calculable. It must
not be paraphrased as validation of every marked slot or every reader named by
the schematic experiment section.

## 15. Full product outcome vector

```text
referent    P13B-POINT-FREE-HISTORY-REFERENT-CONSTRUCTED
law         P13B-ONE-WHOLE-HISTORY-GAMMA-CONSTRUCTED
experiment  P13B-EXPERIMENT-PRESENTATION-ONLY
record      P13B-GRAMMAR-STABLE-RECORD-CONSTRUCTED
division    P13B-COMPLETE-DIVISION-FRONTIERS-CONSTRUCTED
nondivision P13B-NATIVE-INDIVISIBLE-CUT-CONSTRUCTED
size        P13B-VARYING-SIZE-COVARIANT-FAMILY-CONSTRUCTED
response    P13B-RECIPROCAL-RELATIONAL-RESPONSE-CONSTRUCTED
actuality   P13B-ACTUALIZATION-UNCONSTRUCTED
```

`P13B-EXPERIMENT-PRESENTATION-ONLY` is the preregistered negative bucket for
the unearned physical experiment coordinate. The corpus does transport
packet notation, but it does not determine the packet/reader/intervention
object on which a physical probability law is supposed to descend.

## 16. Verdict

**REJECT.** The history groupoid, whole-history probability, quotient
multiplicities, all-size covariance, records, divisions, native nondivision,
and explicit reciprocal-response seed survive hostile reconstruction. The
mandatory complete experiment object does not: the frozen corpus leaves the
admissible intervention and reader domains undefined and gives no unique
same-law evaluation for a typed mode-changing intervention. Fixing that is a
semantic experiment-interface choice, not a bounded proof or prose repair,
and the frozen adjudication rule does not authorize it.

This report is sibling-blind and implementation-free. No sibling review path
or content was inspected, and only this designated report path was created.
