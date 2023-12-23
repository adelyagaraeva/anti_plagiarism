from backend.tree_visitors import *
from backend.metrics import *
from itertools import product


class Model:
    """
    Model is used as an intermediate between
    """

    def __init__(self, parse_python, metrics: list):
        self.parse_python = parse_python
        self.metrics = metrics

    @staticmethod
    def read_file(name):
        with open(name, encoding='utf8') as f:
            file = f.read()
        return file

    def compare_all_files(self, filenames_to_compare):

        if self.parse_python:
            files_to_compare = {filename: Model.preprocessing(self.read_file(filename)) for filename in filenames_to_compare}
        else:
            files_to_compare = {filename: self.read_file(filename) for filename in filenames_to_compare}

        files_pair = [(pair[0], pair[1]) for pair in product(filenames_to_compare, repeat=2) if pair[0] < pair[1]]
        results = {}

        for filename_1, filename_2 in files_pair:
            file_1 = files_to_compare[filename_1]
            file_2 = files_to_compare[filename_2]
            if self.parse_python:
                alphabet = {word: chr(40 + index) for index, word in enumerate(set(file_1).union(set(file_2)))}
            else:
                alphabet = None

            result = [self.predict(file_1, file_2, predicting_functions[metric], alphabet) for metric in self.metrics]
            results[(filename_1, filename_2)] = result

        return results

    @staticmethod
    def preprocessing(code):
        node_visitor = Visitor()
        node_sorter = NodeSorting()
        tree = ast.parse(code)
        node_sorter.run(tree)
        node_visitor.generic_visit(tree)

        return node_visitor.data

    @staticmethod
    def predict(code1, code2, metric, alphabet):
        try:
            if alphabet:
                code1 = ''.join(alphabet[el] for el in code1)
                code2 = ''.join(alphabet[el] for el in code2)
            return metric(code1, code2)
        except SyntaxError:
            return 0
