# Quantum World-Selection Bridge

**Status:** Provisional Bridge — Interpretively Strong, Dynamically Incomplete  
**Source:** QT1 Thread (April 2026)  
**Hard-kernel conflicts:** None  
**Prior theorem count:** 583 unchanged  
**Depends on:** Retained Existence Engine (UD-RetainedExistence.md)  

---

## QX.1 Orientation

This bridge does not yet replace the dynamical quantum formalism; rather, it specifies how UD interprets the passage from candidate quantum branch structure to retained worlded outcome. Its purpose is narrower and cleaner than full quantum closure: it supplies the selector grammar for measurement, collapse, and decoherence.

## QX.2 Core Bridge Claim

Quantum possibility is wider than world. Measurement is the selector process by which a narrower subset becomes retained as world at the relevant descriptive level.

---

## QX.3 Formal Bridge Objects

### QO1 — Candidate Branch Field
$$\mathcal{B} = \{B_\alpha\}$$
Each $B_\alpha$ is a candidate retained branch, not yet a fully worlded outcome.

### QO2 — Worlded Branch Subset
$$\mathcal{B}_W \subseteq \mathcal{B}$$
The subset retained as world at the relevant descriptive level.

### QO3 — Branch Compatibility Function
$$\Gamma(B_\alpha, B_\beta) \in [0,1]$$
Joint retained-world compatibility between candidate branches.

### QO4 — Measurement Map
$$M_{\text{meas}}: \mathcal{B} \to \mathcal{B}_W$$
The selector map from candidate branch field to retained world subset.

---

## QX.4 Worlded Branch Condition

$$B_\alpha \in \mathcal{B}_W \;\Longleftrightarrow\; \Omega(B_\alpha)=1 \;\wedge\; \mathrm{Adm}(B_\alpha)=1 \;\wedge\; \mathrm{Supp}(B_\alpha)=1 \;\wedge\; \mathrm{Clos}(B_\alpha)=1 \;\wedge\; \mathrm{Ret}_t(B_\alpha)=1$$

A branch becomes worlded only if it clears retained-existence selection.

---

## QX.5 Decoherence as Compatibility Loss

Decoherence corresponds to the progressive loss of joint retained-world compatibility among competing candidate branches:

$$\Gamma(B_\alpha, B_\beta) \downarrow 0$$

for relevant incompatible pairs. Decoherence prepares selector narrowing but is not the final verdict.

---

## QX.6 Collapse as Retained-World Narrowing

$$\mathcal{B} \to \mathcal{B}_W, \quad \mathcal{B}_W \subsetneq \mathcal{B}$$

Collapse is not arbitrary erasure of possibility; it is selector-driven narrowing from candidate branch structure to retained world structure.

---

## QX.7 Apparatus / Observer Placement

$$\mathrm{Supp}(B_\alpha \mid E_{\text{obs}})$$

The observer-apparatus complex enters as a support-context modifier, changing coupling, burden routing, closure conditions, and persistence criteria. It is not an extra-theoretic magic source.

---

## QX.8 Branch Weight Architecture

### Hard Exclusion
$$\chi_{\text{hard}}(B_\alpha) \in \{0,1\}$$

Branches failing formation floor, foundational floor, support, closure, or temporal retention are excluded:
$$\chi_{\text{hard}}(B_\alpha) = 0 \;\Rightarrow\; \mu(B_\alpha) = 0$$

### Soft Viability (Canonical First Form — Equal-Exponent Multiplicative)
$$\mu_{\text{soft}}(B_\alpha) = M(B_\alpha) \cdot \hat{A}(B_\alpha) \cdot \hat{S}(B_\alpha) \cdot \hat{C}(B_\alpha) \cdot \hat{R}(B_\alpha)$$

### Compatibility Survival (Exponential)
$$\hat{\Gamma}(B_\alpha \mid \mathcal{B}, t) = \hat{\Gamma}_\alpha(0) \exp\!\left(-\int_0^t D_\alpha(\tau)\,d\tau\right)$$

### Effective Branch Favoring
$$\mu_{\text{eff}}(B_\alpha, t) = \mu_{\text{soft}}(B_\alpha, t) \cdot \hat{\Gamma}(B_\alpha \mid \mathcal{B}, t)$$

### Full Branch Weight
$$\mu(B_\alpha \mid \mathcal{B}, t) = \chi_{\text{hard}}(B_\alpha, t) \cdot \mu_{\text{eff}}(B_\alpha, t)$$

### Normalized World-Favoring (Pre-Born)
$$\tilde{\mu}(B_\alpha \mid \mathcal{B}, t) = \frac{\mu_{\text{eff}}(B_\alpha, t)}{\sum_{\beta \in \mathcal{B}_+} \mu_{\text{eff}}(B_\beta, t)}$$

This is a pre-probabilistic comparative measure, not yet a final Born rule.

---

## QX.9 Unified Branch Favoring Equation (Canonical First Form)

$$\frac{d}{dt}\ln\mu_{\text{eff},\alpha} = \sum_{X \in \{M,A,S,C,R\}} (\Phi_X - \Psi_X)_\alpha - D_\alpha$$

