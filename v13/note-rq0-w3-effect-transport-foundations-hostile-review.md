# Independent hostile review — quantum foundations / process instruments

**Overall verdict: `HEADLINE-DOWNGRADE`**

- Governing pin: `e9948073c38a96e92c9b17bbe1009b1fc1337788`
- Immutable paper: `a57bed6511fd21511d5e25bf351ef5c371ed7d07`
- Paper SHA-256: `6de7743ba614074ca51c68564bd441b870c8210e6f30d49daf3fc297c2970da5`
- Paper size: 58,386 bytes; 1,918 lines
- Review mode: repository read-only; no repository changes; exact scratch calculations only under `/private/tmp`

The total effect/POVM interface, instrument shadow, record-defect laws, and multiplicative-domain theorem survive. The advertised “sharp fact” does not. The W3 seed produces a sharp record observable and a stable branch-memory correlation, but its unitary dynamics do not select an actual record atom or supply an interpretation-independent fact. Correspondingly, `Rec_sharp` transports Boolean propositions, not truth, occurrence, fact identity, or event-token identity.

The admitted-idempotent construction is mathematically type-correct and has a defensible weak referent as repeatable coarse-graining. It does not, by itself, establish independent operational access in the stronger ordinary sense. The highest cumulative headline is therefore withheld even though its operator-system and Karoubi theorems survive separately.

## Rung dispositions

| Rung | Disposition | First obstruction |
|---|---|---|
| `RQ0-L0-W3-EFFECT-TRANSPORT` | **EARNED** | None at the restricted scope: it is total Heisenberg pullback of a declared W3 outcome question along admitted UCP maps, with full instruments only when branches are supplied. |
| `RQ0-L0-SHARP-FACT-TRANSPORT` | **WITHHELD** | Multiplicativity transports sharp propositions but supplies no actual truth valuation, outcome occurrence, co-reference bridge, copying lineage, or token identity. “Fact” exceeds the constructed referent. |
| `RQ0-L0-ADDRESSABLE-W3-OPERATOR-SYSTEM` | **WITHHELD** | The cumulative fact rung has failed; independently, an admitted idempotent certifies repeatable coarse-graining/fixed observables, not general independent preparation, readout, or manipulation of a subsystem. |

The latter two are withheld rather than blocked: their mathematical constructions exist and remain useful under narrower names.

## 1. Independent W3 reconstruction

Use the ordered basis (00,01,10,11) and

\[
U=\operatorname{CNOT}_{b\to m}(H_b\otimes I_m),\qquad
N=H_b\otimes I_m,
\]

\[
V=H_b\otimes I_m,\qquad
E=(H_b\otimes I_m)\operatorname{CNOT}_{b\to m}.
\]

For every basis input,

\[
U|b,m\rangle
=
\frac{|0,m\rangle+(-1)^b|1,m\oplus1\rangle}{\sqrt2}.
\]

The exact write supports are

\[
00\mapsto\{00,11\},\quad
01\mapsto\{01,10\},\quad
10\mapsto\{00,11\},\quad
11\mapsto\{01,10\}.
\]

Each live pair occupies distinct memory sectors. Perfect write correlation therefore holds.

For the no-write control,

\[
N|b,m\rangle
=
\frac{|0,m\rangle+(-1)^b|1,m\rangle}{\sqrt2},
\]

with supports \(\{00,10\}\) or \(\{01,11\}\). The alternatives share one memory value, so the correlation predicate fails. The paper correctly treats “no-write” as a declared operational role rather than deriving historical non-occurrence from that failure alone.

Since \(V\) changes only the branch bit, a final probe \(\langle c,n|\) can receive cut alternatives only from \(|0,n\rangle\) and \(|1,n\rangle\). Availability under the preserving continuation is exact.

For preparation and probe \(00\),

\[
\langle00|EQ_{00}U|00\rangle
=
\langle00|EQ_{11}U|00\rangle
=
\frac12.
\]

The cross-sector product is \(1/4\); the full interference contribution \(2\operatorname{Re}(1/4)\) is \(1/2\). Coherent erasure recombines the two sectors and defeats continuation-relative availability.

The preserving closed amplitude is independently reproduced as

\[
\langle00|VQ_{00}U|00\rangle=\frac12.
\]

The native memory resolution is genuinely a PVM:

\[
P_0=\operatorname{diag}(1,0,1,0),\qquad
P_1=\operatorname{diag}(0,1,0,1),
\]

\[
R_W=C^*(P_0,P_1)=\operatorname{span}\{I,Z_m\}.
\]

