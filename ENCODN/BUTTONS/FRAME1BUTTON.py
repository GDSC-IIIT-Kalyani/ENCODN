
from tkinter import *
from FRAMES import FRAME1


#class Buttons(Button)
#	def _init_(self, master=None):
#		Button._init_(self,master)
		
def button():

	frame = FRAME1.FRAME1

	button1 = Button(frame,text="Games",bg =  '#c4c4c4' ,fg='black',relief=RAISED,font=('Roboto',12,'bold'),command = root.root.destroy,width = '15')
	button1.grid(row = 0,pady = (150,8),padx = 50,sticky = 'W')

	button2 = Button(frame,text="Cryptography",bg = '#c4c4c4',fg='black',relief=RAISED,font=('Roboto',12,'bold'),width = '15')
	button2.grid(row = 2,pady = 8)

	button3 = Button(frame,text="Mathematics",bg = '#c4c4c4',fg='black',relief=RAISED,font=('Roboto',12,'bold'),width = '15')
	button3.grid(row = 3,pady = 8)

	button4 = Button(frame,text="Informatics",bg = '#c4c4c4',fg='black',relief=RAISED,font=('Roboto',12,'bold'),width = '15')
	button4.grid(row = 4,pady = 8)

	button5 = Button(frame,text="Communication",bg = '#c4c4c4',fg='black',relief=RAISED,font=('Roboto',12,'bold'),width = '15')
	button5.grid(row = 5,pady = (8,300))


#root.root.mainloop()
