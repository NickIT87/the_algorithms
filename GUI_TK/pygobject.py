#!/usr/bin/env python
#-*- coding: UTF-8 -*-

# GTK 3 pygobject Msys64

from tkinter import *
from random import randint


root = Tk()
canv = Canvas(root, width=600, height=400)

colors=['red', 'green', 'blue', 'cyan', 'magenta', 'pink', '#F2450C']

def func(event):
    num = randint(1, len(colors))
    cl = colors[num-1]
    wd = randint(20,60)
    ht = randint(20,60)
    x = event.x
    y = event.y
    #circle = canv.create_oval(x,y,x + wd, y + ht, fill=cl, outline="black")
    rect = canv.create_rectangle(x,y,x + wd, y + ht, fill=cl, outline="black")
    print(cl)

canv.bind('<Button-1>', func)

canv.pack()

root.mainloop()
