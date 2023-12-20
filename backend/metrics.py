def wagner_fisher(code1: list, code2: list, shift=0.05, rep_cost=1):
    prev_line = [j for j in range(len(code2))]
    new_line = [0] * len(code2)
    for i in range(len(code1)):
        for j in range(len(code2)):
            if j == 0:
                new_line[0] = i * 1
            else:
                new_line[j] = min(prev_line[j] + 1,
                                  new_line[j - 1] + 1,
                                  prev_line[j - 1] + rep_cost * (code1[i] != code2[j]))
        prev_line, new_line = new_line, [0] * len(code2)
    try:
        return min(1.0, shift + 1 - prev_line[-1] / (rep_cost * max(len(code2), len(code1))))
    except IndexError:
        if len(code1) == len(code2):
            return 1
        return 0


def levenshtein_distance(code1, code2):
    m = len(code1)
    n = len(code2)
    d = [[0] * (n + 1) for i in range(m + 1)]

    for i in range(1, m + 1):
        d[i][0] = i

    for j in range(1, n + 1):
        d[0][j] = j

    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if code1[i - 1] == code2[j - 1]:
                cost = 0
            else:
                cost = 1
            d[i][j] = min(d[i - 1][j] + 1,
                          d[i][j - 1] + 1,
                          d[i - 1][j - 1] + cost)

    return d[m][n]
