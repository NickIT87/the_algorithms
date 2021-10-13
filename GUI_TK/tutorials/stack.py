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

    # https://youtu.be/IlkyJV_7qDc?list=PLku9se_HAVOp8pSgrIWGIjHLP-EOw_ywq&t=377