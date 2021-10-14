from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=5)
e.pack()
e.insert(0, "Enter Your Name: ")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(
    root, 
    text="Click Me", 
    pady=50, 
    command=myClick,
    fg="blue",
    bg="#EA4335"
)
myButton.pack()

root.mainloop()