# UD K4 Primitive Pre-Birth Channel v1.1

**Status:** `STRUCTURAL_PASS__NATIVE_BIRTH_SOURCE_BLOCKED`. Development only. Physical promotion 0.

## What is new

- Exact representation theorem: `dim Hom_S4(C2_signed, C3_sign)=1`; the unique linear source-channel direction is `c ↦ uᵀc`. Its strength and event trigger remain OPEN.
- Exact no-go: no nonzero `S4`-equivariant **linear** map from the signed face representation to an orientation-even scalar.
- Exact all-or-none S4-invariant binary hard-face gate; it cannot choose HOLD or BIRTH.
- Same-input conservative HOLD and multiple BIRTH countermodels preserve quadratic support but differ in event and amplitude.
- Conditional burden-mixing and face→cell support flux formulas do not supply a constitutive pre-birth source.

## Reproduction

```bash
python UD_K4_PREBIRTH_SOURCE_CHANNEL_VERIFY_v1.1.py
python UD_K4_PREBIRTH_SOURCE_INDEPENDENT_FRACTION_v1.1.py
```

Requires Python 3.11+; first verifier requires SymPy; second uses standard library only. Expected **5,377** and **4,760** exact assertion groups respectively.

**Dependencies:** attached Ledger v0.39(2), preceding Face Activation v1.0, Quadrants v0.9. No native coefficient frozen or overwritten; no physical field law claimed.
