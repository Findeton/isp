# Paper 24 round 2 — birth/quantum/corpus closing delta

**Frozen target:** commit
`63ea1863bde134923bb04a5644ae4f10024e9012`.

**Lane:** D24 conditional birth content versus structural opportunity, Q/g
nonselection, the registered root-local quantum instrument, D-origin evidence,
typed identity, D31 and `S^2` synthesis, the pinned pre-D35 census, and review
accounting.

**Verdict:** **SCIENTIFICALLY CLOSED IN THIS LANE. ACCEPT WITH ONE EDITORIAL
NIT.**

**Count:** **0 blockers / 0 majors / 0 minors / 1 nit.**

All eight findings from the round-1 birth/quantum/corpus review are repaired at
their required width. The two terminal executables reproduce under fresh hash
seeds. The corpus repair is stronger than a live-tree filename exclusion: both
the path manifest and every selected file's bytes are read from the pinned
pre-D35 git tree. No ontology or quantum promotion remains in this lane.

## 1. Fresh exact reproduction

### 1.1 Pinned pre-D35 corpus — pass

Fresh executions under `PYTHONHASHSEED=314159265` and `424242424` exited zero
and were byte-identical to the committed receipt. Exact outputs are:

```text
cutoff commit
fc074b9ec4f2c9ecdef28b61c623d89d08e76432

primary / category-relevant files
441 / 427

corpus stream SHA-256
b0e4c7e0be1c8587b5f3b35e36a834fa8f485cf4bd7cfbb61331017bcd1541b7

inventory source SHA-256
445687217819ca8bd39ea881e12795dd472120700bbfe2c2a6055deafbcf0a21

fresh and committed stdout/receipt SHA-256
7f998dea113694b132082bb87cbc4053123788c3411d1b65468e4caccb864182

verdict
PASS 6/6.
```

I also ran the fresh seed with `GIT_TRACE=1`. The trace records exactly:

```text
1 invocation of
git ls-tree -r --name-only <cutoff> -- v1 ... v10

441 invocations of
git cat-file blob <cutoff>:<selected-path>.
```

Thus `cutoff_manifest()` obtains the names from the pinned tree and
`cutoff_bytes()` obtains all 441 contents from that same tree. It does not
construct an old manifest and then accidentally hash live files. The four
historical files named `paper24` in V3, V4, V6 and V7 remain in the receipt;
the current V10 Paper 24 is absent because it did not exist at the cutoff. This
closes round-1 M3 without creating a Paper-25 recurrence.

### 1.2 Terminal D35d — pass

Fresh executions under `PYTHONHASHSEED=271828182` and `161803398` exited zero
and were byte-identical to each other and the committed receipt:

```text
source SHA-256
9ef590992e04beec0672a3772d41e1e01cde8315b65b7cd0aaa207a649c56e28

stdout SHA-256
2150ddecfe92d3d0f2db6505a3e3ccc1c5c8685a4a2ea5a0497280939a023574

internal science SHA-256
79e29b8fd5f5a294b3c2faf438ffcca45434ec78af55b4150324b9939a03f26c

verdict
PASS 18/18.
```

The science receipt again prints, for both Q cells, 16 physical first-call
atoms, 408 second-call refinements, `8 -> 48`, five alternatives, `10/10`
cross-range zeroes, weighted identity, six queried and ten unqueried D
histories, and the exact reach masses `1/16` and `3/40`.

## 2. Birth law and nonselection

### 2.1 D24 is now attributed only its conditional content result

The repaired abstract, ordinary-language summary and section 5 agree on the
three distinct layers:

```text
causal grammar       which structural extensions are admissible;
q_birth              probability of selecting the birth alternative;
B_g                  conditional parent-to-parent+newborn isometry;
g                    a free coupling parameter inside that admitted map.
```

On a selected birth, D24 earns the exact identity

```text
B_g^dag (I tensor |1><1|_new) B_g
  = g (|1><1|_parent tensor I_spectators),
```

equivalently `P(newborn=1)=g P(parent=1)` at the birth instant. D24's own note
states that the attaching collar and the per-birth `g` are free data. Paper 24
now says exactly that: it neither relabels `B_g` as the opportunity selector
nor claims that the D24 family selects a root, ownership graph or coupling.

The D25/D27 ceiling is also carried honestly. `B_g` is one admitted isometry;
the wider preparation-independent distinguishability-preserving reception
class includes orthogonal-range mixtures of isometries. No uniqueness is
inferred from the D24 exhibit.

### 2.2 Q and g remain demonstrably unselected

The two complete accepted cells are printed correctly:

```text
Q1: (idle,birth,visit,fork) = (3/8,1/4,1/4,1/8), g=9/25;
Q2: (idle,birth,visit,fork) = (2/5,1/5,3/10,1/10), g=16/25.
```

Both pass the same terminal gates while giving unequal birth, visit and reach
probabilities. Their two distinct admitted g values also pass the exact D24
birth identity. This proves the paper's stated nonselection conclusion: the
current principles choose neither a unique Q nor a unique g. It does not prove
that Q and g can be varied independently, and the paper does not make that
stronger claim.

## 3. Root-local quantum instrument and the D spectator

Section 6 now identifies the eight-dimensional domain as the registered
`A/B/C` sector, not the complete initial carrier. The seed also contains the
connected D factor, so the full initial carrier has dimension 16. D is not
being erased or declared nonexistent: every displayed root-local map extends
as identity on D and on any other external factor.

The five local matrices have exact shapes

```text
birth                          16 x 8
idle, fork, visit-B, visit-C    8 x 8 each.
```

Orthogonal classical-sector injections give the stated **local-sector** output
dimension `16+4(8)=48`. If one elected to include the D spectator in the
dimension count, this same extension would be `16 -> 96`; that is not the
registered instrument the paper claims. The paper consistently keeps the
local-sector qualifier and does not call 48 the full universe-carrier
dimension.

