__author__ = 'becca.elenzil'

class calculator():
    def __init__(self):
        self.name = "calculator"

    def add(self,num1,num2):
        return num1 + num2

    def subtract(self,num1,num2):
        return num1 - num2

    def multiply(self,num1,num2):
        return num1 * num2


class lazyCalculator(calculator):
    def __init__(self):
        calculator.__init__(self)

    def add(self,num1,num2,num3 = None,num4 = None):
        if num3 == None:
            return super(calculator,self).add(num1,num2)
        else:
            sum1 = self.add(num1,num2)
            sum2 = self.add(num3,num4)
            return self.add(sum1,sum2)

class bamboozler():
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def add(self,num1,num2,num3 = None,num4 = None):
        if num3 == None and num4 == None:
            self.num1 = num1
            self.num2 = num2
            return num1 + num2
        elif num4 == None:
            return "I need 2 or 4 arguments"
        else:
            calc = calculator()
            sum1 = calc.add(num1,num2)
            sum2 = calc.add(num3,num4)
            return sum1 + sum2


lazyOne = lazyCalculator()
print lazyOne.add(1,2)



