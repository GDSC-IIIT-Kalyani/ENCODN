from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.master.title("ENCODN")

        Pane1 = Frame(master, bg="black")
        Pane2 = Frame(master)
        Pane1.grid(row=0, column=0, padx=10, pady=10)
        Pane2.grid(row=0, column=1)
          
        #btNames = ["Morse Code", "Caeser Cypher", "Vignere Cypher"] 
        #will convert this part to a loop 
        frNames = ["Frame1", "Frame2", "Frame3"]  
        
        Button(Pane1, text="Morse Code".format(0), command=lambda: self.show_frame(frNames[0])).grid(row=0,column=0, padx=5, pady=5, sticky=E+W)
        Button(Pane1, text="Caeser Cypher".format(1), command=lambda: self.show_frame(frNames[1])).grid(row=1,column=0, padx=5, pady=5, sticky=E+W)
        Button(Pane1, text="Vignere Cypher".format(2), command=lambda: self.show_frame(frNames[2])).grid(row=2,column=0, padx=5, pady=5, sticky=E+W)

        self.frames = {}
        for F in (Frame1, Frame2, Frame3):
            page_name = F.__name__
            frame = F(parent=Pane2, controller=self)
            self.frames[page_name] = frame

            frame.config()
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Frame1") #so it starts by default 

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class Frame1(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)
        box1 = Frame(self)
        box2 = Frame(self)
        box1.grid(row=0, column=0, rowspan=7, columnspan=7)
        box2.grid(row=1, column=0, rowspan=7, columnspan=7)

        l1 = Label(box1, text="Input Text", fg="green")
        l1.grid(row=0, column=0, padx=5, pady=5)
        e1 = Entry(box1, width=10, borderwidth=5)
        e1.grid(row = 0, column = 3, padx=5, pady=5)        
        l3 = Label(box1, text="Morse code", fg="green")
        l3.grid(row=4, column=0, padx=5, pady=5)
        e3 = Entry(box1, width=10, borderwidth=5)
        e3.grid(row = 4, column = 3, padx=5, pady=5)        
        Button(box1, text="Encrypt", command= lambda: encrypt()).grid(row=2, column=6)

        l4 = Label(box2, text="Morse Code", fg="green")
        l4.grid(row=0, column=0, padx=5, pady=5)
        e4 = Entry(box2, width=10, borderwidth=5)
        e4.grid(row = 0, column = 3, padx=5, pady=5)        
        l6 = Label(box2, text="Plain Text", fg="green")
        l6.grid(row=4, column=0, padx=5, pady=5)
        e6 = Entry(box2, width=10, borderwidth=5)
        e6.grid(row = 4, column = 3, padx=5, pady=5)        
        Button(box2, text="Decrypt", command= lambda: encrypt()).grid(row=2, column=6)

    def encrypt(self):  
        #k = self.e2.get()
        s = self.e1.get()
        ans = ""
        for ch in plaintext.upper():
            if ch.isalpha():
                ans += chr((ord(ch) + key - 65) % 26 + 65)
            else:
                ans += ch
        self.e3.delete(0, END)
        self.e3.insert(0, ans)

