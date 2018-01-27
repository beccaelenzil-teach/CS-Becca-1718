width = 400
height = 400

class Walker(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.choice = 0
        
    def display(self):
        stroke(0);
        point(self.x,self.y)
        
    def step(self):
        self.stepx = random(-1,1)
        self.stepy = random(-1,1)
        self.x += self.stepx
        self.y += self.stepy
        
        self.x = constrain(self.x,0,width-1);
        self.y = constrain(self.y,0,height-1);
        
walker = Walker(width/2, height/2)

def setup():
    background(255)
    size(width,height)
    
def draw():
    walker.display()
    walker.step()


