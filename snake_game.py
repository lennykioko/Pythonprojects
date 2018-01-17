"""sadly workds in mac only for now because windows does not suooort curses, will  sort this out soon"""
import random
import curses

s = curses.initscr() # initialize thr screen
curses.curs_set(0) # set cursor to zero so that it does not show up in screen
sh, sw = s.getmaxyx() # get height and width of screen
w = curses.newwin(sh, sw, 0, 0)  # create with the dimensions starting at top left corner
w.keypad(1) # sets window to accept keypad input
w.timeout(100)  # refresh screen every 100 seconds

# initial snake position
snk_x = sw/4
snk_y = sh/2

# initial snake body parts
snake = [
    [snk_y, snk_x], # head
    [snk_y, snk_x-1], # first segment which is one unit left of the head
    [snk_y, snk_x-2] # second segment which is two units left of the head
]

# initial food location, center of screen
food = [sh/2, sw/2]
# attach food to location specified onto the screen
w.addch(food[0], food[1], curses.ACS_PI)

# initial direction of motion of snake
key = curses.KEY_RIGHT

while True:
    next_key = w.getch() # checks what the next key is
    key = key if next_key == -1 else next_key # gives us either nothing or the next key

    # checks if player fails: if the snake hits the ends of the window or hits itself
    if snake[0][0] in [0, sh] or snake[0][1]  in [0, sw] or snake[0] in snake[1:]:
        curses.endwin() # kill window
        quit() # quit program

    new_head = [snake[0][0], snake[0][1]] # determine new head of snake
    
    # snake navigaation
    if key == curses.KEY_DOWN:
        new_head[0] += 1 # add 1 to y-axis
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1 # add 1 on x-axis

    snake.insert(0, new_head)

    # creates new food when snake eats food
    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI) # add food to window
    else:
        tail = snake.pop() # obtain snke's tail
        w.addch(tail[0], tail[1], ' ') # add a space to where tail was

    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD) # add head of dnake to screen
    