# Example code for GUI based application in Python
# Tkinter library for GUI implementation

from Tkinter import *
import Tkinter
import tkMessageBox


top = Tk() # Initializing class for TKinter module
L1 = Label(top, text="HI") # Label is the method to print the text
L1.pack( side = LEFT)
E1 = Entry(top, bd =5) # Entry method to create a blank entry
E1.pack(side = RIGHT)
B=Button(top, text ="Hello",) # Button is to create button
B.pack()

top.mainloop()
