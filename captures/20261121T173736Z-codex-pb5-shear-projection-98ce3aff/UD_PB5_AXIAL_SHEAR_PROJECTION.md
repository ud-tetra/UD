# PB5 axial and planar shear under the radial trace projector

**Exact for the declared PB5 coefficient carrier and selected encodings. Physical Promotion = 0.**

Let \(A=\partial-\partial^\mathsf T\), \(S\) read the eleven radial edges, and \(P_{\rm rad}=S^\mathsf T S\). This choice reads each radial edge once and gives the same \(MM^+\) as the repeated radial flags in UD #583. The exact observer \(O=[S;SA]\) has rank 22 and its row space is \(A\)-invariant. Let \(P_K\) be the orthogonal projector onto its 21-dimensional null space.

## Planar pair and axial cycle

Use cyclically oriented equatorial edges \(e_j=[j,j+1]\) with indices modulo five. The replay checks \(P_K e_j=e_j\) for all five edges and shows that every other edge coordinate is killed. Let \(c=\sum_j e_j\). In the signed equator, rotation fixes \(c\), a vertical mirror negates \(c\), and pole exchange fixes \(c\). Rotation fixes only this line. A fully equivariant edge encoding of an axisymmetric shear scalar therefore has zero projected image.

For the directional encoding with a supplied cyclic orientation, the three channels are proportional to the edge vectors with coefficients \(1\), \(\cos(4\pi j/5+2\pi/5)\), and \(\sin(4\pi j/5+2\pi/5)\). They are independent by discrete Fourier orthogonality. Since each lies in the equatorial span, \(P_K\) fixes the entire three-dimensional image. The normalized directional preparation has squared gains \(5/6,5/4,5/4\), from the sums of one, cosine squared, and sine squared around the pentagon and the STF normalization. The fully equivariant signed-potential encoding retains only the two planar directions. Its equatorial differences are injective on the rotation weight-two plane because their kernel consists of constant sequences.

| Axial preparation | Planar image rank | Axial image rank |
| --- | ---: | ---: |
| Fully equivariant signed-edge encoding | 2 | 0 |
| Directional encoding with supplied cyclic orientation | 2 | 1 |

In the directional preparation, a declared axial source written as \(b|z|^2 c/\sqrt6\) passes \(P_K\) with its full amplitude. The supplied orientation is essential to this encoding: \(b|z|^2\) is mirror-even and \(c\) is mirror-odd. Also \(Ac\ne0\), so persistence in the lossless carrier does not imply persistence in the same edge coordinate.

## Fully symmetric forcing on the complete carrier

Build the signed-simplex matrices \(T_r,T_m,T_p\) for equatorial rotation, vertical mirror and pole exchange. They commute with \(A\) and \(P_K\). The exact intersection
\[
 K\cap\ker(T_r-I)\cap\ker(T_m-I)\cap\ker(T_p-I)
   =\operatorname{span}\!\left\{\sum_{v=0}^6[v]\right\}
\]
has dimension one. The spanning vector is harmonic under \(A\). Thus a projected, fully equivariant source proportional to the scalar \(b|z|^2\) can only drive that uniform vertex coordinate. Its coefficient and its interpretation as shear are open. If an added source law preserves the uniform vertex component, the projected scalar source vanishes in that model.

The linear projector establishes survival for a specified source vector. Deriving a native pump coefficient, a nonzero forcing law, or a shear readout requires additional constitutive input.

The adjacent SymPy script reconstructs the carrier, verifies the lossless projection and symmetry actions, and computes the full fixed-space intersection over the rationals.

- [UD #583, radial trace pseudoinverse replay](https://github.com/ud-tetra/UD/pull/583)
- [UD-Physics #456, declared shear encodings](https://github.com/ud-tetra/UD-Physics/pull/456)
