# Paper 23a blind review — Seat P (probability/multiplicity)

Date: 2026-08-22

Reviewer seat: probability, orbit pushforward, and multiplicity
descent. Repo read-only; produced solely from the frozen pin (#309),
the candidate (#310, SHA-256
`9cab8d2e78ee5365b0facc86ff059074f482091bbb3621cfd328939b9e247a5a`,
606 LF), the construction note
(`cc157c793cca620b680dca1d93b83a6726dee1e3b7e044647a9cffde889ea10c`),
and terminal Paper 13D (`3b91766f…`). No other seat's report seen.

Verdict: **ACCEPT-WITH-FIXES**

Stage 2 is the seat's mandate; it survives with one definitional
repair and two presentational corrections. The seat also records, as
out-of-mandate observations, that stage 3's class identifications
appear inconsistent with the candidate's own Proposition A.2 — those
belong to the category and fusion seats.

## F-P1 (MAJOR) — Definition 3.1 descent is asserted, not proved, for non-aligning congruent complexes

Defect. Theorem B's proof handles complexes aligned by a single $g$
and shows the descended data agree. But the congruence $\sim$ is the
transitive closure of such alignments: $\chi\sim\chi'$ may hold
through a chain $\chi=\chi_0\sim\chi_1\sim\cdots\sim\chi_k=\chi'$
with *no single* aligning morphism between the endpoints. The proof
of constancy on classes covers only $k\le1$. On the certified
fixtures the defect is latent (each family/size/sort contributes one
class, so chains collapse), but as printed the theorem overstates its
proof.

Replacement sentences for Theorem B's proof, verbatim:

> If $\chi\sim\chi'$ are aligned by $g$, transport by $g$ maps
> presented histories of $\chi$ bijectively onto presented histories
> of $\chi'$ (equivariance of every kernel, Thm 2 of Paper 13D), maps
> stabilizers onto stabilizers, hence orbits onto orbits, and
> preserves each labeled probability because $g$ carries the entire
> seed product (public bits fair, private $\eta$'s, uniforms, and
> cross-pair seeds) onto an identically distributed product.
> Therefore $M_{\chi'}(g[H])=M_\chi([H])$ for every cell, and the
> descended data are invariant under precomposition with the
> stabilizer. For a general chain
> $\chi=\chi_0\sim\chi_1\sim\cdots\sim\chi_k=\chi'$, apply this
> argument to each adjacent pair and compose; on the certified
> fixtures every class is a single family-size-sort cell, so the
> chain argument is available though never needed there.

## F-P2 (MODERATE) — §3.2 arithmetic sentence is false as printed

Defect. "the labeled support has $2^7\times 625=128$ positive
traces" is arithmetically false ($2^7\times625=8000$) and miscounts
the support. Correct census: sixteen source tuples $(q_0,h,c,e^0)$;
for each, four packets are compatible (the packet is a function of
$(c;\eta_X,\eta_Y,e^0)$, and $(c,e^0)$ fixes two of its four free
inputs, leaving $2^2=4$); two endpoint values $q_2$. Hence
$16\times4\times2=128$ positive traces over $16\times625$ seed
combinations.

Replacement sentence, verbatim:

> the labeled support has $16\times4\times2=128$ positive traces
> (sixteen source tuples, four packets compatible with each
> $(c,e^0)$, two endpoints), drawn from $16\times625$ seed
> combinations, and normalization is exact.

## F-P3 (MODERATE) — The endpoint-class mass formula needs its hypothesis printed

Defect. The formula $M([\mathrm{DQ}(n)])(q_2{=}j)=\frac12\sum_a
B^2_{ja}=\frac12$ uses symmetry of $B^2$ and the fair $q_0$ source
marginal; neither hypothesis is stated. Also "endpoint-sector data"
is not a defined object; the masses are complete-reader pushforwards
of the descended cell masses onto the $q_2$ coordinate.

Replacement sentences, verbatim:

> The descended **complete-reader $q_2$-pushforward** of
> $[\mathrm{DQ}(n)]$: the fair source marginal of $q_0$ and the
> column symmetry $B^2_{j0}=B^2_{j1}$ give
> $$M\bigl([\mathrm{DQ}(n)]\bigr)(q_2{=}j)
> =\sum_a \tfrac12\,B^2_{ja}=\tfrac12 .$$

## F-P4 (MINOR) — Theorem B's final clause should name the alignment-independence mechanism

Replacement sentence, verbatim:

> Two alignings of the same pair differ by a stabilizer translate of
> either complex, under which every orbit and every orbit sum is
> fixed pointwise; the descended data therefore do not depend on the
> chosen alignment.

## Mandatory regressions (controls 3, 14, 15, 16, 17)

- Control 3: automorphism orbit sizes never enter $N$; fixed points
  retained inside orbits with actual multiplicity (Def 3.1, §4.1).
  The $n=1$ tables confirm: 64 and 128 fixed traces are inside, not
  identified with, their cells. PASS.
- Control 14: every printed mass is a full-orbit sum; no
  representative mass appears. PASS.
- Control 15: out of mandate; the semiring assertion belongs to the
  fusion seat. Not assessed.
- Control 16: out of mandate; not assessed.
- Control 17: out of mandate; Cor E.1's wall is noted as consistent
  with this seat's findings. PASS as far as seen.

## Independent verification performed (exact rational arithmetic)

From Paper 13D §§6–7, rebuilt independently: β and κ censuses
reproduce $B$, $C$; $B^2$ recomputed; 16 reachable packets at $n=1$;
$U_{\varnothing}(1)$: 128 labeled traces, 96 cells, 64 swap-fixed,
distinct masses {3969/6250000 ×16, 784/390625 ×16, 882/390625 ×16,
2916/390625 ×16, 9216/390625 ×16, 10368/390625 ×16}, total 1 —
matches the candidate's table exactly;
$D\circ Q^0_{\varnothing}(1)$: 256 traces, 192 cells, 128 fixed,
distinct masses {6561/6250000 ×16, 729/390625 ×32, 1296/390625 ×32,
1458/390625 ×16, 2304/390625 ×32, 2592/390625 ×32, 4096/390625 ×16,
4608/390625 ×16}, total 1 — matches; endpoint conditional $B^2$
entrywise; $P(\ell_{ij}{=}1)=1/2$;
$P(\ell_{12}{=}i,\ell_{13}{=}j)=1/4$ uniform; set-level orbit count
2176. One additional check the candidate omits and this seat supplies
as context: at $n=2$ the primitive's bond field is absent at the
source sort, so the $U(2)$ orbit census is the product of two
independent $n=1$ packets' orbits under the $C_2\wr S_2$ stabilizer
— no new phenomenon; the printed all-size endpoint masses
$\tfrac12,\tfrac12$ follow from symmetry alone and are exact at
every $n$.

## Verdict

ACCEPT-WITH-FIXES: apply F-P1, F-P2, F-P3, F-P4 verbatim. Stage 2's
definitions, theorem, and tables then stand as printed at their
declared fixture scope. This seat does not assess stage 3's
classification; its concerns (recorded above as observations) are
referred to the category and fusion seats.
