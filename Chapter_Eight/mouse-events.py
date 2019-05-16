import turtle
pacman = turtle.Turtle()
def move(x,y):
    pacman.forward(50)
    print(x,y)

turtle.onclick(move)
