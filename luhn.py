#!/usr/bin/python3

""" 
    Luhn algorithm  - count control 

    Coder/decoder + checking the validity
"""

def number_sum(string):
    # find sum to all digits without ECC number
    numbers = list(str(string))
    number_sum = 0
    lenght = len(numbers)
    for x in range(0, lenght):
        if x % 2 == 0:
            number = (int(numbers[x]) * 2)
            if int(number) > 9:
                number = number - 9
        else:
            number = (numbers[x])
        number_sum += int(number)
    return(number_sum)

def lunh_controling(string):
    if str(string).isdigit():
        # Count control string.
        number = str(string)[:-1]
        total_count = number_sum(number)
        value = int(total_count) + int(str(string)[-1])
        # Control multiplicity 10
        return(value % 10 == 0)
    else:
        return False    

def to_lunh(string):
    # Add control number.
    if str(string).isdigit():
        total_count = int(number_sum(string))
        # Find control number
        control = 0
        while control < 10:
            value = total_count + control  
            if (value % 10 == 0):
                break
            else:
                control += 1
        #Make new number
        lunh_number = str(string) + str(control)
        return(lunh_number)        
    else:
        return("Wrong date type")

def to_normal(string):
    if not(str(string).isdigit()):
        return("Wrong string")
    # Del control number.
    if lunh_controling(string):
        string = str(string)[:-1]
        return string
    else:
        return("ECC wrong")

"""
# Test

#To lunh
# To normal
print("to_lunh \n")

print(to_lunh(12345))
print(to_lunh("123"))
print(to_lunh("357"))
print("End to_lunh \n")


# To normal
print("to_normal \n")

print(to_normal(12345))
print(to_normal("1230"))
print(to_normal("357"))
print("End to_normal \n")

# Lunh_controling
print("Lunch_Controling \n")

print(lunh_controling(32))
print(lunh_controling(1230))
print(lunh_controling(234))
print("End Lunch_Controling \n")
"""
