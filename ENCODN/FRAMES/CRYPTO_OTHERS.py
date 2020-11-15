from tkinter import *
from tkinter import ttk
from TOOLS1.CRYPTOGRAPHY.OTHERS.BACON.BACON_FRAME import BACON_FRAME
from TOOLS1.CRYPTOGRAPHY.OTHERS.ROZIER.ROZIER_FRAME import ROZIER_FRAME

t_names = ["BACON","ROZIER"]
frames = []
fr_names = [BACON_FRAME,ROZIER_FRAME]

def CRYPTO_OTHERS(master=None):

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
