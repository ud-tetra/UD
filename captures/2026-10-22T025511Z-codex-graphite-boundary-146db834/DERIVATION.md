# Boundary-aware force derivatives

Development — no registry entry. Physical promotion0. Conventional numerical analysis of the declared REBO+smooth KCz model; no UD-native correspondence. Constructor: Codex. Non-constructor reviewers: none.

Let F(q) be the projected force and w a unit coordinate direction. The Hessian action is H w=-dF(q+s w)/ds at s=0. For h>0 define

Q_+(h)=-[-3F(0)+4F(h)-F(2h)]/(2h),
Q_-(h)=-[3F(0)-4F(-h)+F(-2h)]/(2h).

If the one-sided force has a cubic Taylor remainder bounded by O(h³), cancellation of its constant and quadratic terms gives Q_±(h)=Hw+O(h²). If the force is only differentiable at0, both are still consistent as h tends to zero, but that rate is not guaranteed. C2 continuity of energy implies C1 continuity of force only under the stated smoothness of all remaining local factors.

The averaged estimate satisfies exactly in real arithmetic

A(h)=[Q_+(h)+Q_-(h)]/2=2D(h)-D(2h),
D(h)=-[F(h)-F(-h)]/(2h).

At an exact join where the one-sided second force derivatives differ, D(h) can have O(h) bias. A(h) cancels that leading term under the corresponding one-sided Taylor assumptions. An interior crossing between0 and2h changes the asymptotic regime; this protocol does not assume Richardson cancellation is accurate there. It requires observed side and step agreement instead.

The actual stored CH.rebo decimals give, for both carbon angular families, g(-1/2)=13201/250000, g'(-1/2)=17/100, g''(-1/2)=37/100. Their right-minus-left third derivative jump is12167037/500000. Exact rational arithmetic verifies these scalar facts. It does not certify every runtime force term, binary arithmetic or the entire Hessian analytically.

v0.1 restricted allowed crossings to triples starting within1e-10 of-1/2. Geometry showed additional triples cross the same verified join. Both cases failed preflight; four worker assertions aborted before any force evaluation. This failure remains immutable.

v0.2 permits any crossing of that same C2 join, rejects sampled crossings of the other two carbon angular knots, and checks the actual one-sided and centered coordinate representations. The estimator, three fixed h values and force-agreement thresholds are unchanged. This is an explicitly revised, exposed-data numerical protocol, not blind preregistration. It must pass on its own data; prior failed plans are not relabeled.

Fixed h values are2e-5,1e-5,5e-6Å. The middle averaged derivative is retained. Every coordinate and nine directions require side agreement, adjacent-step agreement of both sides and their average, reverse repeats, matrix symmetry and directional agreement. Stability uses a tenfold spectral adjacent-step diagnostic, not a rigorous interval error bound. Qualification is restricted to the fixed-cell primitive-periodic81-coordinate family with global translations removed.
