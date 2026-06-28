Mathematically, a dressed $\mathbb Z_2$ exit basin is an explicit open set of
effective $\mathbb Z_2$ gauge actions for which a strong-coupling/cluster-expansion
theorem applies.

A clean formulation is:

Let $\Lambda \subset \mathbb Z^4$ be a finite lattice. Put $\mathbb Z_2$
variables $u_e \in \{\pm 1\}$ on edges, and define the plaquette flux

$$
F_p(u)=\prod_{e\in\partial p}u_e.
$$

A dressed $\mathbb Z_2$ gauge action is not just

$$
S(u)=-\beta\sum_p F_p(u),
$$

but a general gauge-invariant effective action

$$
S_J(u)=-\sum_X J_X \prod_{p\in X}F_p(u),
$$

where $X$ ranges over finite connected sets of plaquettes. The coefficients
$J_X$ are the dressing: multi-plaquette interactions left behind after
integrating out other degrees of freedom.

Now define a weighted polymer norm, for some fixed $\kappa>0$,

$$
\|J\|_\kappa
=
\sup_p
\sum_{X\ni p}
e^{\kappa(|X|+\operatorname{diam}X)}
|\tanh J_X|.
$$

Then an exit basin is a set of the form

$$
\mathcal X_{\kappa,\epsilon}
=
\{J:\|J\|_\kappa<\epsilon\},
$$

with $\epsilon$ chosen small enough that the polymer/cluster expansion converges
absolutely and uniformly.

The theorem one wants is:

$$
J\in\mathcal X_{\kappa,\epsilon}
\quad\Longrightarrow\quad
|\langle W(C)\rangle_J|
\le
A_0 e^{-\tau\,\operatorname{Area}(C)}
$$

for every Wilson loop $C$, with constants $A_0<\infty$ and $\tau>0$
independent of the volume and stable under boundary/collar conditionings.

Equivalently: inside this basin, the dressed $\mathbb Z_2$ theory is provably
in its disordered/strong-coupling phase. The word exit means that once an RG
flow enters $\mathcal X_{\kappa,\epsilon}$, the hard part is over: standard
convergent expansion gives the required area-law or nonconcentration estimate.
