__author__ = 'becca.elenzil'

fuelNeeded = 42.0/1000
tank1 = 36.0/1000
tank2 = 6.0/1000
"""
print tank1 + tank2 >= fuelNeeded

print fuelNeeded
print tank1
print tank2

print tank1 + tank2
"""

class Rational:
    def __init__(self,num,denom):
        self.numerator = num
        self.denominator = denom

    def __add__(self,other):
        newNumerator = self.numerator * other.denominator + \
                    self.denominator * other.numerator
        newDenominator = self.denominator * other.denominator
        return Rational(newNumerator,newDenominator)

    def __eq__(self,other):
        return self.numerator*other.denominator == self.denominator*other.numerator

    def __ge__(self, other):
        return self.numerator * other.denominator >= \
           self.denominator * other.numerator

    def __str__(self):
        return str(self.numerator)+"/"+str(self.denominator)

    def __repr__(self):
        return str(self.numerator)+"/"+str(self.denominator)


    def simplify(self):
        """
        This method should return the rational number in simplest for in place.
        For example, if r = Rational(10,20), after calling r.simplify(), r should be equal to Rational(1,2)
        """
        if self.denominator <= self.numerator:
            high = self.numerator
        else:
            high = self.denominator

        for n in range(2,high):
            while self.numerator % n == 0 and self.denominator % n == 0:
                self.numerator /= n
                self.denominator /= n

    def gcf(self,a,b):
        """
        finds the greatest common factor
        """
        if self.numerator >= self.denominator:
            a = self.numerator
            b = self.denominator
        else:
            b = self.numerator
            a = self.denominator

"""
        if self.numerator % self.denominator == 0:
                return b
            else:
                return self.gcf(self.denominator, self.numerator % self.denominator)
        else:
            #if a % b == 0:
            #    return b
            #else:
            #    return self.gcf(a, b % a)

r = Rational(46,100)
print r.gcf()






def foo():
    r = Rational(1,3)
    for i in range(10):
        bar(r)
        print r

def bar(number):
    number.numerator += 1


fuelNeeded = Rational(42,1000)
tank1 = Rational(36,1000)
tank2 = Rational(6,1000)

total = tank1+tank2

print total >= fuelNeeded

print str(fuelNeeded)


r1 = Rational(1,2)
r2 = Rational(1,2)
print r1 == r2


r = Rational(20,5)
r.simplify()
print r
print r.denominator
"""