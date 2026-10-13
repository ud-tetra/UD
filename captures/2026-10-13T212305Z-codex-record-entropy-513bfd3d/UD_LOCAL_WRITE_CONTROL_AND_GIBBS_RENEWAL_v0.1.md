# Local write control, Gibbs renewal and repeated resource comparison

2026-10-13. Benjamin Walker Mayes, AI-assisted development. Development — no registry entry. Physical promotion 0; independent review OPEN.

## Outcome and source scope

A local memory-gate sequence now implements the complementary ground encoding from a blank. A matched-energy Gibbs-cell SWAP gives an exact bath-refresh rule. These protocols reproduce the earlier storage kernel, so the retained-information comparison remains valid. Switching work, gate count, latency and consumed reservoir cells are now explicit.

The protocols are declared physical candidates. Native boundary incidence determines allowed neighbor gates. Native UD does not select the coupling-switch law, pulse clock, Gibbs source, transport, recovery efficiency or reset apparatus. G05/G06 remain source-open. The work below supplies concrete conditional mechanisms rather than interpreting the previous ideal collective gate as already local or autonomous.

## 1. Local seed and neighbor fanout

Use the earlier fair binary carrier input: core cell for R=0 and exposed face f for R=1. Reserve the same twelve-bit memory, initially all-zero, and disconnect its thermal bath during writing.

First write P_f into memory bit 0. Then apply eleven neighbor CNOTs, copying an already written parent bit into a still-blank child. The checked target order is

\[
0,2,6,1,4,8,3,5,7,9,10,11.
\]

Every child has a parent sharing a boundary edge. The gate-parent pairs are in results.json. For R=0 all bits remain zero; for R=1 all become one. This implements the same encoded isometry on the declared blank input. It is not asserted to equal the collective complement gate on arbitrary dirty memory.

For a memory CNOT from parent p to target t, use pulse

\[
K_{p,t}=\frac{\pi\hbar}{2\tau_g}n_p\otimes(I-X_t),\qquad n_p=|1\rangle\langle1|.
\]

Temporarily switch off the three Ising bonds incident to the target. The remaining memory Hamiltonian commutes with this pulse, so it produces the intended gate, apart from diagonal free phases that do not change the test's pointer statistics. Restore those bonds after the pulse. This gives a local two-memory-bit gate with local target-bond switching; it does not require a twelve-bit pulse operator.

The carrier seed needs an explicit hold. Set A=P_f and temporarily remove its native cross-incidence terms AH_C(I−A)+(I−A)H_CA. The exposed face has four incidence neighbors: three edges and its attached cell. Removing these four couplings makes A commute with the held carrier Hamiltonian. Apply the analogous A-controlled seed pulse while the target memory bonds are off, then restore the carrier couplings. This records the initial binary label without assuming native carrier evolution stops everywhere.

For the declared real basis inputs the mean carrier coupling-switch work is zero. General coherences need the carrier backaction account. Switching four carrier couplings, three memory bonds, and supplying timed pulses are resource requirements, not native emergent controls. Once the seed is written, the carrier can resume native evolution while fanout acts only on memory.

No independent thermal updates are applied during either write. Gate errors and thermal leakage during isolation are omitted by declaration; they are not asserted physically absent.

## 2. Signed switching work and pulse ledger

Along the R=1 fanout path, the post-gate memory energies in J units are

\[
0,6,8,6,8,10,8,10,8,10,8,6,0.
\]

For each target flip, removing its incident bonds contributes −E_inc(before), and restoring contributes +E_inc(after). Summing over the twelve flips gives −36J and +36J on the R=1 branch. The R=0 branch contributes zero. Thus the fair ensemble gives

\[
W_{\rm off}=-18J,\quad W_{\rm restore}=18J,
\quad W_{\rm net}=0.
\]

The largest conditional memory energy is 10J, matching the independently certified optimal local path barrier. Gross restoration work is not just the maximum energy barrier. The one-hot write instead gives zero bond-removal work and 3J mean bond-restoration work.

For each ideal controlled pulse, let kappa=pi hbar/(2 tau_g). Switching on the pulse contributes kappa/2 mean interaction energy for the fair, perfectly encoded branch ensemble; switching it off recovers the same amount. This cancels in the ideal net pulse work, but its recovery and control hardware are additional requirements. The ground sequence uses twelve such pulses, while one-hot uses one. Losses in pulse control are kept separate from memory-bond recovery below.

Both protocols are externally scheduled. A fixed gate list supplies a reproducible local-control specification, not a source-derived autonomous clock or a proof of zero controller-reset cost.

## 3. Local thermal collision and bath refresh

At each storage step choose a site uniformly. Its three neighbor labels define a memory gap 2J or 6J. Swap the site's energy-ordered bit with the matching bath qubit, leaving the other qubit unchanged. The previously verified conditional swap is an energy-conserving unitary V_i supported on a local star: target, three neighbors and two bath qubits.

An exact pulse generator is pi hbar(I−V_i)/(2 tau_b). Since V_i is an involution commuting with memory-plus-bath energy, so does this generator. This is geometrically local to the star, but it is not a derived two-local Hamiltonian. Resolving it into lower-body couplings is a further control question.

Renew both bath qubits by swapping them with fresh, independent Gibbs cells having the same respective Hamiltonians 2J n and 6J n. A matched-energy SWAP commutes with the sum of those two identical Hamiltonians and has zero net free-energy change of the pair. More strongly, for any correlated old memory/bath state,

