# Retained information per boundary area and resource cost

2026-10-13. Benjamin Walker Mayes, AI-assisted development. Development — no registry entry. Physical promotion 0; independent review OPEN.

## Result and fair comparison

Compare the one-hot and complementary-ground encodings on the same twelve-face memory, at the same temperature beta J=(ln3)/2 and after the same number r of uniform-site thermal updates. Both begin with the same oriented pure blank and encode the same fair binary carrier label. Both reserve the full coupled boundary area A=12a0. A one-face area denominator for one-hot would require a different isolated apparatus and thermal kernel; it cannot be substituted into this comparison.

Exact conditional distributions and energy means determine retained information, readout error and a memory-cycle work bound. Complete apparatus cost remains OPEN because the drive, clock, bath renewal, readout, and controller reset have not been physically specified. This report provides a complete list of those resource categories, not a falsely complete numerical total.

## 1. Information density and retention target

Let R be the carrier label at write time and M_r the memory after storage. Define

\[
\mathcal I_r=I(R:M_r),\qquad
\rho_{\rm info}(r)=\frac{\mathcal I_r}{12a_0}.
\]

This is retained source information in nats per spatial area, not thermodynamic horizon entropy density. Multiplication by k_B gives entropy units without establishing a horizon identification.

| Quantity at r=32 | One-hot | Complementary ground |
|---|---:|---:|
| Retained information, nats | 0.02879899 | 0.66761023 |
| Information density | 0.00239992/a0 | 0.05563419/a0 |
| Optimal equal-prior error | 0.41114666 | 0.00923883 |
| Retained fraction of initial ln2 | 0.04155 | 0.96316 |

The density ratio is approximately 23.18173. Exact rational error probabilities and the underlying rational distributions certify the state evolution; logarithmic displays are ordinary floating evaluations, not rigorous numeric intervals.

For a candidate retention criterion of optimal error at most 1/100 after 32 updates, the ground encoding passes and the one-hot encoding fails. This threshold is an explicitly chosen comparison criterion, not a native UD constant. The optimal-error measurement may require full-word processing. The feasible majority decoder also passes for the ground encoding, with error approximately 0.00934834.

The two encodings each store one source bit, so this comparison measures retention density at finite time, not asymptotic code capacity or an extensive area law.

## 2. Typed energy ledger

Let E_r be the mean memory energy, H_r=H(M_r) its dimensionless marginal entropy, and E_w its energy immediately after the write. For these real carrier test inputs, the pulse work is W_w=E_w: 3J for one-hot and zero for ground. Subsequent memory collisions conserve energy with their baths, so cumulative bath heat is

\[
Q_B(r)=E_w-E_r.
\]

These are different quantities. Negative bath heat means the memory absorbs energy.

The storage entropy balance, with the outgoing baths and degenerate random-site controls included in the environment accounting, gives

\[
\sigma_r=H_r-\ln2+\beta Q_B(r)\ge0.
\]

It is the marginal memory entropy-production expression for the declared thermal process, not a count of lost carrier information. Conditional reference information requires a separate accounting.

Blind reset returns the full memory to the same pure zero-energy blank without using R. Under isothermal reset with a thermal reservoir and a work source,

\[
W_{\rm reset}\ge k_BT H_r-E_r.
\]

Proof: W=Delta E+Q_B, and the thermal entropy inequality gives Q_B>=−T Delta S. Combining gives W>=Delta E−T Delta S, the free-energy change. A pure blank has E=S=0, yielding the expression above.

Therefore the write–store–reset memory-cycle work obeys

\[
\boxed{W_{\rm mem,cycle}\ge
k_BT H_r+Q_B(r)
=k_BT[\ln2+\sigma_r].}
\]

This is a lower bound for a reusable memory with outgoing baths exported and source-label side information unavailable. It is not an attainable finite exact reset recipe. Exact pure reset is blocked with a finite full-rank thermal bath; bounds describe permitted approximations or limiting processes. It also is not a scalar total for returning every control and finite bath to its original state.

An independent relative-entropy evaluation verifies the same reset expression. For Gibbs memory tau_M with partition P,

\[
D(\rho_{M_r}\Vert\tau_M)=-H_r+\beta E_r+\ln P,
\quad W_{\rm reset}^{\rm bound}/(k_BT)=\ln P-D.
\]

The checker evaluates both expressions on the exact propagated states.

## 3. Comparison including reset

At r=32, the modeled ledger is:

| Quantity | One-hot | Complementary ground |
|---|---:|---:|
| Pulse work / J | 3 | 0 |
| Mean memory energy / J | 3.92355 | 3.24654 |
| Cumulative bath heat / J | −0.92355 | −3.24654 |
| Marginal memory entropy, nats | 3.07462 | 3.28057 |
| Storage sigma | 1.87416 | 0.80404 |
| Reset work bound / kBT | 0.91939 | 1.49719 |
| Memory-cycle work bound / kBT | 2.56731 | 1.49719 |

