# D34f — component tomography and full-ancestry necessity

**Status:** preregistered analytical protocol; no D34f executable, receipt or
result exists at this commit.
**Date:** 2026-07-14.

**Parent:** terminal D34e / Paper 22 at commit `b457d42`.

## 1. Question

D34e proves, for the chosen passive D34b law, that:

- a distributed radius-one star is an exact but unbounded carrier for the
  coarse and role-labeled A-wire queries C/L;
- every complete fixed actor radius fails for the full durable ancestry query
  F; and
- A's complete connected component is a sufficient growing carrier for F.

It leaves component necessity and the proposed adaptive F-frontier open.
D34f tests the stronger analytical conjecture:

> At every legal finite stop, the complete Branch-F future law distinguishes
> every gauge-distinct configuration of A's connected component.  Therefore
> the minimal exact predictive quotient is the whole component history modulo
> gauge and lossless recoding.  No adaptive carrier can discard component
> information and remain exact.

This is not a search for a small frontier.  A smaller exact frontier is the
alternative to be demonstrated by a counterexample if the conjecture fails.

## 2. Frozen law and scope

The history law is exactly the terminal chosen D34b exemplar.

- Every active actor has an independent rate-one Poisson ring process.
- At a ring it births with probability `1/4`, interacts with each current
  neighbor with probability `1/(4d)`, and idles with probability `1/2`.
- Birth creates one fresh Ulam child joined only to its parent.
- Interaction appends one shared event to the initiator and receiver wires.
- Every event stores its initiator-own-ring identifier, kind, target, touched
  actors and the previous tip of each touched wire.
- Events and predecessor links persist.  Adjacency is static after birth.
- The chosen law has no dynamic sealing and no joining of previously
  disconnected components.

The physical seed is the connected edge `A--B`; disconnected product controls
may be added only to test factorization.  Every component reached at a finite
stop is finite by the accepted D34b nonexplosion theorem.

Licensed stops are:

1. fixed construction time;
2. A-own-ring hitting times; and
3. A-wire-event hitting times.

Absolute construction time is gauge.  Future event times are elapsed from the
conditioning stop.  Fixed global event depth is an enumeration device, not a
regional physical clock.

No coefficient, seed, adjacency rule or record operation is derived in D34f.

## 3. Frozen query and state object

Branch F retains the complete typed record of every future event touching A,
including its persistent transitive predecessor ancestry and the elapsed time
of the future A event.

Let `K_A(h)` be the complete current D34b configuration of A's connected
component at past `h`:

```text
actor rows and current tips;
the current birth tree and endpoint incidence;
all persistent typed event records;
all predecessor links.
```

Nominal actor names and auxiliary serialization of incomparable events are
gauge.  The distinguished A role, actor parentage, event kinds, targets,
initiator ordinals, touched wires and predecessor DAG are physical marks.
Write `[K_A(h)]_g` for the resulting rooted marked isomorphism class.

The component contains redundant presentations: current ring/birth counts,
carrier parity, degree and tips may be reconstructible from the persistent
event DAG plus the fixed seed.  “Whole component necessary” will therefore
mean predictive injectivity on `[K_A]_g`, not that every field must be stored
twice or that no lossless code is allowed.

## 4. Returnability definitions

For a pre-stop event `e` in A's component, say that `e` is **F-returnable to
A** if there is a finite positive-probability D34b continuation after which a
future event touching A has `e` in its persistent ancestry.

For an actor `v`, root the current birth tree at A and write `parent_A(v)` for
the neighbor one edge closer to A.  A **component sweep** is any post-order
list containing once, for every `v != A`, the interaction

```text
v -> parent_A(v).
```

Children interact inward before their parent interacts inward.  Sibling order
is nominal and may be chosen canonically only after passing to a rooted marked
representative.

## 5. Theorem targets frozen before proof

### T1 — wire-persistence lemma

Every persistent event touching actor `v` is an ancestor of `v`'s current
wire tip.  Every later event touching `v` retains that ancestry.

### T2 — post-order collection theorem

For every finite legal component, a component sweep makes the final A-touching
event contain every pre-stop event in the component.  Consequently every
component event is F-returnable.

If the component has `n` actors, degrees `d(v)` and `m=n-1` sweep edges, the
exact embedded probability of one fixed post-order sweep in the component
clock is

```text
p_sweep(K) = product_(v != A) 1/[4 n d(v)] > 0.
```

For `Delta>0`, the exact registered timed subcylinder is

```text
p_sweep(K) * ErlangCDF(shape=m, rate=n, Delta) > 0.
```

It is a subcylinder probability, not the total probability that the component
is collected by `Delta`.

### T3 — component reconstruction lemma

For the fixed D34b seed/grammar, the complete persistent marked event DAG
determines the component configuration modulo the declared gauge:

- initiated event counts recover ring ordinals;
- birth events recover actors, parentage, birth counts and adjacency;
- interaction parity recovers the modeled carriers;
- maximal events on each wire recover tips; and
- the seed supplies the initial `A--B` edge.

Any exception must be printed as a counterexample and lowers the theorem.

### T4 — timing-sensitive component tomography

For each finite component configuration `K`, construct a Branch-F observable
fingerprint `U_K(Delta)` from a canonical post-order sweep and the complete
ancestry of its future A-touching records.

The fingerprint may not mark an ancestor as “pre-stop” unless that mark is
already part of Branch F.  This prevents a false support proof.  If another
past `K'` lacks records present in `K`, it may create them after the stop and
then imitate the same final ancestry.

