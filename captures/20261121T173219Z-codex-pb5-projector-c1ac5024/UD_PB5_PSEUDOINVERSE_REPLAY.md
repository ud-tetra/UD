# PB5 radial trace and pseudoinverse projector

**Exact for the declared PB5 common-cochain carrier and skew Hodge–Dirac generator. Physical Promotion = 0.**

Use the five tetrahedra \([i,i+1,5,6]\), with the equatorial index taken modulo five and every simplex written in increasing order. The carrier has \(7+16+15+5=43\) simplex coordinates. The five radial faces are \([i,5,6]\). Each face restriction \(R_i\) reads all three oriented edge coordinates separately. Let \(S\) stack these restrictions, \(M=S^\mathsf T\), and \(A=\partial-\partial^\mathsf T\).

The orthogonal radial sink projector \(P=MM^+\) has rank 11. Its image is the coordinate subspace supported on the spine and the ten pole-to-equator edges. The 15 flags repeat the spine coordinate five times. Duplicating all flags for cell-owned traces gives \(M_{\rm copy}=[M\ M]\) with the same column space and the same projector. The exact replay computes the projector with independent columns and the inverse of their Gram matrix.

## Lossless sector

The additive Whitney sink has the form \(D=2 S^\mathsf T W S\) with \(W\) block diagonal and positive definite. Therefore
\[
 \ker D=\ker S=\ker P.
\]
The maximal lossless subspace for either sink in \(\dot x=(A-\gamma D)x\) or \(\dot x=(A-\gamma P)x\), with \(\gamma>0\), is the largest \(A\)-invariant subspace in this common kernel. The ranks of \(S,[S;SA],[S;SA;SA^2]\) are \(11,22,22\). Hence the observation row space closes after \(SA\), and the lossless subspace is exactly \(\ker O\), with \(O=[S;SA]\). Its orthogonal projector is \(I-O^+O\), which has rank 21 and commutes with \(A\). The restricted characteristic polynomial is
\[
 z(z^2+2)^2(z^4+9z^2+19)^4 .
\]
The orthogonal complement has dimension 22. Any purely imaginary eigenvalue there would require a generator eigenvector in the sink kernel, contradicting maximality. The complement therefore decays asymptotically for both positive sink closures. Equality of the kernels and lossless spectra makes no claim about equality of damping rates.

## Face-sum control

If \(M\) instead has one unsigned incidence column per radial face, \(M^\mathsf T\) sums the three edge coordinates in each face. Its image projector has rank 5 and the exact invariant lossless sector has dimension 33. This control distinguishes the observation specified by all edge–face flags from the observation specified by five scalar face sums.

| Sink | Instantaneous sink rank | Invariant lossless dimension |
| --- | ---: | ---: |
| Additive radial Whitney | 11 | 21 |
| Radial trace projector, unique or copied flags | 11 | 21 |
| Unsigned radial face-sum projector | 5 | 33 |

The relative-sign result of the two-cell spin theorem remains separate from this edge-trace calculation. The two-cell unique-simplex carrier is \(5+9+7+2=23\), and its 13,824 frame checks are \(24^3\) tuples of binary tetrahedral elements.

Run `python3 replay_pb5_pseudoinverse.py` with SymPy for the exact replay.

- [Merged two-cell spin transition and incidence projector reference, UD #582](https://github.com/ud-tetra/UD/pull/582)
