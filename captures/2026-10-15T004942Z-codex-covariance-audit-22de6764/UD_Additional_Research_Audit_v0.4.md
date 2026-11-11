# Additional research audit: receipt covariance and twisted phase labels

15 October 2026 UTC. Development - no registry entry. Constructor-checked mathematics; physical promotion 0. No independent review or apparatus execution is claimed. Companion to narrative v0.15.

## Inputs and duplication

Four original DOCX uploads were ingested as source claims, without executing their embedded code. S12 is `1, 2, and 3(12).docx`; S13, S14 and S15 use the corresponding suffixes. Original byte hashes, full main-document XML, paragraph extracts, tables and Office Math XML are preserved. Paragraph anchors are zero-based top-level body paragraphs, counting empty paragraphs. Plain-text equations flatten layout; use the originals or preserved OMML for exact layout.

S12's entire `word/document.xml` is identical to S9, reviewed in the v0.12 package. S13 and S14 have identical main-document XML to each other. These documents have no embedded media, footnotes, endnotes or comments providing additional content. The original ZIP bytes differ and are each preserved, but repeated content is not independent confirmation. The four uploads therefore contain two new distinct document bodies relative to prior ingestion: S13/S14 and S15.

The supplied coefficient ledger v0.39 and CRL2 governance proposal are preserved historical inputs. G05/G06 remain source-open, and development work promotes no physical correspondence. The unavailable `Gap2_FINAL_Finite_Genesis.png` was not used; re-upload it for inclusion. Historical project files outside the declared source scope are not newly validated.

## Claim dispositions

| Source | Claim | Disposition |
|---|---|---|
| S12 P0-186, identical main XML to S9 | Hall quantization, all 144 FO pairs as winding births, order-104 extension | Previously audited conditional network/counting examples and previously corrected errors. No new confirmation. |
| S13/S14 P75-100; S15 P65-91 | Integer tree/chord map and zero held-out residual covariance | Correct for the declared common latent-field observation. Integrate with explicit noise, bias and blind-error qualifications in D.17. |
| S15 P91 | Fourteen columns span the covariance kernel for all PSD training covariances | They are always contained in it; they span the full kernel only for positive definite training covariance. |
| S13/S14 P101-119; S15 P92-121 | Boolean-pair orbit counts and an invariant singlet | Counts correct on Theta under the stated restricted group. Not a quantum singlet, spectral degeneracy, formation law or full-affine invariant. |
| S15 P129-136 | Coprime cohomology splitting and a C13 third-cohomology class | Correct for a declared direct product and trivial U(1) coefficients; proof needs qualification. The factor and physical class are not sourced. |
| S15 P137-142 | H3 proves a protected 3+1-dimensional bulk/Weyl boundary | Unsupported and dimensionally mismatched within the cited bosonic group-cohomology setting. No physical boundary action is supplied. |
| S13/S14 P127-136 | Cyclic cocycle and state sum | Cocycle and normalized flat-edge state sum are standard valid constructions; the alternative direct pairing of integral degree four with a three-cycle is ill-typed. |
| S13/S14 P137-148 | k-dependent rank-169 modular S,T and verified modular identities | Rank is correct for the auxiliary theory; displayed S,T are inconsistent. Exact modular-identity counterexample and repaired formulas below. |
| S13/S14 P156-158 | Componentwise fusion and degeneracy entropy imply area scaling | Nonzero twist changes the fusion group; dimension/degeneracy alone gives no state entropy or horizon-area law. |

The GR/QFT comparison tables state analogies. They do not supply intertwiners, actions, units or observable maps and are not promoted as derivations.

The inherited S12/S9 corrections remain explicit. In the nontrivial order-104 semidirect group, reflection inverts the C13 rotation, so that subgroup is normal but not central. The code's claim G=D4 x C13 is false: the actual center has order2, whereas that direct product has center of order26. The corrected F7 algebra from v0.12 is 4F7 + M2(F7) + 2M2(F(7^6)) + M2(F(7^12)), dimension104; the last 48-dimensional block is missing from the imported expression.

The 144 FO comparisons are Cartesian comparisons, with 36 weight-compatible in the specified F-then-O direction and 72 allowing either ordering in the all-open graph. They do not all identify a ground-to-first winding event. The quadratic increment is kappa*(2n+1), not a constant without the starting-counter assumption. The Hall equations hold for a stipulated cyclic scattering network; neither Weyl chirality alone nor a zero longitudinal drop establishes that network or zero total apparatus dissipation. These are preserved prior repairs, not newly closed native bridges.

