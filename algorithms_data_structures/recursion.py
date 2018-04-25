def distance(s1, s2):
    '''Return the distance between two strings,
       each of which is of length four.'''
    editDist = 0
    if s1[0] != s2[0]:
        editDist = editDist + 1
    if s1[1] != s2[1]:
        editDist = editDist + 1
    if s1[2] != s2[2]:
        editDist = editDist + 1
    if s1[3] != s2[3]:
        editDist = editDist + 1
    return editDist

print("distance: ",distance('spim','spam'))

def simpleDistance(s1, s2):
    '''Takes two strings of the same length and returns the
       number of positions in which they differ.'''
    if len(s1) == 0:     # len(s2) is also 0 since strings
                         # have the same length
        return 0         # base case
    elif s1[0] != s2[0]: # recursive step, case 1
        return 1 + simpleDistance(s1[1:], s2[1:])
    else:                # recursive step, case 2:
                         #   s1[0] == s2[0]
        return simpleDistance(s1[1:], s2[1:])

#print(simpleDistance('spim','spam'))

def factorial(n):
    '''Recursive function for computing
    the factorial of n.'''

    if n == 1:
        return 1
    else:
        result = n * factorial(n-1)
        return result

#print (factorial(4))


def demo(x):
    r = f(x+6) + x
    return r

def f(x):
    r = g(x-1)
    x = 1
    return r + x

def g(x):
    r = x + 10
    return r


def reverse(string):
    '''Takes a string as an argument and returns
       its reversal.'''
    if string == '':            # Is the string empty?
        return ''               # If so, reversing it is easy!
    else:
        firstSymbol = string[0] # Hold on to the first symbol
        return reverse(string[1:]) + firstSymbol

def subset(capacity, items):
    '''Given a suitcase capacity and a list of items
       consisting of positive numbers, returns a number
       indicating the largest sum that can be made from a
       subset of the items without exceeding the capacity.'''

    if capacity == 0 or items == []:
        return 0
    elif items[0] > capacity:
        return subset(capacity, items[1:])
    else:
        loseIt = subset(capacity, items[1:])
        useIt = items[0] + subset(capacity - items[0], items[1:])
        return max(loseIt, useIt)

#print(subset(4, [1,2,3]))


def distance(first, second):
    '''Returns the edit distance between first and second.'''

    if first == '':
        return len(second)
    elif second == '':
        return len(first)
    elif first[0] == second[0]:
        return distance(first[1:], second[1:])
    else:
        substitution = 1 + distance(first[1:], second[1:])
        deletion = 1 + distance(first[1:], second)
        insertion = 1 + distance(first, second[1:])
        return min(substitution, deletion, insertion)


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
#print("fib(6): ",fib(6))
def fact(n):
    '''recursive function for computing factorial of n'''
    if n <= 1:
        return 1
    else:
        return n*fact(n-1)

#print(fact(5))
def exp(b,n):
    if n < 1:
        return 1
    else:
        return b*exp(b,n-1)

#print(exp(5,2))
def mult(b,n):
    if n < 1:
        return 0
    else:
        return b+mult(b,n-1)

print(mult(4,3))
def find_palindrome(word):
    if len(word) == 0 or len(word) == 1:
        return True
    elif word[0].lower() == word[-1].lower():
        return find_palindrome(word[1:-1])
    else:
        return False

print(find_palindrome('123321'))
