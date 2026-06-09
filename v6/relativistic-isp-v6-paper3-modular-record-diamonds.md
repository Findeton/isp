# Paper 3 (v6) - Modular Record Diamonds and the Sealed-Deletion Equivalence Principle

**Author:** Felix Robles Elvira

**Status:** Ontology paper and finite theorem-target campaign. This paper does
not prove that nature realizes the proposed process. It defines the new
branch-A-enriched base required by Papers 1-2, checks which quantities are
intrinsic to that base, and records the finite counterexamples that kill the
weaker bases. Claims are tagged **[DEF]** for definitions, **[THM-TARGET]**
for theorem targets, **[PROBE]** for finite scripts, and **[OPEN]** for
continuum or physical-existence claims not proved here.

Builds directly on:

```text
Paper 1: bare ICS gives geometry but not the full physical event law.
Paper 2: bare branch A fails; branch A-enriched requires a sealed modular
         deletion profile and a fixed CMRP action.
```

The diagnostic scripts for this paper are:

```text
code/v6_p3a_cmrp_ontology_closure.py
code/v6_p3b_cmrp_axiom_independence.py
code/v6_p3c_cmrp_observable_derivation.py
code/v6_p3d_feynman_record_channel.py
code/v6_p3e_mdp_completeness_attack.py
code/v6_p3f_germ_origin_uniqueness_audit.py
code/v6_p3g_canonical_germ_generation.py
code/v6_p3h_germ_origin_decision.py
code/v6_p3i_isp_do_delete_no_go.py
code/v6_p3j_isp_do_delete_derivation_audit.py
code/v6_p3k_do_delete_decision.py
code/v6_p3l_einstein_reality_campaign.py
code/v6_p3m_self_deleting_completeness_campaign.py
code/v6_p3n_nx_origin_campaign.py
code/v6_p3o_intrinsic_collar_separator_theorem.py
code/v6_p3p_tx_origin_campaign.py
code/v6_p3q_eventless_defect_campaign.py
code/v6_p3r_intrinsic_rx_units_resolution.py
code/v6_p3s_imfd_genericity_campaign.py
code/v6_p3t_fixed_cmrp_imfd_dynamics.py
code/v6_p3u_spectrum_flow_origin_campaign.py
code/v6_p3v_k0_origin_campaign.py
code/v6_p3w_sealed_work_profile_campaign.py
code/v6_p3x_feynman_wx_receipts.py
code/v6_p3y_full_branch_a_target_campaign.py
code/v6_p3z_underlying_change_law_campaign.py
code/v6_p3aa_current_rho_origin_campaign.py
code/v6_p3ab_q_origin_einstein_campaign.py
code/v6_p3ac_screen_bridge_theorem_campaign.py
code/v6_p3ad_minimal_complete_screen_campaign.py
code/v6_p3ae_record_completeness_closure_campaign.py
code/v6_p3af_no_silent_seam_origin_campaign.py
code/v6_p3ag_rn_action_conservation_campaign.py
code/v6_p3ah_canonical_reference_campaign.py
code/v6_p3ai_count_functor_origin_campaign.py
code/v6_p3aj_leibniz_record_functor_campaign.py
code/v6_p3ak_record_field_equation_campaign.py
code/v6_p3al_field_equation_candidate_campaign.py
code/v6_p3am_stronger_rigidity_campaign.py
code/v6_p3an_whole_diamond_action_campaign.py
code/v6_p3ao_action_selection_invariant_campaign.py
code/v6_p3ap_relational_field_equation_campaign.py
code/v6_p3aq_field_equation_origin_closure.py
code/v6_p3ar_score_geometry_campaign.py
code/v6_p3as_conditional_score_origin.py
code/v6_p3at_pc_origin_campaign.py
code/v6_p3au_pd_principle_campaign.py
code/v6_p3av_process_law_boundary_campaign.py
code/v6_p3aw_pd_contradiction_campaign.py
code/v6_p3ax_unique_process_law_no_go.py
```

---

## 0. One-page thesis

The base of the theory is not a bare causal set.

The base is a **Cofinal Modular Record Process** (CMRP): a cofinal family of
finite, covariant record processes on causal diamonds. Its local event is a
**sealed modular record diamond**, namely an event germ whose deletion changes
record, source, causal-order, and screen/volume readouts as one fact.

The guiding thought experiment is:

```text
Put the observer inside a closed causal diamond.
Do not give them an external slicing, external sector labels, or a detector
kernel.
Let them compare the internal record law with and without one candidate event x.
Ask what invariant remains.
```

The scalar modular action/readout is the deletion profile:

```math
M_x(k)
=
D\!\left(P_x|F_{x,k}\,\|\,P_{\setminus x}|F_{x,k}\right).
```

Here `P_x` is the retained local law, `P_{\setminus x}` is the deleted local
law, and `F_{x,k}` is the intrinsic causal-diamond shell filtration. The full
physical object is the sealed deletion germ:

```text
G_x = (P_x, P_{\setminus x}, F_{x,k}, role maps, fixed units, action).
```

The profile is the scalar action profile of that germ. It is not merely a
number; its shell increments are the local work of deletion:

```math
w_x(k)=M_x(k+1)-M_x(k).
```

The proposed equivalence principle is a theorem target, not an axiom:

```text
Sealed-deletion equivalence.
Inside a closed causal diamond, record/source/causal/screen descriptions are
one physical event iff their sealed deletion germs agree up to internal
isomorphism. Agreement of the scalar profile M_x(k) is necessary for the
event/action readouts, but it is not by itself the complete finite record law.
```

The finite status after the later W-profile campaigns is sharper:

```text
exact finite leg: record/source KL work split;
exact finite leg: W_x deletion/repair and finite-estimation receipts;
open theorem target: causal-order readout;
open theorem target: screen/volume readout;
branch-A gate: canonical cofinal refinement maps.
```

If that principle is realized by a fixed cofinal process, then the visible
objects are readouts:

```text
event threshold, gamma, H_x, T_x, sigma_x, kappa_G, beta,
ICS order, geometry, source, screen response, and TS additivity.
```

If any of the following are supplied externally, the theory is branch B:

```text
P_x, P_{\setminus x}, F_{x,k}, the profile M_x(k), action coefficients,
screen units, source response, beta, R_x, the projection class, local RN
unit rescalings, or sector labels.
```

---

## 1. Why Paper 3 exists

Paper 1 began with the useful slogan:

```text
division-event causal network -> causal set -> geometry.
```

Paper 2 tested that slogan under hostile branch-A pressure. The result was
negative for bare ICS. A locally finite order plus counting volume does not
determine:

```text
P_x;
P_{\setminus x};
F_{x,k};
sigma_x;
H_x and T_x;
kappa_G;
beta;
one-event role identity.
```

The repair was not a small patch. It changed the base object:

```text
bare ICS
  = locally finite causal order + count;

Modular Physical ICS
  = causal-diamond deletion germ whose order projection is a causal set;

CMRP
  = cofinal finite record process whose stable deletion atoms generate
    Modular Physical ICS.
```

Paper 2 could state this endpoint, but not develop the ontology. Paper 3 does
that development.

---

## 2. Primitive ontology [DEF]

### 2.1 Causal diamonds

For each finite refinement level `n`, the process assigns local objects to
causal diamonds:

```text
D               = finite causal diamond;
R_n(D)          = finite local record algebra;
Omega_n(D)      = finite record-history sample space;
P_n(D)          = covariant record-history law on Omega_n(D).
```

The diamond is sealed: only internal record relations and boundary/screen
responses may be used. A preferred outside time coordinate is not part of the
object.

### 2.2 Deletion instrument

For a candidate event germ `x` inside `D`, the ontology includes an intrinsic
deletion/disintegration operation:

```text
D_x : local law with x retained -> local law with x deleted.
```

It produces two local laws:

```text
P_{n,x}              = retained law;
P_{n,\setminus x}    = deleted law.
```

The deletion is not an observer action. It is the finite counterfactual
operation by which the event's physical role is measured.

### 2.3 Intrinsic shell filtration

The event germ includes canonical causal-diamond shells:

```text
F_{n,x,0} subset F_{n,x,1} subset ... subset F_{n,x,K_n}.
```

These shells are not arbitrary smoothing windows. They are part of the sealed
diamond structure. Their job is to say what it means to look at the deletion
response at increasing causal rank.

### 2.4 Absolute continuity

The retained and deleted laws must be locally comparable:

```math
P_{n,x}|F_{n,x,k}
\ll
P_{n,\setminus x}|F_{n,x,k}.
```

Without this finite Radon-Nikodym relation, the local deletion action is
singular and the modular profile is not a finite invariant.

### 2.5 Role readouts

The same event germ has four readouts:

```text
record readout;
source readout;
causal-order readout;
screen/volume readout.
```

They are not four causes. They are four projections of one deletion fact if
and only if they share the same profile `M_x(k)`.

### 2.6 Fixed action

The CMRP action is not a chosen collapse kernel. Its allowed skeleton is:

```text
I_D(P,D_x,F)
= KL/RN deletion record action
+ count-normalized screen/volume gravity response
+ spacelike-additive locality constraint
+ cofinal stability constraint.
```

All surviving coefficients are units:

```text
logarithmic Radon-Nikodym units;
finite count/screen units.
```

If record weights, gravity weights, kernel widths, temperature units, or
screen units are tunable, the theory has moved to branch B.

### 2.7 Cofinal refinement

The process is a cofinal family:

```text
(R_n(D), P_n(D), D_{n,x}, F_{n,x,k})_{n -> infinity}.
```

The event law is physical only if the profile, source response, screen
normalization, and selected scale converge under refinement.

---

## 3. Ontology closure audit [PROBE]

The first Paper 3 diagnostic asks whether a proposed ontology defines all
objects required by Papers 1-2:

```text
code/v6_p3a_cmrp_ontology_closure.py
```

The audit is:

| candidate | rule | P/Q | F | MDP | H/T/s | kG | beta | ICS | TS | role gap | beta span | verdict |
|---|---|---|---|---|---|---|---|---|---|---:|---:|---|
| bare ICS | order+count | no | no | no | no | no | no | no | yes | 0.0000 | 0.0000 | FAIL-NO-RECORD-ALG |
| Modular Physical ICS | MDP primitive | yes | yes | yes | yes | yes | yes | yes | yes | 0.0000 | 0.0000 | PASS-ENRICHED-PRIMITIVE |
| CMRP without fixed action | free variational law | yes | yes | yes | no | no | no | no | yes | 0.0000 | 0.0000 | FAIL-NO-FIXED-ACTION |
| CMRP role split | sector-coupled | yes | yes | yes | yes | no | yes | yes | yes | 0.1144 | 0.0130 | FAIL-ROLE-SPLIT |
| CMRP free units | screen unit chosen | yes | yes | yes | no | no | no | no | yes | 0.0000 | 0.0000 | FAIL-FREE-UNITS |
| CMRP non-isolated | flat profile | yes | yes | yes | yes | yes | no | no | yes | 0.0000 | 0.0000 | FAIL-NO-BETA |
| CMRP TS failure | nonfactorizing | yes | yes | yes | yes | yes | yes | yes | no | 0.0000 | 0.0000 | FAIL-TS |
| CMRP drift | not cofinal | yes | yes | yes | yes | yes | yes | yes | yes | 0.0000 | 0.1226 | FAIL-DRIFT |
| sealed CMRP | fixed role-blind MDP | yes | yes | yes | yes | yes | yes | yes | yes | 0.0000 | 0.0000 | PASS-CMRP-CLOSURE |

This is the main ontology result. Bare ICS does not close. Modular Physical
ICS closes only as an enriched primitive. The only row that closes as a base
is sealed CMRP.

---

## 4. Axiom independence audit [PROBE]

The second diagnostic removes one axiom at a time:

```text
code/v6_p3b_cmrp_axiom_independence.py
```

The finite witness table is:

| removed | appearance | derived break | verdict |
|---|---|---|---|
| local_diamonds | no closed laboratory | no invariant domain | FAIL-NO-DIAMONDS |
| record_algebras | only order remains | no local record law | FAIL-NO-RECORD-ALG |
| process_law | static event set | no retained law P_x | FAIL-NO-PQ |
| deletion | no counterfactual removal | no P_{delete x} | FAIL-NO-PQ |
| shells | unfiltered diamond | no F_{x,k} or shell work | FAIL-NO-F |
| rn_absolute | singular deletion | no finite M_x(k) | FAIL-NO-MDP |
| role_maps | four labels only | no one-event role identity | FAIL-ROLE-SPLIT |
| fixed_action | action chosen later | no H_x/T_x/sigma/beta | FAIL-NO-FIXED-ACTION |
| count_units | screen unit chosen | free kappa_G and beta | FAIL-FREE-UNITS |
| spacelike_additive | ordered updates | TS loop residue | FAIL-TS |
| isolated | flat memory shell | beta not selected | FAIL-NO-BETA |
| cofinal | refinement drift | no continuum limit | FAIL-DRIFT |
| order_projection | record without geometry | no ICS shadow | FAIL-NO-ICS-SHADOW |

This is not a formal proof of minimality. It is a finite independence audit:
under the present theorem target, every axiom has a concrete job.

---

## 5. Observable derivation [PROBE]

The third diagnostic computes the readouts from a sealed finite profile:

```text
code/v6_p3c_cmrp_observable_derivation.py
```

The receipt is:

| object | formula | value | status |
|---|---|---|---|
| event | positive isolated M_x increments | True | PASS |
| gamma | selected event density | 0.14583 | PASS |
| M_x(k) | sealed deletion profile | (0.0000, 0.1853, 0.5707, 1.1764) | PASS |
| w_x(k) | M_x(k+1)-M_x(k) | (0.1853, 0.3854, 0.6057) | PASS |
| isolation | largest shell gap margin | 0.2203 | PASS |
| H_x | cumulative shell work | (0.0000, 0.1853, 0.5707, 1.1764) | PASS |
| T_x | abs(delta V_x)/delta S_screen,x | 1.0000 | PASS |
| sigma_x | exp(-H_x/T_x)/Z_x | (0.3698, 0.3072, 0.2090, 0.1140) | PASS |
| kappa_G | deletion/source response | 0.4065 | PASS |
| c_G | gamma*kappa_G | 0.05928 | PASS |
| beta | source-response beta selector | 0.6016 | PASS |
| stationarity | Gibbs variational residue | 9.89e-17 | PASS |
| ICS shadow | order projection of sealed atoms | defined | PASS |
| TS residue | spacelike additive deletion action | 0 | PASS |

Thus, inside the finite sealed packet, `gamma`, `beta`, `sigma_x`, `H_x`,
`T_x`, and `kappa_G` are not free parameters. They are readouts of the
profile and fixed count/action units.

---

## 6. Derived definitions

This section records the definition chain in theorem-ready form.

### 6.1 Event

An event germ `x` is selected when its deletion profile has a positive,
isolated component:

```text
E_x = { M_x(k+1)-M_x(k) > 0 and the first memory shell is isolated }.
```

The density of selected stable components is `gamma`.

### 6.2 Modular action

The local deletion action is the RN/KL profile:

```math
M_x(k)
=
D\!\left(P_x|F_{x,k}\,\|\,P_{\setminus x}|F_{x,k}\right).
```

The shell work is the chain-rule increment:

```math
w_x(k)=M_x(k+1)-M_x(k).
```

### 6.3 Hamiltonian

The local modular Hamiltonian is cumulative shell work:

```math
H_x(0)=0,
\qquad
H_x(j)=\sum_{k<j} w_x(k).
```

### 6.4 Temperature

The local KMS temperature is the fixed screen/volume count ratio:

```math
T_x
=
{|\delta V_x|\over \delta S_{{\rm screen},x}}.
```

If the numerator or denominator is externally scaled, the temperature is not
derived.

### 6.5 Reference state

The local reference state is:

```math
\sigma_x
=
{e^{-H_x/T_x}\over {\rm tr}(e^{-H_x/T_x})}.
```

This is not a maximum-entropy convention. It is fixed by the deletion work and
screen/volume normalization.

### 6.6 Source response

The one-event gravity/source amplitude is the deletion response of the same
reference state:

```text
kappa_G = deletion/source response of sigma_x.
```

The gravity blur coefficient is not free:

```math
c_G=\gamma\,\kappa_G.
```

### 6.7 Memory scale

The memory scale is read from the isolated first shell of the profile, or
equivalently from the source-response beta selector:

```text
beta = beta(M_x, sigma_x, kappa_G).
```

If two inequivalent profiles give the same first-order order/count data but
different isolated scales, order/count is not the physical invariant.

### 6.8 ICS projection

The causal set is the order projection of sealed deletion atoms:

```text
ICS(D) = order shadow of { x : E_x in D }.
```

This preserves the geometric role of Paper 1 while demoting bare order from
primitive ontology to readout.

### 6.9 TS additivity

For spacelike-separated diamonds:

```math
I_{D_1\cup D_2}
=
I_{D_1}+I_{D_2},
```

and the local threshold/deletion projectors have zero ordering residue. This
is the CMRP version of Tomonaga-Schwinger compatibility.

---

## 7. What Paper 3 proves at finite level

The finite campaign proves:

```text
1. Bare ICS does not define the objects required by branch A-enriched.
2. Modular Physical ICS defines them only as an enriched primitive.
3. Sealed CMRP defines them as a process-level base.
4. Every axiom in the sealed packet has a finite witness failure if removed.
5. The sealed profile computes the visible event, source, memory, reference,
   gravity, and TS readouts in the finite model.
6. A lower-level whole-diamond record-history channel can generate the sealed
   profile without inserting it by hand.
7. The scalar profile is not the complete finite invariant; the full sealed
   deletion germ is required to capture higher-order record correlations.
8. A retained whole-history law alone does not determine the sealed germ.
9. A canonical germ is generated conditionally by a strict event-intervention
   / do-delete structure with fixed ranks, role maps, units, action, and
   cofinal margins.
```

This is a real advance over the Paper 2 endpoint. Paper 2 found the invariant.
Paper 3 turns it into a base ontology.

---

## 8. What Paper 3 does not prove

It does not prove:

```text
that established ISP dynamics uniquely implies CMRP;
that a continuum interacting relativistic CMRP exists;
that the finite record algebras arise from known local QFT;
that the cofinal limit satisfies full field-theoretic microcausality;
that Jacobson/HKT gravity follows without additional regularity hypotheses;
that the finite beta value is the physical value;
that the lower-level whole-diamond record-history law is unique;
that matching scalar MDP alone proves equality of full physical germs;
that established ISP principles already contain the required do-delete law;
that actual sealed diamonds always lie in the isolated RN partition-spectrum
class.
```

Those are not hidden assumptions inside this paper. They are the remaining
existence and continuum theorems.

---

## 9. Main theorem target

**Sealed CMRP theorem target.** Suppose there exists a cofinal family of finite
covariant record processes on causal diamonds with:

```text
1. local record algebras R_n(D);
2. covariant record-history laws P_n(D);
3. intrinsic event variables and unique deletion/intervention maps D_{n,x};
4. canonical shell filtrations F_{n,x,k};
5. finite RN absolute continuity;
6. role-blind sealed deletion germs across record/source/causal/screen readouts;
7. coefficient-free KL/RN plus screen/volume action;
8. fixed count units;
9. positive isolated shell work;
10. spacelike additivity;
11. intrinsic isolated RN partition spectra for R_x;
12. cofinal convergence.
```

Then:

```text
sealed CMRP
-> Modular Physical ICS event germs
-> ICS order projection
-> geometry/source/screen readouts
-> gamma, H_x, T_x, sigma_x, kappa_G, beta
```

with no free threshold, memory width, source amplitude, or screen unit at the
finite level.

---

## 10. Kill criteria

Paper 3 gives clean falsifiers:

```text
same sealed order but different role-blind MDP;
same MDP total but different shell profile and beta;
same profile but free count/screen unit;
same profile but no isolated shell;
same profile but refinement drift;
same event support but split role profiles;
same local profile but nonzero spacelike loop residue.
same scalar MDP but different internally observable shell correlations.
same sealed law but several zero or minimum-positive RN partitions.
same partition spectrum but local/role-dependent RN unit rescaling.
```

Any one of these kills branch A-enriched for the proposed base. It does not
kill branch B; it says the theory must admit a physical modular kernel or
coefficient as an additional law.

---

## 11. Relation to Papers 1 and 2

Paper 1 should now be read as:

```text
CMRP stable deletion atoms -> ICS order shadow -> geometry.
```

Paper 2 should now be read as:

```text
relativistic integrability and memory force the event law upstream of bare ICS.
```

Paper 3 is the upstream ontology:

```text
sealed finite record diamonds with intrinsic modular deletion profiles.
```

The combined status is:

```text
bare branch A: refuted under current assumptions;
branch A-enriched: alive exactly as sealed CMRP;
branch B: honest fallback if CMRP action/profile/units are supplied.
```

---

## 12. Final branch status

The situation after Paper 3 is:

```text
ICS is not the base.
ICS is the geometric order shadow.

Modular Physical ICS is not enough as an explanation.
It is the enriched local event germ.

CMRP is the candidate base.
It is viable only if its fixed action, deletion map, shell filtration,
role-blind profile, isolated RN partition spectrum, count units, isolated
scale, TS additivity, and cofinal limit are derived as one object.
```

That is the honest final form of branch A-enriched.

---

## 13. Feynman route: make the profile come out [PROBE]

The ontology campaign above defines the sealed CMRP object. The Feynman route
asks for more:

```text
Do not start from M_x(k).
Start from a finite lower-level record dynamics and compute M_x(k).
```

The diagnostic is:

```text
code/v6_p3d_feynman_record_channel.py
```

The finite model uses whole-diamond record-history laws over shell bits. The
retained law and deleted law are explicit finite distributions:

```text
P_x(omega)              = law of internal records with x present;
P_{\setminus x}(omega)  = law of internal records with x deleted.
```

The profile is then computed by marginalizing these laws onto the intrinsic
shell filtration:

```math
M_x(k)
=
D(P_x|F_{x,k}\,\|\,P_{\setminus x}|F_{x,k}).
```

The audit is:

| candidate | rule | earned | whole | role gap | total gap | iso | beta span | nonmarkov | verdict |
|---|---|---|---|---:|---:|---:|---:|---:|---|
| hand-sealed profile | profile supplied | no | yes | 0.0000 | 0.0000 | 0.1454 | 0.0000 | 0.0677 | FAIL-HAND-PROFILE |
| Markov shell generator | transition kernel | yes | no | 0.0000 | 0.0000 | 0.1995 | 0.0000 | 0.0000 | FAIL-MARKOV-GENERATOR |
| split-source channel | sector dynamics | yes | yes | 0.2259 | 0.2259 | 0.1294 | 0.0328 | 0.0677 | FAIL-ROLE-SPLIT |
| same total, shell permuted | total KL only | no | yes | 0.3585 | 0.0000 | 0.1454 | 0.0038 | 0.0677 | FAIL-NO-SHELLS |
| free unit channel | unit chosen | no | yes | 0.0000 | 0.0000 | 0.1454 | 0.0000 | 0.0677 | FAIL-FREE-UNITS |
| drifting channel | not cofinal | yes | yes | 0.0000 | 0.0000 | 0.1454 | 0.1226 | 0.0677 | FAIL-DRIFT |
| sealed whole-history channel | finite record law | yes | yes | 0.0000 | 0.0000 | 0.1454 | 0.0000 | 0.0677 | PASS-FEYNMAN-GENERATIVE |

The positive row matters. It shows a finite lower-level route in which the
profile is not supplied; it is computed from retained/deleted whole-history
record laws.

The negative rows matter just as much:

```text
hand profile         = ontology label, not Feynman closure;
Markov generator     = not Barandes-aligned indivisibility;
split-source channel = branch B coupled sectors;
total KL only        = loses shell work and beta information;
free units           = reintroduces kappa_G/beta freedom;
drift                = no cofinal law.
```

Thus the Feynman route condition is:

```text
The sealed profile must be generated by a whole-diamond, role-blind,
non-Markovian record-history law with intrinsic deletion and canonical shells.
```

Here "non-Markovian" is used in the ISP sense. The finite law is a whole
record-history law on the diamond. The local modular Hamiltonian `H_x` is a
derived deletion-work readout; it is not a time-evolution generator.

---

## 14. MDP completeness attack [PROBE]

The next Feynman question is sharper:

```text
Is M_x(k) itself the complete invariant?
```

The answer is no. The diagnostic is:

```text
code/v6_p3e_mdp_completeness_attack.py
```

It constructs finite whole-diamond record laws with the same scalar deletion
profile but different internal higher-order correlations. The audit is:

| candidate | rule | profile gap | beta gap | total gap | corr gap | verdict |
|---|---|---:|---:|---:|---:|---|
| identical sealed germ | identity | 0.0000 | 0.0000 | 0.0000 | 0.0000 | PASS-SAME-GERM |
| same MDP, different correlations | profile matched | 0.0000 | 0.0000 | 0.0000 | 0.0677 | FAIL-MDP-NOT-COMPLETE |
| same total, different profile | total KL matched | 0.3585 | 0.0038 | 0.0000 | 0.0000 | FAIL-TOTAL-NOT-COMPLETE |
| different profile and mechanism | different germ | 0.3585 | 0.0038 | 0.0000 | 0.0677 | FAIL-TOTAL-NOT-COMPLETE |

This refines the ontology. The scalar profile `M_x(k)` computes the modular
action, shell work, beta, reference state, and source/screen readouts. But it
does not encode every observable of the whole finite record law. A sealed
observer who can measure higher-order shell correlations can distinguish two
laws with the same `M_x(k)`.

Therefore the complete primitive is not:

```text
M_x(k) alone.
```

It is:

```text
G_x = (P_x, P_{\setminus x}, F_{x,k}, role maps, fixed units, action),
```

with `M_x(k)` as its scalar modular action profile.

This strengthens rather than weakens Paper 3. The paper already defined CMRP
as a process-level law, not merely as a profile label. The Feynman attack says
why that extra structure is necessary.

---

## 15. Status after the Feynman profile route

The final status is now:

```text
bare ICS:
  refuted as a base;

Modular Physical ICS:
  closes only as an enriched event germ;

scalar MDP:
  necessary and powerful, but not complete as a finite record invariant;

sealed deletion germ G_x:
  complete local event object at finite level;

sealed CMRP:
  candidate process-level base that generates G_x cofinally.
```

The new theorem target is:

```text
derive the full sealed deletion germ G_x from a whole-diamond finite
record-history law, then show its scalar MDP has the positive isolated,
role-blind, TS-additive, cofinally stable profile needed by Papers 1-2.
```

That is the Feynman route in its honest form.

---

## 16. Origin/uniqueness audit for the full germ [PROBE]

The next target is stricter:

```text
whole-diamond ISP record dynamics -> unique/canonical sealed deletion germ G_x.
```

The diagnostic is:

```text
code/v6_p3f_germ_origin_uniqueness_audit.py
```

It asks what is actually forced by a lower-level record law. The audit is:

| candidate | rule | choices | del | shell | role | profile span | beta span | verdict |
|---|---|---:|---|---|---|---:|---:|---|
| no retained law | order shadow | 0 | no | no | no | 0.0000 | 0.0000 | FAIL-NO-P |
| retained law only | P only | 2 | no | no | no | 0.1456 | 0.0188 | FAIL-NONUNIQUE-DELETION |
| free deletion law | same P, many Q | 2 | no | yes | yes | 0.1456 | 0.0188 | FAIL-NONUNIQUE-DELETION |
| free shell filtration | same P/Q, many F | 2 | yes | no | yes | 0.3585 | 0.0038 | FAIL-NONUNIQUE-SHELLS |
| free role map | same support, split role | 2 | yes | yes | no | 0.2259 | 0.0328 | FAIL-NONUNIQUE-ROLES |
| free action/unit germ | scale chosen | 1 | yes | yes | yes | 0.0000 | 0.0000 | FAIL-FREE-UNITS |
| degenerate action minimum | two equal germs | 2 | yes | yes | yes | 0.3585 | 0.0038 | FAIL-DEGENERATE-MINIMUM |
| drifting germ | not cofinal | 1 | yes | yes | yes | 0.0000 | 0.1226 | FAIL-DRIFT |
| intrinsic intervention germ | unique do-delete | 1 | yes | yes | yes | 0.0000 | 0.0000 | PASS-UNIQUE-GERM |

This is the important no-go:

```text
P_x alone does not determine G_x.
```

Even a whole retained record-history law can be paired with different deletion
laws, shell filtrations, role maps, or units. Therefore the lower-level
dynamics must contain more than a distribution over histories. It must contain
an intrinsic event-intervention/deletion structure.

---

## 17. Conditional positive generation class [PROBE]

The positive question is:

```text
What lower-level structure is sufficient to generate G_x canonically?
```

The diagnostic is:

```text
code/v6_p3g_canonical_germ_generation.py
```

The finite audit is:

| candidate | rule | event | do | ranks | role gap | iso | beta span | nonmarkov | germs | verdict |
|---|---|---|---|---|---:|---:|---:|---:|---:|---|
| latent mixture only | no event variable | no | no | yes | 0.0000 | 0.1454 | 0.0000 | 0.0677 | 2 | FAIL-NO-EVENT-VARIABLE |
| event without do-delete | no intervention | yes | no | yes | 0.0000 | 0.1454 | 0.0000 | 0.0677 | 2 | FAIL-NONUNIQUE-DO |
| rank-degenerate event | tied shells | yes | yes | no | 0.0000 | 0.1454 | 0.0000 | 0.0677 | 2 | FAIL-RANK-DEGENERACY |
| role-specific intervention | four sectors | yes | yes | yes | 0.2259 | 0.1294 | 0.0328 | 0.0677 | 1 | FAIL-ROLE-SPLIT |
| free-unit intervention | unit chosen | yes | yes | yes | 0.0000 | 0.1454 | 0.0000 | 0.0677 | 1 | FAIL-FREE-UNITS |
| weak deletion event | no contrast | yes | yes | yes | 0.0000 | 0.0000 | 0.0000 | 0.0677 | 1 | FAIL-NO-ISOLATION |
| drifting intervention | not cofinal | yes | yes | yes | 0.0000 | 0.1454 | 0.1226 | 0.0677 | 1 | FAIL-DRIFT |
| canonical event intervention | strict do-delete | yes | yes | yes | 0.0000 | 0.1454 | 0.0000 | 0.0677 | 1 | PASS-CANONICAL-GERM |

The finite positive class is:

```text
whole-diamond record-history law
+ intrinsic event variable
+ unique do-delete operation
+ strict causal-rank shell labels
+ role-blind response maps
+ fixed units/action
+ positive isolated deletion work
+ non-Markov whole-history residue
+ cofinal stability.
```

This class generates `G_x` rather than selecting it after the fact. But it is
still conditional: the event-intervention/deletion structure is part of the
lower-level law.

---

## 18. Origin decision ledger [PROBE]

The final diagnostic is:

```text
code/v6_p3h_germ_origin_decision.py
```

It separates refuted bases, conditional generation, and the still-open
existence theorem:

| candidate | input | G_x | MDP | beta | status |
|---|---|---|---|---|---|
| bare ICS | order+count | no | no | no | REFUTED |
| retained whole law only | P_x | no | no | no | REFUTED |
| free deletion/shells | P_x plus choices | nonunique | yes | nonunique | REFUTED |
| hand profile | M_x(k) supplied | no | yes | yes | BRANCH-B |
| whole-history channel | P_x,P_delete,F | partial | yes | yes | CONDITIONAL |
| canonical event intervention | strict do-delete law | yes | yes | yes | PASS-CONDITIONAL |
| established ISP alone | current principles | open | open | open | OPEN-THEOREM |

Thus the campaign's verdict is not "we have proved `G_x` from ISP." It is:

```text
The exact finite generation target is now known.
Established ISP must derive a strict canonical event-intervention/deletion law.
Without that law, G_x remains an enriched primitive or branch-B modular kernel.
```

This is a hard endpoint. The next proof cannot be another selector scan. It
must prove that the indivisible whole-diamond record dynamics itself contains
the canonical `do-delete` structure.

---

## 19. Do-delete observational no-go [PROBE]

The next campaign attacks the exact missing theorem:

```text
ISP whole-diamond record dynamics -> canonical do-delete.
```

The first diagnostic is:

```text
code/v6_p3i_isp_do_delete_no_go.py
```

It constructs two finite lower-level mechanisms with the same observed
whole-diamond law:

```text
P(X,Y_shells)
```

but different intervention semantics for deleting `X`.

The audit is:

| candidate | mechanism | same P(X,Y) | profile | beta | nonmarkov | verdict |
|---|---|---|---|---:|---:|---|
| direct event law | X causes shell response | yes | (0.000,0.210,0.504,0.944) | 0.5714 | 0.0677 | COND-ONE-DO |
| hidden-context law | U causes X and shells | yes | (0.000,0.170,0.390,0.690) | 0.5332 | 0.0812 | FAIL-OBSERVATIONAL-DO |

Both mechanisms induce the same observed record-history law. But their
`do-delete` profiles and beta values differ:

```text
beta span = 0.0382.
```

Therefore:

```text
do-delete is not an observational statistic of the whole-history law.
```

This is the causal-intervention no-go in finite ISP form. Non-Markovian
whole-history probabilities are still probabilities; by themselves they do
not determine what happens under an intervention. The intervention structure
must be derived from something stronger than observational equivalence.

---

## 20. ISP-native do-delete derivation audit [PROBE]

The natural ISP-native proposal is:

```text
do-delete = unique minimum-disturbance factorization repair at a division
event atom.
```

The diagnostic is:

```text
code/v6_p3j_isp_do_delete_derivation_audit.py
```

The finite audit is:

| candidate | rule | atom | null | repair | role gap | iso | beta span | nonmarkov | verdict |
|---|---|---|---|---|---:|---:|---:|---:|---|
| conditioning on absence | P(.|X=0) | yes | yes | no | 0.0000 | 0.1454 | 0.0000 | 0.0677 | FAIL-NO-FACTOR-REPAIR |
| erase event only | remove label | yes | yes | no | 0.0000 | 0.0000 | 0.0000 | 0.0677 | FAIL-NO-FACTOR-REPAIR |
| unconstrained KL repair | free projection | yes | yes | yes | 0.0000 | 0.1454 | 0.0000 | 0.0677 | FAIL-DEGENERATE-REPAIR |
| free-null repair | null chosen | yes | no | yes | 0.0000 | 0.1454 | 0.0000 | 0.0677 | FAIL-FREE-NULL |
| role-specific repair | four repairs | yes | yes | yes | 0.2259 | 0.1294 | 0.0328 | 0.0677 | FAIL-ROLE-SPLIT |
| Markov factor repair | semigroup | yes | yes | yes | 0.0000 | 0.1995 | 0.0000 | 0.0000 | FAIL-MARKOV |
| drifting repair | not cofinal | yes | yes | yes | 0.0000 | 0.1454 | 0.1226 | 0.0677 | FAIL-DRIFT |
| division-event repair | unique factor repair | yes | yes | yes | 0.0000 | 0.1454 | 0.0000 | 0.0677 | PASS-ISP-DO-DELETE-TARGET |

The only passing finite target is not conditioning and not label erasure. It
is a structured repair operation:

```text
fixed division-event atom;
fixed null state;
boundary/collar preservation;
unique minimum-disturbance factorization repair;
role-blind response;
non-Markov retained law;
positive isolated deletion work;
cofinal stability.
```

This is the first clean candidate for how ISP could derive do-delete. The
division event is already the place where indivisible dynamics touches
factorization. The new proposal is that deletion is the unique repair that
removes the event atom while restoring the appropriate local factorization and
preserving the sealed boundary data.

But the result is still conditional. The current established ISP framework
does not yet prove the fixed null state or the uniqueness of the
boundary-preserving repair.

---

## 21. Do-delete decision ledger [PROBE]

The final diagnostic is:

```text
code/v6_p3k_do_delete_decision.py
```

The ledger is:

| candidate | do-delete | G_x | status |
|---|---|---|---|
| observed whole-history law | no | no | REFUTED |
| conditioning on absence | apparent | no | REFUTED |
| erasure of label | apparent | no | REFUTED |
| unconstrained KL projection | nonunique | no | REFUTED |
| SCM/Pearl intervention supplied | yes | yes | BRANCH-B/INPUT |
| division-event factor repair | yes | yes | PASS-CONDITIONAL |
| established ISP alone | open | open | OPEN-THEOREM |

The status after this campaign is:

```text
observational ISP whole-history law:
  not enough;

conditioning or erasure:
  not enough;

external intervention semantics:
  branch B/input;

division-event factorization repair:
  the only current ISP-native positive target;

established ISP alone:
  open until the repair principle is proved.
```

Thus the final missing theorem is now extremely specific:

```text
Division-event repair theorem.
At an ISP division-event atom, the theory derives a unique
boundary-preserving minimum-disturbance repair to a fixed null state, and this
repair is role-blind, spacelike additive, positive-isolated, and cofinally
stable.
```

If this theorem is proved, sealed CMRP becomes a derived ISP ontology. If it
fails, sealed CMRP remains the honest branch-B-enriched modular record theory.

---

## 22. Einstein-real-enough campaign [PROBE]

The preceding endpoint sharpens the philosophical pressure. A sealed modular
deletion profile and a fixed CMRP action are strong enough to compute a
conditional theory, but they are not automatically real enough in the
Einstein-principle sense. They can still be downstream of a supplied
intervention structure.

The Einstein test used here is:

```text
An event is real enough only if the closed-diamond law itself determines
which invariant operation counts as deleting the event.
```

This gives seven requirements:

```text
E1. internal invariance: no slicing, frame, observer simultaneity, or external sector label;
E2. complete germ: retained law, deleted law, shells, roles, units, and action are one object;
E3. self-derived intervention: do-delete is not supplied after the fact;
E4. fixed null state: eventless deletion target is intrinsic;
E5. unique repair: deletion is a unique boundary-preserving minimum-disturbance repair;
E6. one-role identity: record/source/causal/screen responses are derivatives of the same repair;
E7. parameter and refinement closure: beta, kappa_G, TS additivity, and cofinal limits come from that repair.
```

The diagnostic is:

```text
code/v6_p3l_einstein_reality_campaign.py
```

The finite audit is:

