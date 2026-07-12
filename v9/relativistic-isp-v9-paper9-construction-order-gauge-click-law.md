# Construction-order gauge and the underdetermination of the interacting record click law

**Series:** Relativistic ISP, v9 paper 9. **Status:** hostile-review passed at scoped result, 2026-07-11. Three independent referees ran three rounds. Rounds 1–2 returned MAJOR REVISION; every concrete opening was investigated before the next round. Final verification: PASS-WITH-CORRECTIONS / PASS / PASS, with the last restriction-functor blocker repaired and independently rerun. The paper establishes a finite conditional classical template and an underdetermination theorem—not the final unique interacting law. It does not revise Paper 8's reviewed diffusion measurement.

## Abstract

The v7 click law fixes an exact one-lineage marginal, `S(I)=exp(-I)`, but not the joint interacting dynamics. Paper 8's successful diffusion builder uses a global scheduler and does not instantiate that law. We ask whether record sufficiency, construction-order gauge, ancestry locality, exact conditional evidence renewal, conservation, and classical no-signaling force a unique interaction. **(1) Gauge corrected.** Raw local-clock race orders may have unequal probabilities (`0.2353/0.7647`) while pushing forward to one marked partial history; the physical object is the quotient measure, not equal proposal weights. An exact end-to-end finite trace—including common cause, local settings/seals, outcomes, RN block IDs, conservative joint transfer, ancestry, and renewal—has identical canonical pushforwards under unequal-rate priority-queue and direct-trace schedulers. **(2) A conditional classical family exists.** Independent unit Poisson clocks in typed support-evidence compensators generate recurrent private and common-cause seals. Conditional on a realized future incident-evidence increment, lineage survival is exactly exponential; random unconditioned exposure gives `E exp(-Delta I)`, not `exp(-E Delta I)`. Typed lineage ports make disjoint scheduler presentations identical and overlapping events record ancestry. The integrated outcome kernel is two-sided no-signaling and Bell-local (`CHSHmax=0.7`). **(3) RN/KL typing matters.** Conditional likelihood blocks obey the chain rule; marginal KL can miss pure correlation evidence (`0` versus joint `0.3681`), and counting one shared observation twice doubles its evidence (`0.1927 -> 0.3855`). **(4) Support and restriction.** A support-local law cannot merge disconnected components; common-ancestor branching supplies a connected seed but leaves the root/branch rule as boundary law. Cross-boundary joint events retain projected marks, and finite restriction composes exactly. **(5) Main theorem: underdetermination.** Explicit forward/reverse likelihood models with fixed lineage evidences `1.1/0.9` and shared allocations `c=0.2/0.7` satisfy the same corrected finite classical constraints but give covariances `0.02996/0.13720`. Conservative transfers `g=0.1/0.3` independently preserve click marginals and totals while changing dynamics. Hence current principles do **not** force a unique final interacting law. They define a finite gauge-local classical family conditional on support/exposure data; selecting its coupling requires new physics.

## 1. Construction-order gauge: the quotient is the physical object

The preceding first-assembly conclusion is superseded. Three independent hostile reviews reproduced all arithmetic and returned MAJOR REVISION. Their central correction is adopted as a theorem boundary.

Let `Omega_lab` contain scheduler presentations and let `q` map them to covariant marked histories. Record sufficiency requires a physical pushforward measure

`mu_phys(A) = mu_lab(q^{-1}(A))`.

It does not require equal `mu_lab` density at every point of a fiber without first fixing a reference measure/gauge. Two one-shot local clocks of rates `lambda_A != lambda_B` give unequal raw orders

`P(AB)=lambda_A/(lambda_A+lambda_B)`, `P(BA)=lambda_B/(lambda_A+lambda_B)`,

yet after both fire the unordered marked set has probability one. Equal-path diamonds are a sufficient strong gauge convention for a normalized labeled growth kernel, not the general forced statement.

The corrected locality test is likewise marginal: independent components have a factorized semigroup even though a Gillespie implementation normalizes “which fires next?” by the sum of every enabled rate. That algorithmic denominator is not physical action at a distance.

The serial commit label `b` is retained only as a topological sorting used by a simulator. It is absent from the physical event schema and the causal definition. The physical law lives on canonical marked partial histories. This is not the claim that every raw race order has equal density.

