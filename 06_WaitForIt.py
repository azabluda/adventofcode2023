# https://adventofcode.com/2023/day/6
# Day 06: Wait For It

from math import *

def solve(t, d):
    t, d = map(int, [t, d])
    Δ = sqrt(t * t - 4 * d) - 1e-10
    return floor((t + Δ) / 2) - ceil((t - Δ) / 2) + 1

def wait4it(data):
    yield prod(solve(t, d) for t, d in zip(*map(str.split, data.split('\n'))))
    yield solve(*data.replace(' ', '').split('\n'))


def inputs():

    yield """
7  15   30
9  40  200
"""

    yield """
 53     91     67     68
250   1330   1081   1025
"""

for data in inputs():
    print(*wait4it(data.strip()))
