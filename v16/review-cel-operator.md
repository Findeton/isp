# Independent hostile review of CEL — operator algebra, null quotients, and exact resources

Date: 2026-08-18  
Seat: O — operator algebra, null quotients, and exact resources  
Target: v16 Paper 7, `Creation-event universality, recoverable records, and exact flag resources`  
Verdict: **ACCEPT-WITH-FIXES**

## 1. Immutable-target and hash audit

I audited candidate commit
`f3c3ef99f1506f01208a670198a91abe27c952d5` and verification commit
`15299d1ee6ffca4ede9b9bd0ae86dfe2dee386c1`; both resolve as commits.  Before
substantive work I read the full runbook, the frozen CEL hostile protocol and
pin, both freeze notes, generic core, complete data-only fixture, scorer,
transcript, complete receipt, generated Paper 7, and candidate-verification
note.  I did not read or consult either other CEL review.

The immutable bindings reproduce exactly:

| object | frozen and observed SHA-256 |
|---|---|
| pin | `83762533fa6dad63acbeb3c13b2db9a63b6533b0ce113a61012d959552fa542d` |
| generic core | `f08b880095e71ac79082d2672ec849dc9ffd1ab66c702a85f2b24165a02aedac` |
| core-freeze note | `01f584c0117a79f61d9dcb2dc352d7ecf291f4176f583882d72c5a13bfd6966c` |
| physical fixture | `8a18a70f1e1b7781806d800c54afd5dcbd10dbac1307db4420bafcb4b57854f2` |
| scorer | `27ee69af161382dfda3de81e1ea4d0edf4d6b4afb8d11d5f30ec7d3e075749c8` |
| fixture-freeze note | `b5bf12b6d8032601ed59a6d8d32d46ea7f4e809c842c3efa7020f3546d4748e7` |
| transcript | `098d6113fb9f3ce0dbf43a28aeec213a5b06235c55556389989e93e1387028f6` |
| receipt | `a2fe34ccbbc8a1049824fd72020da5806e399f7a50a45e9bdf832e7e45a8eeda` |
| Paper 7 | `acf2dafb165d5ceb82bf4bc532b194f760095ce355b0b5ee7c5996df13878f90` |
| candidate verification | `abbc2eba6042a519769986c480931e10accccbea58454df1750453d3a66c7106` |

A no-`.git` archive of the immutable candidate, executed from
`/private/tmp/cel-operator-offtree`, regenerated transcript, receipt, and
paper byte-identically.  All eight canonical payload seals, 44 passing gates,
13 claims, and outer hashes reconcile.  I invoked all 41 physical mutants;
each was refused.  The nine generic public gates pass, and its three public
mutants are refused at their intended gates.  The off-tree replay therefore
authenticates the delivery and its refusal surface.  It does not prove that a
scalar restriction is a physical gluing law or that a chosen flag basis is
gauge invariant.

## 2. Independent method and tools

I rebuilt the operator calculations in
`/private/tmp/cel_operator_independent.py` without importing `cel_core` or
`cel_score`.  The program uses only `Fraction`, an independent
Gaussian-rational type, direct permutation matrices, exact Gaussian
elimination, principal minors, an independent unpivoted Hermitian
`LDL^dagger`, and an independent four-square search.  It reconstructs both
CNOT orders on all inputs, the spectator lift, the complete real-linear null
space for coincident histories, both JCV instruments, their port rotation,
all registered PSD/rank/Gram controls, the zero matrix, and an extra
grammar-obstruction counterexample.

I separately proved the general `2r` theorem rather than extrapolate it from
the four fixture matrices.  Integrity and mutant checks were performed by
`/private/tmp/cel_integrity_check.py`; those scripts are reviewer scratch, not
candidate evidence.

## 3. Exact recomputation table

