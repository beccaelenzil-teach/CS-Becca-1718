from stacks import Stack

def parenChecker(parenList):
    parenStack = Stack()

    for paren in parenList:
        if paren == "(":
            parenStack.push(paren)
        else:
            try:
                parenStack.pop()
            except:
                return False

    if parenStack.isEmpty():
        return True
    else:
        return False

def balSymChecker(parenList):
    parenStack = Stack()
    openers = "({["
    closers = ")}]"

    for paren in parenList:
        if paren in openers:
            parenStack.push(paren)
        elif paren in closers:
            if parenStack.isEmpty:
                return False
            else:
                matches(paren,parenStack)

    if parenStack.isEmpty():
        return True
    else:
        return False


def matches(paren,parenStack):

    openers = "({["
    closers = ")}]"

    for i in range(3):
        if parenStack.pop() == openers[i] and paren != closers[i]:
            return False
        elif paren == closers[i]:
            try:
                parenStack.pop()
            except:
                return False


print(balSymChecker('{{([][])}()}'))
print(balSymChecker('[{()]'))
print(balSymChecker('[{)]'))


def divideByTwo(dec):
    s = Stack()
    b = " "

    while dec > 0:
        rem = dec % 2
        s.push(rem)
        dec = dec // 2

    while s.isEmpty() == False:
        b += str(s.pop())

    return b

#print divideByTwo(233)



