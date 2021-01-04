# simple stopwatch

from tkinter import *
from datetime import datetime


temp = 0
after_id = ''

def tick():
    global temp, after_id
    after_id = root.after(1000, tick)
    f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")
    label1.configure(text=str(f_temp))
    temp += 1

def start_sw():
    btn1.grid_forget()
    btn2.grid(row=1, columnspan=2, sticky="ew")
    tick()

def stop_sw():
    btn2.grid_forget()
    btn3.grid(row=1, column=0, sticky="ew")
    btn4.grid(row=1, column=1, sticky="ew")
    root.after_cancel(after_id)

def continue_sw():
    btn3.grid_forget()
    btn4.grid_forget()
    btn2.grid(row=1, columnspan=2, sticky="ew")
    tick()

def reset_sw():
    global temp
    temp = 0
    label1.configure(text="00:00")
    btn3.grid_forget()
    btn4.grid_forget()
    btn1.grid(row=1, columnspan=2, sticky="ew")

root = Tk()
root.title("stopwatch")

label1 = Label(root, width=5, font=("Ubuntu", 100), text="00:00")
label1.grid(row=0, columnspan=2)

btn1 = Button(root, text="Start", font=("Ubuntu", 30), command=start_sw)
btn2 = Button(root, text="Stop", font=("Ubuntu", 30), command=stop_sw)
btn3 = Button(root, text="Continue", font=("Ubuntu", 30), command=continue_sw)
btn4 = Button(root, text="Reset", font=("Ubuntu", 30), command=reset_sw)

btn1.grid(row=1, columnspan=2, sticky="ew")

root.mainloop()