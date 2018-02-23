var board_size = 600.0
var spacing = 1.0
var offset = 10.0
var cell_num = 20.0
var cell_num_previous = 20.0
var num_populations = 4
var num_populations_previous = 4
var percent_pops = []
var percent_pops_previous = []
var run
var reset
var reset_percent
var initialize_board = 1

function Cell(row,col,type){
  this.row = row
  this.col = col
  this.type = type
}

function createOneRow(row,cell_num,num_populations){
    single_row = []
    for (col = 0; col < cell_num; col++){
        cell = new Cell(row,col,0)
        single_row.push(cell)
    } 
    return single_row
}

function createBoard(cell_num){
    A = []
    for (row = 0; row < cell_num; row++){
        A.push(createOneRow(row,cell_num))
    }
    return A
}

function createModelBoard(percent_pops, cell_num){
  size = cell_num*cell_num
  size_pops = []
  size_pops.push(percent_pops[0]/100*size)

  size_left = size - size_pops[0]
  
  size_sum = 0

  for (j = 1; j < percent_pops.length-1; j++){
    size_current_pop = percent_pops[j]/100*size_left
    size_pops.push(size_current_pop)
    size_sum += size_current_pop
  }

  size_pops.push(size_left - size_sum)

  population = []
  for (k = 0; k < size_pops.length; k++){
    for (n = 0; n < size_pops[k]; n++){
      population.push(k)
    }
  }
  var new_population = shuffle(population)
  return new_population
 };

function populateBoard(cell_num, percent_pops){
  population = createModelBoard(percent_pops, cell_num)
  A = createBoard(cell_num)
  i = 0
  for (row = 0; row < cell_num; row++){
    for (col = 0; col < cell_num; col++){
      A[row][col].type = population[i]
      i++
    }
  }
  return A
}

function calculate_cell_size(board_size,cell_num){
  cell_size = (board_size-cell_num*spacing)/(cell_num)
  return cell_size
}

function drawBoard(A,cell_size,num_populations){
  for (row = 0; row < A[0].length; row++){
    y_pos = ((cell_size+spacing) * row) + offset
    for (col = 0; col < A.length; col++){
      x_pos = ((cell_size+spacing) * col) + offset
      for (pop = 0; pop < num_populations+1; pop++){
        if (A[row][col].type == pop && A[row][col].type != 0){
          R = (pop+1)*(255/num_populations)
          G = 20*i
          B = (num_populations - pop)*(255/num_populations)
          fill(R,G,B)
        }
        else if (A[row][col].type == 0){
          fill(255)
        }
      }
      rect(x_pos,y_pos,cell_size,cell_size)
    }
  }
  return color
}


function setup() { 
  createCanvas(board_size+2*offset+200, board_size+2*offset);

  percent_pops = [10, 25, 25, 25, 25]

  // inputs
  percent_input = []
  reset_percent = []

  for (i = 0; i<11; i++){
    percent_input[i] = createInput(10)
  }

  // sliders
  slider_cell_num = createSlider(4.0, 75.0, 20.0, 1.0);
  slider_cell_num.position(board_size+10, 50);
  slider_cell_num.style('width', '150px')

  slider_num_pops = createSlider(2, 10, 4, 1);
  slider_num_pops.position(board_size+10, 110);
  slider_num_pops.style('width', '150px')

  // button
  run = createButton('run');
  run.position(board_size+120, 10);

  reset = createButton('reset');
  reset.position(board_size+10, 10);

  cell_size = calculate_cell_size(board_size,cell_num)
  A = populateBoard(cell_num, percent_pops)

}

function draw(){
  
  background(0);

  num_populations = slider_num_pops.value()
  cell_num = slider_cell_num.value()

  
  percent_sum = 0
  
  for (i = 0; i<num_populations+1; i++){
    percent_input[i].position(board_size+50, 110+(i+1)*40);
    percent_input[i].style('width', '100px')


    percent_sum = percent_sum + float(percent_input[i])
    percent_pops[i] = float(percent_input[i].value())

    //reset_percent[i].position(board_size+110, 110+(i+1)*40);
      
    R = (i+1)*(255/num_populations)
    G = 20*i
    B = (num_populations - i)*(255/num_populations)
    if (i == 0){
      fill(255)
    }
    else{
      fill(R,G,B)
    }
    rect(board_size+20, 110+(i+1)*40,20,20)
    text(str(0), board_size+50, 110+(i+1)*40);
    text(percent_input[i].value(), board_size+100, 110+(i+1)*40);
    text(str(100-percent_sum), board_size+150, 110+(i+1)*40);
  }

  for (i = 0; i<num_populations+1; i++){
      
  }

  if (cell_num/cell_num_previous != 1 || num_populations/num_populations_previous != 1){
    cell_size = calculate_cell_size(board_size,cell_num)
    A = populateBoard(cell_num, percent_pops)
  }
  
  drawBoard(A,cell_size,num_populations)

  cell_num_previous = cell_num
  num_populations_previous = num_populations
  percent_pops_previous = percent_pops

}