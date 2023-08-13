import fractions
import functools
import numpy as np


def print_m(m):
    for x in m:
        for y in x:
            print str(y) + "\t",
        print


def lcm(arr):
    l = functools.reduce(lambda x, y: (x*y) // fractions.gcd(x, y), arr)
    return l


def get_terminals(m):
    states = []
    for s, p in enumerate(m):
        if p.count(0) == len(p):
            states.append(s)
    return states


def probability0_matrix(m):
    p_m = []
    for i, x in enumerate(m):
        m[i][i] = 0
        p_m.append([])
        den = float(sum(x)) or 1.
        for y in x:
            p_m[-1].append(y/den)
    return p_m


def coefs(p0_m, init_s=0):
    an = np.array([[x[i] for x in p0_m] for i in range(len(p0_m))], dtype='float')
    np.fill_diagonal(an, -1.)
    a0 = np.array([0]*len(p0_m), dtype='float')
    a0[init_s] = -1.
    return an, a0


def solve_probabilities(p0_m):
    an, a0 = coefs(p0_m)
    return np.linalg.solve(an, a0)


def solution(m):
    p0_m = probability0_matrix(m)   # Probability to directly jump to other states
    pN = solve_probabilities(p0_m)  # Probability to get some state starting from state 0
    terminals = get_terminals(m)
    p_terminals = [prob for state, prob in enumerate(pN) if state in terminals]
    result = [p/sum(p_terminals) for p in p_terminals]
    result = [fractions.Fraction(f).limit_denominator() for f in result]
    common_den = int(lcm([x.denominator for x in result]))
    result = [int(x.numerator*common_den/x.denominator) for x in result] + [common_den]
    return result


if __name__ == "__main__":
    sol1 = solution(
        [
            [0, 1, 0, 0, 0, 1],
            [4, 0, 0, 3, 2, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
    )
    print(sol1, sol1 == [0, 3, 2, 9, 14])

    sol2 = solution(
        [
            [0, 2, 1, 0, 0],
            [0, 0, 0, 3, 4],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
    )
    print(sol2, sol2 == [7, 6, 8, 21])

    sol3 = solution(
        [
            [0, 2, 1, 0, 0],
            [0, 1, 0, 3, 4],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
    )
    print(sol3, sol3 == [7, 6, 8, 21])
