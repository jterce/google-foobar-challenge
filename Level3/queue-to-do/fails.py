import functools


def solution1(start, length):
    acc = 0
    first = start
    for i in xrange(length):
        acc = functools.reduce(lambda x, y: x ^ y, xrange(first, first + length-i), acc)
        first += length
    return acc


def solution2(start, length):
    acc = 0
    line_i = 0
    worker_i = 0
    worker_start = start
    while line_i < length:
        while worker_i < length - line_i:
            acc ^= (worker_start + worker_i)
            worker_i += 1
        line_i += 1
        worker_i = 0
        worker_start += length

    return acc


if __name__ == "__main__":
    print(solution1(17, 4))
    print(solution1(0, 3))
    # print(solution1(0, 1000000))

    print(solution2(17, 4))
    print(solution2(0, 3))
    # print(solution1(0, 1000000))