| candidate | inv | `G_x` | do | null | repair | role gap | beta span | nonmarkov | inputs | verdict |
|---|---|---|---|---|---|---:|---:|---:|---:|---|
| bare ICS order | yes | no | no | no | no | 0.0000 | 0.0000 | 0.0677 | 0 | FAIL-INCOMPLETE-GERM |
| scalar MDP | yes | no | no | yes | no | 0.0000 | 0.0000 | 0.0677 | 2 | FAIL-INCOMPLETE-GERM |
| fixed CMRP action | yes | yes | no | yes | no | 0.0000 | 0.0000 | 0.0677 | 2 | FAIL-DO-SUPPLIED |
| observed non-Markov law | yes | no | no | no | no | 0.0000 | 0.0000 | 0.0677 | 0 | FAIL-OBS-EQUIV |
| external Pearl do | no | yes | no | yes | yes | 0.0000 | 0.0000 | 0.0677 | 1 | FAIL-NONINVARIANT |
| role-sector repair | yes | yes | yes | yes | yes | 0.2259 | 0.0328 | 0.0677 | 0 | FAIL-ROLE-SPLIT |
| Markov factor repair | yes | yes | yes | yes | yes | 0.0000 | 0.0000 | 0.0000 | 0 | FAIL-MARKOV |
| division repair packet | yes | yes | no | yes | no | 0.0000 | 0.0000 | 0.0677 | 2 | FAIL-DO-SUPPLIED |
| self-deleting defect law | yes | yes | yes | yes | yes | 0.0000 | 0.0000 | 0.0677 | 0 | PASS-REAL-ENOUGH-BASE/OPEN-ISP-DERIVATION |
| established ISP alone | yes | no | no | no | no | 0.0000 | 0.0000 | 0.0677 | 0 | FAIL-INCOMPLETE-GERM |

The survivor is not the scalar MDP and not a fixed action sitting on top of a
supplied intervention. The survivor is:

```text
self-deleting factorization-defect law.
```

Finite form. Let `B_x` be the sealed boundary/collar data of the candidate
diamond event and let `N_x(B_x)` be the eventless null-factorization class:

```text
N_x(B_x) =
  finite laws Q that preserve B_x,
  remove the event atom x,
  restore the required local factorization across the x-removal cut,
  preserve spacelike additivity on disjoint collars,
  and remain absolutely continuous with the retained law.
```

Then the deletion law is not supplied. It is the relative-entropy repair:

```math
P_{\setminus x}
=
\operatorname*{argmin}_{Q\in N_x(B_x)}
D(P_x\,\|\,Q).
```

The event action is the corresponding invariant defect:

```math
A_x
=
D(P_x\,\|\,P_{\setminus x}),
```

with shell restrictions giving:

```math
M_x(k)
=
D(P_x|F_{x,k}\,\|\,P_{\setminus x}|F_{x,k}),
\qquad
w_x(k)=M_x(k+1)-M_x(k).
```

The retained-to-repair Radon-Nikodym orientation must be fixed once by the
finite record law and not reselected per event. The finite audit uses the same
orientation throughout.

This is the object that would be real enough. It makes the event the invariant
factorization defect, and makes deletion the unique repair of that defect. The
four roles are then not separate decorations:

```text
record role  = response of local record law under the repair;
source role  = stress/source response of the same repair;
causal role  = order-shadow response of the same repair;
screen role  = screen/volume response of the same repair.
```

The theorem target is therefore stronger and cleaner than "CMRP has a fixed
action":

```text
Self-deleting defect theorem.
For every cofinal finite sealed diamond process, each objective event x is the
unique invariant obstruction to local sealed factorization. The eventless
null-factorization target N_x(B_x) is internally defined and nonempty; either
it is a genuinely convex repair class, or it is a fixed product/exponential
factorization family with a proved KL projection theorem; the entropy repair
P_{\setminus x} exists and is unique; its shell increments are positive and
isolated; the four role derivatives form one full Gram; the selected beta and
kappa_G are functions of this same repair; and the construction is
causal-order invariant, spacelike additive, and refinement stable.
```

If this theorem is adopted as the base law, the object is real enough in the
Einstein sense: no external observer chooses the deletion operation. If the
older ISP principles derive it, branch A-enriched is genuinely derived. If
they do not, the honest base has changed: Paper 3 is no longer bare ICS and no
longer a merely fixed CMRP action; it is a self-deleting modular
factorization-defect process.

---

## 23. Self-deleting defect completeness campaign [PROBE]

The previous section names the real-enough object. This section asks whether
it is actually complete.

The finite challenge is:

```text
Can two internally indistinguishable closed diamonds require different
deletion maps?
```

The answer depends on what "internally indistinguishable" means. If it means
same scalar action, same shell boundary, or same retained law without a fixed
null-factorization target, the ontology is incomplete. If it means the full
self-deleting law:

```text
(P_x, B_x, N_x(B_x), fixed RN orientation, fixed shell order, fixed roles)
```

then the finite repair is unique.

The diagnostic is:

```text
code/v6_p3m_self_deleting_completeness_campaign.py
```

The audit is:

| candidate | readout | same | cut | convex | action gap | repair gap | scale gap | verdict |
|---|---|---|---|---|---:|---:|---:|---|
| same scalar action | `A_x` only | yes | yes | no | 0.0000 | 0.4879 | 0.2914 | FAIL-SCALAR-NOT-COMPLETE |
| same shell boundary | one-shell marginals | yes | yes | no | 0.0178 | 0.0000 | inf | FAIL-BOUNDARY-NOT-COMPLETE |
| same `P`, cut free | `P_x` without `N_x` | yes | no | no | 0.0047 | 0.0119 | 0.6183 | FAIL-CUT-NOT-INTERNAL |
| same boundary, different `P` | boundary not full law | no | yes | no | 0.0154 | 0.0000 | 17.15 | PASS-DISTINGUISHED-BY-FULL-LAW |
| naive product convexity | `N_x` convexity | yes | yes | no | 0.0000 | 0.5040 | 0.0000 | FAIL-NAIVE-CONVEXITY |
| same `P` and same `N_x` | full defect law | yes | yes | no | 0.0000 | 0.0000 | 0.0000 | PASS-FINITE-COMPLETE |

The important counterexample is the cut-free row. The retained law `P_x` is
identical, but two different admissible factorization cuts give two different
repairs:

```text
P_x + cut (0)|(1)|(2)  ->  P_{\setminus x}^{(1)}
P_x + cut (0)|(1,2)    ->  P_{\setminus x}^{(2)}
```

Thus:

```text
P_x alone does not determine do-delete.
```

The full self-deleting law removes the ambiguity by requiring `N_x(B_x)` to
be intrinsic. Once the retained law and the null-factorization target are the
same, the repair is the same:

```text
same P_x + same N_x(B_x) -> same P_{\setminus x}.
```

In the fixed product-partition test, the repair is the product of the retained
group marginals. The finite script samples alternative product repairs and
finds a positive KL margin:

```text
minimum sampled KL margin above product repair = 0.047490.
```

This is not the continuum theorem, but it is the finite chain-rule receipt:
for a fixed product partition, the KL projection is unique.

The campaign also finds a theorem-target correction. A naive product
factorization class is not convex under mixture:

```text
mixture residual showing product-family nonconvexity = 0.135000.
```

Therefore the theorem cannot simply say "the factorization class is convex."
It must prove one of the following:

```text
1. fixed-partition product/exponential projection:
   the intrinsic law fixes the factorization partition and the KL projection
   is unique by the chain rule / information projection theorem;

2. convex repair class:
   the eventless target is not the naive product family but an internally
   defined convex repair set, and strict KL convexity gives uniqueness.
```

The verdict is:

```text
weaker readouts: incomplete;
P_x without N_x: incomplete;
naive convexity claim: false;
full self-deleting law: finite-complete for do-delete uniqueness;
remaining open theorem: derive the intrinsic N_x(B_x), positive shell work,
beta, kappa_G, role Gram, TS additivity, and cofinal stability from the same
law.
```

So the answer to the Einstein test is conditional but encouraging. The
self-deleting defect law is the right kind of principle because it blocks
same-internal/different-delete counterexamples at finite level. But it is only
complete if the null-factorization target is part of the intrinsic law, not a
cut chosen by the theorist after seeing `P_x`.

---

## 24. Intrinsic `N_x(B_x)` origin campaign [PROBE]

The previous section reduced the remaining problem to the origin of the
eventless target:

```text
derive N_x(B_x) intrinsically.
```

This section attacks that target directly. The campaign asks whether the
sealed boundary/collar data can determine the null-factorization target, or
whether `N_x(B_x)` is still a hidden choice.

The diagnostic is:

```text
code/v6_p3n_nx_origin_campaign.py
```

The finite proposal is the **intrinsic collar-separator law**:

```text
B_x -> eventless collar separator relation -> connected components ->
N_x(B_x).
```

In finite form, the sealed collar carries an internally defined eventless
transport/adjacency relation among boundary record atoms after the candidate
event is removed. Its connected components define the factorization blocks.
Then `N_x(B_x)` is not a cut chosen after seeing `P_x`; it is the fixed
product/exponential repair family over those components.

The audit is:

| candidate | rule | intrinsic | partition | sep margin | role gap | action span | repair span | verdict |
|---|---|---|---|---:|---:|---:|---:|---|
| rank-only boundary | shell ranks | no | -- | 0.0000 | 0.0000 | 0.0178 | 0.0441 | FAIL-BOUNDARY-ONLY |
| `P`-only action cut | min action over cuts | yes | 012 | 0.0094 | 0.0000 | 0.0178 | 0.0441 | FAIL-P-ONLY-SELECTOR |
| supplied separator | chosen collar graph | no | 0\|12 | 0.0500 | 0.0000 | 0.0178 | 0.0441 | FAIL-SUPPLIED-SEPARATOR |
| degenerate separator | zero gap collar | yes | 0\|1\|2 | 0.0000 | 0.0000 | 0.0178 | 0.0441 | FAIL-DEGENERATE-SEPARATOR |
| role-split separator | four collar graphs | yes | -- | 0.0000 | 0.0047 | 0.0178 | 0.0441 | FAIL-ROLE-SPLIT |
| drifting separator | not cofinal | yes | 01\|2 | 0.0500 | 0.0000 | 0.0178 | 0.0441 | FAIL-DRIFT |
| intrinsic collar separator | connected components | yes | 0\|1\|2 | 0.0500 | 0.0000 | 0.0178 | 0.0441 | PASS-INTRINSIC-NX-TARGET |

The cut ambiguity without an intrinsic separator is visible:

```text
action span over admissible cuts = 0.017781;
repair distribution span over admissible cuts = 0.044124.
```

The `P`-only action selector is especially instructive. If the theory tries
to select the null target by minimizing action over cuts, the finite audit
selects the trivial all-connected partition:

```text
012.
```

That is not eventless deletion. It is the no-cut option. Thus `N_x(B_x)`
cannot be obtained by asking which cut makes deletion cheapest.

The positive target is instead structural:

```text
Intrinsic collar-separator theorem.
For each sealed event diamond, the boundary/collar data B_x defines a unique
eventless separator relation R_x on collar record atoms. R_x is invariant
under internal relabeling, role-blind across record/source/causal/screen
readouts, has a positive separator margin, and is stable under refinement.
The connected components of R_x define N_x(B_x). The associated
product/exponential information projection is the unique eventless repair
target used by the self-deleting defect law.
```

This is a real derivation of `N_x(B_x)` only if `R_x` is itself internal to
the sealed diamond. If the separator graph is supplied externally, or if
different roles see different separators, or if the separator drifts under
refinement, then `N_x(B_x)` remains branch-B input.

The status after this campaign is:

```text
ranks / shell labels: not enough;
boundary marginals: not enough;
scalar action: not enough;
P_x alone: not enough;
minimum-action cut: fails by choosing the trivial no-cut partition;
supplied separator: branch B;
degenerate separator: unstable;
role-split separator: violates one-event identity;
drifting separator: not cofinal;
intrinsic role-blind collar separator: conditional positive N_x origin.
```

So the next theorem is no longer vague. Branch A-enriched must prove that the
sealed finite record diamond intrinsically carries the eventless collar
separator relation `R_x`. Once `R_x` is proved, `N_x(B_x)` is no longer an
extra primitive: it is the factorization family over the connected components
of `R_x`.

---

## 25. Intrinsic collar-separator theorem campaign [PROBE]

The preceding section left one object exposed:

```text
R_x = eventless collar separator relation.
```

This section asks whether `R_x` is really derived by the sealed diamond or
whether the word "separator" hides a new supplied cut.

The diagnostic is:

```text
code/v6_p3o_intrinsic_collar_separator_theorem.py
```

The finite positive construction is:

```text
sealed collar transfer form T_x
-> sorted internal edge weights
-> unique largest edge gap
-> derived threshold at the gap midpoint
-> strong-edge relation
-> connected components
-> R_x
```

The audit is:

| candidate | rule | intrinsic | partition | gap | margin | invariant | role-blind | verdict |
|---|---|---|---|---:|---:|---|---|---|
| boundary ranks only | no transfer form | no | -- | 0.000 | 0.000 | no | no | FAIL-BOUNDARY-ONLY |
| collar correlations only | no isolated transfer | no | -- | 0.010 | 0.005 | no | no | FAIL-NO-INTRINSIC-TRANSFER |
| supplied threshold | hand cut level | no | 01\|23 | 0.700 | 0.350 | yes | yes | FAIL-SUPPLIED-THRESHOLD |
| node-label separator | first two nodes | no | 01\|23 | 0.000 | 0.000 | no | yes | FAIL-RELABELING |
| tied edge gap | two equal gaps | yes | -- | 0.300 | 0.150 | no | no | FAIL-NONUNIQUE-GAP |
| role-split transfer | four transfer forms | yes | -- | 0.700 | 0.350 | no | no | FAIL-ROLE-SPLIT |
| drifting transfer | not cofinal | yes | 02\|13 | 0.700 | 0.350 | yes | yes | FAIL-DRIFT |
| intrinsic gap transfer | unique edge gap | yes | 01\|23 | 0.700 | 0.350 | yes | yes | PASS-COLLAR-SEPARATOR-TARGET |

The positive row derives the threshold rather than supplying it:

```text
selected partition = 01|23;
derived threshold = 0.470;
edge gap = 0.700;
stability margin = 0.350.
```

This is the finite theorem form:

```text
Gap-isolated collar-separator theorem.
Let the sealed boundary/collar data B_x define a symmetric, role-blind,
internally labeled collar transfer form T_x on finite collar record atoms.
If the sorted edge weights of T_x have a unique largest gap with a positive
cofinal margin, then the midpoint of that gap defines a canonical strong-edge
relation. Its connected components define a separator R_x. The construction
is invariant under internal relabeling, role-blind, and stable under
perturbations smaller than the gap margin.
```

This theorem is not the same as deriving `R_x` from generic boundary data.
The negative rows matter:

```text
boundary ranks: no transfer form;
raw correlations without isolated transfer: no separator;
hand threshold: branch B;
node-label cut: violates relabeling invariance;
tied edge gaps: no unique separator;
role-split transfer: violates one-event identity;
drift: no cofinal separator.
```

Thus the real branch-A-enriched theorem target is now:

```text
sealed diamond law -> role-blind collar transfer form T_x
                   -> unique isolated edge gap
                   -> R_x
                   -> N_x(B_x)
                   -> unique do-delete repair.
```

If `T_x` is an intrinsic record-transport object of the sealed diamond, and
if its edge gap is isolated cofinally, then `R_x` is genuinely derived. If
`T_x` or the gap threshold is supplied externally, `N_x(B_x)` remains branch-B
input.

---

## 26. Intrinsic `T_x` origin campaign [PROBE]

The preceding theorem still exposes one upstream object:

```text
T_x = collar transfer form.
```

The Einstein pressure is that `T_x` must not be a graph, metric, kernel, or
edge weight chosen by the theorist. It must be the unique invariant expression
of record transport across the eventless collar.

The diagnostic is:

```text
code/v6_p3p_tx_origin_campaign.py
```

The finite positive proposal is:

```math
T_x(i,j)
=
I\!\left(Y_i;Y_j\,\middle|\,Y_{\partial x\setminus\{i,j\}}\right),
```

computed in fixed KL/nat units from the eventless sealed collar law. This is
the conditional information carried directly between collar atoms after all
other collar atoms are conditioned out. It is symmetric, nonnegative, and
invariant under internal relabeling.

The audit is:

| candidate | rule | intrinsic | units | partition | gap | margin | invariant | role-blind | verdict |
|---|---|---|---|---|---:|---:|---|---|---|
| boundary ranks only | none | no | yes | -- | 0.000 | 0.000 | no | no | FAIL-NO-EVENTLESS-LAW |
| pair information | pair-information | yes | yes | 0123 | 0.000 | 0.000 | yes | yes | FAIL-HIDDEN-COMMON-CAUSE |
| covariance transport | covariance | yes | yes | -- | 0.000 | 0.000 | yes | no | FAIL-NONUNIQUE-GAP |
| supplied transfer | hand kernel | no | yes | 01\|23 | 0.396 | 0.198 | no | yes | FAIL-SUPPLIED-T |
| node-label transfer | node-label | no | yes | 01\|23 | 1.000 | 0.500 | no | yes | FAIL-RELABELING |
| free-unit CMI | regraduated-conditional | yes | no | 01\|23 | 0.619 | 0.309 | yes | yes | FAIL-FREE-UNITS |
| tied CMI law | conditional-information | yes | yes | 0123 | 0.000 | 0.000 | yes | yes | FAIL-NO-GAP-MARGIN |
| role-split CMI | conditional-information | yes | yes | -- | 0.396 | 0.198 | yes | no | FAIL-ROLE-SPLIT |
| drifting CMI | conditional-information | yes | yes | 02\|13 | 0.396 | 0.198 | yes | yes | FAIL-DRIFT |
| conditional-information transport | conditional-information | yes | yes | 01\|23 | 0.396 | 0.198 | yes | yes | PASS-INTRINSIC-TX-TARGET |

The positive row gives:

```text
selected partition = 01|23;
derived threshold = 0.198167;
edge gap = 0.396106;
stability margin = 0.198053.
```

The negative rows are important. Pair mutual information fails because common
causes can make all collar atoms look mutually connected. Covariance fails
because it is not a complete transport expression and can leave no unique
gap. A supplied kernel and a node-label transport fail the Einstein test.
Regraduating the conditional information keeps the separator but loses the
unique numeric `T_x`; fixed KL/nat units are therefore part of the theorem.

The finite theorem target becomes:

```text
Conditional-information transport theorem.
For each sealed eventless collar law, the intrinsic record-transport form is
the fixed-unit conditional mutual information matrix

  T_x(i,j)=I(Y_i;Y_j | Y_{\partial x\setminus {i,j}}).

It is invariant under internal relabeling, role-blind across
record/source/causal/screen readouts, has a unique isolated edge gap
cofinally, and is stable under refinement. Its gap defines the collar
separator R_x, whose connected components define N_x(B_x).
```

This is the current Einstein-satisfying chain:

```text
sealed eventless collar law
-> fixed-unit conditional-information transport T_x
-> unique isolated edge gap
-> separator R_x
-> null target N_x(B_x)
-> unique do-delete repair
-> shell work, role derivatives, beta, kappa_G, TS receipts.
```

The remaining caveat is sharp. This campaign does not prove that every
physical sealed diamond has an eventless collar law with a cofinally isolated
conditional-information gap. It proves that if such a law exists, `T_x` is no
longer an added graph: it is an internally computed information-transport
object. If the eventless collar law or the fixed KL units are supplied from
outside, the construction remains branch B.

---

## 27. Eventless/event-producing invariant campaign [PROBE]

The previous section still leaves the most Einstein-like question:

```text
What invariant fact inside a sealed finite diamond distinguishes eventless
record transport from event-producing record transport?
```

The answer cannot be "no record transport." An eventless collar may carry real
transport between boundary atoms. It also cannot be one-point marginals, total
entropy, raw pairwise information, an external click label, or a supplied null
state. All of those can be held fixed or chosen without identifying the
objective event.

The diagnostic is:

```text
code/v6_p3q_eventless_defect_campaign.py
```

The finite positive proposal is the **cross-separator factorization defect**.
Let `R_x` be the intrinsic collar separator and let `Pi_{R_x}(P)` be the
finite product/exponential projection over the `R_x` components preserving
each component marginal. Define:

```math
\Delta_x(P)
=
D\!\left(P\,\middle\|\,\Pi_{R_x}(P)\right).
```

Then:

```text
eventless record transport    = internal transport with Delta_x = 0;
event-producing record law    = internal transport plus isolated Delta_x > 0;
do-delete repair              = Pi_{R_x}(P).
```

The audit is:

| candidate | rule | intrinsic | partition | defect0 | defect1 | margin | transport drift | role-blind | repair | verdict |
|---|---|---|---|---:|---:|---:|---:|---|---|---|
| boundary marginals only | marginals | yes | 01\|23 | 0.0000 | 0.1607 | 0.1607 | 1.110e-16 | yes | yes | FAIL-NOT-DEFECT-INVARIANT |
| total entropy only | entropy | yes | 01\|23 | 0.0000 | 0.1607 | 0.1607 | 1.110e-16 | yes | yes | FAIL-NOT-DEFECT-INVARIANT |
| raw transport strength | raw transport | yes | 01\|23 | 0.0000 | 0.2846 | 0.2846 | 1.665e-16 | yes | yes | FAIL-NOT-DEFECT-INVARIANT |
| supplied click label | external click | no | 01\|23 | 0.0000 | 0.1607 | 0.1607 | 1.110e-16 | yes | yes | FAIL-SUPPLIED-CLICK-LABEL |
| supplied null law | cross-separator KL defect | no | 01\|23 | 0.0000 | 0.1607 | 0.1607 | 1.110e-16 | yes | yes | FAIL-SUPPLIED-NULL |
| no sealed law | cross-separator KL defect | no | -- | 0.0000 | 0.0000 | 0.0000 | 0.000e+00 | no | no | FAIL-NO-SEALEDDIAMOND-LAW |
| free-unit defect | cross-separator KL defect | yes | 01\|23 | 0.0000 | 0.1607 | 0.1607 | 1.110e-16 | yes | yes | FAIL-FREE-UNITS |
| role-split defect | cross-separator KL defect | yes | -- | 0.0000 | 0.1607 | 0.1607 | 1.110e-16 | no | yes | FAIL-ROLE-SPLIT |
| small defect | cross-separator KL defect | yes | 01\|23 | 0.0000 | 0.0071 | 0.0071 | 2.776e-16 | yes | yes | FAIL-NO-ISOLATED-DEFECT |
| drifting defect | cross-separator KL defect | yes | 01\|23 | 0.0000 | 0.1607 | 0.1607 | 1.110e-16 | yes | yes | FAIL-DRIFT |
| cross-separator factorization defect | cross-separator KL defect | yes | 01\|23 | 0.0000 | 0.1607 | 0.1607 | 1.110e-16 | yes | yes | PASS-EVENTLESS-DEFECT-TARGET |

The positive receipt gives:

```text
one-point marginal span(eventless,event) = 1.110e-16;
entropy(eventless) = 1.996551;
entropy(event) = 1.835869;
entropy(entropy-matched eventless) = 1.835757;
Delta(entropy-matched eventless) = 0.000000;
Delta(eventless) = 0.000000;
Delta(event) = 0.160682;
Delta(repair(event)) = 0.000000;
KL(event || repair(event)) = 0.160682;
internal transport drift under repair = 1.110e-16;
partition = 01|23.
```

This is the key conceptual separation. Eventless does not mean empty,
uncorrelated, or inactive. It means the record transport factorizes across the
intrinsic collar separator. Event-producing means there is a positive,
isolated cross-separator RN/KL obstruction to that factorization.

The finite theorem target is:

```text
Eventless defect theorem.
Given a sealed finite diamond with an intrinsic role-blind collar separator
R_x and fixed KL/RN units, the invariant distinguishing eventless transport
from an event-producing law is

  Delta_x(P)=D(P || Pi_{R_x}(P)).

Eventless laws are exactly the zero-defect laws. Event-producing laws have
Delta_x bounded below cofinally. The deletion law is the unique
boundary-preserving minimum-disturbance repair Pi_{R_x}(P), which preserves
internal collar transport and removes only the cross-separator defect.
```

This moves the chain one notch closer to a principle:

```text
sealed diamond law
-> intrinsic eventless separator R_x
-> cross-separator defect Delta_x
-> eventless/event-producing distinction
-> unique do-delete repair
-> shell work, role derivatives, beta, kappa_G, TS receipts.
```

The caveat also becomes cleaner. The campaign proves the invariant distinction
inside the positive class; it does not prove that every physical sealed
diamond intrinsically supplies a gap-isolated `R_x` and fixed RN units. If
`R_x`, the projection class, or the KL units are supplied externally, the
eventless/event-producing distinction is still branch B.

---

## 28. Intrinsic `R_x` and RN-unit resolution campaign [PROBE]

The previous caveat had two remaining objects:

```text
R_x = intrinsic collar separator;
fixed RN/KL units = no local action rescaling.
```

Einstein's version of the demand is stricter than "we can choose a nice
separator." The sealed diamond must itself say where the eventless cut is, and
it must do so in an action unit that is not fitted per diamond or per role.

The diagnostic is:

```text
code/v6_p3r_intrinsic_rx_units_resolution.py
```

The finite derivation rule is:

```text
1. Enumerate all nontrivial collar partitions R.
2. For each R compute Delta_R(P)=D(P || Pi_R(P)).
3. If exactly one nontrivial R has Delta_R(P)=0, the law is eventless
   with intrinsic separator R.
4. If no nontrivial zero exists and exactly one R minimizes positive
   Delta_R(P), with a positive floor and isolation margin, the law is
   event-producing with intrinsic separator R.
5. Use the log Radon-Nikodym action. Its chain rule makes it additive under
   sealed composition. A global bits/nats conversion is notation; local or
   role-dependent rescaling is extra physics.
```

The audit is:

| candidate | rule | intrinsic | status | partition | defect | margin | unit error | unit drift | role-blind | verdict |
|---|---|---|---|---|---:|---:|---:|---:|---|---|
| order/counts only | no probability law | no | none | -- | 0.0000 | 0.0000 | 3.469e-18 | 0.000e+00 | no | FAIL-NO-SEALEDDIAMOND-LAW |
| supplied separator | hand R_x | no | supplied | 01\|23 | 0.1607 | 0.0000 | 0.000e+00 | 0.000e+00 | yes | FAIL-SUPPLIED-RX |
| node-label separator | label R_x | no | label | 01\|23 | 0.1607 | 0.0000 | 0.000e+00 | 0.000e+00 | yes | FAIL-RELABELING |
| eventless factorization | zero RN defect scan | yes | eventless | 01\|23 | 0.0000 | 0.3880 | 3.469e-18 | 0.000e+00 | yes | PASS-EVENTLESS-RX |
| fully independent collar | zero RN defect scan | yes | ambiguous-zero | -- | 0.0000 | 0.0000 | 3.469e-18 | 0.000e+00 | no | FAIL-NONUNIQUE-RX |
| symmetric tied law | minimum RN defect scan | yes | ambiguous-positive | -- | 0.3812 | 0.0000 | 2.776e-17 | 0.000e+00 | no | FAIL-NONUNIQUE-RX |
| role-split minimum | minimum RN defect scan | yes | event | -- | 0.1607 | 0.2273 | 0.000e+00 | 0.000e+00 | no | FAIL-ROLE-SPLIT |
| small positive minimum | minimum RN defect scan | yes | event | 01\|23 | 0.0071 | 0.3809 | 6.939e-18 | 0.000e+00 | yes | FAIL-NO-SOURCE-FLOOR |
| drifting minimum | minimum RN defect scan | yes | event | 01\|23 | 0.1607 | 0.2273 | 0.000e+00 | 0.000e+00 | yes | FAIL-DRIFT |
| sqrt regraduation | minimum defect scan | yes | event | 01\|23 | 0.1607 | 0.2273 | 1.875e-01 | 0.000e+00 | yes | FAIL-NONADDITIVE-SCORE |
| local RN rescale | minimum defect scan | yes | event | 01\|23 | 0.1607 | 0.2273 | 0.000e+00 | 7.000e-01 | yes | FAIL-FREE-RN-UNIT |
| role RN rescale | minimum defect scan | yes | event | 01\|23 | 0.1607 | 0.2273 | 0.000e+00 | 4.500e-01 | no | FAIL-FREE-RN-UNIT |
| global bits convention | minimum RN defect scan | yes | event | 01\|23 | 0.1607 | 0.2273 | 0.000e+00 | 0.000e+00 | yes | PASS-GLOBAL-CONVENTION |
| minimum positive RN defect | minimum RN defect scan | yes | event | 01\|23 | 0.1607 | 0.2273 | 0.000e+00 | 0.000e+00 | yes | PASS-INTRINSIC-RX-RN |

The positive target receipt is:

```text
derived status = event;
derived partition = 01|23;
minimum RN defect = 0.160682;
isolation margin = 0.227337;
lowest five partition defects:
  01|23   0.160682
  012|3   0.388019
  0|123   0.388019
  013|2   0.443389
  023|1   0.443389
RN chain error = 0.000e+00;
sqrt-score chain error = 1.875e-01.
```

Thus `R_x` is not an extra object in the positive finite class. It is the
unique nontrivial zero-defect partition for eventless laws, or the unique
minimum positive RN-defect partition for event-producing laws. The fixed unit
is also not a fitted coefficient: the RN action is the logarithm of the
likelihood ratio, fixed by additivity under sealed composition. Writing the
same number in bits rather than nats is a global convention, not a new local
physical parameter.

The finite theorem target is:

```text
Intrinsic separator/RN-unit theorem.
Let P_x be a sealed finite diamond law on collar record atoms. If the
nontrivial partition spectrum

  { Delta_R(P_x)=D(P_x || Pi_R(P_x)) }

has either:

  (i) one isolated zero partition R_x, or
  (ii) no zero partition and one isolated positive minimizer R_x with a
       cofinal source floor,

and if the same R_x is obtained by all record/source/causal/screen readouts
under refinement, then R_x and the RN action unit are intrinsic. The
eventless/event-producing distinction, deletion repair, and downstream
modular observables are then fixed without a supplied separator or local
unit coefficient.
```

But this is not a universal theorem for arbitrary sealed laws. The failure
rows are real counterexamples:

```text
fully independent laws: too many zero partitions;
symmetric tied laws: several equally good positive partitions;
role-split laws: different readouts select different partitions;
small defects: no source floor;
drifting laws: no cofinal identity;
sqrt/regraduated scores: no sealed-composition additivity;
local/role RN rescalings: extra physical units.
```

This resolves the previous caveat rather than hiding it. Branch A-enriched is
closed only for the **isolated RN partition-spectrum class**. If the proposed
physical ontology does not force actual event diamonds into that class, branch
B remains the honest interpretation.

---

## 29. IMFD ontology and genericity campaign [PROBE]

The preceding campaign identifies the exact class. This section names the
ontology and asks whether it is produced generically by dynamics or merely
selected by an admissibility condition.

The beautiful form is:

```text
Physical event =
role-blind, refinement-stable, source-floored isolated
Radon-Nikodym factorization defect of a sealed finite record diamond.
```

Call this an **isolated modular factorization defect** (IMFD). Its finite data
are:

```text
sealed law P_x on collar records;
partition spectrum Delta_R(P_x)=D(P_x || Pi_R(P_x));
unique isolated zero or positive-minimum partition R_x;
log RN action unit;
minimum-disturbance do-delete repair Pi_{R_x}(P_x);
role-blind agreement across record/source/causal/screen readouts;
cofinal refinement stability.
```

The diagnostic is:

```text
code/v6_p3s_imfd_genericity_campaign.py
```

The audit is:

| candidate | dynamics | unique | floor | role | stable | unit | verdict |
|---|---|---:|---:|---:|---:|---|---|
| one random sealed law | full-support simplex | 1.000 | 0.526 | 1.000 | 1.000 | yes | PASS-SINGLE-LAW-GENERIC/NOT-FULL-PHYSICS |
| near-uniform random law | weak-defect simplex | 1.000 | 0.000 | 1.000 | 1.000 | yes | FAIL-NO-SOURCE-FLOOR |
| independent role laws | four generic readouts | 1.000 | 0.082 | 0.008 | 1.000 | yes | FAIL-ROLE-BLIND-NOT-GENERIC |
| role-tied random law | one law four readouts | 1.000 | 0.526 | 1.000 | 1.000 | yes | COND-DYNAMICAL-ROLE-IDENTITY |
| fully independent collar | degenerate eventless | 0.000 | 0.000 | 1.000 | 1.000 | yes | FAIL-NONUNIQUE-ZERO |
| symmetric tied dynamics | exchangeable law | 0.000 | 0.000 | 1.000 | 1.000 | yes | FAIL-SYMMETRY-NONUNIQUE |
| IMFD open neighborhood | stable CMRP toy | 1.000 | 1.000 | 1.000 | 1.000 | yes | PASS-DYNAMICAL-OPEN-CLASS |
| large perturbation | leaves neighborhood | 1.000 | 0.975 | 1.000 | 0.975 | yes | COND-MARGIN-DEPENDENT |
| arbitrary refinement drift | independent scales | 1.000 | 0.526 | 1.000 | 0.000 | yes | FAIL-NO-COFINAL-STABILITY |
| sqrt unit | non-log score | 1.000 | 1.000 | 1.000 | 1.000 | no | FAIL-NONADDITIVE-UNIT |
| log RN unit | sealed composition | 1.000 | 1.000 | 1.000 | 1.000 | yes | PASS-UNIT-FIXED-UP-TO-GLOBAL-CONVENTION |

The result has two layers.

First, for a single full-support finite law, isolated positive minimizers are
generic. The functions

```math
\Delta_R(P)=D(P||\Pi_R(P))
```

are real-analytic on the positive probability simplex. Equalities
`\Delta_R(P)=\Delta_S(P)` are tie hypersurfaces unless forced by symmetry.
Thus a random full-support law almost surely has a unique minimum of the
partition spectrum. This is why the first row has unique rate `1.000`.

Second, a physical event is not just one generic minimum. It needs:

```text
positive source floor;
role-blind equality of the four readouts;
fixed log RN unit;
cofinal refinement stability.
```

Those are not generic for arbitrary dynamics. Four independent generic
readouts almost never pick the same partition. Near-uniform laws have unique
minima but no event floor. Symmetric dynamics can live entirely on tie
surfaces. Independent refinements wander through different partitions even
when each scale has a unique minimum.

Therefore the genericity theorem is conditional:

```text
IMFD open-class theorem.
Within the finite positive simplex, the subset of laws with one isolated
source-floored RN partition minimizer is open. If the CMRP dynamics ties the
four role readouts to the same law and its refinement maps stay inside that
open neighborhood cofinally, then the event, R_x, RN unit, do-delete repair,
and downstream modular readouts are derived.
```

The no-go is equally important:

```text
Genericity no-go for arbitrary dynamics.
Single-law uniqueness does not imply branch-A closure. Without a dynamics
that forces role-blindness, source floor, log RN units, and cofinal stability,
the IMFD class is an admissibility axiom rather than a derived ontology.
```

This is the final Einstein pressure point for Paper 3:

```text
Find or prove a fixed CMRP dynamics whose stable local diamonds are IMFDs.
```

If that theorem is proved, branch A-enriched becomes a genuine derived event
theory. If it is imposed as a filter on allowed diamonds, branch B remains the
honest interpretation, albeit now with a sharply defined modular event kernel.

---

## 30. Fixed CMRP dynamics for IMFDs [PROBE]

The preceding section made the remaining target exact. This section asks for a
fixed finite dynamics, not merely an admissibility filter:

```text
Find a fixed CMRP dynamics whose stable local diamonds are IMFDs.
```

The diagnostic is:

```text
code/v6_p3t_fixed_cmrp_imfd_dynamics.py
```

The finite positive construction is a **spectrum-flow CMRP**:

```text
1. Given a sealed local law P, compute the intrinsic RN partition spectrum.
2. If P has a unique minimizer R(P), use that separator internally.
3. Flow to a fixed log-linear record law E_R(J0,K0).
4. J0 and K0 are fixed constants of the dynamics, not chosen per event.
5. Copy the same law to record/source/causal/screen readouts.
6. Use the log RN action unit.
```

In the finite receipt:

```text
J0 = 1.15;
K0 = 0.62.
```

The separator is not supplied to the readout. It is first recovered from the
RN partition spectrum of the sealed law, and only then used by the fixed
dynamical map.

The audit is:

| candidate | rule | intrinsic | partition | defect | margin | role | stable | fixed | unit | verdict |
|---|---|---|---|---:|---:|---|---:|---|---|---|
| no probability dynamics | order/counts | no | -- | 0.0000 | 0.0000 | no | 0.000 | yes | yes | FAIL-NO-SEALEDDIAMOND-LAW |
| independent Markov collar | spectrum-flow CMRP | yes | -- | 0.0000 | 0.0000 | no | 0.000 | yes | yes | FAIL-NONUNIQUE-RX |
| exchangeable dynamics | spectrum-flow CMRP | yes | -- | 0.0000 | 0.0000 | no | 0.000 | yes | yes | FAIL-NONUNIQUE-RX |
| supplied-R flow | spectrum-flow CMRP | no | 01\|23 | 0.1607 | 0.2273 | yes | 1.000 | yes | yes | FAIL-SUPPLIED-RX |
| free-source flow | spectrum-flow CMRP | yes | 01\|23 | 0.2136 | 0.1744 | yes | 1.000 | no | yes | FAIL-FREE-SOURCE-AMPLITUDE |
| weak-source flow | spectrum-flow CMRP | yes | 01\|23 | 0.0071 | 0.3809 | yes | 0.000 | yes | yes | FAIL-NO-SOURCE-FLOOR |
| role-split flow | spectrum-flow CMRP | yes | -- | 0.1607 | 0.2273 | no | 0.000 | yes | yes | FAIL-ROLE-SPLIT |
| drifting refinement flow | spectrum-flow CMRP | yes | 01\|23 | 0.1607 | 0.2273 | yes | 0.011 | yes | yes | FAIL-NO-COFINAL-STABILITY |
| sqrt-action flow | spectrum-flow CMRP | yes | 01\|23 | 0.1607 | 0.2273 | yes | 1.000 | yes | no | FAIL-NONADDITIVE-UNIT |
| large-noise flow | spectrum-flow CMRP | yes | 01\|23 | 0.1607 | 0.2273 | yes | 0.967 | yes | yes | FAIL-NO-COFINAL-STABILITY |
| fixed spectrum-flow CMRP | spectrum-flow CMRP | yes | 01\|23 | 0.1607 | 0.2273 | yes | 1.000 | yes | yes | PASS-FIXED-CMRP-IMFD |

