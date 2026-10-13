# Record entropy, conditional area law and normalization obstruction

2026-10-12, America/Chicago. Benjamin Walker Mayes, AI-assisted development. Development — no registry entry. Physical promotion 0; independent review OPEN.

## Result

An explicit finite-carrier state and coarse-graining give a well-defined information entropy. They do not establish irreversible entropy production, a universal horizon-area law, or a unique physical area normalization. A declared many-record boundary extension yields an exact conditional area law with normalization k_B h(q)/a0, without any G input. Counterexamples and scale freedom show which assumptions cannot be omitted.

These are mathematical development results. The record channel, probability interpretation and many-record boundary extension below are declared candidates, not newly claimed native physical dynamics. The microscopic carrier and incidence algebra are UD's filled-tetrahedron substrate. Equal terminology in an external “Unified Dynamics” paper does not establish source identity.

## 1. State and coarse-graining declared explicitly

Take the filled tetrahedron with chain register

H_K=C0⊕C1⊕C2⊕C3, dim=(4+6+4+1)=15,

with unit inner product for this example. The complex Hilbert envelope is a mathematical density-matrix representation of the normalized carrier; the real native carrier is included. Let b=c/||c|| and rho=|b><b|. For a positive metric H the analogous normalized vector is H^(1/2)c/||H^(1/2)c||; a metric must be specified before using this expression.

Declare orthogonal chain-degree projectors Pj and the coarse record channel

C(rho)=sum_j Tr(Pj rho)|j><j|,

where j=0,1,2,3 labels a **classical** record. It can be represented by the isometry V=sum_j Pj⊗|j> followed by tracing out the carrier. The probabilities are p_j=||Pj b||², and the coarse record entropy is

S_snap(rho;C)=−k_B sum_j p_j ln p_j.

This functional uses the standard statistical information-entropy convention. It is the entropy of the declared record state, not an independently derived thermodynamic entropy of spacetime. The isometry does not itself imply dissipation: the joint carrier/record state can remain pure. Physically irreversible storage, decoherence or exported entropy requires a source mechanism.

For the same carrier state, a different coarse-graining generally gives a different entropy. Therefore neither carrier support ||c||² nor its conservation determines S_rec without the channel and state statistics. The source ledger also distinguishes micro and coarse functionals; no such equality is introduced here.

## 2. Exact native counterexample to “entropy accumulation”

Let D be oriented incidence lowering the chain degree and B=D^T−D. The checker constructs all fifteen oriented simplices, verifies D²=0 and B^T=−B, and chooses the unit top-cell vector e. Direct calculation gives B²e=−4e and ||Be/2||=1, with Be/2 entirely in the face sector. Thus the exact native solution is

b(u)=cos(2u)e+sin(2u)Be/2.

Here u is the declared dimensionless evolution parameter, not calibrated proper time. Degree probabilities are p3=cos²(2u), p2=sin²(2u), p0=p1=0. Consequently

S_snap(u)=k_B h(sin²(2u)),
h(q)=−q ln q−(1−q)ln(1−q).

| u | Degree-record entropy |
|---|---|
| 0 | 0 |
| pi/8 | k_B ln 2 |
| pi/4 | 0 |

This is a source-bound reversible example. Hence S_snap is not a monotone “entropy generated per update.” At u=pi/4, all four face coordinates have equal squared weight. The degree record has entropy zero while the simplex-coordinate record has entropy k_B ln 4. The same state does not have a channel-independent record entropy.

For classical records retained as a growing history, define instead

S_hist(n)=k_B H(R1,...,Rn).

If old records are retained and the distributions have consistent prefixes, the chain rule gives

S_hist(n)−S_hist(n−1)=k_B H(Rn|R1,...,Rn−1)≥0.

That monotonicity belongs to the declared retained classical history. It is not a theorem about the closed native carrier, thermodynamic entropy production, or a resettable memory. Snapshot entropy and retained-history entropy must not be interchanged.

## 3. Single-register area-growth obstruction

For any orthogonal projective partition into m nonzero blocks in a d-dimensional register,

S_snap≤k_B ln m≤k_B ln d.

This follows from the nonnegative classical relative entropy to the uniform m-outcome distribution. For a single filled tetrahedron the degree channel has bound k_B ln 4 and full-coordinate pinching has bound k_B ln 15.

