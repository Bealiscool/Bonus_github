import curses
import random

# Constants
NORMAL_FOOD = 'π'
SPECIAL_FOOD = 'X'
SNAKE_BODY = 'O'
OBSTACLE = '#'

def main(stdscr):
    # Initialization
    try:
        curses.curs_set(0)
    except curses.error:
        pass  # Handle the error if curs_set fails

    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)
    w.timeout(100)

    # Snake initial position and body
    snake_x = sw // 4
    snake_y = sh // 2
    snake = [
        [snake_y, snake_x],
        [snake_y, snake_x - 1],
        [snake_y, snake_x - 2]
    ]

    # Initial food positions
    normal_food = [sh // 2, sw // 2]
    special_food = [sh // 4, sw // 4]

    # Place food on the screen
    w.addch(normal_food[0], normal_food[1], NORMAL_FOOD)
    w.addch(special_food[0], special_food[1], SPECIAL_FOOD)

    # Obstacles
    obstacles = []
    obstacle_cells = (sh * sw) // 20
    while len(obstacles) < obstacle_cells:
        start_x = random.randint(0, sw - 1)
        start_y = random.randint(0, sh - 1)
        if random.choice([True, False]):
            for i in range(5):
                if start_x + i < sw:
                    obstacles.append([start_y, start_x + i])
        else:
            for i in range(5):
                if start_y + i < sh:
                    obstacles.append([start_y + i, start_x])
    for y, x in obstacles:
        w.addch(y, x, OBSTACLE, curses.A_REVERSE)

    # Initial settings
    key = curses.KEY_RIGHT
    score_normal = 0
    score_special = 0
    paused = False

    def place_food():
        food = [random.randint(1, sh - 2), random.randint(1, sw - 2)]
        while food in snake or food in obstacles:
            food = [random.randint(1, sh - 2), random.randint(1, sw - 2)]
        return food

    while True:
        next_key = w.getch()
        if next_key == ord(' '):  # Pause/resume
            paused = not paused
        if paused:
            continue
        if next_key != -1:
            key = next_key

        # Calculate next coordinates
        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1

        # Wrap around screen boundaries
        new_head[0] = new_head[0] % sh
        new_head[1] = new_head[1] % sw

        # Check for collision with obstacles
        if new_head in obstacles:
            break

        # Check for collision with self
        if new_head in snake:
            break

        # Insert new head
        snake.insert(0, new_head)

        # Check for food consumption
        if snake[0] == normal_food:
            score_normal += 1
            normal_food = place_food()
            w.addch(normal_food[0], normal_food[1], NORMAL_FOOD)
        elif snake[0] == special_food:
            score_special += 1
            special_food = place_food()
            w.addch(special_food[0], special_food[1], SPECIAL_FOOD)
            if len(snake) > 1:
                snake.pop()
        else:
            snake.pop()

        # Refresh screen
        w.clear()
        for y, x in snake:
            w.addch(y, x, SNAKE_BODY)
        for y, x in obstacles:
            w.addch(y, x, OBSTACLE, curses.A_REVERSE)
        w.addch(normal_food[0], normal_food[1], NORMAL_FOOD)
        w.addch(special_food[0], special_food[1], SPECIAL_FOOD)

    # Game over screen
    w.clear()
    w.addstr(sh // 2, sw // 2 - len("Game Over!") // 2, "Game Over!")
    w.addstr(sh // 2 + 1, sw // 2 - len(f"Normal foods eaten: {score_normal}, Special foods eaten: {score_special}") // 2, f"Normal foods eaten: {score_normal}, Special foods eaten: {score_special}")
    w.refresh()
    w.getch()

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except Exception as e:
        print(f"An error occurred: {e}")
