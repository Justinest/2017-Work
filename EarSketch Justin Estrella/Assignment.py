#		python code
#		script_name:Coding 
#
#		author: Justin E
#		description:
#

from earsketch import *
init()
setTempo(120)

#Music
#Section A
def SectionA(startMeasure, endMeasure):
  fitMedia(DUBSTEP_DRUMLOOP_PART_016, 2, startMeasure, endMeasure)
  fitMedia(ELECTRO_ANALOGUE_BASS_007, 1, startMeasure, endMeasure)
  for measure in range(1, 5):
    fitMedia(DUBSTEP_DRUMLOOP_PART_017, 3, measure, measure + 1)
  for measure in range(1, 5, 2):
   fitMedia(ELECTRO_ANALOGUE_BASS_006, 4, measure, measure + 0.5)
  setEffect(4, DELAY, DELAY_TIME, 500)
  

#Section B
def SectionB(startMeasure, endMeasure):
  fitMedia(ELECTRO_DRUM_MAIN_PART_009, 1, startMeasure, endMeasure)
  fitMedia(ELECTRO_MOTORBASS_004, 3, startMeasure, endMeasure)
  fitMedia(EIGHT_BIT_ATARI_LEAD_010, 5, startMeasure, endMeasure)
setEffect(5, VOLUME, GAIN, 5, 5, 0, 13)
  
  
#Section C
def SectionC(startMeasure, endMeasure):
  fitMedia(ELECTRO_RAVELEAD_001, 7, startMeasure, endMeasure)
  fitMedia(ELECTRO_MOTORBASS_004, 8, startMeasure, endMeasure)
  fitMedia(DUBSTEP_BASS_WOBBLE_037, 9, startMeasure, endMeasure)
setEffect(7, VOLUME, GAIN, 10, 19, 0, 28)
setEffect(8, VOLUME, GAIN, 10, 19, 0, 28)
setEffect(9, VOLUME, GAIN, 10, 19, 0, 28)

#Makebeat
def myBeat(startMeasure, endMeasure):
  beatPattern = "0---0---0---0---"
  makeBeat(ELECTRO_RAVELEAD_001, 1, 5, beatPattern)
myBeat(1,5)

#Sections
SectionA(1,5)
SectionB(5,15)
SectionA(15,19)
SectionC(19,30)
SectionA(30,35)
SectionB(35,45)
SectionA(45,51)
finish()
