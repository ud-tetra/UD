# PB5 radial-sink memory decay

**Conditional finite-carrier result. Physical Promotion = 0.**  
[CYCLE-088 planning issue](https://github.com/ud-tetra/UD/issues/592) · [Pinned radial sink, UD #583](https://github.com/ud-tetra/UD/pull/583)

## Model

Use the 43-dimensional oriented PB5 chain carrier with tetrahedra \([i,i+1,5,6]\) for \(i=0,\dots,4\), cyclic in the equator. Let \(A=\partial-\partial^\mathsf T\) in the unit coefficient metric. Resolve the span of the five cell vertex averages. The \(i\)-th column of \(U\) is the indicator of its four vertices and zero on all higher simplices. Rescaling each column by \(1/2\) gives the normalized vertex averages and leaves their span unchanged. The Gram matrix \(J=U^\mathsf TU\) is invertible. Let \(E=UJ^{-1/2}\), \(Q=I-EE^\mathsf T\).

Take \(R\) to select the eleven distinct radial edges (the spine and ten pole-to-equator edges). The declared sink \(D=R^\mathsf TR\) is the same orthogonal image projector as \(MM^+\) on the fifteen copied radial edge flags in #583. Turn off all exterior loss. Write \(L_0=QAQ\), \(L_\gamma=L_0-\gamma D\) restricted to \(\operatorname{im}Q\), and \(F=QAE\). Since \(DE=0\) and \(A^\mathsf T=-A\),
\[
 K_\gamma(t)=-F^\mathsf T e^{t L_\gamma}F.
\]
The norm reported here is the unscaled Frobenius norm in an orthonormal resolved basis.

## Exact asymptotic check

Find the largest \(L_0\)-invariant subspace \(N\) of \(\operatorname{im}Q\cap\ker R\). The rational observation rows start with \([R;U^\mathsf T]\) and close under right multiplication by \(L_0\) at cumulative ranks \(16,27,31,31\). Thus \(\dim N=12\). Its characteristic polynomial is
\[
 (z^2+2)^2(z^4+9z^2+19)^2 .
\]
The exact replay gives \(N^\mathsf T QAU=0\), where the left factor denotes any basis matrix of that subspace transposed. These undamped modes carry zero input–output residue in the selected memory kernel.

Since \(L_0\) is skew and the positive-semidefinite sink kills \(N\), the orthogonal complement of \(N\) inside \(\operatorname{im}Q\) is invariant under \(L_\gamma\). For \(\gamma>0\) an imaginary eigenvalue there would require \(Dv=0\) by the real part of \(v^\ast L_\gamma v\). Such a \(v\) would also be an \(L_0\) eigenvector in the dark subspace, a contradiction. The 26-dimensional complement is strictly stable and contains \(F\), so
\[
 \lim_{t\to\infty}\Vert K_\gamma(t)\Vert_F=0
 \quad\text{for every }\gamma>0 .
\]
This is a statement about the declared projection and interior radial sink. The 12-dimensional compressed dark sector here is distinct from the 21-dimensional lossless sector of the **uncompressed** #583 generator.

## Zero-sink control and numerical values

The exact initial norm squared is \(4295/49\). At \(\gamma=0\), the compressed generator is finite-dimensional and skew. Simultaneous recurrence of its phases brings the kernel arbitrarily close to its nonzero initial value at arbitrarily late times. Thus the ring does not produce decay in the reversible zero-sink model.

| Carrier time | \(\gamma=0\) | \(\gamma=1\) |
| ---: | ---: | ---: |
| 0 | 9.362321359 | 9.362321359 |
| 5 | 9.332963847 | 1.300267298 |
| 10 | 9.283672910 | 0.211063833 |
| 20 | 9.326894956 | 0.005718985 |
| 40 | 9.277145601 | 0.000116606 |
| 80 | 9.348887556 | 0.000000144 |

The displayed samples illustrate the exact asymptotic distinction. They do not certify a finite settling horizon or an error-controlled Markov approximation. Larger-cluster exterior scaling remains the separate CYCLE-088 benchmark.
