__author__ = 'becca.elenzil'



"""
b = box(length = 0.5, width = 2.0, height = 1.5)

#b.length = 0.5  # the box's length just changed
#b.width = 2.0 # the box's width just changed
#b.height = 1.5  # the box's height just changed
b.color = (1.0, 0.0, 0.0)  # the box turned red
b.material = materials.wood  # it's wood-grained!
b.material = materials.glass # it's translucent!

c = box()

print c.color

print b.pos

v = vector(1,2,3)
w = vector(10,20,30)
print v+w

u = vector(1,1,0)
print u.norm()

b.pos = vector(0,1,2)
b.rotate(angle = pi/4)
"""

from visual import *
import random

def spinBox():
    myBox = box(color = (1.0,1.0,1.0))
    while True:
        # Slow down the animation to 60 frames per second.
        # Change the value to see the effect!
        rate(60)
        myBox.rotate(angle=pi/100)


def spinBoxes():
    boxList = []
    for boxNumber in range(10):
        x = random.randint(-5, 5) # integer between -5,5
        y = random.randint(-5, 5)
        z = random.randint(-5, 5)
        red = random.random()     # real number between 0 & 1
        green = random.random()
        blue = random.random()
        newBox = box(pos = vector(x, y, z),
                     color = (red, green, blue) )
        boxList.append(newBox)
    while True:
        for myBox in boxList:
            #rate(60)
            myBox.rotate(angle=pi/100)


spinBoxes()