\[
\mathrm{SWAP}_{B,R}(\rho_{MB}\otimes\tau_R)
\mathrm{SWAP}_{B,R}^\dagger=\rho_{MR}\otimes\tau_B.
\]

Thus the refreshed bath is exactly Gibbs and independent of the retained memory. All old correlations move into the outgoing stream cell. The proof holds quantum mechanically, not only for diagonal inputs. The checker additionally verifies classical factorization examples at probabilities 1/4 and 1/28.

Site selection is represented by a degenerate twelve-state control in the uniform Gibbs state. Refresh it by the same SWAP rule with a fresh independent uniform degenerate cell. This removes old control/memory correlations by export; it does not erase them within a closed finite apparatus.

For 32 storage updates the specified refresh implementation consumes 64 Gibbs qubit cells and 32 uniform twelve-state cells. It requires 64 bath-qubit swaps and 32 site-control swaps, in addition to 32 local thermal collisions. This is a per-run finite stream requirement. Indefinite operation needs continued reservoir supply or a separately specified rethermalization apparatus.

At beta J=(ln3)/2, incoming bath-pair mean energy is

\[
2J(1/4)+6J(1/28)=5J/7.
\]

Thirty-two pairs therefore carry energy inventory 160J/7. This shared incoming inventory is not extra dissipated work to add to the cost ledger. Bath heat is determined by outgoing-minus-incoming energy. Pulse/transport losses, preparing and moving stream cells, and returning the reservoir to its starting state are not determined by the ideal SWAP identity.

## 4. Repeated information and cost comparison

The local write produces the same blank or encoded word as before, and refreshed collisions induce exactly the previous memory kernel. At 32 storage updates:

| Quantity | One-hot | Local ground fanout |
|---|---:|---:|
| Retained information, nats | 0.02879899 | 0.66761023 |
| Information density | 0.00239992/a0 | 0.05563419/a0 |
| Optimal error | 0.41114666 | 0.00923883 |
| Write pulses | 1 | 12 |
| Memory bond off/on rounds | 1 target round | 12 target rounds |
| Mean bond-removal work | 0 | −18J |
| Mean bond-restoration work | 3J | 18J |
| Storage bath/control cells | 64 / 32 | 64 / 32 |
| Ideal memory-cycle work bound | 2.56731 kBT | 1.49719 kBT |

Localizing the write does not change the retained-information numbers under perfect isolated gates. It changes latency and recovery requirements. With durations tau_g and tau_b, total write-plus-storage times are tau_g+32 tau_b and 12 tau_g+32 tau_b. This is a same-storage-horizon comparison, not a same-wall-clock-deadline comparison. Neither duration has a native physical calibration; the extra eleven write slots must not disappear from a performance claim.

To expose sensitivity, declare eta in [0,1] as recovery efficiency for negative memory bond-switch work. Let gamma kBT be the same additional implementation work per local write gate, covering pulse/timing/switch-actuator losses other than the already counted memory bond-recovery loss. Let c0 kBT be common nonnegative excess work from storage, refresh, readout and reset under the stated blind-memory-reset/export convention. Then the corresponding cost floors are

\[
\frac{C_h}{k_BT}\ge b_h+\gamma+c_0,
\qquad
\frac{C_g}{k_BT}\ge b_g+12\gamma+18\beta J(1-\eta)+c_0,
\]

where b_h=2.567311... and b_g=1.497188... are the derived ideal memory-cycle bounds. The eta and gamma laws are declared engineering assumptions; they are not coefficients recovered from UD. Actual reset may exceed its free-energy floor and finite exact pure reset is not supplied.

Comparing these floors, ground has lower total work when

\[
11\gamma+18\beta J(1-\eta)<b_h-b_g.
\]

At gamma=0 this requires eta approximately greater than 0.89177. At eta=1 it requires gamma approximately less than 0.097284 kBT per gate. If neither is met, ground can cost more net work even while retaining much more information.

For the costs assigned by this common-overhead model, retained information per work still favors ground for all nonnegative gamma,c0 and eta in [0,1]. Algebraically let R=I_g/I_h=23.18173...; then R>12 and R b_h>b_g+18 beta J. Therefore

\[
R(b_h+\gamma+c_0)-[b_g+12\gamma+18\beta J(1-\eta)+c_0]>0.
\]

This conclusion concerns the parameterized cost floors or an implementation whose excess costs equal the declared terms. Lower bounds alone cannot rank unknown actual costs. Different costs per gate, technology-dependent readout/renewal, or different reset excesses require a revised ledger. The retained-information advantage does not prove a universal apparatus-efficiency advantage.

## 5. Closure boundary

SPECIFIED and CHECKED under declared protocols: neighboring fanout gates; local target-bond switching; four-incidence carrier seed hold; signed switching work; matched Gibbs refresh; correlation export; exact unchanged storage statistics; latency and recovery sensitivity.

OPEN: source-selected autonomous coupling switches and clock, practical local-star Hamiltonian decomposition, physical control/transport losses, equilibrium stream supply, readout and pure-reset implementation, extensive record density, refinement and horizon normalization. A finite closed reservoir with cyclic restoration is not obtained by relabeling fresh-stream export as renewal.

This step closes the mathematical gate-list and refresh-channel definitions. It does not close native UD provenance or physical apparatus cost. Physical promotion 0; independent review OPEN. No ledger, registry, site or repository entries changed. Gap2_FINAL_Finite_Genesis.png remained unavailable and unused.