### Physical disposition of W3

The record remains internal to one quantum amplitude family. No classical measuring device, collapse map, or outcome instrument is attached. The preserving and erasing alternatives are quantum continuations of the same written correlation.

That success also exposes the headline problem. For input \(00\), the state at the seam is

\[
\frac{|00\rangle+|11\rangle}{\sqrt2},
\]

not an eigenstate of either \(P_0\) or \(P_1\). The construction establishes:

- a sharp observable;
- mutually exclusive record alternatives;
- perfect branch-memory correlation;
- continuation-relative availability; and
- coherent erasability.

It does not establish, without an additional outcome ontology, that one particular \(P_r\) is actually true. The writing interaction occurred as a declared process leg; a determinate record outcome does not follow interpretation-independently. The paper’s refusal to invent an instrument is correct, but it prevents the same unitary seed from being used as an unqualified actual-fact certificate.

Occurrence and availability are otherwise kept distinct correctly: erasure removes later availability without retroactively removing the earlier writing interaction.

## 2. Effect and instrument audit

For a Schrödinger channel \(\Lambda:A_*\to B_*\) with Heisenberg adjoint \(F=\Lambda^*:B\to A\),

\[
\operatorname{Tr}\!\left(\rho F(P_r)\right)
=
\operatorname{Tr}\!\left(\Lambda(\rho)P_r\right).
\]

This gives `Rec_eff` a genuine operational referent: it is the input-side effect for the declared native record-outcome question after the admitted preprocessing channel. The PVM becomes a normalized POVM because positivity and unitality give

\[
0\le F(P_r)\le I,\qquad \sum_rF(P_r)=I.
\]

The undercategory and category-of-elements construction are correctly typed and functorial.

This is Heisenberg predicate pullback. It is not, in general, downstream carriage of a historical record from the native seam to a later boundary. Statements that an “upstream or downstream” channel blurs the record must be read with this variance restriction.

### Instruments versus POVMs

The Schrödinger instrument convention is sound:

\[
\mathcal I_r:\mathcal T(H_A)\to\mathcal T(H_B),\qquad
E_r=\mathcal I_r^*(I_B).
\]

Precomposition by a CPTP channel produces another instrument, and its effects are pulled back by the adjoint channel.

The Lüders/reprepare control is decisive:

\[
\mathcal L_r(\rho)=P_r\rho P_r,\qquad
\mathcal J_r(\rho)=\operatorname{Tr}(P_r\rho)P_+.
\]

Both have effects \(P_r\), but on input \(P_0\), outcome \(0\),

\[
\mathcal L_0(P_0)=P_0,\qquad
\mathcal J_0(P_0)=P_+.
\]

Thus equal effects and equal probabilities do not determine disturbance or continuation dynamics. The hierarchy

\[
\text{instrument}\to\text{POVM}\to\text{sharp Boolean interface}
\]

is faithful at the level of types. The paper does not invent an instrument from the W3 PVM.

### Noisy controls

For the random bit-flip channel,

\[
F(P_0)=
\begin{pmatrix}3/4&0\\0&1/4\end{pmatrix},
\qquad
\Sigma_F(P_0)=\frac3{16}I.
\]

This is a noisy binary predicate—indeed one with a classical random-unitary realization—not destruction of a past occurrence.

For amplitude damping at \(\gamma=1/2\),

\[
A^*(P_1)=\frac12P_1,\qquad
\Sigma_{A^*}(P_1)=\frac14P_1.
\]

This quantifies the probability of obtaining the native excited-state outcome after damping. It does not show that a previously occurred event became historically untrue.

The paper handles these distinctions correctly.

## 3. Record defect and sharp proposition transport

The positive defect

\[
\Sigma_F(P)=F(P)-F(P)^2
\]

exactly detects whether the pulled-back effect is a projection. The two-term chain law is correct, including the qualification that a later nonfaithful map may hide an earlier positive defect.

The multiplicative-domain equivalence is also secure:

\[
R_W\subseteq\operatorname{MD}(F)
\Longleftrightarrow
F|_{R_W}\text{ is a unital *-homomorphism}
\Longleftrightarrow
F(P_r)\text{ are projections}
\Longleftrightarrow
\Delta_F^{\mathrm{rec}}|_{R_W}=0.
\]

The image-containment condition in `SharpRec_D` supplies the target-interface typing missing from mere multiplicativity. Identities and composites close, and `Rec_sharp` is a genuine Boolean functor on this restricted category.

