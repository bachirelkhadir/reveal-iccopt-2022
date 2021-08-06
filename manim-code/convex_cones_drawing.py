
from manimlib import *
exec(get_custom_config()["universal_import_line"])
from colors import *
import numpy as np
from common import *
from slide_scene import SlideScene

class ConvexCones(SVGMobject):
    CONFIG = {
        "file_name": "convex_cones_with_tangents.svg",
        "index_nonneg": 0,
        "index_sos": 1,
        "index_convex_out": 2,
        "index_convex_in": 3,
        "index_tangents_conv": 4,
        "index_tangents_sos": 11
    }

    def __init__(self, **kwargs):
        SVGMobject.__init__(self, "assets/convex_cones_with_tangents.svg")
        #colorsvg.color_svg_like_file(self)
        parts = self.parts = {
            "nonneg": self[self.index_nonneg],
            "sos": self[self.index_sos],
            "convex_out": self[self.index_convex_out],
            "convex_in": self[self.index_convex_in],
            "tangents_conv": self[self.index_tangents_conv:self.index_tangents_sos],
            "tangents_sos": self[self.index_tangents_sos:],
        }
        colors = {
            "nonneg": (GREY, WHITE),
            "sos": (MAROON_E, MAROON_A),
            "convex_out": (GREEN_A, GREEN_E),
            "convex_in": (GREEN_A, GREEN_E),
        }
        # for p, c in zip(parts.values(), colors.values()):
        #     p.set_fill(c[0], opacity=.8)
        #     p.set_stroke(c[1], 4)



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

        add_black_screen(scene)

        #    vars
        #  ==========>
        #   1 2 >= 3


        scene.play(Write(self.label_num_vars),
                  ShowCreation(vertical_arrow),
                  ShowCreation(VGroup(*self.num_vars_hom)))

        add_black_screen(scene)



        add_black_screen(scene)

        # Table border
        for i in range(len(self.num_vars_hom)):
            line = Line( (table_left-.5, table_top-.5-i, 0), (table_right+.5, table_top-.5-i, 0))
            self.my_objects.append(line)
            scene.add(line)

        for i in range(1, len(self.degrees)+1):
            line = Line( (table_left-.5+i, table_top+.5, 0), (table_left-.5+i, table_bottom-.5, 0))
            self.my_objects.append(line)
            scene.add(line)

        
        add_black_screen(scene)

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
        add_black_screen(scene)





    def setup_labels(self):
        self.label_degree = TextMobject("degree")
        self.label_num_vars = TextMobject("\# of variables")
        self.degrees = [TexMobject("2"), TexMobject("4"), TexMobject(r"\ge 6")]
        self.num_vars_hom = [TexMobject("1"), TexMobject("2"), TexMobject("3"),  TexMobject(r"\ge 4")]

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


