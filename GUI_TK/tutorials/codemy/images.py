from tkinter import *

root = Tk()
root.title('Learn To Code at Codemy.com')

img = PhotoImage(file="tkicon.png")
root.iconphoto(False, img)

button_quit = Button(root, text="Exit program", command=root.quit)
button_quit.pack()

root.mainloop()