# Why zero branch clearance is not a Hessian no-go

DERIVED CONDITIONAL. The exact rational interpretation of the actual CH.rebo decimal coefficients gives matching values and first two derivatives for both gC1 and gC2 at c=-1/2. BOUNDARY_JOIN.json records the arithmetic and source digest. The scalar angular functions are C2 at this join; their third derivatives need not match. This is a local source-polynomial result, not a proof of every part of the REBO implementation or a binary error bound.

If the remaining local energy factors are C2, the bond lengths are nonzero and the active angular map is smooth, composition preserves C2 and the local energy Hessian exists across this join. The frozen same-branch stencil is therefore a sufficient procedural guard that can reject a differentiable configuration. This implication does not assert that all its premises have been verified for the full potential.

There is also a concrete reason not to import a second-order convergence assumption. For a scalar force component f along a displacement line, suppose f and f' match at zero with one-sided Taylor expansions through quadratic order and O(|h|³) remainders (for example, bounded one-sided third derivatives). Taylor expansion gives

D_h=[f(h)-f(-h)]/(2h)=f'(0)+(h/4)[f''(0+)-f''(0-)]+O(h²).

Thus even a valid centered estimate of the Hessian (minus the force derivative) may have first-order bias at the join. Away from the exact join, or with additional nearby branch crossings, this expansion has a different regime. Richardson cancellation is not automatically justified by observing three steps.

Next gate: independently check one-sided derivative limits, source smoothness premises, rounded-coordinate errors and crossing membership under a new explicit protocol. Preserve both held cases under the old rule; no thresholds are loosened by this note. Non-constructor review and physical identification remain OPEN.

For both families, the exact shared values are g(-1/2)=13201/250000, g'(-1/2)=17/100 and g''(-1/2)=37/100. The right-minus-left third derivative is12167037/500000. These are potential-file coefficients and derivatives, not UD-native constants or measured material parameters.
