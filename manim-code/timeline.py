#!/usr/bin/env python3
from manimlib import *
exec(get_custom_config()["universal_import_line"])
import numpy as np
np.random.seed(0)


class Timeline(Scene):
    def construct(self):
        arrow = Vector().scale(8)
        self.add(arrow)
        self.wait()
