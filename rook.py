import sys


class Poly:
    def __init__(self, _coeff = ()):
        if _coeff == ():
            self.coeff = (0)
        else:
            self.coeff = _coeff

    def __add__(self, other):
        first = self.coeff
        sec = other.coeff
        res = []
        for index in range(min(len(first), len(sec))):
            res.append(first[index] + sec[index])
        if len(first) > len(sec):
            for index in range(len(sec), len(first)):
                res.append(first[index])
        else:
            for index in range(len(first), len(sec)):
                res.append(sec[index])
        return Poly(tuple(res))

    def const_mul(self, pow, const):
        res = [0] * pow
        first = self.coeff
        for elem in first:
            res.append(elem * const)
        return Poly(tuple(res))

    def __mul__(self, other):
        res = Poly((0, ))
        sec = other.coeff
        for index in range(len(sec)):
            res = res + Poly.const_mul(self, index, sec[index])
        return res

    def str(self):
        res = ''
        first = self.coeff
        for index in range(len(first) - 1, -1, -1):
            if first[index] != 0:
                if index != 0 and index != 1:
                    if abs(first[index]) == 1:
                        if first[index] == 1:
                            res += ' + ' + 'x' + '^' + str(index)
                        if first[index] == -1:
                            res += ' - ' + 'x' + '^' + str(index)
                    else:
                        if first[index] > 0:
                            res += ' + ' + str(first[index]) + 'x' + '^' + str(index)
                        else:
                            res += ' - ' + str(first[index]) + 'x' + '^' + str(index)
                elif index == 0:
                    if first[index] < 0:
                        res += ' - ' + str(first[index])
                    else:
                        res += ' + ' + str(first[index])
                else:
                    if abs(first[index]) == 1:
                        if first[index] == 1:
                            res += ' + ' + 'x'
                        if first[index] == -1:
                            res += ' - ' + 'x'
                    else:
                        if first[index] > 0:
                            res += ' + ' + str(first[index]) + 'x'
                        else:
                            res += ' - ' + str(first[index]) + 'x'

        if res[0: 3] == ' + ':
            res = res[3:]
        if res[0: 3] == ' - ':
            res = '-' + res[3:]
        return res


def rook(m, n):
    if m == 1 or n == 1:
        return Poly((1, m * n))
    else:
        return rook(m - 1, n) + Poly((0, n)) * rook(m - 1, n - 1)


sys.setrecursionlimit(1000000000)
frook = open('rook.tex', 'w')
for m in range(1, 20):
    for n in range(1, 20):
        print('$$f_{' + str(m) + ', ' + str(n) + '}(x): ' + Poly.str(rook(m, n)) + '.$$ ', file = frook)
frook.close()





