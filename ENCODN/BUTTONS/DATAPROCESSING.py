from tkinter import * 
from tkinter import ttk
from FRAMES.TEXTPROCESSING import TEXTPROCESSING
from FRAMES.IMAGEPROCESSING import IMAGEPROCESSING
from FRAMES.RAWDATA import RAWDATA
from FRAMES.DATA_OTHERS import DATA_OTHERS

t_names = ["TEXT PROCESSING", "IMAGE PROCESSING", "RAW DATA", "OTHER"]
frames =[]
fr_names = [TEXTPROCESSING, IMAGEPROCESSING, RAWDATA, DATA_OTHERS]

def DATAPROCESSING(master=None):

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
