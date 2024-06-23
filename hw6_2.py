import random
import math
def create_board(row,col,candy_type):
    board=[[0 for _ in range(col)] for _ in range(row)]
    
    for i in range(row):
        for j in range(col):
            index=random.randint(0,len(candy_type)-1)
            board[i][j]=candy_type[index]
    return board        

def game(board,candy_type):
    print("You switched")
    print_board(board)
    row=len(board)
    col=len(board[0])
    stable=False
    
    while stable==False:
        
        #crush candy
        crush=[[0 for _ in range(col)] for _ in range(row)]#0 is not crushed
        for i in range(row):
            for j in range(col):
                if board[i][j]==0:
                    continue
                
                if i+2<row: #vertical
                    if board[i+1][j]==board[i][j] and board[i+2][j]==board[i][j] :
                        crush[i][j]=1
                        crush[i+1][j]=1
                        crush[i+2][j]=1
                if j+2<col: #horizontal
                    if board[i][j+1]==board[i][j] and board[i][j+2]==board[i][j] :
                        crush[i][j]=1
                        crush[i][j+1]=1
                        crush[i][j+2]=1
        #drop candy
        board_col=[]
        crush_col=[]
        
        for j in range(col):
            
            for i in range(row):
                if crush[i][j]==1:
                    board[i][j]=-1 #-1代表要drop
                    
            
            for i in range(row-1,-1,-1):
                while board[i][j]==-1:
                    for k in range(i,-1,-1):
                        if k-1<0:
                            index=random.randint(0,len(candy_type)-1)
                            board[k][j]=candy_type[index]
                            continue
                        board[k][j]=board[k-1][j]
        
        
            
        #check board
        stable=True
        for i in range(row):
            for j in range(col):
                if board[i][j]==0:
                    continue
                if i+2<row: #vertical
                    if board[i+1][j]==board[i][j] and board[i+2][j]==board[i][j] :
                        stable=False
                if j+2<col: #horizontal
                    if board[i][j+1]==board[i][j] and board[i][j+2]==board[i][j] :
                        stable=False
        
        print("After you switched")
        print_board(board)
               
    return board

def print_board(board):
    row=len(board)
    col=len(board[0])
    
    for i in range(row):
        print(board[i])
        
    print("---------------------------")

num=0       
row_str=input("input the height of the board:")
col_str=input("input the row of the board:")
types_str=input("input the number of candy types:")
row=int(row_str)
col=int(col_str)
types=int(types_str)
candy_type=[]
for i in range(types):
    candy_type.append(random.randint(100,999))

board=create_board(row, col, candy_type)
print("Initial Board")
print_board(board)
board=game(board, candy_type)



num=0
while num<10:
    index1_str=input("input switch1:")
    index2_str=input("input switch2:")
    index1=int(index1_str)
    index2=int(index2_str)

    index1_row=int(index1/row)
    index1_col=index1 % col
    index2_row=int(index2 / row)
    index2_col=index2 % col
    
    temp=board[index1_row][index1_col]
    print(temp)
    print(board[index2_row][index2_col])
    board[index1_row][index1_col]=board[index2_row][index2_col]
    board[index2_row][index2_col]=temp
    
    game(board, candy_type)
    
    num+=1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    