If a sequence of meshes uses one such normalized single register with d=O(L^3) and a boundary area A proportional to L², then S_snap/A≤O(ln L/L²)→0. A positive extensive area coefficient does not follow from this single-register representation. This obstruction is scoped to the stated orthogonal record channel; general instruments can introduce extra apparatus randomness, and a many-body/record-history state space is a separate extension.

In particular, C0⊕C1⊕C2⊕C3 is a direct sum. It is not a tensor product of independent thermodynamic cells. Turning a count of simplices into independent record bits is an additional state-space and dynamics assumption.

## 4. A conditional boundary-area theorem with no G input

Declare a boundary Gamma tiled by N patches, each of independently supplied physical area a0. Extend the model to N classical binary record slots, with joint distribution

p_Gamma(r1,...,rN)=product_i q^(ri)(1−q)^(1−ri), 0≤q≤1.

A micro-to-record rule is the marginal over unobserved variables: a micro-distribution p(r,b)=p_Gamma(r)p(b|r) is mapped to p_Gamma by summing b. The discarded conditional bulk state is arbitrary. This defines a coarse-graining; it does not prove the native carrier prepares that microstate.

The record density matrix is diagonal in the N-bit record basis. Tensor-product eigenvalues give exactly

S_Gamma=k_B N h(q), A_Gamma=N a0,

and therefore

S_Gamma=eta_phys A_Gamma,
eta_phys=k_B h(q)/a0.

At fixed q,a0, a discrete patch variation obeys Delta S=eta_phys Delta A. If these patches are independently shown to represent a local horizon cross-section, this becomes a conditional discretized horizon-area law. The horizon identification, continuum/local-equilibrium limit and local constancy of eta are not proved by counting boundary slots.

For a fair binary record q=1/2, eta_phys=k_B ln 2/a0. If the boundary patches are equilateral triangular faces with an independently given side length ell,

a0=sqrt(3) ell²/4,
eta_phys=4 k_B ln 2/(sqrt(3) ell²).

This is a derived coefficient for the **declared** state and metric convention. No G or Planck length entered. Neither ell nor q has been selected by the present native source, so this is a parameterized normalization, not a universal numerical constant.

## 5. Correlations and history defeat an unconditional law

For an arbitrary joint classical boundary distribution,

H(R1,...,RN)=sum_i H(Ri)−TC_N,

where TC_N=D(p_joint||product_i p_i)≥0 is total correlation. If the marginals all have entropy h(q),

S_Gamma=k_B[N h(q)−TC_N].

All N marginal records may be individually fair while the joint distribution puts probability 1/2 on all zeros and 1/2 on all ones. Then S_Gamma=k_B ln 2 for every N, whereas independent fair records give N k_B ln 2. The same marginal occupancy and patch area do not fix an area entropy density.

A weaker asymptotic theorem is available if an independently derived conditional entropy rate h_* exists: if H(Ri|R1,...,Ri−1)→h_* and A=N a0, the chain rule and Cesaro averaging imply S_Gamma/A→k_B h_*/a0. Finite correlation length alone does not set h_*=ln 2 or make total correlation subleading.

Accumulated records also need not be a function of instantaneous area. A fixed-area memory supplied with n fresh independent fair classical records has S_hist=n k_B ln 2. Thus identifying retained-history accumulation with horizon entropy requires a capacity, export/reset, occupancy or redundancy law that relates the retained state to the current area.

## 6. Physical normalization is not identifiable from these inputs

There are two independent freedoms.

Population freedom: q=1/2 yields h=ln 2, while q=1/4 yields h=2 ln 2−(3/4)ln 3. Both are allowed declared binary record states on the same patches and have different entropy densities. The difference is positive because 27>16. A source-selected equilibrium distribution is needed to choose one.

Scale freedom: rescaling the embedding ell→s ell leaves this dimensionless carrier, record channel and probability distribution unchanged, but a0→s²a0 and eta_phys→eta_phys/s². Thus incidence, simplex counts and dimensionless state probabilities do not determine entropy per square metre. An independent metric/length normalization is necessary.

If the other Jacobson bridge assumptions were also established, the candidate effective coupling would be

G_eff=k_B c³/(4 hbar eta_phys)=c³a0/(4 hbar h_*).

