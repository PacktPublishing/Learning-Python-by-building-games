import turtle
Pen = turtle.Turtle()

Pen.speed(0)
Pen.color(0, 0, 0)


def box(Dimension):  # box method creates a rectangular box
    Pen.begin_fill()
    # 0 deg.
    Pen.forward(Dimension)
    Pen.left(90)
    # 90 deg.
    Pen.forward(Dimension)
    Pen.left(90)
    # 180 deg.
    Pen.forward(Dimension)
    Pen.left(90)
    # 270 deg.
    Pen.forward(Dimension)
    Pen.end_fill()
    Pen.setheading(0)


Pen.penup()
Pen.forward(-100)
Pen.setheading(90)
Pen.forward(100)
Pen.setheading(0)
boxSize = 10

grid_of_pixels = [[1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1]]
grid_of_pixels.append([1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1])
grid_of_pixels.append([1, 1, 1, 0, 0, 0, 3, 3, 3, 3, 3, 0, 3, 1, 1, 1])
grid_of_pixels.append([1, 1, 0, 3, 0, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 1])
grid_of_pixels.append([1, 1, 0, 3, 0, 0, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3])
grid_of_pixels.append([1, 1, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 1])
grid_of_pixels.append([1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1])
grid_of_pixels.append([1, 1, 1, 0, 0, 2, 0, 0, 0, 0, 2, 0, 1, 1, 1, 1])
grid_of_pixels.append([1, 1, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 1, 1])
grid_of_pixels.append([0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0])
grid_of_pixels.append([3, 3, 3, 0, 2, 3, 2, 2, 2, 2, 3, 2, 0, 3, 3, 3])
grid_of_pixels.append([3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3])
grid_of_pixels.append([3, 3, 3, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 3, 3, 3])
grid_of_pixels.append([1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1])
grid_of_pixels.append([1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1])
grid_of_pixels.append([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0])

palette = ["#4B610B", "#FAFAFA", "#DF0101", "#FE9A2E"]

for i in range(0, len(grid_of_pixels)):
    for j in range(0, len(grid_of_pixels[i])):
        Pen.color(palette[grid_of_pixels[i][j]])
        box(boxSize)
        Pen.penup()
        Pen.forward(boxSize)
        Pen.pendown()
    Pen.setheading(270)
    Pen.penup()
    Pen.forward(boxSize)
    Pen.setheading(180)
    Pen.forward(boxSize * len(grid_of_pixels[i]))
    Pen.setheading(0)
    Pen.pendown()
