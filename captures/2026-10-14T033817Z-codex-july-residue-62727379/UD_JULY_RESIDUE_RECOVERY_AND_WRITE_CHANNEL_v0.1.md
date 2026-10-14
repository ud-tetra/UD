# July residue recovery and carrier-to-memory write channel v0.1

**Development — no registry entry. Physical promotion 0. Independent review OPEN.**

## Result and source boundary

The July-labelled Base44 presentation supplies a seven-channel eigensplit and an exponential residue curve. Its public chart code evaluates the exponential formula directly; it does not derive it from a recovered mixing matrix. The linked plot names `ud-k4-residue-accumulation-spec-v1.md` and `IFS_CHANNEL_MIXING_OPERATOR_DERIVATION_v0_1_M_MATRIX.csv`. Their original bytes have not been recovered.

The reported spectrum alone obstructs a direct linear-observable derivation of the quarter-loss law. A seven-channel matrix can be reconstructed conditionally from additional symmetry and stationary-vector assumptions. A separate, local, energy-conserving write interaction produces exponential transfer for an arbitrary coupling-time parameter. Reusing one coherent memory does not produce that exponential law.

None of these results selects the historical 3/4 factor as a native UD constant. The source-authored matrix, state-to-energy map, write mechanism and physical clock remain OPEN.

## 1. What was recovered

Sources inspected: the live Base44 page and its public application bundle; its linked residue plot; legacy UD2, WBS and dashboard pages; the two attached manuscript PDFs and companion DOCX; the supplied reconstruction ZIP and equation placeholders; the supplied notes; and focused Library searches for the two named originals.

The snapshot reports eigenvalues 1 (one dimension), 9/21 (two dimensions), 8/21 (three dimensions), and 0 (one dimension), and declares R(n)=E0[1-(3/4)^n]. The plot groups the modes as 1+5+1. The public `fpe` chart function computes `(3/4)^n` and its complement directly. The downloaded plot is an image, not an executable simulation or matrix CSV. The three supplied files coherence_equation.md, master_action.md and carrier_definition.md contain reconstruction placeholders.

The searches did not resolve the original specification or CSV. This is a bounded recovery result, not a claim that the originals do not exist elsewhere. Public-source URLs, retrieval timestamps and SHA-256 are retained in FETCH_RECEIPT.json. Exact relevant bundle excerpts are preserved separately. The July date is supplied by the user; the inspected live bytes were retrieved in October 2026.

## 2. Exact spectral obstruction

For any seven-dimensional matrix M with the reported algebraic eigenvalue multiplicities,

$$\chi_M(z)=z(z-1)(z-3/7)^2(z-8/21)^3.$$

If x[n+1]=M x[n] and a scalar output is y[n]=ell^T x[n], Cayley-Hamilton gives chi_M(E)y=0, where E shifts n to n+1. A nonzero geometric output y[n]=C q^n requires chi_M(q)=0. At the historical q=3/4,

$$\chi_M(3/4)=-\frac{268119}{275365888}\ne0.$$

Thus a linear observable under direct iteration cannot decay as (3/4)^n. The constant and exponential terms in the proposed residue law cannot be combined into an exact output of that iteration either, because the exponential component violates the recurrence. This statement applies to the declared direct linear model, including matrices with Jordan blocks. A nonlinear readout, changing operator, coarse-graining, forcing or separate write channel must be specified before making a different inference.

## 3. Conditional seven-channel reconstruction

Let the first four coordinates label the vertex-face channels and the last three label opposite-edge channels. Declare the natural S4 permutation action, the unit Euclidean metric, a real self-adjoint mixing operator, and a uniform stationary Perron vector. These are reconstruction assumptions; they are not recovered matrix entries.

Define orthogonal projectors

$$P=J_7/7,\quad V=\operatorname{diag}(I_4-J_4/4,0_3),\quad E=\operatorname{diag}(0_4,I_3-J_3/3),\quad R=I-P-V-E.$$

