from os import system

class Chess():
    def __init__(self,queen):
        self.queen=queen

    def chessboard(self):
        board=[list(' ⬜' for i in range(8)) for i in range(8)]
        for i in range(len(board)):
            if i % 2 == 0:
                for j in range(0,len(board[i]),2):
                    board[i][j]=' ⬛'
            else:
                for j in range(1,len(board[i]),2):
                    board[i][j] = ' ⬛'
        board[7][3]=' ♕'
        board[6][0:8]=[' ♙' for i in range(8)]
        for b in board:
            print(''.join(b))
        print('>'*20)
        system("cls")
        while True:

            ni = int(input('figure x : '))
            nj = int(input('figure y : '))

            newi = int(input('step x : '))
            newj = int(input('step y : '))
            board[ni][nj], board[newi][newj] = ' ⬛' if (ni + nj) % 2 == 0 else ' ⬜', board[ni][nj]

            for b in board:
                print(''.join(b))
            print('>' * 20)
        # board[3+self.queen[1][0]][2+self.queen[1][1]]='♕'“⬛”♙

queenn=Chess(((1,0),(0,1),(1,1)))
queenn.chessboard()
