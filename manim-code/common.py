#!/usr/bin/env python3

from manimlib import *

def make_def(label, name=r"Def"):
    return make_thm(label, name=r"\textbf{Def.}")


def rect_scale(rect, scale_factor):
        rect.apply_points_function(
            lambda points: scale_factor * points,
            works_on_bounding_box=True,
        )

def make_thm(label, name=r"Thm", line_break=True):
    if name is not None:
        label_name = Text(name, weight=BOLD).set_color("#f1bf27")
    else:
        # placeholder
        label_name = Dot().fade(1)

    if line_break:
        label_name.next_to(label, UP, MED_LARGE_BUFF)\
              .align_to(label, LEFT)\
              .shift(LEFT/3)
    else:
        label_name.next_to(label, LEFT, MED_LARGE_BUFF)

    rect = SurroundingRectangle(VGroup(label_name, label))

    scale( rect, 1.1*RIGHT+1.2*UP)
    rect.set_fill(BLACK, opacity=.5)
    rect.set_stroke(BLACK)
    return VGroup(rect, label_name, label)
