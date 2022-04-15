"""even odd method"""

B={'1':2,'2':2,'3':2,'4':2,'5':2,'6':2,'7':2,'8':2,'9':2}
board_keys=[]
for key in B:
    board_keys.append(key)
def printBoard(board):
    print(f" {board['1']} | {board['2']} | {board['3']}")
    print('---+---+---')
    print(f" {board['4']} | {board['5']} | {board['6']}")
    print('---+---+---')
    print(f" {board['7']} | {board['8']} | {board['9']}")

def make():
    if B['5']==2:
        return '5'
    elif B['2']==2:
        return '2'
    elif B['4']==2:
        return '4'
    elif B['6']==2:
        return '6'
    elif B['8']==2:
        return '8'

def switch_player(count):
    current_player='C' if count%2!=0 else 'H'
    return current_player


def go(move):
    B[str(move)]=5

def posswin():
        if B['1']*B['2']*B['3']==18 or B['1']*B['2']*B['3']==50:
            if B['1']==2:
                return 1
            elif B['2']==2:
                return 2
            else:
                return 3
        elif B['4']*B['5']*B['6']==18 or B['4']*B['5']*B['6']==50:
            if B['4']==2:
                return 4
            elif B['5']==2:
                return 5
            else:
                return 6
        elif B['7']*B['8']*B['9']==18 or B['7']*B['8']*B['9']==50:
            if B['7']==2:
                return 7
            elif B['8']==2:
                return 8
            else:
                return 9
        elif B['1']*B['4']*B['7']==18 or B['1']*B['4']*B['7']==50:
            if B['1']==2:
                return 1
            elif B['4']==2:
                return 4
            else:
                return 7
        elif B['2']*B['5']*B['8']==18 or B['2']*B['5']*B['8']==50:
            if B['2']==2:
                return 2
            elif B['5']==2:
                return 5
            else:
                return 8
        elif B['3']*B['6']*B['9']==18 or B['3']*B['6']*B['9']==50:
            if B['3']==2:
                return 3
            elif B['6']==2:
                return 6
            else:
                return 9
        elif B['1']*B['5']*B['9']==18 or B['1']*B['5']*B['9']==50:
            if B['1']==2:
                return 1
            elif B['5']==2:
                return 5
            else:
                return 9
        elif B['3']*B['5']*B['7']==18 or B['3']*B['5']*B['7']==50:
            if B['3']==2:
                return 3
            elif B['5']==2:
                return 5
            else:
                return 7
        else:
            return 0
       
       
def checkwin(current_player):
    if current_player=='C':
        turn="player"
    else:
        turn="computer"
    if B['1']==B['2']==B['3']!=2 or B['4']==B['5']==B['6']!=2 or B['7']==B['8']==B['9']!=2 or B['1']==B['4']==B['7']!=2 or B['2']==B['5']==B['8']!=2 or B['3']==B['6']==B['9']!=2 or B['1']==B['5']==B['9']!=2 or B['3']==B['5']==B['7']!=2:
        printBoard(B)
        print("Game Over!!!.")
        print(" * "+turn+" won. * ")
        return 1
    return 0
def game():
    count=0
    current_player="H"
    for i in range(9):
        printBoard(B)
        print(current_player)
        if current_player=="H":
            print("It's your turn.Move to which place?")
            move=input()
            if B[move]==2:
                B[move]=3
                count+=1
            else:
                print("That square is already filled.\nMove to which square?")
                continue
            current_player=switch_player(count)
        else:
            poss=posswin()
            if poss==0:
                x=make()
                go(x)
            else:
                go(poss)
            print("\nComputer's move\n")
            count+=1
            current_player=switch_player(count)
       
        if count>=5:
            flag=checkwin(current_player)
            if flag:
                break
        if count==9:
            printBoard(B)
            print("Game Over.\n")
            print("it's a tie!!!")
    restart=input("Do you want to play again?(y/n)")
    if restart=="y" or restart=="Y":
        for key in board_keys:
            B[key]=2
        game()
if __name__=="__main__":
    game()
    
    
 """
 output:---
 
 
  2 | 2 | 2
---+---+---
 2 | 2 | 2
---+---+---
 2 | 2 | 2
H
It's your turn.Move to which place?
1
 3 | 2 | 2
---+---+---
 2 | 2 | 2
---+---+---
 2 | 2 | 2
C

Computer's move

 3 | 2 | 2
---+---+---
 2 | 5 | 2
---+---+---
 2 | 2 | 2
H
It's your turn.Move to which place?
2
 3 | 3 | 2
---+---+---
 2 | 5 | 2
---+---+---
 2 | 2 | 2
C

Computer's move

 3 | 3 | 5
---+---+---
 2 | 5 | 2
---+---+---
 2 | 2 | 2
H
It's your turn.Move to which place?
4
 3 | 3 | 5
---+---+---
 3 | 5 | 2
---+---+---
 2 | 2 | 2
C

Computer's move

 3 | 3 | 5
---+---+---
 3 | 5 | 2
---+---+---
 5 | 2 | 2
Game Over!!!.
 * computer won. * 
Do you want to play again?(y/n)n


"""