The positive receipt is:

```text
Phi(P): derive R(P) from the RN partition spectrum, then flow to the
fixed log-linear law E_R(J0,K0) with J0=1.15 and K0=0.62.
derived partition = 01|23;
RN defect = 0.160682;
isolation margin = 0.227337;
stability rate = 1.000;
log-RN chain error = 0.000e+00.
```

This is a genuine finite existence result:

```text
Fixed spectrum-flow theorem.
There exists a finite role-tied CMRP dynamics Phi such that every stable
local diamond in its IMFD basin has:

  unique intrinsic R_x;
  source-floored RN defect;
  fixed log RN unit;
  role-blind record/source/causal/screen readouts;
  cofinal stability under small refinements.

Thus stable local diamonds of Phi are IMFDs without supplying R_x,
K0, or the action unit per event.
```

The failures define the theorem boundary. A Markov/independent collar gives
too many zero partitions. Exchangeable dynamics live on tie surfaces. A
supplied separator is branch B. A free source amplitude reintroduces a model
constant. A weak fixed source has no event floor. Role-split dynamics violate
one-event identity. Drift and large noise leave the IMFD basin. Non-log
scores lose sealed-composition additivity.

Therefore Paper 3 now has a finite branch-A-enriched construction:

```text
fixed spectrum-flow CMRP
-> stable IMFD diamonds
-> intrinsic R_x, RN unit, do-delete repair
-> modular event readouts.
```

The remaining open theorem is no longer "can any fixed dynamics do it?" The
finite answer is yes. The remaining theorem is physical:

```text
derive the spectrum-flow CMRP, or an equivalent fixed IMFD-generating
dynamics, from the deeper ISP/record principle rather than proposing it as
the new dynamical law.
```

If spectrum-flow CMRP is adopted as the primitive dynamics, branch A-enriched
is internally coherent at the finite level. If one demands derivation from a
preexisting ISP law and no such derivation is found, the theory is branch B
with a fixed modular event dynamics.

---

## 31. Invariant origin of spectrum-flow CMRP [PROBE]

The previous section exhibits a fixed finite dynamics. This section asks the
harder Einstein question:

```text
Can the spectrum-flow CMRP itself be derived from a deeper invariant record
principle?
```

The diagnostic is:

```text
code/v6_p3u_spectrum_flow_origin_campaign.py
```

The finite result is mixed. The invariant requirements derive the **form**:

```text
sealed law P
-> RN partition spectrum
-> intrinsic minimizer R(P)
-> log-RN additive action
-> maximum-entropy log-linear law on the selected sufficient statistics.
```

But they do not derive the numerical source-work amplitude. At fixed internal
work `J0`, there is an open family of source amplitudes `K` whose dynamics are
all stable, role-blind, log-RN additive, and IMFD-generating.

The audit is:

| candidate | principle | form | R_x | unit | K span | chosen K | defect | margin | stable | verdict |
|---|---|---|---|---|---:|---:|---:|---:|---:|---|
| order/count invariance | causal order only | no | no | yes | 0.000 | -- | 0.0000 | 0.0000 | 0.000 | FAIL-NO-PROBABILITY-LAW |
| RN spectrum only | partition spectrum | partial | yes | yes | 0.700 | -- | 0.0000 | 0.0000 | 1.000 | FAIL-K-FAMILY |
| max entropy only | least assumption | yes | no | yes | 0.000 | 0.000 | 0.0000 | 0.0000 | 0.000 | FAIL-NO-EVENT |
| minimum norm with floor | floor constrained | yes | yes | yes | 0.000 | 0.275 | 0.0364 | 0.3516 | 0.617 | FAIL-SUPPLIED-FLOOR |
| balanced defect/margin | critical balance | yes | yes | yes | 0.000 | 0.700 | 0.1958 | 0.1922 | 1.000 | COND-SUPPLIED-BALANCE-PRINCIPLE |
| free K spectrum-flow | fixed form/free scalar | yes | yes | yes | 0.700 | 0.325-1.025 | 0.1847 | 0.2033 | 1.000 | FAIL-FREE-SOURCE-SCALAR |
| fixed work normalization | fixed J0,K0 work units | yes | yes | yes | 0.000 | 0.620 | 0.1607 | 0.2273 | 1.000 | PASS-CONDITIONAL-DERIVATION |

The open-family counterexample is:

```text
fixed internal work J0 = 1.150;
passing K values = 29;
K range = 0.325..1.025;
K span = 0.700;

K=0.325: status=event, R=01|23, defect=0.050149,
         margin=0.337870, stable=1.000;
K=0.620: status=event, R=01|23, defect=0.160682,
         margin=0.227337, stable=1.000;
K=1.025: status=event, R=01|23, defect=0.338242,
         margin=0.049777, stable=0.994;

log-RN chain error at K0 = 0.000e+00.
```

This is a negative theorem for the current invariant packet:

```text
Spectrum-flow scalar no-go.
The invariants

  internal isomorphism;
  RN partition-spectrum selection;
  log-RN additivity;
  maximum-entropy log-linear form;
  role tying;
  source floor;
  local refinement stability

do not determine the numerical source-work amplitude K. There is an open
family of fixed spectrum-flow CMRPs with different K values and the same
Einstein-admissible structural properties.
```

The conditional positive theorem is:

```text
Fixed work-normalized spectrum-flow theorem.
If the deeper record principle supplies one additional invariant scalar
normalization, for example a deletion-work quantum or screen/volume response
unit fixing (J0,K0), then the spectrum-flow CMRP is derived at finite level:

  sealed law -> R(P) -> E_R(J0,K0) -> stable IMFD.
```

Therefore the campaign does not leave the target vague. It says exactly what
is missing:

```text
derive the universal source-work normalization K0.
```

Without that scalar, spectrum-flow is a one-parameter family of fixed modular
dynamics. With that scalar derived from the same sealed record principle,
branch A-enriched would be closed at the finite theorem level.

---

## 32. K0 origin campaign: scalar no-go and the work-profile invariant [PROBE]

The previous section ended at one missing number. This section attacks that
number directly:

```text
Can K0 be derived intrinsically?
```

The diagnostic is:

```text
code/v6_p3v_k0_origin_campaign.py
```

The answer is not the answer one would want, but it is clean. The old finite
choice

```text
J0 = 1.150,
K0 = 0.620
```

is not derived by the current CMRP/IMFD packet. It is identifiable from the
full supplied log-linear law, but identifiability is not derivation. A finite
observer can read off which member of a family has been supplied; that does
not explain why the universal dynamics selected that member.

The selector audit is:

| candidate | invariant used | fixed J | selected | K span | defect | isolation | stable | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| current structural packet | status/R/unit/floors/stability | yes | 0.325-1.025 | 0.700 | 0.1847 | 0.2033 | 1.000 | FAIL-OPEN-K-FAMILY |
| measure supplied law | full P_K log-linear projection | yes | 0.620 | 0.000 | 0.1607 | 0.2273 | 1.000 | IDENT-NOT-DERIVATION |
| fixed work quantum | Delta(K)=W_src | yes | 0.625 | 0.000 | 0.1628 | 0.2252 | 1.000 | PASS-CONDITIONAL-WORK-UNIT |
| critical self-isolation | min \|Delta-iota\| | yes | 0.700 | 0.000 | 0.1958 | 0.1922 | 1.000 | PASS-FIXED-J-REVISES-K0 |
| robust self-isolation | max min(Delta,iota) | yes | 0.700 | 0.000 | 0.1958 | 0.1922 | 1.000 | PASS-FIXED-J-REVISES-K0 |
| defect-isolation product | max Delta*iota | yes | 0.700 | 0.000 | 0.1958 | 0.1922 | 1.000 | PASS-FIXED-J-REVISES-K0 |
| scale-free ratio | max min/max | yes | 0.700 | 0.000 | 0.1958 | 0.1922 | 1.000 | PASS-FIXED-J-REVISES-K0 |

Here `Delta` is the RN/KL factorization defect and `iota` is its isolation
from the next competing separator. At fixed `J0`, the receipt has a useful
monotonicity:

```text
defect strictly increases with K: yes;
isolation strictly decreases with K: yes.
```

Therefore a supplied source-work quantum `W_src` would fix `K` uniquely by
inverting

```math
\Delta_{J_0}(K)=W_{\rm src}.
```

This proves a conditional positive theorem, not a derivation. The theorem is:

```text
Fixed-J source-work theorem.
For the finite spectrum-flow class at fixed J0, the RN source-defect map
K -> Delta_J0(K) is strictly monotone on the stable IMFD interval. Hence an
intrinsic source-work quantum W_src selects one K cofinally.
```

The same audit also finds a better Einstein-style clue. At fixed `J0`, four
scale-free criteria all select the same value:

```text
K_crit = 0.700.
```

They are all different ways of saying that the event should be as close as
possible to self-isolated criticality:

```math
\Delta(K)\approx\iota(K).
```

Equivalently, the work needed to make the event should match the work needed
to make the separator ambiguous. This is attractive because it does not ask
for an external numerical target. It uses only the intrinsic RN spectrum of
the sealed diamond.

But it still does not close the theory. Once `J` is also free, the selectors
do not choose one point. The finite two-parameter audit gives:

| selector | J | K | defect | isolation | balance | robust | ratio |
|---|---:|---:|---:|---:|---:|---:|---:|
| balance | 0.550 | 0.375 | 0.0657 | 0.0654 | 0.0002 | 0.0654 | 0.997 |
| max-min | 2.450 | 1.000 | 0.3278 | 0.3217 | 0.0061 | 0.3217 | 0.981 |
| max-product | 2.450 | 1.000 | 0.3278 | 0.3217 | 0.0061 | 0.3217 | 0.981 |
| max-ratio | 1.350 | 0.775 | 0.2293 | 0.2288 | 0.0005 | 0.2288 | 0.998 |

The per-`J` critical curve is:

| J | K_crit | defect | isolation | robust | ratio |
|---:|---:|---:|---:|---:|---:|
| 0.50 | 0.350 | 0.0577 | 0.0533 | 0.0533 | 0.923 |
| 0.75 | 0.500 | 0.1109 | 0.1072 | 0.1072 | 0.966 |
| 1.00 | 0.625 | 0.1628 | 0.1650 | 0.1628 | 0.987 |
| 1.15 | 0.700 | 0.1958 | 0.1922 | 0.1922 | 0.982 |
| 1.40 | 0.800 | 0.2405 | 0.2331 | 0.2331 | 0.969 |
| 1.75 | 0.900 | 0.2848 | 0.2760 | 0.2760 | 0.969 |
| 2.00 | 0.950 | 0.3066 | 0.2965 | 0.2965 | 0.967 |
| 2.25 | 0.975 | 0.3172 | 0.3154 | 0.3154 | 0.994 |

Thus critical self-isolation is not enough by itself. It can derive source
amplitude relative to an already fixed eventless transport amplitude, but it
does not derive the full modular dynamics.

The invariant that would close this family is therefore not a bare number
`K0`. It is the **sealed modular work profile**:

```text
W_x =
intrinsic Legendre/RN work profile of the sealed finite diamond,
with one component for eventless transport and one component for
source-defect production.
```

In finite exponential-family language, `J` and `K` are not arbitrary
couplings. They are the Legendre-dual multipliers of an intrinsic work vector:

```math
W_x=(W_x^{\rm tr},W_x^{\rm src}),
\qquad
(J_x,K_x)=\nabla_W \Psi_x(W_x),
```

where `Psi_x` is the sealed log-partition/record-action potential. In RN
language the same statement is:

```math
W_x^{\rm tr}
=
\partial_{J} A_x,
\qquad
W_x^{\rm src}
=
\partial_{K} A_x,
```

with both derivatives taken internally in the same sealed diamond. The old
open scalar becomes a derived component of one invariant profile.

This is also the object that would close the earlier loose ends at once:

- `R_x` is still selected by the RN partition spectrum;
- log-RN units are fixed by additivity;
- `J_x` fixes eventless collar transport rather than leaving `T_x` free;
- `K_x` fixes source-defect work rather than leaving `K0` free;
- the Hessian of `Psi_x` is the local Fisher/response Gram;
- the source-response amplitude `kappa_G` is a screen/volume derivative of
  the same work profile;
- the cost route for `beta` uses that same Hessian and no free blur
  coefficient.

This is the current branch-A-enriched closure theorem target:

```text
Sealed modular work-profile theorem.
Every stable physical record diamond intrinsically carries a unique
role-blind modular work profile W_x. Its Legendre-dual multipliers generate
the spectrum-flow law, its RN spectrum gives R_x, its Hessian gives the
four-role response Gram, and its screen/volume derivative gives the
gravity/source coefficient. The resulting IMFDs are cofinal and TS-compatible.
```

The result of the campaign is therefore:

```text
K0 as previously printed is not derived.
Kcrit is derivable at fixed J by intrinsic self-isolation, but it revises K0
and leaves J open.
The real invariant needed for full closure is the sealed modular work profile.
If that profile is derived from the ontology, branch A-enriched has a finite
closure path. If it is supplied, the theory remains a parameterized modular
record dynamics.
```

---

## 33. Sealed modular work profile: Einsteinian closure campaign [PROBE]

The previous section named the missing invariant. This section attacks it
directly:

```text
Is W_x intrinsic, or is it another supplied branch-B structure?
```

The diagnostic is:

```text
code/v6_p3w_sealed_work_profile_campaign.py
```

The finite answer is positive, but only for the stronger sealed-diamond
ontology. The structural packet

```text
R_x, event status, source floor, RN unit, refinement stability
```

does not derive `W_x`. It still permits an open work family. But a full sealed
finite record diamond has more than this packet: it has a full local law
`P_x`, an intrinsic separator `R_x`, and a canonical finite count/reference
law `U_x`. From those three objects the work profile is not a convention. It
is the KL/Pythagorean decomposition:

```math
W_x^{\rm tr}
=
D(\Pi_{R_x}P_x\Vert U_x),
\qquad
W_x^{\rm src}
=
D(P_x\Vert \Pi_{R_x}P_x),
\qquad
W_x^{\rm tot}
=
D(P_x\Vert U_x).
```

Here `Pi_R P` is the unique product repair over the `R` components preserving
each component marginal. The finite identity is:

```math
W_x^{\rm tot}
=
W_x^{\rm tr}
+
W_x^{\rm src}.
```

This is not a numerical fit. It is the KL chain rule for the product repair.
The proof is short. Since `U_x` factorizes over the same finite record
components,

```math
\log {P_x\over U_x}
=
\log {P_x\over \Pi_{R_x}P_x}
+
\log {\Pi_{R_x}P_x\over U_x}.
```

Taking `P_x` expectation gives the first term as
`D(P_x || Pi_R P_x)`. The second term depends only on the `R_x` component
marginals, and `P_x` and `Pi_R P_x` have the same component marginals, so it is
`D(Pi_R P_x || U_x)`. Therefore the work decomposition is intrinsic once
`P_x`, `R_x`, and `U_x` are intrinsic.

The audit is:

| candidate | supplied | R_x | U_x | profile | Wsrc span | chain error | injective | verdict |
|---|---|---|---|---|---:|---:|---|---|
| structural packet | R/status/floors | yes | no | no | 0.322221 | 0.00e+00 | no | FAIL-WORK-NOT-IN-DATA |
| full P plus R | P,R | yes | no | source only | 0.322221 | 5.97e-16 | partial | PARTIAL-NO-TRANSPORT-BASE |
| KL/Pythagorean profile | P,R,U | yes | yes | W=(D(PiP\|\|U),D(P\|\|PiP)) | 0.322221 | 5.97e-16 | yes | PASS-FINITE-WX |
| nonlinear work score | P,R,U | yes | yes | sqrt score | 0.322221 | 3.14e-01 | no | FAIL-NONADDITIVE |
| nonisolated RN spectrum | P,R? (ambiguous-positive) | no | yes | multi/ambiguous | 0.000000 | 0.00e+00 | no | FAIL-NO-ONE-EVENT-WX |
| uniform/eventless zero | P,R? (ambiguous-zero) | no | yes | zero/ambiguous | 0.000000 | 0.00e+00 | no | FAIL-NO-SOURCE-PROFILE |

This resolves the old `K` family in the finite class. At fixed `J0`, the
profile separates the source family:

| K | W_tr | W_src | W_tot | chain error |
|---:|---:|---:|---:|---:|
| 0.275 | 0.776038 | 0.036429 | 0.812467 | 9.71e-17 |
| 0.620 | 0.776038 | 0.160682 | 0.936720 | 8.33e-17 |
| 0.700 | 0.776038 | 0.195787 | 0.971825 | 4.16e-16 |
| 1.075 | 0.776038 | 0.358650 | 1.134688 | 1.11e-16 |

The receipt is:

```text
source work range = 0.036429..0.358650;
transport work span at fixed J0 = 2.442e-15;
max chain error = 5.967e-16;
source work strictly monotone in K = yes;
transport work constant at fixed J0 = yes.
```

The two-parameter check also supports the profile as a real coordinate-free
object:

```text
stable structural grid points = 1745;
rounded profile collisions at 6 decimals = 0;
minimum profile separation = 3.596208e-03.
```

Thus `W_x` does not merely rename `K`. It replaces the coordinate coupling
with two invariant RN work components:

```text
eventless transport work = D(Pi_R P || U);
source-defect work       = D(P || Pi_R P).
```

The old scalar `K0` was a coupling coordinate in a chosen log-linear
parametrization. The intrinsic object is `W_x^{src}`. If one wants the
coupling coordinate back, it is obtained as the Legendre-dual multiplier of
the work profile in the selected exponential family. The finite injectivity
receipt says that, in the tested stable spectrum-flow class, the profile
separates the `(J,K)` family.

This gives the strongest current finite branch-A-enriched theorem:

```text
Sealed modular work-profile theorem, finite form.
Let P_x be a positive sealed finite record law, let R_x be its unique isolated
RN separator, and let U_x be the canonical finite count/reference law. Then

  W_x(P_x)
  =
  (D(Pi_R P_x || U_x), D(P_x || Pi_R P_x))

is an intrinsic, role-blind, log-RN additive work profile. It splits total
record action by the KL/Pythagorean identity, separates the stable
spectrum-flow `(J,K)` family, and makes the source amplitude a derived work
component rather than a supplied scalar.
```

This is also the clean branch boundary:

```text
Branch A-enriched survives if the physical ontology is the full sealed finite
record diamond:

  (P_x, R_x, U_x, isolated RN source normal)

with cofinal refinement convergence.

Branch B is the honest verdict if any of these are supplied externally:

  P_x as a chosen stochastic law;
  R_x as a chosen collar;
  U_x as a chosen reference state;
  the isolated source normal as an admissibility axiom.
```

The campaign therefore closes the `K0` issue at finite level by changing the
question. The invariant is not a preferred numerical coupling. The invariant
is the sealed KL work profile. What remains open is the continuum/physical
theorem that the real record ontology supplies `P_x`, `R_x`, `U_x`, and an
isolated RN normal cofinally.

---

## 34. Feynman receipts for the sealed-diamond ontology [PROBE]

The Einstein campaign found the invariant. The Feynman campaign asks whether
it functions as a meter:

```text
Can finite records recover W_x, and does W_x predict independent operations
that cheap event/click data cannot fake?
```

The diagnostic is:

```text
code/v6_p3x_feynman_wx_receipts.py
```

The target sealed diamond is the finite spectrum-flow IMFD at the critical
source-work point:

```text
status = event;
R = 01|23;
K = 0.700;
W_tr = 0.776038;
W_src = 0.195787;
W_tot = 0.971825;
chain error = 4.16e-16.
```

The first receipt is finite estimability. Draw samples from the sealed local
law, reconstruct the empirical law with a small pseudocount, scan the
partition spectrum, and compute the KL work profile.

| samples | R success | event success | mean Wsrc error | mean Wtr error | max chain error | verdict |
|---:|---:|---:|---:|---:|---:|---|
| 250 | 1.000 | 1.000 | 0.02598 | 0.06046 | 3.61e-16 | COND-SAMPLE-SIZE |
| 1000 | 1.000 | 1.000 | 0.01312 | 0.02358 | 4.44e-16 | COND-SAMPLE-SIZE |
| 4000 | 1.000 | 1.000 | 0.00614 | 0.01283 | 4.72e-16 | PASS-FINITE-ESTIMATION |
| 16000 | 1.000 | 1.000 | 0.00359 | 0.00541 | 3.89e-16 | PASS-FINITE-ESTIMATION |

This is a modest but important receipt. `W_x` is not only defined by an
omniscient formula. In this finite class it is recoverable from full local
record samples.

The second receipt is deletion. Repair the diamond by replacing `P` with
`Pi_R P`. The prediction is:

```text
deletion cost = W_src;
source defect after repair = 0;
transport work is preserved;
internal component transport is preserved.
```

The finite audit gives:

| probe | quantity | value | reference | error | verdict |
|---|---|---:|---:|---:|---|
| delete/repair | KL(P\|\|Pi_R P) | 0.195787 | 0.195787 | 0.00e+00 | PASS-DELETION-COST |
| delete/repair | source defect after repair | 0.000000 | 0.000000 | 4.21e-16 | PASS-SOURCE-REMOVED |
| delete/repair | transport work drift | 0.000000 | 0.000000 | 5.55e-16 | PASS-TRANSPORT-PRESERVED |
| delete/repair | internal transport drift | 0.000000 | 0.000000 | 1.67e-16 | PASS-MARGINAL-TRANSPORT-PRESERVED |

The third receipt is the cheap-observable attack. Hold `J0` fixed and compare
two laws with different source amplitudes. Their one-point marginals, internal
mutual information, and transport work agree, but the source work differs:

| probe | quantity | value | verdict |
|---|---|---:|---|
| cheap-observable fake | one-point marginal gap | 0.000000 | PASS-CHEAP-FAILS |
| cheap-observable fake | internal MI gap | 0.000000 | PASS-INTERNAL-UNCHANGED |
| cheap-observable fake | transport work gap | 0.000000 | PASS-TRANSPORT-UNCHANGED |
| cheap-observable fake | source work gap | 0.288094 | PASS-WX-SEPARATES |

This is the cleanest finite reason the ontology is not just "clicks plus
labels." Click-level and first-order data can miss the source difference.
`W_x^{src}` sees it.

The fourth receipt is reference dependence. If the reference law `U_x` is
changed to a biased product law, the KL chain identity still holds, but the
transport work moves:

| probe | quantity | value | verdict |
|---|---|---:|---|
| reference attack | chain error with biased U | 0.000000 | PASS-ADDITIVE-BUT-REFERENCE-DEPENDENT |
| reference attack | transport work shift | 0.039589 | FAIL-U-SUPPLIED-MOVES-WTR |

This is not a weakness of the KL theorem. It is the branch boundary. `U_x`
must be canonical. If `U_x` is chosen externally, the transport side of the
work profile is branch B.

The fifth receipt is sealed composition. Compose two independent copies of
the same sealed diamond. The work components add:

| probe | quantity | error | verdict |
|---|---|---:|---|
| sealed composition | source additivity error | 2.78e-16 | PASS-SOURCE-ADDITIVE |
| sealed composition | transport additivity error | 6.66e-16 | PASS-TRANSPORT-ADDITIVE |
| sealed composition | total additivity error | 2.22e-15 | PASS-TOTAL-ADDITIVE |

The sixth receipt is the bad-case attack. Uniform/eventless and tied
nonisolated laws do not become events by definitional generosity:

| probe | quantity | verdict |
|---|---|---|
| bad-case attack | uniform/eventless status=ambiguous-zero | FAIL-NO-ONE-EVENT-METER |
| bad-case attack | tied/nonisolated status=ambiguous-positive | FAIL-NO-ONE-EVENT-METER |

The seventh receipt is role consistency:

| probe | quantity | value | verdict |
|---|---|---:|---|
| role consistency | role-tied Wsrc span | 0.000000 | PASS-ROLE-BLIND |
| role consistency | role-split Wsrc span | 0.288094 | FAIL-SPLIT-DETECTED |

The Feynman verdict is therefore:

```text
The sealed-diamond ontology has finite operational receipts. W_x is estimable
from full local record samples, predicts deletion cost, composes additively,
and detects source differences hidden from click/one-point observables.

The failures are equally important. First-order data do not determine W_x; a
noncanonical U_x moves W_tr; nonisolated spectra do not give a one-event
meter; and role-split laws are detected rather than rescued.
```

So the ontology makes operational sense exactly as a full sealed record-law
ontology. If the physical theory gives only clicks, order, or a supplied
reference state, the finite Feynman campaign says branch B.

---

## 35. Full branch-A-enriched target campaign [PROBE]

The feedback after the sealed-work campaign is right: the ontology should not
state the four-fold identity as though it were already proved. The exact
finite legs and the theorem targets must be separated.

The diagnostic is:

```text
code/v6_p3y_full_branch_a_target_campaign.py
```

The nine campaign targets are:

```text
1. stop overclaiming;
2. free-Dirac Hessian anchor;
3. refinement cocycle;
4. isolated-gap genericity;
5. refinement-stable source floor;
6. causal-order readout;
7. screen/volume readout;
8. branch-B counterexample suite;
9. publishable verdict.
```

The target audit is:

| target | test | positive | negative | value | verdict |
|---|---|---|---|---|---|
| 1 stop overclaiming | split claims into exact legs and theorem targets | exact: record/source KL split | open: causal order + screen/volume + refinement | paper patched | PASS-CLAIM-DISCIPLINE |
| 2 Dirac Hessian anchor | raw Hess(D(p\|\|u)) support vs free A_R^(1) | A_R offdiag=8 | Hess offdiag=0 | support mismatch=8 | FAIL-PROBABILITY-HESSIAN-NOT-DIRAC |
| 3 refinement cocycle | canonical duplicate projection vs alternate lift | canonical error=8.049e-16 | free-lift drift=0.23324 | cocycle exact only after map choice | PASS-CANONICAL-COCYCLE-FAILS-FREE-LIFT |
| 4 isolated-gap genericity | perturb IMFD basin vs arbitrary positive laws | open-basin rate=1.000 | arbitrary rate=0.008 | trials=240 | PASS-OPEN-CLASS-NOT-GLOBAL-GENERIC |
| 5 refinement-stable source floor | stable K_n vs decaying K_n refinement families | stable min Wsrc=0.20246 | decay min Wsrc=0.00302 | floor=0.03500 | PASS-CONDITIONAL-STABLE-FLOOR |
| 6 causal-order readout | same P,R,U,W with opposite orientation labels | undirected adjacency compatible | orientation not determined | profile gap=0.000e+00 | FAIL-CAUSAL-ORIENTATION-OPEN |
| 7 screen/volume readout | free screen coefficient times same Wsrc | Wsrc=0.195787 | response span=0.293681 | same P,R,U | FAIL-SCREEN-COEFFICIENT-OPEN |
| 8 branch-B counterexample suite | same one-point clicks/R/event status, different W and response | click gap=0.000e+00 | work gap=0.859310 | cheap data cannot close A | PASS-COUNTEREXAMPLE-SUITE |
| 9 publishable verdict | aggregate target status | two exact finite legs | three hard gates remain | hard gates open=3 | A-ENRICHED-PARTIAL-BRANCH-B-BOUNDARY |

The most important row is target 2. The direct free-Dirac Hessian anchor fails
in the strict form:

```text
raw probability Hessian of D(p||u): diagonal Fisher metric;
free one-particle Dirac A_R^(1): signed local comparison generator;
off-diagonal support mismatch: 8 entries.
```

This is not a small normalization error. It says that probability-only
`W_x` supplies a Fisher/response metric, not the signed Dirac localized
intervention generator. To compare with `A_R^(1)`, the theory must also derive
a Dirac tangent/intervention cocycle: the canonical directions in which the
sealed probability law is deformed. If that tangent cocycle is supplied from
the older one-particle Hamiltonian construction, the comparison becomes a
conditional anchor, not a branch-A derivation.

The refinement result is equally sharp. A canonical duplicate projection gives
cofinal consistency at machine precision:

```text
canonical refinement error = 8.049e-16.
```

But an alternate lift of the same refined data changes the work profile:

```text
free-lift drift = 0.23324.
```

Thus refinement canonicity is not optional decoration. It is the branch-A
hinge. Without a record cocycle choosing the refinement maps, the old V2 lift
problem has only been relocated.

The isolated-gap and source-floor targets give conditional positive results:

```text
isolated IMFD open-basin rate under perturbation = 1.000;
arbitrary positive-law event rate = 0.008;
stable refinement source floor = 0.20246;
decaying refinement source floor = 0.00302.
```

So isolated source-floored diamonds form a real open finite class, but they
are not generic among all positive laws. The dynamics must put the process in
that basin cofinally.

The causal and screen/volume targets fail from `P,R,U,W` alone. The same
sealed probability profile is compatible with opposite causal orientations:

```text
same P,R,U,W;
opposite orientation labels;
profile gap = 0.
```

Likewise the same source work admits a free screen coefficient:

```text
response = c_screen W_src;
c_screen in {0.5,1.0,2.0};
response span = 0.293681.
```

Therefore the four-fold identity is not a theorem yet. The honest finite
status is:

```text
proved finite leg: record/source KL work split;
proved finite receipt: W_x estimation, deletion, additivity, cheap-fake attack;
conditional positive: isolated-gap basin and stable source floor;
hard open gate: canonical refinement/Dirac tangent cocycle;
hard open gate: causal-order orientation readout;
hard open gate: screen/volume response coefficient.
```

The publishable verdict is:

```text
A-enriched partial.
The sealed-diamond ontology has two exact KL legs and strong finite receipts.
It is not yet full branch A. Full branch A requires deriving the canonical
refinement maps, the Dirac tangent/intervention cocycle, causal orientation,
and screen/volume response from the same full sealed record process.

If any of these are supplied externally, the theory is a strong branch-B
modular record theory rather than a derived branch-A event theory.
```

---

## 36. Underlying law of possible changes [PROBE]

The previous section identifies the remaining problem. `W_x` gives invariant
work and Fisher geometry, but Einstein's question is sharper:

```text
What is the invariant law of possible changes?
```

The diagnostic is:

```text
code/v6_p3z_underlying_change_law_campaign.py
```

The finite answer is negative for the sealed probability/work diamond
`(P,R,U,W)` alone. It does not derive the signed local tangent/intervention
law needed by the free Dirac benchmark.

The audit is:

| candidate | data | observable | positive | obstruction | value | verdict |
|---|---|---|---|---|---|---|
| probability Hessian | P,R,U,W | Hess(D(p\|\|u)) | Hess offdiag=0 | A_R offdiag=8 | support mismatch=8 | FAIL-NOT-DIRAC-TANGENT |
| exchange curvature | P,R,U,W | [tangent_R,tangent_S] | Dirac comm norm=0.216506 | Fisher comm norm=0.000000 | probability metric has no bracket | FAIL-NO-CHANGE-BRACKET |
| hidden phase/current | same probabilities | Im(conj psi_i psi_j) | probability gap=0.000e+00 | current gap=0.866025 | same P opposite current | FAIL-PROBA-LOSES-CURRENT |
| lambda rule family | same P,R,U,W | A_lambda=c_lambda A | normalized error=0.0e+00 | raw scale span=0.5625 | raw rule not selected | FAIL-RAW-RULE-NONUNIQUE |
| Dirac cocycle supplied | P,R,U,W plus C | C_R=A_R^(1) | support=8 offdiag | C supplied, not derived | comm norm=0.216506 | PASS-CONDITIONAL-DIRAC-ANCHOR |
| sealed current-work diamond | (P,U,R,W,C,rho) | metric + current cocycle | minimal object has metric and bracket | existence not proved | Einstein candidate | THM-TARGET-NOT-CLOSED |
| branch verdict | current ontology | possible-change law | W_x exact kinematics | C/rho dynamics missing | branch-A gate isolated | A-PARTIAL-OR-B |

The four obstructions are distinct.

First, the Hessian of the KL action is a Fisher metric. In raw probability
coordinates it is diagonal at the count reference. The free one-particle
Dirac localized comparison coefficient `A_R^(1)` has signed off-diagonal
support:

```text
Hess(D(p||u)) off-diagonal support = 0;
A_R^(1) off-diagonal support = 8.
```

So no unit conversion can turn probability Hessian data alone into the Dirac
comparison generator.

Second, the Fisher metric has no exchange bracket. The finite Dirac tangent
operators have nonzero commutator:

```text
||[A_R^(1), A_S^(1)]|| = 0.216506;
||[Hess, Hess]||       = 0.
```

Thus the exchange-defect/curvature object lives in a tangent law, not in the
scalar KL work profile alone.

Third, probabilities lose phase/current information. Two finite amplitudes can
have the same probabilities and opposite current:

```text
probability gap = 0;
current gap = 0.866025.
```

Therefore a probability-only sealed diamond cannot know the orientation of
possible change.

Fourth, the old localized-intervention rule family remains visible. The
admissible `lambda` family has

```math
A_{R,\lambda}^{(1)}
=
\lambda(2-\lambda) A_R^{(1)}.
```

The normalized tangent class can agree while the raw scale varies:

```text
normalized error = 0;
raw scale span = 0.5625.
```

So even after adding a Dirac tangent shape, branch A still needs a canonical
rule/normalization or a renormalized equivalence principle.

The minimal object that can satisfy Einstein's demand is therefore not the
sealed probability/work diamond. It is the **sealed current-work diamond**:

```text
E_x =
(P_x, U_x, R_x, W_x, C_x, rho_x).
```

Here:

- `P_x` is the full sealed local record law;
- `U_x` is the canonical count/reference law;
- `R_x` is the intrinsic RN separator;
- `W_x` is the KL/Pythagorean work profile;
- `C_x` is the signed tangent/current cocycle of possible local changes;
- `rho_x` is the canonical refinement/intervention cocycle.

In this object, `W_x` supplies the metric/work profile and `C_x` supplies the
current/bracket. The free Dirac comparison coefficient is then a conditional
anchor:

```text
C_R = A_R^(1)
```

in the free one-particle benchmark, with nonzero exchange bracket. But if
`C_x` is merely imported from the old Hamiltonian construction, this is not a
branch-A derivation. It is branch B with a correct modular receipt.

The theorem target becomes:

```text
Sealed current-work theorem.
The physical cofinal record process intrinsically supplies a unique
role-blind current-work diamond (P,U,R,W,C,rho). The KL part W gives the
record/source work split. The current cocycle C gives the signed local
intervention generators and their exchange brackets. The refinement cocycle
rho makes both W and C cofinally compatible. In the free one-particle Dirac
diamond, C_R converges to the normalized collar-excision A_R^(1) class and
the bond-centered exchange bracket converges to the Dirac-Schwinger
tangential generator.
```

This is the clean Einstein boundary:

```text
W_x = invariant kinematics of events.
C_x,rho_x = invariant dynamics of possible changes.

Branch A-enriched can continue only if C_x and rho_x are derived from the same
sealed physical process. If they are supplied, the theory is branch B.
```

---

## 37. Deriving `C` and `rho`: current-work functor campaign [PROBE]

The preceding section isolates the final Einstein pressure:

```text
Branch A can continue only if C and rho are derived from the physical process.
If C or rho are supplied after P,U,R,W are known, this is branch B.
```

The diagnostic is:

```text
code/v6_p3aa_current_rho_origin_campaign.py
```

The campaign attacks both objects directly. The result is negative for the
old sealed probability/work diamond and positive only for a stronger invariant
process.

### 37.1 Static sealed work cannot derive `C`

Let a sealed finite record law have static marginal `P`, count reference `U`,
and work `W=D(P||U)`. On a three-state record collar take:

```math
P=(0.40,0.35,0.25),
\qquad
Q_\pm
=
P\otimes P
\pm\epsilon J_{\rm cyc},
\qquad
\epsilon=0.030,
```

where `J_cyc` is the divergence-free oriented cycle

```text
0 -> 1 -> 2 -> 0.
```

Both `Q_+` and `Q_-` have the same row and column marginal `P`, hence the
same static `P`, `U`, and `W`. But their currents are opposite:

```text
same P,W opposite C gap = 0.120000;
marginal gap = 0.
```

Thus no function of the static work diamond `(P,U,R,W)` can derive the signed
current/tangent cocycle. Any rule

```text
C = C(P,U,R,W)
```

would have to assign the same `C` to two physically opposite oriented-change
laws.

The maximum-entropy attempt also fails. With only `P` fixed, the maximum
entropy path law is the reversible product law:

```math
Q_* = P\otimes P,
\qquad
C_* = Q_* - Q_*^{\rm rev}=0.
```

The finite audit gives:

```text
selected C norm = 0;
physical C norm = 0.146969.
```

So max-entropy is canonical, but it erases the very current needed by the
possible-change law.

### 37.2 An oriented path law derives `C`

If the physical sealed diamond supplies an oriented path/Radon-Nikodym law
`Q_x` on ordered record changes, then `C` is no longer extra:

```math
C_x(i,j)
=
Q_x(i,j)-Q_x(j,i),
```

and the RN affinity cocycle is

```math
A_x(i,j)
=
\log {Q_x(i,j)\over Q_x(j,i)}.
```

The finite audit gives:

```text
C norm = 0.146969;
cycle RN circulation = 1.769011.
```

The opposite path law has the same static work and the opposite circulation:

```text
opposite circulation gap = 3.538021.
```

This is the key distinction. `C` is derivable from `Q_x`; it is not derivable
from `P_x` alone. Therefore branch A must make the oriented path/RN law part
of the physical process, not an after-the-fact tangent decoration.

### 37.3 Static refinement cannot derive `rho`

The same problem appears for refinement. Build a refined path law with two
coarse projections:

```math
Q_{\rm ref}
=
Q_+\otimes Q_*.
```

Projection onto the first copy recovers the current-carrying law `Q_+`.
Projection onto the second copy recovers the reversible law `Q_*`. Both
projections preserve the same static marginal and static work:

```text
work drift = 1.4e-17.
```

But only the first projection preserves the current:

```text
current error first  = 2.8e-17;
current error second = 0.060000.
```

Therefore a refinement cocycle cannot be derived from static `P,W` data
alone. The old V2 lift ambiguity reappears exactly here.

