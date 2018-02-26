var board_size = 600.0
var spacing = 1.0
var offset = 10.0
var cell_num = 10.0
var cell_num_previous = 20.0
var num_populations = 4
var num_populations_previous = 4
var percent_pops = []
var percent_empty = 10
var percent_empty_previous = 10
var percent_pops_previous = []
var run
var reset
var reset_percent
var initialize_board = 1
var RED = [255, 0, 0, 102, 255, 102, 204, 160, 204, 0 ]
var GREEN = [0, 0, 143, 0, 255, 102, 0, 0, 102, 153]
var BLUE = [0, 255, 0, 204, 0, 102, 102, 160, 0, 153]
var threshold = 0.3

function Cell(row,col,type){
  this.row = row
  this.col = col
  this.type = type
}

function Slider(min,max,initial,step){

  this.min= min
  this.max = max
  this.value = initial
  this.initial = initial
  this.step = step
  this.x_pos = 700
  this.y_pos = 10
  this.radius = 2
  this.width = 100

  this.render = function() {

    stroke(200)
    strokeWeight(4)
    line(this.x_pos, this.y_pos, this.x_pos+this.width, this.y_pos)

    fill(200)
    stroke(0)
    strokeWeight(1)
    difference = this.max - this.min
    percent = this.value/difference
    this.circle_x = this.x_pos + percent*this.width
    ellipse(this.circle_x, this.y_pos, 15, 15)

    distance = sqrt((this.circle_x-mouseX)*(this.circle_x-mouseX)+(this.pos_y-mouseY)*(this.pos_y-mouseY))
    

    if ((distance < 15) && mouseIsPressed && mouseX > this.x_pos && mouseX < (this.x_pos + this.width)){
      this.circle_x = mouseX
      ellipse(circle_x, this.y_pos, 15 ,15)
    }
  }

  this.update = function() {
    difference = this.max - this.min
    num_steps = difference/this.step+1
    this.values = []
    for (i = 0; i < num_steps; i++)
      value = this.initial+i*step
      this.values.push(value)

  }
}

function createOneRow(row,cell_num){
    single_row = []
    for (col = 0; col < cell_num+2; col++){
        cell = new Cell(row,col,-2)
        single_row.push(cell)
    } 
    return single_row
}

function createBoard(cell_num){
    A = []
    for (row = 0; row < cell_num+2; row++){
        A.push(createOneRow(row,cell_num))
    }
    return A
}

function make_copy(A){
  height = A.length
  width = A[0].length
  newA = createBoard(width-2)
  for (row = 0; col < height; row++){
    for (col = 0; col < width; col++){
      newA[row][col] = A[row][col]
    }
  }
  return newA
}

function createModelBoard(percent_empty, percent_pops, cell_num){
  size = cell_num*cell_num
  size_empty = (percent_empty/100*size)
  size_left = size - size_empty
  
  size_sum = 0
  size_pops = []
  population = []
  new_population = []

  for (j = 0; j < percent_pops.length-1; j++){
    size_current_pop = percent_pops[j]/100*size_left
    size_pops.push(size_current_pop)
    size_sum += size_current_pop
  }

  size_pops.push(size_left - size_sum)

  
  for (k = 0; k < size_empty; k++){
    population.push(-1)
  }

  for (k = 0; k < size_pops.length; k++){
    for (n = 0; n < size_pops[k]; n++){
      population.push(k)
    }
  }
  population = population.slice(0,size)
  new_population = population
  new_population = shuffle(population)
  
  return new_population
 };

function populateBoard(cell_num, percent_empty, percent_pops){
  population = createModelBoard(percent_empty, percent_pops, cell_num)
  A = createBoard(cell_num)
  i = 0
  for (row = 1; row < cell_num+1; row++){
    for (col = 1; col < cell_num+1; col++){
      A[row][col].type = population[i]
      i++
    }
  }
  return A
}

function count_neighbors(row, col, A){
  countTotal = 0
  countSame = 0
  for (r = row-1; r < row+2; r++){
    for ( c= col -1; c < col + 2; c++){
      if (A[r][c].type == A[row][col].type){
        countSame += 1
      }

      if (A[r][c].type >= 0){
        countTotal += 1
      }
    }
  }
  countSame = countSame - 1
  countTotal = countTotal - 1
  if (countTotal > 0){
    similarity = float(countSame)/float(countTotal)
  }
  else{
    similarity = 1
  }
  return similarity
}

function index_empties(A){
  empties = []
  height = A.length
  width = A[0].length
  for (row = 1; row < height-1; row++){
    for (col= 1; col< width-1; col++){
      if (A[row][col].type == -1){
        empties.push([row,col])
      }
    }
  }
  new_empties = []
  new_empties = shuffle(empties)
  return new_empties
}


function next_generation(A, threshold){
  height = A.length
  width = A[0].length
  //newA = make_copy(A)
  newA = A
  empties = index_empties(A)
  empties = shuffle(empties)
  i = 0
  for (row = 1; row < height-1; row++){
    for (col= 1; col < width-1; col++){
      similarity = count_neighbors(row,col,A)
      if (A[row][col].type >= 0 && similarity < threshold && i < empties.length){
        newA[empties[i][0]][empties[i][1]].type = A[row][col].type
        newA[row][col].type = -1
        i+=1
      }
      /*else{
        newA[row][col].type = A[row][col].type
      }*/
    }
  }
  return newA
}

function calculate_cell_size(board_size,cell_num){
  cell_size = (board_size-(cell_num+2)*spacing)/(cell_num+2)
  return cell_size
}

