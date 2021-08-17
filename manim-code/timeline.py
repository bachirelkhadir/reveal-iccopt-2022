#!/usr/bin/env python3
from manimlib import *
exec(get_custom_config()["universal_import_line"])
from align_utils import *
from colors import *
import numpy as np
np.random.seed(0)


class Timeline(Scene):
    def construct(self):
        self.add(Text("Class " + type(self).__name__))
        self.wait()