If the refinement morphism is required to push forward the oriented path law,
the ambiguity disappears in the asymmetric finite case:

```math
(\rho\times\rho)_\# Q_{\rm ref}=Q.
```

The audit gives:

```text
path error first  = 9.7e-17;
path error second = 0.180000.
```

So `rho` is conditionally derivable as a `Q`-preserving push-forward morphism.
But a duplicate symmetry attack remains. If both refined copies carry the same
`Q`, both projections are exact:

```text
path tie gap = 0;
current tie gap = 0.
```

Thus `rho` is unique only up to internal automorphism unless the process also
supplies the refinement groupoid/quotient rule. This is acceptable if those
two projections are physically the same refinement under an internal symmetry.
It is branch B if one projection is chosen externally.

### 37.4 The invariant that closes the gate

The finite no-go says the missing invariant is not a scalar coefficient. It
is the **sealed current-work functor**:

```text
F:
sealed finite diamonds and refinements
    -> finite oriented record-change laws,

D
    -> (Omega_D, U_D, Q_D, P_D, R_D, W_D),
```

with:

```math
P_D = {\rm marg}\, Q_D,
```

```math
W_D
=
\left(
D(\Pi_{R_D}P_D\Vert U_D),
D(P_D\Vert \Pi_{R_D}P_D)
\right),
```

```math
C_D = Q_D-Q_D^{\rm rev},
\qquad
A_D = \log {dQ_D\over dQ_D^{\rm rev}},
```

and refinement morphisms `rho_{m n}` satisfying:

```math
(\rho_{m n}\times\rho_{m n})_\# Q_m = Q_n,
\qquad
\rho_{n k}\circ\rho_{m n} = \rho_{m k},
```

up to internal automorphism of indistinguishable refined copies.

This is the smallest object found by the campaign that contains both sides of
the event:

```text
W = invariant work/metric of the event;
C = invariant orientation/current of possible changes;
rho = invariant projective identity of the event under refinement.
```

The audit is:

| target | data | construction | positive | obstruction | value | verdict |
|---|---|---|---|---|---|---|
| `C` from static work | `P,U,W` | try `C=C(P,U,W)` | `W=0.018085` | same `P,W` opposite `C` gap `0.120000` | marginal gap `0.0e+00` | FAIL-STATIC-NO-C |
| max-entropy selector | `P` only | `Q*=P tensor P` | `H(Q*)-H(Q+)=0.026116` | selected `C` norm `0.000000` | physical `C` norm `0.146969` | FAIL-REVERSIBLE-ZERO-C |
| oriented path law | `P,Q` | `C=Q-Q^T` | marginal gap `0.0e+00` | `Q` must be physical, not fitted later | `C` norm `0.146969` | PASS-CONDITIONAL-C-FROM-Q |
| RN current cocycle | `P,Q` | `A=log(dQ/dQ^rev)` | cycle circulation `1.769011` | opposite circulation gap `3.538021` | same static `P,W` | PASS-CONDITIONAL-RN-CURRENT |
| `rho` from static tower | refined `P,W` | choose first or second projection | work drift `1.4e-17` | current error second `0.060000` | both preserve static `P,W` | FAIL-STATIC-RHO-NONUNIQUE |
| `rho` from path functor | refined `Q -> Q` | push forward `Q` exactly | path error first `9.7e-17` | path error second `0.180000` | current error first `2.8e-17` | PASS-CONDITIONAL-RHO-FROM-Q |
| duplicate symmetry attack | refined `Q,Q` | two exact projections | path tie gap `0.0e+00` | current tie gap `0.0e+00` | requires quotient by automorphism | FAIL-UNIQUE-RHO-UP-TO-GAUGE |
| sealed current-work functor | `D -> (P,Q,U,R,W)` | `C` and `rho` by RN functoriality | `C=antisymmetric RN current` | `rho=unique Q-pushforward morphism` | exists only if physical process supplies `Q` | THM-TARGET-SCWF |
| branch verdict | old sealed diamond | `(P,U,R,W)` only | `W` exact kinematics | `C/rho` not derivable | need projective oriented-change law | OLD-A-INCOMPLETE-NEW-A-TARGET |

The branch status is now sharper:

```text
Old branch A-enriched:
  incomplete.  A static sealed probability/work diamond cannot derive C or rho.

New branch A-current:
  alive if the physical process is a sealed current-work functor, so Q is
  primitive/intrinsic and C,rho are readouts of Q and its projective functoriality.

Branch B:
  the verdict if Q, C, or rho are selected after the sealed work diamond is known.
```

This is the current Einstein answer. The event is not only an isolated modular
factorization defect in a static law. The full physical event must also carry
the invariant oriented law of possible changes inside the sealed diamond. If
that oriented law is real, `C` and `rho` are not additions. They are the current
and projective identity of the same fact. If that oriented law has to be
chosen, the theory is branch B.

---

## 38. Einsteinian origin of `Q`: the two-screen bridge [PROBE]

The previous section found the right shape:

```text
If Q is intrinsic, then C and rho are readouts.
If Q is supplied after P,U,R,W, this is branch B.
```

Einstein's next question is therefore:

```text
What invariant fact inside a sealed diamond forces Q?
```

The diagnostic is:

```text
code/v6_p3ab_q_origin_einstein_campaign.py
```

The answer is not that `Q` is forced by the static work diamond. It is not.
The finite counterexamples are direct.

### 38.1 What does not force `Q`

Static sealed work data do not determine an oriented bridge. The same
`P,U,W` admits opposite finite bridges:

```text
W = 0.018085;
opposite Q gap = 0.360000;
same static law.
```

Boundary marginals do not determine it either. The two bridges have the same
input and output marginals:

```text
row gap = 0;
column gap = 0;
Q family gap = 0.360000.
```

Nor does an unordered pair law determine it. If one keeps only

```math
{Q(i,j)+Q(j,i)\over 2},
```

then `Q_+` and `Q_-` become indistinguishable:

```text
sym gap = 0;
current gap = 0.120000.
```

This is the finite version of the Einstein objection. The arrow of possible
change is not a property of the static probability, the boundary marginals, or
the unordered correlation graph.

### 38.2 The invariant candidate: ordered two-screen record bridge

The only finite object in the campaign that makes `Q` unavoidable is an
ordered two-screen sealed diamond. A sealed causal diamond has a lower
boundary/screen and an upper boundary/screen if its causal order is retained:

```text
lower screen = minimal boundary records;
upper screen = maximal boundary records.
```

In the finite toy diamond:

```text
lower = 0,1,2;
upper = 3,4,5;
oriented order ok = true;
unoriented shadow ok = false.
```

If the sealed physical law is the full joint law on those two ordered screens,
then `Q` is not an added current. It is simply:

```math
Q_D(a,b)
=
P_D({\rm lower}=a,{\rm upper}=b).
```

The static law is a marginal/readout of `Q_D`; the current is another readout:

```math
C_D(a,b)
=
Q_D(a,b)-Q_D^{\rm rev}(a,b),
```

and the RN arrow is:

```math
A_D(a,b)
=
\log {Q_D(a,b)\over Q_D^{\rm rev}(a,b)}.
```

The finite bridge has:

```text
C norm = 0.146969;
entropy production = 0.106141;
cycle RN circulation = 1.769011.
```

So `Q` is not a table chosen to repair the theory. It is the ordered
boundary-to-boundary law of the sealed diamond.

### 38.3 Composition is the real test

The bridge must not merely exist locally. Neighboring sealed diamonds must
compose without a hidden slicing convention. In finite form, two adjacent
bridges compose by the Chapman push-forward:

```math
Q_{13}(a,c)
=
\sum_b
Q_{12}(a,b)\,
{Q_{23}(b,c)\over P_2(b)}.
```

The finite receipt gives:

```text
associativity gap = 4.2e-17.
```

But if the same static bridge is used with the opposite orientation, the
composition changes:

```text
orientation mix gap = 0.067371.
```

Thus sealed composition sees the arrow. This is why the invariant cannot be
only a local static work profile. The full law must be a projective,
composable screen-to-screen bridge.

### 38.4 Reversible default is not enough

The maximum-entropy default bridge from `P` is:

```math
Q_0=P\otimes P.
```

It is canonical but reversible:

```text
C_0 norm = 0;
physical C norm = 0.146969.
```

So a reversible default can describe eventless transport, but it cannot by
itself generate the source arrow. The event-producing law must carry a real
oriented bridge.

### 38.5 Result

The audit is:

| target | data | construction | positive | obstruction | value | verdict |
|---|---|---|---|---|---|---|
| static sealed law | `P,U,W` | try `Q=Q(P,U,W)` | `W=0.018085` | opposite `Q` gap `0.360000` | same static law | FAIL-NO-Q-FROM-STATIC |
| boundary marginals | `P_minus,P_plus` | choose bridge `Q` | row gap `0.0e+00`, col gap `0.0e+00` | `Q` family gap `0.360000` | same boundary marginals | FAIL-BRIDGE-NONUNIQUE |
| unordered pair law | `{i,j}` records | `sym(Q)` | sym gap `0.0e+00` | current gap `0.120000` | orientation erased | FAIL-UNORDERED-NO-ARROW |
| causal screen order | finite poset diamond | minimal/maximal screens | lower `0,1,2`; upper `3,4,5` | unoriented shadow ok `False` | oriented order ok `True` | PASS-CONDITIONAL-SCREENS |
| two-screen bridge | ordered screens + full law | `Q=P(screen-,screen+)` | `C` norm `0.146969` | full two-screen law must be intrinsic | entropy prod `0.106141` | PASS-CONDITIONAL-Q-IS-LAW |
| RN arrow invariant | ordered `Q` | `log dQ/dQ^rev` | cycle circulation `1.769011` | zero if detailed-balanced | EP `0.106141` | PASS-CONDITIONAL-ARROW |
| sealed composition | `Q12,Q23` | Chapman push-forward | assoc gap `4.2e-17` | orientation mix gap `0.067371` | composition sees arrow | PASS-CONDITIONAL-FUNCTORIALITY |
| reversible default | `P` plus max entropy | `Q0=P tensor P` | `C0` norm `0.000000` | selects no source arrow | physical `C` norm `0.146969` | FAIL-DEFAULT-NOT-PHYSICAL |
| sealed record bridge functor | ordered screens, `Q`, composition | `Q` primitive as boundary law | `C,rho,W` are readouts | must be physical process, not fit | Einstein candidate | THM-TARGET-SRBF |
| branch verdict | old static diamond | `P,U,R,W` | not enough | `Q` not forced | two-screen functor needed | OLD-A-INCOMPLETE |

The theorem target is therefore:

```text
Sealed record bridge theorem.
The physical finite diamond is intrinsically a two-screen record bridge.
Its causal order supplies lower and upper screens. Its sealed law supplies
the ordered boundary-to-boundary RN measure Q. Its composition law makes Q
projective under gluing and refinement. Then W, C, rho, RN arrow, source
defect, and eventless transport are readouts of the same bridge.
```

This is the current closest Einstein-satisfying formulation:

```text
The invariant is not a chosen Q.
The invariant is the ordered screen-to-screen RN record bridge of a sealed
causal diamond.
```

Branch status:

```text
Old static branch A-enriched:
  dead/incomplete for C and rho.

Branch A-current:
  alive if physical diamonds intrinsically are sealed record bridge functors.

Branch B:
  the verdict if the screen order, bridge law Q, or composition/refinement
  functor is supplied externally.
```

So the next and final version of the open problem is no longer "derive `C`"
or "derive `rho`." It is:

```text
prove that physical sealed causal diamonds are ordered two-screen record
bridges with functorial RN composition.
```

---

## 39. Intrinsic screen-bridge theorem campaign [PROBE]

The previous section leaves one precise Einstein demand:

```text
The sealed causal diamond must itself supply the ordered screens and the
composable screen-to-screen RN bridge.
```

The diagnostic is:

```text
code/v6_p3ac_screen_bridge_theorem_campaign.py
```

The campaign separates three questions:

```text
1. Does the diamond intrinsically supply lower and upper screens?
2. Does the full sealed law intrinsically supply Q?
3. Do adjacent bridges compose without an externally chosen gluing rule?
```

The finite answer is:

```text
screens: yes, if oriented causal order is retained;
Q extraction: yes, if the full sealed law is present;
composition: yes iff the shared screen is a complete RN separator.
```

### 39.1 Ordered screens

In an oriented finite causal diamond, the lower and upper boundary screens are
intrinsic as minimal and maximal boundary antichains:

```text
lower screen = minimal boundary records;
upper screen = maximal boundary records.
```

The finite toy diamond gives:

```text
lower = 0,1;
upper = 4,5;
screen order ok = true.
```

If the order arrow is forgotten and only the undirected comparability graph is
kept, lower and upper screens can be swapped:

```text
screen order ok = false;
past/future swapped.
```

Thus the screen order is intrinsic to an oriented causal diamond, but not to a
bare undirected shadow.

### 39.2 Bridge extraction

Once the ordered screens are fixed, the full sealed law supplies the bridge by
marginalizing over interior records:

```math
Q_{XZ}(x,z)
=
\sum_y P_{XYZ}(x,y,z).
```

The finite extraction error is zero:

```text
extract error = 0.
```

But one-screen marginals do not determine the bridge. For the same lower and
upper marginals, the finite coupling family has:

```text
coupling span = 1.800000.
```

So `Q` is intrinsic only from the full sealed boundary law, not from separate
screen marginals.

### 39.3 Composition and the complete-screen RN defect

Now take three ordered screens:

```text
X = lower screen;
Y = shared screen;
Z = upper screen.
```

The adjacent bridges are:

```math
Q_{XY}(x,y)
=
\sum_z P_{XYZ}(x,y,z),
\qquad
Q_{YZ}(y,z)
=
\sum_x P_{XYZ}(x,y,z).
```

The composed bridge is:

```math
(Q_{XY}\circ Q_{YZ})(x,z)
=
\sum_y
{Q_{XY}(x,y)Q_{YZ}(y,z)\over P_Y(y)}.
```

This equals the directly extracted bridge `Q_XZ` exactly when the shared
screen is a complete RN separator:

```math
\Delta_Y(P)
=
D\!\left(
P_{XYZ}
\;\middle\Vert\;
{P_{XY}P_{YZ}\over P_Y}
\right)
=
I(X;Z\mid Y)
=0.
```

The finite complete-screen law gives:

```text
CMI = 9.3e-17;
composition error = 0.
```

This is the finite theorem:

```text
Q_XZ = Q_XY o Q_YZ
iff
Delta_Y(P) = 0.
```

The proof is the KL equality condition. `Delta_Y(P)` is a relative entropy,
so it is nonnegative and vanishes exactly when

```math
P_{XYZ}
=
{P_{XY}P_{YZ}\over P_Y}.
```

Substituting this identity and summing over `Y` gives the bridge composition
formula.

### 39.4 Hidden-bypass falsifier

A hidden bypass can keep both adjacent bridges fixed while changing the
composite bridge. The finite counterexample uses:

```math
P_\theta(x,y,z)
\propto
1+\theta s_x s_z,
\qquad
\theta=0.40,
```

where `s_x,s_z in {-1,+1}`. The adjacent bridges `Q_XY` and `Q_YZ` are the
same as in the uniform law:

```text
adjacent gaps = 0,0.
```

But the composite bridge changes:

```text
composite gap = 0.400000;
CMI = 0.082283;
composition error = 0.400000.
```

Therefore adjacent local bridges alone do not fix the global bridge. If the
shared screen is not complete, the seam hides an extra event, memory, or
bypass channel.

This point is important: complete-screen RN sufficiency is not a demand that
the universe be globally memoryless. It says that the screen state used for
gluing must include all memory records relevant to that gluing. If a smaller
screen fails the RN test, the correct sealed screen was not complete.

### 39.5 Audit

| target | data | construction | positive | obstruction | value | verdict |
|---|---|---|---|---|---|---|
| ordered screens | oriented causal order | minimal/maximal antichains | lower `0,1`; upper `4,5` | screen order ok `True` | unique as ordered boundary | PASS-INTRINSIC-SCREENS |
| unoriented shadow | comparability graph | forget order arrow | screen order ok `False` | lower/upper exchange symmetry | past/future swapped | FAIL-NO-SCREEN-ARROW |
| bridge extraction | full sealed law + screens | marginalize interior | `Q_XZ=sum_Y P_XYZ` | requires full law | extract error `0.0e+00` | PASS-Q-FROM-FULL-LAW |
| marginals only | `P_lower,P_upper` | choose coupling | coupling span `1.800000` | same marginals many bridges | `Q` not unique | FAIL-MARGINALS-NO-BRIDGE |
| complete shared screen | `P_XYZ` | `I(X;Z\|Y)=0` | CMI `9.3e-17` | composition error `0.0e+00` | `Q13=Q12 o Q23` | PASS-FUNCTORIAL-BRIDGE |
| hidden bypass | same adjacent bridges | `X-Z` memory bypasses `Y` | CMI `0.082283` | composition error `0.400000` | shared screen incomplete | FAIL-SEALING-VIOLATION |
| local-bridge insufficiency | `Q_XY,Q_YZ` | same adjacent data | adjacent gaps `0.0e+00,0.0e+00` | composite gap `0.400000` | locals do not fix global | FAIL-LOCAL-BRIDGES-INCOMPLETE |
| screen RN defect | `P_XYZ,Q_XY,Q_YZ` | `Delta_Y=D(P\|\|P_XY P_YZ/P_Y)` | zero iff bridge composes | Markov `9.3e-17`; bypass `0.082283` | intrinsic seam test | THM-FINITE-RN-SUFFICIENCY |
| branch verdict | sealed diamond process | screens + full law + RN sufficiency | `Q` forced conditionally | sufficiency must be physical | otherwise branch B | A-CURRENT-CONDITIONAL |

The theorem target is now:

```text
Intrinsic screen-bridge theorem.
For every physical sealed causal diamond, oriented causal order determines
lower and upper boundary screens. The full sealed law determines the
screen-to-screen RN bridge Q by marginalization. For every valid gluing,
the shared screen is complete in the RN sense:

  D(P_XYZ || P_XY P_YZ/P_Y) = 0.

Therefore bridges compose functorially, and Q, W, C, rho, eventless transport,
and source defects are all readouts of the same sealed process.
```

This is the current Einstein-satisfying branch-A-current target. The
falsifier is equally clean:

```text
If physical diamonds admit hidden bypasses with the same adjacent bridges but
different composite bridges, and no larger intrinsic screen absorbs the
bypass, then Q-composition is not derived. The theory is branch B.
```

---

## 40. Minimal complete screen theorem campaign [PROBE]

The previous section gives the invariant seam test:

```math
\Delta_Y(P)
=
I(X;Z\mid Y).
```

Einstein's next demand is:

```text
Can the physical screen Y be derived as the unique minimal record closure with
Delta_Y=0?
```

The diagnostic is:

```text
code/v6_p3ad_minimal_complete_screen_campaign.py
```

The finite answer is conditional. A minimal complete screen is derivable in a
real finite class, but not for arbitrary laws and not from correlations alone.

### 40.1 Selection rule

Let `C_x` be the intrinsic causal candidate lattice of antichain record
closures between lower screen `X` and upper screen `Z`. For every candidate
closure `Y in C_x`, compute:

```math
\Delta_Y
=
D\!\left(
P_{XYZ}
\;\middle\Vert\;
{P_{XY}P_{YZ}\over P_Y}
\right)
=
I(X;Z\mid Y).
```

Then select `Y_*` if:

```text
1. Delta_Y* = 0;
2. no proper causal candidate subclosure has Delta=0;
3. every other non-equivalent candidate has Delta >= eta > 0;
4. the same Y_* is obtained by every role readout;
5. duplicate record copies are quotiented by internal automorphism.
```

This is the **minimal complete RN record closure** principle.

### 40.2 Positive finite classes

The simplest positive case is a finite mediator:

```text
X -> S -> Z
```

with an irrelevant noise record `N`. Scanning causal candidates gives:

```text
minimal = {S};
margin = 0.075656;
best Delta = 0.
```

So the noise record is rejected and the mediator screen is derived.

The second positive case contains a bypass record:

```text
X -> S -> Z,
X -> H -> Z.
```

The correct screen is the enlarged closure:

```text
minimal = {S,H};
singletons fail;
margin = 0.011417;
best Delta = 0.
```

This is the finite version of "enlarge the seam until all relevant records are
inside it." The physical screen is not the smallest-looking screen. It is the
smallest complete record closure.

### 40.3 Failure modes

If the bypass record `H` is not in the candidate closure lattice, no complete
screen is found:

```text
best Delta = 0.011417;
verdict = FAIL-NO-COMPLETE-SCREEN.
```

If there is an unrecorded direct channel from `X` to `Z`, even scanning all
available records fails:

```text
best Delta = 0.073040;
full closure still fails.
```

This is the clean branch-A falsifier. Branch A-current requires that physical
influences crossing a seam are recordable in the intrinsic closure lattice. If
there are unrecorded bypasses, the screen is not derived.

If future/oracle variables are allowed, the rule cheats. A future copy

```text
O = Z
```

screens trivially:

```text
all minimals = {O},{S};
causal minimal = {S}.
```

Thus causal admissibility is not decoration. Candidate screens must be
causal antichain separators between lower and upper screens.

If a record is duplicated exactly:

```text
D = S,
```

the scan returns:

```text
minimals = {D},{S}.
```

This is nonunique as a label statement but unique after quotienting by the
internal automorphism that identifies duplicate copies of the same record. If
the quotient is not intrinsic, the screen is supplied.

If a duplicate is noisy but close, the minimizer is unique but the margin can
be small:

```text
minimal = {S};
margin = 0.002204.
```

So refinement stability requires a cofinal margin lower bound, not merely a
zero defect at one finite level.

Finally, role-blindness is essential. A role-split construction gives:

```text
record screen = {S};
source screen = {H};
same = false.
```

That is branch B: different readouts do not identify the same physical seam.

### 40.4 Audit

| target | law | scan | positive | obstruction | value | verdict |
|---|---|---|---|---|---|---|
| minimal mediator | `X-S-Z` plus noise | scan causal candidates | minimal `{S}` | margin `0.075656` | best `0.0e+00` | PASS-UNIQUE-MINIMAL |
| bypass closure | two recorded channels | enlarge screen | minimal `{S,H}` | singletons fail; margin `0.011417` | best `0.0e+00` | PASS-UNIQUE-MINIMAL |
| missing record | `H` not in candidates | try available closure | best Delta `0.011417` | no zero RN screen | candidate set incomplete | FAIL-NO-COMPLETE-SCREEN |
| unrecorded direct channel | direct `X->Z` term | scan all records | best Delta `0.073040` | influence not recorded in screen | full closure still fails | FAIL-NO-COMPLETE-SCREEN |
| duplicate gauge screen | `D=S` copy | scan record copies | minimals `{D},{S}` | two exact screens | same record up to automorphism | COND-QUOTIENT-NEEDED |
| near-duplicate screen | `D` noisy copy of `S` | scan stability margin | minimal `{S}` | margin `0.002204` | small margin means drift risk | PASS-UNIQUE-MINIMAL |
| future oracle | `O=Z` upper copy | scan without causality | all minimals `{O},{S}` | future variable screens trivially | causal minimal `{S}` | FAIL-NEED-CAUSAL-ADMISSIBILITY |
| role split | different role laws | scan per role | record `{S}` | source `{H}` | same `False` | FAIL-NOT-ROLE-BLIND |
| finite theorem packet | causal complete closure | unique zero Delta screen | screen derived | requires gates above | minimal complete RN closure | THM-CONDITIONAL-MCS |

The finite theorem is:

```text
Conditional minimal complete screen theorem.
Let C_x be the intrinsic causal antichain record-closure lattice of a sealed
diamond. If there is a unique minimal equivalence class [Y_*] such that

  Delta_Y* = I(X;Z|Y_*) = 0,

all non-equivalent candidates have Delta >= eta > 0, and the same class is
obtained by record/source/causal/screen readouts, then Y_* is derived as the
physical gluing screen.
```

The finite no-go is:

```text
The theorem fails without causal admissibility, record completeness,
automorphism quotienting, role-blindness, and a refinement-stable margin.
```

This settles the current question. A physical screen can be derived, but only
as a **minimal complete RN record closure**. Branch A-current therefore
requires the physical sealed process to guarantee:

```text
every genuine seam has a unique role-blind minimal complete RN closure,
up to internal automorphism, with cofinal positive margin.
```

If that guarantee is supplied as an admissibility axiom rather than derived
from the dynamics of sealed record formation, the theory is branch B. If it is
proved as a property of the physical process, the screen, `Q`, `C`, `rho`,
and bridge composition become one invariant package.

---

## 41. Record-completeness closure campaign [PROBE]

The previous section identifies the last hidden assumption:

```text
record completeness.
```

Einstein's objection is:

```text
Why must every influence crossing a seam be represented in the intrinsic
record-closure lattice?
```

The diagnostic is:

```text
code/v6_p3ae_record_completeness_closure_campaign.py
```

The finite campaign changes the question. Record completeness is not a
universal property of arbitrary finite laws. The intrinsic object is the
**seam residual spectrum**:

```math
\epsilon_*
=
\min_{Y\in{\cal C}_x}
I(X;Z\mid Y),
```

where `${\cal C}_x` is the causal antichain record-closure lattice. The
physical law should not say "all seams are complete." It should say:

```text
no silent seam.
```

That means every seam is one of two things:

```text
eventless seam:
  epsilon_* = 0 with a unique minimal role-blind complete screen;

eventful seam:
  epsilon_* > 0 with an isolated role-blind residual floor.
```

In the eventful case, the residual is not a missing convention. It is the
event/source defect.

### 41.1 Closure by RN-defect reduction

Start with a causal candidate screen and add only records that reduce the seam
defect:

```text
Y -> Y union {r}
if
I(X;Z|Y union {r}) < I(X;Z|Y).
```

In the simple mediator law:

```text
X -> S -> Z
```

with irrelevant noise `N`, the closure path is:

```text
{S}
```

and the defect is:

```text
Delta = 0;
minimal = {S}.
```

The noise record is not selected.

In the recorded-bypass law:

```text
X -> S -> Z,
X -> H -> Z,
```

the closure path is:

```text
{S} -> {H,S}.
```

The final defect is zero:

```text
Delta = 0;
final = {H,S}.
```

Thus recorded bypasses do not break the theorem. They enlarge the screen.

### 41.2 Silent influence is the falsifier

If `H` exists physically but is omitted from the candidate closure lattice, the
residual remains:

```text
epsilon_* = 0.011417.
```

If that residual is ignored, the theory has a silent influence. That is
branch B.

If there is a direct unrecorded channel:

```text
X -> Z
```

then even scanning all available records gives:

```text
epsilon_* = 0.073040;
no zero screen.
```

This is not an eventless seam. The correct branch-A-current interpretation is:

```text
positive isolated residual = event/source defect.
```

So record completeness becomes a dichotomy. Either the seam closes, or the
non-closing residual is itself the event.

Weak residuals expose the finite floor issue:

```text
epsilon_* = 0.000389;
floor = 0.010.
```

Without a cofinal positive floor, the residual is not a stable objective
event. It is finite noise, a refinement artifact, or an unresolved limit.

### 41.3 Causality, quotienting, and role-blindness

Causal admissibility remains essential. A future oracle `O=Z` would screen
trivially:

```text
all minimals = {O},{S}.
```

But after restricting to causal candidates:

```text
causal minimal = {S}.
```

Duplicate records also need the internal automorphism quotient. If `D=S`,
the scan returns:

```text
minimals = {D},{S}.
```

This is nonunique by label, but one screen class after quotienting.

Role-blindness is the final gate. If record and source readouts select
different closures:

```text
record = {S};
source = {H};
```

then the seam is not one physical fact.

### 41.4 Cofinal floor

The finite refinement test compares a stable residual family with a decaying
residual family:

```text
stable min epsilon_* = 0.073486;
decay min epsilon_*  = 0.000012;
floor = 0.010.
```

The stable residual can be an event. The decaying residual cannot lock an
objective event scale.

### 41.5 Audit

| target | law | invariant | positive | obstruction | value | verdict |
|---|---|---|---|---|---|---|
| eventless mediator | `X-S-Z` plus noise | closure by Delta decrease | path `{S}` | noise not selected | Delta `0.0e+00`; minimal `{S}` | PASS-EVENTLESS-COMPLETE |
| recorded bypass | `X-S/H-Z` | closure adds records | path `{S} -> {H,S}` | single `S` incomplete | Delta `0.0e+00`; final `{H,S}` | PASS-CLOSURE-COMPLETES |
| missing record | `H` omitted | residual spectrum | epsilon* `0.011417` | positive but unrepresented | candidate lattice incomplete | FAIL-SILENT-IF-IGNORED |
| direct residual | unrecorded `X->Z` | min residual epsilon* | epsilon* `0.073040` | no zero screen | path `{S} -> {H,S}` | PASS-RESIDUAL-EVENT |
| weak residual | tiny direct term | floor test | epsilon* `0.000389` | floor `0.010` | margin `0.004189` | FAIL-NO-ISOLATED-FLOOR |
| causal admissibility | future oracle `O=Z` | exclude future screen | causal `{S}` | all `{O},{S}` | oracle would cheat | PASS-ONLY-CAUSAL-LATTICE |
| duplicate quotient | `D=S` | automorphism class | minimals `{D},{S}` | labels nonunique | one screen class after quotient | PASS-CONDITIONAL-QUOTIENT |
| role split | record/source differ | role-blind test | record `{S}` | source `{H}` | screen class mismatch | FAIL-ROLE-COMPLETENESS |
| refinement floor | stable vs decaying residual | cofinal epsilon* | stable min `0.073486` | decay min `0.000012` | floor `0.010` | PASS-STABLE-FAILS-DECAY |
| no-silent-seam law | sealed process | epsilon*=0 or event floor | eventless screen or event | silent residual forbidden | record completeness becomes dichotomy | THM-TARGET-NO-SILENT-SEAM |

The final theorem target is:

```text
No-silent-seam theorem.
For every physical sealed diamond and every intrinsic causal seam, the
residual RN spectrum over causal antichain record closures satisfies exactly
one of:

1. epsilon_* = 0, with a unique role-blind minimal complete screen up to
   internal automorphism;

2. epsilon_* >= epsilon_0 > 0 cofinally, with a unique role-blind residual
   event/source defect.

There is no third case in which positive seam influence is neither recorded
by a complete screen nor counted as an event.
```

This fully exposes the branch boundary:

```text
Branch A-current:
  alive if the physical sealed process proves the no-silent-seam theorem.

Branch B:
  the verdict if the closure lattice, event floor, role agreement, or residual
  classification is supplied externally.
```

This is the tightest current Einstein form. Record completeness is not an
axiom that all seams are already complete. It is the eventless side of a
stronger invariant dichotomy:

```text
complete screen or objective residual event.
```

---

## 42. Origin of the no-silent-seam law [PROBE]

The preceding section gives the correct law-form:

```text
complete screen or objective residual event.
```

Einstein's last question is:

```text
Why should physics obey this law?
```

The diagnostic is:

```text
code/v6_p3af_no_silent_seam_origin_campaign.py
```

The finite answer is that no-silent-seam is not an aesthetic preference. It is
the RN action-conservation law for sealed gluing.

### 42.1 Silent seam as missing RN action

For a three-screen law `P_XYZ`, the eventless gluing law through `Y` is:

```math
G_Y(P)
=
{P_{XY}P_{YZ}\over P_Y}.
```

The silent part of the seam is exactly:

```math
A_{\rm silent}(Y)
=
D(P_{XYZ}\Vert G_Y(P))
=
D\!\left(
P_{XYZ}
\;\middle\Vert\;
{P_{XY}P_{YZ}\over P_Y}
\right)
=
I(X;Z\mid Y).
```

So if a seam is declared eventless, sealed composition requires:

```math
A_{\rm silent}(Y)=0.
```

Otherwise the eventless glued law is not the full sealed law.

The eventless finite seam gives:

```text
Delta = 9.3e-17;
composition error = 0;
missing action = 9.3e-17.
```

The hidden-bypass seam gives:

```text
Delta = 0.082283;
composition error = 0.400000;
unaccounted action = 0.082283.
```

That is the physical reason. A silent seam gives the wrong composite bridge
and leaves positive RN action unaccounted.

### 42.2 The two intrinsic repairs

There are only two invariant repairs.

First, enlarge the screen. In the recorded bypass law:

```text
X -> S -> Z,
X -> H -> Z,
```

the smaller screen has:

```text
Delta_S = 0.011417.
```

The enlarged screen has:

```text
Delta_SH = 0.
```

So the action is absorbed by a complete record closure:

```text
screen absorbs action.
```

Second, if no record closure makes the residual vanish, count the residual as
an event/source defect. In the unrecorded direct-channel test:

```text
epsilon_* = 0.073040;
no zero screen;
event action = 0.073040.
```

The residual is no longer silent. It is the event.

Weak residuals do not close the theorem:

```text
epsilon_* = 0.000389;
floor = 0.010.
```

Without a cofinal floor, the residual is not a stable objective event.

### 42.3 Cofinal action floor and role-blindness

The refinement test distinguishes stable event action from decaying noise:

```text
stable min epsilon_* = 0.073486;
decay min epsilon_*  = 0.000012;
floor = 0.010.
```

Only the stable residual can be an objective seam event.

The action carrier must also be role-blind. A role-split seam gives:

```text
record = {S};
source = {H};
```

Different roles assign the missing action to different carriers. That is not
one physical seam.

Finally, the residual is invariant under naming. Ignoring or omitting records
does not make the action disappear:

```text
with records = 0.073040;
without H    = 0.102814.
```

Renaming a positive residual as "not an event" does not remove the RN action.

### 42.4 Audit

| target | law | invariant | positive | obstruction | value | verdict |
|---|---|---|---|---|---|---|
| eventless action | Markov seam | `D(P\|\|glue_Y P)` | Delta `9.3e-17` | composition error `0.0e+00` | missing action `9.3e-17` | PASS-EVENTLESS-ACTION |
| silent bypass | same adjacent bridges | `D(P\|\|glue_Y P)` | Delta `0.082283` | composition error `0.400000` | unaccounted action `0.082283` | FAIL-SILENT-BREAKS-ACTION |
| recorded repair | bypass record `H` | enlarge `Y` | Delta_S `0.011417` | Delta_SH `0.0e+00` | screen absorbs action | PASS-RECORD-CLOSURE |
| residual event repair | unrecorded direct term | event work epsilon* | epsilon* `0.073040` | no zero screen | event action `0.073040` | PASS-COUNT-RESIDUAL |
| weak residual | tiny direct term | floor test | epsilon* `0.000389` | floor `0.010` | not stable event work | FAIL-NO-COFINAL-FLOOR |
| cofinal action floor | stable vs decaying | liminf epsilon* | stable `0.073486` | decay `0.000012` | floor `0.010` | PASS-STABLE-ONLY |
| role-blind action | split role seams | same residual class | record `{S}` | source `{H}` | different action carriers | FAIL-ROLE-SPLIT-ACTION |
| deletion locality | ignore residual | local action account | with records `0.073040` | without `H` `0.102814` | residual cannot vanish by naming | PASS-RESIDUAL-INVARIANT |
| no-silent-seam origin | sealed RN process | composition + action conservation | Delta `0` or event work | positive ignored Delta forbidden | nothing crosses for free | THM-CONDITIONAL-NO-SILENT |

The finite theorem is:

```text
No-silent-seam origin theorem, finite form.
Assume a sealed finite RN process has:

1. eventless gluing by the adjacent bridge product P_XY P_YZ/P_Y;
2. RN action conservation under sealed gluing;
3. causal record-closure enlargement when records reduce the seam action;
4. a cofinal positive floor for objective residual events;
5. role-blind action carriers.

Then every seam is either RN-complete or carries a positive residual event.
There is no third case in which positive RN seam action crosses for free.
```

This is the promised physical reason:

```text
nothing crosses a sealed seam for free.
```

More formally:

```text
positive RN seam action must be carried either by the complete screen or by an
objective event.
```

Branch status:

```text
Branch A-current:
  alive if sealed composition and RN action conservation are derived physical
  laws of the record process.

Branch B:
  the verdict if action conservation, the event floor, or role-blind action
  carriers are supplied externally.
```

---

## 43. RN action conservation campaign [PROBE]

The preceding section reduces the branch-A-current hinge to:

```text
sealed composition + RN action conservation.
```

Einstein's next question is:

```text
Is RN action conservation another axiom, or is it forced by sealed measure
composition?
```

The diagnostic is:

```text
code/v6_p3ag_rn_action_conservation_campaign.py
```

The finite answer is strong. Once the physical object is a sealed finite
measure functor with a canonical compositional reference law `U`, RN action
conservation is a theorem.

### 43.1 Multiplicative origin of RN action

For independent sealed composition:

```math
P=P_1\otimes P_2,
\qquad
U=U_1\otimes U_2,
```

Radon-Nikodym densities multiply:

```math
{dP\over dU}
=
{dP_1\over dU_1}
{dP_2\over dU_2}.
```

An additive action density must therefore satisfy:

```math
f(ab)=f(a)+f(b).
```

Under the usual finite regularity/continuity condition, the only solutions
are:

```math
f(a)=c\log a.
```

The finite audit gives:

```text
RN product add error = 2.8e-17;
log Cauchy error     = 2.2e-16;
linear score error   = 0.810.
```

So the logarithm is not a cosmetic choice. It is the unique additive
regraduation of multiplicative likelihood ratios, up to one global unit.

### 43.2 Sealed gluing conservation

Let:

```math
G_Y(P)
=
{P_{XY}P_{YZ}\over P_Y}.
```

If the reference `U` composes through the same seam, then the KL/RN action
splits exactly:

```math
D(P_{XYZ}\Vert U_{XYZ})
=
D(P_{XYZ}\Vert G_Y(P))
+
D(G_Y(P)\Vert U_{XYZ}).
```

The first term is the seam residual:

```math
D(P_{XYZ}\Vert G_Y(P))
=
I(X;Z\mid Y).
```

The second term is the eventless glued action. For the finite eventless seam:

```text
conservation error = 0;
seam term vanishes.
```

For the tilted hidden-bypass seam:

```text
total = 0.534029;
seam  = 0.026776;
glued = 0.507253;
conservation error = 1.1e-16.
```

