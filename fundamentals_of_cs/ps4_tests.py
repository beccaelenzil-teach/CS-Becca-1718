import p4_2_game_of_life as life

print('Problem Set 4 Score: ')
print("------------------------------------- ")
print('Random Walk Score: ')
print("------------------------------------- ")
print('Game of Life Score: ')
print('Notes: ')
print("------------------------------------- ")
print(' ')
print('diagonalize()')
print("------------------------------------- ")
A = life.diagonalize(5,5)
life.printBoard(A)
print('innerReverse()')
print("------------------------------------- ")
Areverse = life.innerReverse(A)
life.printBoard(Areverse)
print(' ')
print('randomCells()')
print("------------------------------------- ")
A = life.randomCells(5,5)
life.printBoard(A)
print(' ')
print('countNeighbors()')
print("------------------------------------- ")
A = [ [0,0,0,0,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,0,0,0]]
print('A = ')
life.printBoard(A)
print('countNeighbors(2,2,A) = 2:',life.countNeighbors(2,2,A), 2 == life.countNeighbors(2,2,A))
print(' ')
print('next_life_generation()')
print("------------------------------------- ")
A = [ [0,0,0,0,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,0,0,0]]
print('A = ')
life.printBoard(A)
A2 = life.next_life_generation(A)
print("A2 = next_life_generation(A) --> printBoard(A2) should look like")
print('00000')
print('00000')
print('01110')
print('00000')
print('00000')
print('and it looks like')
life.printBoard(A2)
