#name of the frame is: FRAME1
from tkinter import *
import ENCODN
import FRAME2 as fr2

class FRAME1class(Frame)
  def __init__(self, master=None):
    Frame.__init__(self, master)
    FRAME1 = Frame(master, bg="black")
    FRAME1.grid(row=0, column=0, padx=5, pady=5)
