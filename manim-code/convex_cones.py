#!/usr/bin/env python3
from manimlib import *
exec(get_custom_config()["universal_import_line"])
from colors import *
import numpy as np
from manimslides import SlideScene

class ConvexConesSVG(SVGMobject):
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, "assets/convex_cones_with_tangents.svg")

        index_nonneg= 0
        index_sos= 1
        index_convex_out= 2
        index_convex_in= 3
        index_tangents_conv= 4
        index_tangents_sos= 11
        parts = self.parts = {
            "nonneg": self[index_nonneg],
            "sos": self[index_sos],
            "convex_out": self[index_convex_out],
            "convex_in": self[index_convex_in],
            "tangents_conv": self[index_tangents_conv:index_tangents_sos],
            "tangents_sos": self[index_tangents_sos:],
        }
        colors = {
            "nonneg": (WHITE, BLACK),
            "sos": (MAROON_E, MAROON_A),
            "convex_out": (GREEN_A, GREEN_E),
            "convex_in": (GREEN_A, GREEN_E),
        }

        for p, c in zip(parts.values(), colors.values()):
            p.set_fill(c[0], opacity=.8)
            p.set_stroke(c[1], 4)


class HilbertTable:
    def construct(self, scene):
        self.my_objects = []
        self.setup_labels()
        # helper_grid(self)




        table_left = 9
        table_right = table_left+3
        table_top = -1
        table_bottom = table_top - 4

        # Position table contents
        self.label_degree.shift((table_top+1)*UP + (table_right+table_left)/2 * RIGHT)
        self.label_num_vars.shift((table_left-1)*RIGHT+(table_top-2)*UP).rotate(3*PI/2)
        horizontal_arrow = Arrow((table_left, table_top+.5, 0), (table_right+1, table_top+.5, 0))
        vertical_arrow = Arrow((table_left-.5, table_top, 0), (table_left-.5, table_bottom-1, 0))
        self.my_objects.extend([horizontal_arrow, vertical_arrow])
        # Header / Indeex
        for i, d in enumerate(self.degrees):
            d.move_to((i-1+table_left+2, table_top, 0))


        for i, n in enumerate(self.num_vars_hom):
            n.move_to((table_left, table_top-1-i, 0))



        #    degree
        #  ==========>
        #   2 4 >=6

        scene.play(Write(self.label_degree),
                  ShowCreation(horizontal_arrow),
                  ShowCreation(VGroup(*self.degrees)))

        scene.slide_break()

        #    vars
        #  ==========>
        #   1 2 >= 3


        scene.play(Write(self.label_num_vars),
                  ShowCreation(vertical_arrow),
                  ShowCreation(VGroup(*self.num_vars_hom)))

        scene.slide_break()



        scene.slide_break()

        # Table border
        for i in range(len(self.num_vars_hom)):
            line = Line( (table_left-.5, table_top-.5-i, 0), (table_right+.5, table_top-.5-i, 0))
            self.my_objects.append(line)
            scene.add(line)

        for i in range(1, len(self.degrees)+1):
            line = Line( (table_left-.5+i, table_top+.5, 0), (table_left-.5+i, table_bottom-.5, 0))
            self.my_objects.append(line)
            scene.add(line)


        scene.slide_break()

        def add_x(i, j):
            x = self.x_mark.copy().move_to((table_left+i, table_top-j, 0))
            self.my_objects.append(x)
            return x


        def add_check(i, j):
            check = self.check_mark.copy().move_to((table_left+i, table_top-j, 0))
            self.my_objects.append(check)
            return check


        scene.play(*[FadeIn(add_check(i+1, j)) for i in range(3) for j in (1,2)],
                   *[FadeIn(add_check(1, i+1)) for i in range(4)],
                   FadeIn(add_check(2, 3)),
                   *[FadeIn(add_x(i, j))
                     for (i,j) in ((2, 4), (3, 4), (3, 3))])
        scene.slide_break()





    def setup_labels(self):
        self.label_degree = Text("degree")
        self.label_num_vars = Text("\# of variables")
        self.degrees = [Tex("2"), Tex("4"), Tex(r"\ge 6")]
        self.num_vars_hom = [Tex("1"), Tex("2"), Tex("3"),  Tex(r"\ge 4")]

        self.x_mark = SVGMobject("x-mark.svg").scale(.2).set_color(RED)
        self.check_mark = SVGMobject("correct.svg").scale(.2).set_color(GREEN)

        self.my_objects.extend([
            self.label_degree,
            self.label_num_vars,
            *self.degrees,
            *self.num_vars_hom,
            self.x_mark,
            self.check_mark,
        ])


    def remove_table(self, scene):
        scene.remove(*self.my_objects)


