##
# Project Title
#
# @file
# @version 0.1


CUT_MOV =  "/Users/bachirelkhadir/Documents/GitHub/reveal-iccopt-2022/manim-code/cut_video_on_black_screen_reencode.py"

CauchySchwarz:
	manimgl cauchy_schwarz.py CauchySchwarz -w && cd output/videos/ && ${CUT_MOV} CauchySchwarz.mp4 && cp CauchySchwarz*mp4 ../../../reveal/videos/CauchySchwarz/


ProofScene:
	manimgl convex_cones_drawing.py ProofScene -w && cd output/videos/ && ${CUT_MOV} ProofScene.mp4 && cp ProofScene*mp4 ../../../reveal/videos/ProofScene/


Produce:
	bash -c "cp output/*txt output/*/*mp4 ../reveal/videos"


Timeline:
	manimgl timeline.py Timeline -w && cd output/videos/ && ${CUT_MOV} Timeline.mp4 && cp Timeline*mp4 ../../../reveal/videos/Timeline/