class ConvexConesScene(SlideScene):
    CONFIG = {

    }


    def make_arrow(self, a, b, color=GREEN):
        arrow = Arrow(a, b)
        arrow.set_color(color)
        return arrow



    def construct(self):
        # camera
        frame = self.camera_frame
        frame.save_state()
        frame.scale(1.2).shift(.8*UP)



        self.setup_labels()
        convex_cones = self.convex_cones = ConvexCones()
        convex_cones.set_height(FRAME_HEIGHT-2)
        

        # p(x) =
        self.label_p_eq.shift(4*UP)
        self.add(self.label_p_eq)
        add_black_screen(self)

        self.label_p_hom_eq.move_to(self.label_p_eq)
        self.remove(self.label_p_eq)
        self.add(self.label_p_hom_eq)
        add_black_screen(self)




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
        add_black_screen(self)


        # sos
        self.add(convex_cones.parts['sos'])
        self.label_sos.move_to((-1, -3.5, 0))
        self.arrow_sos = self.make_arrow(
            self.label_sos, 
            Dot().move_to(self.label_sos).shift(2*UP),
            BLUE_E)
        self.add(self.arrow_sos)
        self.add(self.label_sos)
        add_black_screen(self)


        # Zoom out
        scale_factor = 1.3
        shift = FRAME_WIDTH / 2.2  *RIGHT + DOWN
        self.play(
            frame.scale, scale_factor,
            frame.shift, shift,
        )
        self.add(self.label_nonneg_implies_sos)
        add_black_screen(self)


        self.add_hilbert_table()
        add_black_screen(self)


        self.add_motzkin()
        add_black_screen(self)

        
        self.remove_sos_stuff()
        # add_black_screen(self)




        # Convex 
        self.add(convex_cones.parts['convex_out'])
        self.label_conv.move_to((5, -1, 0))
        self.arrow_conv = self.make_arrow(self.label_conv, Dot().move_to(self.label_conv).shift(-3*RIGHT), RED_E)
        self.add(self.arrow_conv)
        self.add(self.label_conv)
        add_black_screen(self)


        self.add(self.label_conv_implies_nonneg)
        add_black_screen(self)


        self.add(self.label_euler)
        add_black_screen(self)


        self.remove_convex_stuff()




        # Convex vs SOS
        self.add(convex_cones.parts['sos'],
                 self.arrow_sos,
                 self.label_sos)
        self.add(convex_cones.parts['convex_out'],
                 self.arrow_conv,
                 self.label_conv)

        add_black_screen(self)
        
        
        self.label_parrilo_asked.to_corner(UR).shift(FRAME_WIDTH/1.4*RIGHT)
        labs = [self.label_parrilo_asked, self.label_blekherman, self.label_no_examples, self.label_minimal_suspects]

        stack_group_text(labs, DOWN, 1)
        align_group_text(labs)
        self.add(self.label_parrilo_asked)
        add_black_screen(self)


        convex_out = convex_cones.parts['convex_out'].copy()
        self.play(Transform(convex_cones.parts['convex_out'], convex_cones.parts['convex_in']))
        add_black_screen(self)

        self.add(self.label_blekherman)
        add_black_screen(self)


        self.play(Transform(convex_cones.parts['convex_out'], convex_out))
        add_black_screen(self)


        self.add(self.label_no_examples)
        add_black_screen(self)

        self.add(self.label_minimal_suspects)
        add_black_screen(self)

        # add pic hilbert 

        self.add_theorem()
        self.wait()

        return


    def setup_labels(self):
        self.label_p_eq = TexMobject(r"p(x) = \sum_{k_1+\ldots+k_n \le 2d} c_k \, x_1^{k_1} \cdots  x_{\color{red}n}^{k_n}")
        self.label_p_hom_eq = TexMobject(r"p(x) = \sum_{k_1+\ldots+k_n = 2d} c_k \, x_1^{k_1} \cdots  x_{\color{red}n}^{k_n}")

        self.label_nonneg = TexMobject(r"p(x) \ge 0 \quad \forall x \in \mathbb R^n").scale(.8)
        self.label_sos = TexMobject(r"p(x) = \sum_i q_i(x)^2").scale(.8)
        self.label_conv = TexMobject(r"p \text{ convex}\\\nabla^2 p(x) \succeq 0").scale(.8)

        # right column
        scale_factor = .9
        self.label_parrilo_asked = TextMobject(*r"07', Parrilo Asked: |\textbf{Are all convex forms sos?}".split("|"))
        self.label_blekherman = TextMobject(*r"""09', Blekherman:
        {No}\\
        For $2d \ge 4$ there are many more convex\\
        forms than sos as $n \rightarrow \infty$""".split("\n"))
        align_group_text([self.label_blekherman[0], *self.label_blekherman[2:]])


        self.label_no_examples = TextMobject(*r"- {No}| explicit examples are known!\\ \hspace{.75cm} - Smallest $(n, 2d)$ for such an example?".split("|"))


        self.label_minimal_suspects = TextMobject(*r"""Minimal suspects:\\
        $(n, 2d) = (4,4)$ and $(3, 6)$""".split("\n"))
        align_group_text(self.label_minimal_suspects)


        # Nonegative ==> SOS?
        self.label_nonneg_implies_sos = TextMobject(r"Nonnegative $\Rightarrow$ ", "SOS", " ?")
        self.label_nonneg_implies_sos[1].set_color(BLUE_B)
        self.label_nonneg_implies_sos.scale(1.5)
        self.label_nonneg_implies_sos.move_to((12, 2, 0))

        # Convex ==> Nonnegative?
        self.label_conv_implies_nonneg = TextMobject(r"Convex $\Rightarrow$ ", "Nonnegative", " ?")
        self.label_conv_implies_nonneg[0].set_color(MAROON_A)
        self.label_conv_implies_nonneg.scale(1.5)
        self.label_conv_implies_nonneg.move_to(self.label_nonneg_implies_sos)


        # Euler identity
        self.label_euler = TextMobject(r"""{\bf Yes!} Euler:
        \begin{align*}p(x) &= \frac 1{2d} x^T \nabla p(x)\\
                           &= \frac 1{2d(2d-1)} x^T \nabla^2 p(x)x
        \end{align*}
        """)\
            .next_to(self.label_conv_implies_nonneg, DOWN, LARGE_BUFF)\
            .shift(RIGHT)


        # scale
        for lab in [self.label_parrilo_asked, self.label_blekherman, self.label_no_examples, self.label_minimal_suspects]:
            lab.scale(scale_factor)
            lab.set_color_by_tex_to_color_map(
                {'{No}': MAROON_A,
                 'Are all convex forms sos?': YELLOW,
                })



    def add_hilbert_table(self):

        # self.table_as_vgroup.shift(2*DOWN +LEFT)


        # image with name
        name = self.name_hilbert = TextMobject(r"\bf Hilbert, 1888", color=YELLOW)
        img_hilbert = self.img_hilbert = ImageMobject("media/hilbert.jpg")

        img_hilbert.scale(2).move_to((15, -2, 0))
        name.next_to(img_hilbert, DOWN)
        self.add(img_hilbert, name)
        add_black_screen(self)

        self.table = HilbertTable()
        self.table.construct(self)
        self.table_as_vgroup = VGroup(*self.table.my_objects)
        add_black_screen(self)


    def add_motzkin(self):
        x_mark = SVGMobject("x-mark.svg").scale(.1).set_color(BLUE_E)
        
        x_motz = x_mark.copy().shift(UP+3*LEFT)
        lab_motz = TextMobject(r"Motzkin\\ (1967)", color=BLACK).scale(.5)
        lab_motz.next_to(x_motz, DOWN)
        self.add(x_motz, lab_motz)
        add_black_screen(self)

        x_robin = x_mark.copy().shift(2*UP+RIGHT)
        lab_robin = TextMobject(r"Robinson\\ (1973)", color=BLACK).scale(.5)
        lab_robin.next_to(x_robin, DOWN)
        self.add(x_robin, lab_robin)
        add_black_screen(self)

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
        statement = TextMobject("Convex ",  "quaternary quartic forms are ", "sos.")
        statement[0].set_color(BLUE_B)
        statement[-1].set_color(MAROON_A)
        thm = make_thm(statement, r"\textbf{Thm.} \; (\textbf{El})")
        thm.move_to((FRAME_WIDTH/2.1, -FRAME_HEIGHT/1.7, 0)).scale(1.1)
        
        self.add(thm)
        


