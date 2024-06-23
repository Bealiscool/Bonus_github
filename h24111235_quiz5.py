
n = int(input("Enter the size of the grid: "))

grid = []
i = 0
while i < n*n:
    grid.append("_")
    i += 1
    
grid_str = ""
i = 0
while i < n*n:
    row = grid[i:i+n]
    grid_str += " ".join(row) + "\n"
    i += n

print(grid_str)



done = False
while not done:
    e = input("Enter the cell coordinates to edit: ")
    if e == "done":
        done = True
    else:
        v = input("Enter the new value for the cell: ")
        ne = e.split(",")
        nne = []
        for i in range(len(ne)):
            nne.append(int(ne[i]))
        grid[(nne[1]-1)+(nne[0]-1)*n] = v
        
        grid_str = ""
        i = 0
        while i < n*n:
            row = grid[i:i+n]
            grid_str += " ".join(row) + "\n"
            i += n
    
        print(grid_str)
    
    