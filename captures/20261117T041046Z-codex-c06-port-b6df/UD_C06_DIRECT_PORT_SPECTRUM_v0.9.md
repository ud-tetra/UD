# C06 direct-port spectrum v0.9

**Status:** EXACT / CONDITIONAL for the declared regular-cell ports and metrics. NO-GO for deriving the common active rate from face-local equivariance and positivity alone. CANDIDATE (agile) for the independent Euclidean flag port. Physical Promotion = 0.

**Sources.** [Paper I v1.1.1, §4.3, propositions T4.4 and P4.5](https://unified-dynamics-public.ben-w-mayes.chatgpt.site/sources/repo-03-UD_PAPER_I_REVIEW_DRAFT_v1.1.1.md). [Paper III v1.1.1, §9](https://unified-dynamics-public.ben-w-mayes.chatgpt.site/sources/repo-00-UD_PAPER_III_REVIEW_DRAFT_v1.1.1.md). [UD #536](https://github.com/ud-tetra/UD/pull/536) and [Discovery #412](https://github.com/ud-tetra/UD-Physics/pull/412) are the integrated v0.8 latch analysis. The twelve-flag lift is the v0.5 copying construction in [UD #527](https://github.com/ud-tetra/UD/pull/527).

## Port and rate definition

Fix one regular tetrahedral cell. Let X be the mean-zero subspace of the real unordered six-edge current module. Its ordinary permutation representation is E plus T2. Give X the Euclidean edge metric. Define F:X→R^12 by (Fx)_(face,edge)=x_edge on the twelve incident edge–face flags. Put independent direct records y on the flags, and allow each face triple a common symmetric metric. Its diagonal entry is u and its off-diagonal entry is v. The metric on all flags is block diagonal across faces. For a positive metric require u−v>0 and u+2v>0. With F* the adjoint for these specified metrics, take the closed dimensionless evolution x' = −F*y, y'=Fx, with source-only initial input (x0,0). This explicitly declares the extra record space. The total stock ||x||²+||y||_flag² is conserved. Singular values of F give phase rates, while the Gram eigenvalues are squared phase rates.

Each edge has two flags. Every pair of distinct adjacent edges occurs in exactly one common face. Opposite edges share no face. Thus

```math
F^*F=2uI+vA_{\rm adj},\qquad
\omega_E^2=2(u-v),\qquad
\omega_{T_2}^2=2u.
```

The adjacency eigenvalues on E and T2 are −2 and 0 by Paper III §9, or by summing the neighboring opposite-pair totals directly. The nonzero equality of rates occurs exactly at v=0 within this class. Positivity and S4 symmetry admit v≠0. For example u=1 and v=1/2 give squared rates (1,2). This is an equivariant split. For independent unit flag records (u,v)=(1,0), both rates are √2 and the common first half-stock latch is t=π/(4√2). This derives the latch for the declared ports. It does not select the independent metric as native.

## Coherent face readout and canonically signed comparison

Summing the three edge values into one real coordinate per face gives the **unsigned** map H=|B2|^T. Its Gram matrix is 2I+A_adj, so its squared rates on (E,T2) are (0,2). That face output loses E and fails positive common-phase half transfer.

The canonical **signed** simplicial edge module has a different group action. For its signed B2^T port, the squared singular values are 0 on cuts and 4 on cycles. For the joint signed port (B1,B2^T), the Gram is 4I, giving a rate of 2 on all six signed-edge modes. The signed module is T1 plus T2, with no E. Consequently its common rate cannot instantiate the shear E-plus-T2 latch without an independently sourced nonlinear or enlarged interface. These statements use the regular unit incidence convention of P4.5 and do not identify signed cochain modes with unordered current coordinates.

## Audit amendments and source gate

For v0.8, the derivative of B=−cos(2θ) is 2ω sin(2θ). Flux peaks at the half split for constant positive rate. With a variable rate it is positive there and need not peak there. Bounded amplitude error gives the transfer-fraction bound at a detected zero. Uniqueness and transversality in the stated window also use the derivative bound. Unequal rates can coincide at a later half-transfer phase. The degeneracy condition here is for a shared first crossing under constant rates in the declared exchange model.

The native decision is now whether an independent source forces v=0 and produces observable auxiliary flag records. The signed boundary identity alone does not supply a shear E carrier. Stage-two depletion and deficit allocation are separate unresolved dependencies. The equal-rate criterion was known. All fixtures are exact mathematical controls, with no empirical fit.
