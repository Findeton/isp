# Paper 12 hostile-review protocol

**Date:** 2026-08-19

**Status:** PROTOCOL — OUTCOME-NEUTRAL, PRE-REVIEW

**Candidate commit:** `7305ebf`

This protocol freezes the review procedure before any Paper 12 reviewer is
assigned.  It contains no preferred scientific outcome, expected metric, or
majority rule.  The candidate is a result-known negative reconstruction, but
every load-bearing claim must be independently rebuilt rather than inherited
from its transcript, receipt, verification note, or prose.

## 1. Immutable review corpus

| role | path | SHA-256 |
|---|---|---|
| ONE-GAMMA gate | `v16/note-apr-one-gamma-paper-review-gate.md` | `06d171a3eea8109e177e2dfa3cb5536fe3785043e676f735c36e91d03834cb51` |
| construction pin | `v16/note-apr-paper12-negative-candidate-pin.md` | `6341a1184426f3a6be0ad619d9f02340124a76e5484bb94609462d5d765a6ebd` |
| exact source | `v16/code/apr_paper12_exact.py` | `c209486a94016c00921c3b9edfeb2f53eef7d005180eb3c1d95153e56fec86a7` |
| transcript | `v16/code/apr_paper12_output.txt` | `7ae34f1fcaf7f8e2739c8e17ac90ee87f629e90713401bc86367524b41f8ab7f` |
| receipt | `v16/code/apr_paper12_receipt.json` | `d4e16c262d1c929d6e0507ef482eef4c2ff26c7f41f9dc4bf0bc58b708adfd39` |
| receipt payload | receipt without `payload_sha256` | `1c6ded1e366cd4e3863a2774285ade5663f80e5228ed4077d0eb5b33bb0286f5` |
| scientific candidate | `v16/paper-12-atomless-regions-and-the-missing-gluing-law.md` | `cdb212c57c8b80099f9fc17eb0b1c5ed90c38ae2f5db7c50eb3038eb893f4de8` |
| candidate verification | `v16/note-apr-paper12-candidate-verification.md` | `0ee0e22879f2c1d086f8ca13d53bed4fc6f5261301865674d2d4368cec136e70` |

The source is frozen in commit `22ba8a1`; the remaining candidate files are
frozen in commit `7305ebf`.  Every reviewer authenticates ordinary bytes and
the canonical receipt payload before scientific work.  A mismatch is an
integrity finding, not evidence for or against a physical claim.

No reviewer may edit the corpus, candidate, source, artifacts, protocol,
status files, logs, plans, or Git.  Scratch work is off-tree and private.

## 2. Evidence rule

The candidate paper is a list of claims, not evidence.  The transcript and
receipt are audit targets, not scientific oracles.  The exact source may be
run as a subprocess for integrity replay, but no reviewer may import or call
its scientific functions.  Independent reconstruction uses separately
written exact arithmetic and data structures.

Every claim receives one evidence grade:

```text
ANALYTICAL-PROOF
INDEPENDENT-EXACT-RECONSTRUCTION
CONDITIONAL-ON-PRINTED-HYPOTHESES
FINITE-CONTROL-ONLY
UNCONSTRUCTED
REFUTED
INCONSISTENT
```

An analytical theorem does not instantiate a missing physical process.  A
finite control does not prove an all-depth or all-context claim.  An absence
row must name the searched interface and its domain; it cannot be inferred
from silence or a result word.

## 3. Mutual blindness

Three seats work independently:

1. **Seat R — regional algebra, questions, quotient and refinement**;
2. **Seat P — process, cospans, boundary gluing and overlapping laws**;
3. **Seat O — ontology, ONE-GAMMA, indivisibility and scientific scope**.

A seat may not read, list, request, receive, or infer another seat's report or
scratch.  Reports freeze separately before an adjudicator may read more than
one.  There is no inter-seat discussion and no majority vote.

Reviewers may consult primary literature only for claims actually made by the
candidate.  They record title, authors, stable URL or DOI, and the exact
implication checked.  Literature cannot supply a construction absent from the
candidate.

## 4. Common integrity reconstruction

Every seat independently:

