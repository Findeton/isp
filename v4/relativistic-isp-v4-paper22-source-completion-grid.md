# Relativistic ISP V4 Paper 22: Source Completion Grid

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

## 0. Purpose

Paper 21 ended with a two-layer decision:

$$
\boxed{
\hbox{source-equivalence supplies admissible form; a licensed source supplies
numbers.}
}
$$

Paper 22 makes that decision exhaustive.  There are two allowed form laws:

$$
\boxed{
\begin{array}{ll}
\mathrm{L1}:&\ell=B\Phi,\\
\mathrm{L2}:&\ell=B\Phi+{\mathcal A}^{hol}.
\end{array}
}
$$

There are three number-source families:

$$
\boxed{
\begin{array}{ll}
\mathrm{F1}:&\hbox{GR/SM calibrated source},\\
\mathrm{F2}:&\hbox{instrument/GCR operational source table},\\
\mathrm{F3}:&\hbox{boundary/action/variational source law}.
\end{array}
}
$$

This gives six source-completion routes:

$$
\boxed{
(L1,F1),\ (L2,F1),\ (L1,F2),\ (L2,F2),\ (L1,F3),\ (L2,F3).
}
$$

Paper 22 also keeps the null route:

$$
\boxed{
\mathrm{NULL}:\hbox{ no licensed number source}.
}
$$

The goal is to audit all seven possibilities.

## 1. Common Bridge Notation

Use the Paper-20 triangle:

$$
\boxed{
s_0\to s_1,\qquad s_1\to s_2,\qquad s_0\to s_2.
}
$$

The corrected value one-form is:

$$
\boxed{
\ell=(\ell_{01},\ell_{12},\ell_{02}).
}
$$

The cycle defect is:

$$
\boxed{
\Omega_{012}
=
\ell_{01}+\ell_{12}-\ell_{02}.
}
$$

The flat law \(L1\) requires:

$$
\boxed{
\Omega_{012}=0.
}
$$

The curved law \(L2\) requires:

$$
\boxed{
\Omega_{012}=H(012)
}
$$

for an independently licensed cycle source \(H\).

## 2. Common Audit Criteria

Each route is audited by six tests:

$$
\boxed{
\begin{array}{ll}
\mathrm{A1}:&\hbox{predeclared before the value query},\\
\mathrm{A2}:&\hbox{falsifiable by a finite bridge table},\\
\mathrm{A3}:&\hbox{compatible with product composition},\\
\mathrm{A4}:&\hbox{compatible with coarse-graining},\\
\mathrm{A5}:&\hbox{noncircular, not row-label repackaging},\\
\mathrm{A6}:&\hbox{numerically useful}.
\end{array}
}
$$

The possible verdicts are:

$$
\boxed{
\mathrm{PASS},\quad
\mathrm{CONDITIONAL},\quad
\mathrm{OPEN},\quad
\mathrm{FAIL}.
}
$$

## 3. Route P22-L1F1: Flat GR/SM Potential

### Definition

Route \(L1F1\) uses GR/SM calibration to print numbers:

$$
\boxed{
\ell_{ij}^{GRSM}
=
\log
\frac{W_{ij,+}^{GRSM}}{W_{ij,-}^{GRSM}}
-
\log
\frac{\rho_{ij,+}^{op}}{\rho_{ij,-}^{op}}.
}
$$

and then asks whether:

$$
\boxed{
\ell^{GRSM}=B\Phi.
}
$$

Equivalently:

$$
\boxed{
\Omega_{012}^{GRSM}=0.
}
$$

### Audit

$$
\boxed{
\begin{array}{c|c|c}
\hbox{test} & \hbox{status} & \hbox{reason}\\
\hline
\mathrm{A1} & \mathrm{PASS} & \hbox{GR/SM rule can be frozen before query}\\
\mathrm{A2} & \mathrm{PASS} & \Omega^{GRSM}\ne0\hbox{ falsifies flatness}\\
\mathrm{A3} & \mathrm{CONDITIONAL} & \hbox{requires GR/SM product calibration}\\
\mathrm{A4} & \mathrm{CONDITIONAL} & \hbox{requires stable reduction of }W^{GRSM}\\
\mathrm{A5} & \mathrm{PASS} & \hbox{physical calibration is not a row label}\\
\mathrm{A6} & \mathrm{PASS} & \hbox{prints }\ell\hbox{ if GR/SM data are supplied}
\end{array}
}
$$

