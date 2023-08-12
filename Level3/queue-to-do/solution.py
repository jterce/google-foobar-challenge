def xor_0(n):

    #         i, 1, 4i+3, 0
    #         --------------
    # i=0  |  0, 1,   3,  0,
    # i=1  |  4, 1,   7,  0,
    # i=2  |  8, 1,  11,  0,

    i, rem = divmod(n, 4)
    if rem == 0: return 4*i
    elif rem == 1: return 1
    elif rem == 2: return 4*i + 3
    elif rem == 3: return 0


def xor_from(start, length):
    return xor_0(start-1) ^ xor_0(start + length - 1)


def solution(start, length):
    r = 0
    id_start = start
    for line_idx in xrange(length):
        r ^= xor_from(id_start, length - line_idx)
        id_start += length
    return r


def print_xor_pattern(n):
    for i in xrange(0, n):
        res = xor_0(i)
        print res,
        if res == 0: print


if __name__ == "__main__":
    # print_xor_pattern(100)
    print(solution(17, 4))
    print(solution(0, 3))
    # print(solution(0, 1000000))
