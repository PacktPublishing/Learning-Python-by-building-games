import turtle 

hexagon = turtle.Turtle()

num_of_sides = 6
length_of_sides = 70
angle = 360.0 / num_of_sides 

for i in range(num_of_sides):
    hexagon.forward(length_of_sides)
    hexagon.right(angle)
    
turtle.done()
