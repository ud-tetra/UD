# UD degree twelve field compatibility

**RESULT — Accept the repaired field construction and character projectors. Reject the claimed automatic period, real orthogonality and revival of the 1146 index plane.** This audit supplies an explicit degree-12 field and tests its projectors against the frozen 600-cell C10 action. Physical promotion remains **0**; development lane, no registry entry; independent review pending.

## Exact field construction

The cubic-residue list in the follow-up is correct: the cubes in F13 are `{0,1,5,8,12}`. Hence `b^3-2` has no root and is irreducible. The quartic `g^4-g^3+g^2-g+1` is also irreducible, since a primitive tenth root has Frobenius orbit length `ord_10(13)=4`.

With b denoting the cubic root and g denoting a primitive tenth root, define

\[
F=\mathbb F_{13}[b,g]/(b^3-2,\;g^4-g^3+g^2-g+1).
\]

The degree-three and degree-four extensions have trivial intersection over F13. Their tensor product is a field of degree twelve, with basis

\[
\{b^r g^s:0\le r<3,\;0\le s<4\}.
\]

This verifies the proposed twelve-coefficient expansion of each field-valued coframe component. It does not assign geometric or spacetime meaning to those coefficients. In particular, the cubic degree is not the dimension of a tetrahedral cell, and the sextic degree is not a derived spacetime dimension.

An explicit one-generator presentation is available. For `t=b+g`, exact multiplication and Frobenius calculation give twelve distinct conjugates. Its irreducible minimal polynomial over F13 is

\[
\begin{aligned}
H(y)={}&y^{12}+10y^{11}+6y^{10}+8y^9+7y^8+3y^7\\
&+5y^6+9y^5+11y^4+8y^3+7y^2+12y+5.
\end{aligned}
\]

Thus `F = F13[t]/H(t)` as well as the two-generator presentation. The supplied implementation uses exact integer coefficients reduced modulo 13, with both polynomial relations enforced. It never treats integer residues modulo 13^12 as this field.

## Subfields and element orders

Let `Phi(z)=z^13`. The fixed subspace of `Phi^d` has F13 dimension d for each divisor d of twelve, as verified on the twelve basis elements:

| d | Fixed field | Degree from F |
|---:|---|---:|
| 1 | F13 | 12 |
| 2 | F_(13^2) | 6 |
| 3 | F_(13^3) | 4 |
| 4 | F_(13^4) | 3 |
| 6 | F_(13^6) | 2 |
| 12 | F | 1 |

The follow-up correctly includes the cubic, quartic and sextic fields, but omits the quadratic subfield. In particular, `F_(13^4) intersect F_(13^6) = F_(13^2)`, while the cubic and quartic intersection is F13.

The notation for the cubic root must stay separate from the prior norm-one element. Exact orders are:

| Element or map | Order | Norm or qualification |
|---|---:|---|
| b, with b^3=2 | 36 | Norm from cubic field to F13 is 2 |
| g, primitive tenth root | 10 | Character scalar |
| eta=(b+b^2)^12 = 7+2b+11b^2 | 183 | Norm from cubic field to F13 is 1 |
| Phi on F | 12 | Field automorphism, not an assigned physical update |
| I3+E12 in SL3(F) | 13 | Counterexample to a universal transition period twelve |

For example, the norm of b is `b^(1+13+169)=b^183=b^3=2`, using its order36. Reusing the symbol beta for both b and eta would equate different objects.

## Projector separation and orthogonality

Let G be the frozen signed C10 generator on the 2640 simplex coordinates. With `10^-1=4` in F13, set

\[
P_m=10^{-1}\sum_{j=0}^9 g^{-mj}G^j,\qquad m=0,\ldots,9.
\]

The certificate checks all one hundred group-algebra products and the identity sum:

\[
P_mP_n=\delta_{mn}P_m,\qquad \sum_mP_m=I.
\]

The actual signed action consists of **264 cycles of length ten**, each with sign product one. A sign change of basis turns each cycle into the regular C10 action. Therefore every projector has rank **264 over F**. Direct sparse integer checks also verify `AG=GA` and `G^T G=I` for the frozen generator A. The finite projectors commute with the reduced A as a consequence.

Here “orthogonal” must be typed. These are mutually annihilating algebraic idempotents. With the ordinary transpose,

\[
P_m^T=P_{-m}.
\]

The bilinear pairing `x^T y` pairs sector m with sector minus m. For m other than zero or five, the pairing within sector m vanishes identically. Thus ten separate character spaces are not ten positive Euclidean-orthogonal real spaces.

A valid additional structure is a finite-field Hermitian form. Define `sigma=Phi^6`; it fixes the sextic subfield and sends g to g inverse. For `X^dagger=sigma(X)^T`, the certificate verifies

\[
P_m^\dagger=P_m.
\]

The sectors are consequently orthogonal for `h(x,y)=sigma(x)^T y`. This form is not a positive real norm; even the nonzero base-field vector `(5,1)` has `h(x,x)=0` in characteristic thirteen. This Hermitian construction is a specified algebraic choice, not a physical metric bridge.

## Field splitting does not separate our readout

The field repair diagonalizes the cyclic action. It does not change what R measures. In both the original 62-channel observer and the augmented 189-channel observer, coordinate **0 is unobserved**, but G sends it to the **observed coordinate44** with positive sign. Consequently

\[
R e_0=0,\qquad R G e_0=R e_{44}\ne0.
\]

No output operator `G_out` can therefore satisfy `R G=G_out R` for either instantaneous observer. This exact witness works over the reals and over the repaired finite field. **Character splitting does not repair snapshot observation equivariance or justify summing sectorwise observation ranks.** The augmented full-history observer still has kernel zero in its frozen real model; snapshot equivariance and full-history identifiability are different properties.

The earlier real results remain scoped to their frozen models: original history rank 1893 and kernel 747; augmented history rank 2640 and kernel 0. Their values have not been rederived over characteristic thirteen here. Nor does this audit enlarge the declared fault family of the 260-preparation validation protocol or transfer its real conditioning bounds to a finite field.

## Claims still rejected or open

**NO-GO — inferring the Pachner period from Frobenius.** `Phi^12=I` is exact. For a specific transition T, `T^12=I` is a separate matrix identity. An element with order 13 exists in the same field's SL3, and g, b and eta have orders 10, 36 and 183. A semilinear transition `T=M Phi` has twelfth power equal to the ordered twisted product `M Phi(M) ... Phi^11(M)`, which need not be I. A topology-changing transition may not even be a square matrix on one fixed carrier.

**NO-GO — restoring the 1146 index plane.** That plane was never defined by a valid index theorem. Correcting coefficient arithmetic does not turn `1893-747` into the Fredholm index of the square Gram operator. The earlier index objection remains.

**NO-GO — curing rank or invertibility by extension.** The earlier base-field Omega remains singular over F; extending a field does not change a fixed matrix's rank. The constraint `K K^dagger=2I3` is still impossible for a 3-by-2 K over any field. These operators need redesign rather than a larger coefficient domain.

**OPEN — curvature, transport and physical meaning.** The scalar2 is fixed by all Frobenius automorphisms. That elementary fact supplies no curvature equation, Borel stability proof, positive real metric, continuous gauge group or physical clock. Each requires a source-defined operator and compatibility proof. The proposed governance amendment remains a proposal; this development calculation makes no promotion claim.

The immediate useful next step is to specify one corrected transport matrix and test invertibility, its stated form-preservation identity, its actual order and its observation-intertwiner defect. The field and projector layer is now concrete enough to perform those tests.
