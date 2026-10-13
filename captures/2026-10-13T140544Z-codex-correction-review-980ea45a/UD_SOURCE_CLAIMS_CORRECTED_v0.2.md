# UD source claims — corrected edition v0.2

**Status:** development — no registry entry. Exact statements are scoped below;
physical promotion **0**; independent review pending.

This edition replaces the four identified claim families in the uploaded
`Pasted text.txt`, together with their immediate mathematical consequences.
The original is preserved byte-for-byte as `sources/PASTED_TEXT_ORIGINAL.txt`.
`RETRACTIONS.json` identifies the affected passages, reasons and replacements.
`SELF_REVIEW.md` and `REVIEW_RECORD.json` document the v0.1-to-v0.2 review.
This edition supersedes v0.1 within its stated correction scope; the original
and v0.1 remain preserved as evidence.
This is not a complete audit or endorsement of the original 2,721-line document.
Missing displayed equations in the pasted export are not reconstructed by guess.

## 1. Carrier and generator — EXACT

The filled tetrahedron is the simplicial complex \(\Delta^3\), not merely the
graph \(K_4\). Its real chain register is
\[
V=C_0\oplus C_1\oplus C_2\oplus C_3,
\qquad \dim V=4+6+4+1=15.
\]
The graph alone has no face or body chain groups unless a filling is specified.
Orient every simplex by increasing vertex order. The boundary maps satisfy
\(B_1B_2=B_2B_3=0\). With the declared unit inner product, use
\[
A=\begin{pmatrix}
0&-B_1&0&0\\
B_1^{\mathsf T}&0&-B_2&0\\
0&B_2^{\mathsf T}&0&-B_3\\
0&0&B_3^{\mathsf T}&0
\end{pmatrix},\qquad A^{\mathsf T}=-A.
\]
Consequently \(U(t)=e^{tA}\) is orthogonal:
\[
\frac{d}{dt}(U^{\mathsf T}U)=U^{\mathsf T}(A^{\mathsf T}+A)U=0,
\qquad U(0)=I.
\]
The self-adjoint real Hodge–Dirac operator with positive adjacent blocks is a
different operator. Its real exponential is not generally orthogonal. On a
complex carrier a self-adjoint Hamiltonian generates a unitary group via
\(e^{-itH}\); this must not be confused with the real native generator above.
The generated single-tetrahedron matrix matches the frozen source operator.
Here \(t\) is an internal evolution parameter. No identification with physical
time or a measured rate is introduced.

## 2. Contraction, loss and receipts — EXACT / SOURCE-BOUND

Let \(T:V\to W\) be a linear contraction between declared Euclidean spaces:
\(T^{\mathsf T}T\preceq I_V\). Retain the signed Gram defect convention
\[
G_T=T^{\mathsf T}T-I_V\preceq0.
\]
The positive retained-support loss is a distinct operator:
\[
L_T=I_V-T^{\mathsf T}T=-G_T\succeq0,
\quad \|x\|^2-\|Tx\|^2=x^{\mathsf T}L_Tx.
\]
Neither the name "defect" nor a positive entry changes these signs. For a general
noncontractive transfer, \(G_T\) need not have either semidefinite sign.

When \(T\) is square and invertible, its polar decomposition is
\(T=VP\), \(P=(T^{\mathsf T}T)^{1/2}\), with \(V\) orthogonal and
\(0\prec P\preceq I\). Then
\[
D_T=-\log P=-\tfrac12\log(T^{\mathsf T}T)\succeq0.
\]
For singular \(T\), the logarithm requires a support restriction or explicit
extended interpretation. A positive operator does not itself establish
physical entropy or irreversible record formation.

For a unit output vector \(u\), a ray projection has unnormalized receipt
\(|u^{\mathsf T}Tx|^2\); its normalized post-transfer fraction is
\(|u^{\mathsf T}Tx|^2/\|Tx\|^2\) when \(Tx\ne0\). If
\(Px=e^{-d}x\), then \(Tx=e^{-d}Vx\). The retained norm scales by
\(e^{-2d}\), but the original projector line is preserved only when \(Vx=\pm x\).
For a nonzero input, preserving the positive signed ray used by real PSR
requires \(Vx=x\). A sign flip preserves a rank-one projector but changes
the oriented, positive projective representative.
The exact two-coordinate counterexample in the replay has retained norm squared
\(1/4\) and zero receipt on the original ray.

