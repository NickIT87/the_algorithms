from tkinter import *

root = Tk()
#the_label = Label(root, text="hello")
#the_label.pack()

top_frame = Frame(root)
top_frame.pack()

bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)

btn1 = Button(top_frame, text="button1", fg="red")
btn2 = Button(top_frame, text="button2", fg="green")
btn3 = Button(top_frame, text="button3", fg="blue")
btn4 = Button(bottom_frame, text="button4", fg="cyan")

btn1.pack(side=LEFT)
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)
btn4.pack(side=BOTTOM)

root.mainloop()