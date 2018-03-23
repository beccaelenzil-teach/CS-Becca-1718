__author__ = 'becca.elenzil'

# use lists
x = None
for i in range(6, 0, -1):
  x = [i, x]

# use tuples
y = None
for i in range(6, 0, -1):
  y = (i, y)

# use dicts
z = None
for i in range(6, 0, -1):
  z = {'data': i, 'next': z}

#print z

# use objects
class Node:
  def __init__(self, data, next):
    self.data = data
    self.next = next

a = None
for i in range(6, 0, -1):
  a = Node(i, a)

firstNodeVal = a.data
firstNode = a
secondNode = firstNode.next
secondNodeVal = secondNode.data

#print firstNodeVal, secondNodeVal

myList = (1, (2, (3, (4, (5, None)))))

def sumList(node, subtotal):
  if not node:
    return subtotal
  else:
    print node[1]
    return sumList(node[1], subtotal + node[0])

total = sumList(myList, 0)
print total