These projection formulas are not the UD Projective Support Receipt theorem.
The frozen manuscript v2.3, §6.2, defines real PSR using normalized simplex
supports, forest-relative signs and one root sign per support component. Sign
propagation reconstructs \(c/\sqrt{S_\mu(c)}\). That source-bound reconstruction
does not assert lossless evolution under an unspecified transfer or Pachner loop.

## 3. Reconstruction and dimensional claims — EXACT BOUNDARY / OPEN BRIDGE

If one independently declares a linear map \(M:V\to\mathbb R^4\) of rank four,
then rank–nullity gives \(\dim\ker M=11\). This is a consequence of that
declared target, not a derivation of a four-dimensional world. The kernel is
not automatically a gauge space, extra spatial dimensions or a supergravity
field representation. Such identifications need specified actions, constraints,
representations and intertwining maps. The proposed 11D correspondence is
withdrawn. A map producing four amplitudes also does not by itself produce a
smooth tetrad field with all its components and compatibility conditions.

The precise positive-inner-product obstruction is:
\[
M^{\mathsf T}HM\succeq0\quad\text{whenever }H\succeq0,
\qquad v^{\mathsf T}M^{\mathsf T}HMv=(Mv)^{\mathsf T}H(Mv)\ge0.
\]
Changing the sign of a row cannot produce a negative Gram eigenvalue. If an
invertible coframe \(e\) and \(\eta=\operatorname{diag}(-1,1,1,1)\) are
assumed, then \(g=e^{\mathsf T}\eta e\) has Lorentzian inertia by congruence;
the indefinite form was supplied as input. It was not derived from a positive
Gram form. This finite pullback statement does not rule out a separately derived
hyperbolic propagation cone in an independently specified continuum limit.

No theorem here requires a time direction to be selected from the kernel of a
loss/order commutator. For symmetric \(L\) and skew \(Q\), \([L,Q]\) is
symmetric; it can vanish identically, as for \(L=I\). Its kernel then supplies
no unique time axis. A skew matrix alone does not encode all the requirements
of a causal partial order.

Likewise, \(dM=M\partial\) is not a meaningful ungraded identity:
\(\partial\) lowers chain degree and \(d\) raises form degree. On a smooth
space that has already been declared, a possible compatibility condition uses
cochains, \(\delta^k=B_{k+1}^{\mathsf T}\), and specified maps
\(R^k:C^k\to\Omega^k\) obeying
\(dR^k=R^{k+1}\delta^k\). This is a condition to prove, not a consequence of
a rank-four projection. It does not establish a continuum metric, connection,
Einstein equation or physical gauge field.

## 4. Edge Laplacian — EXACT RECONSTRUCTION

Use the unit-metric full edge Laplacian
\[
L_1=B_1^{\mathsf T}B_1+B_2B_2^{\mathsf T}.
\]
The replay constructs all faces and edges from the listed cells, with sorted
simplex bases and oriented boundaries. The chosen \(K_+\) labeling has common
edge \(01\); the alternative labeling with common edge \(34\) is equivalent
by a vertex relabeling of the whole pair. The table now labels one actual
2↔3 pair: the old shared face is \(234\) and the new interior edge is \(01\).
The two sides have the same six outer triangles. v0.1 listed independently
valid carrier representatives with unequal boundaries; it did not verify a
labeled move between them. Nothing is inferred from a floating-point eigenvalue fit.

| Declared complex | Cells | Edge dimension | Exact edge spectrum |
|---|---|---:|---|
| \(\Delta^3\) | \(0123\) | 6 | \(4^{\times6}\) |
| \(K_-\) | \(0234,1234\) | 9 | \(3^{\times3},5^{\times6}\) |
| \(K_+\) | \(0123,0124,0134\) | 10 | \(2,5^{\times9}\) |

The additional review replay verifies equality of the oriented outer boundary
chains, failure of the old labels as a move pair, and signed-permutation
covariance of the relabeled old operator. It embeds both generators in the
30-dimensional chain register of \(\partial\Delta^4\): their difference has
rank 18 and kernel dimension 12. These are operator-comparison results, not
state-transfer maps or proofs of lossless transitions.

For each matrix, the replay verifies the spectral annihilating polynomial and
exact eigenspace dimensions. \(\ker B_2\) on \(K_+\) has dimension three,
but these cycles are boundaries of the three tetrahedra; this does not identify
them with physical electromagnetic or color fields.

