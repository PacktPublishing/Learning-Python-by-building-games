import turtle
pacman = turtle.Turtle()


def move(x, y):
    pacman.forward(180)
    print(x, y)


turtle.onscreenclick(move)
turtle.mainloop()