## 1. Useful closure: receipt consistency with an honest error model

The Hasse graph has 15 simplex vertices and 28 adjacent-degree containments. The explicitly supplied 14-edge spanning tree yields signless endpoint-sum matrix S; its 14 chords yield H. An alternating odd-length tree path expresses each chord sum as a signed sum of tree sums, so H=C S with integer entries in {-1,0,1}. The independent replay gives ranks S=14, H=C=10 and maximum row l1 norm ||C||_infinity=7. Its exact matrix and tree lists are stored in COVARIANCE_AND_PHASE_CERTIFICATES.json.

For one common latent field z, Y_H-CY_S is identically zero. Gaussianity is unnecessary. This cancels every latent history, including a wrong proposed dynamics or a different state preparation. A generated Gaussian covariance or small floating residual is therefore an internal consistency check, not an empirical prediction test. The source's printed numerical code uses one Wishart matrix; its narrative assertion of a million-sample execution is not substantiated by the supplied code/output and is not adopted.

With actual errors, r=e_H-Ce_S. The full correlated covariance is

\[
R_r=R_{HH}+CR_{SS}C^T-R_{HS}C^T-CR_{SH}.
\]

Independent unit-variance channel errors give I+C C^T, positive definite, rather than zero. A fixed nonzero held-out bias has zero residual covariance but a nonzero residual mean. Every consistent error (u,Cu) is invisible to r; these form a 14-dimensional subspace. Additional evidence must target those directions or a temporal prediction if it is intended to test the latent state or dynamics.

The covariance embedding M Sigma_train M^T is PSD whenever Sigma_train is PSD; its rank equals rank(Sigma_train). The source's fourteen kernel vectors give the whole kernel only when Sigma_train is positive definite. A rank-one Sigma_train instead gives a 27-dimensional covariance kernel. These distinctions, a possible logarithmic product-receipt application and a deterministic error threshold are integrated into D.17. Signless latent coordinates must not silently replace signed carrier amplitudes or the native generator.

## 2. Boolean-pair classifications: correct group, correct objects

On Theta=F2^3 there are 28 unordered distinct-state pairs: twelve same-Hamming-parity and sixteen opposite-parity. Under coordinate permutations S3 the same-parity pairs have four size-three orbits. Adding common complementation gives two size-six orbits; the cross-parity orbit sizes are 6,1,6,3. The matching stabilizer in S4 acts through an order-two quotient on Theta, giving same-parity orbit sizes 1,1,1,1,2,2,2,2 and cross-parity sizes 1,1,1,1,2,2,2,2,2,2. These finite counts are independently checked.

The unordered antipodal set {000,111} is fixed setwise by S3 times complementation. But under the actual full affine closure of D.14 it has an orbit of four antipodal sets: a single-bit translation sends it to {100,011}. “Full symmetry of the pair fiber” cannot mean the 48-element affine group while retaining the one-element orbit. Likewise an invariant set of classical labels is not automatically a quantum singlet or an attracting structure; no interaction operator or preference law follows from orbit size.

The eight Boolean states and the eight fixed-event receipts F(w,parity) are also different objects. Their equal cardinalities do not identify the two actions. An explicit equivariant correspondence is needed before calling these Theta comparisons a classification of the manuscript's FF receipt block.

## 3. Auxiliary cohomology: what is valid and what does not follow

For the declared finite direct product G_aff x C13, with |G_aff|=48 and trivial U(1) action, the positive-degree splitting is valid. A precise route uses H^n(G,U(1))=H^(n+1)(BG,Z) for finite groups and n>=1, then integral Kunneth: positive-degree cohomology factors are finite torsion killed by the group orders, so coprime mixed tensor/Tor terms vanish. This does not hold merely because arbitrary Sylow cohomology equals group cohomology; restriction generally gives a stable subspace, not an unconditional equality. The source's comment making that general inference is too strong.

The 13-primary summand is C13 in degree three. Its inflation into the product is injective because projection to C13 has a section. The claimed 3-primary summand of G_aff is also consistent: use G_aff=C2 x S4, remove the normal V4 after 3-localization, then S3=C3 semidirect C2. Inversion negates the degree-two integral generator and fixes its square in degree four, yielding the C3 invariant summand. This audit does not compute the complete 2-primary cohomology.