### Current Status

The current corpus does not print the required three GR/SM edge ratios.
Therefore:

$$
\boxed{
\mathrm{P22\text{-}L1F1}^{cur}
=
\mathrm{OPEN}.
}
$$

### Failure Mode

If:

$$
\boxed{
\Omega_{012}^{GRSM}\ne0,
}
$$

then \(L1F1\) fails, but \(L2F1\) may still survive.

## 4. Route P22-L2F1: Curved GR/SM Connection

### Definition

Route \(L2F1\) uses GR/SM calibration for \(\ell\) and allows a licensed
holonomy correction:

$$
\boxed{
\ell^{GRSM}=B\Phi+{\mathcal A}^{hol},
\qquad
\oint_{012}{\mathcal A}^{hol}=H^{GRSM}(012).
}
$$

It requires:

$$
\boxed{
\Omega_{012}^{GRSM}=H^{GRSM}(012).
}
$$

### Audit

$$
\boxed{
\begin{array}{c|c|c}
\hbox{test} & \hbox{status} & \hbox{reason}\\
\hline
\mathrm{A1} & \mathrm{CONDITIONAL} & H^{GRSM}\hbox{ must be predeclared}\\
\mathrm{A2} & \mathrm{PASS} & \Omega^{GRSM}\ne H^{GRSM}\hbox{ falsifies it}\\
\mathrm{A3} & \mathrm{CONDITIONAL} & H^{GRSM}\hbox{ must add under products}\\
\mathrm{A4} & \mathrm{CONDITIONAL} & H^{GRSM}\hbox{ must reduce consistently}\\
\mathrm{A5} & \mathrm{CONDITIONAL} & H^{GRSM}\hbox{ must not be residual-fit}\\
\mathrm{A6} & \mathrm{PASS} & \hbox{prints numbers if }W^{GRSM},H^{GRSM}\hbox{ print}
\end{array}
}
$$

### Current Status

The current corpus does not print \(H^{GRSM}(012)\).  Therefore:

$$
\boxed{
\mathrm{P22\text{-}L2F1}^{cur}
=
\mathrm{OPEN}.
}
$$

### Failure Mode

If \(H^{GRSM}\) is defined only after observing \(\Omega^{GRSM}\), this route
is:

$$
\boxed{
\mathrm{FAIL\ by\ holonomy\ smuggling}.
}
$$

## 5. Route P22-L1F2: Flat Instrument/GCR Potential

### Definition

Route \(L1F2\) asks an operational or GCR table to print:

$$
\boxed{
Y,\quad
\ell_{01},\ell_{12},\ell_{02},\quad
\zeta_{01},\zeta_{12},\zeta_{02}.
}
$$

Then it requires:

$$
\boxed{
\Omega_{012}^{op/GCR}=0
}
$$

within declared tolerance.

### Audit

$$
\boxed{
\begin{array}{c|c|c}
\hbox{test} & \hbox{status} & \hbox{reason}\\
\hline
\mathrm{A1} & \mathrm{OPEN} & \hbox{instrument/GCR protocol not printed}\\
\mathrm{A2} & \mathrm{PASS} & \Omega\ne0\hbox{ falsifies flatness}\\
\mathrm{A3} & \mathrm{OPEN} & \hbox{product behavior of records unproved}\\
\mathrm{A4} & \mathrm{OPEN} & \hbox{coarse-grained readout stability unproved}\\
\mathrm{A5} & \mathrm{OPEN} & \hbox{must exclude row-label repackaging}\\
\mathrm{A6} & \mathrm{PASS} & \hbox{would print numbers if table exists}
\end{array}
}
$$

### Current Status

Paper 20 printed the table schema but not actual entries.  Therefore:

