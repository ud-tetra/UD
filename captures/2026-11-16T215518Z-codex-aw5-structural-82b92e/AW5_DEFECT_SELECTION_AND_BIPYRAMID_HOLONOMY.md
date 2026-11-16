# AW5 defect selection and bipyramid compact holonomy

**EXACT_INTERNAL / CONDITIONAL / NO-GO. Physical Promotion = 0.** This follow-up uses the exposure carrier and orientations in the accompanying draft. It records constructor checks. Independent review is open.

## A proposed defect-selection axiom

In the reference fiber, regard a parity assignment as the subset of the three opposite-edge pairs on which it is nonzero. Assume the empty subset remains active, at least one singleton is defective, relabeling preserves defect status, and a disjoint union of two defective subsets is defective. The opposite-edge permutation action is transitive on singletons. Thus all three singletons are defective. Disjoint union first adds all two-element subsets and then the full three-element subset. The seven nonempty subsets exhaust the fiber. Together with the existing reference-fiber rule, this forces the 185-active, seven-defective split. Disjoint union acts as XOR on disjoint supports.

The weight-one alternative passes relabeling but fails the union rule on any two distinct defective singletons. Each substantive premise has content. Without a singleton seed, the weights-two-or-three set is a countermodel even with relabeling and disjoint union closure. Without closure, weight one is a countermodel. Without relabeling, one singleton alone can be closed. The finite closure proof replaces a blanket declaration that every nonzero assignment is defective with explicit hypotheses about elementary defects and their composition. The native distinction dynamics still need to supply the singleton seed, reference-fiber restriction, and disjoint composition rule. The existing common phase result supplies none of these premises.

## A conditional compact connection on the two-cell bipyramid

Take the oriented simplicial complex with tetrahedra 0123 and 0124 glued along face 012. Write $B_1$ and $B_2$ for the signed edge and face boundaries. The spanning tree formed by the four edges from vertex 0 has five chords. Each chord, together with its two tree edges, forms the boundary of a triangle in the complex. These five cycles are an integer basis for $\ker_{\mathbb Z} B_1$, so $H_1(K;\mathbb Z)=0$. Both tetrahedra contract to their common face by a deformation retraction that fixes that face. Every loop in the filled bipyramid is contractible. The shared-face boundary is a nonzero cycle that bounds a face.

Choose compact edge variables $a\in(\mathbb R/\mathbb Z)^9$, in turns, and vertex phases $\chi\in(\mathbb R/\mathbb Z)^5$, acting by $a\mapsto a+B_1^\mathsf{T}\chi$. For an integer edge cycle $z$, its Wilson loop is $W_z(a)=\exp(2\pi i z^\mathsf{T}a)$. Gauge invariance follows from $B_1z=0$. With $f=012$, choose the native integer cycle $x=B_2e_f$ and define the conditional lift

$$
a(t,\chi)=tx+B_1^\mathsf{T}\chi\pmod 1,\qquad t\in\mathbb R/\mathbb Z.
$$

This lift intertwines the declared action by addition of vertex phases. The shared-face holonomy is $W_x(a)=\exp(2\pi i\,3t)$ because $x$ has three unit signed entries. The exact witness $t=1/4$ gives $W_x=-i$. The face turns $B_2^\mathsf{T}a$ include $3/4$ at the shared face in this witness. The oriented face turns around either tetrahedron sum to zero modulo one by $B_2B_3=0$. Compatibility with both top cells therefore coexists with nonzero curvature.

If every face turn vanishes, the integer spanning-tree cycle basis forces every Wilson loop to be trivial. The nontrivial witness measures curvature through a contractible loop. A flat connection with nontrivial holonomy would require different topology or different model assumptions. Compact edge phases, their normalization, and the local vertex action are explicit inputs of the witness. The scalar parameter is a kinematic choice with no fitted value. Deriving compactification and a local gauge transport law from native dynamical variables remains open.

## Verification

The accompanying pure-Python replay enumerates all reference-fiber alternatives, builds signed integral incidence from both carriers, verifies the single-cell paired-sector algebra and checks the bipyramid Wilson phase in exact turns. Its output is preserved as a separate replay artifact.