Thus eventful seams do not violate conservation. They carry an additional RN
action term. Calling that term silent is what violates the action account.

The glued action also decomposes locally:

```math
D(G_Y(P)\Vert U)
=
D(P_{XY}\Vert U_{XY})
+
D(P_{YZ}\Vert U_{YZ})
D(P_Y\Vert U_Y).
```

The finite local action error is:

```text
0.0e+00.
```

This is the inclusion-exclusion action of adjacent sealed bridges.

### 43.3 Failure tests

Non-log scores do not conserve action. For the same tilted bypass law:

```text
sqrt-KL additive error = 0.145077.
```

Local unit scales also fail:

```text
local-scale error = 0.082708.
```

Only a single global unit convention, such as nats versus bits, preserves the
identity:

```text
global-unit error = 2.2e-16.
```

A noncompositional reference law fails as well. If `U` carries a hidden
three-body seam bias, the same RN formula no longer gives a sealed local
action balance:

```text
noncompositional-reference error = 0.017214.
```

So the reference law is not arbitrary. It must be the canonical
compositional reference of the sealed measure functor.

### 43.4 Audit

| target | data | invariant | positive | obstruction | value | verdict |
|---|---|---|---|---|---|---|
| RN product origin | independent sealed product | `d(P1xP2)/d(U1xU2)` | RN densities multiply | log turns product into sum | add error `2.8e-17` | PASS-RN-MULTIPLICATIVE |
| log uniqueness | likelihood ratios | `f(ab)=f(a)+f(b)` | log error `2.2e-16` | linear error `0.810` | only `c log` survives | PASS-LOG-UNIQUE |
| eventless conservation | Markov seam | `D(P\|\|U)=D(P\|\|G)+D(G\|\|U)` | error `0.0e+00` | seam term vanishes | exact eventless action | PASS-RN-CONSERVATION |
| eventful conservation | hidden bypass | total=seam+glued | total `0.534029` | seam `0.026776`; glued `0.507253` | error `1.1e-16` | PASS-RN-SPLIT |
| local bridge action | glued law | `XY+YZ-Y` inclusion | error `0.0e+00` | requires compositional `U` | local action account | PASS-LOCAL-ACTION |
| non-log score | sqrt KL | try additive score | error `0.145077` | breaks conservation | score not action | FAIL-NONLOG-ACTION |
| local unit scales | role/seam scales | scale terms separately | error `0.082708` | local units create/erase action | only global unit allowed | FAIL-LOCAL-UNITS |
| global unit convention | bits vs nats | one global scale | error `2.2e-16` | unit not physical | global convention only | PASS-GLOBAL-UNIT |
| bad reference | noncompositional `U` | triple-biased reference | error `0.017214` | reference carries hidden seam action | `U` must compose | FAIL-NONCOMPOSITIONAL-U |
| branch verdict | sealed measure functor | compositional `U` + log RN | action conservation theorem | physical status of functor remains | RN action not separate axiom | A-CURRENT-BASE-CANDIDATE |

The finite theorem is:

```text
RN action conservation theorem, finite form.
Let sealed diamonds form a finite measure functor with a canonical reference
U that composes under sealed product/gluing. Let action be additive under
independent sealed composition and depend only on the RN likelihood ratio.
Then the action density is c log(dP/dU), and the expected action is c D(P||U).
For any seam Y,

  D(P_XYZ||U_XYZ)
  =
  D(P_XYZ||P_XY P_YZ/P_Y)
  +
  D(P_XY P_YZ/P_Y||U_XYZ).

The residual term is exactly I(X;Z|Y).
```

This closes the previous hinge:

```text
RN action conservation is not an independent axiom once the base ontology is a
sealed measure functor with canonical compositional reference.
```

The remaining primitive is therefore smaller and clearer:

```text
sealed finite measure functor + canonical compositional reference U.
```

Branch status:

```text
Branch A-current:
  alive if this sealed measure functor is accepted or derived as the physical
  base. RN action conservation, no-silent seams, complete screens, Q, C, rho,
  and W are then linked by finite theorems.

Branch B:
  the verdict if the measure functor or U is selected externally after the
  record ontology is already chosen.
```

## 44. Canonical reference `U` campaign [PROBE]

Section 43 reduced the action problem to one last primitive:

```text
sealed finite measure functor + canonical compositional reference U.
```

Einstein's next objection is exact:

```text
If U is supplied, the zero of action is chosen.  What fact inside the sealed
diamond makes U the reference law?
```

The diagnostic is:

```text
code/v6_p3ah_canonical_reference_campaign.py
```

The answer is neither "eventlessness" nor "composition." Both are too weak.
Biased product references can compose, and biased independent laws can have
zero seam residual. The reference is forced only if the physical base is a
sealed finite **count functor**:

```text
1. each sealed diamond has indivisible record atoms;
2. no internal label distinguishes atoms inside a count fiber;
3. the reference is invariant under all internal relabellings;
4. product/gluing composition is functorial;
5. refinement splits count fibers by a canonical measure-preserving rule;
6. the same reference is used for record, source, screen, and action readouts.
```

In that base, the reference is not another field:

```math
U_D(A)={|A|\over |\Omega_D|}.
```

It is the counting reference of the sealed finite record diamond.

### 44.1 Why eventlessness does not fix `U`

For an eventless bridge, the seam residual is:

```math
I(X;Z)=0
```

or, with a screen,

```math
I(X;Z\mid Y)=0.
```

But an independent biased product law also has zero residual. Therefore
eventlessness tells us:

```text
there is no hidden bridge action.
```

It does not tell us:

```text
which product reference is the zero-action state.
```

The finite audit prints:

```text
eventless residual span = 0.0e+00;
bias span = 0.600.
```

So eventlessness alone is not an origin of `U`.

### 44.2 Why composition does not fix `U`

Product composition requires:

```math
U_{\Omega\times\Lambda}
=
U_\Omega\otimes U_\Lambda.
```

This is necessary for RN action conservation, but not sufficient. Any chosen
biased `U_\Omega` and `U_\Lambda` can be composed this way. The finite audit
prints:

```text
product error = 0.0e+00;
bias span = 0.600.
```

Thus composition constrains the behavior of `U` once `U` is known. It does not
select `U`.

### 44.3 Relabelling invariance and count atoms

If the sealed diamond supplies only `N` indivisible record atoms and no
internal labels, then every permutation of the atoms is a gauge relabelling.
The reference must satisfy:

```math
U_i=U_{\pi(i)}
```

for every permutation `pi`. Normalization then gives:

```math
U_i={1\over N}.
```

This is the finite origin of the zero-action reference. The finite audit gives:

```text
uniform permutation gap = 0.0e+00;
biased permutation gap  = 0.400.
```

So full internal relabelling symmetry fixes the reference. A biased reference
would secretly distinguish atoms that the sealed diamond itself does not
distinguish.

### 44.4 Orbit-weight obstruction

If the diamond has only a smaller automorphism group with more than one orbit,
then invariance fixes equality inside each orbit but does not fix the weights
between orbits:

```text
orbit 1 atoms share one weight;
orbit 2 atoms share another weight.
```

The finite audit gives:

```text
orbit invariance gap = 0.0e+00;
orbit-weight span    = 1.200.
```

This is the clean obstruction. If the ontology says only "use automorphism
invariance," `U` remains underdetermined whenever the diamond has multiple
internal orbits. Branch A-current therefore needs more than automorphism
invariance. It needs the sealed count functor, or an equivalent intrinsic
measure principle that fixes orbit weights.

### 44.5 Refinement obstruction

Uniformity on atoms is stable under refinement only when refinement is
measure-preserving in the count sense. If each coarse atom splits into the same
number of refined atoms, then pushing refined counting measure down recovers
coarse counting measure:

```text
balanced refinement error = 0.0e+00.
```

If different coarse atoms split into different numbers of refined atoms, naive
uniformity on refined atoms pushes forward to a biased coarse law:

```text
unbalanced refinement drift = 0.333.
```

So the intrinsic reference is not "uniform over whatever discretization is
currently drawn." It is the cofinal count measure transported by intrinsic
refinement maps. If the refinement maps or splitting weights are chosen after
the fact, the reference is not derived.

### 44.6 Role-blindness

The same zero-action reference must be used in every readout:

```text
record;
source;
screen/volume;
RN action.
```

If the record role uses one reference and the source role uses another, the
four-role identity has already failed. The finite audit prints:

```text
role-specific reference span = 0.300.
```

Thus `U` is allowed only as a role-blind count reference of the sealed diamond.
Role-specific reference laws reintroduce branch B.

### 44.7 Audit

| target | data | invariant | positive | obstruction | value | verdict |
|---|---|---|---|---|---|---|
| counting reference | four indivisible atoms | full relabelling invariance | uniform permutation gap `0.0e+00` | biased gap `0.400` | `U_i=1/4` | PASS-FULL-SYMMETRY-U |
| product composition | `Omega x Lambda` | `U_Omega x U_Lambda` | product error `0.0e+00` | composition allows bias | bias span `0.600` | PASS-PRODUCT-BUT-NOT-ENOUGH |
| eventless vacuum | independent product | `I(X;Z)=0` | residual span `0.0e+00` | biased products eventless | bias span `0.600` | FAIL-EVENTLESS-NOT-UNIQUE |
| orbit-weight freedom | two automorphism orbits | orbit invariance only | orbit gap `0.0e+00` | orbit weights free | span `1.200` | FAIL-ORBIT-WEIGHT-FREEDOM |
| maximum count entropy | no constraints | maximize `H` over atoms | entropy gap `0.054115` | requires atom count measure | uniform unique on atoms | PASS-CONDITIONAL-MAXENT |
| balanced refinement | equal atom split | pushforward `U_ref=U` | error `0.0e+00` | balanced fibers required | cofinal stable | PASS-BALANCED-REFINEMENT |
| unbalanced refinement | unequal split fibers | uniform refined atoms | drift `0.333` | coarse `U` moves | needs measure-preserving rule | FAIL-UNBALANCED-REFINEMENT |
| fiber equal split | given refinement map | split parent mass equally | push error `0.0e+00` | requires intrinsic map | not a later choice | PASS-CONDITIONAL-FIBER-U |
| role-blind reference | record/source roles | same `U` | record `U` uniform | role span `0.300` | role-specific `U` changes action | FAIL-ROLE-U |
| canonical `U` theorem | sealed count functor | symmetry+product+refinement | `U(A)=|A|/|\Omega|` | requires count atoms and maps | derived if count functor base | THM-CONDITIONAL-CANONICAL-U |

The finite theorem is:

```text
Canonical reference theorem, finite form.
Let D -> Omega_D be a sealed finite count functor. Assume:

1. Omega_D consists of indivisible record atoms;
2. internal relabellings inside each count fiber are gauge symmetries;
3. U_D is invariant under those relabellings;
4. U composes under sealed product/gluing;
5. refinement maps are intrinsic and measure-preserving by equal count
   splitting, or by an equivalent canonical fiber measure;
6. U is role-blind across record, source, screen, and action readouts.

Then the unique reference is

  U_D(A)=|A|/|Omega_D|.

It composes under sealed products, pushes forward under balanced/cofinal
refinements, and supplies the single zero-action reference used by RN action.
```

The corresponding no-go is:

```text
No-go.
Eventlessness, RN action conservation, and product composition do not derive
U.  Biased product references pass those tests.  Orbit-weight freedom and
unbalanced refinement also leave inequivalent U laws unless the count atoms
and refinement maps are intrinsic physical structure.
```

Thus the remaining primitive has changed again, but in a smaller and more
honest direction:

```text
sealed finite count functor with intrinsic cofinal refinement maps.
```

Branch status:

```text
Branch A-current:
  alive if the sealed finite count functor is the physical base. Then U is
  not chosen; it is the unique role-blind count reference. RN action
  conservation and no-silent-seam accounting follow from this base.

Branch B:
  the verdict if atom counts, orbit weights, refinement splits, or role
  references are supplied after the record ontology is chosen.
```

## 45. Sealed finite count-functor origin campaign [PROBE]

Section 44 found the correct next primitive:

```text
sealed finite count functor with intrinsic cofinal refinement maps.
```

Einstein's next demand is:

```text
Do not give me the count functor.  Show me that the closed physical diamond
itself supplies the atoms, the maps, and the role-blind count measure.
```

The diagnostic is:

```text
code/v6_p3ai_count_functor_origin_campaign.py
```

The finite answer is:

```text
a single sealed diamond is not enough.
```

The positive object is slightly more structured:

```text
sealed finite record-algebra functor.
```

That means:

```text
1. each diamond D carries a finite Boolean record algebra B_D;
2. atoms are the minimal nonzero elements of B_D;
3. nested diamonds D <= E carry intrinsic Boolean restriction maps;
4. those maps induce parent maps between atoms;
5. roles are readout maps from the same atom algebra;
6. the reference is the regular count measure, or the projective fiber-count
   measure induced by the same restriction maps.
```

From that object, the count functor is derived. Without that object, it is not.

### 45.1 Atoms are intrinsic only to a full record algebra

In a finite Boolean record algebra, atoms are lattice-theoretic:

```text
minimal nonzero record propositions.
```

For a finite partition, the atoms are its blocks. The finite audit gives:

```text
record algebra atoms = 3;
verdict = PASS-ATOMS-IN-ALGEBRA.
```

This is a real derivation, but it is relative to the supplied record algebra.
If only coarse record blocks are supplied, hidden finer completions are
invisible:

```text
algebra atoms = 3;
hidden micro gap = 3;
verdict = FAIL-COARSE-NOT-FULL.
```

So the correct statement is:

```text
The diamond derives atoms from its full record algebra.
It does not derive a hidden finer atomization from a coarse observable algebra.
```

### 45.2 Endpoint diamonds do not determine refinement maps

Let one diamond have two coarse atoms and a refinement have four fine atoms.
The endpoint atom counts alone allow many surjective refinement maps:

```text
onto maps = 14.
```

Those maps give different pushforwards of uniform fine count measure:

```text
push span = 1.000.
```

Therefore the endpoint data:

```text
four fine atoms;
two coarse atoms;
sealedness;
counting.
```

do not select the refinement map. The map is selected only if the ontology
contains the nested record-algebra relation. Then each fine atom restricts to
a unique coarse atom:

```text
fine atom has unique parent.
```

This is the main no-go:

```text
cofinal refinement maps are not derived from isolated diamonds.
They are derived from the record-algebra functor of nested diamonds.
```

### 45.3 Regular and irregular refinements

If every coarse atom splits into the same number of fine atoms, uniform count
measure is stable:

```text
regular 2/2 split error = 0.0e+00.
```

But regular maps are only a subfamily. In the finite 4-to-2 case:

```text
regular maps = 6 of 14.
```

An irregular 3/1 split breaks global uniform refinement:

```text
drift = 0.500.
```

This gives the refinement theorem boundary:

```text
Global uniform count at every level is compatible only with regular covers.
```

For irregular covers, there is still a canonical projective count measure if
the parent map is intrinsic. Split each parent mass equally among its children.
Then:

```text
projective push error = 0.0e+00;
fine-level nonuniformity = 0.500.
```

That is not a defect. It says the fine atoms are not all equivalent; their
parent fibers distinguish them. The measure is still intrinsic if the parent
map is intrinsic.

Thus Branch A-current has two finite options:

```text
regular-cover branch:
  cofinal refinements are regular, so normalized count is uniform at each
  finite level.

projective-fiber branch:
  refinements may be irregular, but the restriction functor supplies parent
  fibers and U is the projective fiber-count measure.
```

Both are branch-A-compatible only if the refinement maps are physical, not
chosen after the fact.

### 45.4 Role identity requires a common atom algebra

Record and source marginals can agree while the one-event identity fails. The
finite audit compares two laws with the same record/source counts but different
joint role identification:

```text
joint span = 1.000.
```

So same marginal role data do not prove:

```math
E_x^{\rm record}=E_x^{\rm source}.
```

The positive theorem needs one common atom algebra. If record, source, screen,
and action are all readouts of the same atom, role identity is internal:

```text
role mismatch = 0.
```

Thus the four-role identity is not a matching of four separate ledgers. It is
the statement that the four readouts are maps from the same sealed record atom.

### 45.5 Audit

| target | data | invariant | positive | obstruction | value | verdict |
|---|---|---|---|---|---|---|
| record algebra atoms | finite Boolean algebra | minimal nonzero elements | atoms `3` | requires full record algebra | lattice-intrinsic | PASS-ATOMS-IN-ALGEBRA |
| coarse records only | partition blocks | observable algebra atoms | algebra atoms `3` | hidden micro gap `3` | micro-atoms not seen | FAIL-COARSE-NOT-FULL |
| endpoint refinements | four fine, two coarse atoms | surjective maps | onto maps `14` | endpoint data do not select | push span `1.000` | FAIL-ENDPOINTS-NOT-MAP |
| restriction functor | nested Boolean algebras | atom restriction | fine atom has unique parent | requires inclusion map | canonical if functor given | PASS-MAP-FROM-FUNCTOR |
| regular cover | 2/2 fiber split | uniform pushforward | error `0.0e+00` | regular maps `6` of `14` | count stable | PASS-REGULAR-COUNT |
| irregular cover | 3/1 fiber split | uniform fine atoms | drift `0.500` | global count not stable | needs fiber measure | FAIL-IRREGULAR-GLOBAL-U |
| projective fiber count | 3/1 split with parent mass | equal split in each fiber | push error `0.0e+00` | nonuniformity `0.500` | stable if parent map intrinsic | PASS-CONDITIONAL-FIBER-COUNT |
| role marginals | record/source counts | same marginal laws | marginals match | joint span `1.000` | one-event identity not fixed | FAIL-MARGINAL-ROLES |
| common role atoms | one Boolean algebra | role maps share atoms | mismatch `0` | requires common algebra | role identity internal | PASS-ROLE-MAPS-FROM-ALGEBRA |
| single diamond | one closed algebra | no cofinal maps | atoms yes | refinement/action scale no | cannot be enough | NO-GO-SINGLE-DIAMOND |
| count-functor theorem | record-algebra functor | atoms+restrictions+fiber count | all maps internal | physical existence open | branch-A base candidate | THM-CONDITIONAL-COUNT-FUNCTOR |

### 45.6 Finite theorem and no-go

The positive theorem is:

```text
Sealed finite record-algebra functor theorem, finite form.
Let D -> B_D be a functor from sealed finite causal diamonds to finite
Boolean record algebras.  For every nested pair D <= E, let the physical
nesting supply a Boolean restriction map r_ED: B_D -> B_E, equivalently a
parent map At(B_E) -> At(B_D).  Let record, source, screen, and action be
readout maps from At(B_D), not separate atom sets.

Then:

1. atoms are the minimal nonzero elements of B_D;
2. refinement maps are induced by atom restriction;
3. role identity is internal because all roles read the same atoms;
4. U is the normalized count measure for regular covers;
5. more generally, U is the projective fiber-count measure obtained by
   splitting each parent mass equally among its children;
6. U composes and refines through the same functor used by RN action.
```

The no-go is:

```text
No-go.
A single closed diamond, endpoint atom counts, eventlessness, matching role
marginals, and product composition do not determine the sealed finite count
functor.  There are finite same-endpoint/different-refinement counterexamples
and same-marginal/different-role-identity counterexamples.
```

This is the Einsteinian closure point:

```text
The primitive cannot be a single diamond plus a later reference measure.
The primitive must be the sealed finite record-algebra functor itself.
```

Branch status:

```text
Branch A-current:
  alive if physical sealed diamonds intrinsically form this record-algebra
  functor.  Then atoms, role identity, refinement maps, U, RN action, and
  no-silent seams are linked by finite theorems.

Branch B:
  the verdict if the record algebra, nesting maps, regular/projective
  refinement rule, or common role atom maps are supplied externally.
```

## 46. Sealed Leibniz record-functor campaign [PROBE]

Section 45 left the deepest remaining question:

```text
Why should physical sealed diamonds form a record-algebra functor?
```

The Einsteinian answer cannot be "because it is useful." It has to be a
principle saying what counts as a real record distinction. The candidate is:

```text
Sealed Leibniz record principle.
Two alternatives inside a sealed diamond are the same physical atom if no
possible invariant, repeatable, nondisturbing sealed record test can
distinguish them.
```

Equivalently, for each finite diamond `D`, let:

```text
H_D = finite possible sealed local histories/germs allowed by the physical law;
T_D = all invariant, repeatable, nondisturbing sealed record tests in D.
```

Define:

```math
h\sim_D h'
\quad\Longleftrightarrow\quad
T(h)=T(h')\quad\hbox{for every }T\in T_D.
```

Then the record atoms are:

```math
{\rm At}(D)=H_D/\sim_D.
```

The Boolean record algebra is:

```math
B_D=\mathcal P({\rm At}(D)).
```

This is not a detector convention. It is a finite Leibniz quotient: no
physical distinction without a possible sealed record distinction.

The diagnostic is:

```text
code/v6_p3aj_leibniz_record_functor_campaign.py
```

### 46.1 Actual outcomes are not enough

The same actual transcript:

```text
event 0 occurred
```

can sit inside different possible spaces:

```text
binary alternatives:  {0,1};
ternary alternatives: {0,1,2}.
```

The actual fact is identical, but the zero-action reference changes:

```text
RN zero span = 0.405.
```

So the ontology cannot be actual-outcome-only. A record theory must include the
law of possible sealed record distinctions. Otherwise the reference, action
zero, and atom count are underdetermined.

### 46.2 Repeatability is not enough

A test can be individually repeatable:

```text
T^2=T
```

and still fail to commute with another repeatable test. The finite audit uses
two idempotent maps with:

```text
idempotence error = 0;
order gap = 1.
```

Thus repeatability alone does not make a joint objective record algebra.
Stable records need nondisturbing compatibility: reading one record must not
alter the other sealed record.

When two bit readouts are nondisturbing, the joint signatures give:

```text
atoms = 4;
Boolean size = 16.
```

This is the finite classical record algebra.

### 46.3 The Leibniz quotient constructs atoms

Given possible histories and all sealed record tests, the quotient by equal
test signatures constructs atoms:

```text
classes = 4;
Boolean size = 16.
```

An incomplete readout family fails. With parity only:

```text
classes = 2;
hidden response split = 2.
```

Adding the response-distinguishing readout completes the algebra:

```text
classes = 4;
hidden response split = 0.
```

So the complete record algebra is not guessed. It is the quotient by all
possible stable sealed record distinctions. If a hidden difference can affect
any sealed response, it must appear as a further record distinction. If it
cannot affect any possible sealed record distinction, the Leibniz principle
identifies it.

### 46.4 Nested compatibility constructs the functor

For nested diamonds `D <= E`, restriction is well-defined only if `D`-tests are
included as restricted `E`-tests. In the compatible finite case:

```text
restriction ambiguity = 0.
```

In the bad case, an `E`-atom has two different `D` images:

```text
restriction ambiguity = 2.
```

So functoriality is not decorative. It is the statement:

```text
the same sealed record fact has the same restriction no matter which
intermediate diamond is used.
```

If `F <= E <= D`, then:

```math
r_{FD}=r_{ED}\circ r_{FE}.
```

A conflicting direct map gives:

```text
path gap = 2.
```

That is a real failure: the record assigned to a subdiamond depends on the
route used to restrict it.

### 46.5 Roles and count units

Separate role ledgers do not determine one-event identity. The finite audit
keeps the same record/source marginals while changing the joint identity:

```text
joint span = 1.000.
```

If roles are readout functions on the same Leibniz atoms, the mismatch is:

```text
mismatch = 0.
```

The reference measure also needs the count-unit quotient. If two Leibniz atoms
have hidden representative multiplicities `1` and `3`, counting hidden
representatives gives a different reference from counting physical atoms:

```text
U span = 0.500.
```

But the hidden multiplicity is unobservable by hypothesis. The sealed Leibniz
count rule is:

```text
one physical Leibniz atom, one count unit.
```

Then:

```text
permutation gap = 0.0e+00.
```

So `U` is fixed on the quotient atom set.

### 46.6 Audit

| target | data | invariant | positive | obstruction | value | verdict |
|---|---|---|---|---|---|---|
| actual transcript | same event occurred | actual outcome only | actual data identical | possible spaces differ | RN zero span `0.405` | FAIL-ACTUAL-NOT-MODAL |
| repeatability alone | idempotent tests | `T^2=T` | idempotence `0` | order gap `1` | no joint record | FAIL-REPEATABLE-NOT-BOOLEAN |
| nondisturbing tests | two bit readouts | joint signatures | atoms `4` | requires commutation | Boolean size `16` | PASS-JOINT-BOOLEAN |
| Leibniz quotient | possible histories | all sealed readouts | classes `4` | requires possible-test law | Boolean size `16` | PASS-QUOTIENT-ALGEBRA |
| incomplete readouts | parity only | hidden response | classes `2` | split `2` | not complete | FAIL-HIDDEN-RESPONSE |
| completed readouts | parity+response | response-stable classes | classes `4` | split `0` | complete under tests | PASS-COMPLETE-RECORD |
| nested compatibility | `E=(a,b), D=a` | restriction of tests | ambiguity `0` | requires `D`-tests included | well-defined map | PASS-RESTRICTION-WELL-DEFINED |
| bad nesting | `E` knows `b`, `D` asks `a` | restriction attempt | ambiguity `2` | same `E` atom has two `D` images | no functor | FAIL-NESTING-INCOMPATIBLE |
| path independence | `F<=E<=D` | restriction composition | via map fixed | path gap `2` | direct map cannot differ | FAIL-UNLESS-FUNCTORIAL |
| role ledgers | same marginals | separate role atoms | marginals match | joint span `1.000` | identity not fixed | FAIL-SEPARATE-ROLES |
| role readouts | same quotient atom | functions on atoms | mismatch `0` | requires common quotient | one event | PASS-COMMON-ROLE-READOUTS |
| hidden multiplicity | two Leibniz atoms | count representatives | same quotient | `U` span `0.500` | multiplicity is unobservable | FAIL-HIDDEN-MULTIPLICITY |
| count-unit quotient | Leibniz atoms | one atom one unit | perm gap `0.0e+00` | requires no hidden multiplicity | `U` fixed on quotient | PASS-COUNT-UNIT |
| Leibniz functor theorem | possible sealed records | quotient+nested tests+count unit | record functor constructed | physical possible-change law open | branch-A base principle | THM-CONDITIONAL-LEIBNIZ-FUNCTOR |

### 46.7 Finite theorem and no-go

The positive theorem is:

```text
Sealed Leibniz record-functor theorem, finite form.
Assume a physical law supplies, for every sealed finite diamond D:

1. a finite set H_D of possible sealed local histories/germs;
2. a class T_D of invariant, repeatable, nondisturbing sealed record tests;
3. nested compatibility: tests in a subdiamond are restrictions of tests in
   any larger diamond containing it;
4. count-unit identity: hidden multiplicity inside a Leibniz equivalence class
   has no physical count.

Define h ~_D h' iff every T in T_D gives the same value on h and h'.  Then
At(D)=H_D/~_D is intrinsic, B_D=P(At(D)) is the finite Boolean record
algebra, nested restrictions induce functorial atom maps, role readouts are
functions on the same atoms, and U_D is the count/projective fiber-count
reference on At(D).
```

The no-go is:

```text
No-go.
Actual outcomes, repeatability alone, endpoint diamonds, matching role
marginals, and hidden representative counts do not derive the record-algebra
functor.  They admit finite counterexamples with different possible spaces,
noncommuting repeatable tests, bad restrictions, different role identities,
and different U laws.
```

This gives the cleanest current branch-A primitive:

```text
sealed Leibniz record process:
the physical law of all possible invariant sealed record distinctions,
quotiented by no-distinction-without-possible-record-difference.
```

Branch status:

```text
Branch A-current:
  closed at finite structural level if the sealed Leibniz record process is
  accepted as the physical base.  The record-algebra functor is then
  constructed, not chosen.

Branch B:
  the verdict if H_D, T_D, nested compatibility, or the count-unit quotient are
  supplied externally after the ontology is chosen.

Physical-existence gate:
  finite mathematics cannot prove that nature realizes this possible-change
  law.  That is the empirical/theoretical base principle still to be judged.
```

## 47. Sealed record field-equation campaign [PROBE]

Section 46 gives the cleanest current kinematics:

```text
sealed Leibniz record process.
```

It constructs:

```text
atoms;
Boolean record algebra;
nested restrictions;
role readouts;
count/projective reference U;
RN action units.
```

Einstein's final demand is the dynamics question:

```text
What is the record analogue of the field equation?
```

In finite terms, the missing law is:

```text
D -> (P_D, delta_D)
```

where `P_D` is the physical probability law on sealed Leibniz atoms and
`delta_D` is the intrinsic deletion/intervention law. The diagnostic is:

```text
code/v6_p3ak_record_field_equation_campaign.py
```

The finite answer is sharp:

```text
the sealed Leibniz record process closes the kinematics, not the dynamics.
```

### 47.1 Same structure, different event rates

Take the same binary record functor on strings of length `n`:

```text
At(D_n)={0,1}^n;
U_D = uniform count;
restriction = bit marginalization.
```

For every Bernoulli parameter `p`, the product law:

```math
P_p(a)=p^{|a|}(1-p)^{n-|a|}
```

has the same atoms, same `U`, same role grammar, and same restrictions. It is
also projectively consistent:

```text
projective error = 4.2e-17.
```

But its event density changes:

```text
gamma span = 0.600.
```

Therefore the record functor does not determine `gamma`.

### 47.2 Same structure and same event density, different memory scale

Now keep stationary event density fixed at:

```text
gamma = 0.500.
```

Use stationary binary Markov laws with different flip probabilities:

```math
P_q(a_1,\ldots,a_n)
=
{1\over 2}\prod_{i=1}^{n-1}
\begin{cases}
1-q,& a_i=a_{i+1},\\
q,& a_i\ne a_{i+1}.
\end{cases}
```

The atoms, `U`, and restrictions are unchanged. The event rate is unchanged.
The correlation length changes:

```text
corr span = 0.600;
beta inverse span = 3.860.
```

Therefore the record functor does not determine `beta`.

### 47.3 No-silent seams are not dynamics

For a three-bit Markov chain `X-Y-Z`, the no-silent-seam condition is:

```math
I(X;Z\mid Y)=0.
```

The finite audit gives:

```text
CMI max = 0.0e+00
```

for several transition probabilities:

```text
q in {0.1, 0.25, 0.4}.
```

So no-silent-seam accounting is necessary but not dynamical. It says the seam
has no hidden residual. It does not select the transition law.

### 47.4 Observational probability does not determine deletion

Even a fixed observational law `P(X,Y)` does not determine intervention. The
finite audit compares two deletion readings:

```text
1. delete X by marginalizing X;
2. delete X by clamping to the no-event branch X=0.
```

Both are compatible with the same observational `P`. Their downstream response
differs:

```text
Y-response gap = 0.800.
```

Therefore `delta_D` is not contained in the observational probability law. It
must be an intrinsic natural deletion map, or an equivalent deletion-response
rule.

### 47.5 Entropy and boundary constraints do not close dynamics

With only atoms and `U`, maximum entropy gives:

```text
P=U.
```

The finite audit reports:

```text
uniform gap = 0.0e+00.
```

That is unique but physically empty: it does not give source rates, memory,
heating, or nontrivial events.

If one adds a mean event constraint, the exponential-family law is unique, but
the constraint value is supplied. The audit gives:

```text
gamma span = 0.600.
```

So boundary/source constraints are data for solving a dynamics, not the
dynamics itself.

### 47.6 Conditional positive law: RN/Gibbs variational dynamics

If an intrinsic local record action `S_D` is supplied, then the finite
variational law:

```math
P_D
=
\arg\min_P
\left[
D(P\Vert U_D)+E_P(S_D)
\right]
```

has the unique solution:

```math
P_D(a)
=
{U_D(a)e^{-S_D(a)}\over Z_D}.
```

The finite Euler check gives:

```text
Euler error = 1.1e-16.
```

This is the correct finite form of a record field equation for probabilities.
But the action is doing the dynamical work. Scaling the same action form
changes the law:

```text
P span = 0.844.
```

Thus the action scale is not structural. It must be fixed by the physical
record field equation.

Deletion also must be included. The field equation is not just `S_D`; it is:

```text
(S_D, delta_D)
```

where:

```text
S_D       = intrinsic local RN action/potential determining P_D;
delta_D   = intrinsic natural deletion/intervention transformation.
```

### 47.7 Audit

| target | data | invariant | positive | obstruction | value | verdict |
|---|---|---|---|---|---|---|
| same atoms different gamma | binary record functor | same atoms, `U`, restrictions | projective error `4.2e-17` | Bernoulli `p` free | gamma span `0.600` | FAIL-P-NOT-DERIVED |
| same atoms different beta | stationary Markov records | same atoms, `U`, restrictions | gamma `0.500` | corr span `0.600` | beta inverse span `3.860` | FAIL-BETA-NOT-DERIVED |
| no-silent seam family | Markov `X-Y-Z` | `I(X;Z|Y)=0` | CMI max `0.0e+00` | transition parameter free | `q in {0.1,0.25,0.4}` | FAIL-SEAM-NOT-DYNAMICS |
| same `P` different do-delete | observed `X,Y` law | same observational `P` | both maps lawful | intervention not in `P` | response gap `0.800` | FAIL-DO-NOT-DERIVED |
| maximum entropy | atoms+`U` only | maximize `H` | uniform gap `0.0e+00` | selects trivial `U` | no source/memory law | PASS-TRIVIAL-NOT-PHYSICS |
| boundary constraints | same `S=0` | mean event constraints | unique exponential family | constraint value supplied | gamma span `0.600` | FAIL-CONSTRAINT-FREE |
| Gibbs/RN variational law | given action `S` | min `D(P||U)+E[S]` | Euler error `1.1e-16` | `S` is dynamics | `P` unique if `S` fixed | PASS-CONDITIONAL-GIBBS |
| action-scale family | same atoms/action form | scale `S -> cS` | each has unique `P` | scale not structural | `P` span `0.844` | FAIL-SCALE-FREE |
| record field equation | Leibniz functor + `S,delta` | natural action+deletion | `P` and do-response fixed | physical `S_D,delta` open | Einstein equation analogue | THM-CONDITIONAL-FIELD-EQ |

### 47.8 Finite theorem and no-go

The no-go is:

```text
No-go.
The sealed Leibniz record process, by itself, does not determine P_D,
gamma, beta, or delta_D.  Same atoms, U, role readouts, and restrictions
admit finite families with different event rates, different memory widths,
zero no-silent-seam residuals, and different intervention responses.
```

The conditional positive theorem is:

```text
Record field-equation theorem, finite form.
Let the sealed Leibniz record process supply At(D), U_D, roles, and
restriction maps.  If the physical law also supplies:

1. an intrinsic natural local action S_D on the sealed record functor;
2. a role-blind natural deletion/intervention transformation delta_D;
3. a fixed global action unit;
4. boundary/source data only as boundary data, not as fitted dynamics;

then P_D is uniquely determined by

  P_D(a)=U_D(a) exp(-S_D(a))/Z_D,

and deletion responses are determined by delta_D.  The pair (S_D, delta_D)
is the record analogue of a field equation.
```

Branch status:

```text
Branch A-current:
  structurally closed by the sealed Leibniz record process;
  physically closed only if (S_D, delta_D) is derived as an intrinsic natural
  law of that process.

Branch B:
  the verdict if S_D, its scale, the transition law, gamma, beta, boundary
  constraints, or delta_D are chosen phenomenologically.
```

This is the current endpoint:

```text
Sealed Leibniz record process = kinematics/equivalence principle.
Intrinsic (S_D, delta_D) law = dynamics/field equation.
```

## 48. Candidate record field-equation campaign [PROBE]

Section 47 identified the missing dynamical object:

```text
(S_D, delta_D).
```

Einstein's next move is not to name it and stop. It is to ask whether the
usual invariant demands already force it:

```text
full relabelling symmetry;
locality;
additivity;
detailed balance;
no-silent seams;
cofinal consistency;
criticality;
minimal disturbance;
natural deletion.
```

The diagnostic is:

```text
code/v6_p3al_field_equation_candidate_campaign.py
```

The finite answer is negative:

```text
the tested invariances do not derive a unique (S_D, delta_D).
```

### 48.1 Full symmetry gives only the trivial law

If the sealed Leibniz atoms carry no role readout or local structure, full
atom relabelling invariance allows only a constant action. The finite audit
prints:

```text
uniform gap = 0.0e+00;
P = U.
```

This is clean but dynamically empty. It does not produce source rates, memory,
or event density beyond the reference law. Full symmetry alone kills
arbitrary bias, but it also kills nontrivial physics.

### 48.2 Local event-count action leaves a free coefficient

Once an event readout `E` is available, the most obvious local additive action
is:

```math
S_h(a)=h\sum_i E_i(a).
```

This is invariant, local, and additive. But `h` is free:

```text
gamma span = 0.462.
```

So event-count locality gives a chemical-potential family, not a field
equation.

### 48.3 Local memory action leaves a free coefficient

With nearest restrictions, a local pair-memory action is:

```math
S_J(a)=J\sum_i {\bf 1}_{a_i\ne a_{i+1}}.
```

This is also local and role-blind. But `J` is free:

```text
memory span = 0.462.
```

The finite local scalar feature space already shows the issue:

```text
dimension = 3;
two nonconstant coefficients remain.
```

The constant term is normalization. The event-count and transition-count
coefficients are dynamics.

### 48.4 Detailed balance and no-silent seams leave families

Detailed balance with stationary reference `U` is necessary for a reversible
transition law, but it does not select the transition:

```text
detailed-balance error = 0.0e+00;
corr span = 0.600.
```

The no-silent-seam condition:

```math
I(X;Z\mid Y)=0
```

also leaves a Markov family:

```text
CMI = 0.0e+00;
transition parameter free.
```

Thus detailed balance and no-silent seams are consistency conditions, not the
record field equation.

### 48.5 Local finite Gibbs form is not automatically cofinal

A local finite Gibbs action defines a probability law on each fixed diamond.
But a fixed finite-nearest-neighbor action form need not be projectively
consistent under restriction:

```text
push error = 0.078.
```

A stationary transfer process can be cofinal:

```text
push error = 0.0e+00.
```

but the transfer parameter remains free:

```text
q free.
```

So cofinality improves the law shape. It still does not select the dynamics.

