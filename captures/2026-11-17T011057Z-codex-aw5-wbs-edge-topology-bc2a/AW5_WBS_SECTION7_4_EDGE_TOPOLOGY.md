### 7.4. AW5 edge-Laplacian topology and flag scope

**EXACT_INTERNAL / STRUCTURAL_FRACTURE. Physical Promotion = 0.**

With increasing vertex orientation and unit simplex weights, $L_1=B_1^\mathsf T B_1+B_2B_2^\mathsf T$. Two incident edges at a vertex $v$ contribute $[v:e][v:e']$ to the divergence term. If their union is a triangle, $B_1B_2=0$ gives the opposite curl term. If their union is absent from the faces, the divergence term survives with magnitude one. Disjoint edges contribute zero to both terms.

In AW5, each of the four hub vertices is incident to three hub edges and three radial edges. Apex $a_i$ belongs to the leaf opposite hub vertex $i$. At a hub vertex $v$, each radial edge $va_i$ with $i\ne v$ forms exactly one unfilled wedge with a hub edge, namely with $vi$. Each pair of the three radial edges also forms an unfilled wedge because the two apexes lack a connecting edge. All hub-hub wedges and all wedges at an apex are filled. The count is $4(3+3)=24$ unordered wedges, giving **48 nonzero off-diagonal entries**. Equivalently there are $4\binom62+4\binom32=72$ incident pairs and $3\cdot16=48$ triangular pairs. The signs depend on edge orientation. For example, with $a_1=5$ the coefficient for $(01,05)$ is $+1$.

The filled 47D and hollow 46D carriers share $B_1$ and $B_2$, so the complete edge matrices coincide. The six hub edges have diagonal six, and the twelve radial edges have diagonal four. Hub excision changes $B_3$ and $b_2$, which explains why this edge matrix cannot witness the cavity. The exterior-shell discrimination in §7.3 uses the face/bulk subsystem.

For the single-cell C06 comparison, the sampling map $S:\mathbb R^6\to\mathbb R^{12}$ has rank six. The symmetric-matrix pullback $M\mapsto S^\mathsf T M S$ is onto: for $LS=I_6$, any symmetric $H$ is the pullback of $L^\mathsf T H L$. Its kernel therefore has dimension $78-21=\mathbf{57}$. This corrects the reported value 66. The flag metric, midpoint gain and defect-to-response allocation remain underdetermined by the tetrahedral edge energy.

[UD-Physics PR #401](https://github.com/ud-tetra/UD-Physics/pull/401) · [Pinned exact derivation](https://github.com/ud-tetra/UD-Physics/blob/2b58b578c47ab84f8de784a2b35501ddf175fc2f/candidates/c06-incidence-interaction-v03/UD_C06_INCIDENCE_INTERACTION_v0.3.md) · [Exact replay manifest](https://github.com/ud-tetra/UD-Physics/blob/2b58b578c47ab84f8de784a2b35501ddf175fc2f/artifacts/20261117-codex-c06-8e71/c06-incidence-replay/manifest.json).

**Claim boundary footer:** Physical Promotion = 0.
