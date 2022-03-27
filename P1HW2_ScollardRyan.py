# Pizza Counter
# 26 MAR 2022
# CTI-110 P1HW2 - Pizza Order
# Ryan Scollard
#
import math

numStudents = int(input("How many students do you want to order pizza for?\n"))

numSlice = numStudents * 3 # Three slices of pizza per student
numPizza = numSlice / 6 # each pizza comes with six slices


print("-------Pizza Order-------")
print("Number of Students:", numStudents)
print("Pizza Slices Needed:", numSlice)
print("Pizzas Needed:", math.ceil(numPizza)) #Print number of pizza, and round up if there is a float so everyone gets pizza.
print("-------------------------")
