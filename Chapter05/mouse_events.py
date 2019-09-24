import curses as c
import time


def main(screen):
    c.curs_set(0)
    c.mousemask(1)

    inp = screen.getch()
    if inp == c.KEY_MOUSE:
        screen.addstr(17, 40, "Mouse is clicked")
        screen.refresh()

    screen.getch()
    time.sleep(10)


c.wrapper(main)
