from helpers import *

from mobject.tex_mobject import TexMobject
from mobject import Mobject
from mobject.image_mobject import ImageMobject
from mobject.vectorized_mobject import *

from animation.animation import Animation
from animation.transform import *
from animation.simple_animations import *
from animation.playground import *
from topics.geometry import *
from topics.characters import *
from topics.functions import *
from topics.fractals import *
from topics.number_line import *
from topics.combinatorics import *
from topics.numerals import *
from topics.three_dimensions import *
from topics.objects import *
from scene import Scene
from scene.zoomed_scene import ZoomedScene
from scene.reconfigurable_scene import ReconfigurableScene
from camera import Camera
from mobject.svg_mobject import *
from mobject.tex_mobject import *

from topics.graph_scene import GraphScene
from old_projects.eoc.chapter2 import Car, MoveCar
from topics.common_scenes import OpeningQuote, PatreonThanks

class GraphReward(GraphScene):
    CONFIG = {
        "graph_origin" : 3.25*LEFT+2.5*DOWN,
        "x_min" : 0,
        "x_max" : 10,
        "x_axis_width" : 9,
        "x_labeled_nums" : range(1,10,1),
        "x_axis_label" : "Time",
        "y_min" : 0,
        "y_max" : 10,
        "y_tick_frequency" : 1,
        "y_labeled_nums" : range(1,10,1),
        "y_axis_label" : "Reward",
        "exclude_zero_label" : True,
        "num_rings_in_ring_sum_start" : 3,
        "tick_height" : 1,
        "array" : [1,2,5,8,4,6,3,7]
    }
    def setup(self):
        array = self.array
        self.y_max = max(array)
        self.x_max = len(array)+1
        self.setup_axes()

    def construct(self):
        self.drawGraph()

    def drawGraph(self):

        rects = self.bar_graph_bars(
                    self.array, dx = 1,
                    start_color = RED,
                    end_color = ORANGE,
                    width_scale_factor = 0.2
                )
        self.add(rects)
        self.rects = rects
        origin = rects[2].get_critical_point(ORIGIN)
        print(origin)
        path = FunctionGraph(sigmoid,x_min=-6,x_max=7)
        self.play(ShowCreation(self.rects))
        self.play(DrawBorderThenFill(self.rects[4]))
        self.play(ApplyWave(self.rects))
        # self.play(MoveAlongPath(self.rects[2],path))
        self.play(self.rects[0].move_to,self.rects[6])
        self.play(
                self.rects[2].shift, RIGHT*1.3,
                self.rects[2].shift, UP*2.2,
                )
        self.rects[7].save_state()
        self.play(
                self.rects[7].highlight, YELLOW,
                self.rects[7].scale, 1.05, self.rects[7].get_center_of_mass(),
                )
        self.play(self.rects[7].restore)
        self.play(
                self.rects.scale, 0.01,
                self.rects.to_corner, UP,
                )
        self.dither(2)