These are properties of an appended group and coefficient system. They do not identify a Berry connection, physical twist level, matter rail or Weyl boundary in UD. In the bosonic finite on-site group-cohomology setting, spatial dimension d uses H^(d+1), so a 3+1 spacetime bulk uses H4, while H3 is the 2+1 spacetime construction [P2]. A particular gapless physical boundary additionally needs its Hamiltonian, symmetry action, locality and anomaly map.

## 4. Repair of the cyclic twisted modular data

For the explicitly declared auxiliary cyclic theory, let N=13, k in {0,...,12}, and representatives a,b,x,y in {0,...,12}. Define the standard carry cocycle

\[
\omega_k(a,x,y)=\exp\left(\frac{2\pi i k a}{13}\left\lfloor\frac{x+y}{13}\right\rfloor\right).
\]

Its flux-a slant cocycle is a coboundary, but the trivializing cochain must be retained:

\[
\epsilon_a(x)=\exp(2\pi i kax/169),\quad
\rho_{a,b}(x)=\epsilon_a(x)\exp(2\pi i bx/13).
\]

Direct multiplication reproduces the slant cocycle. Evaluating rho at a gives the twist. With the convention in [P1, Eq. (92)],

\[
\theta_{a,b}=\exp\left[2\pi i\left(\frac{ab}{13}+\frac{ka^2}{169}\right)\right],
\]
\[
S_{(a,b),(c,d)}=\frac1{13}\exp\left[-2\pi i\left(\frac{ad+cb}{13}+\frac{2kac}{169}\right)\right].
\]

In particular theta_(1,0)=exp(2*pi*i*k/169), not the source's exp(2*pi*i*7*k/13). The source discards the twist term in S while changing T. Its asserted (ST)^3=S^2 fails already at k=1. An exact certificate reduces Z[zeta_13,1/13] to F53 via zeta_13 ->16: the (00,00) entry of (ST)^3-S^2 is 6 modulo53. A true complex cyclotomic identity would survive this reduction.

In compatible representative labels the repaired fusion law is

\[
(a,b)\star(c,d)=\left((a+c)\bmod13,
\ b+d+2k\left\lfloor\frac{a+c}{13}\right\rfloor\bmod13\right).
\]

One way to derive the carry is the lattice presentation K=[[0,13],[13,-2k]], where (13,0) equals (0,2k) modulo K Z^2. Its inverse gives the displayed quadratic twist and bilinear phase. For nonzero k this fusion group is C169, while for k=0 it is C13 x C13. All 169 simple labels remain one-dimensional; nontrivial carry is not non-Abelian splitting.

The quadratic twist obeys balancing under this law; the bilinear form is nondegenerate. Character orthogonality gives S unitarity and S^2=charge conjugation. Summing theta first over b leaves only a=0, so (1/13)sum(theta)=1; the usual finite quadratic Fourier calculation gives (ST)^3=S^2 and zero chiral central charge modulo8. The replay checks balancing for every label pair and k, exact cyclotomic Gauss sums, nondegeneracy and a necessary repaired-matrix identity after reduction modulo677. That successful reduction alone is not a proof of the complex identity; the character/Gauss argument supplies it. These are repaired auxiliary calculations, not native UD modular data.

## 5. State sum, boundary claims and entropy

The normalized flat-edge state sum with product of omega on oriented tetrahedra is a valid declared Dijkgraaf-Witten construction. For a connected manifold and abelian group, quotienting vertex gauge choices yields the usual 1/13 sum over fundamental-group homomorphisms. Raw flat edge assignments and that quotient are different sets. The source's alternative expression directly pairs c1 cup c1 in integral degree4 with a three-dimensional fundamental class. This is not defined as written. The isomorphism from H3(U(1)) to H4(Z) does not remove the degree mismatch; a U(1)-valued degree-three representative, or a justified secondary construction, is needed for the phase.

