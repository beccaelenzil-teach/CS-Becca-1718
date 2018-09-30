#Hayden Ratliff
import cmath as math
import random
from time import *
from itertools import chain
import copy

class Cube:
   def __init__(self, top, front, right, back, left, bottom):
       t = str(top)
       f = str(front)
       r = str(right)
       b = str(back)
       l = str(left)
       d = str(bottom)

       self.top = [[t[0], t[1], t[2]], [t[3], t[4], t[5]], [t[6], t[7], t[8]]]
       self.front = [[f[0], f[1], f[2]], [f[3], f[4], f[5]], [f[6], f[7], f[8]]]
       self.right = [[r[0], r[1], r[2]], [r[3], r[4], r[5]], [r[6], r[7], r[8]]]
       self.back = [[b[0], b[1], b[2]], [b[3], b[4], b[5]], [b[6], b[7], b[8]]]
       self.left = [[l[0], l[1], l[2]], [l[3], l[4], l[5]], [l[6], l[7], l[8]]]
       self.bottom = [[d[0], d[1], d[2]], [d[3], d[4], d[5]], [d[6], d[7], d[8]]]

   def __repr__(self):
       s = ''
       s += '  ' + 'TOP' + '    ' + 'FRONT' + '   ' + 'RIGHT' + '   ' + 'BACK' + '    ' + 'LEFT' + '   ' + 'BOTTOM'
       s += '\n'
       for b in range (3):
           for a in range (3):
               s += '|' + str(self.top[b][a])
           s += '|' + ' '
           for a in range (3):
               s += '|' + str(self.front[b][a])
           s += '|' + ' '
           for a in range (3):
               s += '|' + str(self.right[b][a])
           s += '|' + ' '
           for a in range (3):
               s += '|' + str(self.back[b][a])
           s += '|' + ' '
           for a in range (3):
               s += '|' + str(self.left[b][a])
           s += '|' + ' '
           for a in range (3):
               s += '|' + str(self.bottom[b][a])
           s += '|'
           s += '\n'
       return s

   """
   layers parallel to ground: U, E, D
   layers perpendicular to user: L, M, R
   layers parallel to user: F, S, B
   all layers move relative to the top of the cube
   yellow is top, red is front, white is bottom
   """

   def U(self):
       cnew = copy.deepcopy(self)
       self.top[1][0] = cnew.top[2][1] # setting middle left piece on face
       self.top[1][2] = cnew.top[0][1] # setting middle right piece on face
       for a in range (3):
           self.top[0][a] = cnew.top[2-a][0] # rotating left face to top
           self.top[2][a] = cnew.top[2-a][2] # rotating right face to bottom
           self.front[0][a] = cnew.right[0][a] # rotating right corresponding face to bottom corresponding face
           self.right[0][a] = cnew.back[0][a] # rotating top corresponding face to right corresponding face
           self.back[0][a] = cnew.left[0][a] # rotating left corresponding face to top corresponding face
           self.left[0][a] = cnew.front[0][a] # rotating bottom corresponding face to left corresponding face

   def F(self):
       cnew = copy.deepcopy(self)
       self.front[1][0] = cnew.front[2][1] # setting middle left piece on face
       self.front[1][2] = cnew.front[0][1] # setting middle right piece on face
       for a in range (3):
           self.front[0][a] = cnew.front[2-a][0] # rotating left face to top
           self.front[2][a] = cnew.front[2-a][2] # rotating right face to bottom
           self.bottom[2][a] = cnew.right[a][0] # rotating right corresponding face to bottom corresponding face
           self.right[a][0] = cnew.top[2][a] # rotating top corresponding face to right corresponding face
           self.top[2][a] = cnew.left[2-a][2] # rotating left corresponding face to top corresponding face
           self.left[a][2] = cnew.bottom[2][2-a] # rotating bottom corresponding face to left corresponding face

   def R(self):
       cnew = copy.deepcopy(self)
       self.right[1][0] = cnew.right[2][1] # setting middle left piece on face
       self.right[1][2] = cnew.right[0][1] # setting middle right piece on face
       for a in range (3):
           self.right[0][a] = cnew.right[2-a][0] # rotating left face to top
           self.right[2][a] = cnew.right[2-a][2] # rotating right face to bottom
           self.bottom[a][0] = cnew.back[a][0] # rotating right corresponding face to bottom corresponding face
           self.back[a][0] = cnew.top[2-a][2] # rotating top corresponding face to right corresponding face
           self.top[a][2] = cnew.front[a][2] # rotating left corresponding face to top corresponding face
           self.front[a][2] = cnew.bottom[2-a][0] # rotating bottom corresponding face to left corresponding face

   def B(self):
       cnew = copy.deepcopy(self)
       self.back[1][0] = cnew.back[2][1] # setting middle left piece on face
       self.back[1][2] = cnew.back[0][1] # setting middle right piece on face
       for a in range (3):
           self.back[0][a] = cnew.back[2-a][0] # rotating left face to top
           self.back[2][a] = cnew.back[2-a][2] # rotating right face to bottom
           self.bottom[0][a] = cnew.left[2-a][0] # rotating right corresponding face to bottom corresponding face
           self.left[2-a][0] = cnew.top[0][a] # rotating top corresponding face to right corresponding face
           self.top[0][a] = cnew.right[a][2] # rotating left corresponding face to top corresponding face
           self.right[a][2] = cnew.bottom[0][a] # rotating bottom corresponding face to left corresponding face

   def L(self):
       cnew = copy.deepcopy(self)
       self.left[1][0] = cnew.left[2][1] # setting middle left piece on face
       self.left[1][2] = cnew.left[0][1] # setting middle right piece on face
       for a in range (3):
           self.left[0][a] = cnew.left[2-a][0] # rotating left face to top
           self.left[2][a] = cnew.left[2-a][2] # rotating right face to bottom
           self.bottom[a][2] = cnew.front[2-a][0] # rotating right corresponding face to bottom corresponding face
           self.front[a][0] = cnew.top[a][0] # rotating top corresponding face to right corresponding face
           self.top[a][0] = cnew.back[2-a][2] # rotating left corresponding face to top corresponding face
           self.back[a][2] = cnew.bottom[a][2] # rotating bottom corresponding face to left corresponding face

   def D(self):
       cnew = copy.deepcopy(self)
       self.bottom[1][0] = cnew.bottom[2][1] # setting middle left piece on face
       self.bottom[1][2] = cnew.bottom[0][1] # setting middle right piece on face
       for a in range (3):
           self.bottom[0][a] = cnew.bottom[2-a][0] # rotating left face to top
           self.bottom[2][a] = cnew.bottom[2-a][2] # rotating right face to bottom
           self.front[2][a] = cnew.left[2][a] # rotating right corresponding face to bottom corresponding face
           self.left[2][a] = cnew.front[2][a] # rotating top corresponding face to right corresponding face
           self.back[2][a] = cnew.right[2][a] # rotating left corresponding face to top corresponding face
           self.right[2][a] = cnew.back[2][a] # rotating bottom corresponding face to left corresponding face

   def Ux(self):
       cnew = copy.deepcopy(self)
       self.top[1][0] = cnew.top[0][1] # setting middle left piece on face
       self.top[1][2] = cnew.top[2][1] # setting middle right piece on face
       for a in range (3):
           self.top[0][a] = cnew.top[a][2] # rotating right face to top
           self.top[2][a] = cnew.top[a][0] # rotating left face to bottom
           self.front[0][a] = cnew.left[0][a] # rotating left corresponding face to bottom corresponding face
           self.right[0][a] = cnew.front[0][a] # rotating bottom corresponding face to right corresponding face
           self.back[0][a] = cnew.right[0][a] # rotating right corresponding face to top corresponding face
           self.left[0][a] = cnew.back[0][a] # rotating top corresponding face to left corresponding face

   def Fx(self):
       cnew = copy.deepcopy(self)
       self.front[1][0] = cnew.front[0][1] # setting middle left piece on face
       self.front[1][2] = cnew.front[2][1] # setting middle right piece on face
       for a in range (3):
           self.front[0][a] = cnew.front[a][2] # rotating right face to top
           self.front[2][a] = cnew.front[a][0] # rotating left face to bottom
           self.bottom[2][a] = cnew.left[2-a][2] # rotating left corresponding face to bottom corresponding face
           self.right[a][0] = cnew.bottom[2][a] # rotating bottom corresponding face to right corresponding face
           self.top[2][a] = cnew.right[a][0] # rotating right corresponding face to top corresponding face
           self.left[a][2] = cnew.top[2][2-a] # rotating top corresponding face to left corresponding face

   def Rx(self):
       cnew = copy.deepcopy(self)
       self.right[1][0] = cnew.right[0][1] # setting middle left piece on face
       self.right[1][2] = cnew.right[2][1] # setting middle right piece on face
       for a in range (3):
           self.right[0][a] = cnew.right[a][2] # rotating right face to top
           self.right[2][a] = cnew.right[a][0] # rotating left face to bottom
           self.bottom[a][0] = cnew.front[2-a][2] # rotating left corresponding face to bottom corresponding face
           self.back[a][0] = cnew.bottom[a][0] # rotating bottom corresponding face to right corresponding face
           self.top[a][2] = cnew.back[2-a][0] # rotating right corresponding face to top corresponding face
           self.front[a][2] = cnew.top[a][2] # rotating top corresponding face to left corresponding face

   def Bx(self):
       cnew = copy.deepcopy(self)
       self.back[1][0] = cnew.back[0][1] # setting middle left piece on face
       self.back[1][2] = cnew.back[2][1] # setting middle right piece on face
       for a in range (3):
           self.back[0][a] = cnew.back[a][2] # rotating right face to top
           self.back[2][a] = cnew.back[a][0] # rotating left face to bottom
           self.bottom[0][a] = cnew.right[a][2] # rotating left corresponding face to bottom corresponding face
           self.left[a][0] = cnew.bottom[0][2-a] # rotating bottom corresponding face to right corresponding face
           self.top[0][a] = cnew.left[2-a][0] # rotating right corresponding face to top corresponding face
           self.right[a][2] = cnew.top[0][a] # rotating top corresponding face to left corresponding face

   def Lx(self):
       cnew = copy.deepcopy(self)
       self.left[1][0] = cnew.left[0][1] # setting middle left piece on face
       self.left[1][2] = cnew.left[2][1] # setting middle right piece on face
       for a in range (3):
           self.left[0][a] = cnew.left[a][2] # rotating right face to top
           self.left[2][a] = cnew.left[a][0] # rotating left face to bottom
           self.bottom[a][2] = cnew.back[a][2] # rotating left corresponding face to bottom corresponding face
           self.front[a][0] = cnew.bottom[2-a][2] # rotating bottom corresponding face to right corresponding face
           self.top[a][0] = cnew.front[a][0] # rotating right corresponding face to top corresponding face
           self.back[a][2] = cnew.top[2-a][0] # rotating top corresponding face to left corresponding face

   def Dx(self):
       cnew = copy.deepcopy(self)
       self.bottom[1][0] = cnew.bottom[0][1] # setting middle left piece on face
       self.bottom[1][2] = cnew.bottom[2][1] # setting middle right piece on face
       for a in range (3):
           self.bottom[0][a] = cnew.bottom[a][2] # rotating right face to top
           self.bottom[2][a] = cnew.bottom[a][0] # rotating left face to bottom
           self.front[2][a] = cnew.right[2][a] # rotating left corresponding face to bottom corresponding face
           self.left[2][a] = cnew.front[2][a] # rotating bottom corresponding face to right corresponding face
           self.back[2][a] = cnew.left[2][a] # rotating right corresponding face to top corresponding face
           self.right[2][a] = cnew.back[2][a] # rotating top corresponding face to left corresponding face

   def E(self):
       cnew = copy.deepcopy(self)
       for a in range(3):
           self.front[1][a] = cnew.left[1][a]
           self.right[1][a] = cnew.front[1][a]
           self.back[1][a] = cnew.right[1][a]
           self.left[1][a] = cnew.back[1][a]

   def M(self):
       cnew = copy.deepcopy(self)
       for a in range(3):
           self.front[a][1] = cnew.top[a][1]
           self.bottom[a][1] = cnew.front[2-a][1]
           self.back[a][1] = cnew.bottom[a][1]
           self.top[a][1] = cnew.back[2-a][1]

   def S(self):
       cnew = copy.deepcopy(self)
       for a in range(3):
           self.top[1][a] = cnew.left[2-a][1]
           self.right[a][1] = cnew.top[1][a]
           self.bottom[1][a] = cnew.right[a][1]
           self.left[a][1] = cnew.bottom[1][2-a]

   def Ex(self):
       cnew = copy.deepcopy(self)
       for a in range(3):
           self.front[1][a] = cnew.right[1][a]
           self.right[1][a] = cnew.back[1][a]
           self.back[1][a] = cnew.left[1][a]
           self.left[1][a] = cnew.front[1][a]

   def Mx(self):
       cnew = copy.deepcopy(self)
       for a in range(3):
           self.front[a][1] = cnew.bottom[2-a][1]
           self.bottom[a][1] = cnew.back[a][1]
           self.back[a][1] = cnew.top[2-a][1]
           self.top[a][1] = cnew.front[a][1]

   def Sx(self):
       cnew = copy.deepcopy(self)
       for a in range(3):
           self.top[1][a] = cnew.right[a][1]
           self.right[a][1] = cnew.bottom[1][a]
           self.bottom[1][a] = cnew.left[2-a][1]
           self.left[a][1] = cnew.top[1][2-a]

   def checkSolved(self):
       vert = [0, 0, 0, 1, 1, 2, 2, 2]
       hori = [0, 1, 2, 1, 2, 0, 1, 2]
       for a in range (8):
           if self.top[vert[a]][hori[a]] != self.top[1][1]: return False
           if self.front[vert[a]][hori[a]] != self.front[1][1]: return False
           if self.right[vert[a]][hori[a]] != self.right[1][1]: return False
           if self.back[vert[a]][hori[a]] != self.back[1][1]: return False
           if self.left[vert[a]][hori[a]] != self.left[1][1]: return False
           if self.bottom[vert[a]][hori[a]] != self.bottom[1][1]: return False
       return True

   def randomConfig(self, mixes):
       functionlist = ["U", "U'", "F", "F'", "R", "R'", "B", "B'", "L", "L'", "D", "D'", "M", "M'", "E", "E'", "S", "S'"]
       for a in range(mixes):
           move = random.choice(functionlist)
           if move == "U": self.U()
           elif move == "F": self.F()
           elif move == "R": self.R()
           elif move == "B": self.B()
           elif move == "L": self.L()
           elif move == "D": self.D()
           elif move == "M": self.M()
           elif move == "E": self.E()
           elif move == "S": self.S()
           elif move == "U'": self.Ux()
           elif move == "F'": self.Fx()
           elif move == "R'": self.Rx()
           elif move == "B'": self.Bx()
           elif move == "L'": self.Lx()
           elif move == "D'": self.Dx()
           elif move == "M'": self.Mx()
           elif move == "E'": self.Ex()
           elif move == "S'": self.Sx()
           print(self)