$$
\boxed{
\mathrm{P22\text{-}L1F2}^{cur}
=
\mathrm{OPEN}.
}
$$

### Failure Mode

If repeated-edge defects persist:

$$
\boxed{
D_{rep}\ne0,
}
$$

then \(Y\) is not a sufficient scalar readout.  If triangle defects persist:

$$
\boxed{
\Omega\ne0,
}
$$

then flatness fails.

## 6. Route P22-L2F2: Curved Instrument/GCR Connection

### Definition

Route \(L2F2\) uses operational/GCR data and allows stable licensed
readout curvature:

$$
\boxed{
\ell^{op/GCR}=B\Phi+{\mathcal A}^{hol}_{op/GCR}.
}
$$

It requires:

$$
\boxed{
\Omega_{012}^{op/GCR}=H^{op/GCR}(012)
}
$$

with \(H^{op/GCR}\) printed by the instrument/GCR protocol, not fitted after
the defect.

### Audit

$$
\boxed{
\begin{array}{c|c|c}
\hbox{test} & \hbox{status} & \hbox{reason}\\
\hline
\mathrm{A1} & \mathrm{OPEN} & H^{op/GCR}\hbox{ not printed}\\
\mathrm{A2} & \mathrm{PASS} & \Omega\ne H\hbox{ falsifies it}\\
\mathrm{A3} & \mathrm{OPEN} & \hbox{holonomy product law unproved}\\
\mathrm{A4} & \mathrm{OPEN} & \hbox{holonomy reduction law unproved}\\
\mathrm{A5} & \mathrm{OPEN} & \hbox{must not be residual-fitting}\\
\mathrm{A6} & \mathrm{CONDITIONAL} & \hbox{numerical if }Y,\ell,H,\zeta\hbox{ print}
\end{array}
}
$$

### Current Status

The current corpus does not print the operational/GCR holonomy table.
Therefore:

$$
\boxed{
\mathrm{P22\text{-}L2F2}^{cur}
=
\mathrm{OPEN}.
}
$$

### Failure Mode

If \(H^{op/GCR}\) is declared only as:

$$
\boxed{
H^{op/GCR}(C):=\Omega_C,
}
$$

after the bridge residual is computed, the route fails by smuggling.

## 7. Route P22-L1F3: Flat Boundary/Action Potential

### Definition

Route \(L1F3\) asks a finite boundary/action/variational principle to print:

$$
\boxed{
\Phi=\Phi_{\partial/action}.
}
$$

Then:

$$
\boxed{
\ell=B\Phi_{\partial/action}.
}
$$

### Audit

$$
\boxed{
\begin{array}{c|c|c}
\hbox{test} & \hbox{status} & \hbox{reason}\\
\hline
\mathrm{A1} & \mathrm{PASS/OPEN} & \hbox{passes if action law is declared}\\
\mathrm{A2} & \mathrm{PASS} & \hbox{wrong }\Phi\hbox{ fails bridge table}\\
\mathrm{A3} & \mathrm{CONDITIONAL} & \hbox{needs additive/local action}\\
\mathrm{A4} & \mathrm{CONDITIONAL} & \hbox{needs boundary reduction rule}\\
\mathrm{A5} & \mathrm{PASS} & \hbox{if action is not fitted to rows}\\
\mathrm{A6} & \mathrm{PASS} & \hbox{prints numbers if }\Phi\hbox{ explicit}
\end{array}
}
$$

### Current Status

No explicit finite action/boundary formula for \(\Phi\) is printed in the
current corpus.  Therefore:

$$
\boxed{
\mathrm{P22\text{-}L1F3}^{cur}
=
\mathrm{OPEN}.
}
$$

### Failure Mode

If the proposed \(\Phi_{\partial/action}\) is defined by solving:

$$
\boxed{
B\Phi=\ell
}
$$

after \(\ell\) is known, then it is not an action law.  It is a fit.

## 8. Route P22-L2F3: Curved Boundary/Action Connection

### Definition

Route \(L2F3\) asks a finite boundary/action/variational principle to print:

