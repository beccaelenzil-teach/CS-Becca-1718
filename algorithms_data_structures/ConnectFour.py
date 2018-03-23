# Connect Four
# Name:
#

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
        nums = ''
        for row in range(0,H):
            s += '|'
            for col in range(0,W):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*W+1) * '-'    # bottom of the board
        s += '\n'
        for col in range(0,W):
            nums += ' ' + str(col % 10)
        s += nums

        # and the numbers underneath here

        return s       # the board is complete, return it

    def addMove(self, col, ox):
        W = self.width
        H = self.height
        moved = False
        row = H-1
        while 0 <= row < H and moved == False:
            if self.data[row][col] == ' ':
                self.data[row][col] = ox
                moved = True
            row -= 1

    def clear(self):
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
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'


    def allowsMove(self, col):
        W = self.width
        H = self.height
        if col < 0 or col >= W:
            return False
        elif self.data[0][col] == ' ':
            return True
        else:
            return False

    def isFull(self):
        W = self.width
        H = self.height
        boolean_sum = 0
        for col in range(0,W):
            if self.allowsMove(col) == False:
                boolean_sum += 1

        if boolean_sum == 0:
            return False
        else:
            return True

    def delMove(self, col):
        H = self.height
        moved = False
        row = 0
        while 0 <= row < H and moved == False:
            if self.data[row][col] != ' ':
                self.data[row][col] = ' '
                moved = True
            row += 1

    def winsFor(self, ox):
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

        #check for vertical wins
        for row in range(0,H-3):
            for col in range(0,W):
                if D[row][col] == ox and \
                   D[row+1][col] == ox and \
                   D[row+2][col] == ox and \
                   D[row+3][col] == ox:
                    return True

        #check for diagonal positive slope wins
        for row in range(0,H-3):
            for col in range(0,W-3):
                if D[row][col] == ox and \
                   D[row+1][col+1] == ox and \
                   D[row+2][col+2] == ox and \
                   D[row+3][col+3] == ox:
                    return True

        #check for diagonal negative slope wins
        for row in range(3,H):
            for col in range(0,W-3):
                if D[row][col] == ox and \
                   D[row-1][col+1] == ox and \
                   D[row-2][col+2] == ox and \
                   D[row-3][col+3] == ox:
                    return True

        return False

    def hostGame(self):
        ox = "X"
        win = False
        while win == False:
            print(self)
            print("It's your turn " + ox)
            users_col = -1
            while self.allowsMove( users_col ) == False:
                users_col = int(input("Choose a column: "))
            self.addMove(users_col, ox)
            win = self.winsFor(ox)
            if win == True:
                print("You won "+ox+"!")
            if ox == 'X':
                ox = 'O'
            else:
                ox = 'X'




#b = Board(7,6)
#b.hostGame()