def rubiksInterface():
   print("Welcome to the rubiks cube interface.")
   print("If you would like a randomly mixed cube, select 'Random'. If you would like to manually input your cube, select 'Manual'")
   cubetype = str.lower(input("(Random / Manual)"))
   if cubetype == "manual":
       c = Cube(str(input("Top side:")), str(input("Front side:")), str(input("Right side:")), str(input("Back side:")),
                str(input("Left side:")), str(input("Bottom side:")))
       print(c)
       k = copy.deepcopy(c)
   else:
       print("Random selected.")
       c = Cube("YYYYYYYYY", "OOOOOOOOO", "GGGGGGGGG", "RRRRRRRRR", "BBBBBBBBB", "WWWWWWWWW")
       c.randomConfig(20)
       print("Your cube:")
       print(c)
       k = copy.deepcopy(c)
   playgame = 1
   while playgame == 1:
       while c.checkSolved() == False:
           print("U, F, R, B, L, and D correspond with the different faces of the cube.")
           print("M, E, and S correspond with the vertical, horizontal, and parallel center thirds, respectively.")
           print("If you want a clockwise rotation of a given face, input the letter.")
           print("If you want a counterclockwise rotation of a given face, input ' after the letter.")
           move = str(input("Your move:"))
           if move == "U": c.U()
           elif move == "F": c.F()
           elif move == "R": c.R()
           elif move == "B": c.B()
           elif move == "L": c.L()
           elif move == "D": c.D()
           elif move == "M": c.M()
           elif move == "E": c.E()
           elif move == "S": c.S()
           elif move == "U'": c.Ux()
           elif move == "F'": c.Fx()
           elif move == "R'": c.Rx()
           elif move == "B'": c.Bx()
           elif move == "L'": c.Lx()
           elif move == "D'": c.Dx()
           elif move == "M'": c.Mx()
           elif move == "E'": c.Ex()
           elif move == "S'": c.Sx()
           else: print("Error: invalid move.")
           print(c)
       print("You solved it!")
       if input("Play again using same cube? (Y / N)") == "Y":
           c = k
       else:
           playgame = 0
           print("Thanks for playing!")

rubiksInterface()

