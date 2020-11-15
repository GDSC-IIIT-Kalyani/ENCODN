from tkinter import *
from tkinter import ttk
from TOOLS1.CRYPTOGRAPHY.MODERNCRYPTOGRAPHY.MD4.MD4_FRAME import MD4_FRAME
from TOOLS1.CRYPTOGRAPHY.MODERNCRYPTOGRAPHY.MD5.MD5_FRAME import MD5_FRAME
from TOOLS1.CRYPTOGRAPHY.MODERNCRYPTOGRAPHY.SHA1.SHA1_FRAME import SHA1_FRAME
from TOOLS1.CRYPTOGRAPHY.MODERNCRYPTOGRAPHY.SHA256.SHA256_FRAME import SHA256_FRAME
from TOOLS1.CRYPTOGRAPHY.MODERNCRYPTOGRAPHY.SHA512.SHA512_FRAME import SHA512_FRAME
from TOOLS1.CRYPTOGRAPHY.MODERNCRYPTOGRAPHY.XOR.XOR_FRAME import XOR_FRAME

t_names = ["MD4","MD5","SHA-1", "SHA-256", "SHA-512", "XOR"]
frames = []
fr_names = [MD4_FRAME, MD5_FRAME, SHA1_FRAME, SHA256_FRAME, SHA512_FRAME, XOR_FRAME]

def MODERNCRYPTOGRAPHY(master=None):

	s = ttk.Style(master)
	s.configure('lefttab.TNotebook',padding=[20,20], tabposition='wn')

	nb = ttk.Notebook(master, s='lefttab.TNotebook', width=800, height=570)
	nb.grid(row=0, column=0, sticky="e", padx=20, pady=15)
	nb.grid_propagate(0)

	for i in range(len(t_names)):
		frames.append(Frame(nb,bg="#7ad159", width = 750, height=500))
		nb.add(frames[i], text=t_names[i])

#calling frame setups here

	for i in range(len(fr_names)):
		fr_names[i](frames[i])
