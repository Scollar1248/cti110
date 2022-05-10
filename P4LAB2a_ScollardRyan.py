#
# Turtle Graphic
# 09 MAY 2022
# CTI-110 P4LAB2 - Turtle Graphic
# Ryan Scollard
#

import turtle

sides_of_shape = int(input('How many sides do you does your shape have?\n'))
#If there isn't an ability to close a shape with sides, its a line.
if sides_of_shape < 3:
    print('Thats not a shape, thats a line.')
#Looks at the number of sides and creates a triangle.
elif sides_of_shape < 4:
    for sides in range(sides_of_shape): 
        turtle.forward(100)      
        turtle.left(120) 
#Looks at the number of sides and creates a square.      
elif sides_of_shape == 4:
    for sides in range(sides_of_shape):
        turtle.forward(100)
        turtle.right(90)
#Looks at the number of sides and creates a multi-sided polygon.        
else:
    for sides in range(sides_of_shape):
         turtle.forward(50)
         turtle.right(360 / sides_of_shape)
turtle.exitonclick()
