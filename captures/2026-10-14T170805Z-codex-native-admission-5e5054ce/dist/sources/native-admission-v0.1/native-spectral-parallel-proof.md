# Independent spectral-distance audit, v0.1

Status: EXACT mathematics for declared comparison; physical promotion 0;
independent human review pending. This is a constructor-team AI audit.

Let the supplied length-10 spin clock have positive frequencies
`kappa * {2,4,6,8,10}` and endpoint time `T = pi/(2*kappa)`. Let the
comparison native spectrum be `gamma * {0,+/-a,+/-b}`. For `x=gamma/kappa`,
define

`b(x) = max_{p in {2,4,6,8,10}} min(p, |p-a*x|, |p-b*x|)`.

Negative native centres never improve the nearest distance of positive targets.
If a complete target-mode isometry E intertwines Hermitian generators up to
`eta = ||H_native E - E H_programme||`, then for every target eigenvector v,
the spectral theorem gives `||(H_native - kappa*p) Ev|| >= kappa*distance`.
Thus `eta >= kappa*b(x)` and `T*eta >= pi*b(x)/2`.

This is a necessary floor for the Duhamel upper-bound budget. It is not an
endpoint-error lower bound and does not give an attainable residual optimum.
Frequency multiplicity and orthogonality can strengthen the obstruction.

## Exact optimized floors

| Complex | a,b | inf b | Optimizing comparison x |
| --- | --- | --- | --- |
| Delta3 | 2,2 | 3 | 7/2 |
| K-minus | sqrt(3),sqrt(5) | 7 sqrt(15) - 25 | 7(sqrt(5)-sqrt(3)) |
| K-plus | sqrt(2),sqrt(5) | 2 | [8/sqrt(5),3 sqrt(2)] |

For Delta3, a radius below 3 forces target4 away from centre0. Targets4 and10
then require the same positive centre, whose minimum covering radius is3.
Radius3 is attained at centre7; this centre is uniquely necessary.

For K-minus, write y=a*x and r=b/a=sqrt(15)/3. A radius below3 cannot assign
target4 to the upper centre: monotonic nearest-centre assignments would also
assign10 there, requiring radius3. Hence4 requires y and10 requires r*y.
The constraints y<=4+epsilon and r*y>=10-epsilon give

`epsilon >= (10-4*r)/(1+r) = 7 sqrt(15)-25`.

At equality, `y=14/(1+r)=7 sqrt(15)-21`; targets2,4,6,8,10 are all covered
by0,y,r*y. Since the floor is below3, the preceding alternative is excluded
and the optimizing x is unique.

For K-plus, r=sqrt(10)/2<2. A radius below2 cannot assign target2 to centre0.
If2 uses the upper centre,10 cannot be covered. If2 uses the lower centre,
y<4 while10 requires r*y>8, contradicting r<2. Thus epsilon>=2.
At epsilon2, target4 must use the lower centre and10 the upper centre, giving
`y<=6` and `r*y>=8`. Conversely all targets are covered for
`8/r<=y<=6`, proving the complete optimizing interval above.

## Independent replay

`native-spectral-parallel-check.py` builds the simplex boundary maps anew,
checks boundary composition and skewness, and obtains exactly:

- Delta3: `lambda*(lambda^2+4)^7`, f=(4,6,4,1).
- K-minus: `lambda*(lambda^2+3)^4*(lambda^2+5)^7`, f=(5,9,7,2).
- K-plus: `lambda*(lambda^2+2)^2*(lambda^2+5)^11`, f=(5,10,9,3).

The code checks all21 monotone assignments per complex. Each branch optimum
is certified exactly by active affine slopes straddling zero, or a valid
one-sided boundary slope. All63 minima are exactly compared. An additional
729 arbitrary assignments are checked numerically, plus dense isometry
residual sanity controls. The latter are generated mathematical controls,
not source-defined native encodings.

The endpoint alias negative control uses H1=H0+4I and T=pi/2. The generator
residual is4, yet the endpoint propagators coincide. The slow-clock control
scales both generators together: eta scales with kappa while T scales as
1/kappa, leaving T*eta unchanged.

All comparison scalings are free mathematical comparisons. None selects a
native metric, coupling, absolute clock or physical calibration. Exact
intertwining for these complete target modes is excluded by the positive
spectral floors. Small-error certification through this Duhamel budget is
unavailable; actual native endpoint error remains unassessed.