1. authenticates all corpus hashes and the canonical receipt payload;
2. replays fixture-free `--selftest` and checks all `13` registered checks;
3. replays one full publication to new private paths without importing source
   functions;
4. verifies byte identity with the frozen transcript and receipt;
5. replays from an alien working directory and a true off-tree/no-`.git` copy
   containing only the source and authenticated required inputs;
6. verifies strict argument refusal, absent-path publication, no overwrite,
   transactional rollback, and no unexpected repository writes;
7. performs an AST/source audit for floats, tolerances, randomness, network,
   Git, runtime-CWD dependence, scorer/fixture imports, expected-result lookup,
   and bare capability-dictionary promotion;
8. independently checks the receipt payload and transcript hashes;
9. confirms that the scientific paper contains no internal unit, ledger,
   scorer, fixture, task, or review-history prose;
10. distinguishes mathematical exactness, physical construction, and ontology
    promotion in every conclusion.

## 5. Common mathematical controls

All seats independently reconstruct, without source functions:

- the prefix-antichain normal form and Boolean operations;
- the generic split `C(w)=C(w0) join C(w1)`;
- the dyadic volume contextual counterexample;
- the two-element ultrafilter-character image;
- positive restriction branches and `Q1+Q0=I` with the zero port retained;
- prefix-free completeness of the four uniform frontiers and
  `{0,10,110,111}`;
- the direct depth-three tree counts `15/14`;
- at least one tagged pushout rather than count-only union;
- the active B0-only identity assignment;
- the two complete global `ABC` laws and their exact marginals;
- the classifier's first-failure precedence;
- the distinction between graph composition and process assignment;
- the absence of a jointly instantiated physical
  `(C_pres,G,C,B,Div,Gamma)`.

Every seat reconstructs the semantic content of the following common controls:

```text
RAW-ATOMLESS
VOLUME-NONCONGRUENCE
ZERO-PORT
ADAPTIVE-FRONTIER
PUSHOUT-NOT-PROCESS
CACHED-MARGINAL
ARBITRARY-SELECTOR
SYNTHETIC-LAW-EXCLUSION
PRIMARY-PRECEDENCE
```

The receipt's pass field is never the predicate.

## 6. Seat R — regional algebra and physical quotient

Seat R independently rebuilds:

1. canonicalization of finite binary prefix antichains;
2. Boolean identities on the registered family;
3. the all-depth atomlessness proof and the distinction from a finite split
   census;
4. whether the all-zero character is a Boolean homomorphism and whether its
   image is atomic;
5. why scalar-volume equality fails meet congruence;
6. exact finite-depth restriction matrices and the symbolic all-depth proof of
   positivity, affinity and normalization;
7. zero-port typing and summation rather than averaging;
8. finite probe separation versus a target-independent generated physical
   compiler;
9. whether any complete contextual equivalence, Boolean congruence, gluing
   congruence, or descended physical atomlessness is actually constructed;
10. every regional and quotient sentence in the paper, abstract, ontology
    ledger and conclusion.

Mandatory fresh changed objects:

- a valid cylinder deeper than every registered row;
- a nonfaithful supported valuation that leaves one subregion dark;
- a constant profile and an ultrafilter profile;
- a Boolean symbol relabeling transported through the valuation;
- a candidate quotient with a proper split before quotient but an atomic
  image afterward.

Seat R must attempt to falsify the paper's raw theorem and must separately
attempt to make its physical-quotient language overclaim.  It reports raw and
post-quotient atomlessness as different coordinates.

## 7. Seat P — process, gluing and global completion

Seat P independently rebuilds:

1. all four uniform frontiers and at least two nonuniform complete adaptive
   frontiers;
2. the three registered tree factorizations;
3. tagged pushout quotienting with boundary-fixed graph equality;
4. the active identity census over B0–B3;
5. the exact inventory of missing process interfaces;
6. why graph pushout, tree restriction and static question normalization are
   three separate controls;
7. whether any total filling-to-map assignment, tensor, interchange,
   naturality, or arbitrary-frontier identity factory exists;
8. exact `AB` and `BC` marginalization of both global laws;
9. whether a Markov, entropy, sparsity, order or hash selector enters the
   primitive law;
