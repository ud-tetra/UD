# Canonical projected-matrix identity: independent proof

Development — no registry entry. Same-team independent mathematical review; external promotion review PENDING. Physical Promotion = 0. The proof and test expectations are frozen before exercising the new implementation.

## Typed matrix and canonical form

The mathematical input is Z=N/2^b, with a positive m by n signed int64 integer matrix N and0<=b<=256; m<=8191 and n<=321 are resource controls. Here “positive m by n” concerns the dimensions; entries may be negative or zero. This identity profile does not require m>=n or spectral factors. Let g be the nonnegative integer gcd of the absolute values of every entry of N, computed with Python mathematical integers. Set

\[
c=\gcd(g,2^b),\quad \bar N=N/c,\quad 2^{\bar b}=2^b/c.
\]

The common divisor c is a power of two and divides every entry of N. For the all-zero matrix, g=0, so c=2^b and the canonical result is the zero matrix with exponent0. For nonzero N, c=2^t where t=min(b,min v2(nonzero entries)), yielding exactly the proposed canonical rule.

An independent Fraction construction reaches the same result: reduce every individual rational N_ij/2^b, take the least common multiple of their reduced denominators, and express every entry using that common denominator. Because every denominator is a power of two, the common denominator is a power of two, exactly2^b/c. This provides an independent oracle without signed bitwise OR or array right-shift operations.

If bar_b>0, at least one entry of bar_N is odd; otherwise a further factor two could have been canceled. If bar_b=0, the numerator may still be entirely even: no negative denominator exponent is permitted. This saturation case is essential for integer matrices.

## Uniqueness and typed bytes

For any fixed dimensions, every exact rational matrix with dyadic entries has a unique least positive common power-of-two denominator and corresponding integer numerators. The gcd/Fraction construction produces it. Hence equal dimensions and equal rational entries imply equal canonical exponent and numerator matrix. Conversely equal canonical exponent/numerators plainly imply equal exact rational entries.

Serialize the canonical matrix using exactly

    b'UD_DYADIC_MATRIX_V1\0' + struct.pack('<IIH',m,n,bar_b)
    + C-order signed little-endian int64 entries of bar_N.

Dimensions/exponent have fixed widths, followed by exactly8*m*n entry bytes. The domain tag, dimensions and fixed encoding make the representation unambiguous. Therefore canonical-byte equality holds **if and only if** the dimensions and exact rational matrix agree. In particular different shapes are different typed matrices even if their flattened entries happen to agree.

Layout and scaling aliases do not change the rational object. A C-order versus Fortran-order NPY wrapper for the same logical N and an admissible scaled pair (2N,b+1) produce identical canonical bytes. Scaling is admissible only when the supplied new numerator still fits signed int64 and the exponent remains inside the declared profile. Changing b without the matching numerator change generally changes the matrix, except for the all-zero case.

All arithmetic defining the oracle uses Python integers/Fraction; abs(-2^63)=2^63 is safe. Division by c cannot enlarge any numerator's magnitude, so canonical numerators remain int64. The input (-2^63,b) can cancel exactlymin(b,63) powers of two. Signed right shift is correct only if the implementation establishes that divisibility; taking a NumPy int64 absolute value of INT64_MIN would overflow and must not underpin the proof.

## Fingerprints versus exact identity

SHA256 of the typed bytes is a cryptographic binding/fingerprint, not a mathematically injective encoding. The canonical-byte equivalence theorem is exact; fingerprint equality alone does not prove that theorem's premises without the usual collision-resistance assumption or a byte comparison. The screen must accurately report LISTED_FINGERPRINT or UNLISTED_FINGERPRINT, rather than silently upgrading a digest comparison to a proof of raw/acquisition equality.

A valid match compares only the projected rational Z. It establishes neither equality nor inequality of raw records, preparation states, spectral factors, hidden states, acquisition events or physical carriers. Independent repetitions can produce the same Z; distinct hidden states can have the same projection. Thus a listed fingerprint is not an independence rejection, and an unlisted fingerprint is not evidence of a fresh preparation or independent acquisition.

For **both valid fingerprint classes**, independent_acquisition and fresh_preparation must remain NOT_ESTABLISHED; provenance_status remains HOLD_PROVENANCE_NOT_ESTABLISHED; numerical_spectral_certificate remains NOT_EVALUATED and physical promotion remains0. A valid screen exits successfully even though provenance is on HOLD. Invalid intake rejects before output creation. Duplicate record IDs in a catalog are invalid, whereas the same fingerprint under different IDs may represent legitimate replicated records and is allowed.

No new acquisition, numerical-spectrum certification, fitted model, physical promotion or universal whole-program/race guarantee follows. Input-byte stability and faithful intake remain explicit program assumptions; finite tests do not prove universal program correctness.
