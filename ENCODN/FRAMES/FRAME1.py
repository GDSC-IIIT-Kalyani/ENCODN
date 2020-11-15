#name of the frame1 is: FRAME1
#name of the frame2 is: FRAME2

from tkinter import *
from tkinter import ttk
from BUTTONS import FRAME1BUTTON as fr1b

class FRAME1class(Frame):
  def __init__(self, master=None):
    Frame.__init__(self, master)

    NB = ttk.Notebook(master)
    NB.grid(sticky="nsew")

    FRAME1 = Frame(NB,width="300", height="768", bg="#222222")
    FRAME1.grid(row=0, column=0)
    
    FRAME2 = Frame(NB,width="724",height="768",bg="#151515")
    FRAME2.grid(row=0, column=1)
    fr1b.FRAME1BUTTON(master=FRAME1, sec_master=FRAME2, nb=NB)
