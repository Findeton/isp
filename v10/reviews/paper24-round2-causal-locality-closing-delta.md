# Paper 24 round 2 — causal locality closing delta

**Frozen target:** commit
`63ea1863bde134923bb04a5644ae4f10024e9012`.

**Manuscript:**
`relativistic-isp-v10-paper24-the-next-click-is-a-causal-diamond-not-a-clock-race.md`.

**Lane:** strong causal acquisition, realized reach and probability,
next-A/no-proper-time interpretation, logical actor and capability locality,
shared joint evaluation, disconnected control, Paper 23 comparison,
global-next-selection language and the status of the proposed overlap
architecture.

**Verdict:** **CAUSAL DELTA ACCEPTED WITH ONE NARROW LOCALITY MINOR AND TWO
NITS. TERMINAL D35 REMAINS UNCHANGED.**

**Count:** **0 blockers / 0 majors / 1 minor / 2 nits.**

Both round-1 majors in this lane are scientifically repaired. Paper 24 now
calls the D35 call diamond a finite realized acquisition/stopping region, not
a minimal predictive state, and calls the overlap program a candidate whose
objects and extension theorem remain undefined. The event/region, cemetery,
effective-menu, positive-source, shared-evaluator, global-selection and
review-count repairs are also present. The remaining minor is one sentence
that describes capability validation as actor/port-only even though the
executable also reads the shared rooted-call boundary and requester/route data.

## 1. Fresh reproduction and commands

The repaired manuscript SHA-256 is

```text
83096d5285b81b9a8374509380516e61941c887357efb7fbba1624e28b7f5809.
```

I ran the unchanged terminal executable under two fresh hash seeds:

```text
PYTHONHASHSEED=67867967 python3 v10/code/d35d_typed_identity_terminal_exact.py \
  > /tmp/p24r2.d35d.67867967.out

PYTHONHASHSEED=86028121 python3 v10/code/d35d_typed_identity_terminal_exact.py \
  > /tmp/p24r2.d35d.86028121.out

shasum -a 256 /tmp/p24r2.d35d.67867967.out \
  /tmp/p24r2.d35d.86028121.out \
  v10/data/d35d_typed_identity_terminal_exact.out
```

All three outputs are byte-identical:

```text
2150ddecfe92d3d0f2db6505a3e3ccc1c5c8685a4a2ea5a0497280939a023574.
```

The source remains

```text
9ef590992e04beec0672a3772d41e1e01cde8315b65b7cd0aaa207a649c56e28,
```

and both runs print

```text
PASS 18/18
TIMELESS ROOTED NESTED-CALL FAMILY / EXECUTABLE.
```

I also independently enumerated the first-call laws, reran the evidence and
rejection gates, and compared the complete connected physical distributions
under the disconnected intervention. The exact output was:

```text
Q1 serializers=16/16/16 reach=6/10 mass=1/16 hops=18
   disconnected root projection equal
   disconnected complete connected distribution equal
   rejection/unchanged/queued=6/6/1
   A2=root actor tip=collector root tip

Q2 serializers=16/16/16 reach=6/10 mass=3/40 hops=18
   disconnected root projection equal
   disconnected complete connected distribution equal
   rejection/unchanged/queued=6/6/1
   A2=root actor tip=collector root tip.
```

Across the 16 completed states in each Q cell, all actor mailboxes,
`issued_incoming` sets and outstanding-call tables were empty; used capability
identifiers were unique across actors. There were 44 used-capability
occurrences across the 16 histories in each cell.

The repair commit itself is whitespace-clean:

```text
git diff --check 63ea186^ 63ea186
repair_commit_diff_check=0.
```

The cumulative round-1-to-repair range is not clean; that separate hygiene
result is recorded as n1 below.

## 2. Strong causal acquisition and binary reach — pass

Sections 3.2--3.4 now preserve the necessary separation:

```text
structural acquisition   a licensed adjacent transfer chain enters NewPast_A;
operational influence    a declared source intervention changes an A2 observable;
realized reach           true or false in one completed history;
reach probability        mass of the completed histories in which reach is true.
```

The paper does not promote ancestry, correlation or entanglement alone into a
message. CAP is stated as the causal principle being imposed, while section
7.2 restricts the demonstrated intervention theorem to one bounded classical
datum and one supplied transport grammar. That is the terminal D35 scope.

The generic cylinder formula now assumes `mu([H0]) > 0` and assigns a cemetery
value when A has no next successor. Reach is false on that value. This closes
the former undefined-denominator/no-A2 case without affecting D35, where the
externally initiated finite call produces A2 with probability one.