class ProofScene(SlideScene):
    CONFIG = {
        'scale_cones': 2,
        }
    
    def construct(self):


        self.setup_cones()
        self.add(self.cone_lab_conv, self.lab_subset, self.cone_lab_sos)
        add_black_screen(self)

        # duality
        self.setup_stars()
        self.add(self.lab_stars)
        add_black_screen(self)

        self.play(ApplyMethod(self.lab_subset.flip))
        add_black_screen(self)


        # blekherman
        self.trace_sos_hyperplanes()
        add_black_screen(self)
        self.show_blekherman_thm()
        add_black_screen(self)


        # cauchy schwarz
        self.trace_conv_hyperplanes()
        add_black_screen(self)
        self.show_cauchy_schwarz()

        self.wait()



    def trace_conv_hyperplanes(self):

        tangents_conv = self.convex_cones.parts['tangents_conv']
        tangents_conv.set_color(GRAY)
        tangents_conv.scale(self.scale_cones)\
                    .move_to(self.cone_conv).shift(UP/8+LEFT/8)
        
        self.play(ShowCreation(tangents_conv))


    def trace_sos_hyperplanes(self):
        tangents_sos = self.convex_cones.parts['tangents_sos']
        tangents_sos.set_color(GRAY)
        tangents_sos.scale(self.scale_cones)\
                    .move_to(self.cone_sos).shift(UP/5+LEFT/5)
        self.play(ShowCreation(tangents_sos))



    def show_blekherman_thm(self):
        img_blekherman_thm = ImageMobject("theorem_blekherman.png")
        img_blekherman_thm.scale(.75)\
            .next_to(self.cone_sos, DOWN, LARGE_BUFF)
        self.add(img_blekherman_thm)


    def show_cauchy_schwarz(self):
        cs_assumption = TextMobject("For any convex form of degree $4$")
        cs_inequality = TexMobject(*r"""\frac1{12}
                                       x^T
                                       \nabla^2p(
                                      y
                                      )
                                       x
                                      \le
                                       \sqrt{p(x)}
                                       \sqrt{p(y)}
                                      \quad \forall
                                       x
                                      ,
                                       y
                                      \in \mathbb R^n""".split("\n"))

        cs_inequality.set_color_by_tex_to_color_map({
            "x": RED,
            "y": BLUE})
        align_group_text(stack_group_text([cs_assumption, cs_inequality]))
        cs_thm = make_thm(VGroup(cs_assumption, cs_inequality),  r"\textbf{Thm} \; (\textbf{El})")
        cs_thm.move_to((-3, -1.5, 0)).scale(.6)
        self.add(cs_thm)


    def setup_stars(self):
        lab_star_conv = TexMobject("*").scale(self.scale_cones)\
                                       .next_to(self.cone_lab_conv, RIGHT+UP)\
                                       .shift(DOWN/2+LEFT/2)

        lab_star_sos = TexMobject("*").scale(self.scale_cones)\
                                      .next_to(self.cone_lab_sos, RIGHT+UP)\
                                      .shift(DOWN/2+LEFT/2)

        self.lab_stars = VGroup(lab_star_conv, lab_star_sos)
        
    def setup_cones(self):
        convex_cones = self.convex_cones = ConvexCones()
        label_conv = TextMobject("convex")
        label_sos = TextMobject("sos")

        cone_conv = convex_cones.parts['convex_in']
        cone_sos = convex_cones.parts['sos']

        lab_subset = self.lab_subset = TexMobject(r"\subseteq")

        # placement, scaling and coloring
        cone_conv.shift(2.5*LEFT+2*UP)\
                 .scale(self.scale_cones)\
                 .set_color(RED)
                 
        lab_subset.scale(2)\
                    .next_to(cone_conv, RIGHT, LARGE_BUFF)

        cone_sos.scale(self.scale_cones)\
                .set_color(BLUE_C)\
                .next_to(lab_subset, RIGHT, LARGE_BUFF)

        label_conv.move_to(cone_conv)
        label_sos.move_to(cone_sos)

        self.cone_conv = cone_conv
        self.cone_sos = cone_sos

        cone_lab_conv = self.cone_lab_conv = VGroup(cone_conv, label_conv)
        cone_lab_sos = self.cone_lab_sos = VGroup(cone_sos, label_sos)








# Local Variables:
# compile-command: "/home/bachir/.local/bin/manim convex_cones_drawing.py MainScene -pl -c=#1f303e"
# End:
