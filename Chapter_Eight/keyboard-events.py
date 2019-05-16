import turtle
star = turtle.Turtle()
def main():
    for i in range(30):
        star.forward(100)
        star.right(144)
turtle.onkeypress(main,"space")
turtle.listen()
