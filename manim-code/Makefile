##
# Project Title
#
# @file
# @version 0.1


CUT_MOV =  "/home/bachir/.local/bin/cut_video_on_black_screen.py"

CauchySchwarz:
	manimgl cauchy_schwarz.py CauchySchwarz -w

ProofScene:
	manimgl convex_cones_drawing.py ProofScene -w

Produce:
	bash -c "cp output/*txt output/*/*mp4 ../reveal/videos"


Timeline:
	manimgl timeline.py Timeline -w && PNG_CONVERTER = "/home/bachir/.local/bin/mov_to_pngs.sh"