What it transports is proposition logic. A Boolean homomorphism contains every possible record proposition, most of which are false in any one run. It carries neither a state nor an actual ultrafilter selecting the true atom. The deterministic bit flip makes this especially clear:

\[
P_0\mapsto P_1,\qquad P_1\mapsto P_0
\]

is perfect sharp transport but is not identity of an outcome fact.

The separate-fair-qubits control likewise shows that abstractly equal Boolean maps and equal binary laws do not supply any physical bridge. The paper makes no illicit inference to availability, occurrence, fact identity, event-token identity, copying lineage, or overlap. Nevertheless, redefining “fact” to mean “sharp proposition” does not earn the physical noun. The surviving result is sharp Boolean proposition pullback.

## 4. Counterfactual law and no-smuggling

The law dependence is explicit and real. With the same W3 amplitudes and native record law:

- an identity-only transport grammar gives \(\operatorname{span}\{I,Z\}\);
- adding a unitary rotation gives \(\operatorname{span}\{I,Z,X\}\);
- admitting a dephasing idempotent provides a proper containing retraction;
- omitting it while retaining only unitary automorphisms gives identity-only access;
- admitting two symmetry-related dephasings gives incomparable minima retained as an orbit/groupoid.

These are genuine counterfactual completions with identical realized W3 behavior and different \(\mathcal S_W\) or addressability classifications. They prove nomological dependence rather than intrinsic support.

The smuggling audit is favorable at the paper’s restricted scope:

- The boundary, W3 cut and PVM are openly declared.
- No outcome instrument is selected from the PVM.
- No Kraus or Naimark presentation enters the constructions.
- Enlarging the transport grammar is explicitly allowed to change the answer.
- An abstract conditional expectation is excluded unless admitted.
- The inaccessible-spectator result uses its exact product and unitality hypotheses and makes no intrinsic-factor claim.
- The symmetry example retains both minima and the exchanging symmetry rather than choosing lexically.

The symmetry grammar is engineered and therefore supplies only a conditional finite control. It genuinely demonstrates nonselection once that grammar and physical symmetry are declared; it does not establish that nature supplies this grammar.

The paper never claims intrinsic support, localization, overlap, topology, influence, causality, geometry, fields, or gravity. Its no-smuggling discipline is substantially better than the rejected Weld paper.

## 5. Idempotents and addressability

An admitted UCP idempotent has a defensible operational meaning. Its Schrödinger adjoint is an executable channel whose second application changes nothing further, and its Heisenberg fixed system consists of observables left invariant by that coarse-graining. The Karoubi envelope repairs the earlier categorical typing failure, and fixed ranges are correctly treated first as operator systems rather than ambient-product subalgebras.

That earns a weak statement:

> The admitted law contains a repeatable coarse-graining preserving the transported record-effect system.

It does not by itself show independent preparation, selective readout, arbitrary manipulation, or nondemolition access to every element of the fixed system. A formal Karoubi object is therefore not automatically a physically independent subsystem or boundary.

The identity-only correction is mathematically necessary: identity always fixes every \(\mathcal S_W\), so literal “no containing idempotent” is impossible. Two physically different cases remain:

1. \(\mathcal S_W=B\), where identity is forced mathematically;
2. \(\mathcal S_W\subsetneq B\), where the admitted grammar simply lacks a proper idempotent.

Only the first establishes global operator content. The second establishes absence of an admitted proper coarse-graining, not intrinsic globality. The paper’s phrase “global at this admitted-law scope” is acceptable only with that strict operational qualification.

The symmetry control is mathematically sound. With \(n\cdot m=1/2\), alternating dephasing words acquire nonunit eigenvalues strictly between zero and one; the only proper containing idempotents in the declared monoid are \(e_n\) and \(e_m\). They are incomparable and exchanged by the declared symmetry. Retaining the action groupoid correctly implements no arbitrary selection.

## 6. Antecedent and descent scope

Terminal RQ0-A remains a valid sharp-map positive control. For its declared isometry \(J\),

\[
F(a)=J^*aJ
\]

is UCP, and the checked relations

\[
J^*P_r^{\mathrm{target}}J=P_r^{\mathrm{source}}
\]

make every record atom sharp. The multiplicative-domain theorem therefore applies to the generated finite record algebra. It does not make the compression multiplicative on the ambient algebra or discover an intrinsic overlap.

Paper 2/W6 remains a necessary negative boundary:

\[
\text{same value}
\not\Rightarrow
\text{same fact}
\not\Rightarrow
\text{same occurrence}
\not\Rightarrow
\text{set-level descent}.
\]

