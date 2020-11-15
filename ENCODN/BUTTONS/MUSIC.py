from tkinter import * 
from tkinter import ttk

def MUSIC(master=None):

	s = ttk.Style(master)
	s.configure('lefttab.TNotebook',padding=[20,20], tabposition='wn')

	nb = ttk.Notebook(master, s='lefttab.TNotebook', width=900, height=600)
	nb.grid(row=0, column=0, sticky="e")
	nb.grid_propagate()

	t_names = ["OPTION1","OPTION2","OPTION3","OPTION4","OPTION5"]
	#fr_names = [TELECOM, OTHERS]

	for i in range(len(t_names)):
		fr = Frame(nb,bg="#215d9c", width = 800, height=550)
		nb.add(fr, text=t_names[i])
