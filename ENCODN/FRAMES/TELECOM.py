from tkinter import *
from TOOLS1.COMMUNICATION.TELECOM.MORSECODE.MORSECODE_FRAME import MORSECODE_FRAME

b = []

class TELECOM(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller

		frame = Frame(parent,bg="#ffffff", width = 750, height=500)
		frame.grid(row=0, column=1, sticky="e",pady=25)
		frame.grid_propagate(0)

		t_names = ["MORSE CODE"]
		func = [MORSECODE_FRAME]

		for i in range(len(t_names)):
			b.append(Button(parent,text=t_names[i],bg ='#121212' ,fg='#ffffff').grid(row=0,column=0,sticky="nw",pady=(32*(i+1))))

