# cp ~/Dropbox/Thesis_ORFE_2020/Slides/CONVSOS/media/videos/min_convex_polynomial/720p30/MinConvexPolyScene.mp4 ~/Dropbox/Thesis_ORFE_2020/Slides/reveal.js/videos/CONV/ && cd ~/Dropbox/Thesis_ORFE_2020/Slides/reveal.js/videos/CONV/


DEBUG = False

import sys
sys.path.append('~/Dropbox/Thesis_ORFE_2020/Slides/CONVSOS/')
sys.path.append('/home/bachir/Dropbox/Thesis_ORFE_2020/Slides/common_imports/')
sys.DEBUG = DEBUG
from scipy.integrate import odeint
from manimlib.imports import *
from character_guy import CharacterGuy
from scipy import linalg
import colorsvg
import numpy as np
from color_map import *
from helper_functions import *


class MinConvexPolyScene(MovingCameraScene):
    def construct(self):


        placeholder = ImageMobject("media/min_convex_poly.png")
        placeholder.scale(5).fade(.8)
        #self.add(placeholder)


        self.setup_labels()
        self.setup_arrows_and_circle()
        


        self.add(self.label_pop)
        add_black_screen(self)

        self.add(self.label_p_convex_poly)
        add_black_screen(self)

        self.add(self.arrow_left)
        self.add(self.label_descent_method)
        add_black_screen(self)

        self.add(self.arrow_right)
        self.add(self.label_sos_hierarchy)
        add_black_screen(self)

        
        self.play(ShowCreation(self.circle))
        add_black_screen(self)


        self.add(self.label_if_we_knew)
        add_black_screen(self)

        self.add(self.label_then)
        add_black_screen(self)








    def setup_labels(self):
        self.label_pop = TexMobject(r"\displaystyle p^* = \min_{x \in \mathbb R^n} p(x)")
        self.label_p_convex_poly = TextMobject("$p$", " convex", " polynomial")
        self.label_p_convex_poly[1].set_color(MAROON_A)
        self.label_p_convex_poly[2].set_color(BLUE_B)
        
        self.label_descent_method = TextMobject(r"Descent methods\\\vspace{.5cm}$x_{k+1} = x_k - \alpha \nabla p(x_k)$")
        self.label_sos_hierarchy = VGroup(TextMobject(r"SOS hierarchies\\\vspace{.5cm}$p^{(1)} = \max \gamma$ s.t. $p - \gamma$ is sos"),
                                          TexMobject(r"\bf \Huge \vdots").shift(1.5*DOWN))
        
        self.label_if_we_knew = TextMobject(r"{\bf If we knew}", r" that $p - \gamma$ nonnegative $\Rightarrow p - \gamma$ sos")
        self.label_then = TextMobject(r"{\bf Then}", r" $p^{(1)}$ would be exact; $p^* = p^{(1)}$ ")
        self.label_if_we_knew[0].set_color(YELLOW)
        self.label_then[0].set_color(YELLOW)


        # placement
        self.label_pop.to_corner(UP)
        self.label_p_convex_poly.next_to(self.label_pop, DOWN)

        self.label_descent_method.scale(.7)\
                                 .shift(DOWN+4*LEFT)

        self.label_sos_hierarchy.scale(.7).\
            align_to(self.label_descent_method, UP)\
            .shift(4*RIGHT)

        self.label_if_we_knew.scale(.75).to_corner(DOWN).shift(UP/2)
        self.label_then.scale(.75).next_to(self.label_if_we_knew, DOWN)
        align_group_text([self.label_if_we_knew, self.label_then], LEFT)


    def setup_arrows_and_circle(self):
        self.arrow_left = CurvedArrow(start_point=self.label_p_convex_poly[1].get_corner(DL), 
                                      end_point=self.label_descent_method.get_corner(UP),
                                      color=MAROON_A, angle=TAU/10)
        self.arrow_right = CurvedArrow(start_point=self.label_p_convex_poly[2].get_corner(DR), 
                                       end_point=self.label_sos_hierarchy.get_corner(UP),
                                       COLOR=BLUE_A, angle=-TAU/10)


        self.circle = DashedVMobject(Circle())\
            .scale((.6,.3,1))\
            .shift((4.9, -1.5, 0))


# Local Variables:
# compile-command: "/home/bachir/.local/bin/manim min_convex_polynomial.py MinConvexPolyScene -pl -c=#1f303e"
# End:

