# C06 one-face odd coordinates and alignment certificate v0.40

**EXACT / CONDITIONAL** on regular tetrahedral incidence, Euclidean edge stock and a prepared odd input. **NO-GO** for inferring purity or alignment from three unrestricted face-edge values. **OPEN** for a native vector-valued seam transfer and its actuation. **Physical Promotion = 0.**

## Local rank and normalization

Take the mean-zero ordinary edge space \(X=E\oplus W\) with \(W=T_2\) and \(E\) the trace-free pair-even sector. For a face \(f\), let \(R_f\) read its three ordinary edge values in a fixed shared order. Each face sees exactly one edge of each opposite pair. On \(W\), opposite values are negatives, so \(R_f|_W\) is invertible and \(T_f=\sqrt2 R_f|_W\) is an isometry onto \(\mathbb R^3\). This uses ordinary oriented-copy data in the sense of a shared face ordering, not signed simplicial boundary values. In particular, this is the three-entry restriction already distinguished from a single scalar face sum in v0.23. It commutes with relabelings of the face when its three coordinates are permuted accordingly.

On coherently oriented neighboring cells with their common face order identified, a candidate seam register \(z\in\mathbb R^3\) has the isometric injection
\[
z\longmapsto \frac1{\sqrt2}\bigl(L_1 T_{f,1}^{-1}z,\ -L_2 T_{f,2}^{-1}z\bigr),
\]
where each \(L_i\) is the v0.36 signed-gradient isometry. The relative signs are those of the v0.39 scalar boundary row. The identifications and transfer of three coefficients are extra premises. This construction gives local coordinate capacity and an algebraic loader. It does not derive stock movement or latch authority from scalar face-to-cell incidence.

For comparison, if the seam sees only the three tangential **signed gradient** edges, the restriction has rank two. Their circulation relation is exact. A vertex potential constant on the face and compensated at the apex gives a nonzero gradient invisible on all three face edges. Three face vertex potentials can recover the whole gradient if their common offset relative to the cell-mean-zero convention is also provided. The tangential differences alone do not supply that offset.

## Alignment on certified odd registers

For a donor \(s\) and an aligned-coordinate archive \(d\) in \(W\), both identified with the same face frame, use \(u=R_fs,\ v=R_fd\). Their full squared norms and inner product are \(2\|u\|^2,\ 2\|v\|^2,\ 2u\cdot v\). In particular the unnormalized Gram determinant is
\[
\|s\|^2\|d\|^2-\langle s,d\rangle^2
=4\sum_{i<j}(u_i v_j-u_j v_i)^2 .
\]
The three minors give an exact pre-transfer alignment test (rank at most one, allowing an empty archive). Under the v0.39 common scalar rotation this determinant stays zero. For positive conserved stock and the declared forward first-lobe preparation, an armed downward correlation zero with archive stock exceeding donor stock then certifies zero donor. A one-shot cut at that point and the \(N/2\) readout still depend on the v0.39 switched model. The v0.39 unaligned witness used two noncollinear, coupled registers; the residual did not require an uncoupled donor mode.

## Mixed-sector obstruction and minimum raw supplement

On unrestricted \(X\), the image \(R_f E=\mathbf1_3^\perp\), since the three pair-even values sum to zero. Every zero-sum odd face vector is therefore indistinguishable from a suitable even signal or can be hidden by its negative. For the hidden donor, take \(R_fs=(1,-1,0)\) in \(W\) and add an even carrier with face values \((-1,1,0)\). The observed donor is zero. An archive with \(R_fd=(1,1,1)\) has true odd correlation zero and larger stock. The ideal directed odd guard would have downward slope but donor fraction \(4/(4+6)=2/5\). All six local raw readings coincide with those at a genuine zero-donor state of the same archive, so those readings cannot certify alignment or completion. Even and odd evolution need not share the same preparation; this is a single-time indistinguishability witness.

Any two opposite-edge values from distinct pairs supplement the face readings to five distinct edges. They determine the sixth by the mean-zero condition, so they determine \(P_-s\) and \(P_-d\) register by register. The two **additional** scalar edge samples per unrestricted register are minimal for linear odd recovery: \(\ker R_f|_X\) has dimension two and intersects \(E\) trivially, so any remaining kernel after supplementing must be zero to recover the odd part. These extra samples go outside the face. A source-defined restriction onto odd registers could instead enforce purity before the seam sees them.

## Replay

The adjacent exact replay checks all faces, 729 preparation pairs per face, and all choices of two opposite-edge supplements. It includes the zero-donor ambiguity at \(2/5\) true residual. The equations above prove the statements beyond the bounded checks.
