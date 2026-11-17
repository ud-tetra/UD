# C06 unilateral apex contact v0.29

**EXACT / CONDITIONAL** for the declared symmetric scalar stop. **OPEN** for a native event that switches the three odd channels while preserving the stored state. **Physical Promotion = 0.**

## Apply the plastic stop to the v0.28 action

Choose one aligned nonzero odd pair and restrict the identical hinges to their symmetric angle. The aggregate inertia \(I>0\) is the sum of the three hinge inertias. On the incoming action of v0.28 set \(q=\phi-k f\). Write the carrier and record as \(u=\sqrt{2A}\cos\theta,\ v=\sqrt{2A}\sin\theta\) on the fixed odd direction, with \(A=N/2>0\). The carrier form \(u\,dv\) differs from \(A\,d\theta\) by an exact differential. Then \(f=\sin^2\theta\) and the free Hamiltonian in the offset coordinates is
\[
\mathcal H=\omega A+\frac{p^2}{2I}+V(q).
\]
The offset branch starts at \(q=p=0\) with \(V'(0)=0\). Take the already prescribed gain \(k=2\phi_*\) to grant the proposed trigger every timing advantage. First contact occurs at \(\theta=\pi/4\) on that branch.

A declared unilateral upper stop is \(g=q+k\sin^2\theta-\phi_*\le0\). At impact, hold coordinates \((q,\theta)\) continuous and use the canonical momentum impulse \((\Delta p,\Delta A)=-J(1,k f_\theta)\) with \(J\ge0\). For perfectly plastic contact require \(\dot g^+=0\). At balance \(f_\theta=1\) and \(\dot\theta=\partial_A\mathcal H=\omega\) on both sides, provided \(A^+>0\). Thus
\[
J=Ik\omega,\quad p^+=-Ik\omega,\quad A^+=A^- -Ik^2\omega .
\]
Choose any \(A^->Ik^2\omega\) to stay in the chart. The hinge stops at the instant of impact, while \(\dot f^+=\omega>0\). The oscillator stock changes by \(-2Ik^2\omega\). The modeled energy decreases by \(Ik^2\omega^2/2\), consistent with a plastic stop. The closure fraction is unchanged at impact because it depends on \(\theta\), which is continuous. Even if a contact reaction keeps the hinge at the stop afterwards, it enters the momentum equations, and cannot change \(\dot\theta=\omega\) in this Hamiltonian and contact model.

The benchmark grants a tuned gain and a plastic contact law. It has no native derivation of either. It is a direct counterexample to inferring carrier hold or an identity amplitude reset merely from hinge stop. It does not cover other reciprocal contact laws that change the port or use further phase variables.

## Rank and regularity scope

For a regular positive-definite mass matrix and one independent gap normal \(n\), the plastic velocity correction is the rank-one projection \(M^{-1}n(n^\mathsf TM^{-1}n)^{-1}n^\mathsf T\). It can remove one normal velocity. The C06 target replaces a coupling on three independent odd modes. Interpreting the scalar contact as a direct rank-one correction to that entire port cannot implement the target. A scalar event may still select a separate full-rank constraint law, but that is additional structure.

The continuous-vector-field scope from v0.28 requires only continuity at the event for a continuous full state and smooth fraction. Removing local Lipschitz regularity alone does not allow a positive-to-zero jump of the slope. A continuous sublinear law can instead approach the stop in finite time with slope already tending to zero, as in v0.15. An actual impact changes momenta and must account for stock and energy. The native same-event identity reset and rank-three switching law remain open. Stage 2 remains open.

Run python3 replay_c06_unilateral_contact.py for exact rational impulse, post-impact velocity and stock/energy witnesses. The test uses symbolic closure units through the free positive gain \(k\).
