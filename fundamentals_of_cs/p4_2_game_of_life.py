import random

def createOneRow(width):
        """ returns one row of zeros of width "width"...
         You should use this in your
         createBoard(width, height) function """
        row = []
        for col in range(width):
            row += [1]
        return row

def createBoard(width, height):
        """ returns a 2d array with "height" rows and "width" cols """
        A = []
        for row in range(height):
            A += [createOneRow(width)]    # What do you need to add a whole row here?
        return A



def printBoard(A):
    """print game of life board"""
    for row in A:
        line = ''
        for col in row:
            line += str(col)
        print(line)



def diagonalize(width,height):
    """ creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells.
    """
    A = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0

    return A

def randomCells(width, height):
        """ creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells.
        """
        A = createBoard(width, height)
        for row in range(height):
            for col in range(width):
                if row == 0 or row == (height - 1) or col == 0 or col == (width - 1):
                    A[row][col] = 0
                else:
                    A[row][col] = random.choice([0, 1])
        return A


def copy(A):
        height = len(A)
        width = len(A[0])
        newA = createBoard(width,height)
        for row in range(height):
            for col in range(width):
                newA[row][col] = A[row][col]
        return newA
        #screen.fill(BLACK)

def innerReverse(A):
    """create a board with the reverse 0s and 1s"""
    height = len(A)
    width = len(A[0])
    newA = copy(A)
    for row in range(1,height-1):
        for col in range(1,width-1):
            if newA[row][col] == 0:
                newA[row][col] = 1
            else:
                newA[row][col] = 0
    return newA

def countNeighbors(row,col,A):
        count = 0
        count += A[row][col+1]
        count += A[row][col-1]
        count += A[row + 1][col - 1]
        count += A[row + 1][col]
        count += A[row + 1][col+1]
        count += A[row - 1][col - 1]
        count += A[row - 1][col]
        count += A[row - 1][col + 1]
        return count

def next_life_generation(A):
        height = len(A)
        width = len(A[0])
        newA = copy(A)
        for row in range(1,height-1):
            for col in range(1,width-1):
                count = countNeighbors(row,col,A)
                if count < 2:
                    newA[row][col] = 0
                elif count > 3:
                    newA[row][col] = 0
                elif count == 3:# and A[row][col] == 0:
                    newA[row][col] = 1
        static = (newA == A)
        #return [static,newA]
        return newA
'''
A = [ [0,0,0,0,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,0,0,0]]

printBoard(A)

A2 = next_life_generation(A)
print ' '
printBoard(A2)

A3 = next_life_generation(A2)
print ' '
printBoard(A3)
'''