On \(K_+\), \(B_1B_1^{\mathsf T}=5I-J\). The gradient projector is
\(P_{\rm grad}=B_1^{\mathsf T}B_1/5\), of rank four. The orthogonal curl
projector \(I-P_{\rm grad}\) has rank six. All gradient modes have eigenvalue
5; the eigenvalue-2 mode lies in the curl sector, together with five eigenvalue-5
curl modes. These are Hodge subspaces, not established physical polarizations.

The uploaded script's printed matrix is retained separately. It has
\[
\operatorname{tr}H_{\rm printed}=47,\qquad
\operatorname{tr}H_{\rm printed}^2=281.
\]
Its claimed spectrum \(1,2,5^{\times8}\) would instead give traces 43 and 205.
The reconstructed \(K_+\) Laplacian has traces 47 and 229. Thus merely changing
the printed matrix's spectral caption to \(2,5^{\times9}\) would also be wrong.
`CORRECTED_OPERATORS.json` supplies the boundary-derived replacement matrix.

The full edge Laplacian of the filled single tetrahedron has no edge zero modes.
If only \(B_1^{\mathsf T}B_1\) is used, the three zero modes belong to a
different, graph-only operator. None of these eigenvalues has been identified
with a physical mass or energy. The mass-gap multipliers and threshold claims
depending on the erroneous spectrum are withdrawn pending a source-bound bridge.

## 5. Propagation and scattering — CONDITIONAL CONTRACT / OPEN

For the reconstructed \(K_+\) edge matrix,
\[
P_2=(5I-L_1)/3,\qquad P_5=I-P_2,
\qquad e^{-itL_1}=e^{-2it}P_2+e^{-5it}P_5.
\]
This is a mathematically valid complex unitary evolution if \(L_1\) is declared
as its Hamiltonian. It is distinct from the real native \(e^{tA}\) flow. A
2↔3 move changes chain spaces. Specify both transfer maps, dwell dynamics and
norm/phase comparison before claiming a round trip is identity. The inverse
combinatorial move alone proves neither lossless state transfer nor phase retention.

The printed scattering script has a syntactically incomplete dislocation mask.
It is not executable as supplied; it was parsed as data and never executed.
The claimed numerical output is withdrawn. No missing mask or dislocation
layout is invented in this corrected edition.

For an optional coherent transport model, declare a device Hamiltonian, leads,
couplings, disorder ensemble, units and energy before computing transmission.
Eliminating lead amplitudes by a block Schur complement gives
\[
G^r(E)=[(E+i0^+)I-H_C-\Sigma_L^r(E)-\Sigma_R^r(E)]^{-1},
\quad \Sigma_\ell^r=V_{C\ell}g_\ell^rV_{\ell C},
\quad \Gamma_\ell=i(\Sigma_\ell^r-\Sigma_\ell^{r\dagger}).
\]
For the declared noninteracting coherent two-terminal contract use
\(\mathcal T(E)=\operatorname{Tr}(\Gamma_LG^r\Gamma_RG^{r\dagger})\).
The lead self-energies and broadenings must be consistent. This is an imported
transport method, not a derivation of leads, charge or a UD physical Hamiltonian.
See the primary reference in `sources/PRIMARY_REFERENCES.json` for the transmission
and broadening convention. The correction introduces no disorder outcome.

As an independently declared scalar illustration, \(\Gamma_L=\Gamma_R=1\),
\(E=\epsilon\), \(\eta=1/100\) gives the unphysical isolated-resolvent
quantity 10000. Consistent wide-band self-energies \(-i/2\) per lead instead
give \(\mathcal T=10000/10201\), tending to 1 as \(\eta\to0\).
This exact illustration is not the missing UD dislocation experiment.

Neither a finite 10×10 matrix nor this transport formula establishes an Anderson
transition, a Chern invariant or disorder-proof unit transmission. A threshold
\(W\ge3/\pi\) requires an independently specified disorder model, spatial
family, spectral/topological diagnostic and finite-size scaling analysis. No
such threshold is derived here. The Planck-to-macroscopic cascade and numerical
target 238.14 remain unevaluated and unsupported by these passages.

## Verification and use

Run `python verify_source_corrections.py --check` and
`python verify_review.py --check` from this capture to replay the
exact Fraction checks and compare both saved result files. The original source,
attached coefficient ledger, governance proposal, frozen manuscript excerpt
source and native operator file remain immutable evidence. The governance
proposal is not silently adopted; constructor verification is not independent
review. Corrected statements replace the identified passages only. Other source
claims remain unaudited until individually source-bound and checked.
