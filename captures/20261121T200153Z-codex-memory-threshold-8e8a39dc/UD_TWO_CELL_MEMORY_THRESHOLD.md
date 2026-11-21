# Exterior absorption and the two-cell memory threshold

**Conditional threshold calculation. Physical Promotion = 0.**

Use the two tetrahedra sharing face 012, the orthogonal projection onto their overlapping vertex-average span, and the six-exterior-face Whitney edge sink from UD #589. The internal shared-face edge sink leaves this memory unchanged. This result concerns those memory-active blocks. It says nothing about uniform decay on the full unresolved space.

In the orthonormal even and odd channels, put \(d=4\gamma_{\rm ext}/3\), \(\omega=\sqrt{32/7}\), \(x=\omega \tau\), and \(\zeta=d/(2\omega)\). The normalized magnitudes divide by the individual nonzero initial kernel magnitudes \(3/7\) and \(3\), respectively. We use \(\delta=1/62\) as a stipulated tolerance for these normalized kernels. A mapping from the coherence-law ambiguity observable to this memory criterion has not been established.

## The tolerance requires an observation horizon

For a prescribed \(T>0\), require both channels to remain within tolerance for **every** \(\tau\ge T\):
\[
 \sup_{\tau\ge T}\max\!\left\{\tfrac73|{\cal K}_+(\tau)|,\tfrac13|{\cal K}_-(\tau)|\right\}\le \delta .
\]
At time zero both normalized channels equal one, independently of coupling. Thus no finite coupling meets the tolerance over all \(\tau\ge0\). Without \(T\) or a different explicit comparison metric there is no unique positive minimum. Conversely any positive coupling eventually crosses a positive tolerance in this exterior model. Memory suppression is a kernel-level test. An error bound for a Markovian approximation must control the convolution against admissible input histories and any unresolved initial forcing.

## Exact tail calculation

Set \(X=\omega T\) and \(L=\log 62\). The odd normalized magnitude is \(e^{-2\zeta x}\), so every feasible coupling obeys \(2\zeta X\ge L\), equivalently \(\gamma_{\rm ext}\ge 3L/(4T)\).

For \(0\le\zeta<1\), set \(\theta=\arcsin\zeta\), \(\nu=\cos\theta\). The even normalized signed response, with the overall negative kernel sign removed, is
\[
 f_\zeta(x)=\frac{e^{-\zeta x}}{\nu}\cos(\nu x+\theta).
\]
Its stationary points are \(x_m=(m\pi-2\theta)/\nu\), with values \((-1)^me^{-\zeta x_m}\). Hence the exact tail maximum is
\[
 H_\zeta(X)=\max\bigl(|f_\zeta(X)|,\ e^{-\zeta x_m},\ e^{-2\zeta X}\bigr),
 \qquad m=\left\lceil\frac{\nu X+2\theta}{\pi}\right\rceil.
\]
Later extrema have smaller magnitude for positive \(\zeta\). At \(\zeta=1\), the even response is \(e^{-x}(1-x)\) and the only later extremum to include is \(x=2\) if \(X\le2\). For \(\zeta>1\), set \(\alpha=\zeta-\sqrt{\zeta^2-1}\), \(\beta=\zeta+\sqrt{\zeta^2-1}\). The even response is
\[
 f_\zeta(x)=\frac{\beta e^{-\beta x}-\alpha e^{-\alpha x}}{\beta-\alpha}.
\]
Compare the endpoint to the magnitude at \(x_*=2\log(\beta/\alpha)/(\beta-\alpha)\) when \(x_*\ge X\). In each case include the odd endpoint. The minimum coupling for a given \(T\) is \(3\omega/2\) times the smallest \(\zeta\) meeting this exact test.

## Worked horizon of one undamped period

Choose \(T=2\pi/\omega\), so \(X=2\pi\). Here the minimum is set by the second even extremum:
\[
 2(\pi-\theta_*)\tan\theta_*=\log 62,\qquad
 \gamma_{\min}=\tfrac32\omega\sin\theta_*
 \simeq 2.071267496
\]
in the declared carrier time units. The replay brackets \(\zeta_*=\sin\theta_*\) between \(0.6458\) and \(0.6459\). At the minimum the even tail reaches exactly \(1/62\), and the odd tail remains below \(0.0003\). A strict inequality calls for coupling slightly above the displayed minimum within the same local regime.

To see minimality, first consider \(\zeta<\zeta_*\) with \(x_2\ge X\). The magnitude at \(x_2\) exceeds \(1/62\) because \(\zeta x_2=2(\pi-\theta)\tan\theta\) is strictly increasing on \(0\le\theta<\pi/2\). In the other case, \(x_2<X\), write \(b=2\pi\nu+2\theta-2\pi>0\). Its maximum is at \(\zeta=1/\pi\) and is less than \(0.34\). The derivative is negative for \(\zeta>1/\pi\), and \(b(0.62)<0\), so \(x_2<X\) implies \(\zeta<0.62\). The endpoint value satisfies
\[
 f_\zeta(X)=e^{-\zeta X}\bigl(\cos b+\tan\theta\sin b\bigr)
 \ \ge\ e^{-0.62X}\cos(0.34)>1/62 .
\]
At \(\zeta_*\), \(x_2>X\), the endpoint response is positive and increasing up to \(x_2\), and all subsequent extrema are smaller. The odd bound also holds. These checks exclude every smaller coupling, including values that momentarily cancel the even channel at some earlier or later phase.

[Exact seam and exterior memory kernels, UD #589](https://github.com/ud-tetra/UD/pull/589)
