# This code will convert any given string from bases 2 through 36 to its decimal equivalent.
# It begins by asking for the string that will be converted. The string gets assigned to
# variable 'conversion_number'. The user then states the base that the given string is currently
# based on.
# 
# As part of the conversion process, each character will be multiplied by its base
# raised to an exponent corresponding to the character's reverse index position. Due to this,
# the conversion_number string must be reversed. This reversed string is used for the
# remainder of the algorithm to ensure that the calculations are being done in the proper order. These
# characters will reference the "values" variable so that any characters within bases 2-36 will be
# compatible with the calculator.
# 
# The algorithm begins with dec_numb which will become our final, converted number.
# It begins at 0 and will end at our final solution. The power begins at 1 and also increases
# by multipling with the base to correspond with the base to decimal conversion formula.
# 
# The for x in conversion_number2 loop will continue until each character in the inputted
# string is checked. Once the final character runs through, the final dec_numb value is the
# converted string now in decimal form.

conversion_number = input("Please enter the string to be converted to decimal: ")
base = int(input("What base from 2-36 was your string? "))

conversion_number2 = conversion_number[::-1]

dec_numb = 0
values = "0123456789abcdefghijklmnopqrstuvwxyz"
power = 1

for x in conversion_number2:
    dec_numb = dec_numb + (values.index(x) * power)
    power = power * base
    print(dec_numb)