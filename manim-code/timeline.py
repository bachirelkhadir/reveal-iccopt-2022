#!/usr/bin/env python3
from manimlib import *
exec(get_custom_config()["universal_import_line"])
import numpy as np
np.random.seed(0)


class Timeline(Scene):
    def construct(self):
        arrow = Vector().scale(10)
        lab_nvar = Text(r"# variables")
        lab_nvar.next_to(arrow, UR).shift(2*LEFT)
        self.add(arrow, lab_nvar)

        tick = Line().rotate(PI/2).scale(.2)
        n3 = tick.copy().shift(3*LEFT)
        n4 = n3.copy().shift(RIGHT)
        nhigh = n3.copy().shift(3*RIGHT)
        self.add(n3, n4, nhigh)
        self.wait()
