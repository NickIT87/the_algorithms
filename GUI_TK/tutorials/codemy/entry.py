from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=5)
e.pack()

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(
    root, 
    text="Enter Your name", 
    pady=50, 
    command=myClick,
    fg="blue",
    bg="#EA4335"
)
myButton.pack()

root.mainloop()