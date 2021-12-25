from tkinter import *
from tkinter import ttk
import drawer

def inst():
    w = window
    w.init(w)
    return w

class window:

    def init(self):
        self.init_main_window(self)
        self.init_buttons(self)
        self.root.mainloop()

    def init_main_window(self):
        print('todo')
    # set window title

    # set window size

    def init_buttons(self):
        self.init_web_display(self)
     #   self.init_animation_buttons(self)
        self.init_vector_buttons(self)
        self.init_download_buttons(self)
        self.init_line_buttons(self)


    #
    # Line options
    #
    def init_line_buttons(self):
        self.init_line_base(self)
        self.init_line_dotted(self)
        self.init_line_spiral(self)

    # Base options init
    def init_line_base(self):
        baseframe = ttk.Frame(self.lineframe)
        baseframe.pack(side=TOP)

        self.drawbutton = Button(baseframe, text='Draw', command=lambda: drawer.draw(self.canvas, self.config))
        self.drawbutton.grid(row=0, column=0)

        # Thickness adjustment option
        thickness_label = Label(baseframe, text='Thickness:')
        thickness_label.grid(row=1, column=0)
        self.line_thickness = Entry(baseframe, textvariable=StringVar())
        self.line_thickness.grid(row=1, column=1)
        self.config.update({'thickness': self.line_thickness})

        # Max branches per line
        max_children_label = Label(baseframe, text='Maximum branches per line:')
        max_children_label.grid(row=1, column=2)
        self.max_branches = Entry(baseframe, textvariable=StringVar())
        self.max_branches.grid(row=1, column=3)
        self.config.update({'max_branches': self.max_branches})

        # Max tree depth
        depth_label = Label(baseframe, text='Depth:')
        depth_label.grid(row=1, column=4)
        self.depth = Entry(baseframe, textvariable=StringVar())
        self.depth.grid(row=1, column=5)
        self.config.update({'depth': self.depth})

        # Max line length parameter
        max_length_label = Label(baseframe, text='Maximum line length:')
        max_length_label.grid(row=2, column=0)
        self.line_length_max = Entry(baseframe, textvariable=StringVar())
        self.line_length_max.grid(row=2, column=1)
        self.config.update({'max_line_length': self.line_length_max})

        # Minimum line length parameters
        min_length_label = Label(baseframe, text='Minimum line length:')
        min_length_label.grid(row=2, column=2)
        self.line_length_min = Entry(baseframe, textvariable=StringVar())
        self.line_length_min.grid(row=2, column=3)
        self.config.update({'min_line_length': self.line_length_min})

        # Starting x coordinate
        starting_x_label = Label(baseframe, text='Starting x:')
        starting_x_label.grid(row=3, column=0)
        self.starting_x = Entry(baseframe, textvariable=StringVar())
        self.starting_x.grid(row=3, column=1)
        self.config.update({'starting_x': self.starting_x})

        # Starting y coordinate
        starting_y_label = Label(baseframe, text='Starting y:')
        starting_y_label.grid(row=3, column=2)
        self.starting_y = Entry(baseframe, textvariable=StringVar())
        self.starting_y.grid(row=3, column=3)
        self.config.update({'starting_y': self.starting_y})

        # Starting angle
        starting_angle_label = Label(baseframe, text='Starting angle').grid(row=3,column=4)
        self.starting_angle = Entry(baseframe, textvariable=StringVar())
        self.starting_angle.grid(row=3, column=5)
        self.config.update({'starting_angle': self.starting_angle})

        projection_angle_label = Label(baseframe, text='Branching projection angle').grid(row=3,column=6)
        self.branching_projection_angle = Entry(baseframe, textvariable=StringVar())
        self.branching_projection_angle.grid(row=3, column=7)
        self.config.update({'projection_angle': self.branching_projection_angle})

    def init_line_dotted(self):
        dlframe = ttk.Frame(self.lineframe)
        # Toggle option
        self.line_dotted_toggle = Button(dlframe, text="+", command=lambda: self.line_toggle_dotted(self))
        ttk.Label(dlframe, text="Dotted").pack(side=LEFT)
        self.line_dotted_toggle.pack(side=RIGHT)
        dlframe.pack(side=LEFT)

        # Whitespace-to-line ratio


    def init_line_spiral(self):
        # Spiral line options buttons frame
        sltop = ttk.Frame(self.lineframe)
        slmain = ttk.Frame(sltop)
        slmain.pack(side=BOTTOM)

        # Toggle option
        self.line_spiral_toggle = Button(sltop, text="+", command=lambda: self.line_toggle_spiral(self))
        ttk.Label(sltop, text="Spiral").pack(side=LEFT)
        self.line_spiral_toggle.pack(side=RIGHT)

        # Radius option
        radius_label = ttk.Label(slmain, text="Radius")
        radius_box = ttk.Entry(slmain, validate='all', validatecommand='%d')
        self.line_spiral_buttons.update({'radiuslab': radius_label})
        self.line_spiral_buttons.update({'radiusval': radius_box})

        sltop.pack(side=LEFT)

    #
    # Line menu toggles

    # Toggles the dotted line settings menu
    def line_toggle_dotted(self):
        if self.line_dotted_toggle['text'] == '+':
            self.line_dotted_toggle['text'] = '-'
        else:
            self.line_dotted_toggle['text'] = '+'

    # Toggles the dotted line settings menu
    def line_toggle_spiral(self):
        if self.line_spiral_toggle['text'] == '+':
            self.line_spiral_toggle['text'] = '-'
            self.line_spiral_buttons.get('radiusval').grid(row=0, column=1)
            self.line_spiral_buttons.get('radiuslab').grid(row=0, column=0)
        else:
            self.line_spiral_toggle['text'] = '+'
            self.line_spiral_buttons.get('radiusval').grid_forget()
            self.line_spiral_buttons.get('radiuslab').grid_forget()
    #
    # Animation options
    #
    def init_animation_buttons(self):
        # Toggle checkbox for enabling/disabling animation
        self.anim_toggle = Button(self.frm, text="Enable animation", command=lambda: self.toggle_animation(self))
        self.anim_toggle.pack()

        # Scale for setting the speed of the animation
        anim_speed = Scale(self.frm)
        anim_speed['state'] = DISABLED
        anim_speed.pack()
        self.anim_buttons.update({'speed': anim_speed})

        # Init animation style options
        # Draw the line backwards
        anim_style_backwards = Checkbutton(self.frm, text="Backwards", var=self.anim_backwards_var, command=lambda: self.anim_toggle_backwards(self))
        anim_style_backwards.pack()
        self.anim_buttons.update({'style_backwards': anim_style_backwards})
        # Draw the line straight
        anim_style_straight = Checkbutton(self.frm, text="Straight", var=self.anim_straight_var, command=lambda: self.anim_toggle_straight(self))
        anim_style_straight.pack()
        self.anim_buttons.update({'style_straight': anim_style_straight})

        self.toggle_animation(self)

    def init_anim_buttons_forwards(self):
        # Draw the line forwards
        anim_style_forwards = Checkbutton(self.frm, text="Forward", var=self.anim_forwards_var, command=lambda: self.anim_toggle_forwards(self))
        anim_style_forwards.grid(row=1, column=5)
        self.anim_buttons.update({'style_forwards': anim_style_forwards})

    #
    # Animation menu toggles
    def toggle_animation(self):
        if self.anim_toggle['text'] == 'Enable animation':
            for key in self.anim_buttons:
                self.anim_buttons.get(key)['state'] = NORMAL
            self.anim_toggle['text'] = 'Disable animation'
        else:
            for key in self.anim_buttons:
                self.anim_buttons.get(key)['state'] = DISABLED
            self.anim_toggle['text'] = 'Enable animation'
        print('toggle')

    def init_vector_buttons(self):
        print('todo')

    def init_download_buttons(self):
        print('todo')

    def init_web_display(self):
        print('todo')


    #
    # main functions

    # Root init
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.pack()

    # Canvas
    canvasframe = ttk.Frame(frm, padding=10)
    canvas = Canvas(canvasframe, bg='white', height=800, width=1000)
    canvas.grid(row=0,column=0)
    canvasframe.pack(side=TOP)

    # Base options set
    config = {}
    line_color = line_count_max = line_thickness = line_length_max = line_length_min = None
    starting_x = starting_y = starting_angle = None
    max_branches = depth = branching_projection_angle = None

    # Line buttons
    lineframe = ttk.Frame(frm, padding=10)
    lineframe.pack(side=LEFT)
    line_options_main = {}
    line_dotted_toggle = None
    line_dotted_buttons = {}
    line_spiral_toggle = None
    line_spiral_buttons = {}

    # Animation buttons
    anim_toggle = None
    anim_buttons = {}
    anim_dotted_var = IntVar()
    anim_straight_var = IntVar()
    anim_spiral_var = IntVar()
    anim_backwards_var = IntVar()
    anim_forwards_var = IntVar()

    # Point buttons
    point_max = point_colors = None