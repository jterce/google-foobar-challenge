import random


def create_list(
        min_len=1,
        max_len=99,
        min_val=0,
        max_val=100
):
    return [random.randint(min_val, max_val) for x in range(random.randint(min_len, max_len))]


def solution(data, n):
    i = 0
    while i < len(data):
        matches = [i]
        id = data[i]
        for j in range(i+1, len(data)):
            if data[j] == id:
                matches.insert(0, j)
        if len(matches) > n:
            for match in matches:
                data.pop(match)
        else:
            i += 1
    return data


if __name__ == "__main__":
    data = create_list(
        min_len=1,
        max_len=30,
    )
    print(data)
    print(solution(data, 1))
    # print(solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1))