Where each $\Phi_X$ is a repair/strengthening term and $\Psi_X$ is an erosion/weakening term across:

| Channel | Repair ($\Phi$) | Erosion ($\Psi$) |
|---------|----------------|-----------------|
| Mechanical | burden relaxation, transport integrity | overstrain, defect leakage |
| Admissibility | constraint satisfaction, gate reinforcement | contradiction load, gate-fragility drift |
| Support | path density, context compatibility | isolation, bottleneck strain |
| Closure | loop completion, closure redundancy | seam mismatch, closure burden |
| Retention | return stability, memory reinforcement | fluctuation washout, horizon fragility |

---

## QX.10 Branch Life-Cycle Phase Grammar

Define the net favoring balance:
$$\Delta_\alpha = \sum_{X \in \{M,A,S,C,R\}} (\Phi_X - \Psi_X)_\alpha - D_\alpha = \frac{d}{dt}\ln\mu_{\text{eff},\alpha}$$

**Phase regions:**
- **Rising:** $\Delta_\alpha > 0$
- **Stable:** $\Delta_\alpha = 0$
- **Falling:** $\Delta_\alpha < 0$
- **Near-excluded:** $0 < \mu_{\text{eff},\alpha} \ll 1$, $\chi_{\text{hard}} = 1$
- **Terminal:** $\chi_{\text{hard}} = 0$

**Recovery:** possible while $\chi_{\text{hard}}(B_\alpha) = 1 \;\wedge\; \Delta_\alpha \geq 0$.

**Terminality:** begins when $\chi_{\text{hard}}: 1 \to 0$.

---

## QX.11 Residue and Re-Entry

After terminality, a branch may leave structured residue:
$$R_{\text{res}}(B_\alpha) = (r_M,\; r_A,\; r_S,\; r_C,\; r_R,\; r_\Gamma)_\alpha$$

A successor branch may later form through residue-driven re-formation:
$$F_{\text{new}}(R_{\text{res}}(B_\alpha), E) \to B_{\alpha'}^{\text{new}}, \quad \chi_{\text{hard}}(B_{\alpha'}^{\text{new}}) = 1$$

---

## QX.12 Microscopic Selector — Seed Transport Laws

### Packet Update Law
$$X_i(t+1) = U_{\text{pkt}}(X_i(t),\; N(i,t),\; E(t))$$

With minimal packet state $X_i = (\rho_i, \theta_i, \chi_i, \sigma_i, b_i)$.

### Burden Update Seed
$$\Delta\rho_i = J_i^{\text{in}} - J_i^{\text{out}} + R_i^{\text{redist}} - D_i^{\text{diss}} + E_i^{\text{env}}$$

### Transport Phase Update Seed
$$\Delta\theta_i = A_i^{\text{align}} + L_i^{\text{loop}} + F_i^{\text{frame}} + E_i^{\theta,\text{env}}$$

---

## QX.13 Bridge Labels

| Label | Name | Type | Status |
|-------|------|------|--------|
| QP1 | Quantum World-Selection Principle | Principle | Canonical bridge |
| QC1 | Decoherence Compatibility Corollary | Corollary | Strong bridge |
| QT1-seed | Quantum Measurement Narrowing Theorem | Theorem seed | Active |
| QS1 | Collapse as Retained-World Narrowing | Statement | Canonical bridge |
| QS2 | Support-Context Measurement Statement | Statement | Canonical placement |

---

## QX.14 Anchor Equations

| Label | Equation |
|-------|----------|
| (QX.1) | $\mathcal{B} = \{B_\alpha\}$ — candidate branch field |
| (QX.2) | $\mathcal{B}_W \subseteq \mathcal{B}$ — worlded branch subset |
| (QX.3) | $M_{\text{meas}}: \mathcal{B} \to \mathcal{B}_W$ — measurement map |
| (QX.4) | Worlded branch condition (see §QX.4) |
| (QX.5) | $\Gamma(B_\alpha, B_\beta) \in [0,1]$ — branch compatibility |
| (QX.6) | $\Gamma(B_\alpha, B_\beta) \downarrow 0$ — decoherence condition |
| (QX.7) | $\mathcal{B} \to \mathcal{B}_W$, $\mathcal{B}_W \subsetneq \mathcal{B}$ — collapse map |
| (QX.8) | $\mathrm{Supp}(B_\alpha \mid E_{\text{obs}})$ — support-context |

---

## QX.15 Explicitly Unresolved Remainder

| ID | Frontier |
|----|----------|
| QR1 | Amplitude dynamics — not yet derived |
| QR2 | Born weighting — not yet derived |
| QR3 | Full branching Hamiltonian — not yet closed |
| QR4 | Quantitative apparatus coupling — not yet specified |
| QR5 | Descriptive-level criterion — not yet formalized |
| QR6 | Empirical frequency bridge — not yet tested |

---

## Scope Boundary

The selector side is now architecturally closed. The remaining quantum burden is the quantitative dynamical law that generates branches, transports their weights, and connects normalized retained-world favoring to empirical outcome statistics.

---

## Closing

A branch lives by world-strength, declines by incompatibility, dies by worldhood failure, and returns only through residue-driven re-formation.

---

*© 2026 Benjamin Walker Mayes*
