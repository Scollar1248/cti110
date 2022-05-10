#
# Turtle Graphic
# 09 MAY 2022
# CTI-110 P4LAB2 - Turtle Graphic - Snowflake
# Ryan Scollard
#


import random
import turtle


#Create variable to hold random interager created
snowflake_poly = random.randint(0, 66)

#Background color black
turtle.bgcolor("black")

#Sets pen size to 5
turtle.pensize(5)

#For loop over random number created
for flake in range(snowflake_poly):
    #List of colors to change for snowflake lengths
    colors = [ "red","purple","blue","green","orange","yellow"]
    turtle.pencolor(colors [flake % 6])
    #Variable to hold random number for lengths    
    ping = random.randint(50, 180)
    turtle.goto(0, flake)
    turtle.forward(ping)
    turtle.back(ping / 3)
    turtle.left(45)
    turtle.forward(25)
    turtle.back(25)
    turtle.left(-90)
    turtle.forward(25)
    turtle.back(25)
turtle.goto(0,0)


    


#Requires user to close turtle window
turtle.exitonclick()
