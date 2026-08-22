# Paper 23a v2 blind review — Seat P (probability/multiplicity)

Date: 2026-08-22

Reviewer seat: probability, orbit pushforward, multiplicity descent.
Repo read-only; produced solely from the v2 pin (#315), the candidate
(#316, SHA-256
`c4503bd309bcc54f0c20de2d8f1a28b4b4742c02c5f9eb7d7b2918deb5889209`),
the construction note
(`26d2134a839f79905a0374690df6592412fc1c30352a7cac81bd3103c3ce2085`),
terminal Paper 13D, and the #314 adjudication. No other v2 seat's
report seen.

Verdict: **ACCEPT-WITH-FIXES**

Stage 2 survives with two repairs. One finding is new; one is a
presentational gap.

## F-P2.1 (MAJOR) — The composite-class mass sentence in §3 is unproved

Defect. §3's final sentences state that composite classes "inherit
masses by the same descent — e.g. $[\Phi_2(1)]$ carries the joint law
of (tensor source, fused target) pairs … its total mass is $1$ by
normalization of the fusion kernel." As printed this is an assertion,
not a descent statement: Theorem B covers congruent complexes, but
nothing in §3 shows the composite's cell partition or that its
printed description ("joint law of pairs") matches the orbit-summed
masses rather than labeled masses. The sentence is true in substance
(orbit pushforward normalizes, Paper 13D §9.1), but stage 2's
discipline requires the orbit-sum statement, not a kernel-level one.

Replacement sentences, verbatim:

> New under trace sensitivity: the composite classes above descend by
> the same Theorem B — their congruence classes are fixed (Prop B of
> §2), and their physical masses are the full-orbit sums of their
> presented laws. In particular $[\Phi_2(1)]$ has as its complete
> reader the identity on the (tensor source, fused target) outcome
> fiber, and its total mass is the stabilizer-orbit sum of a
> normalized presented law, hence exactly $1$ (Paper 13D §9.1);
> representative mass is nowhere used.

## F-P2.2 (MINOR) — §3's chain-collapse remark should not assert uniqueness of the chain

Defect. "on the certified fixtures each class is a single
family-size-sort-trace cell, so chains collapse" — the intended
statement is that congruence classes restrict to single fixtures, so
no nontrivial chain has distinct endpoints within one class. As
worded it could be misread as a claim that congruence chains are
unique.

Replacement sentence, verbatim:

> on the certified fixtures each congruence class consists of exactly
> one family-size-sort-trace cell, so no nontrivial chain has
> distinct endpoints inside a class, and the chain clause is available
> though never needed there;

## Mandatory regressions

- Control 3: orbit sizes excluded from any multiplicity talk; fixed
  points inside orbits. PASS.
- Control 14: full-orbit sums everywhere; F-P2.1's repair strengthens
  this. PASS.
- Controls 15, 16, 17: out of mandate; the FP closure of §4.2 is
  consistent with this seat's findings. Noted.
- Controls 19–22: out of mandate; no rescue quotient seen in §3.

## Independent verification performed

Exact rationals, rebuilt independently: β/κ censuses; B²; 16
reachable packets; U(1) 128 traces / 96 cells / 64 fixed / six
masses; D∘Q⁰(1) 256 / 192 / 128 / eight masses — all matching the
candidate elementwise; endpoint conditional B²; bond marginal ½;
three-pair pattern uniform; set-level orbit count 2176; the
$16\times4\times2=128$ census sentence now correct. Verified the six
#314 replacements appear verbatim in §2/§3. One new check: the
composite $[\Phi_2(1)]$'s presented law normalizes (fusion kernel
normalization over the fresh cross-bond seed), supporting the
repaired sentence.

## Verdict

ACCEPT-WITH-FIXES: apply F-P2.1, F-P2.2 verbatim. Stage 2 then stands
as printed at its declared fixture scope. Stage 3's categorical and
algebraic clauses fall outside this seat's mandate; no defect seen
from the probability side.
