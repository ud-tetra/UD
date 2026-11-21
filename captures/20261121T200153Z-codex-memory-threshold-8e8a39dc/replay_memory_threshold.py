#!/usr/bin/env python3
"""Replay the one-period threshold and the bounds used to prove minimality."""

from math import asin, ceil, cos, exp, log, pi, sin, sqrt, tan


def decay_exponent(zeta):
    theta = asin(zeta)
    return 2 * (pi - theta) * tan(theta)


def phase_offset(zeta):
    return 2 * pi * sqrt(1 - zeta*zeta) + 2 * asin(zeta) - 2 * pi


def main():
    tolerance = 1/62
    target = log(62)
    horizon = 2*pi
    lo, hi = 0.6458, 0.6459
    assert decay_exponent(lo) < target < decay_exponent(hi)
    assert phase_offset(1/pi) < 0.34
    assert phase_offset(0.62) < 0
    assert exp(-0.62*horizon)*cos(0.34) > tolerance
    for _ in range(45):
        mid = (lo + hi)/2
        if decay_exponent(mid) < target:
            lo = mid
        else:
            hi = mid
    zeta = (lo + hi)/2
    theta = asin(zeta)
    nu = cos(theta)
    station = ceil((nu*horizon+2*theta)/pi)
    assert station == 2
    peak_time = (station*pi-2*theta)/nu
    assert peak_time > horizon
    peak = exp(-zeta*peak_time)
    endpoint = abs(exp(-zeta*horizon)*cos(nu*horizon+theta)/nu)
    odd = exp(-2*zeta*horizon)
    assert endpoint < peak and odd < 0.0003
    assert abs(peak-tolerance) < 1e-14
    gamma = 1.5*sqrt(32/7)*sin(theta)
    print(f'One-period horizon: zeta={zeta:.12f}, gamma_ext={gamma:.12f}')
    print(f'Even endpoint={endpoint:.12f}, even tail peak={peak:.12f}, odd tail={odd:.12f}')


if __name__ == '__main__':
    main()
