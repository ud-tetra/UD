# Record energy balance and spatial boundary entropy

2026-10-13. Benjamin Walker Mayes, AI-assisted development. Development — no registry entry. Physical promotion 0; independent review OPEN.

## Result and source scope

The supplied Pasted text(1).txt proposes analogies between adaptive transport networks and GR/QFT, including the candidate conductance rule dC_ij/dt=f(|I_ij|)−gamma C_ij. Pasted text(2).txt includes that material and the earlier entropy calculation. These texts do not specify a quantum recording interaction, Gibbs reservoir, energy calibration, or horizon map. The supplied carrier_definition.md, master_action.md and coherence_equation.md copies are placeholders. Ledger G05 remains source-blocked and G06 lacks a recovered current normalization receipt. This report derives conditional mathematics without replacing those missing sources.

The previous candidate record channel can be dilated explicitly. It nevertheless fails energy covariance for the declared native Hamiltonian. Separately, the five-tetrahedron spatial boundary supplies a categorical record alphabet, not a tensor product of independent face bits. These results prevent promoting the earlier conditional temporal entropy rate to a native thermodynamic horizon-area coefficient.

## 1. Explicit reversible copying and reduced record entropy

For the filled tetrahedron let C have the fifteen simplex basis states |j>, with B=D^T−D. Let memory M and environment E each have fifteen states, initially |0>. Let X be the cyclic shift on either pointer. Define the unitary

\[
W=\sum_{j=0}^{14}|j\rangle\langle j|_C\otimes X_M^j\otimes X_E^j.
\]

Each controlled block is unitary. In particular W|j,0,0>=|j,j,j>. For any carrier density matrix rho,

\[
\operatorname{Tr}_E W(\rho\otimes|00\rangle\langle00|)W^\dagger
=\sum_j\rho_{jj}|j\rangle\langle j|_C\otimes|j\rangle\langle j|_M.
\]

Tracing E yields exactly the earlier dephased projective instrument. For a pure input sum_j a_j|j>, the global output sum_j a_j|j,j,j> remains pure. C+M has entropy H(p), E has entropy H(p), and their mutual information is 2H(p), where p_j=|a_j|² and all information entropies use natural logarithms. Thus reduced record entropy arises from entanglement and discarding environmental information; the complete unitary does not create total von Neumann entropy.

The pure pointer blanks are resources. E is not hereby a finite-temperature Gibbs bath; the existence of this dilation does not derive heat or temperature. Returning W to its input would erase the apparent record reversibly if all coherent degrees of freedom remained controllable.

## 2. Exact obstruction to a stationary energy-conserving recorder

Declare a candidate physical-energy embedding

\[
H_C=i\epsilon B,\qquad \epsilon>0.
\]

This is Hermitian, and exp(−iH_C t/hbar)=exp(B epsilon t/hbar). The native dimensionless gap is Delta=epsilon t/hbar. Neither epsilon nor physical t is independently calibrated here.

Let D_s(rho)=sum_j P_j rho P_j denote simplex dephasing. Because B has zero diagonal, D_s^*(H_C)=0. Hence

\[
\Delta E_C=\operatorname{Tr}[H_C D_s(\rho)]-\operatorname{Tr}(H_C\rho)
=-\operatorname{Tr}(H_C\rho).
\]

For real pure native carrier states this mean is zero. That does not certify energy conservation of the operation: a complex superposition (|a>+i|b>)/sqrt(2) across an incidence B_ab=±1 has initial mean energy −epsilon B_ab and final mean zero. The mean energy change is state-dependent.

More strongly, a stationary apparatus and an energy-conserving unitary can only induce an energy-covariant carrier channel. Specifically, if [sigma_A,H_A]=0 and [V,H_C+H_A]=0, then the reduced channel Phi obeys

\[
\Phi(e^{-iH_Ct/\hbar}\rho e^{iH_Ct/\hbar})
=e^{-iH_Ct/\hbar}\Phi(\rho)e^{iH_Ct/\hbar}.
\]

Proof: insert the stationary apparatus evolution into the input, commute the joint evolution through V, and take the apparatus trace.

Simplex dephasing violates this identity. With rho=P_top,

