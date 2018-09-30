__author__ = 'becca.elenzil'

class calculator():
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def add(self,num1,num2):
        return num1 + num2

    def subtract(self,num1,num2):
        return num1 - num2

    def multiply(self,num1,num2):
        return num1 * num2

class bamboozler():
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def add(self,num1,num2):
        return num1 + num2

    def subtract(self,num1,num2):
        return 2*num1 - num2


class lazyCalculator():

    def add(self,num1,num2,num3 = None,num4 = None):
        calc = calculator()
        if num3 == None and num4 == None:
            return calc.add(num1,num2)
        elif num4 == None:
            return "I need 2 or 4 arguments"
        else:
            sum1 = calc.add(num1,num2)
            sum2 = calc.add(num3,num4)
            final_sum = calc.add(sum1, sum2)
            return final_sum


lazyOne = lazyCalculator()
print(lazyOne.add(1,2,3,4))
