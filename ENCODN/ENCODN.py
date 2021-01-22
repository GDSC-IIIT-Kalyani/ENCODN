from tkinter import *
from tkinter import ttk

#importing functions to initialize buttons
from BUTTONS.COMMUNICATION import COMMUNICATION
from BUTTONS.BIOLOGY import BIOLOGY
from BUTTONS.GAMESANDSOLVERS import GAMESANDSOLVERS
from BUTTONS.MATHEMATICS import MATHEMATICS
from BUTTONS.INFORMATICS import INFORMATICS
from BUTTONS.DATAPROCESSING import DATAPROCESSING
from BUTTONS.HISTORY import HISTORY
from BUTTONS.PHYSICSCHEMISTRY import PHYSICSCHEMISTRY
from BUTTONS.ELECTRONICS import ELECTRONICS
from BUTTONS.MISCELLANEOUS import MISCELLANEOUS
from BUTTONS.DATEANDTIME import DATEANDTIME
from BUTTONS.STEGANOGRAPHY import STEGANOGRAPHY
from BUTTONS.GEOGRAPHY import GEOGRAPHY
from BUTTONS.MUSIC import MUSIC
from BUTTONS.CRYPTOGRAPHY import CRYPTOGRAPHY


root = Tk()
s = ttk.Style(root)

root.call('lappend', 'auto_path', 'C:/Python/THEMES/awthemes-9.3.2')
root.call('package', 'require', 'awdark')

s.theme_use('awdark')
s.configure('lefttab.TNotebook',padding=[50,50], tabposition='wn')

notebook = ttk.Notebook(root, s='lefttab.TNotebook', width=1124, height=768)

t_names = ["      GAMES AND SOLVERS      ", "          CRYPTOGRAPHY           ", "           MATHEMATICS            ", "             INFORMATICS            ", "COMMUNICATION SYSTEMS", "         DATA PROCESSING        ", "                  BIOLOGY                 ", "                  HISTORY                 ", "       PHYSICS-CHEMISTRY      ", "             ELECTRONICS             ", "          MISCELLANEOUS          ", "           DATE AND TIME           ", "          STEGANOGRAPHY        ", "             GEOGRAPHY               ", "                   MUSIC                   "]
lf = []
fr = []

for i in range(15):
	frame = Frame(notebook, bg='#151515', width=900, padx = 30,pady=30, height=600)
	lf.append(LabelFrame(frame, text=t_names[i].strip(), foreground="#dd7a06", background="#222222", width=900, height=600,padx=10, pady=10).grid(sticky="new"))
	notebook.add(frame, text=t_names[i])
	fr.append(frame)
	#frame.grid_propagate(0)

notebook.grid()
notebook.grid_propagate(0)

#calling button setups here
GAMESANDSOLVERS(fr[0])
CRYPTOGRAPHY(fr[1])
MATHEMATICS(fr[2])
INFORMATICS(fr[3])
COMMUNICATION(fr[4])
DATAPROCESSING(fr[5])
BIOLOGY(fr[6])
HISTORY(fr[7])
PHYSICSCHEMISTRY(fr[8])
ELECTRONICS(fr[9])
MISCELLANEOUS(fr[10])
DATEANDTIME(fr[11])
STEGANOGRAPHY(fr[12])
GEOGRAPHY(fr[13])
MUSIC(fr[14])

#215d9c
#if the logo file doesn't show up or has import error try your local path
root.iconphoto(False, PhotoImage(file="ENCODN-logo.png")) 
root.geometry("1124x768")
root.configure(bg="#151515")
root.minsize(1124,768)
#root.maxsize(1124,768)
root.title("ENCODN")

root.mainloop()
