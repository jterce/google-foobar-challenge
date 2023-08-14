def solution(n):
    i = int(n)
    b = bin(i)[2:]
    r = list(reversed(b))
    ops = 0
    ones = 0
    for c in range(len(r) - 1):
        if r[c] == '0':
            # div
            ops += 1
        else:
            ones += 1
            if r[c + 1] == '0':
                if ones < 2:
                    # minus + div
                    ops += 2
                else:
                    # plus + divs for each resulting 0
                    r[c + 1] = '1'
                    ops += 1 + ones
                ones = 0

    if ones == 1:
        ops += 2
    elif ones > 1:
        ops += 1 + ones + 1

    return ops


if __name__ == "__main__":
    results = (
        ('0', 1),
        ('1', 0),
        ('2', 1),
        ('3', 2),
        ('4', 2),
        ('5', 3),
        ('6', 3),
        ('7', 4),
        ('8', 3),
        ('9', 4),
        ('10', 4),
        ('11', 5),
        ('12', 4),
        ('13', 5),
        ('14', 5),
        ('15', 5),
        ('16', 4),
        ('17', 5),
        ('18', 5),
        ('19', 6),
        ('20', 5),
        ('21', 6),
        ('22', 6),
        ('23', 6),
        ('24', 5),
        ('25', 6),
        ('26', 6),
        ('27', 7),
        ('28', 6),
        ('29', 7),
        ('30', 6),
        ('31', 6),
        ('32', 5),
        ('1083', 13)
    )
    for n, target in results:
        sol = solution(n)
        print(n, target, sol, sol == target)

    # sol3 = solution('9'*310)
    # print(sol3)