Their ranks are respectively 1,3,2,1. The conditional operator is

$$M=P+\frac8{21}V+\frac37E
=\frac1{21}\begin{pmatrix}
9&1&1&1&3&3&3\\
1&9&1&1&3&3&3\\
1&1&9&1&3&3&3\\
1&1&1&9&3&3&3\\
3&3&3&3&9&0&0\\
3&3&3&3&0&9&0\\
3&3&3&3&0&0&9
\end{pmatrix}.$$

It is nonnegative, symmetric and doubly stochastic. Its spectrum and multiplicities match the report. Its rank is six. S4 covariance is checked for all 24 vertex permutations.

Uniqueness under these assumptions follows directly. Write a,b for the VF diagonal and off-diagonal entries, c,d for EE entries, and e for the common cross entry. The sector eigenvalues give a-b=8/21 and c-d=3/7. Uniform stationarity gives a+3b+3e=1 and c+2d+4e=1. The zero eigenvalue in the remaining invariant line gives a+3b=4e. The resulting five-equation system has rank five and yields a=c=3/7, b=1/21, d=0, e=1/7.

The kernel is the signed contrast vector (3,3,3,3,-4,-4,-4), not a nonnegative probability occupation. Moreover,

$$RM=MR=0,\qquad RM^n=0\ (n\ge1),\qquad \lim_{n\to\infty}M^n=P.$$

Direct iteration therefore annihilates the kernel component on the first step; it does not accumulate positive energy in that component. Rank(M^n)=6 for every positive n. Physical energy requires a separately declared observable and dynamical mechanism.

This operator has 43 nonzero entries, with mean row support 43/7. That equals the number in ledger entry C07, but does not establish identity with its source derivation. The equality depends on the reconstruction assumptions.

### Why this is not a recovered original

Remove uniform stationarity. Let v=(t,t,t,t,1,1,1), P_t=vv^T/(4t^2+3), and M_t=P_t+(8/21)V+(3/7)E. At t=3/4 this gives a different, nonnegative, self-adjoint, S4-equivariant matrix with the same spectrum and rank, but 49 nonzero entries and nonuniform row sums. Exact projector checks certify its eigensplit. Thus symmetry, positivity, self-adjointness and the reported spectrum do not identify the original matrix without the extra stationary-vector rule.

## 4. General local write interaction, derived before selecting a rate

Declare a binary active carrier A and a memory qubit m with matched excitation energy epsilon:

$$H_0=\epsilon(n_A+n_m),\qquad H_{\rm int}=g(\sigma_A^+\sigma_m^-+\sigma_A^-\sigma_m^+).$$

The interaction conserves total excitation and commutes with H0. For a pulse of duration tau, set theta=g tau/hbar. In the one-excitation sector,

$$|10\rangle\mapsto\cos\theta|10\rangle-i\sin\theta|01\rangle,\qquad q=\cos^2\theta.$$

The parameter q is derived from this declared interaction; no numerical target fixes it. Locality and energy conservation hold for every theta, so neither selects q=3/4.

With a fresh memory initially in |0> at every write, after n pulses the joint state for an initially excited carrier is

$$|\Psi_n\rangle=(\cos\theta)^n|1;0\cdots0\rangle
-i\sin\theta\sum_{j=1}^n(\cos\theta)^{j-1}|0;1_j\rangle.$$

All displayed branches are orthogonal. Hence

$$E_A(n)=\epsilon q^n,\qquad E_M(n)=\epsilon(1-q^n),\qquad E_A(n)+E_M(n)=\epsilon.$$

This reproduces the functional form of the residue curve as a **conditional fresh-memory transfer model**. The historical rate would require theta=k pi +/- pi/6. That is an additional coupling-time requirement, not a native UD derivation or a physical clock calibration. The binary carrier's embedding in the native simplicial carrier is also OPEN.

## 5. One coherent memory recurs

If the same memory is reused with no reset, isolation, dephasing or new cell, repeated pulses compose coherently:

