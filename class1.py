from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, m):
        self.m = deepcopy(m)

    def __str__(self):
        st = ''
        for i in range(len(self.m)):
            for j in range(len(self.m[i])):
                if j != len(self.m[i]) - 1:
                    st += str(self.m[i][j]) + '\t'
                else:
                    st += str(self.m[i][j])
            if i != len(self.m) - 1:
                st += '\n'
        return st

    def size(self):
        c = 0
        p = 0
        for i in range(len(self.m)):
            c += 1
        for j in range(len(self.m[0])):
            p += 1
        return c, p

    def __add__(self, other):
        for i in range(len(self.m)):
            for j in range(len(self.m[i])):
                result = [[self.m[i][j] + other.m[i][j]
                           for j in range(len(self.m[0]))]
                          for i in range(len(self.m))]
        return result

    def __mul__(self, a):
        for i in range(len(self.m)):
            for j in range(len(self.m[i])):
                result = [[self.m[i][j] * a
                           for j in range(len(self.m[0]))]
                          for i in range(len(self.m))]
        return result

    def __rmul__(self, a):
        for i in range(len(self.m)):
            for j in range(len(self.m[i])):
                result = [[a * self.m[i][j]
                           for j in range(len(self.m[0]))]
                          for i in range(len(self.m))]
        return result


exec(stdin.read())