This would predict a coupling from independent source inputs rather than use measured G to choose eta. Here those inputs remain unclosed. Setting a0=4 ell_P² ln 2 with ell_P²=G hbar/c³ would insert G and is explicitly not done.

## 7. Exact source audit and name collision

The external manuscript read from Library is Harold D. Kirk III's *Unified Dynamics from Time Generation: Schrödinger, Yang–Mills, and Einstein as Regimes of Generative Contraction*, DOI 10.5281/zenodo.18662525. This is not Benjamin Walker Mayes's tetrahedral programme. In its section 8.1–8.2, equations (43)–(45), the entropy uses a cutoff epsilon=kappa ell_P and imposes c0 N_eff=kappa²/4 by matching the Bekenstein–Hawking value. Those steps do not satisfy the present requirement of independently deriving an entropy normalization without using G. This is a scoped normalization audit, not a verdict on every claim of that manuscript.

An exact source for the previously vague Bochner-flat claim was also located: Kirk's *Unified Dynamics from the Product Flag Manifold Fl_(1,2)(C^3) x CP^1*, version 2.0, DOI 10.5281/zenodo.19302283. Its repository description advertises both Bochner-flat and Jacobson routes. The downloadable PDF could not be read by the web retrieval service, so its full reduction equations are NOT certified here. Bibliographic recovery does not validate the claimed reduction.

Relevant primary references:

- T. Jacobson, *Thermodynamics of Spacetime: The Einstein Equation of State*, Phys. Rev. Lett. 75, 1260–1263 (1995), DOI 10.1103/PhysRevLett.75.1260; arXiv gr-qc/9504004v2. The area law and Clausius relation are hypotheses of that construction.
- C. Eling, R. Guedens, T. Jacobson, *Non-equilibrium Thermodynamics of Spacetime*, Phys. Rev. Lett. 96, 121301 (2006), DOI 10.1103/PhysRevLett.96.121301; arXiv gr-qc/0602001. Entropy-production terms are explicitly retained.
- R. L. Bryant, *Bochner-Kahler metrics*, J. Amer. Math. Soc. 14, 623–715 (2001); arXiv math/0003099v3. This is a geometric classification/construction source, not a UD-to-Einstein matter reduction.

No exact source is invented for the earlier homepage-only citations. Local carrier/master-action/coherence markdown copies inspected here are placeholders. The attached Mayes v2.2 manuscript contains historical gravitational claims, but its searched text did not supply this record-state/coarse-graining derivation. The current ledger leaves physical action normalization and coarse maps open.

## 8. Bochner-flatness alone: an exact counterexample

Take the Riemannian product S²(+k) x H²(−k), k>0, with its product complex structure. Each factor is a complex curve, so the product is Kahler. In an orthonormal product frame the Ricci eigenvalues are (k,k,−k,−k) and scalar curvature is zero. The four-dimensional Weyl formula gives W=0, hence the Kahler Bochner component also vanishes. Yet Ricci is not lambda*g for any scalar lambda.

The checker verifies every Weyl component for k=1 and the unequal Ricci eigenvalues exactly. Thus Bochner-flat Kahler does not imply an Einstein metric, even before addressing Lorentzian signature. This does not rule out a separately specified sourced reduction; it rules out treating Bochner-flatness alone as that reduction. A full claim needs the reduction map, signature, retained fields, matter action/stress tensor and all reduced equations.

## 9. Disposition and next source gate

EXACT under declared mathematics: record probabilities and entropy; reversible entropy counterexample; conditional product-boundary area coefficient; correlation correction; single-register bound; scale/population nonidentifiability; Bochner-flat non-Einstein counterexample.

CANDIDATE: physical record channel, boundary-only many-record state, equilibrium distribution, metric patch area, horizon identification.

OPEN: native irreversible recording dynamics; source-selected h_* and physical a0; thermodynamic identification of S_rec; local horizon and stress-energy/Unruh/Clausius bridge; normalization agreeing with physical gravity; full flag-manifold reduction.

The next task is to derive a many-record boundary state and its entropy rate from a specific UD interaction plus memory/export rule, and derive its physical patch metric without gravity calibration. Generic topology or a numerical match is insufficient. Registry and website are unchanged; physical promotion remains 0. The unavailable Genesis image was unused.
