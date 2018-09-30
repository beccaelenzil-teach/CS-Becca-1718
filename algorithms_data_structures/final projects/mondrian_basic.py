#
#  Draw random "art" in a Mondrian style
#
import tkinter as tk
from random import randrange, random

WIDTH = 1024
HEIGHT = 768

SPLIT_LOW = 120
SPLIT_PENALTY = 1.5

#
# Select a color randomly
#
def randomColor():
  rv = random()
  if rv < 0.0833:
    return "red"
  elif rv < 0.1667:
    return "skyblue"
  elif rv < 0.25:
    return "yellow"
  elif rv < 0.5:
    return "orange"
  else:
    return "white"

#
# Split the region both vertically and horizontally
#
def split_both(x, y, w, h, canvas):
  hsp = randrange(33, 68) / 100
  vsp = randrange(33, 68) / 100
  left_width = round(hsp * w)
  right_width = w - left_width
  top_height = round(vsp * h)
  bottom_height = h - top_height
  mondrian(x, y, left_width, top_height, canvas)
  mondrian(x + left_width, y, right_width, top_height, canvas)
  mondrian(x, y + top_height, left_width, bottom_height, canvas)
  mondrian(x + left_width, y + top_height, right_width, bottom_height, canvas)

#
# Split so that the regions are side by side
#
def split_h(x, y, w, h, canvas):
  hsp = randrange(33, 68) / 100
  left_width = round(hsp * w)
  right_width = w - left_width
  mondrian(x, y, left_width, h, canvas)
  mondrian(x + left_width, y, right_width, h, canvas)

#
# Split so that one region is above the other
#
def split_v(x, y, w, h, canvas):
  vsp = randrange(33, 68) / 100
  top_height = round(vsp * h)
  bottom_height = h - top_height
  mondrian(x, y, w, top_height, canvas)
  mondrian(x, y + top_height, w, bottom_height, canvas)

#
# Use recursion to draw "art" in a Mondrian style
#
def mondrian(x, y, w, h, canvas):
  # Splits based on the size of the region
  if w > WIDTH / 2 and h > HEIGHT / 2:
    split_both(x, y, w, h, canvas)
  elif w > WIDTH / 2:
    split_h(x, y, w, h, canvas)
  elif h > HEIGHT / 2:
    split_v(x, y, w, h, canvas)
  else:
    # Splits based on random chance
    hsplit = randrange(SPLIT_LOW, max(round(SPLIT_PENALTY * w) + 1, \
                       SPLIT_LOW + 1))
    vsplit = randrange(SPLIT_LOW, max(round(SPLIT_PENALTY * h) + 1, \
                       SPLIT_LOW + 1))

    if hsplit < w and vsplit < h:
      split_both(x, y, w, h, canvas)
    elif hsplit < w:
      split_h(x, y, w, h, canvas)
    elif vsplit < h:
      split_v(x, y, w, h, canvas)

    # No split -- fill the region with yellow, blue, red or white
    else:
      color = randomColor()
      canvas.create_rectangle(x, y, x + w, y + h, \
                              fill=color, outline="black", width=3)

def main():
  # Create a window with a canvas
  master = tk.Tk()
  canvas = tk.Canvas(master, width=WIDTH, height=HEIGHT)
  canvas.pack()

  # Draw the art
  mondrian(0, 0, 1024, 768, canvas)
  tk.mainloop()

main()
