import itertools


def solution(num_buns, num_required):
    key_lists = []
    for b in range(num_buns):
        key_lists.append([])
    key_duplicates = num_buns - (num_required - 1) or 1
    key_dist = list(itertools.combinations(range(num_buns), key_duplicates))
    for i, key in enumerate(key_dist):
        for b in key:
            key_lists[b].append(i)

    return key_lists


if __name__ == "__main__":
    results = (
        ((5, 3), [[0, 1, 2, 3, 4, 5], [0, 1, 2, 6, 7, 8], [0, 3, 4, 6, 7, 9], [1, 3, 5, 6, 8, 9], [2, 4, 5, 7, 8, 9]]),
        ((2, 1), [[0], [0]]),
        ((4, 4), [[0], [1], [2], [3]]),
        ((3, 1), [[0], [0], [0]]),
        ((2, 2), [[0], [1]]),
    )
    for args, target in results:
        sol = solution(*args)
        print(args)
        print("\t" + str(target))
        print("\t" + str(sol))
        print("\t" + str(sol == target))
