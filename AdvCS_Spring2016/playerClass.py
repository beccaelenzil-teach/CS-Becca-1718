import TheBoardClass
import random

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