$$
\boxed{
\Phi_{\partial/action}
\quad\hbox{and}\quad
H_{\partial/action}(C)
}
$$

or equivalently:

$$
\boxed{
{\mathcal A}^{hol}_{\partial/action}.
}
$$

Then:

$$
\boxed{
\ell=B\Phi_{\partial/action}+{\mathcal A}^{hol}_{\partial/action}.
}
$$

### Audit

$$
\boxed{
\begin{array}{c|c|c}
\hbox{test} & \hbox{status} & \hbox{reason}\\
\hline
\mathrm{A1} & \mathrm{PASS/OPEN} & \hbox{passes if action prints }H\hbox{ first}\\
\mathrm{A2} & \mathrm{PASS} & \hbox{wrong curvature fails bridge table}\\
\mathrm{A3} & \mathrm{CONDITIONAL} & \hbox{needs additive action holonomy}\\
\mathrm{A4} & \mathrm{CONDITIONAL} & \hbox{needs curvature reduction law}\\
\mathrm{A5} & \mathrm{PASS/FAIL} & \hbox{fails if }H\hbox{ is fitted residual}\\
\mathrm{A6} & \mathrm{PASS} & \hbox{prints numbers if action is explicit}
\end{array}
}
$$

### Current Status

No explicit finite action/boundary holonomy law is printed.  Therefore:

$$
\boxed{
\mathrm{P22\text{-}L2F3}^{cur}
=
\mathrm{OPEN}.
}
$$

### Failure Mode

If the action prints \(H\) but \(H\) does not satisfy:

$$
\boxed{
H(C_1+C_2)=H(C_1)+H(C_2),
}
$$

then the connection law fails product/cycle consistency.

## 9. Null Route P22-NULL: No Licensed Number Source

### Definition

The null route assumes:

$$
\boxed{
\hbox{no }W^{GRSM},\quad
\hbox{no }Y/\ell/\zeta\hbox{ table},\quad
\hbox{no }\Phi,\quad
\hbox{no }H.
}
$$

### Theorem 9.1: Null Route No-Squeeze

Under the null route, the same-law bridge values remain undetermined.

Proof.  This is Paper 20's no-squeeze theorem and Paper 21's no-free-numbers
theorem.  The form law can restrict the shape of admissible values, but no
numerical source prints the boundary values, edge values, or cycle values.
Therefore \(\ell\) remains uncomputed. \(\square\)

### Verdict

$$
\boxed{
\mathrm{P22\text{-}NULL}
=
\mathrm{FAIL}.
}
$$

This is the support-only endpoint.

## 10. Seven-Route Audit Table

The full route table is:

$$
\boxed{
\begin{array}{c|c|c|c}
\hbox{route} & \hbox{name} & \hbox{current verdict} & \hbox{main missing object}\\
\hline
\mathrm{L1F1} & \hbox{Flat GR/SM Potential} & \mathrm{OPEN} &
\ell^{GRSM}_{ij}\\
\mathrm{L2F1} & \hbox{Curved GR/SM Connection} & \mathrm{OPEN} &
H^{GRSM}\\
\mathrm{L1F2} & \hbox{Flat Instrument/GCR Potential} & \mathrm{OPEN} &
Y,\ell,\zeta\\
\mathrm{L2F2} & \hbox{Curved Instrument/GCR Connection} & \mathrm{OPEN} &
H^{op/GCR}\\
\mathrm{L1F3} & \hbox{Flat Boundary/Action Potential} & \mathrm{OPEN} &
\Phi_{\partial/action}\\
\mathrm{L2F3} & \hbox{Curved Boundary/Action Connection} & \mathrm{OPEN} &
H_{\partial/action}\\
\mathrm{NULL} & \hbox{No Number Source} & \mathrm{FAIL} &
\hbox{all source numbers}
\end{array}
}
$$

## 11. Ranking By Present Usefulness

Current practical ranking:

