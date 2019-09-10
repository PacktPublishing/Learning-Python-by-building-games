import curses as c

screen = c.initscr()

win = c.newwin(20, 60, 0, 0)

c.noecho()
c.cbreak()
screen.keypad(True)
while True:
    char = screen.getch()
    if char == ord('q'):
        break
    if char == ord('p'):
        win.addstr(5, 10, "Hello world")
        win.refresh()

# time.sleep(10)
screen.endwin()
