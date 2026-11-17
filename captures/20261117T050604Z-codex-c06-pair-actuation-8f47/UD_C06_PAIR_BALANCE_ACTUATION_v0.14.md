# C06 pair-balance actuation v0.14

**EXACT / CONDITIONAL** for the stock identity and regularity obstruction. **CANDIDATE (agile)** for a declared threshold switch. **OPEN** for native actuation and deficit allocation. Physical Promotion = 0.

## 1. Port and source boundary

Use ordinary edge coordinates \(x\in X=\mathbf1^\perp\subset\mathbb R^6\). Let \(P_E,P_-\in\operatorname{End}(\mathbb R^6)\) be the orthogonal projections onto the two-dimensional even shear and three-dimensional odd shear sectors from v0.13. Align the active records with the source using the v0.12 sector isometries \(F|_k/\omega_k\), where \(F\) is the flag copy and \(\omega_k>0\) are the unweighted v0.11 phase rates. In these aligned record coordinates \(y\in X\), stocks use the Euclidean norm. Statements about \(y_e\) below assume these coordinates; raw face flags have their declared action metric.

The initial record is empty. The unmodified \(E\) exchange stays independent of the odd block, and each block conserves its own squared stock in dimensionless time. This is the setting tested against v0.12 (UD #540) and v0.13 (UD #541). Ledger v0.39 Q166–Q170 describes signed chain-incidence currents and control-volume stocks. Those sources give current through incidence and a balance law. They supply no mapping from the proposed ordinary opposite-edge product to a transition of the odd coupling coefficient. The inspected binary parity and closure interface in C06 v0.7, *Scoped receipt insufficiency*, also leaves quantitative exchange unspecified.

## 2. The proposed pair product is a mixed stock observable

For an opposite pair \((e,e')\), define \(x_\pm=(x_e\pm x_{e'})/\sqrt2\) and \(y_\pm=(y_e\pm y_{e'})/\sqrt2\). Then

\[
J_{e,e'}=x_e x_{e'}-y_e y_{e'}
=\tfrac12(x_+^2-y_+^2)+\tfrac12(y_-^2-x_-^2).
\]

This scalar is symmetric under \(e\leftrightarrow e'\). The actual odd-sector stock difference is \(B=\|P_-y\|^2-\|P_-x\|^2=\sum_{\rm pairs}(y_-^2-x_-^2)\). Example with raw pairs ordered successively: \(x=(2,0,-1/2,-1/2,-1/2,-1/2)\), \(y=0\). The first pair has \(J=0\) while the odd sector has zero recorded stock. For the aggregate product, the even and odd discrepancies still enter with opposite signs. An exact false trigger for the aggregate is \(x=(6,0,0,-6,0,0)\), \(y=0\). The two initial sector norms are equal and nonzero, giving \(\sum J=0\).

On a pure odd block each pair product equals half its odd stock difference, so its sum is \(B/2\). Under the declared reciprocal odd exchange \(\dot u=-a v,\ \dot v=a u\), where \(u=P_-x,v=P_-y\), the record stock flux is \(2a\langle u,v\rangle\); \(\dot B=4a\langle u,v\rangle\). For the running fixed-rate oscillator at the first half-stock crossing, \(B=0\) and the flux is \(aN>0\), where \(N=\|u\|^2+\|v\|^2>0\).

## 3. Exact finite-time obstruction for regular feedback

Take the aligned direct sum of the unchanged \(E\) exchange and the declared odd exchange above. If \(a\) is locally Lipschitz in state and vanishes at every point of the balance surface \(B=0\), then that surface is invariant. The odd stocks are held there and the even block may continue. Local uniqueness, also backwards, precludes a finite first hit from \(B<0\). The proof assumes both a locally Lipschitz autonomous vector field and an invariant balance surface.

For the explicit smooth candidate \(a=\omega(1-2f)\), \(f=\|v\|^2/N\), the empty-record trajectory has \(u=\cos\theta\,u_0,\ v=\sin\theta\,u_0\) and \(\dot\theta=\omega\cos(2\theta)\). The ratio \(z=\tan\theta\) obeys \(\dot z=\omega(1-z^2)\) from \(z=0\). Thus \(z=\tanh(\omega t)<1\) at every finite \(t\); half-stock is reached only as a limit. A zero of the observable alone supplies no switch.

## 4. Declared finite-time comparator

For \(N>0\), prescribe \(a=\omega\) for \(B<0\) and \(a=0\) for \(B\ge0\); leave a zero-preparation odd block inert. Start from \(v=0\). The resulting absolutely continuous trajectory follows the constant-rate rotation up to \(t=\pi/(4\omega)\) and holds both odd amplitudes there afterwards. In the incoming first-quadrant phase neighborhood the balance is nondecreasing, so autonomous continuation from the first hit stays at balance. This rule uses current state and needs no separately stored completion bit on the ideal trajectory. Cutting the shared scalar cuts both directions and preserves stock. The even exchange stays active during the hold. The v0.12 handoff and full matching swap remain separate assumptions for the final shear response.

This discontinuous rule is a target-informed constitutive choice. The source audit leaves open a native event implementing that discontinuity, a state carrying completion through departures from balance, and Stage 2 selection. With no coupling to the even sector this ideal hold excludes leakage by assumption. The replay uses exact fractions for algebraic controls; the finite-time statements follow from the analytic equations.

## 5. Reproduce

Run python3 replay_c06_pair_balance.py. It checks exchange symmetry, the mixed and aggregate false triggers, true parity-resolved balance, reciprocal stock derivatives, and the switch at an exactly rational normalized balance. It also verifies the smooth Riccati reduction at rational test points.
