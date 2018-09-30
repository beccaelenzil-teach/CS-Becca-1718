# Connect Four Tests

print "---------------------------------------------"
print "print a 7 x 6 board with the columns numbered"
print "---------------------------------------------\n"
b = Board(7,6)
print b

print " "
print "---------------------------------------------"
print "test addMove"
print "---------------------------------------------\n"
print "| | | | | | | |"
print "| | | | | | | |"
print "| | | | | | | |"
print "|X| | | | | | |"
print "|O| | | | | | |"
print "|X| | |O|O|O|O|"
print "---------------"
print " 0 1 2 3 4 5 6\n"
print "==\n"
b.addMove(0, 'X')
b.addMove(0, 'O')
b.addMove(0, 'X')
b.addMove(3, 'O')
b.addMove(4, 'O')  # cheating by letting O go again!
b.addMove(5, 'O')
b.addMove(6, 'O')
print b

print " "
print "---------------------------------------------"
print "test clear"
print "---------------------------------------------\n"
print "print an empty board"
b.clear()
print b

print " "
print "---------------------------------------------"
print "test allowsMove"
print "---------------------------------------------\n"
b = Board(2,2)
b.addMove(0, 'X')
b.addMove(0, 'O')
print b
print " "
print "b.allowsMove(-1) should be False == ",b.allowsMove(-1)
print "b.allowsMove(0) should be False == ",b.allowsMove(0)
print "b.allowsMove(1) should be True == ",b.allowsMove(1)
print "b.allowsMove(2) should be False == ",b.allowsMove(2)

print " "
print "---------------------------------------------"
print "test isFull"
print "---------------------------------------------\n"
b = Board(2,2)
print b
print " "
print "b.isFull() should be False == ", b.isFull()
print " "
b.setBoard( '0011' )
print b
print " "
print "b.isFull() should be True == ", b.isFull()


print " "
print "---------------------------------------------"
print "test delMove"
print "---------------------------------------------\n"

b = Board(2,2)
b.setBoard( '0011' )
print b
print "after the following commands: \n \
b.delMove(1) \n \
b.delMove(1) \n \
b.delMove(1) \n \
b.delMove(0) \n \
The board should look like: \n \
| | | \n \
|X| | \n \
-----\n \
 0 1 \n \
 == "
b.delMove(1)
b.delMove(1)
b.delMove(1)
b.delMove(0)
print b

print " "
print "---------------------------------------------"
print "test winsFor"
print "---------------------------------------------\n"


b = Board(7,6)
b.setBoard( '00102030' )
print "if b.setBoard( '00102030' ), then b.winsFor('X') should be True == ",b.winsFor('X')
print "if b.setBoard( '00102030' ), then b.winsFor('O') should be True == ",b.winsFor('O')

b = Board(7,6)
b.setBoard( '23344545515'  )
print "if b.setBoard( '23344545515'  ), then b.winsFor('X') should be True == ",b.winsFor('X')
print "if b.setBoard( '23344545515'  ), then b.winsFor('O') should be False == ",b.winsFor('O')

print " "
print "---------------------------------------------"
print "host game"
print "---------------------------------------------\n"

# play your game with a friend, tell me who you played with, and confirm that everything works

print "I played with ________"
print "Everything works!"
print "or"
print "It doesn't work"
