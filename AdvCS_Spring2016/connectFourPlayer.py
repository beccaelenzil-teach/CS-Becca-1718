
import random
import sys
from TheBoardClass import Board

class basicPlayer():
    """a basic player class that selects the next move"""
    def __init__(self, ox):
        """the constructor"""
        self.ox = ox

    def __repr__( self ):
        """ creates an appropriate string """
        s = "Basic player for " + self.ox + "\n"
        return s

    def nextMove(self,b):
        """selects an allowable next move at random"""
        col = -1
        while b.allowsMove(col) == False:
            col = random.randrange(b.width)
        return col


class smartPlayer(basicPlayer):
    """ an AI player for Connect Four """
    def __init__(self, ox):
        """ the constructor inherits from from the basicPlayer class"""
        basicPlayer.__init__(self, ox)

    def __repr__( self ):
        """ creates an appropriate string """
        s = "Smart player for " + self.ox + "\n"
        return s

    def oppCh(self):
        if self.ox == 'X':
            return 'O'
        elif self.ox == 'O':
            return 'X'

    def scoresFor(self, b):

        scores = [50]*b.width

        for col in range(b.width):

            if not b.allowsMove(col):
                scores[col] = -1
            else:
                b.addMove(col,self.ox)

                if b.winsFor(self.ox):
                    scores[col] = 100
                else:
                    for colOpp in range(b.width):
                        if b.allowsMove(colOpp):
                            b.addMove(colOpp,self.oppCh())

                            if b.winsFor(self.oppCh()):
                                scores[col] = 0

                            b.delMove(colOpp)

                b.delMove(col)

        return scores

    def nextMove(self, b):

        #score board
        scores = self.scoresFor(b)

        #choose location of max score
        max_index = []
        for i in range(len(scores)):
            if scores[i] == max(scores):
                max_index.append(i)

        col = random.choice(max_index)

        return col


def playGame(pO, pX):

    """
    playerX should be 'basic', 'smart' or 'human'
    playerO should be 'basic', 'smart' or 'human'
    """

    if pX == 'smart':
        pX = smartPlayer('X')
    elif pX == 'basic':
        pX = basicPlayer('X')
    elif pX != 'human':
        print "Player X should be 'smart', 'basic', or 'human'. Try again!"
        sys.exit()#def playGame(playerX, playerO):


    if pO == 'smart':
        pO = smartPlayer('O')
    elif pO == 'basic':
        pO = basicPlayer('O')
    elif pO != 'human':
        print "Player O should be 'smart', 'basic', or 'human'. Try again!"
        sys.exit()

    print pO
    print pX

    b = Board(7,6)
    print b

    while True:
        oCol = -1
        while b.allowsMove(oCol) == False:
            if pO == 'human':
                oCol = input("O, Choose a column: ")
            else:
                oCol = pO.nextMove(b)
                print "O chose: ",oCol, '\n'
        b.addMove(oCol,'O')
        print b

        if b.winsFor('O') == True:
            print 'O won!'
            return 0
        elif b.isFull() == True:
            print "Truce"
            return 2

        xCol = -1
        while b.allowsMove(xCol) == False:
            if pX == 'human':
                xCol = input("X, Choose a column: ")
            else:
                xCol = pX.nextMove(b)
                print "X chose: ",oCol, '\n'
        b.addMove(xCol,'X')
        print b

        if b.winsFor('X') == True:
            print 'X won!'
            return 1
        elif b.isFull() == True:
            print "Truce"
            return 2

playGame('human','smart')

#players = ['O','X','TRUCE']
#numGames = 100
#o_x_truce = [0,0,0]
#for i in range(numGames):
#    winner = playGame('smart', 'smart')
#    o_x_truce[winner] += 1

    #print i
    #print "Game: ",i,"Winner: ",players[winner], '\n'

#print o_x_truce
#print o_x_truce/float(numGames)

#def scoreBoard(self, b):
#    """
#    This should return 100.0 if the board b is a win for self. It should return 50.0 if it is neither a win nor a loss for self,
#    and it should return 0.0 if it is a loss for self (i.e., the opponent won)
#    """
#    if b.winsFor(self.ox) == True:
#        return 100
#    elif b.winsFor(self.oppCh()) == True:
#        return 0
#    else:
#        return 50


#    def tieBreakMove(self, scores):
#        #"""input score: a list of scores"""
#        max_index = []
#        for i in range(len(scores)):
#            if scores[i] == max(scores):
#                max_index.append(i)
#
#        if len(max_index) > 1:
#            if self.tbt == 'LEFT':
#                max_index0 = max_index[0]
#            elif self.tbt == 'RIGHT':
#                max_index0 = max_index[-1]
#            elif self.tbt == 'RANDOM':
#                max_index0 = max_index[random.choice(range(len(max_index)))]
#        else:
#            max_index0 = max_index[0]


#        return max_index0