$$
\boxed{
\begin{array}{c|c|c}
\hbox{rank} & \hbox{route} & \hbox{reason}\\
\hline
1 & \mathrm{L1F1} & \hbox{fastest calibrated numerical route if GR/SM table prints}\\
2 & \mathrm{L1F2} & \hbox{best intrinsic flat route if instrument/GCR table prints}\\
3 & \mathrm{L2F2} & \hbox{best intrinsic curved route if stable holonomy appears}\\
4 & \mathrm{L2F1} & \hbox{possible GR/SM curvature, but must avoid post-hoc }H\\
5 & \mathrm{L1F3} & \hbox{excellent if action potential is discovered}\\
6 & \mathrm{L2F3} & \hbox{excellent if action holonomy is discovered}\\
7 & \mathrm{NULL} & \hbox{fails by no-squeeze}
\end{array}
}
$$

This ranking is pragmatic, not ontological.  Ontologically, \(F2\) or \(F3\)
would be more satisfying than external \(F1\).  Practically, \(F1\) is the
shortest route to numbers.

## 12. Einstein/Feynman Reading Of The Grid

Einstein's lesson:

$$
\boxed{
\hbox{choose }L1\hbox{ or }L2\hbox{ as an admissibility law.}
}
$$

Feynman's lesson:

$$
\boxed{
\hbox{choose }F1,F2,\hbox{ or }F3\hbox{ to print actual numbers.}
}
$$

The combined law is therefore:

$$
\boxed{
\hbox{value completion}=(\hbox{form law})+(\hbox{number family}).
}
$$

## 13. Paper 22 Final Decision

Paper 22 audits all seven routes and finds:

$$
\boxed{
\begin{array}{ll}
\mathrm{D1}:&\hbox{no support-only route remains},\\
\mathrm{D2}:&\hbox{flat potential form }L1\hbox{ is the default admissibility law},\\
\mathrm{D3}:&\hbox{curved form }L2\hbox{ is reserved for stable licensed
cycle defects},\\
\mathrm{D4}:&\hbox{GR/SM calibration }F1\hbox{ is the fastest external number
source},\\
\mathrm{D5}:&\hbox{instrument/GCR }F2\hbox{ remains the intrinsic target},\\
\mathrm{D6}:&\hbox{boundary/action }F3\hbox{ remains a high-value future
route}.
\end{array}
}
$$

Thus the recommended next concrete route is:

$$
\boxed{
\mathrm{P22\text{-}L1F1}
\quad\hbox{for immediate calibrated numbers, while pursuing}\quad
\mathrm{P22\text{-}L1F2}
\quad\hbox{for intrinsic closure.}
}
$$

If \(L1F1\) prints a nonzero cycle defect:

$$
\boxed{
\Omega^{GRSM}_{012}\ne0,
}
$$

then immediately test:

$$
\boxed{
\mathrm{P22\text{-}L2F1}
}
$$

with a predeclared, not post-hoc, GR/SM holonomy source.

## 14. Export To The Next Work

The next work should not invent a new source primitive.  It should choose
one cell of the grid and print its missing object.

The recommended export is:

$$
\boxed{
\begin{array}{ll}
\hbox{primary}:&\mathrm{P22\text{-}L1F1}\hbox{ by printing a GR/SM edge table},\\
\hbox{parallel}:&\mathrm{P22\text{-}L1F2}\hbox{ by printing an instrument/GCR
bridge table},\\
\hbox{fallback}:&\mathrm{P22\text{-}L2F1}\hbox{ or }\mathrm{L2F2}\hbox{ if
stable curvature appears}.
\end{array}
}
$$

This is the complete source-completion grid.

## 15. Continuing The Chosen Pair: L1F1 And L1F2

Paper 22 now continues the two recommended cells:

$$
\boxed{
\mathrm{P22\text{-}L1F1}
\quad\hbox{and}\quad
\mathrm{P22\text{-}L1F2}.
}
$$

The strategy is deliberately two-track:

$$
\boxed{
\begin{array}{ll}
\mathrm{L1F1}:&\hbox{print calibrated numbers now if GR/SM data are
available},\\
\mathrm{L1F2}:&\hbox{pursue intrinsic closure by instrument/GCR records}.
\end{array}
}
$$

