from tkinter import *

b = []

class OTHERS(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller

		frame = Frame(parent,bg="#ff33aa", width = 750, height=500)
		frame.grid(row=0, column=1, sticky="e",pady=25)
		frame.grid_propagate(0)

		t_names = ["OPTION1","OPTION2"]
	#func = [MORSECODE_FRAME]

		for i in range(len(t_names)):
			b.append(Button(parent,text=t_names[i],bg ='#121212' ,fg='#ffffff').grid(row=0,column=0,sticky="nw",pady=(32*(i+1))))

