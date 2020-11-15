from tkinter import * 
from tkinter import ttk
from FRAMES.TELECOM import TELECOM
from FRAMES.COMM_OTHERS import OTHERS
from FRAMES.NUMERAL_SYS import NUMERAL_SYS
from FRAMES.NOTATION_SYS import NOTATION_SYS

t_names = ["TELECOM", "NUMERAL SYSTEM", "NOTATION SYSTEM", "OTHERS"]
frames = []
fr_names = [TELECOM, NUMERAL_SYS, NOTATION_SYS, OTHERS]

def COMMUNICATION(master=None):

	s = ttk.Style(master)
	s.configure('lefttab.TNotebook',padding=[10,20], tabposition='wn')

	nb = ttk.Notebook(master, s='lefttab.TNotebook', width=850, height=650)
	nb.grid(row=0, column=0, sticky="e")
	nb.grid_propagate(0)

	for i in range(len(t_names)):
		frames.append(Frame(nb,bg="#215d9c", width = 850, height=550))
		nb.add(frames[i], text=t_names[i])

#calling frame setups here

	for i in range(len(fr_names)):
		fr_names[i](frames[i])














	