The standard adjacent-swap lemma remains useful: every two linear extensions are connected by swaps of incomparable events (exactly checked on all naturally labeled posets through `n=5`). But equal-path diamonds are only a sufficient strong gauge convention after a labeled reference measure is fixed.

## 2. The recurrent marked-support process

The amended construction is one integrated **classical** process.

1. A finite or locally finite marked support family contains singleton supports and recorded multi-lineage supports.
2. Every support `S` carries an independent unit-rate Poisson process in its own typed intrinsic evidence exposure `I_S`.
3. Every firing writes one atomic marked event containing `S`, its latest parent events on the participating lineages, the evidence block identifier, an outcome mark, and any rational conservative content transfer.
4. A lineage receives a seal whenever any incident support fires. The superposed incident process has total evidence `I_i=sum_{S contains i} I_S`, so its conditional survival after every finite past is `exp(-Delta I_i)` by independent increments.
5. Relative scheduler order of disjoint events is forgotten by `q`; overlapping events share a lineage, hence the later event records the earlier as a parent.
6. A common ancestor can write a hidden classical common-cause mark. Local descendant settings act only on local response kernels. The explicit finite family is normalized, two-sided no-signaling, sequentially composable, and Bell-local (`CHSHmax=0.7`).

Every event uses typed lineage ports `(lineage,parent,content,outcome)`, plus event type and RN likelihood-block identifier. An atomic joint seal is one multi-port common-cause event, not simultaneous distant events. Its descendants inherit local records through their respective ports.

Incident supports are synchronized only through a lineage-local predictable compensator: each support has a unit Poisson process evaluated at its accumulated typed evidence. A global priority queue is one simulation of these local point processes. For disjoint events its relative order is discarded; for overlapping events the shared lineage records parentage. If future compensator increments are predictable and independent of the support clock's future Poisson increments, then conditional on `Delta I` the renewal survival is `exp(-Delta I)`. If the increment remains random, the marginal is `E exp(-Delta I)`, not `exp(-E Delta I)`; the paper makes no stronger claim.

`cg8` integrates a complete finite trace: a common-cause root, two local setting/seal events, outcomes, a conservative joint transfer, explicit RN block IDs, parentage, and a renewed private seal. An unequal-rate priority-queue scheduler and a direct trace scheduler push forward to the identical exact distribution on eight canonical marked histories (total mass one).

This construction remains conditional on the support/exposure process and is classical.

## 3. Marked covariance, restriction, and support bootstrap

Bare causet stems forget exactly the new ontology. The amended finite object is a marked history. `cg5` canonicalizes it under both event and lineage permutations. Disjoint `AB/BA` presentations give one canonical history; overlapping `AJ/JA` give different histories because parentage differs. Event-based transport `(4,2)->(3,3)` is conservative and sealed into the mark. Two histories can share the same bare parent-order code while differing in content marks (`23/16` versus `5/4`), proving why unmarked stems were insufficient.

The round-2 review found and the final receipt repaired a real covariance bug: lineage-owned outcomes now transform in the same typed port as their parent/content marks. The regression history with `(content,outcome)=(3,5;0,1)` versus `(5,3;1,0)` canonicalizes identically after lineage exchange.

The restriction functor projects ports to retained lineages, discards empty events, reconnects same-lineage parents, and retains a `projected-joint` type plus the joint block ID for boundary-crossing events. In `cg8`, restriction commutes with the two scheduler presentations and composes exactly on a three-lineage extension. The induced finite-family law is defined by pushforward through these maps.

This is finite isomorphism covariance and a finite marked restriction system, not yet a marked profinite Stone spectrum. Rational/real marks require finite observable partitions at each resolution or a different compact marked topology. Paper 7's finite-alphabet covtree theorem is not imported.

**No-bootstrap theorem.** If every newly licensed support is contained in one connected component of the existing support hypergraph, connected components can never merge. Proof: subset addition adds no edge across a component partition; induction over support births. Therefore interaction across all descendants requires either a connected boundary seed or a branching event that records a common ancestor before the descendants separate. The receipt implements the latter and explicitly leaves the root/branch law as input.

## 4. RN/KL evidence and exact renewal scope

For evidence, the correct identity is the conditional RN chain rule. If forward and reverse laws factor into conditional blocks,

`dP/dQ = product_j dP_j(.|past)/dQ_j(.|past)`,

then

`D(P||Q)=sum_j E_P D(P_j(.|past)||Q_j(.|past))`.

