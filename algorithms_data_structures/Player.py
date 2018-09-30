from ConnectFour import Board as Board
import sys

import random

class basicPlayer():
    """a basic player class that selects the next move"""
    def __init__(self, ox):
        """the constructor"""
        self.ox = ox
        self.type = "basic"

    def __repr__( self ):
        """ creates an appropriate string """
        s = "Basic player for " + self.ox + "\n"
        return s

    def nextMove(self,b):
        """selects an allowable next move at random"""
        W = b.width
        col = -1
        while b.allowsMove(col) == False:
            col = random.randrange(W)
        return col

class smartPlayer(basicPlayer):
    """ an AI player for Connect Four """
    def __init__(self, ox):
        """ the constructor inherits from from the basicPlayer class"""
        basicPlayer.__init__(self, ox)
        self.type = "smart"

    def __repr__( self ):
        """ creates an appropriate string """
        s = "Smart player for " + self.ox + "\n"
        return s

    def oppCh(self):
        if self.ox == "X":
            return "O"
        else:
            return "X"

    def scoresFor(self, b):
        W = b.width
        score = [50]*W
        for col in range(0,W):
            if b.allowsMove(col) == False:
                score[col] = -1
            else:
                b.addMove(col, self.ox)
                if b.winsFor(self.ox):
                    score[col] = 100
                else:
                    for colOpp in range(W):
                        b.addMove(colOpp, self.oppCh())
                        if b.winsFor(self.oppCh()):
                            score[col] = 0
                        b.delMove(colOpp)
                b.delMove(col)

        return score

    def nextMove(self,b):
        score = self.scoresFor(b)
        max_val = max(score)
        max_indices = []
        for i in range(len(score)):
            if score[i] == max_val:
                max_indices.append(i)

        if len(max_indices) > 1:
            print("max indices random: ", random.choice(max_indices))
            return random.choice(max_indices)
        else:
            print("max indices 0: ", max_indices[0])
            return max_indices[0]

def playGame(playerX, playerO):

    """
    playerX should be 'basic', 'smart' or 'human'
    playerO should be 'basic', 'smart' or 'human'
    """
    if playerX == 'smart':
        pX = smartPlayer('X')
    elif playerX == 'basic':
        pX = basicPlayer('X')
    elif playerX == 'human':
        pX = basicPlayer('X')
        pX.type = "human"
    else:
        print("Player X should be 'smart', 'basic', or 'human'. Try again!")
        sys.exit()

    if playerO == 'smart':
        pO = smartPlayer('O')
    elif playerO == 'basic':
        pO = basicPlayer('O')
    elif playerO == 'human':
        pO = basicPlayer('O')
        pO.type = "human"
    else:
        print("Player O should be 'smart', 'basic', or 'human'. Try again!")
        sys.exit()

    b = Board(7,6)

    print(pO)
    print(pX)

    player = pX
    win = False

    while win == False:
        print(b)
        print("It's your turn " + player.ox)
        col = -1
        while b.allowsMove(col) == False:
            if player.type == "basic" or player.type == "smart":
                col = player.nextMove(b)
            else:
                col = int(input("Choose a column: "))
        b.addMove(col, player.ox)
        win = b.winsFor(player.ox)

        if win == True:
            print(b)
            print("You won "+player.ox+"!")

        if player.ox == 'X':
            player = pO
        else:
            player = pX



playGame("human","smart")




