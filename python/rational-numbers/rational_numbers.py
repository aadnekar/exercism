from __future__ import division


class Rational(object):
    def __init__(self, numer, denom):
        _gcd = gcd(numer, denom)
        self.numer = numer/_gcd
        self.denom = denom/_gcd

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        numer = (self.numer * other.denom + other.numer * self.denom)
        denom = self.denom * other.denom
        return self.__class__(numer, denom)

    def __sub__(self, other):
        numer = (self.numer * other.denom - other.numer * self.denom)
        denom = self.denom * other.denom
        return self.__class__(numer, denom)

    def __mul__(self, other):
        return self.__class__(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return self.__class__(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        return self.__class__(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if power == 0:
            return self.__class__(1,1)
        elif power > 0:
            return self.__class__(self.numer ** power, self.denom ** power)
        else:
            return self.__class__(self.denom ** power, self.numer ** power)

    def __rpow__(self, base):
        if self.numer == 0:
            return 1.0
        return base ** (self.numer / self.denom)

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x