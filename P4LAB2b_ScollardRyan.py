#
# Turtle Graphic
# 09 MAY 2022
# CTI-110 P4LAB2 - Turtle Graphic - Letters
# Ryan Scollard
#


import turtle

#Makes the letter 'R'.
turtle.color('green')
turtle.pensize(20)
turtle.forward(20)
turtle.circle(35, 180)
turtle.forward(20)
turtle.left(90)
turtle.forward(120)
turtle.backward(50)
turtle.left(45)
turtle.forward(70)

#Lifts pen as to not mark surface
turtle.left(45)
turtle.penup()
turtle.forward(75)
turtle.pendown()
#Drops pen as to leave marks on surface


#Makes the letter 'S'.
turtle.forward(30 )
turtle.circle(30, 180)
turtle.forward(20)
turtle.circle(-30, 180)
turtle.forward(35)


turtle.exitonclick()
