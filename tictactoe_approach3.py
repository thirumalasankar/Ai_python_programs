"""magic square"""
class tictactoe:
    def __init__(self):
        self.board=[1,2,3,4,5,6,7,8,9]
        self.startGame(self.board)
    def print_board(self,board):
        print()
        print('', board[0], "|", board[1], "|", board[2])
        print("---|---|---")
        print('', board[3], "|", board[4], "|", board[5])
        print("---|---|---")
        print('', board[6], "|", board[7], "|", board[8])
        print()
    def AImove(self,player,board):
        en=False
        if board[4]!='X' and board[4]!='O':
            board[4]=player
            return  
        if 'O' not in board:
            ip=0
            board[ip]='O'
            return
        ip=self.WinBlock(board,'O')
        if ip>=0 and board[ip]!='X' and board[ip]!='O':
            board[ip]='O'
            return
        ip=self.WinBlock(board,'X')
        if ip>=0 and board[ip]!='X' and board[ip]!='O':
            board[ip]='O'
            return
        ip=self.toWin(board,'X')
        if ip>=0 and board[ip]!='X' and board[ip]!='O':
            board[ip]='O'
            return

    def toWin(self,board,player):
        self.mag=[8,1,6,3,5,7,4,9,2]
        for i in range(9):
            for j in range(9):
                if board[i]=='O' and board[j]!="O" and board[j]!="X" :
                    if 15-self.mag[i]-self.mag[j]<=9 and 15-self.mag[i]-self.mag[j]>0:
                        if board[self.mag.index(15-self.mag[i]-self.mag[j])]!="X" and board[self.mag.index(15-self.mag[i]-self.mag[j])]!="O":
                            return j
        for i in range(9):
            if board[i]!="O" and board[i]!="X":
                return i
       
    def WinBlock(self,board,player):
        self.mag=[8,1,6,3,5,7,4,9,2]
        for i in range(0,9):
            for j in range(0,9):
                if i!=j :
                    if board[i]==player and board[j]==player:
                        res=15-self.mag[i]-self.mag[j]
                        if res>0 and res<=9:
                            ind=self.mag.index(res)
                            if board[ind]!="O" and board[ind]!="X":
                                return self.mag.index(res)
                       
        return -1
    def checkWin(self,player,board):
        self.MagicSquare=[8,1,6,3,5,7,4,9,2]
        count = 0
        for x in range(9):
            for y in range(9):
                for z in range(9):
                    if x != y and y != z and z != x:
                        if board[x] == player and board[y] == player and board[z] == player:
                            if self.MagicSquare[x] + self.MagicSquare[y] + self.MagicSquare[z] == 15:
                                if player=='X':
                                    print("Player", player ,"wins!\n")
                                else:
                                    print("----------Computer wins----------")
                               
                                return True
        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                count += 1
            if count == 9:
                print("-----------The game ends in a Tie----------\n")
                return True
        return False
       
    def startGame(self,board):
        self.end=False
        self.print_board(board)
        while not self.end:
            self.end=self.checkWin('X',board)
            if self.end==True :
                print("----------Game over----------")
                break
            inp=int(input("Enter a value of square to fill in it:"))
           
            if board[inp-1] !='X' and board[inp-1]!='O' and inp<=9 and inp>=1:
                board[inp-1]='X'
            else :
                print("the place is already filled ")
                continue
            self.print_board(board)
            self.end=self.checkWin('X',board)
            if self.end==True:
                print("-----------Game Over----------")
                break    
           
            self.AImove('O',board)
            self.end=self.checkWin('O',board)
            self.print_board(board)
            if self.end==True:
                print("-----------Game Over---------")
                break
        
if __name__=="__main__":
    tictactoe()

    
 """output:--
 
 
 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9

Enter a value of square to fill in it:2

 1 | X | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9


 1 | X | 3
---|---|---
 4 | O | 6
---|---|---
 7 | 8 | 9

Enter a value of square to fill in it:4

 1 | X | 3
---|---|---
 X | O | 6
---|---|---
 7 | 8 | 9


 O | X | 3
---|---|---
 X | O | 6
---|---|---
 7 | 8 | 9

Enter a value of square to fill in it:8

 O | X | 3
---|---|---
 X | O | 6
---|---|---
 7 | X | 9

----------Computer wins----------

 O | X | 3
---|---|---
 X | O | 6
---|---|---
 7 | X | O

-----------Game Over---------
"""
