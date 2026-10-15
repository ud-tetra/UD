# PACKET_VERTEX_CAPACITY_HARD_GATE_INTEGRATION_INTO_STRICT_CONSERVATIVE_ADMISSIBILITY_v0.1

**Status:** LOCKED_PASS  
**Exact capacity gate:** INTEGRATED  
**Strict conservative hard gate:** STRENGTHENED  
**Physical promotion:** 0  
**Numeric governance:** FRACTION_FIRST  
**Crown:** off

## 1. Existing locked hard gate

The current capacity-limited admissibility stratum supplies

\[
\boxed{
a_i
=
\Theta
\left(
\frac{7}{768}-B_i
\right).
}
\]

In the locked equality convention,

\[
\boxed{
B_i\le\frac{7}{768}
\Rightarrow
a_i=1,
}
\]

while

\[
\boxed{
B_i>\frac{7}{768}
\Rightarrow
a_i=0.
}
\]

This is a hard selector.

It is separate from the soft boundary diagnostic \(b_i\).

The underived soft threshold \(b_{\rm crit}\) has already been purged from primitive hard selection.

## 2. Exact regression

Use

\[
\frac1{128}
=
\frac6{768},
\]

\[
\frac7{768},
\]

and

\[
\frac1{96}
=
\frac8{768}.
\]

Then

\[
\boxed{
a\left(\frac1{128}\right)=1,
}
\]

\[
\boxed{
a\left(\frac7{768}\right)=1,
}
\]

\[
\boxed{
a\left(\frac1{96}\right)=0.
}
\]

No decimal approximation is required.

## 3. Branch gate

For a branch using required sites \(\mathcal B\),

\[
\boxed{
\chi_{\rm hard}(\mathcal B)
=
\prod_{i\in\mathcal B}a_i.
}
\]

Thus one capacity violation vetoes the whole branch.

Exact passing load vector:

\[
\left(
\frac1{128},
\frac7{768},
\frac1{128},
\frac1{128}
\right)
\]

gives site gates

\[
\boxed{(1,1,1,1)}
\]

and

\[
\boxed{\chi_{\rm hard}=1}.
\]

Exact failing load vector:

\[
\left(
\frac1{128},
\frac1{96},
\frac1{128},
\frac1{128}
\right)
\]

gives

\[
\boxed{(1,0,1,1)}
\]

and

\[
\boxed{\chi_{\rm hard}=0}.
\]

## 4. Strengthened strict conservative gate

On the explicit capacity-limited same-class conservative subdomain, a target must now pass:

1. group-valued K4 transport closure;
2. aggregate seam/framing/cluster transport balance;
3. same governed closure class;
4. identity/provenance event consistency;
5. per-site capacity hard gates;
6. the branch product gate.

Therefore:

\[
\boxed{
\text{transport closed}
\not\Rightarrow
\text{hard admissible}.
}
\]

A transport-perfect candidate can still be vetoed by exact vertex capacity.

## 5. Soft boundary remains separate

Do not replace

\[
\frac7{768}
\]

with a threshold on the soft boundary variable.

The current semantics remain:

```text
soft b_i:
  graded diagnostic/state

hard capacity predicate:
  exact admissibility gate
```

## 6. Re-entry

A site can later return below capacity and reopen its current-state site gate.

That does not resurrect a branch already terminally excluded.

A later viable branch is a new formation with new branch identity and provenance connection.

## 7. Verdict

\[
\boxed{
\text{the strict conservative hard gate now contains a source-derived non-arbitrary physical exclusion rule in the capacity-limited subdomain}.
}
\]