The exact D experiment remains correctly interpreted. Six structural histories
contain the authenticated `A -> B -> D` route and ten do not. The bit
intervention does not alter their support or probability. It changes the A2
datum exactly on the six queried histories, whose total mass depends on Q.
Thus binary causal membership and numerical dynamics are not conflated.

## 3. A2 is an upper seal, not a clock reading — pass

The repaired title and ordinary-language summary now identify A2 as the upper
seal of the call diamond. The diamond is the whole operational region; A2 is
its first new A-wire event. The lower seal is A1, child work occurs while A's
tip remains A1, and the selected returns are consumed before the root result
becomes both A's tip and the collector root tip.

No duration follows from this order. The actor-owned call ordinal is a fresh
causal identity, mailbox service order is construction gauge, and the paper's
terminal statement now explicitly qualifies the no-proper-time result by the
supplied A-rooted grammar. It makes no statement that a root-free universe can
already choose which actor has the next click without further physics.

## 4. Actor behavior, capabilities and shared joint state — mostly pass

The paper accurately describes the accepted logical actor protocol:

- each connected actor has its own address, tip, owned ports, mailbox,
  issuance/used sets, outstanding return slots and carried evidence fields;
- an unissued capability lookalike rejects;
- capability, option, leg and generated-identity checks precede durable query
  mutation;
- service peeks and acknowledges only after success;
- malformed root input leaves the state unchanged; and
- completed calls have no queued or outstanding work.

It also now discloses the evaluator at every load-bearing summary. The local
menu does not normalize over a spacelike ready set, but the quantum maps are
applied to one shared exact carrier and ancestry is retained in one shared
event-DAG collector. The paper does not call this distributed quantum-state
storage, independent processes or a local hidden-variable factorization.

The effective menu is now exact. It depends on the actor's degree and supplied
Q cell; unavailable visit/fork mass is folded into idle. The printed Q1/Q2
leaf and degree-one rows agree with the executable.

## 5. MINOR m1 — capability admissibility is not actor/owned-port-only

Section 8.3 says that “menu selection, capability admissibility and the chosen
local factors consult only the declared actor/owned-port data.” This remains
too strong for capability validation.

The stochastic menu and selected target legs use the addressed actor's owned
ports plus the supplied Q cell. A query capability is checked against more
data:

```text
the target actor's issued/used sets and adjacent edge key;
the carried namespace, transaction, root event and payload;
Network.current_tx, collector.root_tip and Network.root_payload;
the authenticated root-to-target route;
the requester's child-port ownership and held lower tip; and
the root/nonroot call-shape fields.
```

These checks are causally declared rooted-call data and do not form a global
opportunity normalizer. They are nevertheless not only the target actor's
owned-port state, and several are read from the shared `Network`/collector or
the requester actor.

**Required repair:** replace the sentence with:

> Menu probabilities and target-leg selection use the addressed actor's owned
> ports and the supplied Q cell. Capability admission additionally verifies
> the carried call-boundary fields against the target's issued set, adjacent
> edge/route, requester held tip and shared rooted-call registers. The selected
> quantum maps are evaluated by the disclosed shared joint engine.

This keeps the earned statement—logical causal locality within a supplied
rooted protocol—without implying a target-actor-only validator.

## 6. Disconnected control — pass

The repaired source wording is exact. `output_sources` is called a
positive-source set. A queried zero bit is absent from that set but remains in
the authenticated capability route and event provenance, so zero is not
confused with an unqueried source.

The disconnected fixture is the marked actor/event copy accepted by the D35d
terminal review: seed actor event, two one-parent seed births and a source
seal, placed in disjoint control identity domains with no incidence on A's
component. Changing its bit leaves both the A observable distribution and,
under an independent comparison, the complete connected 16-atom physical
distribution fixed. The paper correctly attributes this to disconnection, not
metric distance; no spatial geometry is assumed.

## 7. Paper 23 comparison — substantive finding closed

Section 9.3 now distinguishes:

```text
Paper 23   minimal exact predictive quotient for unlimited-horizon Branch F
           under the chosen D34b law;

D35        finite realized acquisition/stopping region for one selected A2
           under a different supplied rooted law.
```

It explicitly says that D35's pre-call kernel conditions on the complete typed
rooted state, that the call boundary has not been proved sufficient or minimal,
and that the two papers do not compare minimal predictive-boundary sizes. This
closes round-1 M1. The below-A region is now an analytical causal object, not a
predictive compression theorem.

