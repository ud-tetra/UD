"""Exact, conservative early HOLD for this proposal's residual-budget verifier."""
from fractions import Fraction
from math import isqrt

def pair(x):
    return [x.numerator, x.denominator]

def residual_preflight(squared_residual, coefficient_bound, threshold, bits=100):
    """Call only after the existing all-readings and phase-enclosure checks.

    The exact squared residual uses dyadic approximations to modal phases.
    sqrt(2294)<48 bounds the phase correction for all 62*37 coordinates.
    This gate rejects a proof attempt, not the true spectrum of the record.
    """
    squared_residual = Fraction(squared_residual)
    threshold = Fraction(threshold)
    if squared_residual < 0 or threshold <= 0:
        raise ValueError('Nonnegative residual and positive threshold required')
    if type(coefficient_bound) is not int or coefficient_bound < 0:
        raise ValueError('Nonnegative integer coefficient bound required')
    if type(bits) is not int or bits < 1:
        raise ValueError('Positive integer precision required')
    n = isqrt((squared_residual.numerator << (2*bits)) // squared_residual.denominator)
    lo = Fraction(n, 1 << bits)
    phase = Fraction(48*coefficient_bound, 1 << 120)
    actual_lower = max(Fraction(0), lo-phase)
    hold = actual_lower > threshold
    return {
        'status': 'EARLY_HOLD' if hold else 'CONTINUE_FULL_VERIFIER',
        'exact_squared_dyadic_phase_residual': pair(squared_residual),
        'sqrt_floor_bits': bits,
        'dyadic_phase_residual_lower': pair(lo),
        'sqrt_bracket_width': [1, 1 << bits],
        'coefficient_row_max_sum': coefficient_bound,
        'phase_correction_frobenius_upper': pair(phase),
        'true_proposal_residual_frobenius_lower': pair(actual_lower),
        'selection_threshold': pair(threshold),
        'comparison': 'strict >; equality continues',
        'scope': 'Infeasibility of the current proposal/residual-budget certificate only',
        'true_record_spectral_signature_decided': False,
        'physical_promotion': 0,
    }
