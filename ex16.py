class Fraction(object):
    def __init__(self,num,denom):
        self.num = num
        self.denom = denom

    def __str__(self):
        return "Numerator:" + str(self.num) + ", Denominator:" + str(self.denom)

    def __add__(self,other):
        if self.denom == other.denom:
            return Fraction(self.num + other.num, self.denom)
        else:
            newDenom = self.denom * other.denom
            self.num = self.num * other.denom
            other.num = other.num * self.denom
            return Fraction(self.num + other.num, newDenom)


    def __sub__(self,other):
        if self.denom == other.denom:
            return Fraction(self.num - other.num, self.denom)
        else:
            newDenom = self.denom * other.denom
            self.num = self.num * other.denom
            other.num = other.num * self.denom
            return Fraction(self.num - other.num, newDenom)


    def __mul__(self,other):
        return Fraction(self.num * other.num, self.denom * other.denom)


    def __truediv__(self,other):
        return Fraction(self.num * other.denom, self.denom * other.num)

    def inverse(self):
        self.num, self.denom = self.denom, self.num
        return Fraction(self.num, self.denom)


f1 = Fraction(1,2)
f2 = Fraction(2,3)

print("+ " + str(f1 + f2))

f3 = Fraction(1,2)
f4 = Fraction(1,6)

print("- " + str(f3 - f4))

f5 = Fraction(1,4)
f6 = Fraction(2,3)

print("* " + str(f5 * f6))

f7 = Fraction(5,7)
f8 = Fraction(10,15)

print("/ " + str(f7 / f8))

f9 = Fraction(2,5)

print("*-1 " + str(f9.inverse()))