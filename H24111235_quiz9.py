import random

def generate_path(maze, N, M):
    current = (0, 0)
    maze[current] = 2
    path = [current]
    while current != (N - 1, M - 1):
        x, y = current
        if x == N - 1:
            current = (x, y + 1)
        elif y == M - 1:
            current = (x + 1, y)
        else:
            if random.choice([True, False]):
                current = (x, y + 1)
            else:
                current = (x + 1, y)
        if maze[current] != 1:  # Ensure no obstacle is on the path
            maze[current] = 2
            path.append(current)
    return maze, path

def add_obstacles(maze, min_obstacles, N, M):
    count = 0
    empty_cells = [(i, j) for i in range(N) for j in range(M) if maze[(i, j)] == 0]
    while count < min_obstacles and empty_cells:
        cell = random.choice(empty_cells)
        maze[cell] = 1
        empty_cells.remove(cell)
        count += 1

def set_obstacle(maze, N, M):
    try:
        x, y = map(int, input("Enter the coordinates to set an obstacle (row, col): ").split())
        if (x, y) not in maze or not (0 <= x < N and 0 <= y < M):
            raise KeyError
        if maze[(x, y)] == 2:
            print("Error: Cannot place an obstacle on the path.")
        else:
            maze[(x, y)] = 1
    except (ValueError, KeyError):
        print("Invalid coordinates or out of bounds.")

def remove_obstacle(maze, N, M):
    try:
        x, y = map(int, input("Enter the coordinates to remove an obstacle (row, col): ").split())
        if (x, y) not in maze or not (0 <= x < N and 0 <= y < M):
            raise KeyError
        if maze[(x, y)] == 2:
            print("Error: Cannot remove the path.")
        else:
            maze[(x, y)] = 0
    except (ValueError, KeyError):
        print("Invalid coordinates or out of bounds.")

def print_maze(maze, N, M):
    for i in range(N):
        for j in range(M):
            if maze[(i, j)] == 0:
                print('   ', end='')
            elif maze[(i, j)] == 1:
                print(' X ', end='')
            elif maze[(i, j)] == 2:
                print(' O ', end='')
        print()

def main():
    while True:
        try:
            filename = input("Enter the maze file name: ")
            with open(filename, 'r') as file:
                lines = file.readlines()
                N = int(lines[0].strip())
                M = int(lines[1].strip())
                maze = {}
                for i in range(N):
                    for j in range(M):
                        maze[(i, j)] = int(lines[i + 2][j])
            break
        except IOError:
            print("File not found. Please enter a valid file name.")
        except (ValueError, IndexError):
            print("Invalid file format. Please ensure the file contains the correct format.")

    maze, path = generate_path(maze, N, M)
    
    while True:
        try:
            min_obstacles = int(input("Enter the minimum number of obstacles to add: "))
            if min_obstacles < 0 or min_obstacles >= N * M - len(path):
                raise ValueError
            break
        except ValueError:
            print("Invalid number of obstacles. Please enter a valid number.")

    add_obstacles(maze, min_obstacles, N, M)
    print_maze(maze, N, M)
    
    while True:
        print("\nMenu:")
        print("1. Set an obstacle")
        print("2. Remove an obstacle")
        print("3. Print the maze")
        print("4. Exit")
        
        try:
            option = int(input("Choose an option: "))
            if option == 1:
                set_obstacle(maze, N, M)
                print_maze(maze, N, M)
            elif option == 2:
                remove_obstacle(maze, N, M)
                print_maze(maze, N, M)
            elif option == 3:
                print_maze(maze, N, M)
            elif option == 4:
                break
            else:
                print("Invalid option. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
