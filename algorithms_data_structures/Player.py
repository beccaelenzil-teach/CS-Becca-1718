from ConnectFour import *

import random

class Player:
    "an AI player for Connect Four"
    def __init__(self, ox, tbt, ply):
        self.ox = ox
        self.tbt = tbt
        self.ply = ply


    def __repr__( self ):
        """ creates an appropriate string """
        s = "Player for " + self.ox + "\n"
        s += "  with tiebreak type: " + self.tbt + "\n"
        s += "  and ply == " + str(self.ply) + "\n\n"
        return s

    def oppCh(self):
        if self.ox == "X":
            return "O"
        else:
            return "X"

    def scoreBoard(self, b):
        W = b.width
        H = b.heght
        score = []
        for col in range(0,W):
            if b.allowsMove(col) == False:
                score[col] = 0
            else:
                b.addMove(col)


p = Player('O', 'LEFT', 3)
print(p.oppCh())