function initialize(board_size, cell_num, percent_empty, percent_pops){
  A = []
  cell_size = calculate_cell_size(board_size,cell_num)
  A = populateBoard(cell_num, percent_empty, percent_pops)
}

function drawBoard(A,cell_size,num_populations){
  empties = []
  for (row = 0; row < A[0].length; row++){
    y_pos = ((cell_size+spacing) * row) + offset
    for (col = 0; col < A.length; col++){
      x_pos = ((cell_size+spacing) * col) + offset
      if (A[row][col].type == -1){
        fill(255)
      }
      else if (A[row][col].type == -2){
        fill(200)
      }
      else{
        R = RED[A[row][col].type]
        G = GREEN[A[row][col].type]
        B = BLUE[A[row][col].type]
        fill(R,G,B)
      }
      rect(x_pos,y_pos,cell_size,cell_size)
    }
  }
}


function setup() { 
  createCanvas(board_size+2*offset+300, board_size+2*offset+100);

  percent_pops = [50,50]

  // inputs
  percent_input = []
  percent_slider = []
  reset_percent = []

  for (i = 0; i<10; i++){
    percent_input[i] = createInput(10)
  }

  // sliders
  slider_cell_num = createSlider(4.0, 75.0, 10.0, 1.0);
  slider_cell_num.position(board_size+20, 40);
  slider_cell_num.style('width', '150px')

  slider_num_pops = createSlider(2, 10, 2, 1);
  slider_num_pops.position(board_size+20, 110);
  slider_num_pops.style('width', '150px')

  slider_empty = createSlider(0, 100, 10, 1);
  slider_empty.position(board_size+20, 180);
  slider_empty.style('width', '150px')

  slider_thresh = createSlider(0, 1, 0.3, 0.01);
  slider_thresh.position(board_size+20, 250);
  slider_thresh.style('width', '150px')


  // button
  run = createButton('run');
  run.position(board_size+250, 10);

  reset = createButton('reset');
  reset.position(board_size+250, 50);

  initialize(board_size, cell_num, percent_empty, percent_pops)
}

function draw(){
  
  background(0);

  threshold = slider_thresh.value()

  drawBoard(A,cell_size,num_populations)
  A = next_generation(A, threshold)

  //population and num cells slider text
  fill(255)
  text("Number of Populations", board_size+25, 95);
  text("2", board_size+25, 110);
  text("10", board_size+165, 110);
  text(str(slider_num_pops.value()), board_size+85, 110);

  text("Board Size (height/width", board_size+25, 25);
  text("4", board_size+25, 40);
  text("75", board_size+165, 40);
  text(str(slider_cell_num.value()), board_size+85, 40);

  text("Percent Empty", board_size+25, 160);
  text("0", board_size+25, 175);
  text("100", board_size+165, 175);
  text(str(slider_empty.value()), board_size+85, 175);

  text("Similarity Threshold", board_size+25, 230);
  text("0", board_size+25, 245);
  text("1", board_size+165, 245);
  text(str(slider_thresh.value()), board_size+85, 245);

  num_populations = slider_num_pops.value()
  cell_num = slider_cell_num.value()
  percent_empty = slider_empty.value()

  percent_sum = 0
  percent_pops = []
  for (i = 0; i<num_populations; i++){

    // Position of input bars
    y_pos = 250

    // final population doesn't get an input box (it's 100% - sum)
    if (i == (num_populations-1)){
      fill(255)
      rect(board_size+50, y_pos+2+(i+1)*40, 100, 20)
      fill(0)
      if ((100-percent_sum)>0){
        text(str(100-percent_sum), board_size+55, y_pos+18+(i+1)*40);
      }
      else{
        text(str(0), board_size+55, y_pos+18+(i+1)*40);
      }
    }
    else{
      percent_input[i].position(board_size+50, y_pos+2+(i+1)*40);
      percent_input[i].style('width', '100px')
    }

    percent_pops[i] = float(percent_input[i].value())

    percent_input[i].defaultValue = 100/num_populations

    R = RED[i]
    G = GREEN[i]
    B = BLUE[i]
    fill(R,G,B)

    rect(board_size+20, y_pos+(i+1)*40,20,20)
    text(str(0), board_size+50, y_pos+(i+1)*40);
    text("Population "+str(i+1), board_size+180, y_pos+15+(i+1)*40)

    if (i==(num_populations-1) && ((100-percent_sum) > 0)){
      text(str(100-percent_sum), board_size+100, y_pos+(i+1)*40);
      text(str(100-percent_sum), board_size+150, y_pos+(i+1)*40);
    }
    else if (100-percent_sum > 0){
      text(percent_input[i].value(), board_size+100, y_pos+(i+1)*40);
      text(str(100-percent_sum), board_size+150, y_pos+(i+1)*40);
    }
    else{
      text("N/A", board_size+100, y_pos+(i+1)*40);
      text("N/A", board_size+150, y_pos+(i+1)*40);
    }
    
    percent_sum = percent_sum + float(percent_input[i].value())
  }

  if (cell_num/cell_num_previous != 1 || num_populations/num_populations_previous != 1 || percent_empty_previous != percent_empty){
    initialize(board_size, cell_num, percent_empty, percent_pops)
  }


  for(i = num_populations-1; i<10; i++){
      percent_input[i].hide()
  }
  for( i = 0; i<num_populations-1; i++){
      percent_input[i].show()
  }

  

  
  cell_num_previous = cell_num
  num_populations_previous = num_populations
  percent_empty_previous = percent_empty
  percent_pops_previous = percent_pops
}