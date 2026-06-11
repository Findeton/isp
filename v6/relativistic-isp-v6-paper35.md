# Paper 35 (v6) - SHARD: The Dressed Base - What g = ln(1-eps) Would Mean, and Where It Could Come From

Preprint, not peer reviewed, version 2026-06-11.

Author: Felix Robles Elvira

Subtitle:

```text
JUNO's first data landed within 0.05 sigma of the dressed ladder
base eps_eff = eps(1-eps) - the value the rung-dressing parameter
g = ln(1-eps) produces - while sitting 1.6 sigma from the
registered bare point.  This paper is the full campaign on what
that value WOULD mean and where it could come from, conducted
under explicit anti-numerology discipline (the value was noticed
AFTER the data; nothing here changes the registration).  Results:
(1) PRECISION PINNING - the registered numbers were computed at
3-digit eps; the exact eps = 0.03176863644658 shifts the
registered point by 0.23 sigma at JUNO-final precision, so all
constants are now pinned at 50 digits.  (2) A NEW THEOREM for the
corpus: the exact binding-defect functional of P8 is reconstructed
(defect = ln(1 + lam t^w) - w[D(h*) - D(eta)], reproducing P8's
40-digit table at every weight), and its SECOND ORDER is derived
in closed form: d2(w) = theta^(2w) [ -1/2 + b w + c w^2 ] with
c = eta (1-theta^2)^3 / (theta^2 (1-theta^2+theta)^2), verified to
1e-26 across w = 3..12.  (3) AN HONEST NEGATIVE that narrows the
search decisively: no reading of single-relation perturbation
theory - first order, two-order, or exact - produces the (1-eps)
factor; the w = 3 defect flips sign at second order (binding is
second-order, as P8 proved), so the marginality eps is a
first-order object and the dressed base CANNOT come from deeper
expansion of one relation.  If real, it lives in the
relation-to-rung BRIDGE.  (4) The data discriminates among bridge
mechanisms NOW: per-rung geometric leakage (1-eps)^x survives at
-0.2 sigma(final); capacity depletion is excluded at 9 sigma, the
normalized-evidence reading at 400+ sigma, the two-sided reading
at 7 sigma.  (5) Look-elsewhere, counted: 6 of 12 natural
one-factor forms fit today, 3 of 12 even at JUNO-final - the
final dataset cannot select within the surviving cluster, so the
entire selection burden falls on the derivation, whose target is
now pinned: the bridge must deliver weight eps(1-eps) per rung
unit - the product of BOTH poles of a sealed binary distinction -
and nothing else.  The charged bracket is robust under the
dressing (6/6 both bases); the oscillation-equivalent scenario
table shows only a derivation or precision cosmology separates
the dressed base from its rivals.
```

## 0. Provenance, and the discipline this paper runs under

The chronology, stated first because it determines what this paper
is allowed to claim.  (i) The undressed spectrum point was
registered, with its expected JUNO-era failure computed and
pre-committed (v6/publishable/paper-VII; Paper 34).  (ii) JUNO's
first measurement appeared (arXiv:2511.14593; *Nature* **654**,
343 (2026)): $\Delta m^2_{21} = (7.50 \pm 0.12)\times 10^{-5}$,
giving $S_\nu = 0.17283 \pm 0.00167$.  (iii) *After* that, we
noticed that the dressed base $\varepsilon_{\mathrm{eff}} =
\varepsilon(1-\varepsilon)$ predicts $S = 0.17275$ — within
$0.05\sigma$ of the new central value.

