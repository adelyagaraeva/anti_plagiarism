from sys import stdin
from copy import deepcopy

class MatrixError(BaseException):
    def __init__(self, matrix, other):
        self.matrix2 = other
        self.matrix1 = matrix

class Matrix:
    def __init__(self, list):
        self.matrix = deepcopy(list)

    def __str__(self):
        result = ''
        for i in self.matrix:
            for j in i:
                result += str(j)
                result += '\t'
            result = result[:-1]
            result += '\n'
        result = result[:-1]
        return result

    def size(self):
        return (len(self.matrix), len(self.matrix[0]))

    def __add__(self, other):
        result = deepcopy(self.matrix)
        if (self.size() == other.size()):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    result[i][j] += other.matrix[i][j]
            return Matrix(result)
        else:
             raise MatrixError(self, other)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = deepcopy(self.matrix)
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    result[i][j] *= other
            return Matrix(result)
        elif isinstance(other, Matrix):
            result = [[0] * len(other.matrix[0]) for i in range(len(self.matrix))]
            if self.size()[1] == other.size()[0]:
                for i in range(len(self.matrix)):
                    for j in range(len(other.matrix[0])):
                        for k in range(len(self.matrix[0])):
                            a = (self.matrix[i][k] * other.matrix[k][j])
                            result[i][j] += a
                return Matrix(result)
            else:
                raise MatrixError(self, other)

    __rmul__ = __mul__

    def transpose(self):
        self.matrix = [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]
        return Matrix(self.matrix)

    @staticmethod
    def transposed(other):
        return Matrix([[other.matrix[j][i] for j in range(len(other.matrix))] for i in range(len(other.matrix[0]))])

    def solve(self, b_column):
        full_matrix = [[0.0] * (self.size()[1] + 1) for i in range(self.size()[0])]
        for i in range(self.size()[0]):
            for j in range(self.size()[1] + 1):
                if j < self.size()[1]:
                    full_matrix[i][j] = self.matrix[i][j]
                else:
                    full_matrix[i][j] = b_column[i]
        num_rows = self.size()[0]
        num_col = self.size()[1] + 1

        for i in range(num_rows):
            for j in range(i, num_rows):
                if full_matrix[i][i] == 0.0:
                        raise Exception()
                if full_matrix[j][i] != 0.0:
                    if i != j:
                        full_matrix[j], full_matrix[i] = full_matrix[i], full_matrix[j]
                    break
            n = full_matrix[i][i]
            if n != 0:
                for j in range(i, num_col):
                    full_matrix[i][j] /= n
                for j in range(i + 1, num_rows):
                    c = full_matrix[j][i]
                    for k in range(i, num_col):
                        m = full_matrix[i][k]
                        l = full_matrix[j][k]
                        full_matrix[j][k] -= c * m

        answer = [0.0] * (num_col - 1)
        for i in range(num_col - 2, -1, -1):
            answer[i] = full_matrix[i][num_col - 1]
            for j in range(i):
                full_matrix[j][num_col - 1] -= answer[i]*full_matrix[j][i]
        return (answer)


class SquareMatrix(Matrix):
    def __pow__(self, n):
        def power(self, n):
            if n == 0:
                result = [[0] * len(self.matrix[0]) for i in range(len(self.matrix))]
                for i in range(len(self.matrix[0])):
                    result[i][i] = 1
                return Matrix(result)
            elif n == 1:
                return self
            elif n % 2 != 0:
                return self * power(self, n - 1)
            elif n % 2 == 0:
                return power(self * self, n / 2)
        return power(self, n)

exec(stdin.read())