#
# Estate Summary
# 14 APR 2022
# CTI-110 P2LAB2 - Estate Summary
# Ryan Scollard
#



#Takes input for current price of home and stores value in a variable.
current_price = int(input())

#Takes input for last months price of home and stores value in a variable.
last_months_price = int(input())

#Calulate monthly mortgage and store value in variable.
monthly_mortgage = ((current_price*0.051)/12)

# Display stored Variable and calcualte difference in price from current price of home and last months price. 
print(f'This house is ${current_price}. The change is ${current_price - last_months_price} since last month.')

#Display stored variable for monthly mortgage.
print(f'The estimated monthly mortgage is ${monthly_mortgage:.2f}.')


