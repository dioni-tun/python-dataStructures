# First class module built for the "Fraction" class.
class Fraction:

    # __initialize__ method
    def __init__(self, top, bottom):

        self.num = top
        self.den = bottom

    # __string__ method
    def __str__(self):

        return str(self.num) + "/" + str(self.den)

    # __add__ method:
    def __add__(self, otherFraction):

        newnum = self.num * otherFraction.den + self.den * otherFraction.num
        newden = self.den * otherFraction.den

        common = self.gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

    # __subtraction__ method:
    def __sub__(self, otherFraction):

        newnum = self.num * otherFraction.den - self.den * otherFraction.num
        newden = self.den * otherFraction.den

        common = self.gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

    # __multiply__ method:
    def __mul__(self, otherFraction):

        newnum = self.num * otherFraction.num
        newden = self.den * otherFraction.den

        common = self.gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

    # __division__ method:
    def __truediv__(self, otherFraction):

        newnum = self.num * otherFraction.den
        newden = self.den * otherFraction.num

        common = self.gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

    # __equality__ method:
    def __eq__(self, otherFraction):

        firstnum = self.num * otherFraction.den
        secondnum = otherFraction.num * self.den

        return firstnum == secondnum

    # __lessThan__ method:
    def __lt__(self, otherFraction):

        firstnum = self.num * otherFraction.den
        secondnum = otherFraction.num * self.den

        return firstnum < secondnum

    # __lessOrEqual__ method:
    def __le__(self, otherFraction):

        firstnum = self.num * otherFraction.den
        secondnum = otherFraction.num * self.den

        return firstnum <= secondnum

    # __greaterThan__ method:
    def __gt__(self, otherFraction):

        firstnum = self.num * otherFraction.den
        secondnum = otherFraction.num * self.den

        return firstnum > secondnum

    # __greaterOrEqual__ method:
    def __ge__(self, otherFraction):

        firstnum = self.num * otherFraction.den
        secondnum = otherFraction.num * self.den

        return firstnum >= secondnum

    # __notEqual__ method:
    def __ne__(self, otherFraction):

        firstnum = self.num * otherFraction.den
        secondnum = otherFraction.num * self.den

        return firstnum != secondnum
    
    #-------------------------------------------------------------------------
    # Helper methods
    def gcd(m, n):
        while m % n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm % oldn
        return n
