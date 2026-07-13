# D34b repaired round 1 — independent asymptotic/numerical hostile review

**Verdict:** ACCEPT CORE / MAJOR REVISION AT RECEIPT WIDTH. **Count:** 2 MAJOR / 5 MINOR / 2 NIT. No numerical falsification.

Independently confirmed: the killed-chain recurrence; `S_n ~ 16 k0(k0-1)n^-2` for k0>=2 (k0=1 is geometric); local Exp/Erlang tails; orbit weights `1/2304,1/3072,1/3072 -> 5/4608`; physical split `1/16=1/32+1/32`; Yule population/ring means; and statistical adequacy of A6.

## MAJOR

1. The asymptotic was numerically checked, not proved in the commit. Carry the Yule-martingale proof: for m=k0-1 other records, `exp(-t/4)M_t -> W~Gamma(m,1)`; other-ring count is asymptotic to `4W exp(t/4)`; the independent target-act time is Exp(1/2); inversion/dominated convergence gives `16 E[W^2]=16k0(k0-1)`.
2. Timed projectivity and untimed-DAG projectivity were conflated, and frozen R2's complete physical restriction gate was not delivered. Narrow to projective timed laws plus per-T untimed pushforwards; any intrinsic untimed observation restriction is separate.

## MINOR / NIT

- Add an almost-sure nonexplosion proof, not harmonic means alone.
- Replace tautological E6 factorization with the structural disjoint-source theorem plus the pathwise actor coupling.
- Replace A7 absolute bars with exact standard errors and add the negative-binomial population distribution or narrow the claim.
- Scope tie-zero to ideal exponentials; finite 256-bit ties are guarded, not impossible.
- Scope persistence to this static, no-sealing, always-eligible exemplar.
- Call E3's two halves relative-order cylinders; call A1's checker separately implemented, not fully independent.

The construction survives. The delta is about proof carriage and object boundaries, not the law's existence.
