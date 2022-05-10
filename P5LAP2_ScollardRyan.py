#
# Step Counter
#
# 10 MAY 2022
# CTI-110 P5LAP2 - Step Counter
# Ryan Scollard
#

number_user_values = int(input())
user_values = []

#Create a list to hold numbers
def get_user_values():    
    for number in range(number_user_values):
        new_number = int(input())
        user_values.append(new_number)
    upper_threshold = int(input()) 
    return user_values, upper_threshold

#Removes numbers that are higher than upper_threshold.
def ints_less_than_or_equal_to_threshold(user_values, upper_threshold):
    new_list = []
    for value in user_values:
        if value <= upper_threshold:
            new_list.append(value)    
    user_values.clear()
    user_values = new_list   
    return user_values

if __name__ == '__main__':
    user_values, upper_threshold = get_user_values()
    res_values = ints_less_than_or_equal_to_threshold(user_values, upper_threshold)
    
    for value in res_values:
        print(value)