### NIT n2 — “changes the law by adding” retains an avoidable modification implication

One sentence still says that “D35 changes the law by adding a return-limiting
causal protocol.” The preceding paragraph already says the laws are different,
so the scientific scope is recoverable. “Adding,” however, can still suggest
that D35 augments D34b with a derived limiter. It does not; D35 supplies a
different grammar.

**Repair:** write “D35 instead uses a different supplied, return-limited causal
grammar.”

## 8. Global next selection — pass

The former normalizer/clock-race dichotomy is removed. Section 11.1 now says
that requiring exactly one globally next actor introduces an additional global
selection law and lists ready-set normalization, clock races, priorities,
total orders and deterministic schedulers as examples. This is the invariant
claim D35 supports.

The proposed alternative is also scoped correctly: put a law on causal partial
histories, allow incomparable events and quotient machine linearization. D35
implements this only after externally choosing A and restricting calls to the
laminar ownership grammar; peers, overlaps, cycles and joins remain open.

## 9. Overlap architecture — round-1 major closed by explicit nonclaim

The paper no longer presents `gamma_D` as an existing SHARD object or D35 as a
proved special case. It calls the construction a candidate and lists what a
future investigation must define:

- an oriented region category and variable-support embeddings;
- incoming, generated/outgoing and lateral interfaces;
- boundary and regional-history spaces;
- boundary extraction and restriction/transport;
- conditional kernel composition when a smaller boundary is random;
- coherent positive joint extension on arbitrary finite covers, not only
  pairwise intersections; and
- a global history space with existence and uniqueness/tightness questions.

The displayed composition equation is labeled as the form a future classical
law should take, with domains and measurability still required. The three-
binary-region counterexample correctly shows why pairwise overlap marginals do
not suffice. D35 is called a motivating finite model and explicitly **not** a
proved special case because the embedding has not been defined.

This closes round-1 M2. “The most pressing next investigation” is a research
priority, not a claim that the overlap architecture or root-free measure has
already been constructed.

## 10. Prior-finding dispositions

| Round-1 causal finding | Disposition at `63ea186` |
|---|---|
| M1 completed call promoted to predictive boundary | **closed**; acquisition/stopping only, no sufficiency/minimality |
| M2 overlap object called precise/solved | **closed**; candidate/undefined with missing objects enumerated |
| m1 event identified with whole diamond/root scope weakened | **closed** |
| m2 no A2-existence convention | **closed** by cemetery outcome and positive cylinder mass |
| m3 fixed-q branch formula | **closed** by exact degree-dependent effective menu |
| m4 actor locality omits shared evaluator | **partly closed**; shared evaluator disclosed, actor/port-only capability sentence remains m1 |
| m5 source set described as complete provenance | **closed**; positive-source/route distinction explicit |
| m6 normalizer/clock false dichotomy | **closed** |
| n1 “nine zeroes” | **closed**; three clean lane verdicts |

No new causal, reach, no-time, disconnected-control, Paper 23 predictive-
boundary or overlap-architecture major was found.

## 11. NIT n1 — cumulative review range still fails whitespace hygiene

The repair commit is clean, but the full paper-review range is not:

```text
git diff --check a680c06 63ea186
```

returns four trailing-whitespace diagnostics in
`reviews/paper24-round1-probability-mathematics-hostile-review.md`, lines 4, 6,
9 and 12. They are two-space Markdown hard breaks in review metadata. They do
not affect Paper 24 or D35 science, but they prevent the cumulative review arc
from passing the repository's ordinary diff-hygiene gate.

**Repair:** remove the four terminal two-space suffixes without changing the
historical review text.

## 12. Final tally and allowed scope

```text
B  blockers  0
M  majors    0
m  minors    1
   m1        capability validation described as actor/owned-port-only
n  nits      2
   n1        four historical review lines fail cumulative diff hygiene
   n2        Paper 23 comparison retains “adding” instead of a different grammar
```

**Final count:** **0B / 0M / 1m / 2n.**

Subject to those narrow repairs, this causal-locality lane permits Paper 24 to
retain the terminal D35 noun:

```text
TIMELESS ROOTED NESTED-CALL FAMILY / EXECUTABLE
```

with its mandatory meaning: a supplied A-rooted laminar logical actor protocol
with binary licensed reach and exact local menu probabilities, represented by
a shared event-DAG/joint-carrier evaluator. It does not permit a target-actor-
only implementation claim, a Paper 23 predictive-boundary theorem, a defined
overlap specification, a root-free initiator law, physical proper time or
nature's interactive click law.
