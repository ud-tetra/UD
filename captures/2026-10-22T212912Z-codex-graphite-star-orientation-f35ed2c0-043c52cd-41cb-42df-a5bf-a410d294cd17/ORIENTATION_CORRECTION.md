# Corrected reciprocal-star orientation

The prior capture in draft PR #419 described the reciprocal triple as an oriented 120° star while writing `g3=g1+g2`. For equal-length `g1,g2` separated by 120°, the *oriented* third member is `g3=-(g1+g2)`. The three then sum to zero and every pair is separated by 120°. Since cosine is even, `cos(g3·x)=cos((g1+g2)·x)`; the previous landscape, stationary energies, Hessians, curvature/barrier ratios, and load derivatives are numerically and algebraically unchanged. The uncorrected verbal orientation and object definition are superseded by `GRAPHITE_METHOD_BOOT_AND_CURVATURE_v2.md` and manuscript v4.

This was found by constructor self-review. `verify_curvature_port_oriented.py` now checks all three pairwise reciprocal inner products and the oriented sum exactly. The method receipt in this capture records the changed object definition and dependent conclusions. Physical promotion remains 0.
