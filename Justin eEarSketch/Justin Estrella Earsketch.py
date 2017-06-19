# python code
#
# script_name: Intro Script
#
# author: The EarSketch Team
#
# description: This code adds one audio clip to the DAW
#
#
#

#Setup Section
from earsketch import *
init()
setTempo(50)

#Music Section
fitMedia(DUBSTEP_LEAD_001, 1, 1, 5)
fitMedia(YG_WEST_COAST_HIP_HOP_STRINGS_SHORT_1, 2, 5, 9)
fitMedia(YG_WEST_COAST_HIP_HOP_RIDE_1, 3, 5, 10)
setEffect(1, DELAY, DELAY_TIME, 500)
setEffect(2, DELAY, DELAY_TIME, 500)
#Finish Section
finish()