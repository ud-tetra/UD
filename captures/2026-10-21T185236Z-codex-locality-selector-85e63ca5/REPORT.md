# Locality and conserved-mean selection audit v0.1

**Development — no registry entry; exact finite algebra and conditional proofs; constructor checks only. Physical promotion 0.**

## Premises and conclusion
The subject is the recovered THM561 real unsigned six-edge transport, not the signed23D target representation. Let S exchange opposite tetrahedral edges and J be the6x6 all-ones matrix. The source T=(5I+S+J)/12 and H=I-T have eigenlevels0(1),1/2(2),2/3(3). The prior Kminus phase-lift candidate interpolates these into0,3,5. It did not derive that conversion from a source law. This audit tests whether declared relation locality, symmetry, graph nonnegative conductances and conserved mean repair that gap. They narrow it but do not select the conversion.

## Exact graph family and remaining freedom
The S4 action on ordered edge pairs has exactly three orbits: diagonal(size6), opposite(size6), cross/shared-vertex(size24). Thus every real symmetric S4-invariant conservative scalar graph Laplacian with these relations is

Q(x,y)=(x+5y)I+(y-x)S-yJ.

Here x is the conductance on an opposite-edge pair, y on a cross pair. Nonnegative conductances mean x>=0,y>=0. The connected branch used here has y>0, since y=0 gives three disconnected pairs. Row conservation fixes the diagonal x+4y; incidence identifies the relation types but does not set x/y.

The eigenspaces are P0=J/6, Pminus=(I-S)/2, Phalf=(I+S)/2-J/6. Direct multiplication yields eigenlevels0,6y,2x+4y with dimensions1,2,3. Consequently the ratio is2/3+x/(3y). A common scale leaves x/y unchanged, so locality, symmetry, conservation and conductance positivity leave one independent shape parameter. The source H uses x/y=2 and ratio4/3; the interpolated target match uses x/y=3 and ratio5/3. No source mechanism changing2 into3 is supplied.

## Nonnegative graph weights remove one assignment, not the source gap
The prior conversion fplus(H)=(3/2)H+9H² is exactly Q(3/2,1/2). The swapped conversion fswap(H)=(53/2)H-33H² is Q(-1/6,5/6). Therefore fswap has six positive off-diagonal entries1/6 and fails the nonnegative-conductance graph requirement. This does NOT show instability or failure of energy passivity: fswap is still positive semidefinite with eigenlevels0,5,3. It is excluded only from the stated graph model.

If one FIRST requires the target levels3 and5 and THEN imposes nonnegative graph weights, the unswapped assignment is selected. This is a conditional inverse match. It does not derive the target levels or source conductance ratio before target use. The earlier compatibility construction remains valid in its stated algebraic scope. The nonnegative graph condition is an added branch premise, not a silently recovered native law.

## Fixed mean selects the harmonic restriction conditionally
The source transport has1^T T=1^T, hence its discrete update preserves the observable m=1^T q. The candidate second-order model is q'=v, v'=-Qq. Since1^T Q=0, m'=1^T v and m''=0. Preserving the SAME constant mean along every candidate trajectory is therefore equivalent to1^T v=0 initially and thereafter.

The maximal linear initial-state domain preserving that observable has dimension12-1=11. This supplies a clear selection condition for the prior omitted harmonic momentum, conditional on transferring the original transport's conserved observable. It does not make the second-order law itself a consequence of the first-order Markov update. Harmonic displacement remains allowed. Other physical boundary conditions could change this requirement and would define a new branch.

## State positivity is a separate obstruction
Nonnegative conductances make -Q a Markov generator, but do not make q''=-Qq a Markov process. The admitted11D signed phase space permits q=0 and v=(-1,1,0,0,0,0), with conserved mean and q>=0 initially. Its first coordinate derivative is negative, so q leaves the nonnegative cone immediately. The same boundary test works on a normalized simplex using q supported away from that negative-velocity coordinate. Hence the full signed phase domain does not preserve stochastic state positivity. The existing chain-amplitude model need not require it; stochastic and amplitude readings must remain distinct.

## Standard scalar time-step alternatives also fail, within scope
For L levels3,5 and desired transport levels1/2,1/3, a single exact heat step would require exp(-3t)=1/2,exp(-5t)=1/3, implying2^5=3^3, false. Backward Euler requires step1/3 versus2/5. Crank–Nicolson requires2/9 versus1/5. These are specified order-preserving scalar families; no general functional-calculus or open-system obstruction is asserted. They do not independently select the quadratic interpolation.

## Verification and disposition
verify_selection.py uses exact Fraction arithmetic, computes all ordered-pair orbits, verifies24 unsigned group commutations for each of four graph cases, the two spectral projectors, both interpolation weights, the conservation constraints and scalar-step mismatches. The boundary velocity is an exact positivity counterexample; the immediate exit follows from differentiability, not a finite numerical step. Scientific JSON replay is byte-identical.

AUTO_FREEZE this branch's use of the quadratic interpolation as a source-derived physical law. Preserve its conditional exact realization, readout and metric. No previously frozen theorem is retracted: the prior report already labeled interpolation and phase-domain choices. The present audit conditionally closes the fixed-mean domain requirement and narrows admissible graph assignments; the conductance-selection/source-action gate remains OPEN. Registration remains incomplete CRL-2a; no particle labels, target exposure, action units or empirical score are added.

## Next dependency and stopping rule
A new constitutive derivation or recovered native action must determine the opposite/cross conductance ratio (and physical observable) before using a desired target spectrum. Repeating interpolations, rescaling or basis changes cannot close this dependency. Stop promoting this candidate without that new source evidence. Physical promotion0; external non-constructor review pending. Gap2_FINAL_Finite_Genesis.png remains unavailable and unused; re-upload if it contains relevant source evidence.
