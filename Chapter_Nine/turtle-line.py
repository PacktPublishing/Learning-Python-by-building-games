def line(a, b, x, y):
    "Draw line from `(a, b)` to `(x, y)`."
    import turtle
    turtle.up()
    turtle.goto(a, b)
    turtle.down()
    turtle.goto(x, y)
