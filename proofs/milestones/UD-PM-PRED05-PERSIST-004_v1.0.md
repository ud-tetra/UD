# UD-PM-PRED05-PERSIST-004 v1.0 — Retained memory alone does not protect first homology

**Kind:** NO_GO / constructive topological counterexample. **Status:** VERIFIED_SCOPED / EXACT_CONDITIONAL. **Review:** DEFERRED. **Physical promotion:** 0.

## Statement

Let a tetrahedral supported complex be the product of a punctured planar disk (annulus) with an interval. Preserve every original excision mark and never restore a removed tetrahedron. Allow additional star-excision at other sites. These two conditions alone do **not** ensure preservation of nontrivial first homology.

## Proof

Select a radial path connecting the inner annular boundary to its outer boundary. Excise an open regular neighborhood of that path across the interval, retaining the original excisions. The resulting planar region is a disk with a notch reaching its boundary and is contractible. Its product with an interval therefore has first integral homology zero. This occurs without restoring any previously removed tetrahedron and with monotone accumulated marks. Consequently monotone memory plus a restoration veto is insufficient for topological persistence when other topology-changing deletions remain admissible. QED.

## Finite independent witness

The independent Freudenthal checker removed the columns based at all planar grid vertices `(x,N/2)` for `x=N/2,...,N` on all three vertical levels. This strictly enlarges the original center-column mark set. For `N=4,6,8,10`, the surviving complexes have F2 Betti vector `(1,0,0,0)`, compared to `(1,1,0,0)` for the initial completed tunnel.

## Scope and reopening

Topological persistence requires a post-event update class that fixes the supported complex or restricts changes to PL-homeomorphism-preserving moves (or another independently proved topological protection rule). This NO-GO does not exclude energetic stability from a different source law. The boundary and memory maps are assumed, not derived from UD dynamics. Review DEFERRED; physical promotion 0.
