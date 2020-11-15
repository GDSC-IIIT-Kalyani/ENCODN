from tkinter import * 
from tkinter import ttk
from FRAMES.ARITHMETICS import ARITHMETICS
from FRAMES.SYMBOLIC_COMP import SYMBOLIC_COMP
from FRAMES.COMBINATORICS import COMBINATORICS
from FRAMES.FUNCTIONS import FUNCTIONS
from FRAMES.GEOMETRY import GEOMETRY
from FRAMES.MATRIX import MATRIX
from FRAMES.GRAPH import GRAPH
from FRAMES.SERIES import SERIES
from FRAMES.STATISTICS import STATISTICS
from FRAMES.MATH_OTHERS import MATH_OTHERS

t_names=["ARITHMETICS", "SYMBOLIC_COMP", "COMBINATORICS", "FUNCTIONS", "GEOMETRY", "MATRIX", "GRAPH THEORY", "SERIES", "STATISTICS","OTHERS"]
frames=[]
fr_names = [ARITHMETICS, SYMBOLIC_COMP, COMBINATORICS, FUNCTIONS, GEOMETRY, MATRIX, GRAPH, SERIES, STATISTICS, MATH_OTHERS]

def MATHEMATICS(master=None):

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
