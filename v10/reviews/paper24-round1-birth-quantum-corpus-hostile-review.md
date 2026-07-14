# Paper 24 round 1 — birth/quantum/corpus hostile review

**Frozen paper target:** commit
`a680c06749c2c25bbd6ce28098c4afdae6c1e51a`.

**Lane:** D24--D35 birth and reception inheritance, the common-input quantum
instrument, D-origin evidence, corpus/profinite/V9 synthesis, ontology and the
terminal claim ceiling.

**Verdict:** **MAJOR REVISION. THE D35d QUANTUM, BIRTH AND EVIDENCE RESULTS
REPRODUCE, BUT PAPER 24 PRINTS A FALSE CALL-PROBABILITY FORMULA, MISSTATES THE
D31 THEOREM AS A LOCALITY RESULT, AND LISTS A CORPUS EXECUTABLE THAT FAILS IN
THE PAPER'S OWN COMMIT.**

**Count:** **0 blockers / 3 majors / 2 minors / 3 nits.**

None of the three majors refutes the accepted D35d rooted family. One is a
paper equation that omits the executable's degree-dependent idle mass, one is
a false synthesis of an earlier theorem, and one is a historical-census
boundary bug exposed by adding Paper 24 itself. All have determinate repairs.

## 1. Reproduction and independent reconstruction

### 1.1 Terminal D35d receipt — pass

Fresh `PYTHONHASHSEED=1357911` and `2468022` executions of
`d35d_typed_identity_terminal_exact.py` exited zero, were byte-identical to
each other and the committed receipt, and reproduced:

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

The standalone D24 executable passed `7/7` under fresh seed `97531`; its fresh
stdout hash was
`4d3b6fdcedad4969fa264a96b67e6adfd5c760d924b9a75e32a42c0d644306ff`.
The standalone D27 Busch executable passed `5/5` under fresh seed `86420`; its
fresh stdout hash was
`d2290d51397b980f41eea0962f69412ec93d6ee66994dd88c5a5f29f3f8dcf5b`.

### 1.2 Independent `8 -> 48` instrument — pass

I reconstructed the local maps from the lexicographic `|A B C>` basis without
calling the candidate's instrument summary. In menu order

```text
birth, fork(B,C), idle, visit-B, visit-C
```

their shapes are

```text
16x8, 8x8, 8x8, 8x8, 8x8.
```

Injecting them at row offsets `0,16,24,32,40` gives five `48x8` maps. Exact
rational multiplication independently returns:

```text
self Grams equal I_8                       5/5
unordered cross Grams equal 0_8          10/10
Q1 weighted Gram sum equals I_8             yes
Q2 weighted Gram sum equals I_8             yes.
```

The exact weights are:

```text
Q1: birth 1/4, fork 1/8, idle 3/8, visit-B 1/8, visit-C 1/8;
Q2: birth 1/5, fork 1/10, idle 2/5, visit-B 3/20, visit-C 3/20.
```

This confirms Paper 24 section 6 at its **registered root-local sector**
scope. The direct sum is a classical-output instrument; it is not a coherent
amplitude sum over alternative support graphs.

### 1.3 D24 `B_g` versus opportunity `q` — pass

The independently reconstructed birth isometry obeys

```text
B_g^dag (I_ABC tensor |1><1|_N) B_g
  = g (|1><1|_A tensor I_B tensor I_C)
```

exactly, with `g=9/25` in Q1 and `g=16/25` in Q2. Thus the paper correctly
separates:

```text
q_birth   probability of selecting the structural birth alternative;
B_g       conditional newborn-content isometry after selection;
g         unselected coupling inside that content map.
```

D24 supplies an admitted identifiable one-parent family, not the opportunity
selector or a unique reception law. D27's thermal receiver independently
confirms that the admitted trace-norm-isometric CP class is broader than one
isometry: preparation-independent mixtures of isometries with orthogonal
ranges. Paper 24 preserves that distinction and does not promote D24 over the
Busch class.

### 1.4 D-origin intervention and disconnected control — pass

I independently paired `do(D=0)` and `do(D=1)` histories by generated event
address, initiator, operation, typed legs, route and coupling, excluding the
source value and the candidate's pairing key. Results:

```text
Q1: same 16 structural atoms; 6 queried, 10 unqueried; reach mass 1/16;
Q2: same 16 structural atoms; 6 queried, 10 unqueried; reach mass 3/40;
paired probability mismatches                                      0;
A2 intervention mismatches outside queried histories               0.
```

The disconnected control is the exact marked event/actor-incidence copy

```text
A -> B -> D       seed, seed-birth, seed-birth, source-seal
u -> v -> w       seed, seed-birth, seed-birth, source-seal,
```

up to identity domain and disconnection. Flipping its terminal bit leaves the
complete connected 16-atom physical distribution—not merely the coarse root
tuple—exactly unchanged in both cells. Sections 7.1--7.4 state the limited
operational result honestly: one declared classical channel in one supplied
transport grammar, not generic quantum signalling or ancestry-as-influence.

## 2. What the synthesis gets right

