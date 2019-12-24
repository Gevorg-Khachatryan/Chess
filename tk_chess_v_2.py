from tkinter import *


class Chess:
    chess = Tk()
    chess.title('Chess')
    # img = PhotoImage(file=r'stockIcon.png')
    # chess.call('wm', 'iconphoto', chess._w, img)
    chess.iconbitmap('stockIcon.ico')
    board = [[[i, j]   for i in range(1, 9)] for j in range(1, 9)]
    w = Canvas(chess, width=300, height=300)
    w.pack()
    w_pawn = [[[i, j] for i in range(1, 9)] for j in range(1, 4)]
    b_pawn = [[[i, j] for i in range(1, 9)] for j in range(6, 9)]

    def __init__(self):
        self.createboard()
        self.enumerate()
        self.figures()
        self.b()

    def createboard(self):
        for i in self.board:
            for j in i:
                if (j[0] + j[1]) % 2 == 0:
                    self.w.create_rectangle(30 * j[0], 30 * j[1], 30 + 30 * j[0], 30 + 30 * j[1], fill='peru')
                else:
                    self.w.create_rectangle(30 * j[0], 30 * j[1], 30 + 30 * j[0], 30 + 30 * j[1], fill='white')

    def enumerate(self):
        xcor = list('ABCDEFGH')

        ycor = list('87654321')

        for i in range(len(xcor)):
            self.w.create_text(15, 15 + 30 * (i + 1), text=ycor[i])
            self.w.create_text(290, 15 + 30 * (i + 1), text=ycor[i])
            self.w.create_text(15 + 30 * (i + 1), 15, text=xcor[i])
            self.w.create_text(15 + 30 * (i + 1), 290, text=xcor[i])

    def figures(self):
        for i in self.w_pawn:
            for j in i:
                if (sum(j)%2==0):
                    self.w.create_text(15 + 30 * j[0], 15 + 30 * j[1], text='♙', font="Times 20  ")
        for i in self.b_pawn:
            for j in i:
                if (sum(j) % 2 == 0):
                    self.w.create_text(15 + 30 * j[0], 15 + 30 * j[1], text='♟', font="Times 20  ")

    def b(self):
        self.w.bind("<Button-1>", self.click)

    def click(self, event):
        print(event.x, event.y)


Chess()
mainloop()
