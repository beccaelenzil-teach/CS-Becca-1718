__author__ = 'becca.elenzil'


class Board:
    """ a datatype representing a C4 board
        with an arbitrary number of rows and cols
    """

    def __init__( self, width, height ):
        """ the constructor for objects of type Board """
        self.width = width
        self.height = height
        W = self.width
        H = self.height
        self.data = [ [' ']*W for row in range(H) ]

        # we do not need to return inside a constructor!


    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        H = self.height
        W = self.width
        s = ''   # the string to return
        for row in range(0,H):
            s += '|'
            for col in range(0,W):
                s += self.data[row][col] + '|'
            s += '\n'



        s += (2*W+1) * '-'    # bottom of the board
        s += '\n'
        for i in range(W):
            n = i % 10
            s += ' ' + str(n)

        return s       # the board is complete, return it

    def addMove(self, col, ox):

        """adds and 'X' or an 'O' to a specified column"""
        H = self.height
        W = self.width

        rowReverse = range(0,H)
        rowReverse.reverse()

        for row in rowReverse:
            if self.data[row][col] == ' ':
                self.data[row][col] = ox
                return self.data

    def clear(self):
        """clears the board"""
        W = self.width
        H = self.height
        self.data = [ [' ']*W for row in range(H) ]

    def setBoard( self, moveString ):
        """ takes in a string of columns and places
        alternating checkers in those columns,
        starting with 'X'

        For example, call b.setBoard('012345')
        to see 'X's and 'O's alternate on the
        bottom row, or b.setBoard('000000') to
        see them alternate in the left column.

        moveString must be a string of integers
        """
        nextCh = 'X'   # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)

            if nextCh == 'X':
                nextCh = 'O'
            else:
                nextCh = 'X'

    def allowsMove(self, col):
        """This method should return True if the calling object (of type Board) does allow a move into column c.

        It returns False if column c is not a  legal column number for the calling object.

        It also returns False if column c is full.
        """

        W = self.width

        if col < 0 or col >= W:
            #print "That column is not on the board"
            return False
        elif self.data[0][col] != ' ':
            #print "That column is full"
            return False
        else:
            return True

    def isFull(self):
        """returns true if board is totally full"""
        W = self.width
        H = self.height
        for col in range(W):
            if self.allowsMove(col) == True:
                return False
        return True

    def delMove(self,col):
        """remove top checker from a col"""
        """adds and 'X' or an 'O' to a specified column"""
        H = self.height
        W = self.width

        for row in range(0,H):
            if self.data[row][col] != ' ':
                self.data[row][col] = ' '
                return self.data

    def winsFor(self, ox):
        """checks for a win for "X" or "O"""
        H = self.height
        W = self.width
        D = self.data
        # check for horizontal wins
        for row in range(0,H):
            for col in range(0,W-3):
                if D[row][col] == ox and \
                   D[row][col+1] == ox and \
                   D[row][col+2] == ox and \
                   D[row][col+3] == ox:
                    return True

            for col in range(W-1,2,-1):
                if D[row][col] == ox and \
                   D[row][col-1] == ox and \
                   D[row][col-2] == ox and \
                   D[row][col-3] == ox:
                    return True

        #check for vertical wins
        for col in range(0,W):
            for row in range(0,H-3):
                if D[row][col] == ox and \
                   D[row+1][col] == ox and \
                   D[row+2][col] == ox and \
                   D[row+3][col] == ox:
                    return True

            for row in range(H-1,2,-1):
                if D[row][col] == ox and \
                   D[row-1][col] == ox and \
                   D[row-2][col] == ox and \
                   D[row-3][col] == ox:
                    return True

        #check for diagonal negative slope
        for col in range(0,W-3):
            for row in range(0,H-3):
                if D[row][col] == ox and \
                   D[row+1][col+1] == ox and \
                   D[row+2][col+2] == ox and \
                   D[row+3][col+3] == ox:
                    return True

        #check for diagonal positive slope
        for col in range(0,W-3):
            for row in range(H-1,2,-1):
                if D[row][col] == ox and \
                   D[row-1][col+1] == ox and \
                   D[row-2][col+2] == ox and \
                   D[row-3][col+3] == ox:
                    return True

        return False

def hostGame():

    w = input('How wide would you like the board to be (7)? ')
    h = input('How tall would you like the board to be (6)? ')

    b = Board(w,h)
    print b

    while True:
        oCol = -1
        while b.allowsMove(oCol) == False:
            print '\n'
            oCol = input("O, Choose a column: ")
            print '\n'
        b.addMove(oCol,'O')
        print b

        if b.isFull() == True:
            print "Truce"
            return
        elif b.winsFor('O') == True:
            print 'O won!'
            return

        xCol = -1
        while b.allowsMove(xCol) == False:
            print '\n'
            xCol = input("X, Choose a column: ")
            print '\n'
        b.addMove(xCol,'X')
        print b

        if b.isFull() == True:
            print "Truce"
            return
        elif b.winsFor('X') == True:
            print 'X won!'
            return
"""
hostGame()


b = Board(7,6)
b.addMove(0, 'X')
b.addMove(0, 'O')
b.addMove(0, 'X')
b.addMove(3, 'O')
b.addMove(4, 'O')  # cheating by letting O go again!
b.addMove(5, 'O')
b.addMove(6, 'O')
print b

b.clear()
print b

b.setBoard('0123456')
print b

b = Board(2,2)
print b

b.addMove(0, 'X')
b.addMove(0, 'O')
print b

print b.allowsMove(-1)
print b.allowsMove(0)
print b.allowsMove(1)
print b.allowsMove(2)

b = Board(2,2)
print b.isFull()

b.setBoard( '0011' )
print b.isFull()


b = Board(2,2)
b.setBoard( '0011' )
b.delMove(1)
print b
b.delMove(1)
print b
b.delMove(1)
print b
b.delMove(0)
print b


b = Board(7,6)
b.setBoard( '00102030' )
print b
print b.winsFor('X')
print b.winsFor('O')

b = Board(7,6)
b.setBoard( '23344545515' )
print b
print b.winsFor('O')
"""

