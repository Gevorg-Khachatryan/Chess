from tkinter import *
import time
master = Tk()
x=False
step=''
step2=''
canvas_width = 800
canvas_height = 400
w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()
e =''
def click(event):

    global x,step,step2,e
    ex = event.x // 30
    ey = event.y // 30

    if x==True:
        w.delete(step,step2)
        w.delete(e)
        e = w.create_text(15 + (30 * ex), 15 + (30 * ey), text='♙', font="Times 20  ")
        x=False
    else:
        x=True
        if ex >1 and ey >1:
            step2= w.create_rectangle(-30 + (30 * ex), 30 + (30 * ey), 00 + (30 * ex), 60 + (30 * ey), fill="green")

        step = w.create_rectangle(30 + (30 * ex), 30 + (30 * ey), 60 + (30 * ex), 60 + (30 * ey), fill="green")


def b():
    red = 'red'
    black = 'black'
    m = 30
    n = 60
    for j in range(4):
        x = 30
        y = 60
        for i in range(4):
            w.create_rectangle(x, m, y, n, fill=red)
            w.create_rectangle(x + 30, m, y + 30, n, fill=black)
            x += 60
            y += 60
        x = 30
        y = 60
        for i in range(4):
            w.create_rectangle(x, m + 30, y, n + 30, fill="black")
            w.create_rectangle(x + 30, m + 30, y + 30, n + 30, fill="red")
            x += 60
            y += 60
        m += 60
        n += 60

b()
e= w.create_text(45, 45, text='♙', font="Times 20  ")
w.bind("<Button-1>", click)

mainloop()