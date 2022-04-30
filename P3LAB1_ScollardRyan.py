#
# Remove gray from RBG
# 29 APR 2022
# CTI-110 P3LAB1 - Remove gray from RBG
# Ryan Scollard
#

#Ask use for color input
color_red  = int(input())
color_green = int(input())
color_blue = int(input())

# Prepare variable to store lowest value of input color
lowest_color_vaule = 0

# Check color value to idenity lowest color value, store lowest color value in variable.
if (color_red < color_green) and (color_red < color_blue):
    lowest_color_vaule = color_red
elif (color_green < color_red) and ( color_green < color_blue):
    lowest_color_vaule = color_green
else:
    lowest_color_vaule = color_blue

# Subtract lowest color value from all RGB number.
grayless_red = (color_red - lowest_color_vaule)
grayless_green = (color_green - lowest_color_vaule)
grayless_blue = (color_blue - lowest_color_vaule)

# Neatly output grayless RGB values using a f-string.
print(f'{grayless_red} {grayless_green} {grayless_blue}')