The following paper-level conclusions survive hostile comparison with the
D24--D35 terminal record:

- realized evidence reach is binary, while its pre-completion probability is
  a measure of completed histories containing the licensed route;
- record-wire succession is causal order, not elapsed time;
- D24 content, structural opportunity and numerical selection weights are
  distinct layers;
- the executable is a logical actor/mailbox model with one disclosed shared
  event DAG and joint carrier vector, not OS processes or actor-owned
  wavefunctions;
- the completed measure is classical and rooted/laminar; coherent graph-sector
  completion remains open;
- the D35 law and Paper 23's D34b law ask different predictive questions, so
  their finite call boundary and whole-component theorem do not contradict;
- the finite rooted-call tower is related to but not identified with the V9
  stem spectrum;
- a full profinite bridge still needs bonding maps for all marked sectors,
  topology/continuity, nonlaminar overlap consistency and quantum positivity;
- inverse limits preserve compatible finite laws but do not select Q1 or Q2;
- no D35 result establishes cone roundness, dimension, the `S^2` channel
  manifold, metres, seconds, `G` or the actual law of nature; and
- the root, ownership orientation, Q, g, peer/cycle/join sectors and overlap
  law remain supplied or open.

The terminal limitations in sections 11--13 are unusually explicit and must
survive the repairs below unchanged.

## 3. Major findings

### M1 — section 4.4's call-diamond probability formula omits folded idle mass

The paper first correctly says that unavailable visit/fork mass is assigned to
idle. It then defines the base cell

```text
q = (q_idle,q_birth,q_visit,q_fork)
```

and prints

```text
P(D | H,A1)
  = product_v q(action at v) / number of selected v-local port sets.
```

That equation is false for idle at degree zero or one. Let `d` be the actor's
current child count. The executable's actual local menu is

```text
p_v(birth)       = q_birth;
p_v(visit port)  = q_visit / d                         if d >= 1;
p_v(fork pair)   = q_fork / binomial(d,2)             if d >= 2;
p_v(idle)        = q_idle
                   + 1[d=0] q_visit
                   + 1[d<2] q_fork.
```

The correct diamond law is the product of these **effective local-menu**
probabilities, not the product of the four base tuple entries.

Exact counterexamples from the paper's own cells are:

```text
Q1 leaf idle:                         actual 3/4, printed factor 3/8;
Q1 degree-one idle:                   actual 1/2, printed factor 3/8;
Q1 A-visit-B / B-idle history:        actual 1/16, paper formula 3/64;
Q1 A-visit-B / B-visit-D / D-idle:    actual 3/128, paper formula 3/256;

Q2 leaf idle:                         actual 4/5, printed factor 2/5;
Q2 degree-one idle:                   actual 1/2, printed factor 2/5;
Q2 A-visit-B / B-idle history:        actual 3/40, paper formula 3/50;
Q2 A-visit-B / B-visit-D / D-idle:    actual 9/250, paper formula 9/500.
```

The executable, its normalization, the 16 atoms and the reach masses are
correct; only the paper's displayed general formula is wrong. This remains a
major because section 4.4 presents the formula as the mathematical law from
which normalization and covariance follow.

**Required repair:** replace the equation by the degree-dependent menu above,
write `P(D|H,A1)=product_v p_v(action_v,ports_v | local state_v)`, and add at
least one degree-zero and one degree-one exact branch check. Preserve the
separate proof that each effective menu sums to one.

### M2 — D31 does not force local graph/collar dependence

Section 2.2 says D31 pushes a serious selector toward local graph/collar
structure. Section 11.4 is stronger and lists

```text
local graph/collar dependence forced by D31.
```

The cited theorem explicitly denies that conclusion. D31 proves that in the
none-free unbounded-growth grammar, a stationary path-covariant birth-positive
kernel whose per-labelled weights depend only on the unsealed count `u` is
pure birth. Its honest conclusion is:

```text
an interacting stationary path-covariant kernel must consult state richer
than u; locality is NOT specifically forced.
```

The surviving information may be local degree/collar data, but D31 also leaves
component data and global invariants admissible. Moreover its covariance
premise is itself the recorded-history-versus-gauge physical fork.

This is a major corpus-synthesis error because Paper 24 twice attributes a
stronger selection principle to a terminal theorem than that theorem proves,
and the false version favors the paper's proposed local-diamond program.

**Required repair:** change section 2.2 item 8 to “D31 excludes the
stationary/path-covariant graph-blind unbounded-growth class and forces only
richer-than-count sensitivity.” In section 11.4 replace the false bullet by:

```text
richer-than-count state dependence forced by D31 under its covariance fork;
local collar dependence imposed separately as the desired locality condition.
```

Carry the birth-positivity, none-free, unbounded-growth and covariance-fork
hypotheses wherever the no-go is summarized.

### M3 — the advertised pre-D35 corpus executable fails at the Paper 24 commit

The historical receipt is internally consistent:

