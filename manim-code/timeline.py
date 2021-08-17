#!/usr/bin/env python3
from manimlib import *
exec(get_custom_config()["universal_import_line"])
import numpy as np
from colors import *
np.random.seed(0)

def add_author(name, pos):
    wedge = Triangle().move_to(pos).scale(.1).shift(DOWN/3)
    wedge.set_fill(color=BABY_YELLOW, opacity=1)
    wedge.set_stroke(opacity=0)
    lab = Text(name).scale(.6).rotate(-PI/3).next_to(wedge, DOWN,)
    lab.set_color(BABY_YELLOW).shift(RIGHT/3)
    return Group(wedge, lab)


class Timeline(Scene):
    def wait(self):
        color = BLACK
        timeout = 1
        rect = Rectangle(fill_color=color, strole_color=color, fill_opacity=1).scale(100)
        super().wait(timeout)
        self.add(rect)
        super().wait(timeout)
        self.remove(rect)

    def construct(self):

        title = Text("Convex but not SOS?").to_edge(UP)
        self.add(title)

        arrow = Vector().scale(10).shift(LEFT)
        lab_nvar = Text(r"# variables")
        lab_nvar.next_to(arrow, UR).shift(LEFT)
        self.play(GrowArrow(arrow))
        self.add(lab_nvar)
        self.wait()


        # green/red rects
        green_rect = Line()\
            .set_stroke(color=BABY_GREEN, width=30, opacity=.7)
        green_endpoint= Dot(color=BABY_GREEN).move_to(arrow.get_corner(RIGHT))
        green_rect.add_updater(lambda z: z.become(Line(arrow.get_corner(RIGHT), green_endpoint.get_center()-.01*RIGHT).match_style(z)))
        self.add(green_rect, green_endpoint)


        red_rect = Line()\
            .set_stroke(color=BABY_PINK, width=30, opacity=.7)
        red_endpoint= Dot(color=BABY_PINK).move_to(arrow.get_corner(LEFT))
        red_rect.add_updater(lambda z: z.become(Line(arrow.get_corner(LEFT), red_endpoint.get_center()).match_style(z)))
        self.add(red_rect, red_endpoint)
        green_endpoint.set_opacity(0)
        red_endpoint.set_opacity(0)

        def match_fct(obj):
            return lambda z: z.move_to(obj)



        # hilbert bound


        hilbert_tick = Tex("]").move_to(arrow).shift(5*LEFT)
        hilbert_lab = Tex("3").next_to(hilbert_tick, UP)
        hilbert_name = add_author("1888, Hilbert", hilbert_tick)
        hilbert = Group(hilbert_tick, hilbert_lab, hilbert_name)
        match_hilbert = match_fct(hilbert_tick)
        red_endpoint.add_updater(match_hilbert)
        self.play(hilbert.animate.shift(RIGHT))

        red_endpoint.remove_updater(match_hilbert)
        self.wait()

        # blekherman bound

        blek_tick = Tex("|").move_to(arrow).shift(10*RIGHT)
        blek_lab = Tex("n").next_to(blek_tick, UP)

        blek_name = add_author("09', Blekherman", blek_tick)
        blek = Group(blek_tick, blek_lab, blek_name)

        match_blek = match_fct(blek_tick)
        green_endpoint.add_updater(match_blek)
        self.play(blek.animate.shift(8*LEFT))
        green_endpoint.remove_updater(match_blek)
        self.wait()

        blekh_lab_explicit = Tex(r"\sim 10^{10}").move_to(blek_lab)
        self.play(Transform(blek_lab, blekh_lab_explicit))
        self.wait()


        # james bound

        james_tick = Tex("|").move_to(arrow).move_to(blek_tick)
        james_lab = Tex("272").next_to(james_tick, UP)
        james_name = add_author("21', Saunderson", james_tick)
        james = Group(james_tick, james_lab, james_name)

        match_james = match_fct(james_tick)
        green_endpoint.add_updater(match_james)
        self.play(FadeIn(james), james.animate.shift(2*LEFT))

        green_endpoint.remove_updater(match_james)
        self.wait()


        # bachir
        bachir_tick = Tex("|").move_to(hilbert_tick)
        bachir_lab = Tex("4").next_to(bachir_tick, UP)
        bachir_name = add_author("Today", bachir_tick)
        bachir = Group(bachir_tick, bachir_lab, bachir_name)
        match_bachir = match_fct(bachir_tick)
        red_endpoint.add_updater(match_bachir)
        self.play(FadeIn(bachir), bachir.animate.shift(RIGHT))
        red_endpoint.remove_updater(match_bachir)
        self.wait()


        # remove names
        self.remove(bachir_name, hilbert_name, james_name, blek_name)
        self.wait()