The required discriminator is instead the small-time order:

```text
P(U_K(Delta) | K) >= c_K Delta^m + O(Delta^(m+1)),  c_K>0;

for K' not gauge-isomorphic to K,
P(U_K(Delta) | K') is either zero or O(Delta^(m+1)).
```

The second row requires a catch-up lemma: no nonisomorphic `K'` can produce
K's exact sweep fingerprint in `m` or fewer future component rings.  Missing
initiator ordinals require at least one catch-up event; altered/extra immutable
records cannot be overwritten or removed.  Therefore the two conditional
Branch-F laws differ for all sufficiently small positive `Delta`.

If a nonisomorphic equal-order emulator exists, T4 is false and its complete
pair must be printed.

### T5 — predictive injectivity and necessity

Let `B(h)` be any exact sufficient carrier for Branch F at the licensed scope.
If T4 holds, then

```text
B(h)=B(h')  implies  [K_A(h)]_g = [K_A(h')]_g.
```

Thus the Branch-F predictive quotient is isomorphic to the full component
configuration modulo gauge.  The literal component is sufficient; every exact
alternative is a lossless recoding of its gauge class.  This is an
information-necessity theorem, not a claim about one preferred data format.

### T6 — unbounded information lower bound

Construct a positive-cylinder family of at least `2^M` gauge-distinct
component histories whose M independent record choices are all recoverable by
the component sweep.  Any exact Branch-F carrier over that family has at least
`2^M` states and therefore needs at least `M` bits in the worst case.

The receipt will also enumerate the number `g_N` of gauge-distinct reachable
component configurations in finite audit domains and print
`ceil(log2(g_N))`.  Global depth is used only to select a finite witness set.

## 6. Exact executable gates

One self-contained standard-library program under `v10/code/` must carry:

```text
E1  literal D34b finite-domain normalization and nonexplosive dependency;
E2  wire-persistence on every enumerated legal state;
E3  event-DAG reconstruction of every enumerated component;
E4  post-order sweep collects every pre-stop event;
E5  Fraction-exact sweep mass and 100-decimal Erlang evaluation;
E6  rooted nominal-gauge and sibling-order covariance;
E7  finite fingerprint injectivity plus explicit equal-order emulator search;
E8  catch-up/extra/altered-record hostile pair battery;
E9  exact 2^M family and finite gauge-class information ledger;
E10 first-applicable verdict and infinite/profinite ceiling.
```

Finite enumeration is a regression and counterexample search.  T1--T6 require
the all-finite analytic arguments above; no finite count is promoted into a
general proof.

Discrete probabilities use `Fraction`.  Erlang/exponential evaluations use at
least 100 decimal digits and are labeled evaluations of analytic formulas.
The program exits nonzero on any failed gate and prints source, stdout and
internal-summary hashes.

## 7. Frozen decision rule

Apply the first eligible row.

1. **COMPONENT PREDICTIVE-IDENTITY / UNBOUNDED:** T1--T6 pass; the component
   gauge class is both sufficient and necessary up to lossless recoding.
2. **PROPER ADAPTIVE FRONTIER:** returnability is a strict subset or a
   noninjective exact carrier is explicitly constructed and verified.
3. **RETURNABLE BUT TOMOGRAPHY UNPROVED:** T1--T3 pass but an equal-order
   emulator defeats T4 or the catch-up proof remains incomplete.
4. **QUERY ILL-TYPED:** the advertised fingerprint consumes a pre/post mark,
   remote timestamp or instrument not present in Branch F.
5. **REFUSAL/UNDEFINED:** a required conditional law or state object is absent.

No outcome is permitted to derive D34b, identify nature's law, prove a v9
posterior factorization, define an intrinsic quantum boundary, or infer
spacetime geometry.

## 8. Infinite-history and profinite ceiling

At each legal finite stop, D34b gives a finite component almost surely.  T5, if
proved, concerns that finite current component and implies no uniform finite
capacity over unbounded growth.

The locally finite serialized marked-prefix tree has finite levels and an
ordinary inverse-limit end space.  That observation alone does not establish:

- a construction-order-gauge quotient with canonical bonding maps;
- an identification with the v9 unmarked stem spectrum;
- continuity of the Branch-F predictive map on either completion; or
- a finite physical record carrying one completed inverse-limit point.

The receipt may state the finite-level compatibility inherited from D34e but
must return `OPEN` on those stronger bridges.

## 9. Physical interpretation ceiling

If row 1 survives, then for the chosen connected seed the exact full-ancestry
boundary is universe-component-sized.  This does not predict how large the
real universe is.  It says the required exact information scales with the
component produced by this chosen law.

A smaller operational boundary would require changing at least one input:

- finite prediction horizon;
- coarser observations than complete ancestry;
- genuine horizons or irreversible sealing;
- attenuation/approximate equivalence;
- or a different interaction law with causal speed structure.

Those are later investigations, not silent repairs to Branch F.

## 10. Review protocol

After the first receipt, three independent hostile streams must separately
attack:

1. probability, small-time order, predictive injectivity and profinite scope;
2. graph/DAG returnability, component reconstruction, gauge and locality; and
3. query measurability, ancestry emulation and quantum/geometry nonclaims.

Every major opening is frozen before repair.  Fresh deltas must inspect the
exact repaired commit.  Paper 23 is written only after the D34f theorem ceiling
survives these reviews.
