from tkinter import *
from tkinter import ttk
from tkinter import font


cell_size = 60      # размер ячейки
cell_num = -1       # номер текущей ячейки
cells = []          # список ячеек

row_count = 5
col_count = 9
cells_count = row_count * col_count

canv_width = cell_size * col_count
canv_height = cell_size * row_count

root_color = "thistle"
fon_color = "#00ffff"
cell_color = "#FAF0BE"

btn_width = 7


def add_fragm():
    global cells
    global cell_num

    if cell_num == cells_count - 1:
        return
    
    cell_num += 1
    row_num = cell_num // col_count
    col_num = cell_num % col_count
    text_tag = 't'+str(cell_num)

    x_beg = col_num * cell_size; x_end = x_beg + cell_size
    y_beg = row_num * cell_size; y_end = y_beg + cell_size
    oval = canv.create_oval(x_beg+2, y_beg+2, x_end-2, y_end-2, fill=cell_color,
                            tag=text_tag, width=2)
    
    val = var_val.get()
    cells.append([val, oval])

    cell_text = str(val)
    canv.create_text(x_beg+cell_size/2, y_beg+cell_size/2, text=cell_text,
                     fill="black", font=digFont, tag=text_tag)


def del_fragm():
    global cell_num
    if cell_num < 0:
        return

    val = cells[cell_num][0]
    var_val.set(val)

    text_tag = "t"+str(cell_num)
    canv.delete(text_tag)
    del(cells[-1])

    cell_num -= 1


root = Tk()
stl = ttk.Style()
dFont = font.Font(family="helvetica", size=16)
digFont = font.Font(family="helvetica", size=20)

root.configure(background=root_color)
stl.configure('.', font=dFont, background=root_color, foreground="black")

ttk.Label(root, text="Обработка стека:", background=root_color).\
    grid(row=1, column=0, padx=5, pady=5, sticky=E)

var_val = IntVar()
var_val.set(1)
edt_val = ttk.Entry(root, width=5, textvariable=var_val, justify=RIGHT, font=dFont)
edt_val.grid(row=1, column=1, padx=5, pady=5)


def fnc_push():
    add_fragm()


btn_push = ttk.Button(root, text="push", width=btn_width, command=fnc_push)
btn_push.grid(row=1, column=2, sticky=E, pady=5, padx=5)


def fnc_pop():
    del_fragm()


btn_pop = ttk.Button(root, text="pop", width=btn_width, command=fnc_pop)
btn_pop.grid(row=1, column=3, sticky=E, pady=5, padx=5)


def fnc_clear():
    global cell_num
    global cells
    canv.delete("all")
    cells = []
    cell_num = -1


btn_clear = ttk.Button(root, text="clear", width=btn_width, command=fnc_clear)
btn_clear.grid(row=1, column=4, sticky=E, pady=5, padx=5)

pnl_canv = Frame(root)
pnl_canv.grid(row=2, column=0, columnspan=col_count, sticky=S, pady=5, padx=5)

canv = Canvas(pnl_canv, width=canv_width, height=canv_height, background=fon_color)
canv.pack(side="top")

root.mainloop()