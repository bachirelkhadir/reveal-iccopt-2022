from manimlib import *
exec(get_custom_config()["universal_import_line"])
from colors import *
import numpy as np
from common import *
from manimslides import SlideScene


np.random.seed(0)

t2c={"{x}": RED, "y": BLUE}

DEBUG = False

class CauchySchwarz(SlideScene):
    CONFIG = {
#    '{V}': "#72d8ff",
        'color_x': "#94ff90",
        'color_y': YELLOW,
        'color_arrow': WHITE,
        'video_shift': DOWN
    }


    def make_arrow(self, a, b):
        arrow = Arrow(a, b, max_tip_length_to_length_ratio=.05)

        arrow.set_color(self.color_arrow)
        return arrow.set_stroke(width=1)

    
    def construct(self):

        if DEBUG:
            pass
            #helper_grid(self)

        # Show theorem
        self.show_cauchy_schwarz()
        self.slide_break()

        # Show hints
        self.show_ideas()

        # video place holders
        video_placeholder = ImageMobject("assets/c4_placeholder.png")\
            .set_width(FRAME_WIDTH)
        video_placeholder.scale(.75).shift(self.video_shift+DOWN)
        if DEBUG:
            self.add(video_placeholder)


        self.show_one_line_proof()
        self.slide_break()




        self.wait(1)


    def show_ideas(self):
        idea_txt = r"""Generalizes Cauchy-Schwarz inequality
        If $Q \succeq 0$ (i.e., $p(x) = x^TQx$ convex)
        $x^TQy \le \sqrt{p(x)}\sqrt{p(y)}$"""
        lab_gen_cs = VGroup(
            Text("Generalizes Cauchy-Schwarz inequality",
                 t2w={"Cauchy-Schwarz": BOLD},).scale(.9),
            Tex(r"\text{If}  Q \succeq 0  (\text{i.e.}, p(x) = x^TQx \text{convex})"),
            Tex(r"x^TQy \le \sqrt{p(x)}\sqrt{p(y)}")

        )
        lab_gen_cs.scale(.5)

        lab_gen_cs.arrange(DOWN)

        lab_gen_cs.to_corner(UR)

        for lab in lab_gen_cs:
            self.add(lab)
            self.slide_break()



        



    def show_cauchy_schwarz(self):
        cs_assumption = Text("For any convex form of degree 4").scale(.9)
        cs_inequality = Tex(r"\frac1{12} {x}^T \nabla^2p(y) {x} \le \sqrt{p(x)} \sqrt{p(y)} \quad \forall {x} , y \in \mathbb R^n",
                            tex_to_color_map=t2c)

        VGroup(cs_assumption, cs_inequality).arrange(DOWN)
        cs_thm = make_thm(VGroup(cs_assumption, cs_inequality), )
        cs_thm.scale(.6).to_corner(UL)
        self.add(cs_thm)


    def show_one_line_proof(self):
        lab_one_line_proof = Tex(r"p({x})p(y) - \left(\frac1{12} {x}^T \nabla^2p(y) {x} \right)^2 = \frac1{12} \,p(y)\,({x} -\lambda y)^T \nabla^2p({x} + \lambda y)({x} -\lambda y)", tex_to_color_map=t2c)

        lab_lambda = Tex(r"\left(\text{with } \lambda = \sqrt{{x^T\nabla^2p(y)x} \over {p(y)}}\, \right)",)

        lab_one_line_proof.scale(.7)\
                          .shift(LEFT+UP/2)
        lab_lambda.scale(.4).next_to(lab_one_line_proof, RIGHT, SMALL_BUFF)
        self.add(lab_one_line_proof)
        self.add(lab_lambda)
        

#
