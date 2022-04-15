#
# Total Purchases
# 14 APR 2022
# CTI-110 P2HW1 - Total Purchases
# Ryan Scollard
#

#Estimated Sales Tax
sales_tax = .07

#Asks user input for item price stores float in to an item variable.
item_one = float(input('Enter the price of item # 1: '))
item_two = float(input('Enter the price of item # 2: '))
item_three = float(input('Enter the price of item # 3: '))
item_four = float(input('Enter the price of item # 4: '))
item_five = float(input('Enter the price of item # 5: '))

#Subtotal caculates total price of items without taxes
subtotal = (item_one+item_two+item_three+item_four+item_five)

#Calculates total Sales Tax
total_taxes = (subtotal*sales_tax)

#Calcualtes subtotal and sales tax
total = (subtotal+total_taxes)

#Outputs results of program calculations 
print('---------Results----------')

#Outputs subotal of items with a floating point value.
print(f'Subtotal: ${subtotal:.2f}')

#Outputs total Sales Tax of items with a floating point value.
print(f'Sales Tax: ${total_taxes:.2f}')

#Outputs Total price of items to include Sales Tax with a floating point value.
print(f'Total: ${total:.2f}')
