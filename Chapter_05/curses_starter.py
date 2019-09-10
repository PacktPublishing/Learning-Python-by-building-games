import curses
import time

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
screen.addstr(5, 5, "Hello")
screen.refresh()
time.sleep(3)
curses.endwin()
