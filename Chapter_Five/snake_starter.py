import curses as c
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

c.initscr()
win = c.newwin(20, 60, 0, 0)
win.keypad(1)
c.noecho()
c.curs_set(0)
win.border(0)
win.nodelay(1)

snake = [[4, 10], [4, 9], [4, 8]]
food = [10, 20]

win.addch(food[0], food[1], 'O')

c.endwin()

key = KEY_RIGHT  # default key

# ASCII value of ESC is 27
while key != 27:
    win.border(0)
    win.timeout(100)  # speed for snake
    default_key = key
    event = win.getch()
    key = key if event == -1 else event
    if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:
        key = default_key
