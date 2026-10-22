# Stationary constrained material preparation

DERIVED conditional construction; imposed smooth classical force model. Physical promotion0.

Let the Cartesian reference be X0 with N equal-mass carbon atoms, d primitive groups, and count r_g atoms per group. Define P_ig=1/sqrt(r_g) for i in group g and zero otherwise. Then P^T P=I. Source groups are ordered by layer, with d/2 groups in each layer.

Let S be the block-diagonal sum of one Helmert complement to the constant vector in each layer, and Q one Helmert complement to the global constant vector. Both are orthonormal. The Cartesian displacement embedding is

    delta X_x=P S q_x
    delta X_y=P S q_y
    delta X_z=P Q q_z.

Each layer's mean lateral displacement is zero. The overall mean vertical displacement is zero. Relative layer height can change, and all internal primitive-periodic displacements in this affine space are admitted. Equal within-layer replication counts are part of the input; the verifier retains group labels/counts. There are2(d-2)+(d-1)=3d-5 coordinates:79 for d28 and151 for d52. This is a specified mechanical preparation, not a native UD carrier dimension.

Writing the flattened embedding as B, B^T B=I. The restricted potential is V(q)=U(X0+Bq), its gradient is -B^T F, and its Hessian is H=B^T H_cart B. Constraints are linear and fixed in time, so no constraint-curvature term is omitted. A stationary constrained configuration satisfies B^T F=0. Individual forces may remain as reactions in forbidden coordinates; zero projected force does not mean every Cartesian force is zero.

At a stationary point, positive H is sufficient for a strict local minimum on this affine coordinate space. Finite central-difference eigenvalues and their step discrepancy are numerical evidence, not a rigorous interval proof. They do not establish a global minimum, uniqueness, full-supercell/Bloch stability, nonlinear long-time behavior or experimental stability.

Split q=(ell,z) into internal lateral and vertical coordinates. The symmetric constrained stiffness has blocks

$$H=\begin{pmatrix}A&C\\C^{T}&K\end{pmatrix}.$$

C nonzero gives vertical/lateral harmonic coupling at a stationary reference. The norm ||C||F/||H[:,z]||F measures the derivative block relative to the full force derivative on vertical inputs; it is not a friction coefficient or energy fraction. If H is positive, A and the Schur complement K-C^T A^-1 C are positive. A finite conservative lateral block can be eliminated into a history kernel but does not, by itself, create irreversible damping. Identifying a reservoir requires a state/preparation, boundary/limit, loss/noise/export prescription and physical clock.

Layer registry here means fixed mean lateral positions within the unchanged box and layer membership. Local atoms can reconstruct and relative displacements can vary within the moire cell. This is not pointwise locking, a maintained external lateral drive or a derived physical contact controller. The nominal zero normal load is the absence of an external normal-force term in the retained source model. The imposed fixed-normal KCz interaction is preserved as written; no claim is made that it captures every relaxation or dissipation mechanism in real graphite.
