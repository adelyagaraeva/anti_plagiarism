from backend.tree_visitors import *
from backend.metrics import *


class Model:

    @staticmethod
    def preprocessing(code):
        node_visitor = Visitor()
        node_sorter = NodeSorting()
        tree = ast.parse(code)
        node_sorter.run(tree)
        node_visitor.generic_visit(tree)

        return node_visitor.data

    def __init__(self):
        pass

    @staticmethod
    def predict(code1, code2, function, alphabet):
        try:
            if alphabet:
                code1 = ''.join(alphabet[el] for el in code1)
                code2 = ''.join(alphabet[el] for el in code2)
            return function(code1, code2)
        except SyntaxError:
            return 0