### 48.6 Criticality and minimum disturbance do not close generally

Criticality can select a point in special models, but the finite record
problem does not contain a universal isolated critical point. In the finite
one-dimensional chain audit:

```text
response span = 0.252;
verdict = FAIL-CRITICALITY-FREE.
```

Minimum disturbance has the same problem for deletion. It can choose a map
only after a disturbance metric or cost is supplied:

```text
metric span = 0.800.
```

Thus neither criticality nor minimal disturbance is a general Einsteinian
closure law unless the metric/cost/critical structure is itself derived.

### 48.7 Natural deletion is not unique

For the same observed correlated law `P(X,Y)`, two role-blind deletion maps are
available:

```text
delete by marginalizing X;
delete by clamping X to the no-event branch.
```

Both are natural enough at this finite level. They give different downstream
responses:

```text
gap = 0.800.
```

Therefore naturality alone does not determine `delta_D`.

### 48.8 Audit

| target | data | invariant | positive | obstruction | value | verdict |
|---|---|---|---|---|---|---|
| full relabelling | bare Leibniz atoms | all atom permutations | uniform gap `0.0e+00` | only constant action | `P=U` | PASS-TRIVIAL-ONLY |
| event-count action | event readout `E` | `S=h sum E` | local/additive | `h` free | gamma span `0.462` | FAIL-FREE-H |
| pair-memory action | nearest restrictions | `S=J transitions` | local/role-blind | `J` free | memory span `0.462` | FAIL-FREE-J |
| local feature space | binary chain | translation local scalars | dim `3` | two nonconstant coefficients | needs dynamics | FAIL-FEATURE-SPACE |
| detailed balance | stationary `U` | `pi_i K_ij=pi_j K_ji` | error `0.0e+00` | flip parameter free | corr span `0.600` | FAIL-DB-NOT-ENOUGH |
| no-silent seam | Markov `X-Y-Z` | `I(X;Z|Y)=0` | CMI `0.0e+00` | transition parameter free | family survives | FAIL-SEAM-FAMILY |
| local Gibbs form | finite chain action | nearest-neighbor `S` | well-defined finite `P` | not automatically cofinal | push error `0.078` | FAIL-LOCAL-NOT-COFINAL |
| transfer process | stationary Markov `K` | cofinal consistency | push error `0.0e+00` | `K` parameter free | `q` free | PASS-COFINAL-BUT-FREE |
| finite criticality | one-dimensional finite chain | response scan | detects response | no isolated universal point | response span `0.252` | FAIL-CRITICALITY-FREE |
| natural deletion | same observed `P` | role-blind maps | multiple natural maps | no unique do-law | gap `0.800` | FAIL-DELETE-FREE |
| minimal disturbance | delete response | minimize change | can pick a map | metric/cost free | metric span `0.800` | FAIL-METRIC-FREE |
| action scale | same action form | `S -> cS` | each law valid | global scale free | gamma span `0.282` | FAIL-SCALE-FREE |
| unique field equation | sealed Leibniz process | natural `S_D` and `delta_D` | would close branch A | not derived by tested invariants | open theorem | OPEN-UNIQUE-FIELD-EQ |

### 48.9 Result

The finite result is:

```text
No tested Einsteinian invariance derives a unique record field equation.
```

The exact no-go is:

```text
No-go under tested principles.
Full relabelling, locality, additivity, detailed balance, no-silent seams,
cofinal consistency, finite criticality, minimum disturbance, and deletion
naturality do not determine (S_D, delta_D).  They either select the trivial
uniform law or leave a family of coefficients, transition laws, scales, or
intervention maps.
```

The remaining theorem target is:

```text
Unique record field-equation theorem.
Derive a unique natural local action S_D and a unique natural deletion
transformation delta_D from the sealed Leibniz record process itself.
```

Until that theorem is proved, the honest branch status is:

```text
Branch A-current:
  structurally closed; dynamically open.

Branch A-full:
  requires the unique record field-equation theorem.

Branch B:
  the status if S_D, delta_D, their coefficients, or their scale are chosen
  phenomenologically.
```

## 49. Stronger record-field rigidity campaign [PROBE]

Section 48 killed the obvious candidates. The remaining question is whether a
stronger Einsteinian mechanism can still close Branch A-full:

```text
natural transformation uniqueness;
RN cocycle rigidity;
deletion-action duality;
refinement/anomaly cancellation;
self-consistency fixed point;
gravity/screen response rigidity;
all of the above together.
```

The diagnostic is:

```text
code/v6_p3am_stronger_rigidity_campaign.py
```

The finite answer is still negative:

```text
the stronger candidates do not produce a finite uniqueness theorem.
```

### 49.1 Natural transformations are not unique

On the binary record functor, the natural local scalar features already include
two independent nonconstant generators:

```text
event count;
transition count.
```

The finite audit gives:

```text
rank = 2.
```

So naturality does not give a unique action. It gives a feature space. A
dynamics is still needed to choose a direction and a scale in that space.

### 49.2 RN cocycles are not rigid

For Bernoulli product laws, the RN action:

```math
A_p(a)=\log {P_p(a)\over U(a)}
```

is a product cocycle:

```math
A_p(xy)=A_p(x)+A_p(y).
```

The finite audit gives:

```text
cocycle error = 2.2e-16.
```

But `p` is free:

```text
span = 6.931.
```

Thus cocycle structure alone does not select the record field equation. It
only says how action composes once a law is chosen.

### 49.3 Deletion-action duality is not unique without a generator rule

One can try to derive deletion from action. But the same correlated law admits
two natural action-compatible readings:

```text
1. deletion as KL projection / marginalization;
2. deletion as removal of the positive branch / clamping.
```

They give different downstream responses:

```text
response gap = 0.800.
```

So deletion-action duality is promising only if the action also supplies a
unique deletion generator. Without that generator condition, `delta_D` remains
free.

### 49.4 Anomaly cancellation leaves the Markov family

Refinement/anomaly cancellation is stronger than finite locality. A stationary
Markov transfer law is exactly projective:

```text
push error = 0.0e+00.
```

But the transition parameter survives:

```text
beta span = 3.860.
```

Therefore anomaly cancellation is necessary but not sufficient. It removes
bad finite actions; it does not isolate the memory scale.

### 49.5 Self-consistency fixed points depend on the map

The idea:

```text
allowed tests depend on P;
P depends on allowed tests;
solve a fixed point.
```

is natural, but it does not close unless the self-consistency map is itself
derived. In a finite logistic toy:

```text
p = F_a(p)
```

has different fixed-point structure as the slope changes:

```text
fixed-point count span = 2.
```

So self-consistency can be a mechanism only after the map `F` is fixed by the
sealed record process. Otherwise it is another parameterized dynamics.

### 49.6 Gravity/screen response leaves the response coefficient

The work/screen objective has the right shape:

```text
information per physical cost.
```

It can produce an interior optimum. But the gravity/screen response coefficient
moves the selected width:

```text
beta span = 0.192.
```

This repeats the earlier C-lock lesson in the new language: source/screen
identity must fix the response amplitude, not merely the source count.

### 49.7 Combined constraints still leave a family

The simultaneous finite family satisfies:

```text
detailed balance;
Markov/no-silent seams;
cofinal consistency;
role-blind U.
```

Yet the memory scale remains free:

```text
beta span = 3.860.
```

So the combination of the tested consistency constraints is still not the
unique record field equation.

### 49.8 Audit

| target | data | invariant | positive | obstruction | value | verdict |
|---|---|---|---|---|---|---|
| natural action space | binary record functor | natural local scalars | rank `2` | rank greater than `1` | event+transition | FAIL-NATURAL-NOT-UNIQUE |
| RN cocycle family | Bernoulli products | `A(xy)=A(x)+A(y)` | cocycle error `2.2e-16` | `p` parameter free | span `6.931` | FAIL-COCYCLE-NOT-RIGID |
| deletion-action duality | same correlated `P` | action-generated deletion | two generators natural | generator condition free | response gap `0.800` | FAIL-DUALITY-NOT-UNIQUE |
| anomaly cancellation | stationary Markov family | projective consistency | push error `0.0e+00` | `q` parameter survives | beta span `3.860` | FAIL-ANOMALY-NOT-ENOUGH |
| self-consistency | tests depend on `P` | `p=F_a(p)` | fixed points exist | map/slope free | count span `2` | FAIL-FIXED-POINT-FREE |
| gravity response | screen/work objective | information per cost | interior optima | response coefficient free | beta span `0.192` | FAIL-GRAVITY-COEFF-FREE |
| simultaneous constraints | DB+Markov+cofinal+`U` | all consistency tests | family survives | memory scale free | beta span `3.860` | FAIL-COMBINED-FAMILY |
| action-deletion generator | same `S/P` | delete from action | projection or clamp | generator convention free | gap `0.800` | FAIL-GENERATOR-FREE |
| rigidity theorem target | sealed Leibniz process | `H^1` unique + anomaly isolate + deletion generated | would close A-full | not found finitely | target named | OPEN-RIGIDITY-THEOREM |

### 49.9 Truth boundary

The finite result is:

```text
No stronger candidate principle tested here derives the unique record field
equation.
```

The exact remaining theorem is:

```text
Record-field rigidity theorem.
For the sealed Leibniz record process, prove all three:

1. natural action cohomology is one-dimensional after imposing all physical
   sealed-record constraints;
2. anomaly/refinement equations isolate the remaining action scale;
3. deletion is generated uniquely by the same action, so delta_D is not an
   independent intervention convention.

Then (S_D, delta_D) is derived.
```

The finite campaign finds the opposite pattern in the tested models:

```text
natural action space dimension > 1;
RN cocycle families survive;
anomaly-free Markov families survive;
self-consistency maps are not unique;
gravity/screen response carries a coefficient;
deletion generation is conventional unless the generator rule is fixed.
```

So the current branch status is:

```text
Branch A-current:
  structurally closed; dynamically open.

Branch A-full:
  possible in principle, but requires the record-field rigidity theorem above.

Branch B:
  the honest status if the action direction, action scale, response
  coefficient, self-consistency map, or deletion generator is supplied.
```

## 50. Whole-diamond action unification campaign [PROBE]

Section 49 asked for a rigidity theorem. There is a more basic question first:

```text
Can one object at least do the three jobs?
```

The three jobs are:

```text
1. RN cocycle / probability law;
2. refinement anomaly / coarse-graining law;
3. deletion generator / intervention law.
```

The diagnostic is:

```text
code/v6_p3an_whole_diamond_action_campaign.py
```

The finite answer is:

```text
yes, conditionally.
```

Given a finite sealed Leibniz atom set `At(D)`, count reference `U_D`, and a
positive law `P_D`, define the whole-diamond RN action:

```math
S_D(a)
=
-\log {dP_D\over dU_D}(a).
```

Equivalently:

```math
P_D(a)
=
{U_D(a)e^{-S_D(a)}\over Z_D}.
```

This action is unique up to an additive constant once `P_D` is supplied:

```text
reconstruction error = 5.6e-17.
```

So the unified object exists. The remaining question is whether the sealed
Leibniz process selects it.

### 50.1 RN cocycle

For a sealed product:

```math
D=D_1\sqcup D_2,
\qquad
S_D(a_1,a_2)=S_{D_1}(a_1)+S_{D_2}(a_2),
```

the RN density composes multiplicatively, so the action composes additively.
The finite audit gives:

```text
product law error = 1.4e-16.
```

This is the cocycle leg.

### 50.2 Refinement anomaly

Let a refinement forget a fiber variable. The coarse law is:

```math
P_{\rm coarse}(b)
=
\sum_{a\mapsto b}P_{\rm fine}(a).
```

The corresponding coarse RN action is generated by log-sum-exp over the same
fine action:

```math
S_{\rm eff}(b)
=
-\log
\mathbb E_{U_{\rm fine}|b}
\left[
e^{-S_{\rm fine}(a)}
\right]
```

up to an additive normalization constant. The finite audit reconstructs the
coarse marginal:

```text
coarse error = 8.3e-17.
```

This is the anomaly leg: the anomaly is not a new object. It is the partition
work of forgotten fibers under the same whole action.

### 50.3 Deletion generator

In a finite product/readout basis, any whole action has a unique Walsh/Mobius
interaction decomposition:

```math
S(a)
=
\sum_{I\subseteq \{1,\ldots,n\}} c_I \chi_I(a).
```

Deleting event/readout `x` has a canonical action-surgery meaning:

```text
remove exactly the interaction terms c_I with x in I.
```

Then the deletion law is the Gibbs law of the reduced action. In the finite
audit:

```text
removed interaction norm = 2.100.
```

The deletion law differs from mere observational marginalization:

```text
marginal gap = 0.546.
```

That is not a bug. It is the point: intervention is not the same operation as
forgetting. The same action supplies both the marginal/refinement operation
and the deletion operation, but they are different readouts of `S`.

This deletion leg is conditional on having the event/readout product basis.
Without that basis, "terms involving x" is not defined.

### 50.4 Non-Markovianity

The finite action may contain whole-diamond terms, for example a triple
interaction:

```math
c_{123}\chi_1\chi_2\chi_3.
```

The audit gives:

```text
I(X;Z|Y)=0.318.
```

So the construction is not secretly Markovian. It supports whole-history /
whole-diamond interactions in the Barandes-aligned indivisible sense.

### 50.5 Why this still does not close Branch A-full

The same machinery works for a family of whole actions. Varying the triple
coefficient preserves the RN, anomaly, and deletion construction:

```text
identities preserved;
P span = 0.790.
```

Scaling the action also preserves the construction:

```text
P span = 0.672.
```

And the same coarse marginal can arise from different fine actions:

```text
same coarse action;
fine action gap = 0.693.
```

Therefore the whole-diamond action solves the unity problem, not the selection
problem.

### 50.6 Audit

| target | data | invariant | positive | obstruction | value | verdict |
|---|---|---|---|---|---|---|
| RN whole action | positive law `P` | `S=-log(dP/dU)` | recon error `5.6e-17` | `P` must be supplied | unique up to const | PASS-RN-ACTION |
| product cocycle | sealed product | `S(xy)=S(x)+S(y)` | law error `1.4e-16` | only for product composition | RN cocycle | PASS-COCYCLE |
| refinement anomaly | forget fibers | log-sum-exp `S_eff` | coarse error `8.3e-17` | requires fine `S` | anomaly from `S` | PASS-ANOMALY |
| deletion generator | Walsh interactions | remove terms involving `x` | removed norm `2.100` | needs product/readout basis | marginal gap `0.546` | PASS-CONDITIONAL-DELETE |
| non-Markovian action | triple interaction | whole-diamond term | CMI `0.318` | not step Markov | allowed | PASS-NONMARKOV |
| same machinery family | vary triple term | RN+anomaly+delete all pass | identities preserved | `S` coefficient free | `P` span `0.790` | FAIL-UNIQUE-S |
| scale family | `S -> cS` | same construction | identities preserved | scale free | `P` span `0.672` | FAIL-SCALE |
| same coarse law | different hidden fibers | same marginal `P` | coarse action same | fine `S` differs | `S` gap `0.693` | FAIL-COARSE-NOT-FINE |
| whole-action theorem | supplied positive `P/S` | RN+anomaly+delete | one object unifies three jobs | does not select `P/S` | conditional success | THM-CONDITIONAL-WHOLE-ACTION |
| selection theorem | sealed Leibniz process only | derive `S` intrinsically | not found | families survive | A-full open | OPEN-SELECTION |

### 50.7 Result

The positive finite theorem is:

```text
Whole-diamond action unification theorem, finite form.
Given a finite sealed Leibniz record diamond with count reference U and a
positive law P, the whole RN action S=-log(dP/dU) is unique up to an additive
constant.  In a finite product/readout basis its Walsh/Mobius decomposition is
unique.  The same S:

1. generates P by the RN/Gibbs law;
2. generates sealed-product RN cocycles;
3. generates refinement anomalies by log-sum-exp over forgotten fibers;
4. generates deletion by removing the unique interaction terms involving the
   deleted event/readout.
```

The no-go is:

```text
Selection no-go.
The whole-action theorem does not derive S.  Families of non-Markovian
whole-diamond actions satisfy all three structural identities while changing
P, scale, hidden fine structure, and deletion response.
```

This is the clean truth:

```text
The unified object exists.
It is the right shape for Branch A-full.
It is not selected by the sealed Leibniz kinematics alone.
```

Branch status:

```text
Branch A-current:
  structurally closed and now dynamically unified conditionally by a
  whole-diamond action.

Branch A-full:
  still requires an intrinsic selection/rigidity theorem for S_D itself.

Branch B:
  the honest status if the whole-diamond action or its coefficients are
  chosen phenomenologically.
```

## 51. Invariant whole-action selection campaign [PROBE]

Section 50 found the right unified object:

```math
S_D=-\log {dP_D\over dU_D}.
```

It also found the remaining Einsteinian objection. The action unifies
probability, refinement anomaly, and deletion, but it is not selected. The
question now is deliberately narrow:

```text
Find the invariant condition on sealed diamonds that makes S_D unique.
```

The diagnostic is:

```text
code/v6_p3ao_action_selection_invariant_campaign.py
```

The result is mostly negative, but it is the clean negative result we needed.
The structural sealed-diamond invariants do not select a unique nontrivial
action.

### 51.1 Orbit theorem: covariance is not selection

Let `At(D)` be the finite atom set of a sealed diamond and let `G_D` be its
internal automorphism group. A covariant whole action must satisfy:

```math
S_D(g a)=S_D(a),
\qquad
g\in G_D.
```

Therefore `S_D` is constant on automorphism orbits. The vector space of
covariant actions is:

```math
\mathbb R^{At(D)/G_D}.
```

Since additive constants do not change the Gibbs/RN law, the nontrivial
covariant action space has dimension:

```math
|At(D)/G_D|-1.
```

This gives the finite no-go:

```text
If |At(D)/G_D| = 1, covariance selects only the uniform/vacuum law.
If |At(D)/G_D| > 1, covariance leaves a continuous family of nonconstant
actions.
```

So pure invariance has the wrong shape. Too much symmetry kills events. Enough
symmetry to allow events leaves coefficients.

The finite audit prints this explicitly. With full atom relabeling and bit-flip
symmetry:

```text
orbit dim = 1;
nontrivial action dimension = 0.
```

With causal-rank shell symmetry on four bits:

```text
orbit dim = 5;
nontrivial action dimension = 4;
P span across invariant shell actions = 0.566.
```

The first case is unique but physically empty. The second case is physically
nontrivial but not unique.

### 51.2 Product composition and RN cocycles

The product condition:

```math
S_{D_1\sqcup D_2}=S_{D_1}+S_{D_2}
```

is the right RN cocycle law, but it is not a selector. Even in the equal-site
case:

```math
S_\theta(a)=\theta\sum_i \sigma_i(a)
```

all `theta` values obey the product law. The finite span across three
allowed scales is:

```text
P span = 1.429.
```

So composition fixes the algebraic way actions combine. It does not fix the
local action scale.

### 51.3 Refinement stability

Refinement stability says that forgotten fibers generate coarse actions by
log-sum-exp:

```math
S_{\rm coarse}(b)
=
-\log
\mathbb E_{U_{\rm fine}|b}
\left[
e^{-S_{\rm fine}(a)}
\right].
```

This is functorial for any fine action. That is why it is powerful as a
consistency law, but weak as a selector. It tells us how a supplied fine
action descends. It does not tell us which fine action exists.

### 51.4 No-silent-seam cycle closure

No-silent-seam consistency can be written as a closed-work condition around
sealed record cycles:

```math
\oint dS=0.
```

In finite form this means the action differences form an exact potential. But
exact potentials can carry arbitrary couplings. The audit tests a two-site
boundary coupling `J`:

```text
cycle residual = 0.0e+00;
P span = 0.822.
```

The seam is not silent: the cycle closes. But the coupling is still free.
No-silent-seam is therefore a consistency condition, not a dynamics.

### 51.5 Fixed units and isolated defects

One might try to remove the scale freedom by normalizing the action after
additive constants:

```math
\|S_D-\langle S_D\rangle\|=1.
```

This can fix one scalar scale. It does not fix the direction in the invariant
action space when that space has dimension greater than one. In the shell
example:

```text
P span across normalized directions = 0.898.
```

Similarly, isolated non-Markovian defects are stable on open parameter
intervals. A triple whole-diamond term gives:

```text
minimum CMI = 0.152;
P span across defect interval = 0.348.
```

That is a good stability result. It is not a uniqueness result.

### 51.6 Max entropy and self-duality

Maximum entropy gives the uniform law unless a nontrivial moment constraint is
supplied. If a mean shell count is supplied, maximum entropy gives an
exponential family:

```math
P_\theta(a)\propto e^{-\theta k(a)}.
```

But the multiplier `theta` is fixed by the supplied moment, not by the sealed
diamond alone. The finite audit gives two different nontrivial constraints:

```text
theta = 0.511 and theta = -0.511;
P span = 0.734.
```

Self-duality or criticality can select a point inside a previously chosen
model family. The standard finite symbol is:

```math
\sinh(2K)=1,
\qquad
K_c=0.4407.
```

This is a real selector only after the graph, the duality map, and the Ising
action family have already been supplied. It does not select the whole action
from sealed diamonds alone.

### 51.7 The only pass that is not a derivation

If the full law `P_D` is supplied, the RN action is unique:

```math
S_D=-\log {dP_D\over dU_D}.
```

The audit reconstructs it with:

```text
reconstruction error = 1.1e-16.
```

But this is not Branch A closure. It is just the section-50 theorem repeated:
given the law, the action is unique. The missing step is deriving the law.

### 51.8 Audit

| target | invariant condition | positive result | obstruction | diagnostic value | verdict |
|---|---|---|---|---|---|
| full internal symmetry | all atom relabelings/bit flips | orbit dim `1` | only constant `S`; no event/defect | nontriv dim `0` | FAIL-NONTRIVIAL |
| causal-rank covariance | permutation-invariant shells | orbit dim `5` | rank-shell coefficients free | `P` span `0.566` | FAIL-SHELL-FAMILY |
| product composition | `S(D1+D2)=S1+S2` | cocycle exact | local action scale remains free | `P` span `1.429` | FAIL-SCALE |
| refinement stability | log-sum-exp coarse action | functorial for any fine `S` | does not choose fine `S` | identity-level | FAIL-SELECTION |
| no silent seams | closed action cycles vanish | cycle residual `0.0e+00` | exact potentials can have any coupling | `P` span `0.822` | FAIL-COUPLING-FREE |
| fixed KL/action unit | normalize `||S||` after constants | scale can be fixed | direction in invariant space remains free | `P` span `0.898` | FAIL-DIRECTION-FREE |
| isolated defect | positive non-Markovian CMI | min CMI `0.152` | open interval, not a point | `P` span `0.348` | FAIL-OPEN-FAMILY |
| maximum entropy | least biased law | uniform if no constraint | nontrivial law needs supplied moment | `theta=0.511/-0.511`, span `0.734` | FAIL-CONSTRAINT-EXTERNAL |
| self-duality/criticality | fixed point of supplied dual map | `Kc=0.4407` | requires chosen graph/family/duality | conditional point | COND-NOT-INTRINSIC |
| full RN data | `P_D` supplied by diamond | `S=-log(dP/dU)` unique | tautological unless `P_D` is derived | recon err `1.1e-16` | PASS-IF-P-SUPPLIED |
| finite no-go | `G`-invariant sealed diamond only | `S` constant on orbits | unique nonconstant `S` impossible without extra equations | `|A/G|-1` degrees | THM-INVARIANT-NO-GO |
| remaining opening | derive the equation `F_D(S)=0` | would select `S` if unique | `F_D` is the missing dynamics | not found here | OPEN-FIELD-EQUATION |

### 51.9 Result

The finite theorem is:

```text
Invariant action-space theorem.
For a finite sealed diamond with atom set At(D) and internal automorphism
group G_D, every covariant whole-diamond action is constant on G_D-orbits.
After quotienting additive constants, the dimension of the covariant action
space is |At(D)/G_D|-1.
```

The corollary is:

```text
Invariant selection no-go.
Structural sealed-diamond invariance alone cannot select a unique nontrivial
whole action.  If the orbit count is one, the only action is the uniform
vacuum-like law.  If the orbit count is greater than one, nontrivial actions
exist as a continuous family.
```

The stronger audited conditions do not close the gap. Product cocycle,
refinement stability, no-silent-seam cycle closure, fixed action units,
isolated defects, maximum entropy, and self-duality either leave a family,
select only the trivial law, or require an externally supplied
constraint/equation/family.

Therefore the target has changed in a precise way:

```text
The missing object is not another invariant adjective on sealed diamonds.
The missing object is an intrinsic record field equation:

F_D(S_D)=0,

derived from the sealed physical process, with a unique nontrivial solution
modulo additive constants.
```

That is the standard Einstein would demand. Branch A-full is not refuted in
principle, but the route is now narrow:

```text
Branch A-full lives only if the sealed record process derives F_D.
Branch B is the honest status if F_D, a constraint, a duality map, or an
action family is chosen.
```

## 52. Relational record field equation campaign [PROBE]

Section 51 refuted the hope that an invariant adjective on sealed diamonds
selects `S_D`. Einstein's next demand is therefore:

```text
The event is relational; the equation must be relational too.
```

The diagnostic is:

```text
code/v6_p3ap_relational_field_equation_campaign.py
```

The campaign finds the right finite equation form:

```math
F_D(S_D)=L_D S_D-\rho_D=0.
```

Here:

```text
L_D   = the relational Laplacian of allowed sealed-diamond changes;
rho_D = the zero-sum modular defect source;
S_D   = the whole-diamond RN action, modulo additive constants.
```

This is not a coordinate field equation. It is a Hodge/Poisson equation on the
finite change graph of a sealed diamond.

### 52.1 Finite Hodge/Poisson theorem

Let `C^0(D)` be real functions on finite sealed-diamond states and let
`C^1(D)` be real functions on allowed changes. With a weighted incidence
operator:

```math
d:C^0(D)\to C^1(D),
```

define the relational Laplacian:

```math
L_D=d^\dagger d.
```

For a zero-sum source:

```math
\sum_a \rho_D(a)=0,
```

the field equation is:

```math
L_D S_D=\rho_D,
\qquad
\sum_a S_D(a)=0.
```

Finite theorem:

```text
If the allowed-change graph is connected, then L_D S_D = rho_D has a unique
mean-zero solution for every zero-sum rho_D.
```

Equivalently, `S_D` is the unique minimizer of the record-work functional:

```math
\mathcal E_D(S)
=
{1\over2}\langle dS,dS\rangle
-\langle \rho_D,S\rangle.
```

The Euler equation of this functional is exactly:

```math
d^\dagger dS_D=\rho_D.
```

The finite receipt gives:

```text
residual = 1.4e-16;
lambda_1 = 0.382;
energy margin under a mean-zero perturbation = 0.575.
```

This is the positive result. If `L_D` and `rho_D` are intrinsic, then the
action is unique modulo constants.

### 52.2 Eventless collars

An eventless collar has no modular defect source:

```math
\rho_D=0.
```

On a connected change graph the unique mean-zero solution is:

```math
S_D=0.
```

The finite receipt gives:

```text
||S|| = 0.0e+00.
```

This is the field-equation version of eventless record transport: no source,
no record-work potential, no hidden event.

### 52.3 No-silent seams as exactness, not dynamics

The record-work 1-form is:

```math
J_D=dS_D.
```

For an exact 1-form, every closed record loop has zero work:

```math
\oint J_D=0.
```

The finite cycle receipt gives:

```text
loop residue = 2.8e-17.
```

This is good: the relational equation obeys no-silent-seam consistency. But it
does not derive the source. It only says that once `S_D` is known, its work
form has no hidden loop seam.

### 52.4 The cycle-current attack

A divergence-free cycle current can have the same local source divergence and
still carry hidden loop work. In the audit:

```text
divergence gap = 1.1e-16;
loop shift = 6.000.
```

So local source data alone do not determine the full record-work current
unless no-silent-seam exactness kills the cycle component.

The Hodge language is precise:

```math
J_D=dS_D+J_D^{\rm cyc}.
```

The field equation controls:

```math
d^\dagger J_D=\rho_D.
```

But a cycle component with:

```math
d^\dagger J_D^{\rm cyc}=0
```

is invisible to the source. Branch A therefore requires:

```text
sealed eventless collars derive J_D^{cyc}=0,
```

not merely `d^\dagger J_D=rho_D`.

### 52.5 The source-amplitude attack

Even if the event support is known, the source amplitude can remain free:

```math
\rho_{\alpha,x}
=
\alpha\left(\delta_x-{1\over |D|}\mathbf 1\right).
```

All amplitudes solve a valid relational field equation:

```math
L_D S_{\alpha}=\rho_{\alpha,x}.
```

The finite audit gives:

```text
P span = 0.219.
```

Therefore support-only event information does not derive `S_D`. The amplitude
of `rho_D` must be fixed by the same modular defect law that identifies the
event.

### 52.6 The change-operator attack

Even with the same states and the same source, changing the allowed-change
operator changes the action. The audit compares a path change graph and a
cycle change graph on the same five states:

```text
P span = 0.428.
```

Thus the relation:

```math
L_D S_D=\rho_D
```

is not enough unless `L_D` is intrinsic. The sealed diamond must derive its
allowed changes and their weights. If `L_D` is selected by us, the equation is
branch B.

### 52.7 Refinement receipt and hidden-weight attack

The Feynman receipt is Schur/Kron refinement. If a fine change graph is reduced
to boundary states by the canonical Schur complement:

```math
L_{\rm coarse}
=
L_{TT}-L_{TI}L_{II}^{-1}L_{IT},
```

then the coarse equation reproduces the boundary response of the fine
equation. The finite receipt gives:

```text
boundary error = 0.0e+00.
```

This is a serious positive check: the relational field equation is
refinement-compatible when the reduction map is fixed.

But the hidden-weight attack remains. Different interior weights with the same
boundary source give different boundary responses:

```text
gap span = 0.500.
```

So refinement compatibility does not derive the fine weights. It only gives
the correct descent once the fine change operator is known.

### 52.8 Defect-source origin

There is one non-circular way to close the source term:

```text
rho_D must be the divergence of the intrinsic modular factorization defect.
```

If the sealed diamond supplies the full log defect law, then `rho_D` is fixed.
But if it supplies only the defect support, the amplitude remains free. And if
the full log defect law is just `P_D` in another form, then the construction is
tautological:

```text
given P_D -> S_D -> rho_D.
```

Branch A needs the harder direction:

```text
sealed relational defect -> rho_D -> unique S_D -> P_D.
```

### 52.9 Audit

| target | relational object | positive result | obstruction | diagnostic value | verdict |
|---|---|---|---|---|---|
| relational equation | change Laplacian `L_D` and source `rho_D` | residual `1.4e-16` | `L_D` and `rho_D` must be intrinsic | `L_D S=rho` | THM-POISSON-IF-DATA |
| eventless collar | `rho_D=0` | only constant mean-zero action | trivial but necessary | `||S||=0.0e+00` | PASS-FLAT |
| unique representative | connected change graph | `lambda_1=0.382` | fails on disconnected graphs | energy margin `0.575` | PASS-UNIQUE-MOD-CONST |
| no-silent seam | exact record-work `dS` | closed loop work vanishes | kills cycle current, not source | loop residue `2.8e-17` | PASS-EXACT-WORK |
| cycle-current attack | same divergence/source | div gap `1.1e-16` | hidden loop current changes work | loop shift `6.000` | FAIL-SOURCE-NOT-FULL-CURRENT |
| source amplitude attack | same marked event support | all solve `L S=rho_alpha` | amplitude `alpha` is free | `P` span `0.219` | FAIL-RHO-AMPLITUDE |
| change graph attack | same vertices and source | path and cycle both covariant | `L_D` changes the action | `P` span `0.428` | FAIL-L-DERIVATION |
| refinement receipt | Schur/Kron coarse change law | boundary error `0.0e+00` | works only if reduction map fixed | fine/coarse agree | PASS-IF-SCHUR |
| hidden refinement attack | same boundary source | all have valid reductions | interior weights alter response | gap span `0.500` | FAIL-HIDDEN-WEIGHTS |
| factorization source | modular defect log ratio | `rho` fixed if full defect law supplied | support-only defect leaves amplitude free | conditional | COND-RHO-FROM-DEFECT |
| field equation status | `F_D(S)=L_D S-rho_D` | relational and unique if data intrinsic | not selected by kinematics alone | right form, open origin | OPEN-L-RHO-ORIGIN |

### 52.10 Result

The positive theorem is:

```text
Relational record field equation theorem, finite form.
Given a connected finite sealed-diamond change graph with intrinsic weights
and a zero-sum modular defect source rho_D, the equation

    L_D S_D = rho_D

has a unique mean-zero solution.  The solution is the unique minimizer of
record-work energy.  Eventless collars are exactly the rho_D=0 flat solutions.
```

This is the best current form of the missing equation:

```text
F_D(S_D)=d^\dagger dS_D-\rho_D=0.
```

It is relational. It is non-Markovian-compatible because the states may be
whole-diamond states, not instantaneous Markov states. It has a real uniqueness
theorem. It has a refinement receipt through Schur/Kron reduction.

But the full Branch-A closure is still conditional:

```text
L_D must be derived as the intrinsic allowed-change operator.
rho_D must be derived as the intrinsic modular defect source with fixed
amplitude.
no-silent-seam exactness must remove divergence-free cycle currents.
```

If all three are proved from the sealed physical process, Branch A has a real
field law. If any of the three is supplied, the construction is branch B.

The campaign therefore does not prove Branch A-full. It proves where the proof
must now live:

```text
derive L_D, derive rho_D, prove exactness.
```

## 53. Origin closure for `L_D`, `rho_D`, and exactness [PROBE]

Section 52 found the relational field-equation form:

```math
L_D S_D=\rho_D.
```

It also identified the three objects that must be intrinsic:

```text
1. L_D, the allowed-change operator;
2. rho_D, the modular defect source with fixed amplitude;
3. exactness/no-silent-seam removal of divergence-free cycle currents.
```

The diagnostic is:

```text
code/v6_p3aq_field_equation_origin_closure.py
```

The result is a finite origin no-go:

```text
sealed kinematics and symmetry restrict these objects, but do not select them.
```

### 53.1 Edge-orbit Laplacians

If a sealed diamond has an internal automorphism group, an invariant change
operator can assign weights only by edge orbit. Thus:

```text
edge-orbit symmetry -> weights constant on edge orbits.
```

But unless there is only one edge orbit and the scale is fixed, the weights
remain free. On a reflection-invariant five-state path, the boundary edges and
interior edges form two orbits. The finite audit gives:

```text
P span = 0.164.
```

Even with one edge orbit, the overall scale remains free:

```text
P span = 0.536.
```

A complete-graph attempt gives a canonical graph shape, but it is too broad as
a locality principle and still leaves scale:

```text
P span = 0.082.
```

Therefore symmetry can define an invariant cone of Laplacians. It does not
select a unique `L_D`.

### 53.2 Vertex-orbit sources

The same problem appears for sources. An invariant zero-sum source is constant
on vertex orbits. For a reflection-invariant five-state path the vertex orbits
are:

```text
{0,4}, {1,3}, {2}.
```

The zero-sum invariant source space is therefore two-dimensional. The audit
finds:

```text
P span = 0.214.
```

If the vertex action is transitive, an invariant source is constant, and
zero-sum forces:

```text
rho_D=0.
```

That is eventless:

```text
source dimension = 0.
```

If a marked event is supplied, the source shape:

```math
\rho_x=\delta_x-{1\over |D|}\mathbf 1
```

is natural, but the amplitude is still free:

```text
P span = 0.219.
```

Thus `rho_D` cannot come from support or symmetry alone.

### 53.3 Exactness origin

On a graph with cycles, the cycle rank is:

```math
b_1=|E|-|V|+c.
```

A divergence-free cycle current can change loop work without changing the
local source. The audit gives:

```text
cycle rank = 1;
divergence gap = 0.0e+00;
loop gap = 5.0.
```

So exactness:

```math
J_D=dS_D
```

is not derived from divergence data. It is an additional physical requirement
unless the sealed eventless-collar law proves it.

Tree graphs have no cycle current, but choosing a tree and its weights is not a
dynamics. It removes one ambiguity by narrowing the allowed graph class, while
leaving the origin of the class itself open.

### 53.4 Minimum complexity does not help

One might try:

```text
choose the least complex action.
```

Without a derived source this selects:

```text
S_D=0.
```

The audit records:

```text
||S|| = 0.0.
```

So minimum complexity gives the eventless law unless the event source is
already known. It cannot derive nontrivial events by itself.

### 53.5 Audit

| target | invariant data | positive result | obstruction | value | verdict |
|---|---|---|---|---|---|
| edge-orbit Laplacian | reflection-invariant path | weights constant on edge orbits | orbit weights remain free | `P` span `0.164` | FAIL-L-WEIGHTS |
| one edge orbit | edge-transitive graph | only one weight ratio | overall scale remains free | `P` span `0.536` | FAIL-L-SCALE |
| complete graph attempt | maximal invariant adjacency | canonical graph shape | nonlocal and scale still free | `P` span `0.082` | FAIL-CANONICAL-GRAPH |
| vertex-orbit source | reflection-invariant source | source constant on vertex orbits | orbit amplitudes remain free | `P` span `0.214` | FAIL-RHO-ORBIT |
| transitive source | all vertices indistinguishable | zero-sum invariant source is zero | no nontrivial event | source dim `0` | FAIL-TRIVIAL-RHO |
| marked source | event support supplied | `delta_x-uniform` source shape | amplitude remains free | `P` span `0.219` | FAIL-RHO-AMPLITUDE |
| cycle exactness | graph with cycles | cycle rank `1` | cycle current invisible to divergence | div gap `0.0e+00`, loop gap `5.0` | FAIL-EXACTNESS-ORIGIN |
| tree exactness | cycle-free graph | no harmonic cycle current | tree choice and weights remain free | possible states `16` | COND-NOT-DYNAMICS |
| minimum complexity | minimize `||S||` or work without source | unique zero action | selects eventless law | `||S||=0.0` | FAIL-TRIVIAL |
| full closure packet | intrinsic `L_D`, `rho_D`, exactness | then `S_D` is unique | packet is exactly missing dynamics | conditional theorem | THM-CLOSED-IF-PACKET |
| origin no-go | sealed kinematics alone | restricts to invariant cones | does not select point in cones | families survive | THM-ORIGIN-NO-GO |