Shared data appears once as a joint-support block. Pure correlation can have zero marginal KL and positive joint KL; duplicating one shared observation doubles its evidence. `cg9` constructs explicit blocks with `P=(1,0)`, `Q=(exp(-d),1-exp(-d))`, hence exact KL `d`, and realizes both nonunique models below inside the licensed RN class.

The recurrent theorem is conditional: for independent unit Poisson support processes with predictable compensators, the random-time-change/independent-increment property gives `P(no firing | F_tau, realized Delta I)=exp(-Delta I)` after a finite stopping history. Exposure generation itself remains an input. Local nonexplosion holds when every finite restriction has finite total incident compensator; no global nonexplosion theorem for arbitrary branching is claimed.

## 5. Underdetermination theorem

**Theorem 5.1 (current principles do not select the joint law).** Fix two lineages with total incident evidences `I_A,I_B`. For every `c` in `(0,min(I_A,I_B))`, take private evidence allocations `a=I_A-c`, `b=I_B-c` and one shared support exposure `c`. Then

`S_A=exp(-I_A), S_B=exp(-I_B)`

for every `c`, construction quotient and renewal identities are unchanged, and the shared support is local relative to the same recorded ancestry. But

`S_AB=exp(-(I_A+I_B-c))`

and hence the joint covariance varies strictly with `c`. Therefore exact click marginals, finite refinement/restriction, construction quotient, causal-sufficiency form, and support locality do not select `c` within this classical support family. Separately, any rational conservative transfer fraction `g in [0,1]` preserves total content and the click marginal while changing later marked contents. Thus the tested interaction law contains at least two independent unselected continuous parameters; in the general version these become kernels. ∎

The receipt instance at `I_A=1.1,I_B=0.9` gives covariance `0.0299636` at `c=0.2` and `0.1371965` at `c=0.7`; `g=0.1/0.3` maps `(4,2)` to `(3.6,2.4)/(2.8,3.2)`.

**Corollary 5.2.** No theorem from the current v7 marginal plus the listed finite classical gauge/locality/no-signaling/conservation constraints can produce a unique member of this support family. A selection principle must determine at least the shared likelihood allocation and transfer kernel. Additional full SHARD structure could in principle select them; no such selector is supplied here.

`cg9` strengthens the witness: the two `c` values are realized by explicit forward/reverse likelihood blocks, not abstract hazards, and use the same declared outcome module and conservative transfer. Analytically taking the product with the Bell-local kernel already certified in `cg4` leaves the RN nonuniqueness unchanged.

## 6. Receipts and review record

First campaign (historical diagnostics): `cg1` 6/6 exact, `cg2` 5/5 at `dps=120`, `cg3` 4/4 exact. Hostile round 1 reproduced all arithmetic and refused promotion because the modules were not integrated and the gauge definition was too strong.

Round-2 openings: `cg4` 6/6, `cg5` now 7/7 after the referee-found typed-outcome correction, `cg6` 6/6, `cg7` 5/5. Hostile round 2 accepted the underdetermination direction but found the marked-port bug, shallow projective test, missing end-to-end trace, and abstract likelihood witness.

Final openings: `cg8` 4/4 exact (end-to-end trace, scheduler pushforward, cross-boundary restriction, functor composition); `cg9` 4/4 at `dps=120` (explicit RN models, compensator scope, common outcome/transfer modules). Cancellation-sensitive residuals are `1e-121` class. These values certify arithmetic identities and implementation wiring, not physical truth.

## 7. Final status

What now exists is a normalized finite-restriction, quotient-covariant, H-local classical marked process template with exact conditional exponential renewal, integrated local-common-cause outcomes, event-based conservation, finite marked restriction consistency, and explicit RN/KL typing.

What does not exist is a unique or quantum-complete final law. The support seed/branch rule, actual likelihood blocks, shared allocation, transfer fraction, outcome instrument, and quantum correlation structure remain inputs. Continuous diffusion and cone geometry are downstream effective questions and are not used to certify the law.

The correct headline is therefore:

> **Conditional on a covariant support/exposure process, a finite gauge-local classical recurrent click family exists; current record principles do not select its coupling.**

No quantum/entanglement result, proper time, relativistic locality theorem, marked profinite completion, global nonexplosion result, 3+1 geometry, or absolute scale is claimed.
