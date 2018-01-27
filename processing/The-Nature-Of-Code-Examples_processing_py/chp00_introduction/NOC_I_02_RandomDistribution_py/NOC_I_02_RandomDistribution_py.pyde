randomCounts = []
total = 20

def setup():
  size(640,240);
  for i in range(total):
    randomCounts.append(0)
    
def draw():
    background(127)
    index = floor(random(0,total))
    randomCounts[index] += 1
    
    #Draw a rectangle to graph results
    stroke(0)
    strokeWeight(2)
    fill(255)
    w = width/len(randomCounts)

    for x in range(len(randomCounts)):
        # rect(p1,p2,p3,p4) draws a rectangle to the screen.
        # By default, the first two parameters set the location of the upper-left corner, 
        # the third sets the width, and the fourth sets the height.
        rect(x*w, height - randomCounts[x], w-1, randomCounts[x])

