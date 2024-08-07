import random
import tkinter as tk

import sudokuGenerator as sg
import sudokuTemplates as st

root = tk.Tk()
root.title("Sudoku")
testIndex = random.randint(0, (len(st.template) -1))

data = st.template[testIndex]

answer = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
]

def setValue(x, y, value):
    data[x][y] = value.get()

canvas = tk.Canvas(root)
canvas.grid(row=0 , column=0)

cell_width = 30
cell_height = 30

for i, row in enumerate(data):
    for j, value in enumerate(row):
        x = j * cell_width + cell_width / 2
        y = i * cell_height + cell_height / 2
        
        entry_value = tk.StringVar(value=str(value))
        entry_value.trace("w", lambda name, index, mode, sv=entry_value, i=i, j=j: setValue(i, j, sv))

        entry = tk.Entry(canvas, width=2, justify='center', textvariable=entry_value)
        canvas.create_window(x, y, window=entry)

        if j < len(row) and j % 3 == 0 :
            canvas.create_line(j * cell_width,
                i * cell_height,
                j * cell_width,
                (i + 1) * cell_height
            )

        if i < len(data) and i % 3 == 0:
            canvas.create_line(j * cell_width,
                i * cell_height,
                (j + 1) * cell_width,
                i * cell_height
            )


canvas.config(width=cell_width * len(data[0]), height=cell_height * len(data))

tk.Button(root, text="Quit", command=root.destroy).grid(column=0, row=11)
tk.Button(root, text="Solve", command= lambda: sg.solve(data)).grid(column=0, row=10)


root.mainloop()