The present paper respects that boundary. Equal fair laws and abstract Boolean identities are used only as negative controls. No Weld overlap or chart claim is restored.

## 7. Four-gate audit

| Object | Referent | Necessity | No-smuggling | Discriminator | Disposition |
|---|---|---|---|---|---|
| effect | probability propensity for a declared native outcome after admitted preprocessing | generic channels do not preserve projections | no identity or occurrence inferred | unitary versus random-unitary/amplitude damping | **PASS, with Heisenberg-pullback scope** |
| POVM | complete outcome-probability interface | total UCP pullback of the PVM | no disturbance map invented | same POVM, different instruments | **PASS** |
| instrument | outcome plus conditional process update | required to represent disturbance | branches must be supplied | Lüders versus reprepare | **PASS** |
| record defect | algebraic failure of the predicate transformer to preserve record products | separates sharp from unsharp interfaces | distinct from the Born defect and historical loss | zero unitary/dephasing versus noisy channels | **PASS as diagnostic** |
| multiplicative domain | maximal algebra on which one UCP map acts homomorphically | types the sharp subcategory | supplies no truth, co-reference, or token lineage | sharp versus noisy PVM images | **PASS mathematically; “fact” referent fails** |
| operator system | least linear statistical envelope of transported record effects | avoids inventing products | grammar and PVM remain declared | three-dimensional seed versus four-dimensional C*-closure | **PASS law-relatively** |
| admitted idempotent | executable repeatable coarse-graining | types invariant access without abstract expectations | admission is required | admitted/unadmitted dephasing | **QUALIFIED PASS; insufficient for strong addressability** |
| Karoubi object | formal split object of an admitted idempotent | repairs categorical typing | does not promote arbitrary subalgebras | proper, ambiguous and identity-only controls | **PASS formally; physical subsystem meaning qualified** |

## 8. Fatal referent failures

These failures are fatal to the later headlines, not to the surviving operator theorems.

1. **Native fact actualization is absent.** The W3 unitary writes an entangled correlation but supplies no selected outcome, valuation, collapse branch, hidden actual variable, or declared relative-fact interpretation.
2. **`Rec_sharp` has proposition—not fact—codomain.** A Boolean homomorphism preserves logical operations but contains no occurrence or truth data.
3. **Strong addressability is not supplied by invariance alone.** An admitted idempotent establishes a repeatable coarse-graining; its formal fixed object is not automatically an independently preparable, readable, or controllable physical subsystem.

## 9. Required scope and terminology restrictions

These are interpretive restrictions on surviving results, not proposed repository repairs.

- “Transport” means Heisenberg predicate pullback along the displayed arrows.
- “Sharp fact” must be read only as “sharp record proposition”; under ordinary foundations usage the fact headline is unearned.
- “Unsharp evidence” means a POVM effect governing a declared outcome probability, not destruction of a historical event.
- \(\Sigma_F\) is a sharpness diagnostic, not a monotone amount of record destruction.
- “Addressable” means idempotent-coarse-grainable at the admitted-law scope.
- “Identity-only/global” means no admitted proper retraction unless \(\mathcal S_W=B\) is separately proved.

## 10. Surviving insights and theorems

The following survive intact:

1. the complete W3 write/preserve/erase/no-write reconstruction and closed amplitude \(1/2\);
2. the native record PVM and the occurrence/availability distinction, understood as correlation and continuation claims;
3. total UCP effect and POVM pullback;
4. instrument precomposition and the same-POVM/different-disturbance separation;
5. positivity, exact sharpness detection, covariance and chain laws for the record defect;
6. the multiplicative-domain equivalence and partial sharp Boolean functor;
7. the law-relative minimal observability operator system and spectator law;
8. Karoubi typing and fixed-range operator-system results;
9. the correction from impossible “no containing idempotent” to “no proper admitted idempotent”;
10. exact proper, identity-only and symmetry-groupoid controls;
11. terminal RQ0-A as a finite declared-projector-pullback positive control; and
12. every explicit non-result concerning intrinsic support, overlap, localization and later physics.

## 11. Optional future work

None is proposed or evaluated. Any outcome ontology, instrument-native actuality criterion, or stronger operational subsystem notion would require a separate authorization and lies outside this review.

The durable scientific result is therefore total law-relative effect/POVM pullback plus a restricted sharp-proposition theorem and a weak admitted-idempotent classification—not transport of physical facts and not an intrinsic addressable quantum region.
