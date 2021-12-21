import math
width = height = thickness = maxlen = None

# Three main functions:
#         -draw() is called by the window when the "Draw" button is pressed and supervises drawing
#         -collect_lines() calculates the coordinates of every line according to specifications in the config list
#         -drawlines() actually puts the lines in the list on the canvas. this function exists separately from the other two in order to make room for future animation handling
def draw(newcanvas, config):
    width = newcanvas.winfo_width()
    height = newcanvas.winfo_height()
    thickness = checkfloat(config.get('thickness').get())
    maxlen = checkfloat(config.get('max_line_length').get())
    min_line_length = checkfloat(config.get('min_line_length').get())

    starting_x = checkfloat(config.get('starting_x').get())
    starting_y = checkfloat(config.get('starting_y').get())
    starting_angle = checkfloat(config.get('starting_angle').get())

    branches = checkfloat(config.get('max_branches').get(), 5)
    max_depth = checkfloat(config.get('max_depth').get(), 2)
    projection_angle = checkfloat(config.get('projection_angle').get(), 180)
    # Get the first set of lines branching out from the starting coordinates
    current_depth = 1
    lineset = get_next_lineset(starting_x, starting_y, maxlen, branches=branches, projection_angle=projection_angle)
    # Loop to draw until the maximum depth has been reached
    while current_depth<=max_depth:
        lineset = replace_lineset(newcanvas, lineset, branches, projection_angle)
        current_depth += 1

# Creates a set of line coordinates to be drawn given initial x and y values and the maximum length allowed for drawing lines
def get_next_lineset(x, y, maxlength, branches, projection_angle, minlength=0):
    ret = []
    lilangle = projection_angle/branches
    bigangle = lilangle/2
    # Each line begins at a different angle
    for line in range(branches):
        angle = bigangle%90 if bigangle>90 else bigangle
        coordinates = get_next_coordinates(x, y, angle, maxlength)
        ret.append([x,y,coordinates[0],coordinates[1]])
    return ret

# Adjust x and y coordinates based on which quadrant they should appear in given an angle and some particular line length
def get_next_coordinates(x, y, angle, length):
    # Handling for lines that go parallel to either the x or y axis
    if angle==90 or angle==270:
        return [0, length]
    elif angle==180 or angle==360:
        return [length, 0]
    # Handling for lines projecting into the first quadrant (positive x and positive y)
    if angle<90:
        return [ (math.sin(angle)*length)+x, (math.cos(angle)*length)+y ]
    # Handling for lines projecting into the second quadrant (negative x and positive y)
    elif angle<180:
        angle = angle%90
        return [ -(math.sin(angle)*length)+x, (math.cos(angle)*length)+y ]
    # Handling for lines projecting into the third quadrant (negative x and negative y)
    elif angle<270:
        angle = angle%90
        return [ -(math.sin(angle)*length)+x, -(math.cos(angle)*length)+y ]
    # Handling for lines projecting into the fourth quadrant (positive x and negative y)
    elif angle<360:
        angle = angle%90
        return [ (math.sin(angle)*length)+x, -(math.cos(angle)*length)+y ]

# Takes a set of coordinate arrays (lines), draws them, and returns an array of new lines
def replace_lineset(canvas, lineset, branches, projection_angle):
    for i in range(len(lineset)):
        line = lineset[i]
        if type(line[0]) is list:
            lineset[i] = replace_lineset(line)
        else:
            canvas.create_line(line[0], line[1], line[2], line[3], width=thickness)
            lineset[i] = get_next_lineset(line[2], line[3], length, branches, projection_angle)
    return lineset

def get_line(startx, starty, nextx, nexty):
    return [newy, newx, starty, startx]

def checkfloat(val, substitute=-1):
    print(val)
    try:
        return float(val)
    except Exception:
        return substitute
