#
# Automobile Service Cost
# 29 APR 2022
# CTI-110 P3LAB2 - Automobile Service Cost
# Ryan Scollard
#

#Ask user for input for service.
service_request = input('Enter desired auto service:\n')

#Print to screen recieved input
print(f'You entered: {service_request}')

#Store strings in variable
oil_change = "Oil change"
tire_rotation = "Tire rotation"
car_wash = "Car wash"

#Store service price in a variable
price_oil = 35
price_rotation = 19
price_wash = 7

#Check for service requested, then print string displaying price.
if service_request == oil_change:
    print(f'Cost of oil change: ${price_oil}')
elif service_request == tire_rotation:
    print(f'Cost of tire rotation: ${price_rotation}')
elif service_request == car_wash:
    print(f'Cost of car wash: ${price_wash}')
else:
    print('Error: Requested service is not recognized')
