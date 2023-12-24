
from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, n_matrix, m_matrix):
        self.matrix1 = n_matrix
        self.matrix2 = m_matrix


class Matrix:
    def __init__(self, m_matrix):
        self.matrix = deepcopy(m_matrix)

    # def solve(self, b_i):
    #
    #     return list(numpy.linalg.solve(self.matrix, b_i))
    def __str__(self):
        return "\n".join(["\t".join([str(i) for i in j]) for j in self.matrix])

    def size(self):
        return len(list(self.matrix)), len(list(self.matrix[0]))

    def __add__(self, other):
        # print("aboba")
        # m = self.size()
        # print(m)
        # print(self.size() == other.size(),self.size(),  other.size())
        if (self.size() != other.size()):
            raise MatrixError(self, other)
        for i in self.matrix:
            # print("aboba")
            if (len(i) != len(self.matrix[0])):
                raise MatrixError(self, other)
        for i in other.matrix:
            if (len(i) != len(other.matrix[0])):
                raise MatrixError(self, other)

        n = []
        for i in range(len(self.matrix)):
            tmp = []
            for j in range(len(self.matrix[0])):
                tmp.append(self.matrix[i][j] + other[i][j])
            n.append(tmp)
        return Matrix(n)

    def transpose(self):
        self.matrix = list(zip(*self.matrix))
        return Matrix(self.matrix)

    def transposed(self):
        return Matrix(list(zip(*self.matrix)))

    def __mul__(self, l):
        n = []
        if (type(l) == int or type(l) == float):
            for i in range(len(self.matrix)):
                tmp = []
                for j in range(len(self.matrix[0])):
                    tmp.append(self.matrix[i][j] * l)
                n.append(tmp)

            return Matrix(n)
        else:
            p = self.size()[1]
            # print(p)
            q = l.size()[0]
            # print(q)
            if (p != q):
                raise MatrixError(self, l)
            for i in range(len(list(self.matrix))):
                tmp = []
                for j in range(l.size()[1]):
                    s = 0
                    for k in range(q):
                        s += (self[i][k] * l[k][j])
                    tmp.append(s)
                n.append(tmp)
            return Matrix(n)

    def __rmul__(self, l):
        n = []
        for i in range(len(self.matrix)):
            tmp = []
            for j in range(len(self.matrix[0])):
                tmp.append(self.matrix[i][j] * l)
            n.append(tmp)

        return Matrix(n)

    def __getitem__(self, idx):
        return self.matrix[idx]


class SquareMatrix(Matrix):
    # def __init__(self, m_matrix):
    #     Matrix.__init__(self, m_matrix)

    def __pow__(self: Matrix, p: int) -> Matrix:
        n = Matrix(self)
        if (self.size()[0] != self.size()[1]):
            raise MatrixError(self, self)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                n.matrix[i][j] = 0
                if (i == j):
                    n.matrix[i][j] = 1
        else:
            res = n
            n = Matrix(self)
            while p:
                if p & 1:
                    res *= n
                n *= n
                p >>= 1

        return res


exec(stdin.read())