| object | candidate value | reviewer value | status |
|---|---:|---:|---|
| first CNOT order on inputs `0..7` | only `100 -> 111` printed | `(0,1,3,2,7,6,4,5)` | PASS / EXTENDED |
| second CNOT order on inputs `0..7` | only `100 -> 110` printed | `(0,1,3,2,6,7,5,4)` | PASS / EXTENDED |
| biased completeness | `I_8` | `I_8` | PASS |
| balanced completeness | `I_8` | `I_8` | PASS |
| `100 -> 111` probability | `16/25` versus `1/2` | `16/25` versus `1/2` | PASS |
| idle-spectator lift | same screens, complete | same screens, `I_16` for both kernels | PASS |
| coincident-history raw kernels | unequal | unequal | PASS |
| coincident-history channels | equal | both identity channel | PASS |
| full coincident-history null | not characterized | real dimension `3`: `a+d+2 Re z=0` | NEW LOAD-BEARING CHECK |
| retained calibrated ports on null-equivalent kernels | not run | `(1,0)` versus `(0,1)` | NEW COUNTERCONTROL |
| history exchange | biased fails, balanced fixed | same | PASS |
| shared-token restrictions | `(3/5,4/5)`, `(3/5,5/13)` | same | PASS |
| mismatched restriction | shared value `1/2` refused | same | PASS |
| affine universality price | `2 -> 1` | zero constraint versus `x-y=0`, hence `2 -> 1` | PASS |
| first JCV kernel | `diag(16/25,9/25)` | same | PASS |
| second JCV kernel | same | same | PASS |
| first class operators | implicit | `diag(0,24/25)`, `diag(1,7/25)` | PASS |
| second class operators | implicit | `diag(7/25,1)`, `diag(24/25,0)` | PASS |
| both Stinespring stacks | isometries | `S^dagger S=I_2` | PASS |
| flag vectors | `(0,1)/(24/25,7/25)` and `(7/25,24/25)/(1,0)` | same | PASS |
| unconditioned channel | equal | `rho -> (16/25)rho+(9/25)Zrho Z` for both | PASS |
| fixed-label first-port probability | `0` versus `49/625` | same | PASS |
| port rotation between factors | not printed | `C_2=U C_1`, `U=[[24/25,7/25],[-7/25,24/25]]` | NEW GAUGE CHECK |
| corresponding probability under declared relabel | not printed | `p_1(f0|m0)=p_2(f1|m1)=0` | NEW GAUGE CHECK |
| registered PSD ranks | `[2,2,1,2]` | `[2,2,1,2]` | PASS |
| independent LDL pivots | not printed | `(2,1/2)`, `(2,1/2)`, `(0,1)`, `(1,1,0)` | PASS |
| constructed row counts | `[2,2,1,2]` | `[2,2,1,2]` | PASS |
| zero matrix | theorem text only | empty factor, rank and row count `0` | PASS / EXTENDED |
| non-PSD control | refused | determinant `-3`, refused | PASS |
| `7/5` direct rows | minimum `2` | one row impossible; `(1+3i/5, i/5)` gives two | PASS |
| `diag(7/5,1)` direct rows | minimum `3` | two impossible; displayed three-row factor exact | PASS |
| some factor versus grammar factor | separated | rank-one Gram example exists but violates a one-parent support grammar | PASS / EXTENDED |

The full coincident-history statement is especially important.  For

$$
M=\begin{pmatrix}a&z\\\bar z&d\end{pmatrix},\qquad V_1=V_2=I,
$$

the induced map is

$$
\Phi_M(\rho)=(a+d+2\operatorname{Re}z)\rho.
$$

Its real-linear kernel is therefore three-dimensional, not merely the one
displayed difference `diag(1,-1)`.  Complete kernels occupy the affine
hyperplane `a+d+2 Re z=1`, further intersected with the PSD cone.

## 4. Theorem and proof audit

### 4.1 Recurrence and the null quotient

The CNOT calculation proves a genuine nonselection statement: locality of
the two permutation histories and all-input completeness admit at least two
different diagonal probability kernels that move a calibrated screen.  The
spectator calculation proves the same after tensoring an idle identity.  It
does not derive equality between separately declared contexts; equality is
obtained only after invoking the standing spectator-naturality axiom.

The operational-null quotient is mathematically valid only at a stated
operational grain.  If every future observable factors through the
unconditioned channel `Phi_M`, then `M~M+N` for `N` in the channel kernel is
sound.  It is not sound for a law that also retains a calibrated port or
history decomposition.  For the two displayed null-equivalent kernels, take

$$
C_L=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
C_R=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
$$

They satisfy `C_L^dagger C_L=M_L` and
`C_R^dagger C_R=M_R`; with coincident histories their unconditioned channel
is the same, but fixed two-port probabilities are `(1,0)` and `(0,1)`.
Therefore the qualifier `KERNEL-IDENTITY-ONLY-MODULO-OPERATIONAL-NULL` needs
the words “for the unconditioned operational algebra and every licensed
continuation that factors through it.”

### 4.2 Shared-token restriction and universality