$$E_A^{\rm reuse}(n)=\epsilon\cos^2(n\theta),\qquad E_m^{\rm reuse}(n)=\epsilon\sin^2(n\theta).$$

At the illustrative historical parameter theta=pi/6, three pulses transfer all excitation into memory; six return all excitation to the carrier. The irreversible-looking exponential law therefore requires a renewal or record architecture. It is not implied by a two-qubit energy-conserving write alone. The verifier uses exact Chebyshev polynomials to check these probabilities without trigonometric rounding.

## 6. Declared record coarse-graining and entropy

Declare the pointer readout J_n: no write yet, or excitation deposited in cell j. For the initially excited carrier,

$$P(J_n=\varnothing)=q^n,\qquad P(J_n=j)=(1-q)q^{j-1},\quad1\le j\le n.$$

Define the record entropy operationally as S_rec(n)=kB H(J_n | initially active). It is the entropy of this declared readout, not an automatic thermodynamic entropy production claim. Its exact law is

$$\frac{S_{\rm rec}(n)}{k_B}=h(q)\frac{1-q^n}{1-q},\qquad
\frac{S_{\rm rec}(n+1)-S_{\rm rec}(n)}{k_B}=q^n h(q),$$

where h is binary entropy in nats and q<1. The endpoint q=1 has zero record entropy. At q=3/4 the limiting entropy is 4h(3/4)=4 ln4-3 ln3, about 2.24934 nats.

Before coarse-graining, the state for the known active input is pure and its joint von Neumann entropy is zero. An actual durable, classical record requires the physical readout/dephasing apparatus and its resource account. The increasing pointer entropy is not a derivation of a horizon-area law.

## 7. Retained distinguishability and resource boundary

Now let X be an equally likely input bit encoded as ground/excited carrier. X=0 leaves the memory empty. The conditional memory states for X=0 and X=1 differ with trace distance

$$D_M(n)=1-q^n,\qquad e_{\rm opt}(n)=q^n/2.$$

The full pointer readout retains

$$I(X:J_n)=h\!\left(\frac{1-q^n}{2}\right)-\frac12h(q^n)\le\ln2.$$

Timing information about the first write and information about the input bit are distinct quantities. At n=7, q=3/4, the energy transferred is exactly 14197/16384 (about 86.6516%); the conditional pointer entropy is about 1.94909 nats; retained source information is about 0.487733 nats; optimal source-bit error is exactly 2187/32768 (about 6.6742%).

This implementation uses n initially blank memory cells and n addressed pulses. If each allocated cell occupies boundary area a_cell, its retained-information density is I/(n a_cell), bounded by ln2/(n a_cell) and tending to zero. This is a conditional architecture comparison, not a universal lower bound on all possible implementations. Compression, reuse or reset requires its own channel and resource accounting.

Full cost remains OPEN: pure blank preparation, clock/control, switching, readout, retention, reset and renewal. Matched-excitation energy conservation is established for the ideal interaction; it does not assign zero total apparatus work. No G value, dimensional entropy density or physical area scale is supplied.

## 8. Source handoff and verification

The next source dependencies are the original seven-by-seven CSV; the original residue update specification and any decimation/write operator; its state normalization and energy observable; the source rule selecting coupling and clock; and the memory/bath renewal mechanism. These should be recovered before claiming the reconstructed operator or exponential write channel is native UD.

verify_residue.py is newly authored standard-library code. It checks exact projector ranks, all S4 actions, conditional matrix uniqueness, the same-spectrum counterexample, kernel behavior, Cayley-Hamilton and the nonzero chi(3/4) obstruction. For five declared q values and 17 write ages it checks exact normalization, energy inventories, Bayes error, the record entropy recurrence, retained information and coherent reuse. Decimal logarithms are displays checked to 1e-12; acceptance and algebraic equalities use fractions.

Constructor verification PASS. Independent review OPEN. Original July source claims are preserved as source claims, not promoted. This result extends the current record-entropy programme without superseding its native carrier definitions or previous apparatus models.
