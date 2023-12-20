from tree_visitors import *
from metrics import *


class Model:

    @staticmethod
    def preprocessing(code):
        node_visitor = Visitor()
        node_sorter = NodeSorting()
        tree = ast.parse(code)
        node_sorter.run(tree)
        node_visitor.generic_visit(tree)

        return node_visitor.data

    def __init__(self, rep_cost=1, shift=0.05):
        self.rep_cost = rep_cost
        self.shift = shift

    def predict(self, code1, code2):
        try:
            return wagner_fisher(code1, code2, self.shift, self.rep_cost)
        except SyntaxError:
            return 0
