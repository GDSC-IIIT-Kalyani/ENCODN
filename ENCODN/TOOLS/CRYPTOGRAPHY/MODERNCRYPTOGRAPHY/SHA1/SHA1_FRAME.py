from tkinter import *
from tkinter import ttk
from .SHA1 import encrypt, decrypt

def SHA1_FRAME(master=None):

	s = ttk.Style(master)
	s.theme_use('awdark')

	lf1 = ttk.LabelFrame(master)
	lf1.grid(row=1, column=1, sticky="nsew", padx=150, pady=40)

	ttk.Label(lf1, text="Plaintext").grid(row=0,column=0, columnspan=2, padx=20, pady=20, sticky="nsew")
	ttk.Label(lf1, text="SHA-1 Hash").grid(row=2, columnspan=2, padx=20, pady=20, sticky="nsew")

	inp = ttk.Entry(lf1)
	out = ttk.Entry(lf1)
	inp.grid(row=0, column=2)
	out.grid(row=2, column=2)

	ttk.Button(lf1, text="Encrypt", command=lambda: out.insert(0,encrypt(inp.get()))).grid(row=1, column = 7, padx=20, pady=20, sticky="nsew")

	lf2 = ttk.LabelFrame(master)
	lf2.grid(row=2, column=1,sticky="nsew", padx=150, pady=40)

	ttk.Label(lf2, text="SHA-1 Hash").grid(row=14,column=0, columnspan=2, padx=20, pady=20, sticky="nsew")
	ttk.Label(lf2, text="Plaintext").grid(row=16, columnspan=2, padx=20, pady=20, sticky="nsew")

	inp1 = ttk.Entry(lf2)
	out1 = ttk.Entry(lf2)
	inp1.grid(row=14, column=2)
	out1.grid(row=16, column=2)

	ttk.Button(lf2, text="Decrypt", command=lambda: out1.insert(0,decrypt(inp1.get()))).grid(row=15, column = 7, padx=20, pady=20, sticky="nsew")
