import sys
import os

# import re
from tkinter import filedialog
from tkinter import *

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
scale1 = Scale(topFrame, length = 200, variable = var1, label = "S")
scale1.grid(column = 0, row = 1, pady = 50)

#A scale
scale2 = Scale(topFrame, length = 200, variable = var2, label = "A")
scale2.grid(column = 1, row = 1, pady = 50)

#T scale
scale3 = Scale(topFrame, length = 200, variable = var3, label = "T")
scale3.grid(column = 2, row = 1, pady = 50)

scale4 = Scale(topFrame, length = 200, variable = var4, label = "Number of Trials", orient = HORIZONTAL)
scale4.grid(column = 1, row = 2)

#Button that launches main.py & passes values to it.
button = Button(topFrame, width = 20, text = "Start", command = done)
button.grid(column = 1, row = 2, pady = (100, 0))




window.mainloop()