The positive and negative restriction calculations are correct.  They are
coordinate consistency, not a gluing theorem for a dynamical law.  The
fixture stores one triple of rational values and two index maps; it contains
no joint channel, history kernel, overlap interaction, or compatibility
proof.  Thus “shared-token gluing propagates recurrence” is licensed only if
one first postulates that the physical law is a token-indexed scalar section.
Without that postulate, this is a correctly typed equality control.

The `2 -> 1` price is exact but equally transparent: the independent system
has a zero row, while type universality adds `x-y=0`.  It measures the price
of the declared universality dictionary; it does not derive that dictionary.

### 4.3 JCV dilation and gauge

For histories `(I,Z)`, direct expansion gives the four class operators in the
table.  Each family sums to `I` in `sum_j K_j^dagger K_j`, and both induce

$$
\Phi(\rho)=\frac{16}{25}\rho+\frac9{25}Z\rho Z.
$$

The printed flag vectors and fixed-label probabilities are exact.

Before calibration, the two full-rank factors are related by the exact port
rotation

$$
U=\begin{pmatrix}24/25&7/25\\-7/25&24/25\end{pmatrix},\qquad
C_2=UC_1,
$$

so they are two Kraus unravellings of one channel.  Once the flag outcomes are
calibrated, arbitrary left-unitary mixing is no longer gauge.  The surviving
continuous gauges are independent row phases, history rephasings compensated
in coefficient columns, and boundary basis changes with preparations and
effects transported covariantly.  A licensed outcome permutation is gauge
only when the apparatus labels move with it.

That last sentence exposes one unresolved typing choice in the candidate.
The relational weld also declares an input/output reversal carrying the first
stack into the second.  Under that simultaneous relabeling, corresponding
statistics agree: `p_1(f0|m0)=p_2(f1|m1)=0`.  The contrast `0 -> 49/625`
instead holds when the names `m0,f0` are fixed.  Both statements are lawful,
but they cannot be conflated.  If the reversal is gauge, the printed contrast
is not an invariant of that quotient.  If `m0,f0` are physically calibrated,
the contrast is physical but the reversal is a covariance between distinct
calibrated settings, not an identification.  The paper must freeze which
reading it uses.

### 4.4 General Gaussian-rational `2r` theorem

The general theorem is correct.  Let `A` be any finite PSD Hermitian matrix
over `Q(i)`.  At each stage of unpivoted Hermitian elimination, the remaining
Schur complement is PSD.  If its next diagonal pivot is zero, every `2x2`
principal minor through that pivot reads `-|s_jk|^2 >= 0`; hence the entire
residual row and column vanish.  Division by zero is therefore never needed.
All positive pivots are positive rationals, `L` remains over `Q(i)`, and
`rank(A)` equals the number of positive diagonal pivots because `L` is
invertible.

For a positive pivot `d=p/q` in lowest terms, Lagrange's theorem gives

$$
pq=a^2+b^2+c^2+e^2,
$$

so

$$
d=\left|\frac{a+ib}{q}\right|^2+
  \left|\frac{c+ie}{q}\right|^2.
$$

Multiplying the corresponding row of `L^dagger` by those two Gaussian
rationals supplies at most two Gram rows per positive pivot.  This proves
`C^dagger C=A` with at most `2 rank(A)` rows.  The proof includes the zero
matrix, leading/intermediate/trailing zero pivots, arbitrary singular
patterns, and non-real entries.  The registered examples are checks, not the
induction base of the theorem.

### 4.5 Minimal resource witnesses

A positive rational is one Gaussian-rational norm exactly when every prime
`3 mod 4` has even exponent in its reduced numerator-minus-denominator prime
valuation.  The prime `7` occurs to odd exponent in `7/5`, so one row is
impossible.  Yet

$$
\frac75=|1+3i/5|^2+|i/5|^2,
$$

making two rows both sufficient and minimal.

For any two-row factor of the two-column matrix `diag(7/5,1)`, `C` is square
and

$$
\det(C^\dagger C)=|\det C|^2.
$$

Because `7/5` is not a Gaussian-rational norm, no two-row factor exists.  Rank
already excludes fewer than two rows, and the displayed three-row factor

$$
C=\begin{pmatrix}1+3i/5&0\\1/5&0\\0&1\end{pmatrix}
$$

is exact.  Thus “minimum three” is licensed among all direct `Q(i)` Gram
factors, not merely among a special square ansatz.

