circle_list = []
n = 200
h = 700
w = 1000
m = 0

function setup() {
  createCanvas(w,h)
  background(0)
  for(i=0; i<n; i++){
  	circ = new circle(random(0,w+1),random(0,h+1),random(9,12),random([0,1]),random([-10,-5,5,10]),random(-4,4))
  	circle_list.push(circ)
  }

}

function draw() {
  if (mouseIsPressed){
  	clear()
  	background(0)
  	circle_list = []
  	for(i=0; i<n; i++){
  		circ = new circle(random(0,w+1),random(0,h+1),random(9,12),random([0,1]),random(-4,4),random(-4,4))
  		circle_list.push(circ)
  	}
  }
  for (i=0; i<n; i++){
  	if (m % 5 == 0){
  		circle_list[i].display()
  		circle_list[i].move()
  		if (circle_list[i].x > w || circle_list[i].x < 0){
  			circle_list[i].change_x()
  		}
  		if (circle_list[i].y > h || circle_list[i].y < 0){
  			circle_list[i].change_y()
  		}
  	}
  }

  d = random(15,25)
  ellipse(mouseX,mouseY,d,d)
  if (m % 1 == 0){
  	fill(random(0,256),random(0,256),random(0,256))
  }

  m+=1

}

function circle(x,y,d,a,speed_x,speed_y){
	this.x = x
	this.y = y
	this.d = d
	this.speed_x = speed_x;
	this.speed_y = speed_y;

	this.change_x = function(){
		this.speed_x *= -1
	}
	this.change_y = function(){
		this.speend_y *= -1
	}

	this.move = function(){
		//this.x += random(-this.speed, this.speed);
    	//this.y += random(-this.speed, this.speed);
    	this.x += this.speed_x
    	this.y += this.speed_y
	}

	this.display = function() {
		ellipse(this.x, this.y, this.d, this.d)
    	fill(random(0,256),random(0,256),random(0,256))
  	}

}