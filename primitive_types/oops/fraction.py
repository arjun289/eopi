def gcd(a, b):
    if b % a == 0:
        return a
    else:
        return gcd(b % a, a)


class Fraction:
    def __init__(self, num, den):
        if type(num) == int and type(den) == int:
            self.num = num
            self.den = den
        else:
            raise Exception("Numerator/denominator is not int!")

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, f2):
        newnum = self.num * f2.den + self.den * f2.num
        newden = self.den * f2.den

        common = gcd(newnum, newden)

        return Fraction(newnum/common, newden/common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum


if __name__ == "__main__":
    frcn = Fraction(3, 5)
    print(frcn)

    f1 = Fraction(1, 4)
    f2 = Fraction(1, 2)
    f3 = f1 + f2
    print(f3)
    f4 = Fraction(2, 'x')
