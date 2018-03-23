__author__ = 'becca.elenzil'


matrix = [[1,1,1,1],[2,2,2,2],[3,3,3,3]]

n = len(matrix)
m = len(matrix[0])

a = n-1
b = n-1
c = 0
d = 0

i = 0
j = 0
k = n-1

while a < (n-1)//2:
    while i < a:
        print(matrix[i][j])
        i+=1
    a-=1

    while j < b:
        print(matrix[i][j])
        j+=1
    a-=1



print(n)
print(m)