A nonzero cyclic twist does not by itself forbid gapped boundaries of the gauged theory. The pure-charge subgroup {(0,b)} has trivial self/mutual phases, size13, and is its own bilinear annihilator. Boundary constructions for twisted quantum doubles allow the trivial subgroup with trivial restricted cocycle [P3]. This does not assert that a specified ungauged SPT boundary can be gapped preserving a separately imposed physical symmetry; it shows why the imported broad protection claim needs a precise boundary theory and symmetry map. Symmetry-extension constructions also exhibit gapped boundaries in the appropriate higher-dimensional setting [P4].

Torus ground-state degeneracy 169 is a topological Hilbert-space dimension. A pure chosen ground state has zero von Neumann entropy; the maximally mixed state on that subspace has entropy ln169. Selecting a thermal or record state is additional input. Neither number establishes entropy proportional to boundary area, and triangulation refinement can change geometric counts while preserving that topological degeneracy. No horizon-area coefficient, action normalization or G is derived here.

## 6. Integration and next priority

Narrative v0.15 gains D.17 and a short explanation in the reconstruction/uncertainty discussion: receipt consistency, independently acquired noise, covariance rank qualifications and blind-error directions. The group/orbit/topological repairs remain in this companion audit, preserving the manuscript's main argument. The new inputs supply no finite sensor, back-action law, renewal cost or native source selection, so the v0.14 apparatus frontier remains open.

The strongest next theoretical task is still a specified finite acquisition channel with its joint output, back-action and preparation/renewal ledger. Its validation must separate algebraic receipt checks from state/dynamics evidence, and must test mean errors as well as covariance. A corrected optional group model can be explored separately once its relation to the carrier is actually declared.

## Primary references inspected