10. the cached-marginal mutation and every process/gluing sentence in the
    paper.

Mandatory fresh changed objects:

- the adaptive cover `{00,01,1}`;
- a fresh four-stage tree factorization with one changed boundary leg;
- a naive disjoint union in place of a tagged pushout;
- a parity-perturbed positive `ABC` distribution with the same pair shadows;
- a mutation preserving `AB` while moving `BC`;
- an assigned same-boundary nonidentity graph presented as an identity.

The parity control is a non-kill when independently derived pair shadows remain
equal: it strengthens global underdetermination.  A process claim fails unless
the assignment and its equations are present, not merely because the graph
counts match.

## 8. Seat O — ontology, ONE-GAMMA and scope

Seat O independently rebuilds:

1. the actual measured process role from generated outputs;
2. the distinction between presentation region and physical region;
3. the distinction between static restriction and region rewriting;
4. the complete ONE-GAMMA primitive-input inventory;
5. whether any unique nomological transition root exists;
6. whether regional shadows, instruments, records, comparisons or rewrites
   are derived from such a root;
7. whether division and durable-record status are independently earned;
8. whether a raw relation label is promoted to geometry;
9. whether the synthetic executable-law control appears as physical evidence;
10. every claim attributed to Barandes, Sorkin, and structured cospans;
11. every actualization, point-free, relational, metric, curvature, gravity,
    QFT and prediction wall;
12. whether the successor motivation correctly requires a preregistered
    explicit `Gamma_lambda` family without pretending to construct it.

Mandatory fresh changed objects:

- treat a neutral tree node as a beable and test relabeling;
- rename candidate memory as a durable record without a reader;
- rename a raw relation as distance or curvature without calibration;
- insert a disconnected synthetic executable law beside the finite controls;
- retrofit a wrapper `Gamma` from the observed `AB/BC` tables;
- convert alternative law arguments into co-actual histories;
- replace the ontology candidate while holding all measured coordinates fixed.

Seat O prints two verdicts: the immediate construction role and the separate
candidate ontology.  A negative construction does not refute the ontology; it
leaves it unconstructed or postulated.

## 9. Complete control assignment

Beyond the common controls, Seat R owns independent semantic reconstruction of

```text
ATOMIC-CHARACTER
FRESH-PROBE
```

Seat P owns

```text
IDENTITY-DOMAIN
```

Seat O owns

```text
RAW-NODE-ONTOLOGY
ANCHOR-FAILURE
```

Every frozen control is therefore reconstructed by at least one seat.  A row
may be graded `FINITE-CONTROL-ONLY` or `UNCONSTRUCTED`; the protocol does not
require the candidate's label to survive.

## 10. Hard scientific kills

Any reproducible item below defeats the associated universal or promoted
claim.

`K1` — raw prefix syntax, tree leaves, graph nodes, or a finite split census is
called an atomless physical region algebra.

`K2` — volume/profile equality is called a Boolean or process congruence after
the contextual counterexample.

`K3` — an ultrafilter-character atomic image is ignored while quotient
atomlessness is claimed generally.

`K4` — a finite question catalogue is called a complete generated physical
future grammar.

`K5` — the zero port is dropped, branches are averaged, or each branch is
renormalized before nonselective composition.

`K6` — finite graph pushouts, matching tree unions, or typed legs are called a
horizontal process without a filling-to-map assignment.

`K7` — identity at B0 is generalized to unassigned boundaries.

`K8` — sequential composition substitutes for tensor or an unattached map
substitutes for naturality.

`K9` — one compatible `ABC` completion is selected by convention, order,
entropy, sparsity, hash, or a silent Markov assumption.

`K10` — a simultaneous regional coupling diagnostic is called a transition,
division, causal order, or indivisible stochastic law.

`K11` — the generic synthetic executable-law object supplies any physical
Paper 12 coordinate.

`K12` — a wrapper around independently supplied modules is called `Gamma`.

`K13` — appended syntax is called a durable record, or a declared boundary is
called a lawful division, without same-law recovery.

`K14` — raw relation labels, graph adjacency, word depth, or tree order are
promoted to geometry, distance, curvature, place, or time.

