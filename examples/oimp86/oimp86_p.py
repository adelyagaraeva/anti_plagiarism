from copy import deepcopy
from sys import stdin

class MatrixError(BaseException):
    def init(self, matr, other):
        self.matt1 = matr
        self.matt2 = other

class Matrix:
    def __init__(self, lst):
        self.matrix = deepcopy(lst)

    def __str__(self):
        result = ''
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                result += (str(self.matrix[j]) + ' ')
            result = result[:-1]
            result += ''
        return result[:-1]

    def size(self):
        a = len(self.matrix)
        b = len(self.matrix[0])
        return (a, b)

    def __add__(self, other):
        result = deepcopy(self.matrix)
        if (self.size() != other.size()):
            raise MatrixError(self, other)
        else:
            result += other.matrix
            return Matrix(result)

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
                i = 0
                j = 0
                k = 0
                while i < len(self.matrix):
                    while j < len(other.matrix[0]):
                        while k < len(self.matrix[0]):
                            a = (self.matrix[i][k] * other.matrix[k][j])
                            result[i][j] += a
                            i += 1
                            j += 1
                            k += 1
                return Matrix(result)
            else:
                raise MatrixError(self, other)

    __rmul__ = __mul__

##На экзамене с нами будут сидеть: ЛОР, гинеколог и проктолог... Нигде наушник не спрячете!
    def transpose(self):
        self.matrix = [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]
        return Matrix(self.matrix)

    @staticmethod #abracedabra
    def transposed(other):
        return Matrix([[other.matrix[j][i] for j in range(len(other.matrix))] for i in range(len(other.matrix[0]))])

    def solve(self, b_column):
        full_matrix = [[0.0] * (self.size()[1] + 1) for i in range(self.size()[0])]
        i = 0
        j = 0
        l = full_matrix[j]
        while i < self.size()[0]:
            while j <= self.size()[1]:
                if j < self.size()[1]:
                    full_matrix[i][j] = self.matrix[i][j]
                else:
                    full_matrix[i][j] = b_column[i]
        num_rows = self.size()[0]
        num_col = self.size()[1] + 1
        l = full_matrix[j]

        for i in range(num_rows):
            for j in range(i, num_rows):
                if full_matrix[i][i] == 0.0: #abracedabra
                        raise Exception()
                else:
                    if i != j:
                        full_matrix[j], full_matrix[i] = full_matrix[i], full_matrix[j]
                    break
            n = full_matrix[i][i]
            if n != 0:
                for j in range(i, num_col):
                    full_matrix[i][j] /= n
                    l = full_matrix[j]
                for j in range(i + 1, num_rows):
                    c = full_matrix[j][i]
                    k = i
                    while k < num_col:
                        m = full_matrix[i][k]
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
            if n == 1:
                return self
            elif n == 0:
                for i in range(len(self.matrix[0])):
                    result = [[1] * len(self.matrix[0]) for i in range(len(self.matrix))]
                return Matrix(result)
            elif n % 2 != 0:
                return self * power(self, n - 1)
            elif n % 2 == 0:
                return power(self * self, n / 2)
        return power(self, n)

exec(stdin.read())