## 5. Operator, representation, and resource audit

The candidate successfully separates three mathematical objects: a PSD
history kernel, a particular calibrated factor `C`, and a Stinespring stack.
It does not derive the extra relational typing.  The created-cell name,
attachment, allowed support, and relabel maps are fixture data; the scorer
checks their compatibility with the two stacks.  This proves that the
specified instruments admit one supplied relational reading, not that every
Gram factor has that reading or that the attachment is operator-detectable.

An explicit separation is

$$
M=\begin{pmatrix}1&i\\-i&1\end{pmatrix}
  =\begin{pmatrix}1&i\end{pmatrix}^\dagger
   \begin{pmatrix}1&i\end{pmatrix}.
$$

This is PSD of rank one and has a one-row `Q(i)` factor.  A declared support
grammar in which every output row has at most one history parent forces every
off-diagonal Gram entry to zero, so no factor can satisfy that grammar.  “A
factor exists” therefore never implies “the declared catalogue/rewrite can
realize it.”

Likewise, Gram-row count equals orthogonal port count only in the direct
Stinespring implementation.  One multi-level flag, several smaller cells, or
a cascade can encode the same port space with different relational resource
costs.  The theorem prices minimal direct Gaussian-rational Gram rows.  It
does not by itself price cell count, graph growth, cascade depth, or a unique
physical flag dimension.

There is also an implementation-size wall.  The PSD predicate enumerates all
`2^n-1` principal minors.  `factor_integer` uses trial division, and the
four-square constructor nests bounded searches whose running time is
polynomial in the integer magnitude rather than its bit length in the worst
case.  These searches are finite and do not weaken the existence proof, but
the delivered constructor is not a scalable decision procedure.  The
separate continuation-semigroup routine also refuses beyond 4096 elements;
that cap affects the finite record certificates, not the `2r` theorem.

## 6. Counterexamples and unrun controls

1. **Ports revive a channel-null difference.**  The exact `C_L,C_R` pair
   above shows why the null quotient is conditional on discarding calibrated
   ports and every future use of history identity.
2. **The declared relabel moves the calibration.**  `0 -> 49/625` at fixed
   labels becomes equality `0=0` on corresponding relabeled input/output
   ports.  The candidate has not fixed whether that permutation is gauge or a
   physical covariance.
3. **Scalar restrictions are not joint dynamics.**  The gluing fixture would
   pass unchanged if all CNOT histories, channels, and record structures were
   removed.  A genuine successor control needs a joint operator law whose two
   restrictions reproduce local laws.
4. **Gram existence is not grammar existence.**  The rank-one complex matrix
   above violates the one-parent-per-output support grammar despite its
   minimal Gram factor.
5. **Resource minima are implementation-relative.**  No fixture compares one
   qutrit flag with cascaded binary flags, graph-cell count, or locality of
   the dilation.
6. **The constructor has no size stress test.**  No large-bit pivot or
   high-dimensional PSD family probes the exponential principal-minor census
   or magnitude-scale four-square search.
7. **No complete fiber quotient is computed.**  Row phases, history phases,
   port rotations, boundary conjugations, and discrete calibrated relabels
   are described here, but the candidate does not calculate their stabilizer
   and orbit space jointly.

## 7. Consequence and scope reclassification

| statement | reviewer classification |
|---|---|
| overlapping CNOT nonselection | exact finite counterexample to selection by locality/completeness |
| spectator lift | exact tensor control; recurrence follows only after standing naturality is invoked |
| channel-null quotient | exact at the unconditioned algebra; invalid when calibrated ports/history identity remain operational |
| exchange-fixed balanced kernel | exact within the declared exchange orbit |
| shared-token gluing | typed scalar equality control, not a joint dynamical gluing theorem |
| token-disjoint universality `2 -> 1` | exact price of a nomological postulate, not a derivation |
| JCV common kernel and stacks | exact finite reconstruction |
| `0 -> 49/625` | exact at fixed calibration; not invariant under the declared simultaneous relabel |
| port fiber as created cell | one supplied grammar-compatible dilation, conditional on metadata and calibration |
| general `2r` bound over `Q(i)` | proved for every finite PSD Hermitian matrix |
| `7/5` and `diag(7/5,1)` minima | exact minimum direct Gram-row counts `2` and `3` |
| number-field resource hierarchy | direct exact-representation cost, not yet physical cell cost or ontology |
| continuation-stable recoverability | finite grammar-relative certificate; catalogue closure remains open |
| one creation-event layer | useful conditional common interface; no single joint successor/selection law is derived here |
| couplings, catalogue, actualization, backreaction, arbitrary `n`, QFT/GR | correctly unselected or unconstructed |

