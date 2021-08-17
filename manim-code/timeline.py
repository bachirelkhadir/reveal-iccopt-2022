#!/usr/bin/env python3
from manimlib import *
exec(get_custom_config()["universal_import_line"])
import numpy as np
np.random.seed(0)


class Timeline(Scene):
    def construct(self):

        title = Text("Form of Degree 4 that is Convex but not SOS?").to_edge(UP)
        self.add(title)

        arrow = Vector().scale(10).shift(LEFT)
        lab_nvar = Text(r"# variables")
        lab_nvar.next_to(arrow, UR).shift(LEFT)
        self.add(arrow, lab_nvar)

        # hilbert bound


        hilbert_tick = Tex("]").move_to(arrow).shift(5*LEFT)
        hilbert_lab = Tex("3").next_to(hilbert_tick, UP)
        hilbert = Group(hilbert_tick, hilbert_lab)
        self.play(hilbert.animate.shift(RIGHT))

        # blekherman bound

        blek_tick = Tex("|").move_to(arrow).shift(5*LEFT)
        blek_lab = Tex("3").next_to(blek_tick, UP)
        blek = Group(blek_tick, blek_lab)
        self.play(blek.animate.shift(4*RIGHT))


        # james bound

        #today

        tick = Line().rotate(PI/2).scale(.2)
        n3 = tick.copy().shift(3*LEFT)
        n4 = n3.copy().shift(RIGHT)
        nhigh = n3.copy().shift(6*RIGHT)

        n3_lab = Tex("3")
        always(n3_lab.next_to, n3, UP)

        n4_lab = Tex("4")
        always(n4_lab.next_to, n4, UP)

        nhigh_lab = Text("high")
        always(nhigh_lab.next_to, nhigh, UP)

        self.add(n3, n4, nhigh)
        self.add(n3_lab, n4_lab, nhigh_lab)
        self.wait()
