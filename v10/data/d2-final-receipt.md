# D2 final canonical receipt

**Frozen:** 2026-07-11  
**Verdict:** `CONDITIONAL-COMPOSITION + CARRIER-BIRTH-REFUSAL UNDER THE FROZEN
MARKED-SUPPORT-SKELETON AXIOMS`.  
**Accepted scope:** exact finite marked support incidence.

## Source hashes (SHA-256)

```text
bf8e9a749dc961978263fb787ac059567467890f204d5a9b1e39bf94235300e8  v10/code/d2_marked_diamond_amalgamation_exact.py
edd7c62e5424ed4143f219432758489f2c1bf40f9310fd9b82d88f6cd82975a1  v10/note-d2-primitive-carrier-amalgamation.md
fcdbd17dc7abdbd9a272749e27b8dd5c8b65a73c186722cb9e302acdf49240bd  v10/relativistic-isp-v10-paper3-diamond-amalgamation-is-composition-not-carrier-birth.md
```

## Execution

```bash
PYTHONDONTWRITEBYTECODE=1 \
  python3 v10/code/d2_marked_diamond_amalgamation_exact.py
```

Result:

```text
RECEIPT: 33/33 exact checks passed
```

Two final runs were byte-identical. Canonical stdout hash:

```text
4163c3be7450c2510d62ebe241011c8c96e098b3be7f9e083d561c2c1fa27559  D2 stdout
```

## Final theorem boundary

1. In the explicit category of finite marked support skeletons and weak
   mark-preserving support homomorphisms, a supplied span with injective legs
   has a support-conserving pushout, unique up to marked isomorphism.
2. True compatible iterated pushouts are construction-order gauge.
3. Pushout composition does not create a primitive support across exclusive
   records, and its universal property does not select its own interface legs.
4. On pair-support graphs, strong restriction naturality plus extensivity,
   deterministic covariance, idempotence, and edgeless two-record refusal
   force the identity closure; the structural proof extends to every finite
   vertex set.
5. Higher-support fill remains nonunique: intersection projection leaves two
   laws; contained-event projection leaves larger families.
6. Deterministic covariance cannot select one pair from a transitive
   three-port orbit. Uniform stochastic `1/3` selection is covariant but fails
   strong restriction against edgeless-pair refusal.
7. If a full variable-history path measure is primitive, its conditional law
   already supplies `Ext_mu(H)` and the carrier marginal. D2 addresses only the
   stronger derivation program.
8. No theorem for full probability, collar, source, transport, holonomy,
   continuum, or profinite gluing is claimed.

## Independent hostile closure

- `reviews/d2-round2-mathematics-hostile-review.md` — final PASS;
- `reviews/d2-round2-independent-rebuild-hostile-review.md` — final PASS;
- `reviews/d2-round2-ontology-locality-hostile-review.md` — final PASS.

Round-1 major reviews and their disposition ledger remain preserved in
`v10/reviews/`.
