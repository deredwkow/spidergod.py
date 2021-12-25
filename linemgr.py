# A separate .py for containing functions pertaining to creating each line to be drawn to canvas
import math

# The line class acts as an n-tree, with each payload consisting of the information necessary for drawing some line on a canvas and each child being another line object
class line:
    parent = startx = starty = endx = endy = children = None
    maxl = minl = None

    # Init is called whenever creating a new line. For some reason, Python's __init__ built-in function does not work in my current IDE.
    # Acts recursively as a tree generation tool.
    def init(self, x: int, y: int, direction_angle: int, projection_angle:int, branches: int, maxlen: int, minlen: int, depth: int):
        # Decrement depth by 1 per line
        if depth <= 0:
            return None
        depth -= 1
        self.generate_own_line(self, x, y, direction_angle, maxlen, minlen)
        self.generate_child_lines(self, x, y, direction_angle, projection_angle, branches, maxlen, minlen, depth)

    # Assigns each attribute necessary for drawing this particular line on canvas
    def generate_own_line(self, x, y, angle, maxlen, minlen):
        endpoint = self.get_max_endpoint(x,y,angle,maxlen)
        self.startx = x
        self.starty = y
        self.endx = endpoint[0]
        self.endy = endpoint[1]

    # Retrieves x and y coordinates for the expected end of a line before collision detection. Takes starting xy coordinates, the angle defining which direction to draw the line in, and
    # the maximum length allowed for a line
    @staticmethod
    def get_max_endpoint(x, y, angle, maxlength):
        angle %= 360
        length = maxlength
        # Handling for lines that go parallel to either the x or y axis
        if angle==90 or angle==270:
            return [0, length]
        elif angle==180 or angle==360 or angle==0:
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

    # Generates a set of segment coordinates that branch out from the endpoint of the current line
    def generate_child_lines(self, x: int, y: int, direction_angle: int, projection_angle:int, branches: int, maxlen: int, minlen: int, depth: int):
        self.children = []
        offset = projection_angle/(branches+1)
        starting_point = direction_angle+projection_angle
        for i in range(1, branches+1):
            l = line
            a = starting_point+(offset*i)
            l.init(l, x, y, a, projection_angle, branches, maxlen, minlen, depth)
            self.children.append(l)