Proposed frozen-finding disposition:

1. **Preserve** the local-surface nonselection, spectator calculation,
   exchange action, and `2 -> 1` universality price.
2. **Narrow** `RECURRENCE-PROPAGATED-BY-NATURALITY-SYMMETRY-AND-GLUING`:
   naturality and symmetry are declared principles, while the delivered
   gluing arm is a scalar restriction control.
3. **Narrow** `KERNEL-IDENTITY-ONLY-MODULO-OPERATIONAL-NULL` to the
   unconditioned operational algebra and its factor-through continuations.
4. **Preserve** both JCV factorizations and the fixed-label port witness, but
   make its calibration/relabel choice explicit.
5. **Preserve** `GAUSSIAN-RATIONAL-REALIZATION-BOUND-PROVED`; the general
   theorem survives hostile proof audit.
6. **Narrow** “flag resource” to direct orthogonal Gram-row/port resource
   until a relational implementation cost is defined.
7. **Preserve** all stated walls on selected couplings, catalogue,
   actualization, fundamental dynamics, and higher physical reconstructions.

## 8. Grade

**ACCEPT-WITH-FIXES.**

The mathematical core is unusually solid.  All CNOT, completeness,
spectator, exchange, JCV, Stinespring, channel, PSD, rank, determinant, and
minimum-row claims reproduce exactly.  The `2r` construction is a genuine
general theorem, including singular and complex cases, and not merely an
empirical pattern in four examples.

The needed fixes are nevertheless load-bearing for the ontology.  The null
quotient is unconditioned-grain relative; the token fixture is not a joint-law
gluing theorem; the JCV movement depends on which relabelings calibration
allows; and Gram rows are not automatically relational flag cells.  These
corrections narrow the primary to a conditional common creation-event
interface.  They do not reject the exact operator and number-theory advance.

## 9. Numbered repairs and kill conditions

1. State the full coincident-history null space
   `a+d+2 Re z=0` and restrict quotient language to the unconditioned
   operational algebra plus licensed continuations that factor through it.
2. Add the retained-port countercontrol `C_L,C_R`.  Any assertion of raw-law
   recurrence must specify whether port calibration and history identity are
   retained.
3. Reclassify shared-token “gluing” as a scalar equality control.  Promote it
   only after a frozen joint channel/kernel/rewrite has both local laws as
   actual restrictions.
4. Resolve the JCV gauge fork explicitly: either fix `m0,f0` as physical
   calibrations and treat the reversal as covariance, or quotient the
   reversal and drop `0 -> 49/625` as an invariant contrast.
5. Publish the residual gauge: row phases, compensated history phases,
   covariant boundary changes, and only those outcome permutations that
   transport the apparatus calibration.  Do not treat arbitrary Kraus
   rotations as gauge after outcome calibration.
6. Preserve the general `2r` theorem but separate its mathematical proof from
   the exponential principal-minor and magnitude-scale four-square
   implementation.  Register a complexity wall rather than imply scalable
   construction.
7. Replace “minimum flag-cell dimension/resources” by “minimum direct
   `Q(i)` Gram-row/orthogonal-port count” unless a catalogue-level cost
   equivalence is independently proved.
8. Add a grammar-obstruction control such as
   `[[1,i],[-i,1]]`: its Gram factor exists, while a one-parent support rule
   forbids every realization.  Keep some factor, specified instrument, and
   grammar-typed dilation separate.
9. Keep the creation-event headline conditional.  A common vocabulary across
   three fixtures is not yet one selected joint successor law.

A counterexample to the zero-pivot lemma, rational-pivot decomposition, or
`2r` reconstruction would kill the exact resource theorem; I found none.  A
failure of either CNOT completeness or either JCV Stinespring identity would
kill the finite construction; I found none.  The exact counterchecks instead
kill only the unconditional null, gluing, gauge-invariance, and physical
resource promotions identified above.

## 10. Report SHA-256

The canonical SHA-256 of this report, computed after replacing the 64
hexadecimal characters on the next line by 64 ASCII zeroes, is:

`0c4f3f472d8ec49cfe45710c4786e493f28d9ab783c3c7dbc4ddf9640c886455`
