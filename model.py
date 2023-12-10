from tree_visitors import *


class Model:

    @staticmethod
    def preprocessing(code):
        node_visitor = Visitor()
        node_sorter = NodeSorting()
        tree = ast.parse(code)
        node_sorter.run(tree)
        node_visitor.generic_visit(tree)

        return node_visitor.data

    @staticmethod
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

    def __init__(self, rep_cost=1, shift=0.05):
        self.rep_cost = rep_cost
        self.shift = shift

    def predict(self, code1, code2):
        try:
            return Model.wagner_fisher(code1, code2, self.shift, self.rep_cost)
        except SyntaxError:
            return 0
