from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(
        root, 
        text="Look! I clicked a button!"
    )
    myLabel.pack()

myButton = Button(
    root, 
    text="Click Me!", 
    pady=50, 
    command=myClick,
    fg="blue",
    bg="red"
)
myButton.pack()

root.mainloop()