class ConvexCones(SlideScene):
    def construct(self):
        # camera
        frame = self.camera.frame
        frame.save_state()
        frame.scale(1.2).shift(.8*UP)



        self.setup_labels()
        convex_cones = self.convex_cones = ConvexConesSVG()
        convex_cones.set_height(FRAME_HEIGHT-2)


        # p(x) =
        self.label_p_eq.shift(4*UP)
        self.add(self.label_p_eq)
        self.slide_break()

        self.label_p_hom_eq.move_to(self.label_p_eq)
        self.remove(self.label_p_eq)
        self.add(self.label_p_hom_eq)
        self.slide_break()




        # nonneg
        #scene.play(GrowFromCenter(convex_cones.parts['nonneg']))
        self.add(convex_cones.parts['nonneg'])
        self.label_nonneg.move_to((5, 2., 0))
        arrow = self.make_arrow(
            self.label_nonneg,
            Dot().move_to(self.label_nonneg).shift(-4*RIGHT),
            GREEN)\
                    .shift(UP/6)
        self.add(arrow, self.label_nonneg)
        self.slide_break()


        # sos
        self.add(convex_cones.parts['sos'])
        self.label_sos.move_to((-1, -3.5, 0))
        self.arrow_sos = self.make_arrow(
            self.label_sos,
            Dot().move_to(self.label_sos).shift(2*UP),
            BLUE_E)
        self.add(self.arrow_sos)
        self.add(self.label_sos)
        self.slide_break()


        # Zoom out
        scale_factor = 1.3
        shift = FRAME_WIDTH / 2.2  *RIGHT + DOWN
        self.play(
            frame.scale, scale_factor,
            frame.shift, shift,
        )
        self.add(self.label_nonneg_implies_sos)
        self.slide_break()


        self.add_hilbert_table()
        self.slide_break()

        return

        self.add_motzkin()
        self.slide_break()


        self.remove_sos_stuff()
        # self.slide_break()




        # Convex
        self.add(convex_cones.parts['convex_out'])
        self.label_conv.move_to((5, -1, 0))
        self.arrow_conv = self.make_arrow(self.label_conv, Dot().move_to(self.label_conv).shift(-3*RIGHT), RED_E)
        self.add(self.arrow_conv)
        self.add(self.label_conv)
        self.slide_break()


        self.add(self.label_conv_implies_nonneg)
        self.slide_break()


        self.add(self.label_euler)
        self.slide_break()


        self.remove_convex_stuff()




        # Convex vs SOS
        self.add(convex_cones.parts['sos'],
                 self.arrow_sos,
                 self.label_sos)
        self.add(convex_cones.parts['convex_out'],
                 self.arrow_conv,
                 self.label_conv)

        self.slide_break()


        self.label_parrilo_asked.to_corner(UR).shift(FRAME_WIDTH/1.4*RIGHT)
        labs = [self.label_parrilo_asked, self.label_blekherman, self.label_no_examples, self.label_minimal_suspects]

        stack_group_text(labs, DOWN, 1)
        align_group_text(labs)
        self.add(self.label_parrilo_asked)
        self.slide_break()


        convex_out = convex_cones.parts['convex_out'].copy()
        self.play(Transform(convex_cones.parts['convex_out'], convex_cones.parts['convex_in']))
        self.slide_break()

        self.add(self.label_blekherman)
        self.slide_break()


        self.play(Transform(convex_cones.parts['convex_out'], convex_out))
        self.slide_break()


        self.add(self.label_no_examples)
        self.slide_break()

        self.add(self.label_minimal_suspects)
        self.slide_break()

        # add pic hilbert

        self.add_theorem()
        self.wait()

        return


    def setup_labels(self):
        self.label_p_eq = Tex(r"p(x) = \sum_{k_1+\ldots+k_n \le 2d} c_k \, x_1^{k_1} \cdots  x_{\color{red}n}^{k_n}")
        self.label_p_hom_eq = Tex(r"p(x) = \sum_{k_1+\ldots+k_n = 2d} c_k \, x_1^{k_1} \cdots  x_{\color{red}n}^{k_n}")

        self.label_nonneg = Tex(r"p(x) \ge 0 \quad \forall x \in \mathbb R^n").scale(.8)
        self.label_sos = Tex(r"p(x) = \sum_i q_i(x)^2").scale(.8)
        self.label_conv = Tex(r"p \text{ convex}\\\nabla^2 p(x) \succeq 0").scale(.8)

        # right column
        scale_factor = .9
        self.label_parrilo_asked = Text(r"07', Parrilo Asked: Are all convex forms sos?")
        self.label_blekherman = Text(r"""09', Blekherman:
        {No}
        For $2d \ge 4$ there are many more convex
        forms than sos as $n \rightarrow \infty$""")


        self.label_no_examples = Text(r"""- {No} explicit examples are known!
        \hspace{.75cm} - Smallest $(n, 2d)$ for such an example?""")


        self.label_minimal_suspects = Text(r"""Minimal suspects:
        (n, 2d) = (4,4) and (3, 6)""")


        # Nonegative ==> SOS?
        self.label_nonneg_implies_sos = Tex(r"\text{Nonnegative }\Rightarrow \text{ SOS} ?")
        self.label_nonneg_implies_sos.scale(1.5)
        self.label_nonneg_implies_sos.move_to((12, 2, 0))

        # Convex ==> Nonnegative?
        self.label_conv_implies_nonneg = Text(r"\text{Convex }\Rightarrow \text{ Nonnegative} ?")
        self.label_conv_implies_nonneg.scale(1.5)
        self.label_conv_implies_nonneg.move_to(self.label_nonneg_implies_sos)


        # Euler identity
        self.label_euler = Text(r"""{\bf Yes!} Euler:
        \begin{align*}p(x) &= \frac 1{2d} x^T \nabla p(x)
                           &= \frac 1{2d(2d-1)} x^T \nabla^2 p(x)x
        \end{align*}
        """)\
            .next_to(self.label_conv_implies_nonneg, DOWN, LARGE_BUFF)\
            .shift(RIGHT)


        # scale
        for lab in [self.label_parrilo_asked, self.label_blekherman, self.label_no_examples, self.label_minimal_suspects]:
            lab.scale(scale_factor)


    def add_hilbert_table(self):

        # self.table_as_vgroup.shift(2*DOWN +LEFT)


        # image with name
        name = self.name_hilbert = Text(r"\bf Hilbert, 1888", color=YELLOW)
        img_hilbert = self.img_hilbert = ImageMobject("media/hilbert.jpg")

        img_hilbert.scale(2).move_to((15, -2, 0))
        name.next_to(img_hilbert, DOWN)
        self.add(img_hilbert, name)
        self.slide_break()

        self.table = HilbertTable()
        self.table.construct(self)
        self.table_as_vgroup = VGroup(*self.table.my_objects)
        self.slide_break()


    def add_motzkin(self):
        x_mark = SVGMobject("x-mark.svg").scale(.1).set_color(BLUE_E)

        x_motz = x_mark.copy().shift(UP+3*LEFT)
        lab_motz = Text(r"Motzkin\\ (1967)", color=BLACK).scale(.5)
        lab_motz.next_to(x_motz, DOWN)
        self.add(x_motz, lab_motz)
        self.slide_break()

        x_robin = x_mark.copy().shift(2*UP+RIGHT)
        lab_robin = Text(r"Robinson\\ (1973)", color=BLACK).scale(.5)
        lab_robin.next_to(x_robin, DOWN)
        self.add(x_robin, lab_robin)
        self.slide_break()

        self.motz_robin = VGroup(x_motz, lab_motz, x_robin, lab_robin)


    def remove_sos_stuff(self):
        self.table.remove_table(self)
        self.remove(self.img_hilbert, self.name_hilbert, self.label_nonneg_implies_sos, *self.motz_robin)
        self.remove(self.convex_cones.parts['sos'])
        self.remove(self.arrow_sos, self.label_sos)


    def remove_convex_stuff(self):
        self.remove(self.convex_cones.parts['convex_out'])
        self.remove(self.arrow_conv, self.label_conv,
                    self.label_euler, self.label_conv_implies_nonneg)



    def add_theorem(self):
        statement = Text("Convex ",  "quaternary quartic forms are ", "sos.")
        statement[0].set_color(BLUE_B)
        statement[-1].set_color(MAROON_A)
        thm = make_thm(statement, r"\textbf{Thm.} \; (\textbf{El})")
        thm.move_to((FRAME_WIDTH/2.1, -FRAME_HEIGHT/1.7, 0)).scale(1.1)

        self.add(thm)

    def make_arrow(self, a, b, color=GREEN):
        arrow = Arrow(a, b)
        arrow.set_color(color)
        return arrow
