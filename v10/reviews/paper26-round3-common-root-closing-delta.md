# Paper 26 round 3 — common-root closing delta

**Frozen target:** `9f50a8a` (`Make Paper 26 shared lines restriction-natural`).
**Review mode:** three independent lanes; audit only; no reviewer edits.
**Aggregate verdict:** `0B/1M/1m/0n`.
**Promotion:** withheld for a two-line corpus repair only.  The executable,
probability, countable-core and D26/D36 evidence repairs close cleanly.

## 1. Independent lane verdicts

```text
probability / countable core   scientific PASS; stale-note census/text only
hostile causal evidence        0B / 0M / 0m / 0n
paper / corpus conformance     0B / 1M / 1m / 0n
```

The aggregate uses the corpus lane's severity assignments.  The probability
lane classified the same two local note defects more lightly; it found no
additional issue.

## 2. Common-root repair closes the prior blocker

The prior frozen target `e66cc1e` silently ordered same-line opportunities by
`cell.vertices`.  Commit `9f50a8a` removes that order.  Every declared line
has one canonical `PARENT_LINE_ROOT(ell)`, and every proposal-specific
`OPPORTUNITY_PARENT(v)` has the matching root as its sole parent.

Independent attacks establish:

- all seven nonempty subregions of a three-opportunity shared line restrict
  event-for-event to independent local realizations;
- all six declaration permutations produce one identical full DAG;
- 875 restriction comparisons and 750 declaration-permutation comparisons
  over 125 three-line states pass;
- all seven tested shared-line interface relabelings commute;
- missing, foreign, extra, retargeted and cross-line roots reject; and
- the countable core uses injective canonical IDs and needs no line
  enumeration.

The finite imported D36b append adapter remains separate from the countable
identity theorem, as stated.

## 3. D26 and D36 evidence

D26's same-parent newborn maps commute for every tested ordering of three
heterogeneous couplings.  For three `g=9/25` births the traced parent coherence
factor is exactly `64/125`.  The common-root DAG therefore supports the
commuting-child product without selecting a transaction order.

All 192 registered D36 prepares (`10+6+20+156`) reconstruct as locked D36b
`Record`/`Envelope` objects and pass `participant_accepts_prepare()`.  Fresh
signature, capability, attempt and evidence mutations reject.

## 4. Probability and fail-closed controls

The receipt remains `PASS 9/9`.  The independent feasible-addition census is

```text
pair 2 + path 5 + triangle 3 + path5 20 = 30 distinct edges,
```

all with exact quotient two.  Decrementing the S0, S2, S7 or S8 evidence
counters makes the corresponding gate fail.

Fresh seeds `0`, `3`, `65537`, `271828`, `314159`, `1000003` and randomized
hashing reproduce byte-identically.  Frozen hashes are:

```text
source    b15e577bfdf03e1bc78628d9d934bab1e604da9f4b62f7c6372fa61dca7fcbd9
stdout    df5aa182d432206642ed3440d8d0b7f4cc9e971bd2d014811b9fea9e47391c16
science   82a2dac6a1f9c5352ea05309b1ae24f38098924c5be595f5b6dfb49960fdf126
complete  20d4b2f6add6db3296f221c184be539dd62c66ada81f32418b9288bebf778ed8
D36b      57ff22ab4711b63d476192c2ff19b02bb7f76fda5124b4d1afd23d30a20b376b
```

## 5. Remaining corpus repair

The D37 note alone retains two stale statements:

1. it reports 140 K1 typed events instead of the current 158; and
2. it describes the deleted sequential same-line chain and causal
   comparability instead of common-root sibling opportunity parents and the
   commuting-child product.

Paper 26, README, the executable, receipt and latest ledger entry already use
the correct common-root account and counts.  Authorship must repair those two
note passages and obtain a string-only closing delta before promotion.