P1. Yuting Hu, Yidun Wan and Yong-Shi Wu. *Twisted Quantum Double Model of Topological Phases in Two Dimensions*. Phys. Rev. B87,125114 (2013). [arXiv:1211.3695v2](https://arxiv.org/abs/1211.3695v2), §VII.A, Eqs. (89)-(92). Cyclic cocycle, trivializing cochain and twist-dependent modular formulas inspected in the full paper.

P2. Xie Chen, Zheng-Cheng Gu, Zheng-Xin Liu and Xiao-Gang Wen. *Symmetry protected topological orders and the group cohomology of their symmetry group*. Phys. Rev. B87,155114 (2013). [arXiv:1106.4772](https://arxiv.org/abs/1106.4772). Abstract's spatial-dimension classification inspected; no claim of classifying all possible SPT phases outside that setting.

P3. Alex Bullivant, Yuting Hu and Yidun Wan. *Twisted Quantum Double Model of Topological Orders with Boundaries*. Phys. Rev. B96,165138 (2017). [arXiv:1706.03611](https://arxiv.org/abs/1706.03611). Abstract's subgroup/cochain boundary construction inspected; applying the normalized cocycle to the trivial subgroup makes the consistency condition trivial.

P4. Juven Wang, Xiao-Gang Wen and Edward Witten. *Symmetric Gapped Interfaces of SPT and SET States: Systematic Constructions*. Phys. Rev. X8,031048 (2018). [arXiv:1705.06728](https://arxiv.org/abs/1705.06728). Abstract's symmetry-extension and gapped-boundary scope inspected; no unspecified UD boundary is identified with it.

## Reproduction and preserved evidence

Run `python verify_research_batch4.py` with SymPy and NumPy. Twenty-five check families pass. COVARIANCE_AND_PHASE_CERTIFICATES.json stores the exact matrices, path lengths, residual unit-noise covariance and modular-identity failure witness. RESEARCH_BATCH4_CHECKS.json distinguishes finite-field checks from written complex proofs. SOURCE_DOCUMENTS.tar.xz preserves all four original DOCX bytes plus the supplied ledger/governance; extracts preserve every main paragraph, table and Office Math equation. SOURCE_REGISTER.json pins the v0.14 baseline/evidence and duplication hashes. No imported script is executed and no generated trace is called empirical data.

## Manuscript insertion

## D.17 Receipt consistency, covariance and errors it cannot reveal

### D.17.1 The declared signless tree map

The filled tetrahedron has a Hasse graph with 15 simplex vertices and 28 adjacent-degree containment edges. Choose the 14-edge spanning tree and 14 chords specified in the certificate [30]. For a declared latent field $z\in\mathbb R^{15}$, let $S,H\in\{0,1\}^{14\times15}$ map $z$ to endpoint sums on tree and chord edges. These are signless observation matrices, not the signed boundary operator or skew generator.

The graph is bipartite by simplex-degree parity. Let $v$ have value $-1$ on even degrees and $+1$ on odd degrees. Then $Sv=Hv=0$. Connectivity gives $\ker S=\operatorname{span}\{v\}$, so every chord row is in the tree row space. Along its odd-length tree path, alternating the endpoint sums cancels internal vertices and retains the two endpoints. Hence

\[
H=CS,\qquad C\in\{-1,0,1\}^{14\times14}.
\]

For the supplied tree, $\operatorname{rank}S=14$ and $\operatorname{rank}H=\operatorname{rank}C=10$. The longest chord path has seven edges. A different tree can change $C$ and its error amplification. The graph argument is standard incidence/path algebra; the certificate identifies this particular split, not a new general reconstruction method.

A possible magnitude-receipt application requires a separate map. On full nonzero support, if a product receipt is $|J_{ij}|=2|B_{ij}||c_i||c_j|$, define $z_i=\log|c_i|$ and $y_{ij}=\log(|J_{ij}|/(2|B_{ij}|))$. Then $y_{ij}=z_i+z_j$. Zero amplitudes, phase/sign information and calibration require additional treatment. Applying these signless matrices directly to the chain amplitudes instead defines another observable. The null direction $v$ is a measurement gauge: $Av\ne0$ for the native canonical generator, so it is not a harmonic carrier mode.

### D.17.2 What zero residual covariance establishes

For noiseless observations $Y_S=Sz$ and $Y_H=Hz$,

\[
r=Y_H-CY_S=0
\]

holds for every realization, independently of Gaussianity or the dynamics that generated $z$. With finite second moments, $\Sigma_{HH}=C\Sigma_{SS}C^T$ and $\Sigma_{HS}=C\Sigma_{SS}$. If $M=(I;C)$, any positive semidefinite supplied training covariance produces

\[
\Sigma_{28}=M\Sigma_{SS}M^T\succeq0,
\quad \operatorname{rank}\Sigma_{28}=\operatorname{rank}\Sigma_{SS}.
\]

The equality of ranks follows because $M$ has the left inverse selecting its first 14 rows. The 14 independent columns of $(-C^T;I)$ lie in the covariance kernel. They span the entire kernel only when $\Sigma_{SS}$ is positive definite; otherwise the kernel is larger.

Thus zero residual from the same generated latent field confirms the enforced observation identity. It does not independently validate the carrier evolution, a source law or a physical prediction. Any alternative latent history passed through the same matrices satisfies it too. A covariance propagation identity is not an empirical held-out success.

### D.17.3 A residual error contract and its blind subspace

Now declare independently acquired channels with errors, allowing arbitrary correlations:

\[
\widetilde Y_S=Sz+e_S,\qquad\widetilde Y_H=Hz+e_H,
\qquad r=e_H-Ce_S.
\]

Writing $R_{ij}=\operatorname{Cov}(e_i,e_j)$, finite second moments give

\[
\operatorname{Cov}(r)=R_{HH}+CR_{SS}C^T-R_{HS}C^T-CR_{SH}.
\]

The cancellation of $z$ is pointwise, so this formula does not require the errors to be independent of $z$. For zero-mean independent equal-variance errors across all 28 channels it becomes $\sigma^2(I+CC^T)$, positive definite when $\sigma>0$. For componentwise error bounds,

\[
\|r\|_\infty\le\varepsilon_H+7\varepsilon_S
\]

on this tree. The row-specific coefficient is its path length, ranging from three to seven here. These are supplied noise contracts, not a derived sensor law. The residual mean must also be tested: a constant nonzero $e_H=b$, $e_S=0$ has zero covariance but residual $b$.

Finally set $L=(-C,I)$. Its full blind error subspace is

\[
\ker L=\{(u,Cu):u\in\mathbb R^{14}\},\qquad\dim\ker L=14.
\]

Such errors change both blocks consistently and produce zero residual. Since $S$ is surjective, each is the observation of some latent-field perturbation. Additional roots or stock references can resolve aspects of the measurement gauge, but a dynamics test still needs a specified temporal prediction or other independent observable. The residual can detect failures of the declared receipt consistency relation; passing it cannot establish that all state estimates, event sources or physics are correct. This distinction qualifies how the sampled receipts of D.16 can be audited without claiming unearned predictive validation.
