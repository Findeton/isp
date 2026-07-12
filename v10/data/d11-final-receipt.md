# D11 final receipt

**Date:** 2026-07-11  
**Final verdict:** `INCOMPLETE-PACKET`  
**Hostile closure:** unanimous PASS at the narrowed verdict scope.

## Reproduction

Exact:

```text
python3 v10/code/d11_complete_bloch_lorentz_exact.py
python3 -O v10/code/d11_complete_bloch_lorentz_exact.py
```

Both succeed and are byte-identical:

```text
checks=73
stdout_sha256=639154ac73e65adb1b528a2bc1d5f6fa1dc4ffc1bc8a1e94bb643742891021f4
semantic_receipt=c45eea0b4d50ec1644627a722bfa6f010f238ae581f66391eba7aeff4c32b62e
```

Numerical:

```text
/Users/felixrobles/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 \
  v10/code/d11_generated_history_geometry.py
```

Two independent rebuild runs are byte-identical:

```text
stdout_sha256=56f5a51f928a1e26441455b5bbb996ac3c35ba911529a6d735ba27d0640e8ee9
semantic_receipt=f1ab9e04caa42f200c3af53adb295d8f78d547178d0b67fff0bcffd9af547224
```

## Exact result

```text
dual_sl2c_born_gauge=TEMPLATE_PASS_NOT_INTEGRATED_HISTORY
split_sibling_merge_terminal_seal_instruments=PASS
typed_complete_next_history_kernel=PASS
disjoint_split_state_probability_commutation=PASS_ONE_CELL
canonical_projective_pushforward=OPEN
decentralized_local_click_law=OPEN
ancestry_subset_positive_cone=PASS
naive_join_negative_control=FIRED
pairwise_positivity_equals_influence=FALSE
cone_containment_is_construction_theorem=YES
equal_activity_population=A_S_EXTINCTION_THEOREM
```

Typed durable outcomes carry rule/value-paired input-domain effects:
`K_g^dagger K_g=I/2` for SPLIT, `P_b` for terminal SEAL, and the 4-by-4
`J_b^dagger J_b` for sibling-MERGE. A separate exact gate reconstructs their
Born weights. Tokens store actual matrices. Merge outputs store both parent
ports and anchor frame data.

## Population theorem

For `p>0` open ports and `j` enabled sibling merges, `0<=j<=p/2` and

```text
Pr(up|H)=p/(2p+j)
Pr(down|H)=(p+j)/(2p+j)
E[Delta p|H]=-j/(2p+j)<=0
```

The total terminal-SEAL probability is at least `2/5`; root immediate
extinction is exactly `1/2`. Optional stopping plus the bounded-region seal-run
argument proves almost-sure extinction.

## Frozen numerical result

```text
cutoff  reached  terminal  median_clicks  max_clicks  merge_seal_influence  rank4
512     0/24     24/24     1              49          1/24                  3/24
1024    0/24     24/24     3              171         4/24                  5/24
2048    0/24     24/24     1              47          5/24                  4/24

ancestry_edge_violations=0
influence_cone_violations=0
median_support=-1.0000,-0.8515625,-1.0000
valid_generated_F_dom=1,3,1
valid_generated_F_m4=1,0,0
M4_time_axis_valid=24/24,24/24,24/24
M4_time_axis_means=1.085537373230,1.079347373771,1.078453579417
M4_diagonal_axis_valid=0/24,0/24,0/24
frozen_registry_verdict=INTERACTION-INERT
mechanism_diagnosis=POPULATION-EXTINCT_INTERACTION-SPARSE
```

No survivor selection, parameter sweep, or imputed shape value is used.

## Final artifact hashes

```text
e66dc317764d1bd19229b98d446165c1ccc2a141b53572419fbc3de3115384dc  code/d11_complete_bloch_lorentz_exact.py
60d7a905158dd9e08b7713b34e67e61a45214e7e7c6ab2e4c9b61979930e7c00  code/d11_generated_history_geometry.py
6672fb35e320ebee70ea1b59d083eb17768c1018e30a5786e31b8980c633035e  note-d11-complete-bloch-lorentz-scir-protocol.md
efad9e513715c4defb0433a9805da127c02b8d8c0bfa4866b2cf5c67c7815bc7  note-d11-complete-bloch-lorentz-scir-investigation.md
5f5587dc0f3f45b0aa165dbbc16d2fb69579c37a2dba4e5871cddc76c7333417  note-d11-literature-audit-complete-packet-and-extinction.md
c2c754b816ceb692ba37b179de9be195ed6dc3731c9416f6d3d94036048e383c  note-d11-round1-opening-repairs.md
044154486930da0ddc0c00aac2bc0fbcb817d370497a68a4db365c5b0675486f  relativistic-isp-v10-paper12-complete-lorentz-rulebook-that-cannot-grow-a-universe.md
```

## Hostile closure

```text
mathematics: PASS
  review d11-round4-mathematics-hostile-review.md
  sha256 b6663f59d501f20735f4e2fbf07a6bb4dbac4f3ed921db949489af4f781c050e

ontology/locality: PASS AT NARROWED INCOMPLETE-PACKET SCOPE
  review d11-round3-ontology-locality-hostile-review.md
  sha256 657caa357d113208498d3b9e79660a39a56df276fbf86e8f3fc67f2ae3649bca

independent rebuild: PASS STRICTLY AT INCOMPLETE-PACKET SCOPE
  review d11-round2-independent-rebuild-hostile-review.md
  sha256 ad2b5ff4ade164d05bba3a9a7a5d7e3b5fab72190bfd70d440771237a072e239
```

## Claim ceiling

D11 is a complete globally normalized finite-prefix kernel with
incidence-scoped exact instruments, a separately proved dual-covariance
template, constructed algebraic cone containment, a real owned sibling
interaction witness, and an almost-sure extinction theorem.

It is not the final interactive record click law. It does not yet provide a
decentralized local event-selection gauge, generated multi-frame histories,
canonical projective pushforward, cross-component bridge birth, finite record
capacity, physical metric scale, or an equality between algebraic and
interventional cones. `SEAL -> COMMIT` is one new primitive candidate, not a
derived law.