Both use the flat law:

$$
\boxed{
L1:\quad \ell=B\Phi.
}
$$

Thus both are falsified by the same cycle defect:

$$
\boxed{
\Omega_{012}=\ell_{01}+\ell_{12}-\ell_{02}.
}
$$

## 16. CAL-GRSM-001: Calibrated Number Protocol For L1F1

The first concrete calibrated-number object is:

$$
\boxed{
\mathrm{CAL\text{-}GRSM\text{-}001}.
}
$$

It prints the GR/SM edge table:

$$
\boxed{
\begin{array}{c|c|c|c|c|c}
\hbox{edge} & W_-^{GRSM} & W_+^{GRSM} &
\rho_-^{op} & \rho_+^{op} & \ell^{GRSM}\\
\hline
01 & W_0 & W_1 & r_0 & r_1 & \ell_{01}^{G}\\
12 & W_1' & W_2 & r_1' & r_2 & \ell_{12}^{G}\\
02 & W_0' & W_2' & r_0' & r_2' & \ell_{02}^{G}
\end{array}
}
$$

where:

$$
\boxed{
\ell_{ij}^{G}
=
\log\frac{W_+^{GRSM}}{W_-^{GRSM}}
-
\log\frac{\rho_+^{op}}{\rho_-^{op}}.
}
$$

The primes allow the three edges to be different fibers with the same
readout endpoints.  If the same microscopic rows are used, one may set:

$$
\boxed{
W_0=W_0',
\quad
W_1=W_1',
\quad
W_2=W_2',
\quad
r_0=r_0',
\quad
r_1=r_1',
\quad
r_2=r_2'.
}
$$

## 17. CAL-GRSM-001 Flatness Test

Compute:

$$
\boxed{
\Omega_G
=
\ell_{01}^{G}+\ell_{12}^{G}-\ell_{02}^{G}.
}
$$

The calibrated flat verdict is:

$$
\boxed{
\begin{array}{c|c}
|\Omega_G|\le\tau_G & \mathrm{P22\text{-}L1F1\ FLAT}\\
|\Omega_G|>\tau_G & \mathrm{P22\text{-}L1F1\ FAIL;\ test\ L2F1}
\end{array}
}
$$

If flat, print:

$$
\boxed{
\Phi_G(s_0)=0,
\qquad
\Phi_G(s_1)=\ell_{01}^{G},
\qquad
\Phi_G(s_2)=\ell_{02}^{G}.
}
$$

Then:

$$
\boxed{
\ell^G=B\Phi_G
\quad\hbox{up to }\tau_G.
}
$$

## 18. CAL-GRSM-001 Current-Corpus Fill

The current corpus has not printed:

$$
\boxed{
W_0,W_1,W_1',W_2,W_0',W_2',
\qquad
r_0,r_1,r_1',r_2,r_0',r_2'.
}
$$

Therefore:

$$
\boxed{
\mathrm{CAL\text{-}GRSM\text{-}001}^{cur}
=
\mathrm{OPEN}.
}
$$

But this is the fastest route to actual calibrated numbers, because once the
GR/SM table is supplied, \(\ell^G\), \(\Omega_G\), and \(\Phi_G\) are
immediately computable.

## 19. INT-GCR-001: Intrinsic Number Protocol For L1F2

The parallel intrinsic object is:

$$
\boxed{
\mathrm{INT\text{-}GCR\text{-}001}.
}
$$

Here \(Y\) is either:

$$
\boxed{
Y=O^{inst}
\quad\hbox{or}\quad
Y=\chi^{NN}(C^{GCR,sw}).
}
$$

The table is:

$$
\boxed{
\begin{array}{c|c|c|c|c|c|c}
\hbox{edge} & q^- & q^+ & y^- & y^+ & \ell^{I} & \zeta\\
\hline
01 & q_{01}^- & q_{01}^+ & s_0 & s_1 & \ell_{01}^{I} & \zeta_{01}\\
12 & q_{12}^- & q_{12}^+ & s_1 & s_2 & \ell_{12}^{I} & \zeta_{12}\\
02 & q_{02}^- & q_{02}^+ & s_0 & s_2 & \ell_{02}^{I} & \zeta_{02}
\end{array}
}
$$

