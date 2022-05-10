#
# Track Laps
# 10 MAY 2022
# CTI-110 P5LAP1 - Track Laps
# Ryan Scollard
#



#Function that takes user input and calulates mileage.
def laps_to_miles(user_laps):
    num_laps = user_laps
    x = 0
    if x != num_laps:
        laps_to_miles = num_laps * lap_distance
        return laps_to_miles

#Lap Distance
lap_distance = 0.25

#Takes input and converts to float in fstring.
if __name__ == '__main__':
    print(f'{laps_to_miles(user_laps = float(input())):.2f}')
