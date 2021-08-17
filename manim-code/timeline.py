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


        # green/red rects
        green_rect = Line()\
            .set_stroke(color=BABY_GREEN, width=30, opacity=.7)
        green_endpoint= Dot()
        green_rect.add_updater(lambda z: z.become(Line(arrow.get_corner(RIGHT), green_endpoint).match_style(z)))
        self.add(green_rect, green_endpoint)


        red_rect = Line()\
            .set_stroke(color=BABY_PINK, width=30, opacity=.7)
        red_endpoint= Dot()
        red_rect.add_updater(lambda z: z.become(Line(arrow.get_corner(LEFT), red_endpoint).match_style(z)))
        self.add(red_rect, red_endpoint)

        def match_fct(obj):
            return lambda z: z.move_to(obj)



        # hilbert bound


        hilbert_tick = Tex("]").move_to(arrow).shift(5*LEFT)
        hilbert_lab = Tex("3").next_to(hilbert_tick, UP)
        hilbert = Group(hilbert_tick, hilbert_lab)
        match_hilbert = match_fct(hilbert_tick)
        red_endpoint.add_updater(match_hilbert)
        self.play(hilbert.animate.shift(RIGHT))
        red_endpoint.remove_updater(match_hilbert)
        self.wait()

        # blekherman bound

        blek_tick = Tex("|").move_to(arrow).shift(10*RIGHT)
        blek_lab = Tex("n").next_to(blek_tick, UP)
        blek = Group(blek_tick, blek_lab)

        match_hilbert = match_fct(hilbert_tick)
        green_endpoint.add_updater(match_blek)
        self.play(blek.animate.shift(8*LEFT))
        green_endpoint.remove_updater(match_blek)
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
