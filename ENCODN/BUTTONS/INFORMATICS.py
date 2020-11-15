from tkinter import * 
from tkinter import ttk
from FRAMES.ALGORITHM import ALGORITHM
from FRAMES.CHAR_ENCODING import CHAR_ENCODING
from FRAMES.INTERNET import INTERNET
from FRAMES.GEEK import GEEK
from FRAMES.PROG_LANG import PROG_LANG
from FRAMES.INFO_OTHERS import INFO_OTHERS

t_names = ["ALGORITHM", "CHARACTER ENCODING", "INTERNET", "GEEK", "PROGRAMMING LANGUAGE", "OTHERS"]
frames = []
fr_names = [ALGORITHM, CHAR_ENCODING, INTERNET, GEEK, PROG_LANG, INFO_OTHERS]

def INFORMATICS(master=None):

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
