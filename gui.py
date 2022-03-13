from guizero import App, Combo, Text, CheckBox, ButtonGroup, PushButton, info
import glob
import os
import sys
mdir="/home/"+(os.getlogin())+"/Music"
if len(sys.argv) >= 2:
	if sys.argv[1] != "":
		mdir=sys.argv[1]

def transmit():
	info("Status", "Transmitting Now")
	print( file_choice.value )
	print( repeat_mode.value )
	if repeat_mode.value == 0:
		os.system("cd /fm_transmitter && sudo ./fm_transmitter -f "+frequency.value+" -d 255 "+file_choice.value)
	elif repeat_mode.value == 1:
		os.system("cd /fm_transmitter && sudo ./fm_transmitter -f "+frequency.value+" -d 255 -r "+file_choice.value)

app = App(title="Fm_Transmitter GUI", width=300, height=200, layout="grid")
file_choice = Combo(app, options=(glob.glob(mdir+"/*.wav")), grid=[0,0], align="left")
file_caption = Text(app, text="What To Transmit?", grid=[0,1], align="left")
frequency = ButtonGroup(app, options=[ ["87.5MHz", "87.5"], ["90MHz", "90.0"],["95.5MHz", "95.5"] ],
selected="M", horizontal=True, grid=[0,3], align="left")
repeat_mode = CheckBox(app, text="Repeat Mode", grid=[0,2], align="left")
play_file = PushButton(app, command=transmit, text="Transmit File", grid=[0,4], align="left")
app.display()
