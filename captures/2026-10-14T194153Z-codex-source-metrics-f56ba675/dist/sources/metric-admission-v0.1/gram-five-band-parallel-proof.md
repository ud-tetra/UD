# C0173 Gram family: exact five-band compatibility obstruction

Status: exact conditional mathematical obstruction. New constructor-team AI
verification, not independent human review. Physical promotion 0. Prior source
bytes and prior parallel evidence are unchanged.

## Source and regenerated spectrum

C0173, Geometric inner-product interface, declares the fixed-shape Gram rules
A and B, not a unique source-selected native dynamics. Increasing simplex
orientation fixes the boundaries. On vertices (1,1,r), (1,-1,-r), (-1,1,-r),
(-1,-1,r), r>0, put q=r^2 and p=1 (A) or p=2 (B). The metric is

    G_0=I_4,
    G_1=diag(a,a,1,1,a,a), G_2=b I_4, G_3=(c),
    a=((1+q)/2)^p, b=((2q+1)/3)^p, c=q^p.

The five possible positive squared frequencies are

    u=4/a, v=2+2/a, x=4a/b, y=2(a+1)/b, z=4b/c.

The full skew-generator characteristic polynomial is

    lambda (lambda^2+u)(lambda^2+v)^2
           (lambda^2+x)(lambda^2+y)^2(lambda^2+z).

Fresh Fraction code builds Gram determinants directly from coordinates,
normalizes them by the regular reference determinants (8,48,256), regenerates
all boundary signs, computes G^-1 D^T G-D, and checks all characteristic
coefficients and exact degree-block eigenspace multiplicities. Eight samples
r=1,2,3/2,1/3, each with p=1,2, pass. At q=4:

| Rule | u | v | x | y | z |
|---|---:|---:|---:|---:|---:|
| A | 8/5 | 14/5 | 10/3 | 7/3 | 3 |
| B | 16/25 | 58/25 | 25/9 | 29/18 | 9/4 |

## Exact invariant and finite obstruction

For every a,b,c>0 in this diagonal metric pattern,

    u/v+x/y = 2/(a+1)+2a/(a+1)=2.

This identity is stronger in scope than a check at fixed q or only the two
source rules: neither b nor c nor a common overall rate affects it.

The n=10 programme has five distinct positive frequency squares proportional
to {1,4,9,16,25}. If one Gram carrier or identical uncoupled copies admitted an
exact invariant isometric full-generator embedding, its native spectrum would
have to contain all five of these distinct positive bands. There are only five
native candidates u,v,x,y,z. Thus they would have to be distinct and be a
bijection to the five target squares, up to their common proportional factor.
In particular u,v,x,y would assign to four distinct targets. That would require

    U/V+X/Y=2.

All 5*4*3*2=120 ordered assignments violate this equality. The smallest
absolute violation is exactly 1/144, attained by

    (U,V,X,Y)=(4,9,25,16),
    4/9+25/16=289/144=2+1/144,

and its pair-swapped assignment (25,16,4,9). The complete 120-row rational
receipt is preserved in the JSON. Repeated native candidates produce fewer
than five distinct bands and already fail the necessary count.

Therefore no positive metric in this diagonal Gram pattern, including every
q>0 Rule A or B, admits exact full-generator embedding of the default n=10
programme in one tetrahedron or identical uncoupled copies under a common
rate. This does not rely on optimizing q, approximating irrational roots,
or choosing an encoding from spectral targets.

## Scope limits

The 1/144 quantity is a dimensionless finite invariant gap; it is not directly
an operator residual or evolution-error lower bound. A conversion would require
additional admitted scale and denominator bounds. Endpoint agreement may still
occur despite generator mismatch. Heterogeneous copies, couplings between
copies, different diagonal patterns, other complexes, and non-invariant or
restricted-input comparisons are distinct classes not excluded here. No
source-selected Gram rule, physical metric, SI time, energy, protected export
or laboratory realization is established.
