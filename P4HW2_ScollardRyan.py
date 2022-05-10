# Pizza Order 
# 09 May 2022
# CTI-110 P4HW2 - Pizza Order
# Ryan Scollard
#

from difflib import restore
import math
while True:
    #Ask user for number of students
    numStudents = int(input("\nHow many students do you want to order pizza for? "))
    #Ask user if they are going to share
    number_share = float(input('Enter the number of people per pizza (1.5, 2 or 3): '))

    #List of approved people per pizza
    numshareList = [1.5, 2, 3]

    #Checks to see if number of people sharing the pizza is in the approved list. If not pop error else pass.
    if number_share not in numshareList:
        print('\nINVALID ENTRY !!!!!')
        print('Should have entered 1.5, 2 or 3')
        print()
        number_share = float(input('Enter the number of people per pizza (1.5, 2 or 3) again: '))
        
    else:
        pass


    #Figures out number of pizzas required by taking number of students divided by people sharing each pizza
    numPizza = numStudents / number_share

    #Always got to pay the man
    sales_tax = .06

    #Price of pizza
    pizza_price = 5

    #Subtotal prices, total taxes, and total price
    subtotal = (numPizza * pizza_price)
    total_taxes = (subtotal*sales_tax)
    total_price = (subtotal + total_taxes)


    #Prints order
    print("\n-------Pizza Order-------")
    print("Number of Students:", numStudents)
    print("Pizzas Needed:", math.ceil(numPizza)) #Print number of pizza, and round up if there is a float so everyone gets pizza.
    print(f'Price: ${total_price:.2f}')#Fstring to make money look pretty
    print("-------------------------")
    
# Entire program is wrapped in a while true statement,  to exit the program respond to re-run program
    while True:
        restart = input('\nWould you like to run program again (y for yes) : ')
        if restart == 'y':
            break
        else:
            exit()
