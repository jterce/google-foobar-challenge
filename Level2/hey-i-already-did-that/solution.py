def int_to_base(n, b):
    if n == 0:
        return '0'
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return ''.join([str(x) for x in digits[::-1]])


def get_next(n, b):
    k = len(n)
    sorted_chars = sorted(n)
    y = int(''.join(sorted_chars), b)
    sorted_chars.reverse()
    x = int(''.join(sorted_chars), b)
    z = x - y
    return int_to_base(z, b).zfill(k)


def solution(n, b):
    ids = [n]
    n1 = n
    idx_match = 0
    while idx_match == len(ids) - 1:
        n1 = get_next(n1, b)
        ids.append(n1)
        idx_match = ids.index(n1)
    return len(ids) - idx_match - 1


if __name__ == "__main__":
    print(solution('210022', 3))
    print(solution('1211', 10))
