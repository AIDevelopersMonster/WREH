#!/usr/bin/env python3
"""Exact rational checks of WR-V's finite benchmark; no external packages."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))

def main():
    a = (F(0), F(1, 2), F(1))
    d = (F(0), F(0), F(1))
    tested = 0
    # Enumerate the simplex independently of the manuscript's interval formula.
    for i in range(41):
        for j in range(41-i):
            k = (F(i, 40), F(j, 40), F(40-i-j, 40))
            m, n = dot(a, k), dot(d, k)
            lower, upper = max(F(0), 2*m-1), m
            assert lower <= n <= upper
            assert (1-2*m+n, 2*m-2*n, n) == k
            assert 0 <= m <= 1
            tested += 1
    # Test a continuum parameterization on an independent rational response grid.
    curves = 0
    for i in range(81):
        m = F(i, 80)
        lo, hi = max(F(0), 2*m-1), m
        assert (lo == hi) == (m in (0, 1))
        for j in range(11):
            t = lo + F(j, 10)*(hi-lo)
            k = (1-2*m+t, 2*m-2*t, t)
            assert min(k) >= 0 and sum(k) == 1 and dot(a, k) == m
            curves += 1
    middle = (F(0), F(1), F(0))
    mix = (F(1, 2), F(0), F(1, 2))
    assert dot(a, middle) == dot(a, mix) == F(1, 2)
    assert dot(d, middle) != dot(d, mix)
    # An instrument's outcome marginal is independent of its successor row.
    for k in [(F(1), F(0), F(0)), (F(0), F(1), F(0)), mix]:
        rows = [tuple(F(1, 2)*v for v in k) for _ in range(2)]
        assert [sum(r) for r in rows] == [F(1, 2), F(1, 2)]
    # The null vector meets one-sided support constraints exactly in the example.
    v = (F(1), F(-2), F(1))
    assert sum(v) == 0 and dot(a, v) == 0
    def direction_allowed(k, vec):
        return all(value >= 0 for weight, value in zip(k, vec) if weight == 0)
    for endpoint in [(F(1), F(0), F(0)), (F(0), F(0), F(1))]:
        assert not direction_allowed(endpoint, v)
        assert not direction_allowed(endpoint, tuple(-t for t in v))
    assert direction_allowed(middle, v)
    # A positive uncertainty bound defeats the exact m=0 boundary certificate.
    eps = F(1, 100)
    nearby = (1-2*eps, 2*eps, F(0))
    assert dot(a, nearby) == eps and nearby != (1, 0, 0)
    # Overlap-compatible triangle: no global assignment; split labels: eight.
    global_count = sum((A^B == 1 and B^C == 1 and A^C == 1)
                       for A, B, C in product((0, 1), repeat=3))
    split_count = sum((a0^b0 == 1 and b1^c0 == 1 and a1^c1 == 1)
                      for a0, b0, b1, c0, a1, c1 in product((0, 1), repeat=6))
    assert global_count == 0 and split_count == 8
    posterior = F(9, 10)**3 / (F(9, 10)**3 + F(1, 10)**3)
    assert posterior == F(729, 730) and 0 < posterior < 1
    # Individually plausible probe probabilities can be jointly incompatible.
    bad_m, bad_n = F(1, 4), F(1, 2)
    bad_k = (1-2*bad_m+bad_n, 2*bad_m-2*bad_n, bad_n)
    assert 0 <= bad_m <= 1 and 0 <= bad_n <= 1
    assert sum(bad_k) == 1 and dot(a, bad_k) == bad_m and dot(d, bad_k) == bad_n
    assert min(bad_k) < 0  # Full rank fixes the affine candidate, which is inadmissible.
    # A single likelihood zero eliminates a candidate, not necessarily every rival.
    first = (F(1), F(0), F(1, 2))
    assert sum(w > 0 for w in first) == 2
    accumulated = tuple(x*y for x,y in zip(first,(F(1),F(1,2),F(0))))
    assert sum(w > 0 for w in accumulated) == 1
    report = {
        'arithmetic': 'exact fractions; no sampling', 'simplex_cases': tested,
        'curve_cases': curves, 'instrument_models': 3,
        'original_triangle_assignments': global_count,
        'split_triangle_assignments': split_count,
        'positive_likelihood_posterior': str(posterior),
        'joint_probe_incompatibility': {'m':'1/4','n2':'1/2','affine_candidate':['1','-1/2','1/2'],'status':'PASS'},
        'zero_likelihood_support_sizes': [2,1],
        'status': 'PASS', 'scope': 'finite benchmarks; not a proof of general theorems'
    }
    (ROOT/'verification.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))

if __name__ == '__main__':
    main()