class Frame2(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        box1 = Frame(self)
        box2 = Frame(self)
        box1.grid(row=0, column=0, rowspan=7, columnspan=7)
        box2.grid(row=1, column=0, rowspan=7, columnspan=7)

        l1 = Label(box1, text="Input Text", fg="green")
        l1.grid(row=0, column=0, padx=5, pady=5)
        e1 = Entry(box1, width=10, borderwidth=5)
        e1.grid(row = 0, column = 3, padx=5, pady=5)
        l2 = Label(box1, text="Key", fg="green")
        l2.grid(row=2, column=0, padx=5, pady=5)
        e2 = Entry(box1, width=10, borderwidth=5)
        e2.grid(row = 2, column = 3, padx=5, pady=5)        
        l3 = Label(box1, text="Caeser code", fg="green")
        l3.grid(row=4, column=0, padx=5, pady=5)
        e3 = Entry(box1, width=10, borderwidth=5)
        e3.grid(row = 4, column = 3, padx=5, pady=5)        
        Button(box1, text="Encrypt", command= lambda: encrypt()).grid(row=2, column=6)

        l4 = Label(box2, text="Input Caeser Code", fg="green")
        l4.grid(row=0, column=0, padx=5, pady=5)
        e4 = Entry(box2, width=10, borderwidth=5)
        e4.grid(row = 0, column = 3, padx=5, pady=5)
        l5 = Label(box2, text="Key", fg="green")
        l5.grid(row=2, column=0, padx=5, pady=5)
        e5 = Entry(box2, width=10, borderwidth=5)
        e5.grid(row = 2, column = 3, padx=5, pady=5)        
        l6 = Label(box2, text="Plain Text", fg="green")
        l6.grid(row=4, column=0, padx=5, pady=5)
        e6 = Entry(box2, width=10, borderwidth=5)
        e6.grid(row = 4, column = 3, padx=5, pady=5)        
        Button(box2, text="Decrypt", command= lambda: encrypt()).grid(row=2, column=6)

    def encrypt(self):  
        k = self.e2.get()
        s = self.e1.get()
        ans = ""
        for ch in plaintext.upper():
            if ch.isalpha():
                ans += chr((ord(ch) + key - 65) % 26 + 65)
            else:
                ans += ch
        self.e3.delete(0, END)
        self.e3.insert(0, ans)

class Frame3(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        box1 = Frame(self)
        box2 = Frame(self)
        box1.grid(row=0, column=0, rowspan=7, columnspan=7)
        box2.grid(row=1, column=0, rowspan=7, columnspan=7)

        l1 = Label(box1, text="Input Text", fg="green")
        l1.grid(row=0, column=0, padx=5, pady=5)
        e1 = Entry(box1, width=10, borderwidth=5)
        e1.grid(row = 0, column = 3, padx=5, pady=5)
        l2 = Label(box1, text="Key", fg="green")
        l2.grid(row=2, column=0, padx=5, pady=5)
        e2 = Entry(box1, width=10, borderwidth=5)
        e2.grid(row = 2, column = 3, padx=5, pady=5)        
        l3 = Label(box1, text="Vignere code", fg="green")
        l3.grid(row=4, column=0, padx=5, pady=5)
        e3 = Entry(box1, width=10, borderwidth=5)
        e3.grid(row = 4, column = 3, padx=5, pady=5)        
        Button(box1, text="Encrypt", command= lambda: encrypt()).grid(row=2, column=6)

        l4 = Label(box2, text="Input Vignere Code", fg="green")
        l4.grid(row=0, column=0, padx=5, pady=5)
        e4 = Entry(box2, width=10, borderwidth=5)
        e4.grid(row = 0, column = 3, padx=5, pady=5)
        l5 = Label(box2, text="Key", fg="green")
        l5.grid(row=2, column=0, padx=5, pady=5)
        e5 = Entry(box2, width=10, borderwidth=5)
        e5.grid(row = 2, column = 3, padx=5, pady=5)        
        l6 = Label(box2, text="Plain Text", fg="green")
        l6.grid(row=4, column=0, padx=5, pady=5)
        e6 = Entry(box2, width=10, borderwidth=5)
        e6.grid(row = 4, column = 3, padx=5, pady=5)        
        Button(box2, text="Decrypt", command= lambda: encrypt()).grid(row=2, column=6)

    def encrypt(self):  
        k = self.e2.get()
        s = self.e1.get()
        ans = ""
        for ch in plaintext.upper():
            if ch.isalpha():
                ans += chr((ord(ch) + key - 65) % 26 + 65)
            else:
                ans += ch
        self.e3.delete(0, END)
        self.e3.insert(0, ans)

root = Tk()
root.geometry("500x500+300+100")
app = Application(master=root)
app.mainloop()