`K15` — the negative locality coordinate is described as a measured physical
nonlocality rather than an unconstructed promotion.

`K16` — Hilbert/history objects or a Hamiltonian are promoted from
representation to ontology.

`K17` — normalization or branching is said to derive which outcome becomes
actual.

`K18` — source precedent is claimed to derive ISP's point-free catalogue,
changing geometry, stable records, locality, actualization, or numerical law.

`K19` — the paper implies metric, curvature, backreaction, continuum, GR, QFT,
particles, constants, or empirical predictions.

`K20` — the successor's proposed `Gamma_lambda` is described as already
constructed, selected, or tested.

## 11. Integrity blocks

Review returns `INTEGRITY-BLOCK` if it confirms any of:

- corpus or payload hash mismatch;
- source importing scorer/fixture scientific functions;
- expected-result lookup or fixture-ID branch controlling a metric;
- float/tolerance/randomness on a substantive path;
- Git, network, untracked-scratch, or CWD dependence;
- repository/off-tree replay disagreement;
- partial publication or overwrite;
- mutation evidence with identical before/after object bytes and no separately
  hashed provenance envelope;
- paper prose claiming receipt evidence that cannot be reconstructed;
- reviewer access to another seat's report before its own freeze.

An integrity block does not determine the physical outcome.  It blocks
certification until a separately authorized repair.

## 12. Registered outcome and coordinate vocabulary

The adjudicator selects the earliest supported primary from the complete
ladder frozen in the construction pin.  Reviewers may recommend a word from
that ladder but may not invent a stronger one.

Orthogonal coordinates remain independently graded:

- raw versus physical atomlessness;
- static response versus horizontal process;
- presentation versus physical region;
- finite graph gluing versus process composition;
- complete future profiles and regional congruence;
- comparison and dynamic locality;
- contact and causal order;
- ONE-GAMMA provenance and law selection;
- measured ontology role versus candidate ontology;
- actualization;
- metric/curvature/gravity scope.

The precedence order is normalization, raw regional algebra, boundary gluing,
two-arrow typing, future completeness, regional congruence, comparison,
dynamic support, causal order, and joint law.  A later exact theorem cannot
override an earlier absence.

## 13. Required report schema

Each report contains, in order:

1. seat identity and mutual-blindness declaration;
2. complete read set with hashes;
3. replay commands, return codes, and artifact hashes;
4. independent reconstruction method and private script hash;
5. claim-by-claim evidence table;
6. analytical proofs used;
7. frozen-control and fresh changed-object results;
8. numbered `KILL`, `REPAIR`, and `NARROWING` findings;
9. scoped coordinates and earliest recommended primary;
10. ontology and GR/QFT/actualization walls;
11. candidate-paper grade;
12. normalized self-hash and ordinary external SHA-256.

Candidate grades are:

```text
ACCEPT
ACCEPT-WITH-FIXES
MAJOR-REPAIR
REJECT-AS-WRITTEN
INTEGRITY-BLOCK
```

For the normalized report hash, replace the value on the line
`normalized_sha256:` with sixty-four ASCII zeroes, normalize line endings to
LF, and hash the complete bytes.  The ordinary file hash is reported
externally after freeze.

## 14. Adjudication

Adjudication begins only after all three reports are frozen and hashed.  The
adjudicator may read all reports; reviewers never do.

For every disagreement, the adjudicator independently reconstructs the
smallest decisive counterexample or identity.  There is no majority rule.  A
single reproducible type error or counterexample defeats a universal claim.
Positive scope is the intersection of independently supported evidence.

The adjudication must preserve the reports byte-for-byte and end with:

- one strict primary;
- all orthogonal coordinates;
- accepted theorems with exact scope;
- killed or narrowed promotions;
- paper grade and any permitted editorial changes;
- an ontology declaration ledger;
- ordered successor debts;
- a normalized and ordinary SHA-256.

An editorial correction that changes no theorem, evidence, coordinate, or
primary may be applied only after adjudication explicitly authorizes it.
Changing scientific bytes, measurements, primary, or ontology requires a new
pin and at least a delta review.

No physical `Gamma` construction, metric investigation, curvature unit, or GR
recovery begins until this candidate is terminal.
