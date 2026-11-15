# Seam Phase Transport

## Purpose
This file replaces the placeholder with the current seam-phase transport formalism summary.

## 1. Seam links as transport primitives
Packet-to-packet transport occurs across shared seam interfaces. Each oriented seam link \((ij)\) carries a transport operator \(U_{ij}\) acting on the local seam-framing state space.

The current local transport law is

\[
U_{ij}=\exp\!\left[
\frac{i}{2}\left(A_{ij}^1\sigma_1+A_{ij}^2\sigma_2+A_{ij}^3\sigma_3\right)
\right].
\]

## 2. Generator decomposition
The three local generator channels are interpreted as

\[
A_{ij}^3 \sim a\,\Delta\chi_{ij},
\]

\[
A_{ij}^1 \sim b\,\Delta\sigma_{ij},
\]

\[
A_{ij}^2 \sim c\,\Delta\theta_{ij}.
\]

So:

- \(\Delta\chi_{ij}\): closure-orientation bias,
- \(\Delta\sigma_{ij}\): framing-flip transport,
- \(\Delta\theta_{ij}\): phase-twisted framing transport.

## 3. Holonomy around loops
For any closed seam loop \(C\), the accumulated transport is

\[
\mathcal{U}(C)=\prod_{(ij)\in C}U_{ij}.
\]

If \(\mathcal{U}(C)\neq I\), the loop encloses nontrivial transport curvature. This provides the discrete bridge to gauge flux and coarse-grained curvature observables.

## 4. Abelian reduction
In the abelian limit where only the diagonal channel survives,

\[
U_{ij}=e^{iq\phi_{ij}},
\]

and the loop phase is simply

\[
\Phi_C = \sum_{(ij)\in C}\phi_{ij}.
\]

This is the present \(U(1)\)-like seam-phase transport limit.

## 5. Non-Abelian transport meaning
The full transport is non-Abelian because the three seam processes act non-commutatively on the same local two-state lifted seam-framing basis. In the current interpretation, this is the microscopic source of the provisional local \(SU(2)\)-like transport sector.
