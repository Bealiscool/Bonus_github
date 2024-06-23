import random

def create_board(board): # 0:safe 1:penalty
    
    for i in range(len(board)):
        penalty=random.randint(1, 10)
        if penalty<4:
            board[i]=1

def dice():
    dice=random.randint(1, 6)
    return dice

def print_board(A_index,B_index,board):
    if A_index>len(board)-1:
        A_index=len(board)-1
    if B_index>len(board)-1:
        B_index=len(board)-1
    for i in range(len(board)):
        if i==A_index and i==B_index:
            if board[A_index]==1 and board[B_index]==1:
                print("x",end="")
            elif board[A_index]==0 and board[B_index]==0:
                print("X",end="")
        elif i==A_index:
            if board[A_index]==0:
                print("A",end="")
            else:
                print("a",end="")
        elif i==B_index:
            if board[B_index]==0:
                print("B",end="")
            else:
                print("b",end="")
        else:
            print("_",end="")

def print_penalty(board):
    for i in range(len(board)):
        if board[i]==1:
            print("P",end="")
        else:
            print("_",end="")
            
board=[0]*30
create_board(board)
    
end=5
A_index=0
B_index=0
A_penalty=0  #0:no penalty 1:punish next time 2:have punished
B_penalty=0
A_dice=0
B_dice=0

while (end>0):
    
    
    if A_penalty!=1:
        A_dice=dice()
        A_index=A_index+A_dice
    else:
        A_dice=0
        A_penalty=2
    if B_penalty!=1:
        B_dice=dice()
        B_index=B_index+B_dice
    else:
        B_dice=0
        B_penalty=2
    print_board(A_index, B_index, board)
    print(" (A: ",A_dice,", B: ",B_dice,")")
    
    if A_index>=len(board)-1 and B_index>=len(board)-1:
        print("Both player win!")
        break
    elif A_index>=len(board)-1 :
        print("Player A wins!")
        break
    elif B_index>=len(board)-1 :
        print("Player B wins!")
        break
    # determines Win or lose
    if board[A_index]==1 and A_penalty!=2:
        A_penalty=1
    if board[B_index]==1 and B_penalty!=2:
        B_penalty=1
    
    if A_penalty==2:
        A_penalty=0
    if B_penalty==2:
        B_penalty=0
    
print_penalty(board)
