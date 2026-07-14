# Paper 22 round 2 — predictive/profinite closing hostile delta

**Frozen target:** commit `8e820cc2464eeefeabafe49ed64246e98d51ce4a`.
**Compared against:** commit `c236a6f` and
`paper22-round1-predictive-profinite-hostile-review.md`.
**Verdict:** **SCIENTIFIC DELTA ACCEPTED; ONE BIBLIOGRAPHIC REPAIR REQUIRED —
0 blockers / 0 majors / 1 minor / 0 nits.**

The repaired code, output, D34e note and Paper 22 close every scientific defect
assigned to this stream.  In particular, the Branch-F selector is now the
remote actor's own-ring ordinal everywhere; the fixed-radius probability
argument still has the advertised exact lower bound and zero branch; the
all-future and stopping claims remain pointwise and correctly inherited; and
the paper distinguishes a sufficient strong refinement from the open minimal
weak/timed quotient.  The finite profinite calculation is not promoted into a
completed-history theorem.

The only surviving defect is in the new bibliographic metadata.  Reference 3
prints the wrong DOI, and reference 4 prints the wrong issue/pages.  This is a
source-provenance defect, not a theorem defect, but it prevents a clean
terminal stamp on the present commit.

## 1. Frozen artifacts and independent reproduction

The full `c236a6f..8e820cc` delta contains five files and reports
`238 insertions(+), 36 deletions(-)`.  `git diff --check` is clean.  The frozen
artifact hashes reproduce exactly:

```text
paper   1718dce460c5d1711fa3b02fe8424c9a5b4819abb8b9facd0d64abbff14b92ee
note    af3c9b6fdf7590c6a28db93f0e473691b30c00ae921440156a7e48e8cb19a98c
code    1dd1a69be94a0fb614f909745e7db772ac5e5f134b97cbdcdf10c45a08f606c5
stdout  158c491d7376b165556364fee2f0266447e7f5becfdbda5a8f4ae600114e9fb7
```

Fresh executions with `PYTHONHASHSEED=314159,271828,999983` all exit zero,
print `13/13`, and reproduce internal digest

```text
9f9cea1886db0c889677fdb735b8cb9fc76ae4d2ba18b501242f58331795e017.
```

The `999983` stdout is byte-identical to the committed output.  The reproduced
high-value counts are:

```text
reachable levels                 1,6,40,304,2576
cumulative states                2,927
strong classes H=1,2,3           111,111,111
synthetic classes                106,110,110
B3 updates                       35,898
disjoint swaps                   120,276
regional compositions           159,734
malformed messages rejected      9/9
radius lower bounds              1/24,1/1024,1/64000,1/5308416
moving-tip attacks               16/16
unmarked classes depth 3/4       4/10
quantum                          REFUSAL
```

Commands used included:

```text
git diff --stat c236a6f..8e820cc
git diff --check c236a6f..8e820cc
git diff c236a6f..8e820cc -- v10/
shasum -a 256 <paper> <note> <code> <stdout>
env PYTHONHASHSEED=<salt> python3 v10/code/d34e_predictive_boundary_exact.py
cmp -s <fresh-output> v10/data/d34e_predictive_boundary_exact.out
rg -n -i 'wire.{0,20}ordinal|ordinal.{0,20}wire|own-ring|D#r|pre-stop' <artifacts>
```

## 2. Own-ring versus wire position — round-1 m1 closed

The code selects

```text
pre_stop_ordinal = state["actors"][D]["ring"]
selected_id = f"{D}#r{pre_stop_ordinal}".
```

Paper, note, code and stdout now consistently call this D's **own-ring
ordinal**.  The note explicitly warns that passive incoming records can make
the wire position differ.  No live “D-wire ordinal” occurrence remains in the
four target artifacts.  The terminology now matches both the event identifier
and the executable selector.

## 3. Fixed-radius probability and event scope — pass

I re-attacked the theorem by separating the conditioning past, selected event,
forced future cylinder and timed completion factor.

For radius `r`, the construction has `r+3` active actors during inward
propagation.  Each of the `r+1` required rings must choose one specified actor
and then one specified degree-two interaction.  Hence every factor is

```text
(1/(r+3)) * (1/(4*2)) = 1/(8(r+3)),
```

and the exact embedded subcylinder mass is

```text
p_r = [1/(8(r+3))]^(r+1).
```

This is correctly described as a lower bound for the broader event, not as its
total probability.  In the idle past the selected immutable `D#r_k` event has
kind idle and the common inward chain imports it into A ancestry.  In the
interaction past that same event identifier already has immutable kind
interaction, so the event requiring idle has exact probability zero.  Later
idles, interactions, unrelated A events and repeated D events cannot rewrite
that selected record; the registered `16/16` interloper battery confirms the
intended moving-tip attack.