### 53.6 Result

The finite no-go is:

```text
L/rho/exactness origin no-go.
Sealed finite-diamond kinematics and internal symmetry restrict L_D to an
edge-orbit invariant cone, rho_D to a vertex-orbit invariant zero-sum space,
and cycle currents to a harmonic sector.  They do not select the edge weights,
source amplitudes, or exactness condition.
```

The positive conditional theorem is:

```text
If the sealed physical process derives the complete packet

    (L_D, rho_D, exactness),

then the relational field equation uniquely determines S_D modulo constants.
```

Therefore the full Branch-A law is now equivalent to deriving that packet.
The open problem is no longer diffuse:

```text
derive the intrinsic allowed-change operator;
derive the intrinsic defect source and its amplitude;
derive no-silent-seam exactness.
```

If any of these are selected by hand, the construction is branch B.

## 54. Intrinsic score-geometry campaign [PROBE]

Sections 52-53 show that the relational field equation:

```math
L_D S_D=\rho_D
```

is the right form, but that `L_D`, `rho_D`, and exactness must be derived. The
most promising route is to derive all three from one deeper object:

```text
the intrinsic score geometry of the sealed diamond.
```

The diagnostic is:

```text
code/v6_p3ar_score_geometry_campaign.py
```

The guiding idea is:

```text
allowed changes = internally distinguishable infinitesimal record-law changes.
```

If the sealed process supplies a positive local law `P_\theta` and intrinsic
parameters `theta_i`, the score directions are:

```math
u_i
=
{\partial\over\partial\theta_i}\log P_\theta.
```

Then the missing packet is:

```math
L_{ij}
=
\mathbb E_P[u_i u_j],
\qquad
\rho_i
=
\mathbb E_P[\Delta u_i],
```

where:

```math
\Delta
=
\log {P_D\over P_LP_R}
```

is the modular factorization defect. The equation:

```math
L s=\rho
```

is exactly the normal equation for the Fisher projection of the defect onto
the score span. The action is:

```math
S_D^{\rm score}
=
\sum_i s_i u_i.
```

### 54.1 Positive finite theorem

In the two-bit bridge model:

```math
P_\theta(x,z)
\propto
\exp(\theta xz),
```

the bridge score is:

```math
u=xz-\mathbb E[xz].
```

The modular defect:

```math
\Delta=\log {P(x,z)\over P(x)P(z)}
```

lies in the score span. The finite audit recovers:

```text
pair coefficient = 0.900;
projection error = 5.1e-17.
```

So the score geometry fixes both `L_D` and `rho_D` once the score direction and
log defect are intrinsic. The amplitude is not free: it is the log-RN defect.

### 54.2 Basis covariance

The construction depends on the score span, not on a coordinate basis. Rescale
the bridge score:

```math
u\mapsto 2u.
```

The coefficient changes, but the projected action does not. The audit gives:

```text
projected-action gap = 0.0e+00.
```

This is good: the score-geometry equation is internally coordinate-covariant.

### 54.3 Missing bridge score attack

If the score space contains only single-site directions:

```math
u_x=x-\mathbb E[x],
\qquad
u_z=z-\mathbb E[z],
```

the same bridge defect is invisible. The formal Gram exists, but the projection
misses the event:

```text
projection error = 0.628.
```

Thus score geometry closes Branch A only if the sealed process derives the
right score space. A detector-chosen or analyst-chosen score space is branch B.

### 54.4 Supplied score-family attack

In a three-bit diamond with pair and triple whole-diamond components, adding a
triple score direction by hand improves the projection:

```text
error 0.353 -> 0.168;
projected-action gap = 0.487.
```

That is a useful receipt and a serious warning. The score geometry is not a
selector if score directions are added after seeing the defect. The score
manifold itself must be intrinsic.

### 54.5 Exactness

Score-generated work is exact because it is generated by one log-likelihood
potential. For a closed parameter loop, the action returns to itself:

```text
loop residue = 0.0e+00.
```

An artificial work form with nonzero curl gives:

```text
loop residue = 1.0.
```

So no-silent-seam exactness follows from integrable score geometry, but not
from arbitrary local currents.

### 54.6 Refinement receipt

Under coarse-graining, scores descend by conditional expectation. Fisher
information decreases:

```text
information loss = 0.712.
```

This is the score-geometry version of refinement stability: hidden score
directions can be integrated out, but the loss is real. If the hidden scores
were physical, dropping them changes `L_D`.

### 54.7 Audit

| target | score object | positive result | obstruction | value | verdict |
|---|---|---|---|---|---|
| score Gram derives `L` | `u_i=d log P/d theta_i` | Fisher `L_ij=<u_i,u_j>` | score space must be intrinsic | pair coeff `0.900` | PASS-IF-SCORES |
| defect projection derives `rho` | `Delta=log P/(P_L P_R)` | `rho_i=<Delta,u_i>` | requires full log defect, not support | projection err `5.1e-17` | PASS-FIXED-AMPLITUDE |
| basis covariance | same score span, rescaled basis | projected action invariant | only span matters | gap `0.0e+00` | PASS-GAUGE-SPAN |
| missing bridge score | single-site scores only | formal Gram exists | bridge defect invisible | projection err `0.628` | FAIL-INCOMPLETE-SCORES |
| supplied score family | add triple score by hand | projection improves | chosen score space changes `S` | err `0.353->0.168`, gap `0.487` | FAIL-SCORE-SELECTION |
| defect amplitude | full RN/KL `Delta` | amplitude fixed by log ratio | support-only scaling remains free | scaled span `0.525` | COND-LOG-DEFECT-NEEDED |
| exactness | integrable score potential | closed parameter-loop action vanishes | non-score currents can have curl | loop `0.0e+00` | PASS-EXACT-SCORES |
| nonintegrable current attack | artificial work form | local components can be assigned | curl creates silent seam | loop `1.0` | FAIL-NONINTEGRABLE |
| refinement score receipt | conditional expectation of scores | Fisher information decreases | hidden scores change `L` if retained | info loss `0.712` | PASS-MONOTONE |
| support-only source attack | same bridge support | all have same event support | theta/log amplitude changes law | `P` span `0.614` | FAIL-SUPPORT-ONLY |
| score-geometry theorem | intrinsic score manifold + log defect | derives `L,rho,exactness` | conditional on intrinsic manifold | one packet | THM-CONDITIONAL-SCORE-GEOMETRY |
| closure status | sealed kinematics alone | not enough to pick score manifold | score-origin theorem missing | A-full open | OPEN-SCORE-ORIGIN |

### 54.8 Result

The conditional theorem is:

```text
Score-geometry closure theorem.
If the sealed physical process intrinsically supplies the score manifold of
internally distinguishable record-law changes and the full modular log defect,
then:

1. L_D is the Fisher/response Gram of those scores;
2. rho_D is the projection of the modular log defect onto those scores;
3. no-silent-seam exactness follows from score integrability.
```

This is the strongest current closure route. It derives the whole packet:

```text
(L_D, rho_D, exactness)
```

from one object. But it is conditional. The next question is whether the score
manifold itself can be derived without choosing features.

## 55. Conditional score-space origin campaign [PROBE]

The previous section still allowed a score-family choice. There is a more
canonical construction:

```text
allowed scores = all infinitesimal log-law changes that preserve the sealed
collar.
```

The diagnostic is:

```text
code/v6_p3as_conditional_score_origin.py
```

Assume the sealed diamond supplies:

```text
P_D = a positive finite record law;
C_D = the intrinsic collar/boundary sigma-algebra.
```

Then the canonical score space is:

```math
T_{C_D}
=
\{u:\mathbb E_P[u\mid C_D]=0\}.
```

These are exactly the infinitesimal log-law changes that preserve the collar
marginals.

### 55.1 Conditional exponential tilting

For `u in T_C`, define:

```math
P_t(a)
=
{P(a)e^{t u(a)}
\over
\mathbb E_P[e^{t u}\mid C](c(a))}.
```

This preserves the collar marginal exactly. The finite receipt gives:

```text
collar marginal gap = 0.0e+00.
```

The conditional score basis also has:

```text
dimension = 4;
max conditional mean = 1.2e-16.
```

So if `P_D` and `C_D` are intrinsic, the score space is intrinsic too.

### 55.2 Source projection and boundary nulls

Projecting a defect onto `T_C` gives a canonical internal source. Boundary-only
defects vanish under this projection:

```text
||projection|| = 1.2e-16.
```

That is the right behavior: if a term is measurable on the fixed collar, it is
not an internal event-producing change relative to that collar.

The internal defect projection is canonical but may have residual:

```text
projection residual = 0.507.
```

The residual is the component of the defect outside the collar-preserving
tangent space.

### 55.3 Collar choice attack

Different collar sigma-algebras give different canonical score spaces. The
finite audit compares two collar choices and finds:

```text
projection gap = 0.666.
```

Therefore the collar cannot be selected by the analyst. Branch A requires the
sealed diamond to derive `C_D`.

### 55.4 Over-broad and over-fine attacks

If the collar partition is trivial, the score space is the full mean-zero
simplex tangent space. It projects any finite defect:

```text
error = 3.9e-16.
```

That is too permissive and nearly tautological.

If the collar partition is singleton-fine, there are no allowed internal
variations:

```text
error = 0.813.
```

That kills events. The right collar is neither arbitrary nor maximal nor
minimal. It must be the intrinsic sealed separator.

### 55.5 Base-law dependence

With the same support and the same collar, changing the base law changes the
Fisher geometry and projection:

```text
projection gap = 1.256.
```

So the score-space theorem also requires the actual positive record law `P_D`.
If `P_D` is supplied phenomenologically, the construction is not Branch A.

### 55.6 Exactness

Conditional score tilts are score-generated, so closed score loops return:

```text
finite score loop = 0.000.
```

The infinitesimal loop receipt is also stable:

```text
4.86e-17 -> 4.16e-17.
```

This is the exactness origin: no-silent-seam follows from a genuine conditional
score manifold.

### 55.7 Audit

| target | intrinsic object | positive result | obstruction | value | verdict |
|---|---|---|---|---|---|
| canonical score space | `T_C={u:E[u|C]=0}` | basis dimension derived | requires intrinsic collar `C` | dim `4`, cond `1.2e-16` | PASS-IF-COLLAR |
| collar-preserving tilt | conditional exponential family | collar marginal preserved exactly | requires positive `P` | gap `0.0e+00` | PASS-TILT |
| source projection | project defect onto `T_C` | canonical projection exists | residual if defect has boundary part | residual `0.507` | PASS-CONDITIONAL-RHO |
| boundary-only defect | defect measurable on `C` | projection vanishes | right if collar is fixed | `||proj||=1.2e-16` | PASS-BOUNDARY-NULL |
| partition choice attack | different collar sigma-algebra | each score space canonical | projections differ | gap `0.666` | FAIL-COLLAR-CHOICE |
| over-broad score space | trivial collar partition | full mean-zero projection | too permissive/tautological | err `3.9e-16` | FAIL-FULL-SIMPLEX |
| over-fine score space | singleton collar partition | no allowed variation | kills events | err `0.813` | FAIL-SINGLETON |
| base-law dependence | same support and collar | both score spaces canonical | Fisher/projection changes with `P` | gap `1.256` | FAIL-P-SUPPLIED |
| infinitesimal exactness | score manifold connection | small loop curvature shrinks | finite frozen-score loops need connection | `4.86e-17->4.16e-17` | PASS-INFINITESIMAL |
| finite score loop | frozen score directions | closed score loop returns | only for score-generated tilts | loop `0.000` | PASS-FINITE-EXACT |
| conditional score theorem | positive `P` plus intrinsic `C` | derives score space, `L,rho,exactness` | conditional on `P` and `C` | one packet | THM-CONDITIONAL-SCORE-ORIGIN |
| origin status | sealed kinematics alone | does not derive `P` or `C` | Branch A still needs `P/C` theorem | open | OPEN-P-C-ORIGIN |

### 55.8 Result

The positive theorem is:

```text
Conditional score-space theorem.
Given a positive sealed record law P_D and an intrinsic collar sigma-algebra
C_D, the canonical allowed score space is

    T_C = {u : E_P[u | C_D] = 0}.

Conditional exponential tilting preserves the collar exactly.  The Fisher Gram
on T_C derives L_D.  Projection of the modular defect onto T_C derives rho_D.
Score integrability derives exactness.
```

This is the best current answer to how all three missing objects could come
from one invariant.

But the theorem is conditional on two inputs:

```text
P_D, the actual sealed record law;
C_D, the intrinsic collar/boundary sigma-algebra.
```

So the Branch-A target has moved one level down, and this time the movement is
mathematically controlled:

```text
derive P_D and C_D from the sealed physical process.
```

If `P_D` and `C_D` are derived, the score-geometry route closes the relational
field equation. If either is supplied, the construction remains branch B.

## 56. `P_D` and `C_D` origin campaign [PROBE]

Section 55 reduces score-geometry closure to two objects:

```text
P_D = the actual positive sealed record law;
C_D = the intrinsic collar/boundary sigma-algebra.
```

The diagnostic is:

```text
code/v6_p3at_pc_origin_campaign.py
```

The campaign asks whether these can be found from sealed relational facts.

### 56.1 Exact Markov-blanket collar

Given a positive law `P_D`, the best intrinsic collar criterion is:

```math
I(L;R\mid C_D)=0.
```

That is: the collar is the internal record sigma-algebra that screens the left
and right sides in eventless transport.

In a finite chain:

```math
P(x,y,z)\propto \exp(J_Lxy+J_Ryz),
```

the middle variable screens the sides. The finite receipt gives:

```text
I(L;R) = 0.079;
I(L;R | C) = -5.9e-18;
minimal exact candidates = 1.
```

So when there is a unique exact minimal Markov blanket, `C_D` is derived from
`P_D`.

### 56.2 Why this does not derive `P_D`

The same collar can support many different laws. Holding the middle collar
structure fixed and changing couplings gives:

```text
P span = 0.639.
```

Full positive support also does not determine the law:

```text
P span = 0.853.
```

And left/right symmetry does not determine the coupling:

```text
P span = 1.077.
```

Thus `P_D` is not derived from support, symmetry, or separator structure.

### 56.3 Approximate and nonunique collars

Approximate collars require thresholds:

```text
loose threshold candidates = 2;
strict threshold candidates = 1.
```

So approximate conditional independence is not canonical unless the tolerance
is itself derived.

Minimal separators can also be nonunique. In the graph:

```text
L-A-C-R
L-B-C-R
```

there are two inclusion-minimal separators:

```text
{C} and {A,B}.
```

So uniqueness of `C_D` is a theorem target, not automatic.

### 56.4 Cofinal identification is not derivation

Cofinal record counts can identify a supplied process law:

```text
L1 error 0.022 -> 0.000
```

as sample size grows in the finite proxy. This is useful Feynman discipline:
the law is measurable in records. But it is not a derivation of the process
law. It tells us how to estimate `P_D` once nature supplies it.

### 56.5 Audit

| target | relational test | positive result | obstruction | value | verdict |
|---|---|---|---|---|---|
| exact collar criterion | `I(left;right|C)=0` | chain middle screens sides | requires exact positive `P` | `I0=0.079`, `IC=-5.9e-18` | PASS-MARKOV-BLANKET |
| unique minimal collar | minimal exact separator | one candidate in chain | not generic | candidates `1` | PASS-IN-CHAIN |
| same collar different law | same Markov blanket | `C` remains middle variable | couplings remain free | `P` span `0.639` | FAIL-P-FREE |
| same support attack | full positive support | support unchanged | law changes substantially | `P` span `0.853` | FAIL-SUPPORT |
| symmetry attack | left/right symmetric chain | symmetry preserved | coupling still free | `P` span `1.077` | FAIL-SYMMETRY |
| approximate collar | thresholded CMI | loose thresholds find candidates | threshold changes answer | loose `2`, strict `1` | FAIL-THRESHOLD |
| separator nonuniqueness | graph minimal separators | separators exist | minimal separator need not be unique | `2: {C} and {A,B}` | FAIL-C-UNIQUENESS |
| cofinal frequencies | empirical record counts | `P` can be identified from process | identification is not derivation | L1 `0.022->0.000` | IDENT-P-NOT-DERIVE |
| `P/C` closure theorem | actual `P` plus unique exact `C` | conditional score geometry closes | conditional on process law | one route | THM-CONDITIONAL-PC |
| origin status | sealed kinematics alone | cannot derive `P`; `C` can fail uniqueness | needs physical process law | A-full open | OPEN-PROCESS-LAW |

### 56.6 Result

The conditional theorem is:

```text
P/C closure theorem.
If the sealed physical process supplies the actual positive record law P_D and
P_D has a unique exact minimal Markov-blanket collar C_D, then C_D is intrinsic
and the conditional score-geometry theorem derives the packet

    (score space, L_D, rho_D, exactness).
```

The finite no-go is:

```text
P-origin no-go.
Support, symmetry, separator structure, and cofinal identifiability do not
derive P_D.  They can identify or restrict an already supplied process law, but
they do not select the law.
```

Therefore the final Branch-A pressure point is:

```text
derive the physical process law P_D itself, and prove unique exact collar
existence for the relevant sealed diamonds.
```

This is not a defect of the score-geometry route. It is the place where any
candidate Branch-A theory must finally become dynamics.

## 57. Invariant physical principle for `P_D` [PROBE]

Section 56 leaves one question:

```text
Find the invariant physical principle that fixes the positive sealed record
law P_D.
```

The diagnostic is:

```text
code/v6_p3au_pd_principle_campaign.py
```

The finite answer is negative for the tested class of principles:

```text
invariance, optimization, locality, detailed balance, refinement, criticality,
and empirical identification do not derive a nontrivial P_D without supplied
dynamical data.
```

The pattern is simple:

```text
No nontrivial constraint -> uniform/eventless law.
Nontrivial law -> moment/action/coupling/source/rate/duality/code/process was
already supplied.
```

### 57.1 Maximum entropy

Unconstrained maximum entropy selects the uniform law:

```text
H = 2.079
```

on the three-bit finite diamond. This is unique, invariant, and eventless.

If a moment constraint is added:

```math
\mathbb E[xz]=c,
```

maximum entropy selects:

```math
P_\theta(x,z)\propto e^{\theta xz}.
```

But the correlation `c` is supplied. The audit scans three moment constraints:

```text
theta 0.203 -> 1.472;
P span = 0.700.
```

So maximum entropy is a correct inference rule after constraints, not a source
of the physical process law.

### 57.2 Locality, Markov blankets, and symmetry

Locality/Markov structure gives a factorization:

```math
P(x,y,z)
\propto
\exp(J_Lxy+J_Ryz).
```

It fixes the graph of dependence but not the couplings:

```text
P span = 0.668.
```

Internal symmetry reduces parameters but does not set them:

```text
P span = 1.128.
```

Thus locality and symmetry define families of laws, not the member of the
family.

### 57.3 Detailed balance and refinement fixed points

Detailed balance is also not a selector. For many positive stationary laws,
one can build reversible transition rates. The audit varies the stationary
law/action and finds:

```text
P span = 0.749.
```

Detailed balance reads a supplied stationary law. It does not derive it.

A simple refinement fixed-point test has the same problem in a different form.
For 1D decimation:

```math
\theta'
=
\operatorname{atanh}(\tanh^2\theta),
```

the uniform fixed point is exact, while finite nontrivial fixed points are not
selected:

```text
residuals = 0.0e+00 / 0.337 / 0.347.
```

Refinement fixed points can be powerful only after a real refinement map and
action family are supplied.

### 57.4 Self-duality, maximum caliber, least action, and coding

Self-duality can select a point in a chosen model:

```math
\sinh(2K)=1,
\qquad
K_c=0.4407.
```

But the graph, duality map, and action family are inputs.

Maximum caliber gives a path law, but a nontrivial path law requires a supplied
transition statistic. The finite two-state path audit gives:

```text
unconstrained q = 0.5;
P span = 1.440 when transition constraints vary.
```

Least record action gives the zero/eventless law unless a source or
correlation is supplied:

```text
P span = 0.600 across supplied source/correlation targets.
```

Algorithmic simplicity chooses the uniform law or a grid-minimal nonzero law,
but the code/grid is not invariant:

```text
grid span = 0.090.
```

### 57.5 Gibbs variational and empirical identification

The Gibbs variational principle:

```math
P\propto e^{-A}
```

is exact once an action `A` is supplied. The audit gives:

```text
P span = 0.688
```

across supplied actions. This is not a derivation of `P_D`; it is section 50
again in variational language.

Cofinal frequencies can identify a process law:

```text
L1 error 0.018 -> 0.000.
```

That is operationally important, but identification is not derivation.

### 57.6 Audit

| target | principle | positive result | obstruction | value | verdict |
|---|---|---|---|---|---|
| maximum entropy | maximize `H(P)` | unique law without constraints | uniform/eventless | `H=2.079` | FAIL-TRIVIAL |
| max entropy with moment | fix `E[xz]` | unique exponential law | moment/correlation supplied | theta `0.203->1.472`, span `0.700` | COND-MOMENT |
| local Markov blanket | `P` factorizes over cliques | collar/locality structure fixed | clique couplings free | `P` span `0.668` | FAIL-COUPLINGS |
| internal symmetry | left/right and flip symmetries | reduces parameters | symmetric coupling remains free | `P` span `1.128` | FAIL-SYMMETRY |
| detailed balance | reversible sealed transport | consistent rates exist | stationary law/action supplied | `P` span `0.749` | FAIL-READS-PI |
| RG/refinement fixed point | 1D decimation `theta'=atanh(tanh^2 theta)` | uniform fixed point exact | finite nontrivial fixed point absent | res `0.0e+00/0.337/0.347` | FAIL-TRIVIAL-RG |
| self-duality | `sinh(2K)=1` | selects `K` in chosen model | duality/action family supplied | `Kc=0.4407` | COND-FAMILY |
| maximum caliber | maximize path entropy | uniform `q` if unconstrained | flip count/current supplied | `q0=0.5`, span `1.440` | COND-PATH-CONSTRAINT |
| least record action | minimize work norm | zero law without source | nonzero source/correlation supplied | `P` span `0.600` | COND-SOURCE |
| algorithmic simplicity | shortest code / smallest coupling | uniform or grid-minimal law | code/grid not invariant | grid span `0.090` | FAIL-CODE |
| Gibbs variational | minimize `E[A]-H` | unique `P` for supplied `A` | `A` is the process law in disguise | `P` span `0.688` | PASS-IF-A-SUPPLIED |
| cofinal frequencies | record-count convergence | identifies actual `P` | identification not derivation | L1 `0.018->0.000` | IDENT-NOT-DERIVE |
| score geometry | derive packet from `P,C` | closes downstream machinery | requires `P_D` first | `P_D input` | DOWNSTREAM |
| principle no-go | invariance/optimization only | restricts or identifies `P` | does not select nontrivial `P_D` | families survive | THM-P-PRINCIPLE-NO-GO |

### 57.7 Result

The finite no-go is:

```text
P-principle no-go, finite tested form.
The audited invariant principles either select the uniform/eventless law or
select a nontrivial law only after a moment, action, coupling, transition
statistic, source, duality map, code, or empirical process has been supplied.
```

Therefore:

```text
P_D is not downstream of score geometry, Markov blankets, cocycles,
refinement consistency, or generic optimization.
P_D is the dynamical law itself.
```

This is the end of the reduction chain. To continue Branch A, one must state a
physical process principle that directly generates `P_D`.

## 58. Boundary of a genuine process-law principle [PROBE]

Section 57 says what fails. The next question is what would count as success.

The diagnostic is:

```text
code/v6_p3av_process_law_boundary_campaign.py
```

A genuine Branch-A process-law principle must be a complete finite generative
law:

```text
D |-> P_D
```

for every sealed finite diamond `D`, satisfying:

```text
1. generativity: outputs P_D, not a family;
2. projectivity: commutes with refinement/marginalization;
3. positivity: gives finite RN actions;
4. nontriviality: produces modular defects/events;
5. unique collar: gives exact minimal C_D where needed;
6. no free coefficients: all numerical constants are derived by the rule.
```

### 58.1 Why each clause is needed

Projective consistency alone is not enough. Independent-spin toy laws commute
with marginalization exactly:

```text
projective error = 0.0e+00.
```

But the projective family still varies:

```text
span = 1.098.
```

Positivity gives finite RN actions, but near-degenerate positive limits remain:

```text
span = 0.238.
```

Nontrivial defects allow events, but the defect amplitude remains free:

```text
span = 0.594.
```

Unique collars feed score geometry, but do not set couplings:

```text
span = 0.382.
```

The no-free-coefficient clause is therefore decisive.

### 58.2 The trivial complete law

There is a complete formal law:

```text
P_D = uniform for every D.
```

It is generative, positive, projective, and coefficient-free. But it is empty:

```text
no events;
no sources;
no beta;
no branch-A physics.
```

So the law must be nontrivial, not merely complete.

### 58.3 Empirical law is not a principle

One can fit `P_D` from records. This is operationally good, but the fitted
correlations are supplied by nature:

```text
span = 0.600
```

across supplied empirical correlations. This is measurement, not derivation.

### 58.4 Audit

| target | required clause | positive result | failure if absent | value | verdict |
|---|---|---|---|---|---|
| generative law | outputs `P_D` for every sealed `D` | well-defined process object | otherwise `P_D` is input | binary yes/no | REQ-GENERATIVE |
| projective consistency | marginals match refinements | toy error `0.0e+00` | consistent families still vary | span `1.098` | REQ-PROJECTIVE-NOT-ENOUGH |
| positivity | `P_D(a)>0` | RN actions finite | near-degenerate limits still allowed | span `0.238` | REQ-POSITIVE-NOT-ENOUGH |
| nontrivial defect | modular factorization fails | events possible | defect amplitude remains free | span `0.594` | REQ-DEFECT-NOT-ENOUGH |
| unique collar | exact minimal Markov blanket | feeds score geometry | does not set couplings | span `0.382` | REQ-COLLAR-NOT-ENOUGH |
| no free coefficients | all numbers derived by rule | would close Branch A | missing in tested candidates | decisive | REQ-NO-FREE-COEFF |
| trivial complete rule | uniform `P_D` for all `D` | closes formally | no events/sources/beta | eventless | FAIL-CLOSES-EMPTY |
| empirical process rule | fit `P_D` from records | identifies law operationally | correlations supplied by nature | span `0.600` | IDENT-NOT-PRINCIPLE |
| Branch-A law target | generative+projective+positive+nontrivial+unique collar+no coeffs | would fix `P_D` | not found in finite campaign | the final theorem | OPEN-UNIQUE-PROCESS-LAW |

### 58.5 Result

The theorem target is now exact:

```text
Unique nontrivial process-law theorem.
There exists a sealed finite-diamond process rule D |-> P_D that is
generative, projective, positive, nontrivial, unique-collar, and has no free
coefficients.  This rule fixes P_D for every sealed diamond.
```

This theorem has not been proved. The finite campaign shows why weaker
principles fail.

So the honest final status of Branch A-full is:

```text
Branch A-full is equivalent to the unique nontrivial process-law theorem.
Branch B is the honest status if the process law, action, coupling, source,
moment, transition statistic, duality map, or code is supplied.
```

## 59. `P_D` contradiction campaign [PROBE]

Section 58 gives the theorem target. Einstein's sharper follow-up is:

```text
What physical impossibility occurs if two different positive laws are allowed
on the same sealed diamond?
```

The diagnostic is:

```text
code/v6_p3aw_pd_contradiction_campaign.py
```

The finite answer is:

```text
No contradiction follows from sealed skeleton data alone.
```

Different positive laws can be coherent, projective, reversible, share the
same collar, and agree on low-order records while disagreeing on joint
probabilities and downstream receipts.

### 59.1 Coherent alternatives

On the same finite atom set, two positive normalized laws are both coherent:

```text
support same = True.
```

Probability theory does not forbid alternatives. It forbids assigning two
different probabilities to the same event under the same objective law. That
last phrase is the issue.

### 59.2 Same low-order records

Two bridge laws:

```math
P_\theta(x,z)\propto e^{\theta xz}
```

with different `theta` have the same one-site marginals:

```text
marginal gap = 0.0e+00.
```

but different joint laws:

```text
P span = 0.509.
```

So finite first-order record receipts do not force `P_D`.

### 59.3 Same exact collar

Two chain laws:

```math
P(x,y,z)\propto e^{J_Lxy+J_Ryz}
```

with different couplings have the same exact Markov blanket `C={y}`:

```text
I(L;R|C)=4.4e-17.
```

but different laws:

```text
P span = 0.450.
```

Thus a unique collar can be shared by many laws.

### 59.4 Same projective form and detailed balance

Projective Bernoulli field families commute with refinement:

```text
projective error = 1.4e-16.
```

while varying:

```text
P span = 0.729.
```

Detailed balance also allows many stationary laws:

```text
P span = 0.564.
```

Both principles are consistency laws, not uniqueness laws.

### 59.5 Predictive and empirical forks

Different `P_D` laws produce different downstream objects:

```text
Fisher gap = 0.556;
RN gap = 0.326.
```

They are also empirically distinguishable in cofinal records:

```text
KL = 0.235 / 0.173.
```

But distinguishable alternatives are not contradictions. They are different
physical predictions. That is exactly why Branch B is meaningful.

### 59.6 Where contradiction actually appears

If all atomic probabilities are equal, the laws are identical:

```text
L1 = 0.0e+00.
```

That is tautological completeness: a full probability law is complete as a
probability law.

If one asserts:

```text
P(A)=p
P(A)=q
```

for the same event `A` in the same objective law, then there is a contradiction:

```text
|p-q| = 0.127.
```

But this contradiction requires the identity principle:

```text
the same sealed physical diamond includes the full objective law P_D.
```

With that principle, two different `P_D` are not two laws for one object. They
are two different physical diamonds, or two branch-B parameter choices.

### 59.7 Audit

| target | same data | positive result | obstruction | value | verdict |
|---|---|---|---|---|---|
| probability coherence | same finite atom set | both laws normalized and positive | coherence permits alternatives | support same `True` | NO-CONTRADICTION |
| same low-order records | same one-site marginals | local receipts agree | joint bridge differs | marg gap `0.0e+00`, `P` span `0.509` | FAIL-LOW-ORDER |
| same exact collar | same Markov blanket `C` | `I(L;R|C)=0` for both | couplings differ | CMI `4.4e-17`, `P` span `0.450` | FAIL-COLLAR |
| same projective rule form | Bernoulli field family | refinement exact for both | field parameter differs | proj err `1.4e-16`, span `0.729` | FAIL-PROJECTIVE |
| detailed balance | reversible transport possible | both can be stationary laws | rates/action differ | `P` span `0.564` | FAIL-DB |
| downstream machinery | same skeleton, different `P` | score/Fisher/RN all computable | outputs differ, no contradiction | Fisher gap `0.556`, RN gap `0.326` | PREDICTIVE-FORK |
| empirical records | cofinal sampling | laws distinguishable in limit | distinguishable is not impossible | KL `0.235/0.173` | EMPIRICAL-FORK |
| complete probabilities | all atomic probabilities same | then laws identical | tautological completeness | L1 `0.0e+00` | PASS-TAUTOLOGY |
| simultaneous assignment | same event same objective law | `P(A)=p` and `P(A)=q` conflicts | requires law-identity axiom | `|p-q|=0.127` | PASS-IF-P-IDENTITY |
| Leibniz record identity | same physical diamond includes `P_D` | two `P_D` become two objects | identity principle is added | not kinematic theorem | COND-IDENTITY-AXIOM |
| contradiction no-go | same skeleton without `P_D` | families remain admissible | no impossibility found | KL example `0.235/0.263` | THM-NO-CONTRADICTION |

### 59.8 Result

The finite no-go is:

```text
P-contradiction no-go.
Allowing two different positive laws on the same sealed skeleton creates a
predictive fork, not a logical or kinematic contradiction.  The laws can share
support, low-order records, exact collars, projective consistency, detailed
balance, and positivity while differing in joint probabilities and downstream
receipts.
```

The positive identity statement is:

```text
Complete sealed-record identity.
If the same sealed physical diamond is defined to include the full objective
law P_D, then two different laws are two different physical objects.  A
simultaneous assignment of two probabilities to the same event in the same law
is contradictory.
```

This is an ontology principle, not a derivation from sealed kinematics. It is
Einstein-clean but not free:

```text
Branch A may adopt complete sealed-record identity.
Branch A-full still needs a unique nontrivial process-law theorem to derive
which P_D obtains.
Branch B remains the honest status if one chooses among admissible P_D laws by
parameter, source, action, or empirical fit.
```

## 60. Unique nontrivial process-law no-go [PROBE]

Section 59 showed that multiple laws on the same skeleton create a predictive
fork, not a contradiction. The remaining question is no longer:

```text
Which nice principle might select P_D?
```

It is:

```text
Can the current sealed-diamond ontology derive a unique nontrivial
generative rule D |-> P_D?
```

The diagnostic is:

```text
code/v6_p3ax_unique_process_law_no_go.py
```

The answer is:

```text
No.
```

This is now a finite no-go theorem for the current ontology, not merely an
open target.

### 60.1 The exchangeable hidden-record family

For every finite size `n` and every parameter:

```math
\theta\in(0,1),
```

define:

```math
P_\theta(x_1,\ldots,x_n)
=
{1\over2}
\prod_i {1+\theta x_i\over2}
+
{1\over2}
\prod_i {1-\theta x_i\over2}.
```

This is a sealed whole-diamond record law with a hidden orientation averaged
out. It is:

```text
positive;
permutation invariant;
projective under deleting records;
nontrivially correlated for theta != 0.
```

The finite audit gives:

```text
family span = 1.319;
permutation invariance error = 0.0e+00;
projectivity error = 0.0e+00;
minimum probability at theta=0.9 is 1.128e-03;
mutual information at theta=0.7 is 0.125.
```

Thus the current structural requirements admit a continuum of nontrivial
positive process laws.

### 60.2 Same local receipts, different law

Different `theta` values have the same one-site means and the same projective
consistency:

```text
one-site gap = 0.0e+00;
projective error = 0.0e+00.
```

but different joint laws:

```text
P span = 0.925.
```

So local receipts and projectivity do not fix `P_D`.

### 60.3 Convex closure no-go

Let `U_D` be the uniform projective law. If a nontrivial projective law `P_D`
is admitted, then for:

```math
\lambda\in[0,1)
```

the mixture:

```math
P_D^{(\lambda)}
=
(1-\lambda)P_D+\lambda U_D
```

is also:

```text
positive;
projective;
covariant whenever P_D is covariant;
nontrivial for lambda < 1.
```

The finite receipt gives:

```text
mixture projective error = 0.0e+00;
mixture span = 0.850.
```

Therefore any admitted nontrivial law generates a continuum of admitted
nontrivial laws unless the ontology includes an additional selector forbidding
the mixture. The current ontology does not include such a selector.

### 60.4 Orbit-simplex no-go

For any finite skeleton with automorphism group `G_D`, a covariant law is
constant on automorphism orbits. Therefore the covariant law space is a
simplex over orbit weights. If there are `m` orbits, the dimension is:

```math
m-1.
```

The audit records:

```text
dimension = 2 for 3 orbits.
```

If `m=1`, the law is uniform and eventless. If `m>1`, there is a family.
Again:

```text
unique -> trivial;
nontrivial -> not unique.
```

### 60.5 Empirical fork

Different `theta` values are empirically distinguishable:

```text
KL = 0.597 / 0.558.
```

But empirical distinguishability is not a contradiction. It means the laws are
different predictions. That is a branch choice, not a derivation.

### 60.6 Audit

| target | test | result | obstruction | value | verdict |
|---|---|---|---|---|---|
| explicit law family | exchangeable hidden-record `P_theta` | positive laws for all `theta in (0,1)` | `theta` not selected | span `1.319` | FAMILY |
| covariance | permutation invariance | all `P_theta` invariant | covariance does not fix `theta` | err `0.0e+00` | FAIL-UNIQUENESS |
| projectivity | delete one record | marginals match smaller diamonds | projectivity does not fix `theta` | err `0.0e+00` | FAIL-UNIQUENESS |
| positivity | full support | RN action finite | positive interval remains | min `P=1.128e-03` | FAIL-UNIQUENESS |
| nontriviality | pair modular dependence | MI positive for `theta != 0` | defect amplitude `theta^2` free | MI `0.125` | FAIL-UNIQUENESS |
| same local receipts | one-site means and projectivity | receipts agree | joint law differs | one gap `0.0e+00`, proj `0.0e+00`, span `0.925` | FAIL-RECEIPTS |
| convex closure | mix `P_theta` with uniform law | positive/projective family persists | continuum from any nontrivial law | proj `0.0e+00`, span `0.850` | THM-MIXING-NO-GO |
| orbit simplex | laws constant on automorphism orbits | dimension is `orbit_count-1` | nontransitive skeletons give families | dim `2` for 3 orbits | THM-ORBIT-NO-GO |
| uniform rule | `theta=0` | unique if maximal symmetry imposed | eventless/trivial | corr `0.0e+00` | FAIL-TRIVIAL |
| empirical fork | cofinal records | theta values distinguishable | distinguishable is not impossible | KL `0.597/0.558` | PREDICTIVE-FORK |
| current ontology verdict | sealed skeleton + structural axioms | admits nontrivial law families | no unique nontrivial derivation possible | proved by family | THM-UNIQUE-P-LAW-IMPOSSIBLE |

### 60.7 Theorem

The finite theorem is:

```text
Unique nontrivial process-law no-go.
From the current sealed-diamond ontology and structural requirements
alone, no unique nontrivial generative rule D |-> P_D can be derived.
```

Proof, finite form:

```text
1. The exchangeable hidden-record family P_theta gives a continuum of
   positive, covariant, projective, nontrivial laws indexed by theta in (0,1).
2. These laws satisfy the current structural sealed-diamond requirements but
   differ in joint probabilities and empirical predictions.
3. Therefore those requirements do not select a unique nontrivial law.
4. More generally, if any nontrivial projective/covariant law P is admitted,
   then (1-lambda)P + lambda U gives a continuum of admitted laws, where U is
   the uniform projective law.
5. If symmetry is strengthened enough to force uniqueness, it forces the
   uniform eventless law.
```

Therefore:

