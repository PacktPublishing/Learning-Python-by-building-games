import turtle
star = turtle.Turtle()

exit = False
def main():
    if not exit:
            star.forward(50)
            star.right(144)
    turtle.ontimer(main,500)
main()

