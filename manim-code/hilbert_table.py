class HilbertTable(Scene):
    def construct(self):
        self.setup_labels()
        # helper_grid(self)


        table_left = -2
        table_right = 1
        table_top = 2
        table_bottom = -1

        # Position table contents
        self.label_degree.shift((table_top+1)*UP)
        self.label_num_vars.shift((table_left-1)*RIGHT).rotate(3*PI/2)
        horizontal_arrow = Arrow((table_left, table_top+.5, 0), (table_right+1, table_top+.5, 0))
        vertical_arrow = Arrow((table_left-.5, table_top, 0), (table_left-.5, table_bottom-1, 0))

        # Header / Indeex
        for i, d in enumerate(self.degrees):
            d.move_to((i-1, table_top, 0))

        for num_vars in (self.num_vars, self.num_vars_hom):
            for i, n in enumerate(num_vars):
                n.move_to((table_left, 1-i, 0))



        #    degree
        #  ==========>
        #   2 4 >=6

        self.play(Write(self.label_degree),
                  ShowCreation(horizontal_arrow),
                  ShowCreation(VGroup(*self.degrees)))

        add_black_screen(self)

        #    vars
        #  ==========>
        #   1 2 >= 3


        self.play(Write(self.label_num_vars),
                  ShowCreation(vertical_arrow),
                  ShowCreation(VGroup(*self.num_vars)))

        add_black_screen(self)




        add_black_screen(self)

        # Table border
        for i in range(len(self.num_vars)):
            self.add(Line( (table_left-.5, table_top-.5-i, 0), (table_right+.5, table_top-.5-i, 0)))

        for i in range(1, len(self.degrees)+1):
            self.add(Line( (table_left-.5+i, table_top+.5, 0), (table_left-.5+i, table_bottom-.5, 0)))

        
        add_black_screen(self, .5)

        add_x = lambda i, j: self.x_mark.copy().move_to((table_left+i, table_top-j, 0))
        add_check = lambda i, j: self.check_mark.copy().move_to((table_left+i, table_top-j, 0))
        # n = 1
        self.play(*[FadeIn(add_check(i+1, 1)) for i in range(3)])
        add_black_screen(self)


        # d = 2
        self.play(*[FadeIn(add_check(1, i+1)) for i in range(3)])
        add_black_screen(self)

        # n=2, d=4
        self.play(FadeIn(add_check(2, 2)))
        add_black_screen(self)

        # x everywhere else
        self.play(*[FadeIn(add_x(i, j)) for (i,j) in ((2, 3), (3, 3), (3, 2))])
        add_black_screen(self)


        # homogenous case
        self.play(*[Transform(non_hom, hom) for (non_hom, hom) in zip(self.num_vars, self.num_vars_hom)])

        self.wait()


    def setup_labels(self):
        self.label_degree = TextMobject("degree")
        self.label_num_vars = TextMobject("\# of variables")
        self.degrees = [TexMobject("2"), TexMobject("4"), TexMobject(r"\ge 6")]
        self.num_vars = [TexMobject("1"), TexMobject("2"),  TexMobject(r"\ge 3")]

        self.num_vars_hom = [TexMobject("2"), TexMobject("3"),  TexMobject(r"\ge 4")]

        self.x_mark = SVGMobject("x-mark.svg").scale(.2).set_color(MAROON_A)
        self.check_mark = SVGMobject("correct.svg").scale(.2).set_color(GREEN)

