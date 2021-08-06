import os
import shutil
from manimlib import *

class SlideScene(Scene):
    def setup(self):
        super(SlideScene, self).setup()
        self.breaks=[0]

    def slide_break(self,t=0.5):
        self.breaks+=[self.time+t/2]
        self.wait(t)

    def save_times(self):
        self.breaks+=[self.time]
        template ="<p class=\"fragment\" type='video' time_start={b} time_end={bb}></p>"
        out= "\n".join([
                template.format(b=b, bb=bb)
                for b, bb in zip(self.breaks, self.breaks[1:])])

        txt_path = "output/%s.txt" % type(self).__name__
        with open(txt_path,'w') as f:
            f.write(out)


    def tear_down(self):
        super().tear_down()
        self.save_times()
