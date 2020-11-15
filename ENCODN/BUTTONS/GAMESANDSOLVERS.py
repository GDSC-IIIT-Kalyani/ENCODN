from tkinter import * 
from tkinter import ttk
from FRAMES.BOARDGAMES import BOARDGAMES
from FRAMES.MOBILEGAMES import MOBILEGAMES
from FRAMES.WORDGAMES import WORDGAMES
from FRAMES.NUMBERGAMES import NUMBERGAMES
from FRAMES.WORDSEARCH import WORDSEARCH

t_names = ["BOARD GAMES","MOBILE GAMES","WORD GAMES","NUMBER GAMES","WORD SEARCH"]
frames = []
fr_names = [BOARDGAMES, MOBILEGAMES, WORDGAMES, NUMBERGAMES, WORDSEARCH]

def GAMESANDSOLVERS(master=None):

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
