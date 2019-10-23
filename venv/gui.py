import sys
import os

# import re
from tkinter import filedialog
from tkinter import *
from tkinter import ttk

#function to pass values out.
def done():
    selection.append(var1.get())
    selection.append(var2.get())
    selection.append(var3.get())
    selection.append(var4.get())
    coffee = os.getcwd() + "/main.py "
    # print(coffee)
    temp = 'python ' + coffee + " " + str(selection[0]) + " " + str(selection[1]) + " " + str(selection[2]) + " " + str(selection[3])
    # print(temp)
    os.system(temp)
    selection.clear()

selection = []

window = Tk()
window.geometry('500x450')
window.title("Tile Simulator")

topFrame = Frame(window)
topFrame.pack()
bottomFrame = Frame(window)
bottomFrame.pack(side = BOTTOM)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()


#S scale
# scale1 = Scale(topFrame, length = 200, variable = var1, label = "S", to = 10000)
s1 = Spinbox(topFrame, from_ = 0, to = 10000, width = 10, textvariable = var1)
s1.grid(column = 0, row = 1, pady = 50)
lbl1 = Label(topFrame, text = "S")
lbl1.grid(column = 0, row = 1, padx = (0, 130))

#A scale
# scale2 = Scale(topFrame, length = 200, variable = var2, label = "A", to = 10000)
s2 = Spinbox(topFrame, from_ = 0, to = 10000, width = 10, textvariable = var2)
s2.grid(column = 1, row = 1, pady = 50)
lbl2 = Label(topFrame, text = "A")
lbl2.grid(column = 1, row = 1, padx = (0, 130))

#T scale
# scale3 = Scale(topFrame, length = 200, variable = var3, label = "T", to = 10000)
s3 = Spinbox(topFrame, from_ = 0, to = 10000, width = 10, textvariable = var3)
s3.grid(column = 2, row = 1, pady = 50)
lbl3 = Label(topFrame, text = "T")
lbl3.grid(column = 2, row = 1, padx = (0, 130))

# scale4 = Scale(topFrame, length = 200, variable = var4, label = "Number of Trials", orient = HORIZONTAL, to = 10000)
s4 = Spinbox(topFrame, from_ = 0, to = 10000, width = 10, textvariable = var4)
s4.grid(column = 1, row = 2)
lbl4 = Label(topFrame, text = "Range")
lbl4.grid(column = 1, row = 2, padx = (0, 150))

#Button that launches main.py & passes values to it.
button = Button(topFrame, width = 20, text = "Start", command = done)
button.grid(column = 1, row = 2, pady = (100, 0))

# progressbar = ttk.Progressbar(topFrame,orient=HORIZONTAL,length=100,mode='determinate')
# progressbar.grid(column = 1, row = 2, pady = (200, 0))

window.mainloop()
