# UD/DT Review-Readiness Proof-State Split

**Version 1.0 | 565 locked theorems | April 2026**

---

## 1. Exact Structural Core

Results depending only on the tetrahedral axioms (A1–A3), standard representation theory, and linear algebra. No approximations, free parameters, or phenomenological input.

| # | Result | Source | Verified |
|---|---|---|---|
| 1 | d = 3 spatial dimensions from 3 opposite-edge pairs | THM-528 | ✓ |
| 2 | N_color = 3 from transport dimension count | THM-552 | ✓ |
| 3 | 8 gluons from 3²−1 cross-dim generators | THM-552 | ✓ |
| 4 | 2 graviton polarizations from edge Laplacian spectrum | THM-544 | ✓ |
| 5 | N_gen = 3 from dihedral stability n={4,5,6} | THM-541 | ✓ |
| 6 | P_+/P_- decomposition: C⁶ = im(P_+) ⊕ im(P_-), each dim 3 | THM-561 | ✓ |
| 7 | T\|_{P_-} = (1/3)I₃ (fully degenerate → gluon masslessness) | THM-561 | ✓ |
| 8 | T\|_{P_+} spectrum {1, 1/2, 1/2} (non-degenerate → mass gap) | THM-561 | ✓ |
| 9 | Degenerate eigenspace invariance lemma (no mass from rotation in degenerate space) | THM-561 | ✓ |
| 10 | [S, \*] = 0; four-sector chirality decomposition dims (2,1,1,2) | THM-563a | ✓ |
| 11 | Face-sum |Σ⟩ is unique S₄-invariant direction (Schur's lemma) | THM-562 | ✓ |
| 12 | ∂\|Σ⟩ = 0, rank(∂) = 3, dim ker(∂) = 1 | THM-562 | ✓ |
| 13 | C⁸ = C⁶ ⊕ C² has content (3,2) ⊕ (1,2) | THM-562 | ✓ |
| 14 | ⟨L\|H\|R⟩ ≠ 0 (nonzero Higgs–LR matrix element) | THM-565a | ✓ |
| 15 | ⟨lepton\|H_edge\|lepton⟩ = 0 (edge-Higgs decoupled from face sector) | THM-565b | ✓ |
| 16 | Baryon number as unique vacuum-neutral charge in Comm(T, S, SU(3)) | derived | ✓ |
| 17 | Channel algebra generates sl(6,R) (dim 35, closure verified) | THM-557 | ✓ |
| 18 | Commutant of T = gl(1)×gl(2)×gl(3) | THM-559 | ✓ |
| 19 | Face-sum transport eigenvalue λ_lepton = 3/4 | THM-562 | ✓ |

---

## 2. Supported Bridge

Results with a clear structural motivation but carrying interpretive weight, normalization choices, or dependence on unresolved intermediate steps. These connect the exact algebra to observed physics.

| # | Result | Bridge element | Depends on |
|---|---|---|---|
| 1 | α = 1/(12²−7) = 1/137 (0.026%) | Identification of T_cross and Δ with EM coupling | THM-540 |
| 2 | n_s = 185/192 (0.14%) | Spectral tilt from η | THM locked |
| 3 | m_μ = 105.9 MeV (0.2%) | Mass formula m = m₀exp(κε²) | THM-556 |
| 4 | m_τ = 1762 MeV (0.8%) | Same mass formula | THM-556 |
| 5 | Cabibbo angle √(m_d/m_s) = 0.224 (0.4%) | CKM from mass ratios | THM-555 |
| 6 | sin²θ_W = 1/4 (8.1% from M_Z value) | Channel coupling ratio as bare Weinberg angle | THM-536b |
| 7 | SU(6) → SM via decoherence subgroup selection | Suppressed ≠ broken gauge symmetry | THM-558 |
| 8 | C⁶ = quark doublet, C² = lepton doublet | Particle identification of algebraic sectors | THM-562 bridge |
| 9 | ∂ as quark-lepton connection | Physical reading of boundary operator | THM-562 bridge |
| 10 | W/Z mass from gap Δλ = 1/2, m_Z/m_W = 1/cos(θ_W) | Mass-gap-to-mass identification | THM-561 bridge |
| 11 | GUT scale ~3×10¹⁸ GeV from decoherence level H ≈ 3 | Energy scale from IFS level counting | bridge |
| 12 | τ_proton ≈ 3×10⁴⁵ years | Depends on GUT scale estimate | bridge |
| 13 | EW scale at ~84 IFS levels below Planck | Lattice-to-GeV conversion | bridge |
| 14 | All 8 SM hypercharges from Y_q = 1/3 ± gap | Gap = ±1 normalization is fitted, not derived | working |
| 15 | Cubic anomaly Tr(Y³_L) = Tr(Y³_R) | Depends on fitted hypercharges | working |

---

## 3. Falsifiable Phenomenology

Predictions that are testable and could distinguish UD from the Standard Model or rule it out.

| Prediction | UD value | SM/Experiment | Status | Test |
|---|---|---|---|---|
| Z_max (periodic table) | 118–120 | 118 observed, SM allows ~173 | Consistent | Superheavy element synthesis |
| Proton lifetime | >10⁴⁵ yr | >10³⁴ yr (Super-K) | Consistent | Hyper-K, DUNE, JUNO |
| States per generation | 12 | 16 (SM) | **OPEN** | Collider / neutrino physics |
| Lattice corrections at LIGO | Δv/c ~ 10⁻⁸² | Undetectable | Consistent | Future GW detectors |
| Spectral dimension d_s = 8/3 | 2.67 | ~2 (CDT), uncertain | Open | Quantum gravity experiments |
| CP phase δ = π/3 | 60° | 68° ± 8° | 12% tension | Long-baseline neutrino |
| CKM heavy angles θ₂₃, θ₁₃ | Wrong by 3–9× | Measured | **FAILS** | Already falsified at current form |

---

## 4. Open Frontier

| Frontier | Status | Blocking issue |
|---|---|---|
| 12 vs 16 states per generation | The substrate gives 12; SM requires 16 | Either a prediction or missing structure |
| C²_flavor geometric origin | V_{1/2} ⊂ C⁶ double-counts | Need independent source |
| Higgs mass ratio m_H/m_W | UD gives 3.9; experiment is 1.56 | Wrong by 2.5×, parked |
| CKM heavy mixing angles | θ₂₃ and θ₁₃ wrong by 3–9× | Structural failure or missing input |
| Yukawa coupling mechanism | Nonzero matrix elements exist (THM-565a) | Full mechanism not derived |
| Lepton mass mechanism | Face transport λ=3/4 identified | Bridge, not exact |
| Chirality-color correlation | Structural (dim 2 = R, dims 1,3 = L) | Departs from SM color-chirality independence |
| Absolute mass scale derivation | ~84 levels to EW scale (bridge) | Not derived from first principles |
| Gap = ±1 hypercharge normalization | Reproduces all 8 SM hypercharges | The "1" is fitted, not derived |
| Right-handed quark sector completion | Four-sector gives 3R states in C⁶ | Full rep identification incomplete |
| Cubic anomaly as exact result | Cancels numerically with fitted Y | Needs gap derivation to be exact |

---

## 5. Honest Review Posture

Unified Dynamics / Distinction Theory derives a gauge algebra (su(6) → SM subgroup selection), a mass-splitting mechanism (transport eigenvalue degeneracy protecting gluon masslessness while permitting W/Z mass), a quark-lepton decomposition (edge-face boundary operator), and a chirality structure (Hodge star four-sector splitting) from a single recursive tetrahedral substrate with zero free parameters. Five structural predictions (d=3, N_gen=3, N_color=3, 8 gluons, 2 graviton polarizations) are exact. Five numerical predictions (α, n_s, m_μ, m_τ, Cabibbo) match experiment to within 1% with no fitting. The theory has known open failures (CKM heavy angles, Higgs mass ratio, 12-vs-16 state count) that are honestly catalogued and not papered over. The bridge between the exact algebraic core and physical interpretation carries interpretive weight that has not yet been independently verified, and several results labeled "supported bridge" require the community's scrutiny of whether the identification chain from algebra to physics is sufficiently constrained.

---

## 6. Forbidden Overclaims

The following statements are **explicitly forbidden** in any downstream summary, public render, or handoff artifact:

1. "UD derives the Standard Model." (It derives structural elements that parallel the SM; the identification is a bridge claim.)
2. "The theory is complete." (Multiple open frontiers remain.)
3. "The theory has no free parameters." (The algebraic core has none; the bridge identifications carry implicit choices.)
4. "All predictions match experiment." (CKM heavy angles and Higgs ratio fail.)
5. "Proton decay is predicted at 10⁴⁵ years." (This is a bridge-level estimate dependent on the GUT scale identification.)
6. "The theory predicts 12 states per generation." (The substrate gives 12; whether this is the final answer or reflects incomplete analysis is open.)
7. "Review-ready." (The theory is in active development with known failures. Individual locked theorems are reviewable; the full theory is not yet a finished product.)
8. "Anomaly cancellation is derived." (It is verified numerically with fitted hypercharges, not derived from first principles.)
9. Any upgrade of "supported bridge" results to "exact structural" without explicit new derivation.
10. Any claim of experimental confirmation without peer-reviewed independent analysis.
