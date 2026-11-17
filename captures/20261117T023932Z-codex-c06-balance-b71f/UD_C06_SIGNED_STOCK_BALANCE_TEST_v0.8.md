# C06 signed stock-balance crossing v0.8

**Status:** EXACT / CONDITIONAL for a measurable two-port exchange. NO-GO for using flux zero as the half-transfer trigger in that exchange, and for using aggregate balance to infer a half transfer in each sector without synchronization. CANDIDATE (agile) as a UD receipt law. Physical Promotion = 0.

**Sources.** [Paper I v1.1.1, §5.1, Proposition T5.1](https://unified-dynamics-public.ben-w-mayes.chatgpt.site/sources/repo-03-UD_PAPER_I_REVIEW_DRAFT_v1.1.1.md) gives signed incidence-current cut balance. [UD #534](https://github.com/ud-tetra/UD/pull/534) and [Discovery #410](https://github.com/ud-tetra/UD-Physics/pull/410) provide v0.7 transfer fractions and binary-receipt underdetermination. The calculation below assumes a closed, isolated exchange between the declared source and direct-record ports. That identification, latch, and measurement are not supplied by the general cut theorem.

**Audit correction.** A complete matching swap gives a squared-gain ratio of 1/f. Thus f=1/5 gives 5:1. The archived 4:1 witness is f=1/4. The binary underdetermination is established by alternative conservative completions with the same receipts. A Boolean rule could assign a real constant once a constitutive interpretation is supplied.

## Exact half-transfer discriminator

Let x and y be real amplitudes in the same finite-dimensional Euclidean space. Use dimensionless time and the norm-preserving equations

```math
\dot x=-\omega(t)y,\qquad \dot y=\omega(t)x,\qquad x(0)=x_0\ne0,\quad y(0)=0.
```

Assume continuous positive rate ω(t)≥ω_min>0, shared by all input components. There are no other fluxes. Set C=||x0||², θ(t)=integral ω(t)dt and f=||y||²/C. The normalized balance B=(||y||²−||x||²)/C equals 2f−1=−cos(2θ). Its first zero is at θ=π/4, with B'=2ω>0 and f=1/2. Thus arbitrary common positive rate variation shifts the crossing time while preserving the fraction exactly.

The signed flux from source to record is J=2ω<x,y>=Cω sin(2θ), so B'=2J/C. At the half split J=Cω>0. The endpoint zeros of J include the initial state and full direct transfer. For constant rate the flux takes the same value at complementary first-quadrant phases, and for variable rate its maximum need not occur at half transfer. An instantaneous unsigned or signed flux zero therefore does not supply the half trigger. With the declared source-only initial condition, its directed integral reaches C/2 at half transfer, by the closed cut balance. A single local incidence current encodes this only when it equals the complete transfer flux of the declared cut.

## Perturbed balance observation

On the phase window π/4±δ with 0<δ<π/4, let the normalized measured balance be B+e, where |e|≤ε<sin(2δ) and |e'|≤κ<2ω_min cos(2δ). Assume e is continuous and differentiable there. The measured endpoints have opposite signs, and its derivative is bounded below by 2ω_min cos(2δ)−κ>0. There is exactly one transversal measured zero in this window. At that zero the true balance obeys |B|≤ε, so |f−1/2|≤ε/2. This is a bracketed guarantee. To identify the first global trigger, the implementation must also exclude prior triggers. A global amplitude bound |e|≤ε on the preceding first-quadrant phase segment suffices because its true balance stays below −sin(2δ) before the bracket. No physical fixture or noise estimate is inferred.

## Sector-specific obstruction

If the positive exchange rates differ between sectors, aggregated balance can hide unequal fractions. Take rate 1 on pair-even E and rate 2 on pair-odd T2, with equal initial edge-stock in the two sectors. At t=π/6 the direct fractions are 1/4 and 3/4, respectively. Aggregate balance crosses zero transversally there since each ideal first-window derivative is positive. Both stocks are exactly conserved sector by sector. Even if the second stage then performs a complete retained-even swap, the record gains are 1 and 3/4, so the shear weights are 1/2 and 3/4. The global guard does not guarantee isotropy. Rates here are a falsifying control for the aggregate rule. A native source must derive shared phase accumulation or a place to read and compare sector-resolved balances, and still source the second-stage depletion guard and deficit allocation.

## Replay scope

Rational checks verify the stock/flux identity at analytic phase controls, the error-margin logic with exact witness bounds, the 1/4 versus 3/4 sector counterexample and the archived 4:1 witness. Trigonometric identities and the derivative bounds above establish the claims beyond the sampled cases. The target half split was already known. No empirical data or fitted coupling enters.