Item (iii) is a post-diction.  Under the program's own trials
discipline it carries essentially no evidential weight (Section 3
counts the look-elsewhere cost explicitly: six of twelve natural
one-factor forms fit today's data).  What a post-diction *can*
legitimately do is define a sharp target for a derivation and map
what would follow if the derivation existed.  That is this paper's
entire ambition: theoretical analysis of what $g = \ln(1-
\varepsilon)$ would mean, executable derivation attempts inside
the corpus' own binding theory, and the computational receipts
for both.  **Nothing here changes the registration** — the
registered point remains the undressed spectrum, with its
correction record.

Receipts: `code/v6_p35_dressed_base_campaign.py`, canonical
`/tmp/v6_p35_campaign.out`, bit-identical rerun verified; all
constants at 50 digits.

## 1. Three equivalent readings of the value

Exact constants (P8's closed form, $\kappa = \eta(1-\theta^2)/
(1-\theta^2+\theta)$, $\varepsilon = 3\kappa - 1$):

```text
   eps     = 0.031768636446581816
   eps_eff = 0.030759390184906729
   g       = ln(1-eps) = -0.0322842083290128
```

The three readings, algebraically identical:

1. **Rung dressing**: masses $m(x) = \varepsilon^x e^{gx}$ with
   $g = \ln(1-\varepsilon)$ — the form Paper 34's O34.1 target was
   stated in.
2. **Base renormalization**: $m(x) = [\varepsilon(1-
   \varepsilon)]^x$ — the ladder is untouched; its base is not the
   binding weight but $\varepsilon(1-\varepsilon)$.
3. **Per-step survival**: $m(x) = \prod_{k=1}^{x}\varepsilon\,
   (1-\varepsilon)$ — each rung step is a binary event that
   *commits* with weight $\varepsilon$ and *does not leak* with
   weight $(1-\varepsilon)$; equivalently, each step is a sealed
   binary distinction whose weight is the product of both poles.

Reading 3 is the physically suggestive one: $p(1-p)$ is the
product of the two branch weights of a recorded binary
distinction — the same combination whose normalized form
$4p(1-p)$ is the corpus' own commitment-evidence law (P7).  The
*unnormalized* product is what the data wants; the normalized form
is excluded at $428\sigma$ (Section 3).

## 2. Precision pinning (a correction with teeth)

The registered numbers were computed at $\varepsilon = 0.0318$
(three digits).  At exact $\varepsilon$:

```text
   bare point, eps = 0.0318:  S = 0.17555605
   bare point, eps exact:     S = 0.17547212
   shift: 8.4e-5 = 0.23 sigma at JUNO-final precision
   dressed point, eps_eff:    S = 0.17274688
                              (-0.05 s now, -0.22 s at JUNO-final)
```

A quarter-sigma self-inflicted error at the deciding precision is
not acceptable bookkeeping: **all registered comparisons must use
$\varepsilon$ to at least 10 digits from now on**, and the
external registration carries a precision note to this effect.

## 3. What the data already discriminates

**Among dressing mechanisms** (rungs $x \in \{0, \tfrac12, 1\}$,
full spectrum recomputed per law):

```text
   bare (D = 1)                    S = 0.175472   +1.6 s now  +7.1 s final
   geometric leakage (1-eps)^x     S = 0.172747   -0.05 s now -0.22 s final
   capacity (1-eps)^(x(x-1)/2)     S = 0.176205   +2.0 s now  +9.1 s final
   normalized evidence (4e(1-e))^x S = 0.330995   excluded (428 s)
   two-sided (1-eps)^(2x)          S = 0.170061   -1.7 s now  -7.5 s final
```

The data *already* selects the geometric (per-rung-distance)
leakage law within this family and kills the natural rivals: the
quadratic capacity-depletion law, the evidence-normalized law,
and the doubled law.  Whatever derivation is attempted, its
output must be the simple exponential in rung distance.

**Look-elsewhere, counted against ourselves.**  Twelve natural
one-factor forms $\varepsilon \cdot f(\varepsilon)$:

```text
   within 1 sigma of JUNO-now:    6 / 12   (a 'hit' today is cheap)
   within 1 sigma at JUNO-final:  3 / 12   (eps(1-eps), eps/(1+eps),
                                            eps e^-eps  - the cluster)
```

Even the final dataset cannot select within the surviving cluster
(the three forms differ by $0.2\sigma$ at ultimate precision).
Conclusion, stated as the campaign's organizing fact: **experiment
will confirm or kill the one-marginality-factor suppression as a
class; only a derivation can pick the member.**

## 4. The derivation attempt: into the corpus' own binding theory

**Theorem 35.1 (the defect functional, reconstructed).**  The P8
single-relation binding defect is exactly

$$
\mathrm{defect}(w; \lambda) \;=\; \ln(1 + \lambda t^w) \;-\;
w\,[\,D(h^*) - D(\eta)\,], \qquad D(h) = h e^{-h} - \ln\cosh h,
$$

with $t = \tanh h^*$ and $h^*(w, \lambda)$ the commitment fixed
point $\langle s\rangle = e^{-h}$ of P8's scalar equation.
*Receipt*: reproduces all nine printed 40-digit values of P8's
table with worst deviation $4.9\times 10^{-16}$ (the table's own
print precision).  The first-order law $d_1(w) = \theta^w(1 -
w\kappa)$ is re-verified to $10^{-38}$.

**Theorem 35.2 (the exact second order — new).**  Expanding
$h^* = \eta + \lambda h_1 + \lambda^2 h_2$ in the fixed-point
equation and assembling the defect functional gives, in closed
form (all quantities at $\theta$, $\Delta = 1-\theta^2+\theta$):

$$
h_1 = -\frac{(1-\theta^2)\,\theta^{w-1}}{\Delta}, \qquad
h_2 = \frac{(1-\theta^2)\theta^{2w-1} - \tfrac12 G''h_1^2 -
h_1 P'}{\Delta},
$$

with $G'' = -\theta(3-2\theta^2)$, $P' = (1-\theta^2)\theta^{w-2}
[(w-1)(1-\theta^2) - 2\theta^2]$, $D'(\eta) = -\eta\theta$,
$D''(\eta) = -(2-\eta)\theta - (1-\theta^2)$, and

$$
d_2(w) = w\theta^{w-1}(1-\theta^2)h_1 - \tfrac12\theta^{2w}
+ w\eta\theta\, h_2 - \tfrac{w}{2} D'' h_1^2
\;=\; \theta^{2w}\Bigl[-\tfrac12 + b\,w + c\,w^2\Bigr],
$$

$$
c = \frac{\eta\,(1-\theta^2)^3}{\theta^2\,\Delta^2}
= 0.46254616774\ldots, \qquad b = -0.87755242177\ldots
$$

*Receipt*: the closed form matches the high-precision numerical
extraction at every $w \in \{3,\ldots,12\}$ to $1.9\times
10^{-26}$; the intercept is exactly $-\tfrac12$ (the
$\ln$-expansion term), verified to $10^{-24}$.  This is, to our
knowledge, the first piece of the binding theory's second order
in closed form — usable beyond this paper's question.

## 5. The honest negative: the dressed base is NOT in the single relation

With the exact second order in hand, every reading of "the
marginality, more accurately" can be computed:

```text
   eps (registered, first order)        +0.0317686
   two-order reading -(d1+d2)/theta^3   -0.1338075
   exact reading    -defect(3)/theta^3  -0.0525041
   TARGET eps(1-eps)                    +0.0307594
```

None lands anywhere near the target; the second order *flips the
sign* of the $w = 3$ defect ($d_2/d_1 = -5.21$) — the triangle
binds at second order, exactly as P8 proved, and the
"marginality" $\varepsilon$ is a strictly first-order object that
deeper expansion *destroys* rather than refines.

**Verdict (the campaign's central structural result).**  The
dressed base cannot be obtained by computing the single-relation
defect more accurately.  If $\varepsilon_{\mathrm{eff}} =
\varepsilon(1-\varepsilon)$ is physical, it must arise in the
**relation-to-rung bridge** — the identification (I1/I2 in the
P29 audit; corpus-bound, never constructed explicitly) that maps
binding structure to mass-ladder rungs.  And the target for that
bridge is now fully pinned by Sections 1 and 3: *each unit of
rung distance must contribute the product of both poles of a
sealed binary distinction*, $\varepsilon(1-\varepsilon)$ —
unnormalized (the $4p(1-p)$ normalization is excluded at
$428\sigma$), linearly in rung distance (capacity depletion is
excluded at $9\sigma$), once per unit (the doubled law is
excluded at $7.5\sigma$).

Two bridge mechanisms produce exactly this and survive:

- **(M-a) Product-of-poles seam**: a rung step is a sealed binary
  distinction; axiom S demands the distinction be recorded, and a
  recorded distinction carries both branches; its history weight
  is the branch product.
- **(M-b) Geometric leakage**: a rung step commits with weight
  $\varepsilon$ and survives un-screened with weight
  $1-\varepsilon$; $x$ steps compound multiplicatively.

These are observationally identical (both give $D(x) =
(1-\varepsilon)^x$); they differ in what they would imply
elsewhere (M-a ties the ladder to the silent-seam axiom and would
apply wherever distinctions seal; M-b is a statement about
screening dynamics).  Deciding between them *is* constructing the
bridge — named open problem **O35.1**, superseding Paper 34's
O34.1 with the sharper statement: *derive the relation-to-rung
bridge and show its per-rung weight is $\varepsilon(1-
\varepsilon)$ exactly; the pinned target is $g =
-0.0322842083$.*

## 6. What would follow if the bridge derivation lands

1. **The prediction is resurrected as a sharper one.**  $S =
   0.1727469$ exactly (no free parameters), currently at
   $-0.05\sigma$; at JUNO-final it is separated from the bare
   point by $7\sigma$ — the experiment cleanly picks one or kills
   both.
2. **Minimality is rescued, not executed.**  Paper 34 showed the
   minimal texture gives coefficient $1$ in *texture* terms; a
   derived base renormalization means the expected failure of the
   bare point was a wrong constant, not a wrong selection
   principle — and minimality's other load-bearing uses (d = 3,
   the (3,2) tower) are untouched.
3. **The audit chain gains a link.**  $\theta \to \kappa \to
   \varepsilon \to \varepsilon(1-\varepsilon) \to$ ladder: one
   identification (the bridge) becomes a theorem, and the
   registered chain's weakest graded link is discharged.
4. **The corpus inherits cleanly.**  The charged bracket claim is
   unchanged (receipt: 6/6 adjacent steps inside
   $[\,\mathrm{base}^2, \sqrt{\mathrm{base}}\,]$ under both
   bases); the binding laws (P8) are untouched (they use
   $\varepsilon$ as marginality, not as ladder base); only
   ladder-application papers (P23/P25/P28/P29 rows) re-evaluate.

If instead the bridge derivation produces the *bare* base (or a
different factor), the dressed-base reading dies as numerology —
recorded in advance, exactly like the registered point's own
expected death.

## 7. What experiment can and cannot separate

The oscillation-equivalent worlds (all consistent with JUNO-now):

```text
                                S          m1        Sum(m_nu)
   bare point (C=1, C1=1)       0.175472   1.59 meV  60.66 meV
   dressed base (eps_eff)       0.172747   1.54 meV  60.47 meV
   texture survivor (P34)       0.173003   2.08 meV  61.15 meV
   m1 anomaly (C1=1.40)         0.172770   2.23 meV  61.33 meV
```

$S$ separates the bare point from the rest at JUNO-final; it
cannot separate the dressed base from the texture survivor or the
$m_1$ anomaly (all within $\sim 0.7\sigma$ of each other at final
precision), and $\Sigma m_\nu$ spreads by only $\sim 0.9$ meV
across the non-bare scenarios — far below near-term cosmology.
**The dressed base is distinguishable from its rivals only by
possessing a derivation.**  This is not a weakness peculiar to
this proposal; it is the structure of the observable (one number,
several parameters), and we state it rather than imply the data
could do more.

## 8. Algebraic status of the constants

PSLQ at 50 digits with symbolic verification (residuals
$10^{-50}$, i.e. exact):

```text
   11 kappa = eta (7 - 2 theta + theta^2)
   11 eps   = -11 + eta (21 - 6 theta + 3 theta^2)
   11 eps_eff = -22 + eta(63 - 18 theta + 9 theta^2)
                    - eta^2 (36 - 18 theta + 18 theta^2)
   kappa NOT in Q(theta) at height 1e8: the 'transcendental-form'
   grading (P7) is receipted; eps_eff inherits it (eta-quadratic).
```

The $\varepsilon_{\mathrm{eff}}$ relation is the unique low-height
one — there is no cheaper numerological route to the dressed base
than through $\kappa$ itself, which closes off one class of
spurious "derivations" in advance.

## 9. Verdict and ledger updates

**Verdict.**  The dressed base is a coherent, sharply defined,
currently data-favored hypothesis with three equivalent readings,
a pinned 10-digit target, a derivation route that is now *narrowed
by theorem* (not in the single relation — in the bridge), an
exact second-order toolkit built for whoever constructs that
bridge, and a fully counted look-elsewhere cost that keeps its
present 0.05-sigma agreement from being mistaken for evidence.
It is the program's best-defined open derivation, and nothing
more until O35.1 is executed.

**Ledger updates:**

- **O35.1** (supersedes O34.1): derive the relation-to-rung
  bridge; success criterion: per-rung weight
  $\varepsilon(1-\varepsilon)$ exactly ($g = -0.0322842083$,
  pinned); failure criterion: any other factor, in which case the
  dressed-base reading is withdrawn as numerology.  *[Paper 36
  executed the campaign: all mechanical routes excluded with
  exact receipts; the sole survivor is the coherence
  identification, and O35.1 reduces to one question: can a record
  be sealed in modulus and silent in phase?]*
- **Precision rule** (new, corpus-wide): registered comparisons
  use $\varepsilon$ at $\ge 10$ digits; the 3-digit rounding in
  the registration is corrected by a dated note (0.23 sigma at
  JUNO-final).
- **The registration is unchanged**: the registered point remains
  the undressed spectrum; the dressed point may be registered
  only if O35.1 lands, with this paper as its provenance record.

## Receipts

```text
code/v6_p35_dressed_base_campaign.py   the whole campaign
/tmp/v6_p35_campaign.out               canonical (BIT-IDENTICAL rerun)
P0 exact constants (50 dps); P1 precision pinning (0.23 s shift);
P2 defect functional reconstructed (worst 4.9e-16 vs P8 table);
P3 d1 re-verified (1e-38), d2 closed form derived + verified
   (1.9e-26, w = 3..12), intercept -1/2 exact (1e-24);
P3b no single-relation reading reaches eps(1-eps);
P4 dressing-law table (leakage -0.22 s final; rivals 7-428 s);
P5 look-elsewhere 6/12 now, 3/12 final; P6 charged bracket 6/6
   both bases; P7 scenario degeneracy (Sum spread ~0.9 meV);
P8s exact algebraic relations (residuals 1e-50), kappa not in
   Q(theta) at height 1e8.
```
