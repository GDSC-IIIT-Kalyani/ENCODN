from tkinter import *
from tkinter import ttk

t_names = ["BARCODE 39", "BARCODE 93", "QR CODE", "EXCESS 3 CODE", "UNICODE"]
frames = []
fr_names = []

def CHAR_ENCODING(master=None):

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

#calling frame setups here

	for i in range(len(fr_names)):
		fr_names[i](frames[i])