The ground memory has higher reset work at this time, but lower combined write–store–reset work bound. Net endpoint write work alone would hide this distinction.

At r=0, both memory-cycle bounds are exactly k_BT ln2. The one-hot write deposits 3J which can offset reset work; the ground encoding deposits no energy. Thus zero ground write work does not imply zero blind-reset cycle cost. At infinite storage time both memory states tend to the same Gibbs state and retain no source information. Their modeled memory-cycle bounds tend respectively to 3J+k_BT ln P and k_BT ln P, assuming the same blind reset convention.

Dividing retained information by a thermodynamic lower bound gives an optimistic score, not an actual efficiency. At 32 updates these scores are about 0.01122 and 0.44591 nats per k_BT of memory-cycle bound. Real control and reset costs can reduce achievable efficiencies and can change their ordering.

## 4. Preparation, side information and omitted costs

The oriented blank is common initial infrastructure. Preparing it from the declared Gibbs memory has free-energy work bound

\[
W_{\rm prep}\ge k_BT\ln P(1/3)
=k_BT[23\ln2-13\ln3]
\approx1.66043\,k_BT.
\]

Count this once at startup, then amortize over reuse only if each cycle actually returns the apparatus to the same blank. Adding it to a single startup-plus-memory-cycle job gives bounds approximately 4.22774 k_BT for one-hot and 3.15761 k_BT for ground. Re-adding it every cycle after already charging a return-to-blank reset would double-count preparation.

If R is physically available as usable reset side information, a separate ideal conditional-reset free-energy bound replaces H_r by H(M_r|R)=H_r−I_r. The modeled cycle bound is reduced by k_BT I_r. At 32 updates the corresponding bounds are about 2.53851 k_BT for one-hot and 0.82958 k_BT for ground. A bookkeeping reference label does not make that access free: retaining and controlling from the actual source system requires its own apparatus and cost. The blind-reset comparison does not assume it.

| Resource category | One-hot | Complementary ground | Current accounting |
|---|---|---|---|
| Reserved boundary memory | 12 bits, area 12a0 | Same | Exact state-space cost |
| Initial oriented blank | Same pure state | Same pure state | Free-energy lower bound; exact preparation OPEN |
| Carrier write | Controlled single memory flip for binary test | Controlled global 12-bit complement | Endpoint work derived; drive/clock cost OPEN |
| Single-bit implementation | Face flip reaches 6J | Best local path barrier 10J | Exact path energies; losses and controller OPEN |
| Storage for 32 updates | 64 fresh Gibbs bath qubits | Same | States and heat specified; renewal implementation OPEN |
| Site-selection control | 32 fresh uniform 12-state degenerate controls | Same | State entropy specified; routing/reset OPEN |
| Readout | Optimal full-word discrimination | Optimal full-word or majority | Error derived; apparatus and output-memory cost OPEN |
| Return to blank | Blind reset | Blind reset | Free-energy lower bound; protocol/excess cost OPEN |
| Native normalization | J, epsilon, T, clock, a0 | Same | Not derived; G05/G06 remain OPEN |

The fresh-bath count is the resource consumption of the declared replay implementation, not a theorem that every implementation needs 64 distinct qubits. Reuse needs a lawful renewal rule. The 10J barrier is a transient energy requirement for single-bit paths, not an extra 10J of irreversible net work to add to the ledger. A collective drive bypasses that particular path restriction while introducing a different control requirement.

## 5. What ranking is justified

Within this declared memory model, at the same area and 32-update horizon, ground encoding retains more information, has lower modeled cycle work bound, and passes the stated 1/100-error criterion. It is the better candidate for this retention task. No global encoding optimum or complete apparatus-cost advantage is proved.

For positive, consistently defined actual total costs C_g and C_h, retained information per cost favors ground exactly when

\[
\frac{C_g}{C_h}<\frac{I_g}{I_h}\approx23.18173.
\]

This threshold states how much cost overhead the information advantage can tolerate; it does not assign the unknown actual costs. A vector of preparation purity, physical memory, control locality, bath consumption and reset work must remain visible until a scalar objective is declared.

## Next gate and disposition

DERIVED: retained-information density; exact retained-error comparison; memory energies and heat; consistent blind-reset cycle bounds; preparation amortization rule; side-information dependence; explicit resource gaps.

OPEN: complete autonomous control/renewal/readout/reset apparatus, physical calibration, extensive logical code density, refinement consistency and horizon interpretation. The highest-priority mathematical continuation is a local-control write/retention design with specified bath renewal and output retention, followed by the same ledger. Further optimizing a zero-write-energy code without closing those source choices cannot establish a thermodynamic gravitational coefficient.

Development — no registry entry. No ledger, registry, site or repository updates. Physical promotion 0; independent review OPEN. The unavailable Gap2_FINAL_Finite_Genesis.png was unused.