For each alternative `V_o^dag V_o=I_8`. The five block ranges are orthogonal,
so all ten unordered cross Grams vanish. The actual degree-two alternative
weights are

```text
Q1: birth 1/4, fork 1/8, idle 3/8, visit-B 1/8, visit-C 1/8;
Q2: birth 1/5, fork 1/10, idle 2/5, visit-B 3/20, visit-C 3/20.
```

Each row sums to one, hence the weighted Gram sum is exactly `I_8`. This earns
the paper's classical-output common-input instrument. The repaired manuscript
retains the essential ceiling: it is not a coherent amplitude sum over
different support graphs.

## 4. Evidence and identity semantics

### 4.1 `output_sources` is now correctly a positive-source set

Section 7 distinguishes the carried bit from its structural route. When D's
source bit is one and D is queried, D appears in `output_sources`. When the bit
is zero, it does not. The zero-valued query is nevertheless present in the
issued capability path, event ancestry and authenticated provenance. Therefore
absence from `output_sources` is no longer narrated as absence of a query.

The paper retains the exact limited intervention statement: paired
`do(D=0)`/`do(D=1)` histories preserve support and probability; A2 changes in
the six queried histories and not in the ten unqueried histories. It does not
promote the positive-source set into complete provenance or this classical
transport experiment into generic quantum signalling.

### 4.2 Typed identity is restricted to what was tested

Section 8.2 now names the disjoint supplied/generated actor/event/control
storage domains and restricts covariance to the declared six-event supplied
seed, its reachable rooted grammar, ordinary alpha renaming and the registered
display-collision classes. Immediate event collision, delayed call-five event
collision and future-newborn actor display collision retain the exact
`16/408/408` projectivity and `6/6` continuation receipts.

The paper explicitly refuses a general graph-canonization theorem. Typed
storage proves that supplied and generated identities cannot collide merely
because their printable strings agree; it does not solve arbitrary root-free
graph isomorphism. The claim now matches the executable's scope.

## 5. Corpus synthesis

### 5.1 D31 width — closed

Both section 2.2 and section 11.4 now carry the load-bearing hypotheses:

```text
none-free;
birth-positive at every reachable count;
unbounded growth;
stationary path covariance;
per-labelled weights depending only on the unsealed count u.
```

At that scope D31 rules out positive interactions in the graph-blind class and
therefore forces only state sensitivity richer than u. The paper expressly
says D31 does **not** force that richer datum to be local. Local collar
dependence is listed separately as a proposed physical principle; component
data and global invariants are not silently excluded. Round-1 M2 is closed.

### 5.2 `S^2` and the V9 bridge — closed

The repaired notation is `S^2`, and the phrase appears only as a possible
channel-manifold symmetry inherited from “many clocks, few factors.” Section
12 says the D35 rooted call tree neither realizes that algebraic manifold nor
sets spacetime dimension or cone shape. It requires a root-free grown web
before the channel structure, order dimension and cone tests are revisited.
No `S^2 -> 3+1` bridge is claimed from the present instrument.

### 5.3 Reproducibility record — substantively closed

The paper prints the full pinned cutoff, 441/427 counts, unchanged corpus
stream, new inventory source/receipt hashes, all three D35d hashes and the
three terminal `0B/0M/0m/0n` lane verdicts. The round-1 reports and eleven
repair dispositions are named. The former “nine zeroes” arithmetic is gone.

## 6. Prior-finding dispositions

| Round-1 finding | Round-2 disposition |
|---|---|
| M1: base-q branch product omitted folded idle mass | **closed** — exact degree-dependent effective menu and leaf/degree-one checks printed |
| M2: D31 promoted to a locality theorem | **closed** — only richer-than-u sensitivity is forced; locality separately proposed |
| M3: live corpus scanner failed at 442/441 | **closed** — manifest and all bytes read from pinned pre-D35 tree; `PASS 6/6` |
| m1: eight-dimensional carrier described as the full seed | **closed** — A/B/C root-local sector; D/external identity spectators |
| m2: subtitle called the model a rooted universe | **closed** — rooted family/logical-actor sampler; root-free law refused |
| n1: normalization credited with termination | **closed** — local normalization, strict descent and commuting factors receive separate attributions |
| n2: “nine zeroes” | **closed** — three clean lane verdicts |
| n3: `S2` notation | **closed** — `S^2`, with the bridge still open |

The adjacent round-1 positive-source and typed-alpha scope repairs also close,
as checked in section 4 above.

## 7. New finding

### n1 — section 14 still says the paper-level hostile review “remains required”

Section 14 ends:

> “Paper-level hostile review remains required before this synthesis is
> terminal.”

Sections 15 and 16 immediately document that completed hostile round and its
repair receipt, while the status line correctly says that only focused deltas
are pending. The stale sentence does not alter any theorem, receipt or scope,
but it makes the review chronology momentarily self-contradictory.

**Exact repair:** replace it with:

> “Paper-level hostile round 1 and its repair receipt follow; focused closing
> deltas decide paper-level promotion.”

## 8. Final disposition

**Final count:** **0B / 0M / 0m / 1n.**

The birth/quantum/corpus lane supports paper-level scientific closure. D24 is
kept conditional, Q and g remain unselected, the quantum result is expressly
root-local and classical-output, D remains an identity spectator rather than a
discarded factor, zero-valued source queries retain structural provenance,
typed identity stays within its tested grammar, D31 is no longer a locality
theorem, `S^2` is only a future symmetry candidate, and the historical corpus
is reproducible from the pinned git object database. Apply the single stale
review-accounting sentence as an editorial cleanup; no further scientific
rerun is required for this lane.
