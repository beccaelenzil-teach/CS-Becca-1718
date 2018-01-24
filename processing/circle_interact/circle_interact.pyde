import random

def setup():

    size(1400,1000)
    background(random.choice([0,255]))
    global circle_list
    circle_list = []
    for i in range(200):
        circ = circle(random.randint(1,1400), random.randint(1,1000), random.randint(9,11))
        circle_list.append(circ)
    
def draw():
    for circ in circle_list:
        ellipse(circ.x,circ.y,circ.d,circ.d)
        fill(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    

    
    ball = circle(50,50,50)
    ellipse(ball.x,ball.y,ball.d,ball.d)
    
    ball.x += ball.change_x
    ball.y += ball.change_y
    
    if ball.x <= 0 or ball.x >= 1400:
        ball.change_x*=-1
    if ball.y <= 0 or ball.y >= 100:
        ball.change_y*=-1
    
    
    d = random.randint(15,25)
    ellipse(mouseX,mouseY,d,d)
    
    current_x = mouseX
    
    if mousePressed:
        clear()
        background(random.choice([0,255]))


class circle():
    def __init__(self,x,y,d):
        self.x = x
        self.y = y
        self.d = d
        self.change_x = 1
        self.change_y = 1
    