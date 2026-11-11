# Retained-sector coupling criterion

DERIVED, conditional on a conservative differentiable force law at a declared reference state. This is a tangent-force test, not a physical bath identification.

Let u in R^(3N) be Cartesian displacement from the reference, F0 the full reference force and H=-dF/du its symmetric Hessian. Write F(u)=F0-Hu+O(|u|^2). The equal atomic masses make Euclidean orthogonal projectors compatible with the common scalar mass metric. Let R have orthonormal columns embedding the primitive-periodic vertical translation quotient, P_R=RR^T and P_O=I-P_R.

The homogeneous linearized dynamics leave the retained space invariant iff

    P_O H R=0.

For symmetric H, this is equivalent to [H,P_R]=0, or to both reciprocal cross blocks vanishing. The forward columns H R alone determine P_O H R; constructing or diagonalizing the full3N by3N Hessian is unnecessary for this criterion. They do not determine the omitted self block P_O H P_O, its spectrum or stability. The normalized Frobenius statistic is a coordinate-invariant block norm for the declared subspace, not a decay rate.

The affine system also requires P_O F0=0 to stay inside the reference-centered retained space. If lateral residual forces are nonzero, the reference is not a free3D equilibrium. It cannot be used as a full3D normal-mode vacuum without balancing those forces or re-equilibrating under a specified preparation. A tangent cross block at that reference is still a well-defined derivative.

Let P be the atom-to-primitive-group isometry. With the fixed vertical Helmert quotient Q, R q is the Cartesian vector with z=P Q q and x=y=0. The force-column array C=-dF/dq_primitive_z has shape N by3 byd. The tested columns are C Q. Orthogonal output blocks are:

- z outside im(P): (I-PP^T) C_z Q;
- x/y inside im(P): P^T C_x Q and P^T C_y Q;
- x/y outside im(P): (I-PP^T) C_x Q and (I-PP^T) C_y Q;
- global vertical translation: the constant component of P^T C_z Q, retained as a numerical null diagnostic.

Their squared Frobenius norms add with the retained z block. The full vertical primitive block agrees with the previous constrained Hessian when only force observation is changed; a line-force constraint would otherwise erase the omitted output by construction. Removing that constraint for the derivative is explicitly a released-coordinate model extension. It does not revise the earlier fixed-lateral calculations.

## Conditional translation-symmetry obstruction

For a finite periodic supercell, let T_g be orthogonal atom permutations representing a group of primitive translations. If the reference geometry and force law are translation-equivariant, H T_g=T_g H for every g. The group average Pi=(1/|G|)sum_g T_g is the orthogonal projector onto primitive-periodic coordinates, so H Pi=Pi H. Thus nonprimitive wavevector sectors cannot receive linear harmonic forcing from a primitive-periodic displacement. This statement includes all Cartesian directions in Pi; it does not forbid z-to-in-plane coupling within the same primitive wavevector sector.

The actual relaxed arrays have finite periodicity and force-evaluation error. Tiny measured nonprimitive outputs corroborate the conditional symmetry mechanism; they are not an exact proof of zero at the saved floating-point geometries. Defects, boundaries, nonuniform preparation, symmetry breaking and anharmonic interactions change the premise set. They are not tested by this derivative audit.

## From coupling to a reservoir

If released coordinates y are introduced, the homogeneous blocks have the form

    x'' + H_RR x + H_RO y=0
    y'' + H_OO y + H_OR x=0.

A nonzero H_OR is necessary for this linear coupling route. It is not sufficient for irreversible dissipation. A finite positive conservative H_OO gives reversible memory after elimination. A bath interpretation additionally needs a specified spectrum, state/preparation, boundary or continuum limit and energy/export accounting. No H_OO spectrum, physical loss coefficient or UD-to-material map is inferred here.
