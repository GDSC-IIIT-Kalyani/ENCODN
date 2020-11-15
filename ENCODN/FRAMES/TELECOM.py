from tkinter import * 
from tkinter import ttk
from TOOLS1.COMMUNICATION.TELECOM.MORSECODE.MORSECODE_FRAME import MORSECODE_FRAME
from TOOLS1.COMMUNICATION.TELECOM.DECABIT.DECABIT_FRAME import DECABIT_FRAME
from TOOLS1.COMMUNICATION.TELECOM.MULTITAP.MULTITAP_FRAME import MULTITAP_FRAME
from TOOLS1.COMMUNICATION.TELECOM.T9.T9_FRAME import T9_FRAME

t_names = ["DECABIT CODE", "MORSE CODE","MULTI-TAP PHONE CIPHER", "T9" ]
frames = []
fr_names = [DECABIT_FRAME,MORSECODE_FRAME, MULTITAP_FRAME, T9_FRAME]

def TELECOM(master=None):

	s = ttk.Style(master)
	s.configure('lefttab.TNotebook',padding=[20,20], tabposition='wn')

	nb = ttk.Notebook(master, s='lefttab.TNotebook', width=800, height=570)
	nb.grid(row=0, column=0, sticky="e", padx=20, pady=15)
	nb.grid_propagate(0)

	for i in range(len(t_names)):
		frames.append(Frame(nb,bg="#7ad159", width = 750, height=500))
		nb.add(frames[i], text=t_names[i])

#calling frame setups here

	for i in range(len(fr_names)):
		fr_names[i](frames[i])
