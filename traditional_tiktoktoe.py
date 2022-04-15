"""general approach"""

B = {'1': ' ' , '2': ' ' , '3': ' ' ,
     '4': ' ' , '5': ' ' , '6': ' ' ,
      '7': ' ' , '8': ' ' , '9': ' ' }
board_keys = []
for key in B:
    board_keys.append(key)
def printBoard(board):
    print(f" {board['1']} | {board['2']} | {board['3']}")
    print('---+---+---')
    print(f" {board['4']} | {board['5']} | {board['6']}")
    print('---+---+---')
    print(f" {board['7']} | {board['8']} | {board['9']}")
def game():
    turn = 'T'
    count = 0
    for i in range(10):
        printBoard(B)
        print("It's your turn," + turn + ".Move to which place?")
        move = input()        
        if B[move] == ' ':
            B[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue
        # Now we will check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            if B['1']==B['2']==B['3']!=' ' or B['4']==B['5']==B['6']!=' ' or B['7']==B['8']==B['9']!=' ' or B['1']==B['4']==B['7']!=' ' or B['2']==B['5']==B['8']!=' ' or B['3']==B['6']==B['9']!=' ' or B['1']==B['5']==B['9']!=' ' or B['3']==B['5']==B['7']!=' ':
                printBoard(B)
                print("\nGame Over.\n")                
                print(f" ****  {turn} won \U0001F970 \U0001F60D7 ****")                
                break  
        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")
        if turn =='T':
            turn = 'H'
        else:
            turn = 'T'        
    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            B[key] = " "
        game()
if __name__ == "__main__":
    game()
    
    
"""
output:--


  |   |  
---+---+---
   |   |  
---+---+---
   |   |  
It's your turn,T.Move to which place?
4
   |   |  
---+---+---
 T |   |  
---+---+---
   |   |  
It's your turn,H.Move to which place?
1
 H |   |  
---+---+---
 T |   |  
---+---+---
   |   |  
It's your turn,T.Move to which place?
7
 H |   |  
---+---+---
 T |   |  
---+---+---
 T |   |  
It's your turn,H.Move to which place?
5
 H |   |  
---+---+---
 T | H |  
---+---+---
 T |   |  
It's your turn,T.Move to which place?
2
 H | T |  
---+---+---
 T | H |  
---+---+---
 T |   |  
It's your turn,H.Move to which place?
9
 H | T |  
---+---+---
 T | H |  
---+---+---
 T |   | H

Game Over.

 ****  H won 🥰 😍7 ****
Do want to play Again?(y/n)n"""