```text
Branch A-full, as a derivation from the current sealed-diamond ontology, is
impossible.
```

The remaining options are:

```text
Branch B:
  choose a process law/action/coupling/source/parameter empirically or
  phenomenologically.

New Branch A axiom:
  add a genuinely new generative physical law that fixes P_D.  This is no
  longer derived from the current ontology; it is new dynamics.
```

This is the clean endpoint of Paper 3's campaign.

## 61. Literature-grounded campaign for the right law [PROBE]

The no-go in §60 is not a failure of imagination; it is a constraint on what
any successful imagination has to do. The current sealed-diamond ontology
cannot derive a unique nontrivial law `D |-> P_D` from covariance,
positivity, projectivity, locality, collars, or refinement consistency alone.
Therefore the next question is:

```text
Is there a known kind of invariant physical principle that actually selects a
law, rather than a family?
```

The literature gives a sharp map.

**Exchangeability and de Finetti.** Exchangeability is the clean mathematical
version of "no hidden label order." It does not select a unique law. It
represents exchangeable laws as mixtures of simpler laws. This is exactly the
shape of the §60 exchangeable hidden-record counterfamily.

**Hammersley-Clifford, DLR, and Gibbs measures.** Positivity plus Markov
structure gives Gibbs/exponential form. It does not fix the potential or
couplings. Locality is a representation theorem, not a dynamics theorem.

**Rideout-Sorkin causal-set sequential growth.** Discrete general covariance
and a causality condition produce a general family of stochastic growth
dynamics, not one dynamics. This is the closest causal-set warning: even
strong causal covariance does not pick the transition weights.

**Barandes / indivisible stochastic processes.** Barandes' framework says the
primitive can be a whole non-Markovian stochastic law, with Hilbert space
secondary. That is exactly the right kind of object for this program. But the
framework is generic: it does not by itself decide which indivisible law
nature uses.

**Maximum entropy, maximum caliber, and Schrodinger bridges.** These are real
selection principles once a reference measure and constraints are supplied.
Without physical constraints they select the uniform/eventless law. With
constraints they select an exponential/bridge law. Thus they can be the form
of the answer, but not the whole answer unless the constraints are intrinsic.

**Petz recovery and quantum Markov structure.** Exact recovery is a beautiful
no-silent-seam principle. But exact recoverability is a consistency condition
on a supplied state/channel; it leaves families of recovered laws.

**Locally covariant QFT and relative Cauchy evolution.** The functorial
principle is close in spirit to sealed-diamond covariance. It can identify
stress-energy as the response to metric variation. But the theory functor is
still supplied.

**Jacobson/Casini modular-entanglement gravity.** This is the most relevant
positive analogy. A small causal diamond plus a modular/entropy first law can
turn an equilibrium condition into gravitational field equations. The price is
that the local vacuum, modular Hamiltonian, and universal entropy density are
real physical inputs or theorem targets.

**Causal fermion systems.** This is the closest structural cousin to a
fully relational law. The causal structure and field equations are tied to a
spectral action over operator-valued spacetime points. But the causal action
and its constraints are primitive. It teaches the same lesson in a positive
way: a real theory may need a fixed action principle, not only an ontology.

The literature verdict is therefore:

```text
principles of invariance and consistency give families;
principles of action/equilibrium/relative entropy can select laws;
but only after a physical work/action/source constraint is intrinsic.
```

### 61.1 Candidate: sealed modular entropic equivalence

The strongest law found in this campaign is a synthesis of the Schrodinger
bridge / maximum-caliber form with the Jacobson modular-equilibrium idea:

```text
Sealed Modular Entropic Equivalence Law (SMEEL).
```

For a sealed finite record diamond `D`, let:

```text
U_D = intrinsic count/reference law;
C_D = intrinsic complete collar/separator system;
W_D(c) = intrinsic screen-volume modular work assigned to each collar c.
```

Then the physical law is:

```math
P_D
=
\arg\min_{P\ll U_D}
D(P\Vert U_D)
```

subject to the sealed modular work constraints:

```math
D(P_c\Vert \Pi_c P_c)=W_D(c)
```

for every intrinsic collar/subdiamond `c`, together with sealed composition
and no-silent-seam RN additivity.

Equivalently:

```text
the physical diamond is the least extra-structured positive law whose
factorization defects exactly equal the intrinsic screen-volume work profile.
```

This is not "choose a kernel." It is a variational law. If `W_D` is derived
from the sealed diamond, the law selects `P_D`. If `W_D` is supplied, the law
is branch B with a better costume.

The diagnostic is:

```text
code/v6_p3ay_right_law_literature_campaign.py
```

### 61.2 Finite positive theorem

In the two-screen binary diamond, write:

```math
P_\theta(x,y)
=
{1+\theta xy\over4},
\qquad x,y\in\{-1,1\}.
```

The screen marginals are uniform, and the modular work / factorization defect
is:

```math
W(\theta)
=
D(P_\theta\Vert P_XP_Y)
=
{1\over2}\{(1+\theta)\log(1+\theta)
 +(1-\theta)\log(1-\theta)\}.
```

For `theta in (0,1)`,

```math
{dW\over d\theta}
=
{1\over2}\log {1+\theta\over1-\theta}
>0.
```

Therefore every intrinsic work value:

```math
W_D\in(0,\log 2)
```

selects exactly one nontrivial positive law `P_theta`. The finite receipt
uses `W_D=0.125` and obtains:

```text
theta = 0.489280512348;
reconstruction error = 1.388e-16.
```

This is the first genuinely law-shaped positive result:

```text
intrinsic modular work -> unique nontrivial sealed law.
```

### 61.3 Attacks

The same diagnostic also attacks the law.

| target | principle | selection | obstruction | value | verdict |
|---|---|---|---|---:|---|
| old structural axioms | covariance + positivity + projectivity | admits all theta | defect amplitude remains free | span 0.600 | FAIL-UNIQUE |
| maximum entropy | maximize H(P) with no physical work constraint | unique uniform law | eventless | MI 0.000 | FAIL-TRIVIAL |
| modular entropic equivalence | max entropy subject to intrinsic W_D | unique tilted law | works only if W_D is intrinsic | W 0.125, theta 0.4893 | PASS-CONDITIONAL |
| work-target drift | same rule, different supplied W_D | different laws | W_D is the hidden selector | theta span 0.4891 | FAIL-IF-W-SUPPLIED |
| Schrodinger bridge, no coupling | minimize KL to count/reference with only screen marginals | unique product bridge | no event-producing correlation | MI 0.000 | FAIL-EVENTLESS |
| Schrodinger/MaxCal with work | minimize KL with boundary marginals plus work | unique bridge | work/action constraint is extra | KL-to-uniform 0.125 | COND-ACTION |
| Petz/Markov recovery | exact recovery I(A:C\|B)=0 | whole family | recovery exactness is consistency, not dynamics | CMI 0.0e+00, span 1.000 | FAIL-UNIQUE |
| Barandes/unistochastic form | probabilities from an indivisible stochastic-quantum dilation | family of unitary angles | Hamiltonian/action still selects the law | p span 0.574 | FAIL-DYNAMICS-FREE |
| causal-action analogue | minimize positive spectral/RN defect action | zero-defect law unless constrained | nonzero event needs volume/trace/work constraint | min at theta 0 | FAIL-TRIVIAL-OR-COND |
| best candidate | sealed modular entropic equivalence law | P_D = max-ent law matching intrinsic screen-volume work profile | not closed until that profile is derived from the diamond | finite theta 0.4893 | CANDIDATE-LAW |

The attacks say:

```text
1. Entropy alone gives the eventless law.
2. Bridge principles alone give product transport unless a coupling/work
   constraint is present.
3. Recovery/no-silent-seam principles give consistency but not amplitude.
4. Indivisible stochastic form gives the right object type but not the
   Hamiltonian/action.
5. Causal-action analogues need a nonzero constraint to avoid the zero-defect
   minimizer.
```

Thus SMEEL is innovative only as a synthesis:

```text
sealed finite ISP law
+ Schrodinger/MaxCal relative entropy selection
+ modular factorization defect
+ Jacobson-style screen-volume work balance
+ sealed composition/no-silent-seam constraints.
```

Each ingredient has literature ancestors. The proposed unity of them as a
finite sealed-diamond record law is new relative to the present manuscript,
but it is not magic. It inherits the exact old burden:

```text
derive W_D intrinsically.
```

### 61.4 Result

The campaign finds the strongest candidate law:

```text
Sealed Modular Entropic Equivalence Law.
```

Finite theorem:

```text
If a sealed diamond intrinsically supplies a screen-volume modular work
profile W_D(c), then P_D is the unique relative-entropy-minimal positive law
whose collar factorization defects equal W_D(c), provided the constraint
family is feasible and separating.
```

Finite falsifier:

```text
If W_D is not intrinsic, changing W_D changes the selected law while preserving
the same structural ontology. Then branch A is not closed.
```

So the clean endpoint is:

```text
Right law candidate:
  P_D = the least RN-disturbing sealed law matching intrinsic modular
  screen-volume work.

Branch A-full:
  alive only if W_D is derived from the sealed diamond's physical
  screen/volume geometry, not assigned as a constraint.

Branch B:
  the verdict if W_D, an action, a Hamiltonian, or a bridge cost is supplied.
```

This is the most Einstein-compatible law found by the literature campaign:
not "choose a stochastic process," but:

```text
the stochastic process is the unique least-action/least-relative-entropy way
for a sealed causal diamond to realize its own intrinsic modular work.
```

The remaining theorem is no longer "find any law." It is:

```text
Intrinsic Work Theorem.
Every physical sealed record diamond derives a unique screen-volume modular
work profile W_D(c), and the SMEEL constraints are feasible, separating, and
cofinally stable.
```

If that theorem fails, the §60 no-go remains decisive: a unique nontrivial
`D |-> P_D` cannot be derived from the current sealed-diamond ontology alone.

## 62. Diamond work-balance principle [PROBE]

Section 61 still left one exposed surface: it selected `P_D` only after an
intrinsic work profile `W_D` was known. That is better than choosing a kernel,
but not yet the law. The stronger move is to remove `W_D` as a separate
object.

The new principle is:

```text
Diamond Work-Balance Principle.
A primitive sealed event defect is physical iff its stored modular
factorization work equals its own intrinsic screen-response curvature.
```

In symbols:

```math
W_{\rm info}(P_D,R_D)=J_{\rm screen}(P_D,R_D).
```

Here both sides are computed from the same sealed law:

```text
W_info    = RN/KL work stored in the failure of sealed factorization;
J_screen  = Fisher/Hessian response of the same lower-to-upper screen score.
```

This is the finite version of the desired equivalence principle. It does not
say "match an externally supplied work." It says the diamond is physical when
the modular work it stores is exactly the screen response it itself makes
available.

The diagnostic is:

```text
code/v6_p3az_diamond_work_balance_principle.py
```

### 62.1 Primitive two-sector theorem

For an indivisible binary sealed defect, let the intrinsic collar score be:

```math
q=xy\in\{-1,+1\},
```

with count reference:

```math
U(q=\pm1)=1/2.
```

The positive role-blind laws are:

```math
P_\theta(q)
=
{1+\theta q\over2},
\qquad
\theta\in[0,1).
```

Equivalently:

```math
P_\eta(q)
=
{e^{\eta q}\over2\cosh\eta},
\qquad
\theta=\tanh\eta.
```

The stored modular factorization work is:

```math
W(\theta)
=
D(P_\theta\Vert U)
=
{1\over2}\{(1+\theta)\log(1+\theta)
 +(1-\theta)\log(1-\theta)\}.
```

The intrinsic screen response is the Fisher curvature of the same normalized
screen score:

```math
J(\theta)
=
{\rm Var}_{P_\theta}(q)
=
1-\theta^2.
```

The physical law is:

```math
W(\theta)=J(\theta).
```

This equation has exactly one nontrivial solution. Define:

```math
F(\theta)=W(\theta)-J(\theta).
```

Then:

```math
F(0)=-1,
\qquad
\lim_{\theta\to1^-}F(\theta)=\log2,
```

and:

```math
F'(\theta)
=
\operatorname{arctanh}\theta+2\theta
>0
```

for every `theta in (0,1)`. Therefore there is one and only one crossing:

```text
theta_* = 0.797003794162878;
eta_*   = 1.090344354879492;
W_*     = J_* = 0.364784952089976.
```

This is a real selection theorem in the primitive finite class:

```text
no supplied threshold;
no supplied beta;
no supplied work target;
no supplied source amplitude.
```

The law itself fixes the common work/response value.

### 62.2 Receipts

The finite audit gives:

| target | invariant | result | value | verdict |
|---|---|---|---:|---|
| old family | covariance/projectivity only | theta remains free | balance residual span 0.845 | FAIL-OLD-A |
| eventless maximum entropy | theta=0 | unique but no defect | W-J -1.000 | FAIL-TRIVIAL |
| diamond work balance | W_info(theta)=J_screen(theta) | unique nonzero theta | theta 0.797003794163 | PASS-SELECTS-P |
| uniqueness proof | F'=atanh(theta)+2 theta > 0 | one crossing in (0,1) | F(0)=-1, F(1-)=log2 | PASS-THEOREM |
| no supplied W_D | W is computed from P, J is computed from P | fixed point supplies common work | W=J=0.364784952090 | PASS-NONCONDITIONAL |
| composition | independent sealed copies | balance is additive | abs(2W-2J)=2.2e-16 | PASS |
| pure refinement | split atoms without changing modular score | balance is stable | abs(W-J)=2.2e-16 | PASS |
| four-role identity | RN/deletion/source/screen score directions | all roles colinear | cos min 1.000000000000 | PASS |
| beta lock | beta^2=J=W at fixed point | scale fixed in count/RN units | beta 0.603974297541, heat 0.033267015318 | PASS |
| mixture attack | mixing moves theta off fixed point | mixtures fail unless at theta* | L1 gap from theta=.45 is 0.347 | PASS-REJECTS-FAMILY |
| three-shell extension | normalized count-variance score | unique tested crossing | eta 1.149609, abs(W-J)=1.7e-16 | PASS-FINITE-EXT |

The important line is the fifth:

```text
W_D is not supplied.
```

The common work value is:

```math
W_D=J_D
```

at the fixed point.

### 62.3 What this collapses

In the primitive sealed event class, the work-balance law collapses the old
list of targets:

```text
P_D:
  selected as the unique positive law satisfying W=J.

threshold:
  zero RN boundary of the selected exponential family.

deletion:
  product/RN repair of the unique nonzero factorization defect.

source amplitude:
  the centered RN score, fixed by eta_*.

screen response:
  J_* = W_*.

beta:
  beta^2 = J_* = W_* in count/RN units.

four-role identity:
  record, deletion, source, and screen derivatives are the same centered score.
```

Thus the old overconstraint becomes useful. The separate gates were shadows of
one equality:

```text
stored modular work = available screen response.
```

### 62.4 What is still not claimed

This does not say every arbitrary sealed law is selected. It says the
primitive indivisible defect has a nonconditional fixed law once the defect is
really a two-sector normalized modular score.

The remaining generalization target is now much smaller than §61's open
surface:

```text
Primitive Defect Theorem.
Every objective event of the full sealed record process reduces locally,
after intrinsic collar minimization, to a normalized one-dimensional
two-sector modular score.
```

If that theorem holds, the branch-A-enriched process has an actual law:

```text
D -> intrinsic primitive score q_D -> unique theta_* -> P_D.
```

If it fails, the work-balance equation may still define a useful branch-B or
effective law, but not the pure primitive event theory.

### 62.5 Verdict

The campaign did find a nonconditional law in the primitive finite class:

```text
Diamond Work-Balance Law:
  D(P_D || Pi_R P_D) = Fisher_screen(P_D,R_D).
```

This is the first place where the finite theory stops asking for `W_D` and
computes the selected value internally. It is also Barandes-aligned: the
object selected is a whole sealed non-Markovian record law, not a transition
kernel. The next attack is no longer "derive the work target." It is:

```text
derive primitive two-sector modularity from sealed indivisibility.
```

## 63. Full prove/discard campaign for work balance [PROBE]

Section 62 proved something real, but it did not prove the universal law. The
full question is:

```text
Does Diamond Work-Balance select a unique physical law on arbitrary sealed
finite diamonds?
```

The diagnostic is:

```text
code/v6_p3ba_work_balance_full_campaign.py
```

The answer is:

```text
No, not universally.
Yes, in the primitive binary modular-score class.
```

This is a prove/discard split, not another conditional.

### 63.1 What is proved

For the primitive binary modular score:

```math
q\in\{-1,+1\},
\qquad
P_\theta(q)={1+\theta q\over2},
```

the balance equation:

```math
W(\theta)=J(\theta)
```

has exactly one nonzero solution:

```text
theta = 0.797003794162878;
eta   = 1.090344354879492;
W=J   = 0.364784952089976.
```

The proof is strict. With:

```math
F(\theta)=W(\theta)-J(\theta),
```

we have:

```math
F(0)=-1,
\qquad
\lim_{\theta\to1^-}F(\theta)=\log2,
```

and:

```math
F'(\theta)
=
\operatorname{arctanh}\theta+2\theta
>0.
```

Therefore one and only one positive root exists. In this class, the law really
selects:

```text
P_D;
beta;
source amplitude;
common modular work;
four-role derivative direction.
```

### 63.2 What is discarded

The universal version is false. Diamond work-balance does not select a unique
law on arbitrary finite sealed score spectra.

First, a finite one-score counterexample exists. Let the count reference be a
uniform finite multiset with five score values and multiplicities:

```text
values:
  -15.848391065169443
  -15.26135706229148
  -6.540840401342667
   0.8016439899950072
  18.903204268406732

multiplicities:
  1141481, 45, 1310511, 67, 3.
```

After intrinsic normalization to count-mean zero and count-variance one, the
same equation:

```math
D(P_\eta\Vert U)= {\rm Var}_{P_\eta}(q)
```

has three positive roots:

```text
eta = 1.103863589440738;
eta = 1.629645500280153;
eta = 2.425948703849044.
```

Thus work-balance alone does not guarantee uniqueness even in a one-dimensional
finite score law.

Second, multi-score diamonds are underdetermined. For two independent binary
primitive channels:

```math
F(\theta_1)+F(\theta_2)=0
```

is one scalar equation on two amplitudes. The diagnostic gives two distinct
solutions:

```text
(theta1, theta2) = (0.797004, 0.797004);
(theta1, theta2) = (0.550000, 0.965326).
```

So scalar work-balance cannot be the complete law for general multi-defect
diamonds. Componentwise balance would select:

```text
theta_i = theta_*
```

in each primitive channel, but then the theory must derive the canonical
primitive channel decomposition. Without that, the scalar law is not complete.

### 63.3 Audit

| target | result | value | verdict |
|---|---|---:|---|
| primitive binary theorem | unique nonzero root because F'=atanh(theta)+2theta>0 | theta=0.797003794162878, eta=1.090344354879492, W=J=0.364784952089976 | PROVED |
| regular one-score spectrum | tested three-shell count spectrum has one root | 1.149609196642 | PASS-EXAMPLE |
| general one-score uniqueness | finite count-multiplicity spectrum has three roots | 1.103863589441, 1.629645500280, 2.425948703849 | REFUTED-GENERAL |
| multi-score scalar balance | F(theta1)+F(theta2)=0 has more than one solution | (0.797004,0.797004) and (0.550000,0.965326) | REFUTED-SCALAR-SELECTION |
| componentwise repair | F_i(theta_i)=0 would select theta* in each primitive channel | theta_i=0.797003794163 | COND-NEEDS-CANONICAL-CHANNELS |
| universal DWB law | not valid as a uniqueness law on arbitrary sealed finite diamonds | one-score and vector counterexamples | DISCARDED |
| primitive DWB law | valid for indivisible binary modular-score defects | selects P_D, beta, source amplitude, common work | SURVIVES |

### 63.4 Final verdict

The universal claim is discarded:

```text
Diamond Work-Balance is not a complete unique law on arbitrary sealed finite
diamonds.
```

The primitive claim is proved:

```text
Diamond Work-Balance is a complete unique law for a normalized indivisible
binary modular-score defect.
```

Therefore branch A cannot say:

```text
all sealed diamonds satisfy scalar W=J, therefore P_D is fixed.
```

It can say only the sharper statement:

```text
an objective primitive event is a normalized binary modular defect, and that
defect's law is fixed by W=J.
```

So the law is not dead, but it has been narrowed. The correct ontology cannot
be "arbitrary sealed diamond plus work balance." It must be:

```text
sealed finite record process
-> intrinsic decomposition into primitive indivisible binary modular defects
-> componentwise Diamond Work-Balance on each primitive defect.
```

This is the clean result. The law either reduces events to primitive binary
modular defects, or it fails as branch A.

## 64. Primitive-defect theorem campaign [PROBE]

Section 63 narrowed the problem to one question:

```text
Does sealed indivisibility force a primitive binary modular defect?
```

The diagnostic is:

```text
code/v6_p3bb_primitive_defect_theorem_campaign.py
```

The answer is:

```text
No, not from the current weak meanings of indivisibility.
```

This matters because the primitive binary Diamond Work-Balance law is proved,
but it becomes branch-A closure only if physical sealed events really are
binary modular defects. The campaign tests the tempting routes one by one.

### 64.1 Product indivisibility is not enough

Take a finite score with three count atoms:

```text
q = (-1, 0, +1),
```

then normalize it to count-mean zero and count-variance one. Since the atom
count is prime, there is no nontrivial Cartesian product factorization of the
atom set. In that sense the score is product-indivisible.

But it has three score levels, not two:

```text
levels = 3.
```

It even has a unique work-balance root:

```text
eta = 1.149609196641639.
```

Therefore:

```text
indecomposable atom set does not imply binary modular defect.
```

### 64.2 Rank-one score geometry is not enough

The same three-level score defines a one-parameter exponential law:

```math
P_\eta(a)
\propto
e^{\eta q(a)}.
```

Its Fisher geometry has one score direction. Thus the score geometry is
rank-one. But the score spectrum is still:

```text
three-level.
```

Therefore:

```text
rank-one Fisher/score geometry does not imply binary.
```

### 64.3 Unique work-balance root is not enough

The three-level score has one `W=J` crossing, but the score is not binary.
So even a successful scalar work-balance selection does not prove the event is
a binary primitive.

The implication fails:

```text
unique W=J root -> binary.
```

### 64.4 Rank-one collar interaction is not enough

One might try to save the theorem by requiring the collar interaction itself
to have rank one. Let:

```math
q(i,j)=a_i b_j,
```

with:

```text
a=(-1,0,+1),
b=(-1,0,+1).
```

The interaction matrix has rank:

```text
rank = 1.
```

But the score values are:

```text
-1, 0, +1,
```

so the collar interaction is still nonbinary. Thus:

```text
rank-one collar coupling does not imply binary modular defect.
```

### 64.5 General one-score spectra can also break uniqueness

The previous section already found a finite one-dimensional spectrum where
work-balance has three roots. The same counterexample is repeated here because
it attacks the primitive-defect theorem directly.

Use a uniform finite multiset represented by values:

```text
-15.848391065169443
-15.26135706229148
-6.540840401342667
 0.8016439899950072
18.903204268406732
```

with multiplicities:

```text
1141481, 45, 1310511, 67, 3.
```

After count normalization, the one-score equation:

```math
D(P_\eta\Vert U)= {\rm Var}_{P_\eta}(q)
```

has:

```text
three roots.
```

Therefore not only does one-dimensionality fail to imply binary; it can also
fail to imply unique work-balance selection.

### 64.6 The only finite route that forces binary

The campaign found one clean invariant route to binary:

```text
saturated modular contrast.
```

For any finite score with count/reference weights, Popoviciu's variance bound
gives:

```math
{\rm Var}(q)
\le
{({\rm max}\,q-{\rm min}\,q)^2\over4}.
```

Equality holds only when the score takes endpoint values only. Thus a
score that saturates the available contrast has exactly two levels. The finite
audit gives:

```text
binary Popoviciu ratio      = 1.000;
three-shell Popoviciu ratio = 0.667.
```

So a stronger principle would work:

```text
Saturated Boolean Modular Contrast:
an objective primitive event is a sealed modular defect whose count-normalized
score saturates the endpoint variance bound.
```

This principle forces the score to be binary, and then §62's Diamond
Work-Balance theorem fixes the law.

But this is not derived from weak sealed indivisibility. It is a stronger
physical invariant.

### 64.7 Audit

| target | test | result | value | verdict |
|---|---|---|---:|---|
| product indivisibility | 3 atoms have no nontrivial Cartesian product factorization | indecomposable but nonbinary | levels=3, roots=1 | REFUTES-WEAK-INDIV |
| rank-one score geometry | single exponential parameter over three score levels | Fisher rank one but nonbinary | levels=3 | REFUTES-RANK1-IMPLIES-BINARY |
| unique DWB root | three-shell score has one W=J crossing | unique root but nonbinary | 1.149609196642 | REFUTES-ROOT-IMPLIES-BINARY |
| rank-one collar interaction | q(i,j)=a_i b_j has interaction matrix rank one | collar interaction rank one but nonbinary | rank=1, levels=3 | REFUTES-COLLAR-RANK1 |
| general score spectrum | finite uniform multiset represented by multiplicities | one-dimensional DWB can have three roots | atoms=2452107, roots=3 | REFUTES-GENERAL-PRIMITIVE |
| saturated contrast | Popoviciu ratio Var/(range^2/4) | saturation forces endpoint-only score | binary=1.000, three-shell=0.667 | PROVES-BINARY-IF-AXIOM |
| current sealed indivisibility | product/rank/root/collar indivisibility audits | does not force binary | counterexamples above | DISCARDED-AS-DERIVATION |
| stronger invariant | saturated Boolean modular contrast | would force primitive binary defects | new physical law/principle | REQUIRED-TO-CLOSE |

### 64.8 Verdict

The current primitive-defect theorem is false:

```text
sealed indivisibility, understood as no product split, rank-one score,
unique work-balance root, or rank-one collar interaction, does not force a
binary modular defect.
```

The stronger theorem is true:

```text
saturated endpoint modular contrast forces a binary defect.
```

Therefore the Branch-A closure chain becomes:

```text
Saturated Boolean Modular Contrast
-> primitive binary modular defect
-> Diamond Work-Balance
-> unique P_D, beta, source amplitude, and four-role derivative.
```

This is a clean outcome. It discards the hope that "indivisible" alone does
the work. It replaces that hope with the only invariant found in the finite
campaign that actually forces binary:

```text
objective events are saturated two-endpoint modular contrasts.
```

If that principle is adopted as the real primitive event principle, Branch A
has a tight law. If it cannot be justified physically, the primitive binary law
is a strong model postulate rather than a derivation.

## 65. Saturation principle campaign [PROBE]

Section 64 found that weak sealed indivisibility does not force a binary
defect. The surviving invariant was:

```text
Saturated Boolean Modular Contrast.
```

This section asks whether that saturation can itself be derived, or whether it
is just the next assumption.

The diagnostic is:

```text
code/v6_p3bc_saturation_principle_campaign.py
```

The answer is a split:

```text
weak indivisibility -> saturation: false;
lossless Boolean readout + count-dual endpoints -> saturation: true.
```

### 65.1 The three pieces are distinct

There are three properties:

```text
Booleanity:
  the event score has only two values.

Count-duality:
  the two endpoint alternatives have equal count/reference weight.

Saturation:
  Var(q) = (max q - min q)^2 / 4.
```

They are not the same.

A three-shell score:

```text
q=(-1,0,+1)
```

has a unique work-balance root, but it is not Boolean. Its best binary
coarse-graining leaves positive residual:

```text
Boolean residual = 0.250.
```

An unbalanced binary score is Boolean but not saturated. With endpoint count
weights:

```text
3:1,
```

the Boolean residual is zero, but the count-duality gap is:

```text
0.250,
```

and the Popoviciu saturation ratio is:

```text
0.750.
```

So binary alone does not preserve the universal constants. The work-balance
root shifts:

```text
balanced eta   = 1.090344354879;
unbalanced eta = 1.166712545485.
```

Thus:

```text
binary is not enough;
balanced binary is the real primitive.
```

### 65.2 Boolean sufficiency theorem

Let `q` be a finite count-normalized modular score. Consider all binary
readouts:

```text
B:{score levels}-> {0,1}.
```

For each `B`, compute the residual:

```math
{\rm Res}_B(q)
=
E_U\{(q-E_U[q|B])^2\}.
```

Then:

```text
min_B Res_B(q)=0
```

if and only if `q` takes at most two distinct values.

Therefore a physical principle can force binary if it says:

```text
the objective event readout is a lossless Boolean statistic of the modular
score.
```

This is stronger than "indivisible." It says the event has no interior modular
value left over after the yes/no event readout is known.

### 65.3 Count-duality theorem

For any finite score:

```math
{\rm Var}_U(q)
\le
{({\rm max}\,q-{\rm min}\,q)^2\over4}.
```

Equality holds exactly when the count/reference law is supported on the two
endpoints with equal endpoint weight. Therefore:

```text
Booleanity + count-duality <=> Popoviciu saturation.
```

In normalized units this gives:

```text
q in {-1,+1} with U(q=-1)=U(q=+1)=1/2.
```

That is precisely the primitive class used by the Diamond Work-Balance theorem.

### 65.4 Audit

| target | test | result | value | verdict |
|---|---|---|---:|---|
| balanced binary | Boolean residual + count-duality + Popoviciu saturation | levels=2, roots=1 | res=0.000, gap=0.000, pop=1.000 | PASS-SATURATED |
| three-shell event | Boolean residual + count-duality + Popoviciu saturation | levels=3, roots=1 | res=0.250, gap=0.167, pop=0.667 | FAIL-INTERIOR-SLACK |
| unbalanced binary | Boolean residual + count-duality + Popoviciu saturation | levels=2, roots=1 | res=0.000, gap=0.250, pop=0.750 | FAIL-COUNT-DUALITY |
| four-level score | Boolean residual + count-duality + Popoviciu saturation | levels=4, roots=1 | res=0.228, gap=0.000, pop=0.547 | FAIL-BOOLEAN-LOSS |
| Boolean sufficiency theorem | min residual after all binary coarse-grainings | zero iff score is two-valued | finite enumeration | PROVES-BINARY |
| count-duality theorem | two-valued score plus equal count weights | equivalent to Popoviciu saturation | pop=1 | PROVES-SATURATION |
| unbalanced constants attack | binary without count-duality | DWB root changes | balanced eta=1.090344354879, unbalanced eta=1.166712545485 | REFUTES-BINARY-ALONE |
| derivation status | weak sealed indivisibility | does not imply Boolean sufficiency or count-duality | requires stronger event principle | NOT-DERIVED |
| closure principle | lossless Boolean readout + count-dual endpoints | derives saturated Boolean modular contrast | then DWB closes primitive law | CLOSES-IF-ADOPTED |

### 65.5 Result

The finite result is:

```text
Saturation is not derived from weak indivisibility.
```

But saturation is not arbitrary either. It is exactly the combination of two
clean event principles:

```text
1. Lossless Boolean event readout:
   knowing whether the event occurred loses no modular-score information.

2. Count-dual endpoints:
   before the event law tilts the diamond, the two endpoint alternatives are
   equally represented in the sealed count/reference structure.
```

Together they give:

```text
Saturated Boolean Modular Contrast.
```

Then §62 gives:

```text
Saturated Boolean Modular Contrast
-> balanced primitive binary defect
-> unique Diamond Work-Balance law
-> fixed P_D, beta, source amplitude, and four-role derivative.
```

The current Branch-A status is therefore:

```text
closed at finite primitive level if the event principle is
lossless Boolean + count-dual.

not derived from weaker sealed indivisibility.
```

This is as clean as the finite campaign can make it: the missing invariant is
not "saturation" as a naked axiom, but:

```text
objective event = lossless count-dual Boolean readout of modular contrast.
```

## 66. Event-principle identity campaign [PROBE]

Section 65 still used the phrase:

```text
lossless count-dual Boolean readout.
```

This section pins it down as a finite theorem packet. The question is:

```text
Can this principle be stated as an intrinsic event identity rather than as a
new tuning condition?
```

The diagnostic is:

```text
code/v6_p3bd_event_principle_identity_campaign.py
```

The finite answer is:

```text
yes, if objective event means a complete idempotent event proposition whose
complement is count-indistinguishable before the event law tilts the diamond.
```

It is not derived from weak sealed atoms/order/rank/root data. It is a sharper
primitive identity principle.

### 66.1 Event proposition forces Booleanity

In a finite commutative record algebra, an event proposition is an idempotent:

```math
E^2=E.
```

Pointwise, this implies:

```math
E(a)\in\{0,1\}.
```

Thus a real finite idempotent record event is automatically Boolean. A fuzzy
middle value is not an event proposition:

```text
E=[0,0.5,1] has max |E^2-E| = 0.250.
```

This is the first real nail:

```text
event proposition -> Boolean readout.
```

### 66.2 Completeness forces losslessness

Let `q` be the modular contrast score of the candidate event. The event
proposition `E` is complete for that contrast iff:

```math
{\rm Var}_U(q|E)=0.
```

Equivalently:

```math
q=E_U[q|E],
```

so `q` is affine in the idempotent `E`:

```math
q=q_0(1-E)+q_1E.
```

Therefore `q` has at most two values. This gives:

```text
complete idempotent event -> lossless Boolean modular contrast.
```

The three-shell countermodel shows why completeness is necessary. With:

```text
q=(-1,0,+1),
```

and any Boolean event grouping, an interior modular residue remains. The audit
gives:

```text
sufficiency residual = 0.250.
```

So the event readout was not complete.

### 66.3 Leibniz complement symmetry forces count-duality

Booleanity alone is not enough. The count/reference law may already privilege
one endpoint. For a binary score with count weights:

```text
3:1,
```

the event is Boolean and complete, but not count-dual:

```text
complement gap = 0.500;
Popoviciu ratio = 0.750.
```

The Diamond Work-Balance constant moves:

```text
balanced eta   = 1.090344354879;
unbalanced eta = 1.166712545485.
```

Thus the event principle needs a prior-indifference clause:

```text
Before the event law tilts the diamond, event and complement are related by a
count/reference-preserving internal automorphism.
```

Call this:

```text
Leibniz complement symmetry.
```

It implies:

```math
U(E=0)=U(E=1)=1/2.
```

Therefore:

```text
complete idempotent event + Leibniz complement symmetry
-> lossless count-dual Boolean modular contrast.
```

### 66.4 Closure theorem

The finite closure theorem is:

```text
Primitive Event Identity Theorem.
Let D be a finite sealed record diamond with count/reference law U. Suppose
there is an event proposition E such that:

1. idempotence: E^2=E;
2. completeness: Var_U(q|E)=0 for the event's modular score q;
3. complement symmetry: an internal U-preserving automorphism sends E to 1-E.

Then q is count-equivalent to the balanced binary score {-1,+1}.
```

Proof:

```text
Idempotence makes E Boolean.
Completeness makes q affine in E, hence two-valued.
Complement symmetry gives equal count/reference weight to E=0 and E=1.
After count normalization, q is {-1,+1} with equal weights.
Therefore the Popoviciu bound is saturated.
```

Then the primitive Diamond Work-Balance theorem applies and fixes:

```text
theta_* = 0.797003794162878;
eta_*   = 1.090344354879492;
W_*=J_* = 0.364784952089976.
```

### 66.5 Audit

| target | test | result | value | verdict |
|---|---|---|---:|---|
| event proposition | pointwise idempotence E^2=E | real finite idempotent has values 0 or 1 | err(E=[0,1])=0.0e+00 | PROVES-BOOLEAN-READOUT |
| non-idempotent readout | allow middle value | not an event proposition | err(E=[0,.5,1])=0.250 | REJECTS-FUZZY-EVENT |
| balanced primitive packet | idempotent + sufficiency + complement symmetry | packet values | idem=0.000, suff=0.000, comp=0.000, pop=1.000 | PASS-CLOSES |
| three-shell countermodel | idempotent + sufficiency + complement symmetry | packet values | idem=0.000, suff=0.250, comp=0.333, pop=0.667 | FAIL-SUFFICIENCY |
| unbalanced binary countermodel | idempotent + sufficiency + complement symmetry | packet values | idem=0.000, suff=0.000, comp=0.500, pop=0.750 | FAIL-COMPLEMENT |
| complete-event theorem | E idempotent and Var(q\|E)=0 | q is affine in E, hence two-valued | finite conditional variance identity | PROVES-LOSSLESS-BOOLEAN |
| Leibniz complement theorem | count/reference automorphism E <-> 1-E | U(E=0)=U(E=1)=1/2 | orbits have equal count | PROVES-COUNT-DUALITY |
| saturation theorem | lossless Boolean + complement symmetry | Popoviciu ratio is one | balanced pop=1.000 | PROVES-SATURATION |
| DWB constants | balanced vs unbalanced binary | unbalanced endpoint priors move eta | balanced=1.090344354879, unbalanced=1.166712545485 | PROVES-COMPLEMENT-NEEDED |
| weak ontology | sealed atoms/order/rank/root without event identity | admits countermodels above | not enough | REFUTED |
| nailed event principle | complete idempotent event + Leibniz complement symmetry | derives lossless count-dual Boolean contrast | feeds primitive DWB | FINITE-CLOSURE |

### 66.6 Final finite branch-A packet

The finite packet is now:

```text
Primitive event identity:
  complete idempotent event proposition
  + Leibniz complement symmetry.

implies:
  lossless count-dual Boolean modular contrast.

implies:
  saturated primitive binary defect.

implies:
  Diamond Work-Balance unique law.
```

This closes the primitive finite chain:

```text
E^2=E;
Var_U(q|E)=0;
E <-> 1-E under U;
D(P || Pi P)=Fisher_screen(P);
```

gives:

```text
fixed P_D;
fixed beta;
fixed source amplitude;
fixed four-role derivative.
```

The negative result is equally important:

```text
sealed atoms/order/rank/root/weak indivisibility do not derive this packet.
```

So the honest status is:

```text
Branch A finite primitive: closed by the Primitive Event Identity packet.
Branch A from weaker sealed ontology alone: refuted by countermodels.
Branch B: if the event identity packet is treated as phenomenological rather
than as the primitive definition of objective event.
```

This is no longer a loose search for a parameter. It is a precise choice of
primitive:

```text
objective event = complete count-symmetric idempotent modular proposition.
```
