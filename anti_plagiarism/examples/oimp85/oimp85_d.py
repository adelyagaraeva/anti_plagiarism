
from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, n_matrix, m_matrix):
        self.matrix1 = n_matrix
        self.matrix2 = m_matrix


class Matrix:
    def __init__(self, m_matrix):
        self.matrix = deepcopy(m_matrix)

    def solve(self, b_i):
        for i in range(len(self.matrix)):
            self.matrix[i].append(-b_i[i])
        ans = []
        for j in range(len(self.matrix)):
            first_non_zero = 0
            for i in range(len(self.matrix)):
                if self.matrix[i][0] != 0:
                    first_non_zero = i
                    break
            tmp = []
            for i in self.matrix[first_non_zero][1:]:
                tmp.append(-1.0 * i / self.matrix[first_non_zero][0])
            ans.append(tmp)
            self.matrix.pop(first_non_zero)
            for i in self.matrix:
                for j in range(len(ans[len(ans) - 1])):
                    i[j + 1] += i[0] * ans[len(ans) - 1][j]
                i.pop(0)
        ans.reverse()
        res = [ans[0][0]]
        for i in range(1, len(ans)):
            m_sum = ans[i][len(ans[i]) - 1]
            for j in range(0, len(ans[i]) - 1):
                m_sum += ans[i][j] * res[-1 - j]
            res.append(m_sum)
        res.reverse()
        return res


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

exec(stdin.read())
