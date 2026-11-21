# PB5 quaternion rim flux and relative holonomy

**Exact for the specified \(Q_8\) link model. Physical Promotion = 0.**

On each oriented PB5 edge, take a reciprocal \(Q_8=\{\pm1,\pm i,\pm j,\pm k\}\) link, with \(U_{ba}=U_{ab}^{-1}\). A vertex gauge transform sends \(U_{ab}\) to \(g_aU_{ab}g_b^{-1}\). Use the group product in written traversal order. For a loop based at \(a\), the product transforms by conjugation by \(g_a\).

## The rim-only obstruction

Vertical reflection reverses the equatorial loop based at vertex 0. A gauge-invariant measurement of this loop alone depends only on the conjugacy class \([W]\). There are five classes: \(\{1\}\), \(\{-1\}\), and \(\{\pm i\},\{\pm j\},\{\pm k\}\). Each class is preserved by inversion. For example \(jij^{-1}=-i=i^{-1}\). Thus a noncentral \(W\) can differ from its inverse as a group element while giving exactly the same gauge-invariant rim data. This rules out a mirror-odd orientation selector from this one loop, including every character of \(Q_8\).

In particular, the order-four rim sector has a mirror-symmetric realization up to gauge. Set every positive-traversal rim link to \(i\), and all remaining links to \(1\). The rim product is \(i^5=i\). Vertical reflection inverts each rim link, and a uniform gauge conjugation by \(j\) restores the assignment. Pole exchange already fixes it. The claim concerns this group and this observable. Noncommutativity alone does not establish which conjugacy classes a general group allows.

## A mirror-odd comparison on the full connection

Let \(\chi(q)=\operatorname{tr}\rho(q)/2\) for the two-dimensional quaternionic representation in \(SU(2)\). Thus \(\chi(\pm1)=\pm1\) and \(\chi(\pm i)=\chi(\pm j)=\chi(\pm k)=0\). At rim vertex \(a\), let \(W_a\) be the positive-traversal rim holonomy and let \(V_{a,\delta,p}\) be the triangular holonomy of \((a,a+\delta,p,a)\), for \(\delta=\pm1\) and \(p\in\{5,6\}\). Rim indices are modulo five. Define
\[
 t_a=\tfrac14\sum_{\delta,p}\chi(V_{a,\delta,p}),\qquad
 d_a=\tfrac14\sum_{\delta,p}\{\chi(W_a V_{a,\delta,p})-
                       \chi(W_a^{-1} V_{a,\delta,p})\},\qquad
 \Xi=\sum_{a=0}^{4}t_a d_a.
\]
The two factors in each mixed trace share the same basepoint. Their simultaneous conjugation leaves the trace invariant. Rotations permute the five basepoints, and pole exchange permutes the two pole choices. Vertical reflection permutes the reference triangles, reverses \(W_a\), and therefore negates \(\Xi\). The weight \(t_a\) is mirror-even.

An explicit example has \(U_{01}=i\), \(U_{25}=U_{26}=j\), and all other increasing-edge links equal to \(1\). The two poles are exchanged exactly by symmetry. The rim loop based at 0 gives \(i\), while the triangle \((1,2,5,1)\) gives \(j\), so the loop data generate \(Q_8\). Here \(\Xi=-1/2\) and its mirror gives \(+1/2\). Therefore these two full connections are gauge-inequivalent. The exact replay verifies the example, the 512 simultaneous conjugation controls, and the 56 one-vertex gauge switches that generate the gauge action.

This example witnesses mirror breaking in **supplied joint holonomy data**. The fixed orientation of the rim in the formula defines the sign convention for \(\Xi\). Reversing that convention also negates the signed equatorial cycle \(c\), so the vector \(\Xi c\) is convention-independent. A candidate term \(b|z|^2\Xi c\) has the appropriate mirror parity and lies in the previously established lossless equatorial edge space. Its coefficient and the production of a nonzero \(\Xi\) remain constitutive. A deterministic equivariant update defined on gauge classes keeps an exactly mirror-fixed initial class in the mirror-fixed set. The construction supplies no autonomous symmetry breaking or physical shear mechanism.

- [UD #585, inversion-even \(\mathbb Z_2\) control](https://github.com/ud-tetra/UD/pull/585)
- [UD #584, PB5 signed equatorial edge projection](https://github.com/ud-tetra/UD/pull/584)
- [Trinity College Dublin, quaternionic character table](https://www.maths.tcd.ie/~mascotn/teaching/2025/MAU34104/Sol4.pdf)
