import jellyfish


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


predicting_functions = {'lev': jellyfish.levenshtein_distance,
                        'dam-lev': jellyfish.damerau_levenshtein_distance,
                        'jaro': jellyfish.jaro_similarity,
                        'wag-fish':wagner_fisher}