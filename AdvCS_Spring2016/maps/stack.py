__author__ = 'becca.elenzil'


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


def parChecker(parenList):
    s = Stack()
    for paren in parenList:
        if paren == "(":
            s.push(paren)
        elif paren == ")":
            try:
                s.pop()
            except:
                return False

    if s.size() == 0:
        return True
    else:
        return False

print "parChecker('((()))') == True: ", parChecker('((()))')
print "parChecker('())') == False: ", parChecker('())')


