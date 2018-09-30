__author__ = 'becca.elenzil'
import random
import time

class Card():
    # simple card class with the following attributes:
    # value - the cards value for finding pairs
    # row, col - the location on the board
    # turned over - whether it's visible or not
    def __init__(self, value, row, col):
        self.turnedOver = False
        self.col = col
        self.row = row
        self.value = value

class Board():
    def __init__(self, size):
        # the size is the side length of the square board, only even values are allowed
        self.size = size

    def populateBoard(self):
        s = self.size
        #this list will hold the card objects
        self.cards = []
        numbers = []

        #these are the values for the cards
        for n in range(s**2/2):
            numbers.append(n)
            numbers.append(n)
        random.shuffle(numbers)

        #create all the cards for the board
        k = 0
        for i in range(s):
            for j in range(s):
                self.cards.append(Card(numbers[k],i,j))
                k += 1

    def printBoard(self):
        # a bare bones print board function, this could use a fix to the formating and column and row numbers
        s = self.size
        k = 0
        b = ' '
        for row in range(s):
            b += ' | '
            for col in range(s):
                if self.cards[k].turnedOver == True:
                    b += str(self.cards[k].value) + ' | '
                else:
                    b += '* | '
                k+=1
            b += '\n'
        print b

    def playGame(self):
        count = 0
        s = self.size
        numPairs = s**2 / 2

        while count < numPairs:

            self.printBoard()

            print "Choose a card to flip over"
            firstRow = input("Pick a row: ")
            firstCol = input("Pick a col: ")


            m = (firstRow-1)*s + firstCol #this translates the row, col values to an index in the cards list
            self.cards[m].turnedOver = True
            self.printBoard()

            secondRow = input("Pick a row: ")
            secondCol = input("Pick a col: ")

            n = (secondRow-1)*s + secondCol #this translates the row, col values to an index in the cards list
            self.cards[n].turnedOver = True
            self.printBoard()

            #check if it's a pair
            #if it's a pair
            if self.cards[m].value == self.cards[n].value:
                print "Congrats! You got a pair.\n"
                self.cards[m].value = ' ' #remove the cards if they're a pair
                self.cards[n].value = ' ' #remove the cards if they're a pair
                count += 1
            else:
                print "Rats, that's not a pair. Choose new cards.\n"
                self.cards[m].turnedOver = False #turn the cards back over if they are not a pair
                self.cards[n].turnedOver = False #turn the cards back over if they are not a pair
            time.sleep(2)

def hostGame():
    b = Board(2)
    b.populateBoard()
    b.playGame()

hostGame()







