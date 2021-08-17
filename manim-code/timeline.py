#!/usr/bin/env python3
from manimlib import *
exec(get_custom_config()["universal_import_line"])
import numpy as np
from colors import *
np.random.seed(0)


class Timeline(Scene):
    def construct(self):

        title = Text("Convex but not SOS?").to_edge(UP)
        self.add(title)

        arrow = Vector().scale(10).shift(LEFT)
        lab_nvar = Text(r"# variables")
        lab_nvar.next_to(arrow, UR).shift(LEFT)
        self.add(arrow, lab_nvar)

        # hilbert bound


        hilbert_tick = Tex("]").move_to(arrow).shift(5*LEFT)
        hilbert_lab = Tex("3").next_to(hilbert_tick, UP)
        hilbert_tracker = Line()\
            .set_stroke(color=BABY_PINK, width=30, opacity=.7)
        hilbert_tracker.add_updater(lambda z: z.become(Line(
            arrow.get_corner(LEFT), hilbert_tick).match_style(z)))
        hilbert = Group(hilbert_tick, hilbert_lab)
        self.add(hilbert_tracker)
        self.play(hilbert.animate.shift(RIGHT))
        self.wait()

        # blekherman bound

        blek_tick = Tex("|").move_to(arrow).shift(10*RIGHT)
        blek_lab = Tex("n").next_to(blek_tick, UP)
        blek_tracker = Line().set_stroke(color=BABY_GREEN, width=30, opacity=.7)
        blek_tracker.add_updater(lambda z: z.become(Line(
            arrow.get_corner(RIGHT), blek_tick).match_style(z)))
        blek = Group(blek_tick, blek_lab)
        self.add(blek_tracker)
        self.play(blek.animate.shift(8*LEFT))
        self.wait()

        blekh_lab_explicit = Tex(r"\sim 10^{10}").move_to(blek_lab)
        self.play(Transform(blek_lab, blekh_lab_explicit))
        self.wait()


        # james bound

        james_tick = Tex("|").move_to(arrow)
        james_lab = Tex("272").next_to(james_tick, UP)
        james = Group(james_tick, james_lab)
        self.play(FadeIn(james))
        self.wait()


        # bachir
        bachir_tick = Tex("|").move_to(arrow).shift(2*LEFT)
        bachir_lab = Tex("4").next_to(bachir_tick, UP)
        bachir = Group(bachir_tick, bachir_lab)
        self.play(FadeIn(bachir))
        self.wait()
