import random
import time
import math
        


def bombs (x,y): #recursively find answer
    if map[x][y]!=0:
        if map[x][y]!=9:    
            map_fold[x][y]=1
        return True
    for r in range (max(0,x-1),min(x+2,9)):
        for c in range(max(0, y-1),min(y+2,9)):
            if map_fold[r][c]!=0:
                continue
            else:
                if map[r][c]!=9:
                    map_fold[r][c]=1
                bombs(r,c)


    
def print_map ():
    print("  ",end="")
    print("  a ",end="")
    print("  b ",end="")
    print("  c ",end="")
    print("  d ",end="")
    print("  e ",end="")
    print("  f ",end="")
    print("  g ",end="")
    print("  h ",end="")
    print("  i ")
    print("  ",end="")
    for i in range(9):
        print("+---",end="")
    print("+")
    for i in range(9):
        print(i+1,end="")
        for j in range(9):
            print (" | ",end="")
            if map_fold[i][j]==0:
                print (" ",end="")
            if map_fold[i][j]==1:
                print (map[i][j],end="")
            if map_fold[i][j]==2:
                print ("F",end="")
            
        print (" |",end="")
        print ()
        print("  ",end="")
        for k in range(9):
            print("+---",end="")
        print("+")
        
def print_map_ans ():
    print("  ",end="")
    print("  a ",end="")
    print("  b ",end="")
    print("  c ",end="")
    print("  d ",end="")
    print("  e ",end="")
    print("  f ",end="")
    print("  g ",end="")
    print("  h ",end="")
    print("  i ")
    print("  ",end="")
    for i in range(9):
        print("+---",end="")
    print("+")
    for i in range(9):
        print(i+1,end="")
        for j in range(9):
            print (" | ",end="")
            if map[i][j]!=9:    
                print (map[i][j],end="")
            else:
                 print ("X",end="")   
            
        print (" |",end="")
        print ()
        print("  ",end="")
        for k in range(9):
            print("+---",end="")
        print("+")
        
def print_map_fold (): #another map to record is opened or not
    print(" ",end="")
    for i in range(9):
        print("+---",end="")
    print("+")
    for i in range(9):
        for j in range(9):
            print (" | ",end="")
            if map_fold[i][j]==0:
                print (map_fold[i][j],end="")
            if map_fold[i][j]==1:
                print (map_fold[i][j],end="")
            
        print (" |",end="")
        print ()
        print(" ",end="")
        for k in range(9):
            print("+---",end="")
        print("+")

        





end=0
mine_found=0
start_time=time.time()
while (end!=-1):#game loop
    if end==0:
        map=[[0]*9 for i in range(9)]
        for i in range(9):
            for j in range(9):
                map[i][j]=9
        #create map

        map_fold=[[0]*9 for i in range(9)]
        for i in range(9):
            for j in range(9):
                map_fold[i][j]=0
        #create map_fold
    print_map()
   
    mine_unfound=10-mine_found#mine left
   
    valid=0
    while (valid==0):
        print("Enter the cell (",mine_unfound,"mines left)")
        step=input("")
        while (step=='help'):
            print("Enter column followed by the row (ex: a5). To add or remove a flag,")
            print("add 'f' to the cell (ex: a5f). Type 'help' to show this message again")
            print()
            print("Enter the cell (",mine_unfound,"mines left)")
            step=input("")
        if len(step)>3:
            print("invalid cell")
            continue
        if step[0]=='a':
            step_col=0
            valid=1
        elif step[0]=='b':
            step_col=1
            valid=1
        elif step[0]=='c':
            step_col=2
            valid=1
        elif step[0]=='d':
            step_col=3
            valid=1
        elif step[0]=='e':
            step_col=4
            valid=1
        elif step[0]=='f':
            step_col=5
            valid=1
        elif step[0]=='g':
            step_col=6
            valid=1
        elif step[0]=='h':
            step_col=7
            valid=1
        elif step[0]=='i':
            step_col=8
            valid=1
        else :
            print("invalid cell")
            continue
        step_row=int(step[1])-1
        if int(step[1])>9:
            print ("invalid cell")
            continue
        else:
            step_row=int(step[1])-1#input to index
            valid=1
        
        if map_fold[step_row][step_col]==1:
            if len(step)!=3:
                print("That cell is already shown")
                valid=0
                continue
            else:
                print("Cannot put a flag there")
                valid=0
                continue
        if map_fold[step_row][step_col]==2:
            if len(step)!=3:
                print("There is a flag there")
                valid=0
                continue
            
        
    while (map[step_row][step_col]!=0 and end==0):#ensure first step is safe 0
       for i in range(9):
           for j in range(9):
               map[i][j]=0
       for i in range(9):
           for j in range(9):
               map_fold[i][j]=0
       mine=[0]*10
       for i in range(10):
           mine[i]=random.randint(1,1000)%81
           x=int(mine[i]/9)
           y=mine[i]%9
           map[x][y]=9        
       count=0
       for r in range(9):
           for c in range(9):
               if map[r][c]==9:
                   continue
               if r+1 < 9:
                   if map[r+1][c]==9:
                       count += 1
               if c+1 < 9:
                   if map[r][c+1]==9:
                       count += 1
               if r-1 > -1:
                   if map[r-1][c]==9:
                       count += 1
               if c-1 > -1:
                   if map[r][c-1]==9:
                       count += 1
                       
               if r+1 < 9 and c+1 < 9 :
                   if map[r+1][c+1]==9:
                       count += 1
               if r+1 < 9 and c-1 > -1:
                   if map[r+1][c-1]==9:
                       count += 1
               if r-1 > -1 and c+1 < 9:
                   if map[r-1][c+1]==9:
                       count += 1
               if r-1 > -1 and c-1 > -1:
                   if map[r-1][c-1]==9:
                       count += 1        
               map[r][c]=count
               count=0
                 
    end+=1
    if len(step)==3:
        if map_fold[step_row][step_col]==2:
            map_fold[step_row][step_col]=0
        else: 
            map_fold[step_row][step_col]=2

    else:
        if map[step_row][step_col]==9:
            print("Game Over")
            print_map_ans()
            again=input("Play again? (y/n)")
            if again=='y':
                end=0
                continue
            elif again=='n':
                break
        
        bombs(step_row,step_col)
        map_fold[step_row][step_col]=1
    
    mine_found=0
    for i in range(9):
        for j in range(9):
            if map_fold[i][j]==2 and map[i][j]==9:
                mine_found+=1
                print(mine_found)
    if mine_found==10:
        print("You Win. ",end="")
        end_time=time.time()
        total_time=round(end_time-start_time)
        minutes=int(total_time/60)
        seconds=total_time%60
        print("It took you ",minutes,"minutes and ",seconds," seconds.")
        print_map_ans()
        again=input("Play again? (y/n)")
        if again=='y':
            end=0
            continue
        elif again=='n':
            break

    
    

   # print_map_ans()
    
#main code