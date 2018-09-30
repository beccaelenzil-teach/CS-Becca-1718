let phase, speed, maxCircleSize, numRows, numCols, numStrands, colorA, colorB;

function setup() {
	createCanvas(500, 500);

	noStroke();

	phase = 0;
	speed = 0.1;
	maxCircleSize = 20;

	numRows = 10;
	numCols = 16;
	numStrands = 2;

	colorA = color(2, 174, 20);
	colorB = color(226, 129, 16);

	var vid = createVideo(['vid.mp4'])
}

function draw() {
  
  // This is a conditional statement that changes the 
  // colors, speed, circle size, number of columns and rows
  // when the mouse is clicked
  if (mouseIsPressed){
    speed = random([0.01, 0.02, 0.03, 0.04, 0.05, 0.07, 0.1, 0.15])
    
    //colors are chosen randomly
    colorA = color(random(256),random(256),random(256))
    colorB = color(random(256),random(256),random(256))
    maxCircleSize = random(10,30)
    numCols = random([5,10,15,20,30,40])
    numRows = random([2, 5, 10,20])
  }
  
  
  // this is the background color represented as RGB
	background(5, 58, 74);

  
  //this is the motion
	for(let strand = 0; strand < numStrands; strand += 1) {
		for(let col = 0; col < numCols; col += 1) {
			for(let row = 0; row < numRows; row += 1) {
				
				let strandPhase = phase + map(strand, 0, numStrands, 0, TWO_PI);
				
				let colOffset = map(col, 0, numCols, 0, TWO_PI);
				let x = map(col, 0, numCols, 50, width - 50);
				let y = height/3 + row * 10 + sin(strandPhase + colOffset) * 50;
				
				let sizeOffset = (cos(strandPhase - (row / numRows) + colOffset) + 1) * 0.5;
				
				let circleSize = sizeOffset * maxCircleSize;

        
				fill(lerpColor(colorA, colorB, row / numRows));
				ellipse(x, y, circleSize, circleSize);
			}
		}
	}

	phase = frameCount * speed;
}

