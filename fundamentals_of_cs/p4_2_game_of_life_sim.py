import arcade
import p4_2_game_of_life as life


def constants():
    width = 60
    height = 60
    cell_size = 12
    spacing = 1
    return [width,height,cell_size, spacing]

def draw_board(dt):

    [width,height,cell_size, spacing] = constants()

    global A

    A = life.next_life_generation(A)

    # Start the render process. This must be done before any drawing commands.
    arcade.start_render()

    for row in range(1,height):
        x_pos = row*(cell_size+spacing)
        for col in range(1,width):
            y_pos = col*(cell_size+spacing)
            if A[row][col] == 1:
                arcade.draw_rectangle_filled(x_pos, y_pos, cell_size, cell_size, arcade.color.WHITE)
            elif A[row][col] == 0:
                arcade.draw_rectangle_filled(x_pos, y_pos, cell_size, cell_size, arcade.color.BLACK)

def main():

    [width,height,cell_size, spacing] = constants()

    # Open the window. Set the window title and dimensions (width and height)
    arcade.open_window(width*(cell_size+spacing), height*(cell_size+spacing), "Game Of Life")

    # Set the background color to BLACK
    arcade.set_background_color(arcade.color.BLACK)

    global A
    A = life.randomCells(width,height)

    arcade.schedule(draw_board, 1/80)

    # Finish the render.
    # Nothing will be drawn without this.
    # Must happen after all draw commands
    arcade.finish_render()

    # Keep the window up until someone closes it.
    arcade.run()

main()


