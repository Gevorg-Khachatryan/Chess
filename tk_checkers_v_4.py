from tkinter import *
from random import randrange


class Chess:
    checkers = Tk()
    checkers.title('Checkers')
    clc = False
    x = None
    y = None
    # img = PhotoImage(file=r'stockIcon.png')
    # chess.call('wm', 'iconphoto', chess._w, img)
    checkers.iconbitmap('stockIcon.ico')
    board = [[i, j] for i in range(1, 9) for j in range(1, 9)]
    w = Canvas(checkers, width=300, height=300)
    w.pack()
    w_pawn = [[i, j] if (i + j) % 2 == 0 else [0, 0] for i in range(1, 9) for j in range(1, 4)]

    b_pawn = [[i, j] if (i + j) % 2 == 0 else [0, 0] for i in range(1, 9) for j in range(6, 9)]

    a = []
    b = []
    for i in range(len(w_pawn)):
        if w_pawn[i][0] != 0:
            a.append(w_pawn[i])
        if b_pawn[i][0] != 0:
            b.append(b_pawn[i])
    w_pawn = a.copy()
    b_pawn = b.copy()

    print(w_pawn, len(w_pawn))
    print(b_pawn)
    b_pawn.sort(key=lambda x: x[1])

    def __init__(self):
        self.createboard()
        self.enumerate()
        self.figures()
        self.b()

    def createboard(self):
        for j in self.board:

            if (j[0] + j[1]) % 2 == 0:
                self.w.create_rectangle(30 * j[0], 30 * j[1], 30 + 30 * j[0], 30 + 30 * j[1], fill='peru')
            else:
                self.w.create_rectangle(30 * j[0], 30 * j[1], 30 + 30 * j[0], 30 + 30 * j[1], fill='white')

    def enumerate(self):
        xcor = list('ABCDEFGH')

        ycor = list('12345678')

        for i in range(len(xcor)):
            self.w.create_text(15, 15 + 30 * (i + 1), text=ycor[i])
            self.w.create_text(290, 15 + 30 * (i + 1), text=ycor[i])
            self.w.create_text(15 + 30 * (i + 1), 15, text=xcor[i])
            self.w.create_text(15 + 30 * (i + 1), 290, text=xcor[i])

    def figures(self):
        for j in self.w_pawn:

            if (sum(j) % 2 == 0):
                self.w.create_text(15 + 30 * j[0], 15 + 30 * j[1], text='♙', font="Times 20  ")
        for j in self.b_pawn:

            if (sum(j) % 2 == 0):
                self.w.create_text(15 + 30 * j[0], 15 + 30 * j[1], text='♟', font="Times 20  ")

    def b(self):
        self.w.bind("<Button-1>", self.click)

    def click(self, event):
        print('----------------------------------------------')
        if 0 < event.x // 30 < 9 and 0 < event.y // 30 < 9 and (event.x // 30 + event.y // 30)%2==0:
            if [event.x // 30, event.y // 30] in self.w_pawn and self.clc == False:
                self.x = event.x // 30
                self.y = event.y // 30
                self.clc = True
            if self.clc and [event.x // 30, event.y // 30] not in self.w_pawn :

                if [event.x // 30, event.y // 30] not in self.b_pawn:
                    for i in self.w_pawn:
                        if i == [self.x, self.y]:
                            i[0], i[1] = event.x // 30, event.y // 30
                    self.x, self.y = None, None
                    self.clc = False

                elif [event.x // 30, event.y // 30]  in self.b_pawn\
                    and [event.x//30-(self.x-event.x//30),event.y//30-(self.y-event.y//30)] not in self.b_pawn\
                    and [event.x//30-(self.x-event.x//30),event.y//30-(self.y-event.y//30)] not in self.w_pawn\
                        and 0<event.x//30-(self.x-event.x//30)<9 and 0<event.y//30-(self.y-event.y//30)<9:
                    print([event.x//30-(self.x-event.x//30),event.y//30-(self.y-event.y//30)],'else')
                    for i in self.w_pawn:
                        if i == [self.x, self.y]:
                            i[0], i[1] = event.x//30-(self.x-event.x//30),event.y//30-(self.y-event.y//30)
                    t=0
                    while t < 12:
                        if self.b_pawn[t][0] == event.x//30 and self.b_pawn[t][1] == event.y//30:
                            print(self.b_pawn[t])
                            del self.b_pawn[t]
                            break
                        t += 1

                    self.x, self.y = None, None
                    self.clc = False
                self.pc()
                self.createboard()
                self.figures()

        #print(self.w_pawn)
        #print(self.b_pawn)


    def pc(self):
        for i in range(len(self.b_pawn)):
            x=self.b_pawn[i][0]
            y=self.b_pawn[i][1]
            y-=1
            x-=randrange(-1,2,2)
            nx, ny = x - (self.b_pawn[i][0] - x), y - (self.b_pawn[i][1] - y)
            if 0 < x  < 9 and 0 < y < 9 and (x +y) % 2 == 0 :
                if [x,y]not in self.w_pawn and [x,y]not in self.b_pawn:
                    self.b_pawn[i][0]=x
                    self.b_pawn[i][1]=y
                    break
                if [x,y] in self.w_pawn and [nx,ny] not in self.w_pawn and [nx,ny]not in self.b_pawn and 0<nx<9 and 0<ny<9:
                    self.b_pawn[i][0] = nx
                    self.b_pawn[i][1] = ny
                    t=0
                    while t<12:
                        if self.w_pawn[t][0]==x and self.w_pawn[t][1]==y:
                            del self.w_pawn[t]
                            break
                        t+=1

                    break

        self.b_pawn.sort(key=lambda x:x[1])




Chess()
mainloop()