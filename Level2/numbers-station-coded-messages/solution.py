def solution(l, t):
    acc = 0
    first = 0
    last = 0
    while True:
        if acc < t:
            acc += l[last]
            last += 1
            if last >= len(l) and acc < t:
                break
        elif acc > t:
            if first < last:
                acc -= l[first]
                first += 1
                if first == len(l) and acc != t:
                    break
        if acc == t:
            return [first, last-1]

    return [-1, -1]


if __name__ == "__main__":
    print(solution([4, 3, 5, 7, 8], 12))
    print(solution([1, 2, 3, 4], 15))
    print(solution([4, 3, 10, 2, 8,12], 12))