The superscript \(I\) means the edge value is printed by the intrinsic
instrument/GCR source protocol, not imported from GR/SM.

## 20. INT-GCR-001 License Conditions

The intrinsic table is licensed only if:

$$
\boxed{
\begin{array}{ll}
\mathrm{I1}:&Y\hbox{ is actual finite record data, not a row label},\\
\mathrm{I2}:&Y\hbox{ is fixed before the value query},\\
\mathrm{I3}:&q_{01},q_{12},q_{02}\hbox{ are selected by protocol},\\
\mathrm{I4}:&\ell^I_{ij}\hbox{ is printed by the intrinsic source protocol},\\
\mathrm{I5}:&K^Y,\lambda^Y,\Delta^Y,B^Y\hbox{ are printed or bounded},\\
\mathrm{I6}:&\zeta_{ij}=C_\eta B^Y_{ij}\Delta^Y_{ij}/|s_j-s_i|\hbox{ is
finite},\\
\mathrm{I7}:&\hbox{repeated-edge defects vanish if repeated edges are
present}.
\end{array}
}
$$

The row-label exclusion is essential:

$$
\boxed{
Y(q)\ne\hbox{``the answer row of }q\hbox{''}.
}
$$

## 21. INT-GCR-001 Flatness And Control Test

Compute:

$$
\boxed{
\Omega_I
=
\ell_{01}^{I}+\ell_{12}^{I}-\ell_{02}^{I}.
}
$$

and:

$$
\boxed{
\zeta^{max}
=
\max\{\zeta_{01},\zeta_{12},\zeta_{02}\}.
}
$$

The intrinsic flat verdict is:

$$
\boxed{
\begin{array}{c|c}
|\Omega_I|\le\tau_I\hbox{ and }\zeta^{max}\le\tau_S &
\mathrm{P22\text{-}L1F2\ INTRINSIC\ FLAT}\\
|\Omega_I|>\tau_I &
\mathrm{P22\text{-}L1F2\ FAIL;\ test\ L2F2}\\
\zeta^{max}>\tau_S &
\mathrm{P22\text{-}L1F2\ WEAK\ CONTROL}
\end{array}
}
$$

If intrinsic flatness passes, print:

$$
\boxed{
\Phi_I(s_0)=0,
\qquad
\Phi_I(s_1)=\ell_{01}^{I},
\qquad
\Phi_I(s_2)=\ell_{02}^{I}.
}
$$

Then:

$$
\boxed{
\ell^I=B\Phi_I
\quad\hbox{up to }\tau_I.
}
$$

## 22. INT-GCR-001 Current-Corpus Fill

The current corpus has not printed a licensed completed table for:

$$
\boxed{
Y,\quad
\ell^I_{01},\ell^I_{12},\ell^I_{02},
\quad
\zeta_{01},\zeta_{12},\zeta_{02}.
}
$$

Therefore:

$$
\boxed{
\mathrm{INT\text{-}GCR\text{-}001}^{cur}
=
\mathrm{OPEN}.
}
$$

This is the intrinsic closure target, but not yet a completed route.

## 23. Agreement Test Between Calibrated And Intrinsic Routes

If both \(CAL\text{-}GRSM\text{-}001\) and \(INT\text{-}GCR\text{-}001\)
print, compare:

$$
\boxed{
\Delta_{ij}^{GI}
:=
\ell_{ij}^{G}-\ell_{ij}^{I}.
}
$$

Let:

$$
\boxed{
\Delta_{GI}^{max}
=
\max_{ij\in\{01,12,02\}}
|\Delta_{ij}^{GI}|.
}
$$

The agreement verdict is:

$$
\boxed{
\begin{array}{c|c}
\Delta_{GI}^{max}\le\tau_{GI} &
\hbox{GR/SM calibration and intrinsic source agree}\\
\Delta_{GI}^{max}>\tau_{GI} &
\hbox{calibrated and intrinsic source split}
\end{array}
}
$$

