# Master Action

## Purpose
This file replaces the placeholder with the current unified effective action bridge for Distinction Dynamics.

## 1. Effective field content
The present low-energy effective field content is:

- metric/depth sector: \(g_{\mu\nu},\mathcal{D}\),
- matter spinor defect fields: \(\psi_i\),
- gauge transport fields: \(A_\mu, W_\mu^a, G_\mu^a\),
- closure-background order parameter: \(\Sigma\),
- scalar burden-amplitude sector: \(\phi\) when needed.

## 2. Unified action density
The effective Lagrangian density is

\[
\mathcal{L}_{\text{DT,eff}}=
\mathcal{L}_{\text{grav}}
+
\mathcal{L}_{\text{gauge}}
+
\mathcal{L}_{\text{matter}}
+
\mathcal{L}_{\Sigma}
+
\mathcal{L}_{\text{Yukawa}}
+
\mathcal{L}_{\phi}.
\]

with the sectors defined below.

### Gravitational / depth sector
\[
\mathcal{L}_{\text{grav}}=
\sqrt{-g}\left[
A R
-
\frac{B}{2}(\nabla\mathcal{D})^2
-
V(\mathcal{D})
+
C\,\mathcal{D}\,\mathcal{B}
\right].
\]

### Gauge sector
\[
\mathcal{L}_{\text{gauge}}=-\frac14\left(
F_{\mu\nu}F^{\mu\nu}
+
W_{\mu\nu}^aW^{a\mu\nu}
+
G_{\mu\nu}^aG^{a\mu\nu}
\right).
\]

### Matter sector
\[
\mathcal{L}_{\text{matter}}=
\sum_i \bar\psi_i(i\gamma^\mu D_\mu-m_i)\psi_i,
\]

with

\[
D_\mu = \partial_\mu + iqA_\mu + ig_2\tau_a W_\mu^a + ig_3\lambda_a G_\mu^a.
\]

### Symmetry-breaking / closure-background sector
\[
\mathcal{L}_{\Sigma}=|D_\mu\Sigma|^2 - V(\Sigma).
\]

### Yukawa-like coupling
\[
\mathcal{L}_{\text{Yukawa}}=-y_\psi\Sigma\bar\psi\psi.
\]

After \(\langle\Sigma\rangle=v\), this yields

\[
m_\psi = y_\psi v.
\]

### Scalar burden-amplitude sector
\[
\mathcal{L}_{\phi}=\frac12(\partial\phi)^2-U(\phi).
\]

## 3. Action functional
The total effective action is

\[
S_{\text{DT,eff}} = \int d^4x\;\mathcal{L}_{\text{DT,eff}}.
\]

## 4. Interpretation
This action is not claimed to be the microscopic substrate law. It is the current coarse-grained bridge showing how curvature, transport, matter-like defects, symmetry breaking, and scalar burden sectors may appear as effective low-energy descriptions of packet transport, closure stress, and burden dynamics.
