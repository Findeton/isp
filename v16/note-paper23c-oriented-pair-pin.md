# Paper 23c oriented-pair side gate pin (Unit C)

Date: 2026-08-22

Status: **PIN FROZEN — construction authorized on these bytes alone**

This is Unit C of the #308 register: one mathematics-only theorem/no-go.
Question: can terminal $\Gamma_D$ derive the **exchangeable oriented
null-realizer pair** consumed by Paper 15's conditional full-pattern
rigidity theorem (§4.8, its "exact open emergence gate" per #239), or
is that pair **provably underdetermined** by $\Gamma_D$? Both outcomes
are wins. This pin freezes before any construction.

## 1. Bound corpus

| object | ordinary SHA-256 |
|---|---|
| Paper 13D (sole physical source) | `3b91766fe269e8145766f4622f99e9009c3270530670119735e6045a473de5c9` |
| Paper 15 (target contract ONLY) | `254178e18f06fb58eb023c5fa6e33b0165c95356dabd9e7aeba2d968830f14f6` |
| Paper 14 (poset-input provenance record) | `ffc3dca2863bf9f36c9fe62e8dff80628c59c8837b3d96006e449329dee05ec1` |
| #322 correction | `7420231c00d931969344cc7c3d9321a33cd1bf71aa178d3da82a9e8a531d7055` |
| #323 clarification | `7f13dd5de12d2b9106066e167b5877911b0016bf30219d7f2cb0ad5a85737e15` |
| #237 decoder-nonselection wall (PLAN record) | PLAN.md at freeze hash below |

## 2. The target object (from Paper 15 §4.8; contract only)

A **null-realizer pair** for a finite structured occurrence set is an
*ordered* pair $(L_1,L_2)$ of total orders on the carrier such that the
structural dependency relation equals their intersection,
$x\prec y\iff x<_{L_1}y \wedge x<_{L_2}y$ — the two "null ranks" whose
oriented permutation patterns feed Paper 15's rigidity input. The pair
is **exchangeable** when it is taken up to simultaneous presentation
transport and the swap $L_1\leftrightarrow L_2$ (Paper 15's own
$\pi_n$ is invariant under both). The gate asks whether $\Gamma_D$
*derives* such a pair covariantly, or whether the derivation is blocked.

## 3. What may be imported and what may not

Paper 15 supplies **only** the target contract in §2 above: the
definition of the realizer pair and the rigidity theorem's input role.
NOT importable from Paper 15 or anywhere else:

- the Poisson/Palm sampling regime and density calibration;
- the copula family $c_\theta$, decoder class, affine profile, $\phi_*$
  perturbation, or any curvature computation;
- any orientation convention, smoothness axiom, or aesthetic selection
  principle (#237 wall:
  `P15-B-AND-TWO-POINT-ORDER-UNDERDETERMINE-DECODER-AND-CURVATURE`);
- any metric, dimension, chronology, or geometry conclusion;
- Paper 14's dependency poset as physics (it is a structural referent
  only, per Paper 15 §1).

The sole scientific source is terminal Paper 13D
(`3b91766f…`). Its directly load-bearing facts:

- occurrence carriers are arbitrary finite sets (§3.1); no order, no
  coordinates, no metric exists natively;
- the presentation groupoid $\mathcal G$ contains per-occurrence
  $X/Y$ port swaps (§3.1) acting locally, plus global bijections;
- every kernel is $\mathcal G$-equivariant; physical objects are
  stabilizer orbits with pushed-forward masses (§9.1); representative
  mass is forbidden;
- complete histories retain all traversed generator boundaries and
  sorts (§7.1); execution paths form no causal order (§1);
- readers are derived equivariant observables; a naked presentation
  coordinate is not a reader (§9.2);
- the declared native carrier contains no private seed, control phase,
  or history identifier (§12 continuity discussion);
- Exec_D quotients only by symmetric-monoidal axioms, covariance
  equations, and n-ary permutation invariance (§5.2) — no order
  selection equation exists.

