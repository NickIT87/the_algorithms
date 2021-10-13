## https://www.youtube.com/watch?v=YXPyB4XeYLA

from tkinter import *

root = Tk()

myLabel1 = Label(root, text="Hello world")
myLabel2 = Label(root, text="My name is Nick")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

root.mainloop()