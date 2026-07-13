# D34c round 1 — independent quantum mathematics hostile review

**Target:** commit `9f92a95`. **Verdict:** MAJOR REVISION. **Count:** 0 BLOCKER / 3 MAJOR / 3 MINOR / 1 NIT.

Both fresh salted reruns reproduced 10/10 and SHA-256 `f3a5aa379e857370a35d794db67d8af1da7bf980fc342fab83b54020037389db`. Independent derivation confirmed the four-qubit formula, spectrum `{1/4 x4,0 x4}`, interference law, `8->4->2` restriction, Busch block-norm identity, and exact `Q(sqrt(2))` implementation.

## Major findings

1. **C8 is a product witness, not actor/history sewing.** Its vectors are exactly `sqrt(w_k)|k> tensor |psi_alpha>` and the depth-two analog. Thus `D_comb=diag(w) tensor D_diamond`; the checked `k_ops` never enter the combined branches.
2. **“Every finite D34b cylinder” is unreceipted.** Only one/two iid kind words appear. Targets, degree, Ulam birth, passive reception, actor identities/state, clocks, placement, physical DAGs and quantum remote factorization are absent.
3. **The path-record receiver is imposed rather than built.** C3 zeros `p!=p'` entries manually. Construct an explicit receiver/copy isometry and recover the masked Gram matrix independently.

Minor: rank is incremented rather than computed; the C8 off-diagonal gate is weak; C0 is a declaration, not a substantive gate. NIT: remove unused helpers.

**Surviving noun:** exact diamond + abstract finite Busch/NSE lift + spectator product compatibility. Dynamic D34b actor/quantum sewing remains unproved.