```text
selected paths                 441
category-relevant paths        427
stream SHA-256
b0e4c7e0be1c8587b5f3b35e36a834fa8f485cf4bd7cfbb61331017bcd1541b7
inventory source SHA-256
49e1de97450a83763aa478bedacc8c13793af7e569bafe79acb9045f858d663a
receipt SHA-256
fde217caff5e31c670cfc49c98ecea12048a3a2cd28ae1334026999f0f676fc6.
```

But the executable does not encode a historical manifest or commit cutoff. It
dynamically scans current V1--V10 files and excludes only filenames containing
`d35`. At commit `a680c06`, Paper 24 itself satisfies the selector. Fresh runs
under seeds `42424243` and `86753099` both abort before producing a receipt:

```text
AssertionError: (442, 441).
```

Comparing the current selector output to the committed 441 receipt gives:

```text
newly selected path
v10/relativistic-isp-v10-paper24-the-next-click-is-a-causal-diamond-not-a-clock-race.md

missing historical paths
none.
```

Thus the paper's historical number is not shown false; rather, the primary
reproducibility artifact listed in section 14 cannot reproduce it in the
paper's own tree. The same failure will recur for every later non-D35 paper or
note matching the dynamic selector.

**Required repair:** freeze the antecedent boundary as an explicit manifest of
the 441 paths and their expected hashes, or run the census against a pinned git
tree/commit. Do not patch this only by excluding the string `paper24`, which
would fail again at Paper 25. Rerun the manifest-based census at the Paper 24
commit, preserve the historical stream if all antecedent bytes match, update
the inventory source/receipt hashes, and state the frozen cutoff in sections
2.1 and 14.

## 4. Minor findings

### m1 — the eight-dimensional input is root-local, not the full initial carrier

Section 6 begins:

> “The root initially carries three qubits, A, B and C.”

The supplied initial carrier has four connected factors, `A,B,C,D`, hence full
dimension 16. D is not a zero-information fiction: its exact initial one
probability is `1296/15625` in Q1 and `4096/15625` in Q2. The accepted
eight-dimensional domain is the **registered root-local A/B/C sector**; D and
any later outside factors are identity spectators for that local instrument.

The section eventually says “registered local sector,” so the operator theorem
is not wrong. The opening ontology sentence is.

**Required repair:** write: “The registered root-local sector consists of A
and its immediate children B,C and has dimension eight. The complete initial
carrier also contains D; every displayed local map is extended by identity on
D and other external spectators.” Do not call 48 the universe-carrier output
dimension.

### m2 — “an executable rooted universe” exceeds the accepted noun

The subtitle advertises “an executable rooted universe,” while the abstract,
sections 1, 11 and 13 repeatedly and correctly say the object is a supplied
A-rooted nested-call family and **not** a root-free universe law. The prominent
subtitle should not use the larger noun that the body refuses.

**Required repair:** replace it with “an executable rooted history family” or
“an executable rooted actor model.” The accepted terminal noun remains

```text
TIMELESS ROOTED NESTED-CALL FAMILY / EXECUTABLE.
```

## 5. Nits

### n1 — normalization is not what proves termination

The abstract says “Exact local normalization proves finite termination and
construction-order covariance.” Termination is proved by strict descent on a
finite ownership tree plus exclusion of same-call newborn queries.
Normalization proves total probability one.

**Repair:** split the sentence: strict descent proves termination; effective
local normalization and commuting incomparable operations prove the
probability/covariance statements.

### n2 — three clean `0B/0M/0m/0n` reports contain twelve, not nine, zero entries

Section 14 says the terminal round “closes with nine zeroes” and then prints
three four-field zero reports. Either say “three clean terminal reports” or
“twelve zero entries.”

### n3 — write the channel manifold as `S^2`, not `S2`

Sections 11.4 and 12 use `S2`. The inherited many-clocks/few-factors object is
the two-sphere `S^2`. This is notation only; no D35 result derives or tests the
bridge.

## 6. Final disposition

| Paper claim | Disposition |
|---|---|
| D35d receipt and hashes | pass |
| D24 newborn instant and isometry | pass |
| `q_birth` / `B_g` / `g` separation | pass |
| D25/D27 broader Busch-class wording | pass |
| Common `8 -> 48` local instrument | pass after root-local scope repair |
| Five self / ten cross / weighted Gram identities | pass |
| Coherent graph-sector refusal | honest |
| D-origin paired intervention | pass |
| Reach masses `1/16`, `3/40` | pass |
| Isomorphic disconnected record gadget | pass |
| General local branch-probability equation | **false; major** |
| 441/427 historical receipt | internally correct |
| Corpus executable at Paper 24 commit | **fails; major** |
| D31 theorem synthesis | **false locality promotion; major** |
| Profinite versus stem-spectrum distinction | honest |
| V9 cone/dimension/units refusal | honest |
| Root-free/uniqueness/nature-law refusal | honest |

**Final count:** **0B / 3M / 2m / 3n.**

**Final recommendation:** retain the paper's causal answer and the complete
D35d evidence package, but withhold paper-level terminal status. Repair the
effective-menu equation, restore D31's actual theorem width, and make the
pre-D35 corpus boundary reproducible from the current tree. Then narrow the
two ontology phrases and apply the three small wording corrections before the
next hostile round.
