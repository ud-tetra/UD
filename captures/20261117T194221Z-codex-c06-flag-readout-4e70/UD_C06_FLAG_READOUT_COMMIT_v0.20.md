# C06 flag readout and terminal commit v0.20

**EXACT / CONDITIONAL** for the readout on the declared invariant range and the off-range counterexample. **CANDIDATE** for a shared terminal commit. **Physical Promotion = 0.**

## Local flag observations

Use the v0.11 Whitney flag port and the v0.12 and v0.16 aligned dynamics. Let \(G\) be the copy map from mean-zero ordinary-edge coordinates into twelve face flags, \((Gz)_{f,e}=z_e\) for \(e\subset f\). The unit-cell metric on the three cooriented flags of a face is \((u-v)I+v\mathbf 1\mathbf 1^\top\), with \(u=53/9,\ v=47/9\). Each odd basis vector \(\psi_i=(e_i-e_i')/\sqrt2\) uses a pair of opposite edges. The aligned record coordinate is \(b_i=\langle G\psi_i,y\rangle_Y/\omega_-\), where \(G^\dagger G\psi_i=\omega_-^2\psi_i\) and \(\omega_-^2=106/9\).

For an empty initial record and the declared closed flow, \(\dot y=Gx\) keeps \(y\in\operatorname{im}G\). The dynamics after the selective cut also map source into this range. Thus \(y=Gz\) and
\[
b_i=\omega_-\langle\psi_i,z\rangle
=\frac{\omega_-}{\sqrt2}\left(y_{f,e_i}-y_{f',e_i'}\right),
\quad e_i\subset f,\ e_i'\subset f'.
\]
Any one flag on each edge suffices. The even component cancels because it is equal on the two opposite edges. Consequently the v0.19 pair guard can read the balanced odd stock from the carrier-edge difference, two flag samples and the declared rate. Opposite edges lie on disjoint pairs of faces. The formula requires access across the pair, with no assumption that an existing native process supplies this access.

The formula has a sharp range condition. Each face contains exactly one edge of a given opposite pair. The coefficients of \(\langle G\psi_i,y\rangle_Y\) on that face are signed \(u/\sqrt2\) on that edge and signed \(v/\sqrt2\) on each other edge. For the unweighted unit cell all twelve coefficients are nonzero. Perturbing one off-pair flag changes the exact aligned coordinate while preserving the four flags of the observed pair. Hence the four pair flags alone cannot recover that coordinate on the full record space. With the declared alternative \(v=0\), the off-pair coefficients vanish, confirming the role of metric mixing. Invariant-range preparation avoids this obstruction. Disturbances outside that range require a separate bound or full readout.

## Simultaneous receipts

Suppose the common-phase preparation and direct access of v0.19 hold. All populated pairs report the first upward balance at one model time. An atomic shared Ready-to-Hold transition may consume any nonempty batch of qualifying receipts at that time, set the terminal record once and select \(GP_+\) without advancing the amplitude state. The OR of qualification is invariant under ordering and duplicate insertion. Equivalent serial processing with no intervening flow and a shared atomic Ready test commits once. This is a conditional logical construction. Independent pair-local Ready bits would each permit a commit and supply no global exclusion. The flag-copy geometry and metric furnish readout identities, while native cross-pair access, shared arbitration and same-event actuation remain open. Stage 2 remains open.

## Exact replay

Run python3 replay_c06_flag_readout.py. The replay constructs the tetrahedron faces, tests all three adjoint rows and all corresponding flag choices, checks the off-range witness and enumerates ordered receipt lists of lengths 0–3 with duplicate submissions.
