class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
'''
s=Stack()
print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())
'''

def parenChecker(par_string):
    parStack = Stack()
    for p in par_string:
        if p == "(":
            parStack.push(p)
        elif p == ")":
            try:
                parStack.pop()
            except:
                return False

    if parStack.isEmpty() == True:
        return True
    else:
        return False


#print("parenChecker('((()))') == True: ", parenChecker('((()))'))
#print("parenChecker('(()') == False: ", parenChecker('(()'))
#print("parenChecker('())') == False: ", parenChecker('())'))

def matches(closing, opening):
    openings = ["(","[","{"]
    closings = [")","]","}"]
    for i in range(len(openings)):
        if opening == openings[i]:
            index = i
    if closings[index] != closing:
        return False
    else:
        return True


def balSymChecker(par_string):
    parStack = Stack()
    for p in par_string:
        print(parStack.size())
        if p in ["(","[","{"]:
            parStack.push(p)
        elif p in [")","]","}"]:
            match = matches(p, parStack.peek())
            print(p, parStack.peek(),match)
            if match == True:
                try:
                    parStack.pop()
                except:
                    return False
            else:
                return False

    if parStack.isEmpty() == True:
        return True
    else:
        return False

#print("balSymChecker('{{([][])}()}') == True: ",balSymChecker('{{([][])}()}'))
#print("balSymChecker('[(()}]') == False: ",  balSymChecker('[(()}]'))

def divideby2(number):
    if number <= 0:
        print("Your decimal number must be greater than 0")

    binary_stack = Stack()
    while number > 0:
        print(number)
        remainder = number % 2
        binary_stack.push(str(remainder))
        number = number // 2
        binary_string = ''


    print(binary_stack.size())
    while binary_stack.isEmpty() != True:

        binary_string += binary_stack.pop()
        #print(binary_string)


    return binary_string


print(divideby2(233))