## 4. Authorized construction (mathematics only)

Exactly one of:

**(T) Derivation.** Construct, from Paper 13D objects alone, a
presentation-covariant assignment $\widehat e\mapsto[(L_1,L_2)]$ — an
exchangeable oriented null-realizer pair on the occurrence carrier of
every admitted experiment's target — together with proof that the
assignment is (i) well defined under the full stabilizer-orbit
quotient, (ii) equivariant, (iii) non-vacuous (realizes the
intersection condition wherever a dependency relation is even defined),
and (iv) unique in whatever sense is claimed. Any uniqueness claim must
be proved, not assumed.

**(N) Underdetermination.** Prove that no such covariant assignment
exists: exhibit two presented experiments related by admissible
transport (or one experiment with two stabilizer-equivalent
representatives / two admitted reader choices) on which every candidate
assignment either fails covariance, fails the intersection condition,
or splits into distinct values that $\Gamma_D$'s physical quotient does
not separate — so the pair is not derivable from the accepted law.

Hybrid outcomes are allowed but must be stated as exactly one primary
disposition with scope engraved.

No code. Exact arithmetic where arithmetic appears (all constants here
are rational). No new physical postulate; no new generator, sort,
kernel, or quotient; no repair of any frozen artifact; no automatic
successor unit.

## 5. Pre-registered outcomes

Exactly one primary outcome will be earned:

```text
P23C-ORIENTED-PAIR-DERIVED-COVARIANTLY        (outcome T)
P23C-ORIENTED-PAIR-NOT-DERIVABLE              (outcome N)
P23C-ORIENTED-PAIR-GATE-BLOCKED               (hybrid, scope engraved)
```

Sub-coordinates earned as proved: existence/uniqueness clauses as
applicable, each tagged `P23C-*`. No coordinate may be claimed that
depends on smoothness, aesthetics, dimension, metric, chronology, or
any Paper 15 import listed in §3.

**Dimension firewall:** Unit C alone cannot open dimension selection.
The ensemble gate (Unit D territory) remains closed; even outcome T
supplies at most the realizer-pair bridge, never the ensemble battery.
Paper 15's rigidity theorem remains CONDITIONAL regardless of outcome.

## 6. Hostile controls (mandatory regressions)

| # | control | requirement |
|---|---|---|
| 1 | smuggled smoothness | no regularity axiom on any constructed order |
| 2 | smuggled metric | no distance, volume, or conformal factor |
| 3 | representative choice | every construction survives representative change (§9.1) |
| 4 | naked-coordinate reader | any order used must be derived equivariantly, not a presentation coordinate (§9.2) |
| 5 | chronology leakage | derived orders are structural; no causal-order claim (13D §1) |
| 6 | local-swap blindness | constructions must respect per-occurrence $X/Y$ swaps acting locally, not merely globally |
| 7 | Paper 15 import drift | every step traceable to 13D bytes or the §2 contract |
| 8 | vacuous derivation | an assignment defined only where no dependency relation exists earns nothing |
| 9 | uniqueness assumed | any uniqueness clause carries a proof or is not claimed |
| 10 | dimension creep | no cardinality/dimension statement beyond the carrier being finite |

## 7. Scope walls

No channel odds, opportunity/activity/root law, $\Pi_{\rm phys}$,
$\Gamma_{\rm struct}$, actuality, chronology, operational influence,
dimension, signature, metric, curvature, gravity, continuum, or QFT.
Paper 17 gate CLOSED. Paper 22 v3 (`#307`) consumed nowhere. Paper 23a
v2's corrected coordinates (#321–#323) are context, not input. Decoder
nonselection wall #237 respected verbatim.

## 8. Process after this freeze

Construction → three-seat blind review (category/structure seat,
probability/instrument seat, quantum/emergence seat; each blind to the
others, delta format vs the pinned claims) → adjudication → repair if
ordered → terminal disposition. Pins freeze before construction;
hashes before ledger entries; forward-only corrections thereafter.