This is the actual A/B bridge comparison in the new language.

## 24. Four Possible Outcomes Of The Chosen Pair

The paired program has four possible outcomes:

$$
\boxed{
\begin{array}{c|c|c|c}
\hbox{case} & CAL\text{-}GRSM & INT\text{-}GCR & \hbox{meaning}\\
\hline
1 & \mathrm{FLAT} & \mathrm{FLAT,\ agrees} &
\hbox{calibrated and intrinsic closure coincide}\\
2 & \mathrm{FLAT} & \mathrm{OPEN} &
\hbox{usable calibrated numbers; intrinsic still pending}\\
3 & \mathrm{FLAT} & \mathrm{FLAT,\ disagrees} &
\hbox{calibration/intrinsic split}\\
4 & \mathrm{FAIL} & \mathrm{any} &
\hbox{test }L2F1\hbox{ for calibrated curvature}
\end{array}
}
$$

If \(INT\text{-}GCR\) fails flatness with stable nonzero cycle defect, test:

$$
\boxed{
\mathrm{P22\text{-}L2F2}.
}
$$

## 25. Continuation Verdict

Continuing the two chosen routes gives:

$$
\boxed{
\begin{array}{c|c|c}
\hbox{object} & \hbox{current status} & \hbox{next missing print}\\
\hline
CAL\text{-}GRSM\text{-}001 & \mathrm{OPEN} &
W^{GRSM},\rho^{op}\hbox{ on three edges}\\
INT\text{-}GCR\text{-}001 & \mathrm{OPEN} &
Y,\ell^I,\zeta\hbox{ on three edges}\\
\hbox{agreement test} & \mathrm{OPEN} &
\ell^G\hbox{ and }\ell^I\hbox{ both printed}
\end{array}
}
$$

Thus the recommended concrete next action remains:

$$
\boxed{
\hbox{print }CAL\text{-}GRSM\text{-}001\hbox{ first for calibrated numbers,
and print }INT\text{-}GCR\text{-}001\hbox{ in parallel for intrinsic closure.}
}
$$

## 26. Final Reflection: Seven Routes Are Three Generators With Two Geometries

The grid is correct, but it is not the deepest ontology.  Paper 22 has seven
routes because it separated two different questions:

$$
\boxed{
\begin{array}{ll}
\hbox{geometry question}:&\hbox{is the value one-form flat or curved?}\\
\hbox{source question}:&\hbox{what finite mechanism produces the value?}
\end{array}
}
$$

The geometry question has two answers:

$$
\boxed{
\begin{array}{ll}
L1:&\ell=B\Phi,\\
L2:&\ell=B\Phi+{\mathcal A}^{hol}.
\end{array}
}
$$

The source question has three live generator families:

$$
\boxed{
\begin{array}{ll}
G1:&\hbox{GR/SM calibrated finite generator},\\
G2:&\hbox{instrument/GCR finite record generator},\\
G3:&\hbox{boundary/action finite generator}.
\end{array}
}
$$

Therefore:

$$
\boxed{
\hbox{six non-null routes}
=
\hbox{three value generators}\times\hbox{two output geometries}.
}
$$

The null route is not a generator.  It is the control case:

$$
\boxed{
P22\text{-}NULL
=
\hbox{support and admissibility without a value-generating law}.
}
$$

Thus the next paper should not add an eighth route.  It should replace the
source table itself by a finite generating law:

$$
\boxed{
Z_{ij}
=
\sum_{\gamma:i\to j}
{\mathfrak m}(\gamma)\exp A(\gamma),
\qquad
\ell_{ij}
=
\log Z_{ij}-\log \rho^{op}_{ij}.
}
$$

Then:

$$
\boxed{
\hbox{the source table is no longer input; it is output.}
}
$$

This is the handoff to Paper 23.  The Paper-22 grid remains the audit
surface, but Paper 23 must build the finite value-generating machines behind
the three source families:

$$
\boxed{
\mathrm{P23}
=
\hbox{finite generating functional for source values}.
}
$$
