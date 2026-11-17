# UD C06 local matching exchange v0.6

**Status:** EXACT / CONDITIONAL for the declared exchange maps. NO-GO for persistent equal response in this constant-coupling model. CANDIDATE (agile) for a finite two-stage update. Physical Promotion = 0.

**Inputs.** [C06 evidence through v0.5](https://github.com/ud-tetra/UD/pull/527), [Paper I v1.1.1, §5.1](https://unified-dynamics-public.ben-w-mayes.chatgpt.site/sources/repo-03-UD_PAPER_I_REVIEW_DRAFT_v1.1.1.md), [Paper III v1.1.1, §9](https://unified-dynamics-public.ben-w-mayes.chatgpt.site/sources/repo-00-UD_PAPER_III_REVIEW_DRAFT_v1.1.1.md), [Coefficient Ledger, C05–C06](https://unified-dynamics-public.ben-w-mayes.chatgpt.site/sources/ledger-recovery-v0.1/library_LEDGER_v0.85.json). There are separate Whitney investigations in [Discovery #404](https://github.com/ud-tetra/UD-Physics/pull/404) and [#405](https://github.com/ud-tetra/UD-Physics/pull/405). Their calculations are outside this test.

## State and interaction

Let U be the three-by-six normalized opposite-pair sum map. Write P = U*U, so P is a projector and UU* = I. Use Euclidean source x and direct record y in R^6 and matching record z in R^3. Prepare (x0,0,0) on a regular filled tetrahedron. The input x0 is the stripped polarized edge current from v0.4, with squared pair-even and pair-odd norms of ||Q_E||²/2 and ||Q_T2||². Parameters a,b are real internal rates. The evolution parameter t is dimensionless. The readout is ||y||²+||z||². All ports are closed.

```math
\dot x=-ay-bU^*z,\qquad \dot y=ax,\qquad \dot z=bUx.
```

The generator is skew, conserving ||x||²+||y||²+||z||². It decomposes into independent opposite-pair blocks and commutes with tetrahedral relabeling. Opposite edges have no shared vertex. The block interaction assumes locality in the matching relation and includes an additional matching record.

## Exact continuous response

Write R = (aI,bU) vertically. The source oscillator is x'' = -R*R x with x'(0)=0. Since R*R = a²I+b²P, the recorded squared gains are

```math
\mu_+(t)=\sin^2(\sqrt{a^2+b^2}\,t),\qquad
\mu_-(t)=\sin^2(|a|t).
```

A sector with zero coupling contributes zero. Where the odd gain is positive, the ratio tends to (a²+b²)/a² as t tends to zero. Thus |a|=|b|>0 gives 2:1 in the leading transfer. At unit rates the Q-space contrast is (1/2)sin²(√2 t) − sin²(t) = −t⁴/3 + O(t⁶). More generally, there is no open time interval with positive exact equalization in this constant-rate model. Analyticity would make equality an identity. Its quadratic coefficients force a²+b²=2a² and its quartic coefficients then disagree for a≠0. For a=0 the odd sector never records. The full readout that includes the retained source has unit gain on both edge sectors by conservation.

## Exact finite-step candidate

Stage one applies the same balanced orthogonal exchange to every direct edge port. This leaves x=x0/√2 and y=x0/√2. Stage two swaps the retained pair-even amplitude into z, leaving its orthogonal complement in x. On source-only inputs the final map is

```math
x_0\longmapsto ((I-P)x_0/\sqrt2,\; x_0/\sqrt2,\; Ux_0/\sqrt2).
```

The three Gram contributions sum to I, and the two record contributions sum to (I+P)/2. Thus the records alone give positive equal Q-space weights 1/2 in all five directions. If the direct stage partitions a fraction f of squared source amplitude and the matching stage still fully transfers pair-even residual, the record gains are 1 and f. The balanced fraction f=1/2 is exactly the condition required for equalization. These stages are norm-preserving and fixed once declared. The split, ordering, access to the matching channel and stopping point are candidate assumptions. A native UD rule that supplies them and a separate deficit-allocation law remain open.

## Verification

The constructor replay independently assembles the opposite-pair projector, exact generator and record map, verifies skewness and the local sector Taylor coefficients through order four, and checks the two-stage norm and gain identities. The equal-response criterion and prior C06 ratio were already known. No measured value enters.
