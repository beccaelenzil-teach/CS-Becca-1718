function setup() {
  createCanvas(800, 800, WEBGL);
}

function draw(){
  background(200,0,200);
  for (i=1; i<10; i++){
    rotateX(frameCount * 0.1/i);
    rotateY(frameCount * 0.1/i);
    rotateZ(frameCount * 0.1/i);
    fill(i*20,i*20,i*20)
    translate(i*4,i*4,i*4)
    box(20)
  }
}