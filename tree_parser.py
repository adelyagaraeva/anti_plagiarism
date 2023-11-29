import ast


class NodeSorting(ast.NodeVisitor):

    def __init__(self):
        self.sizes = {}
        self.temp_res = 0

    def sorting_module(self, obj):
        if str(obj) in self.sizes.keys():
            return self.sizes[str(obj)]
        else:
            return 0

    def run(self, module):
        assert isinstance(module, ast.Module), "search must start from module"
        for functor in module.body:
            if not isinstance(functor, (ast.FunctionDef, ast.ClassDef)):
                continue

            self.generic_visit(functor)
            self.sizes[str(functor)] = self.temp_res
            self.temp_res = 0

        module.body = sorted(module.body, key=lambda x: self.sorting_module(x), reverse=True)

    def generic_visit(self, node):
        self.temp_res += 1
        super().generic_visit(node)


class Visitor(ast.NodeVisitor):

    from constants import builtin_functions, builtin_methods

    def __init__(self):
        self.data = []

    def generic_visit(self, node):
        self.data.append(node.__class__.__name__)
        super().generic_visit(node)

    def visit_Constant(self, node):
        self.data.append(node.value)
        super().generic_visit(node)

    def visit_Call(self, node):
        if hasattr(node.func, 'id') and node.func.id in self.builtin_functions:
            self.data.append(node.func.id)
        elif hasattr(node.func, 'attr') and node.func.attr in self.builtin_methods:
            self.data.append(node.func.attr)
        else:
            self.data.append(node.__class__.__name__)

        super().generic_visit(node)

    def visit_Import(self, node):
        for import_name in node.names:
            self.data.append(import_name.name)

    def visit_ImportFrom(self, node):
        self.data.append(node.module)


if __name__ == "__main__":
    tree = ast.parse("""
print(1)

def f(x):
    for i in range(x):
        print(i)
    return x - 1


def g(x):
    return x ** 2 - 4

def h(x, y):
    return x == y

for i in range(100):
    ke = f(x, y, z)
    ke **= 2
    print(ke)
""")
    visitor = Visitor()
    visitor.generic_visit(tree)
    node_sort = NodeSorting()
    node_sort.run(tree)