For a finite elapsed window, multiplying this embedded mass by the
`Erlang(r+1, rate=r+3)` completion CDF is a valid positive subcylinder lower
bound.  The paper says exactly that and does not confuse it with the complete
timed event probability.  The two conditioning pasts remain positive
cylinders and have identical complete radius carriers because D is at distance
`r+1` and outside predecessors remain genuinely opaque.

## 4. Pointwise, all-future and stopping scope — pass

Theorem 1 is explicitly pointwise on every legal finite D34b generator state.
The proof is the arbitrary-state five-row partition, not extrapolation from
the depth-four census.  Its boundary rate

```text
q(c,h) = 1 + d_A/4 + sum_k n_k/(4k) <= 1 + d_A/2
```

is used only as the relevant projected jump intensity.  D34b's inherited Yule
nonexplosion gives the all-future pure-jump law, and the monotone A-own and
A-wire counters give the two licensed local hitting stops.  Fixed construction
time, A-own-ring stops and A-wire-event stops remain distinct; future times are
elapsed from the stop under common time-translation gauge.  No statement is
made for global embedded-depth stopping.

The component ceiling is likewise limited to continuous construction time and
component-local stops.  Since the law cannot join disconnected components,
the independent component factorization is sufficient.  The paper does not
claim component necessity.

## 5. Sufficient carrier, predictive quotient and profinite ceiling — pass

The finite `111,111,111` census is accurately named a strong boundary-
transition bisimulation refinement.  Silent neighbor births are internal
transitions rather than A-wire observations.  The paper explicitly leaves
elimination of arbitrarily many such events, the canonical weak/timed observed-
process quotient, a bounded physical alternative and minimality open.  Thus
“behavioral state” in the abstract does not upgrade B3 into a proved minimal
causal state; sections 1 and 10 immediately separate quotient, carrier and
complete history.

The finite mark-forgetting identity also remains exactly scoped:

```text
(u_3 o r_(4->3))_* mu_4 = (u_3)_* mu_3.
```

Labeled committed-prefix truncation occurs before forgetting marks.  The paper
does not invent an unmarked `4 -> 3` map, a completed marked-history map, a v9
stem-spectrum posterior, or a posterior screening factorization.  The
profinite and quantum branches therefore remain honest refusals beyond their
finite domains.

The paper-level provenance chain is also accurate: terminal D34e note and
three closing reviews at `d10ca52`, repaired executable/output at `6e6676b`,
and the present validator hardening still labeled a candidate awaiting closing
delta.  The strengthened validator's claimed checks match the implementation:
event-ID ownership/ordinals, predecessor visibility and acyclicity, actor
counters, carrier parity, degree/ports, wire counts and maximal visible tips.

## 6. MINOR finding

### m1 — two new bibliography fields are false

The body now places references [3]–[5] at the claims they contextualize and
carefully avoids attributing SHARD results to those papers.  That closes the
round-1 citation-placement defect.  But two new metadata strings are wrong:

1. Shalizi and Crutchfield, *Computational Mechanics: Pattern and Prediction,
   Structure and Simplicity*, has DOI
   `10.1023/A:1010388907793`, not the printed
   `10.1023/A:1010148903217`.
2. Geiger and Temmel, *Lumpings of Markov Chains, Entropy Rate Preservation,
   and Higher-Order Lumpability*, is **Journal of Applied Probability 51(4),
   1114–1132 (2014)**, not `51A, 368–388`.  The printed DOI
   `10.1239/jap/1421763331` is correct.

The first paper's title, journal, volume and pages are otherwise correct.  The
Pollock et al. entry is correct.  The Geiger–Temmel metadata is independently
confirmed by the publisher's DOI record:
`https://doi.org/10.1239/jap/1421763331`.

**Required repair:** correct those two reference entries.  No theorem, code,
output, hash-pinned receipt or note result needs to change.

## 7. Exact terminal recommendation

Do **not** terminal-stamp commit `8e820cc` because its claimed provenance
metadata contains two factual errors.  Make the two-line bibliography repair,
record the resulting manuscript hash and run a narrow source-only closing
delta.  The executable need not be regenerated if code and output remain
byte-identical.

Subject to that repair, this stream recommends terminal acceptance at the
following exact ceiling:

> Paper 22 proves a pointwise, all-future sufficient distributed B3 carrier for
> the chosen passive C/L law at fixed-time and licensed local count stops;
> proves that this realization has unbounded width; excludes every complete
> fixed-radius carrier for full durable ancestry using the own-ring-selected
> positive-cylinder event; and retains the whole connected component only as a
> sufficient ceiling.  Minimal weak/timed prediction, a bounded alternative,
> the adaptive ancestry frontier, the completed profinite bridge and the timed
> controlled quantum lift remain open.

**Final count: 0B / 0M / 1m / 0n.**