\[
D_s([H_C,\rho])=0,\qquad[H_C,D_s(\rho)]=[H_C,\rho]\ne0.
\]

The derivative at t=0 already contradicts covariance. Native pre-evolution commutes with energy translations, so composing it with D_s does not cure the obstruction.

**Scoped NO-GO:** exact simplex dephasing for arbitrary carrier inputs cannot come from a stationary apparatus via an energy-conserving joint unitary under H_C=i epsilon B. Possible candidate extensions include an apparatus with energy coherence, a clock/work resource, a different observable, an approximate recorder, or a different energy embedding. The sources must select and account for the extension. This is not a universal impossibility of recording.

For the explicit copying dilation with degenerate pointers H_M=H_E=0, the operation is not energy conserving. With interaction switched off at both endpoints, its change in free energy expectation is supplied as work, not automatically heat: W_ext=Delta E_C. Work may vanish for the tested real inputs while the operation still requires a resource to violate covariance.

## 3. Exact entropy balance with a declared thermal reservoir

Let X denote the carrier plus all retained memory and apparatus degrees of freedom kept in the accounting. Declare a reservoir R initially independent of X and in tau_R=exp(−beta H_R)/Z, beta=1/(k_B T), with T positive and finite. Let the joint process be unitary. Define Q_R=Tr[H_R(rho_R'−tau_R)], heat deposited in R, and dimensionless entropy s(rho)=−Tr rho ln rho. Then

\[
\boxed{\Delta s_X+\beta Q_R=I(X':R')+D(\rho_R'\Vert\tau_R).}
\]

This is the equality form of Landauer's principle, with entropy decrease convention translated to Delta s_X; see Reeb–Wolf, Theorem 3, arXiv:1306.4352v3, DOI 10.1088/1367-2630/16/10/103011.

The proof is short: initial independence and global entropy conservation give I=Delta s_X+Delta s_R. The Gibbs identity gives D=beta Q_R−Delta s_R. Adding them proves the equation. Both terms on the right are nonnegative. Writing Q_X=−Q_R gives

\[
\Delta S_X=Q_X/T+k_B\Sigma,\qquad
\Sigma=I+D\ge0,\quad S_X=k_Bs_X.
\]

This equation supplies the missing conditional entropy balance; it does not identify X with a spacetime horizon or equate its joint entropy with the marginal history entropy. Work enters the energy balance separately. Initial bath correlations, nonthermal baths, unaccounted apparatus memory, or retained interactions require additional terms or revised definitions.

For a finite bath with full-rank tau_R, Sigma=0 forces rho_R'=tau_R and I=0, hence Q_R=0 and Delta s_X=0. Therefore a nontrivial finite process does not satisfy exact Clausius equality merely by setting its production term to zero. A controlled limiting construction would be required.

Blindly resetting a classical n-record memory with entropy H_n to a blank gives the formal bound Q_R>=k_B T H_n under these assumptions. If the latest carrier label is retained as usable side information, erasing history while preserving that label instead decreases joint entropy by H_n−H(R_n). In the stationary fifteen-label chain, H_n=ln 15+(n−1)h_star, so this joint entropy decrease is (n−1)h_star. At Delta=pi/4, h_star=(32/15)ln 2. Accessible side information and reset protocol must be declared; the random label process alone does not fix reset cost.

Exact pure reset of a mixed local memory is impossible with a finite full-rank thermal bath: input rank r*d_R exceeds d_R when r>1, but a final pure-memory product state has rank at most d_R. The heat bound is a necessary bound for permitted resets/limits, not an existence proof for finite exact erasure.

## 4. Five tetrahedra: an actual spatial record rule

Use core cell 0123 and attach one new apex to each core face, giving five cells total. Exact enumeration gives

\[
f=(8,18,16,5),\quad\dim C_\bullet=47,
\quad N_{\rm exposed}=12,\quad N_{\rm internal}=4.
\]

Every boundary edge belongs to two exposed faces and the boundary Euler characteristic is 2. Under a declared equilateral metric with edge ell, each exposed triangle has area a0=sqrt(3)ell²/4 and A=12a0=3sqrt(3)ell². The combinatorics do not fix ell or identify this spatial boundary as a causal horizon.

Declare face projectors P_f onto the twelve exposed face coordinates and P_out=I−sum_f P_f. For normalized rho on the 47-dimensional carrier,

\[
p_f=\operatorname{Tr}(P_f\rho),\quad
p_{\rm out}=1-\sum_f p_f,
\quad S_{\rm spatial}=-k_B\sum_{x\in\{f,\mathrm{out}\}}p_x\ln p_x.
\]

This is a simultaneous spatial coarse-graining with thirteen mutually exclusive outcomes. In an equivalent twelve-bit occupancy representation, at most one bit is 1. The bits are correlated by the single-carrier constraint. Consequently

\[
0\le S_{\rm spatial}\le k_B\ln13.
\]

For boundary-supported states p_out=0, the bound is k_B ln12. It is attained by a declared uniform superposition of the twelve faces. This example gives eta=k_B ln12/(12a0), but the uniform state is a candidate and the number is not universal.

For an N-face family using this same single-carrier rule, S_spatial<=k_B ln(N+1). With fixed a0 and growing area A=N a0, S_spatial/A tends to zero. Thus this rule cannot yield a positive extensive boundary-area density. A multi-carrier/tensor-product local memory construction, extensive temporal placement, or another physical record rule would be needed. This does not rule out an area law for a separately derived many-body boundary state.

Refinement adds another constraint. Splitting one outcome of probability p into m equiprobable resolved children increases entropy by k_B p ln m even though its total metric area remains fixed. Redundant copies add zero joint entropy. A coarse-to-fine state/readout map must distinguish these two operations. Geometric refinement alone does not choose one.

## 5. How the adaptive-conductance proposal can contribute

Changing incidence weights in a prescribed real skew generator B(C(t)) keeps each carrier evolution unitary. It does not by itself create total information entropy or supply a thermal bath. State-dependent feedback also needs a declared physical feedback implementation rather than assuming a linear quantum channel.

A separate classical candidate can be stated: nonnegative symmetric rates w_ij=w_ji=alpha_ij C_ij, with dot p_i=sum_j w_ij(p_j−p_i). For positive probabilities its Shannon entropy satisfies

\[
\dot H=\frac12\sum_{ij}w_{ij}(p_j-p_i)\ln(p_j/p_i)\ge0.
\]

This proves a conditional mixing law, not a UD heat law. To obtain heat accounting, independently declare energies and local detailed balance w_ij/w_ji=exp[−beta(E_j−E_i)], with w_ij now denoting i-to-j rates. Then for J_ij=p_iw_ij−p_jw_ji,

\[
\dot S-k_B\beta\dot Q_{\rm in}
=k_B\sum_{i<j}J_{ij}\ln\frac{p_iw_{ij}}{p_jw_{ji}}\ge0,
\quad\dot Q_{\rm in}=\sum_{i<j}J_{ij}(E_j-E_i).
\]

If energies change, sum_i p_i dot E_i is a work term. Conductance maintenance and feedback resources must also be included. The pasted adaptation equation does not specify f, the rates, energy gaps, or bath temperature, so no particular entropy production follows from it yet. Its other analogy claims are not used as evidence here.

## Disposition

DERIVED under declared choices: reversible copying dilation; energy-covariance obstruction; thermal entropy identity; five-tetrahedron spatial alphabet; logarithmic entropy bound; refinement dependence.

OPEN: source-derived recorder/resource, physical energy and clock normalization, many-body boundary state, extensive local record capacity, causal horizon, and gravitational normalization. G was not used. No ledger, registry, repo, or website entries were changed. The unavailable Gap2_FINAL_Finite_Genesis.png was unused.

Next source programme: construct local boundary memory coupled to the carrier with a declared conserved energy, clock/work source and Gibbs bath, and derive the coarse-to-fine state map. Test entropy production and area scaling together rather than fitting either coefficient independently.

## Exact external source

David Reeb and Michael M. Wolf, *An improved Landauer Principle with finite-size corrections*, New Journal of Physics 16 (2014) 103011. https://arxiv.org/abs/1306.4352 ; https://doi.org/10.1088/1367-2630/16/10/103011 . Theorem 3 and Sections 3.2–3.3. This is an external statistical-mechanics theorem, not a native UD source derivation.
