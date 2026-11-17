# C06 second-order trimmed Whitney lift on the regular tetrahedron

**EXACT / CONDITIONAL** for the stated space, data, and energy forms. **Physical Promotion = 0.**

## Space and boundary constraints

Use the regular unit tetrahedron and the second-order trimmed Whitney one-form space defined by the span of \(\lambda_k w_{ij}\), where \(w_{ij}=\lambda_i\,d\lambda_j-\lambda_j\,d\lambda_i\), \(i<j\), and \(k\) ranges over the four vertices. This definition fixes the meaning of second order. For each triple of vertices there is a relation \(\lambda_i w_{jk}-\lambda_j w_{ik}+\lambda_k w_{ij}=0\), so the 24 generators have rank at most 20. The exact volume mass Gram has rank 20.

The full tangential trace has rank 20. In the usual boundary description this counts two moments per edge and two per face, for \(6\cdot2+4\cdot2=20\). The face modes are boundary degrees of freedom. There are no cell bubbles with zero full tangential trace in this space on the single tetrahedron. Fixing the complete compatible trace therefore leaves a unique bulk form.

If only the six original oriented edge integrals are fixed, the restriction has rank six and its kernel has dimension 14. These free modes include additional boundary data. This is a weaker boundary condition than prescribing the full trace.

## Exact variational test with prescribed edge integrals

Use \(C\) for the six edge-integral constraints and \(G\) for the coefficient Gram matrix of the chosen volume-averaged quadratic form. On a generator \(\lambda_k w_{ij}\), only edge \(ij\) can contribute an integral, with value \(1/2\) if \(k\) is one of its vertices and zero otherwise. Let \(R\) be a right inverse of \(C\) and let the columns of \(N\) span \(\ker C\). For data \(x\), write the lift as \(Rx+Nz\), and solve
\[
(N^\mathsf T G N)z=-N^\mathsf T G R x.
\]
Each form used here is positive semidefinite, so a feasible stationary lift minimizes the energy. Singular derivative forms can admit several minimizing lifts with the same energy.

The Gram matrices use exact barycentric moments \(\overline{\lambda^\alpha}=3!\prod_i\alpha_i!/(3+|\alpha|)!\) and gradient products \(d\lambda_i\cdot d\lambda_j=2(\delta_{ij}-1/4)\). For the tangential trace rank, restrict each polynomial to a face by setting the omitted coordinate to zero and resolve its two tangent components. The six edge-coefficient data split into cut and cycle spaces of dimension three each. Direct rational elimination gives:

| Minimized form on the unit tetrahedron | Cut eigenvalue | Cycle eigenvalue |
| --- | ---: | ---: |
| Mass \(\overline{\|w\|^2}\) | \(31/560\) | \(1/12\) |
| Curl Dirichlet form \(\overline{\|dw\|^2}\) | \(0\) | \(144/19\) |
| Full gradient Dirichlet form \(\overline{\|\nabla w\|_F^2}\) | \(0\) | \(48/11\) |
| Mass plus curl with coefficient one in unit-side normalization | \(5701/40250\) | \(92399/12030\) |

Pure derivative forms have zero cut energy because a constant field realizes any cut edge data. Their entries are stiffnesses, with different length scaling from mass. The last row tests a particular unit-side normalization of a combined quadratic form; it is not a claim that geometry selects a constitutive weight.

For the mass lift the original lowest-order bulk split was \((1/2,1/5)\). Relaxation lowers both weights; the cut weight falls below the cycle weight. Consequently, this lift neither increases the effective cycle mass toward \(1/2\) nor holds the cut weight at its original value. The unweighted Dirichlet tests are likewise non-scalar. A cell-bubble lift using a larger polynomial space is a different problem.

## Reproduction and scope

[The lowest-order result](https://github.com/ud-tetra/UD-Physics/pull/407) uses the same edge normalization. Its equal-weight soft spectrum \((1/5,2/19)\) uses an averaged Whitney boundary mass penalty. A Euclidean edge residual would instead give \((1/3,1/6)\) at unit side. These are distinct penalty forms.

The accompanying exact replay requires SymPy and was run with version 1.14.0. It constructs the mass, curl, and gradient Grams, proves the trace and restriction ranks by elimination, and verifies each stationary lift and its spectral split. These conclusions apply to the stated trimmed space and constraints.

**Claim boundary footer:** Physical Promotion = 0.
