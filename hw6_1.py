def game(board):
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
                            board[k][j]=0
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
        
        
                
    return board

def print_board(board):
    row=len(board)
    col=len(board[0])
    
    for i in range(row):
        print(board[i])
            
board1=[[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]] 
board2=[[9,9,7,9,9,9],[7,7,6,8,9,9],[5,6,5,6,8,8],[1,5,1,4,1,1],[2,1,4,1,1,1],[1,4,1,3,1,1],[1,1,2,1,3,1],[1,2,1,1,1,3]]
print_board(board1)
print("-----------------------------")
print_board(game(board1))
print("-----------------------------")
print_board(board2)
print("-----------------------------")
print_board(game(board2))