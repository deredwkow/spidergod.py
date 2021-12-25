import math

import linemgr

width = height = thickness = maxlen = None

# Three main functions:
#         -draw() is called by the window when the "Draw" button is pressed and initializes the tree of coordinate values used when drawing lines to canvas
#         -drawlines() actually puts the lines in the list on the canvas. this function exists separately from the other two in order to make room for future animation handling
def draw(newcanvas, config):
    width = newcanvas.winfo_width()
    height = newcanvas.winfo_height()

    # Grab some values from 'config' and run an error check on each of them to get either the user's input or a default value
    starting_x = checkfloat(config.get('starting_x').get(), 0)
    starting_y = checkfloat(config.get('starting_y').get(), 0)
    starting_angle = checkfloat(config.get('starting_angle').get(), 0)
    maxlen = checkfloat(config.get('max_line_length').get(), 500)
    minlen = checkfloat(config.get('min_line_length').get(), 0)
    projection_angle = checkfloat(config.get('projection_angle').get(), 180)
    depth = checkfloat(config.get('depth').get(), 5)
    branches = checkfloat(config.get('max_branches').get(), 5)

    # Initialize the first line in an n-tree of lines with the values grabbed from the config list
    parent_line = linemgr.line
    parent_line.init(parent_line, starting_x, starting_y, starting_angle, projection_angle, branches, maxlen, minlen, depth)

    # test function for basic drawing of tree
    draw_top_to_bottom(newcanvas, parent_line)

def draw_top_to_bottom(canvas, parent_line):
    canvas.create_line(parent_line.startx, parent_line.starty, parent_line.endx, parent_line.endy, width=1)
    for line in parent_line.children:
        draw_top_to_bottom(canvas, line)

def checkfloat(val, substitute=-1, expected_type=int):
    print(val)
    try:
        return expected_type(val)
    except Exception:
        return substitute
