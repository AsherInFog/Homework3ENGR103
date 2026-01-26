##########################################################################
# Program Filename: Homework2.py
# Author: Asher Charlton
# Date: 1/20/2026
# Description: Calculates the fractional number of machines required for a 3 step 
#              widget manufacturing process
# Input: Scrap percentages as (d1, d2, d3), good widgets (good_widgets), 
#        standard time per part (stand_time_part), hours per shift (number_hours_shift),
#        machine reliability (machine_relib), and machine efficiency (machine_effic)
# Output: Fraction machines required as a decimal (to two decimal points) and 
#         rounded up to the next whole number 
##########################################################################


# Imports, using the math library to access the ceil funciton for rounding,
# then using time library so I can use the time.sleep function which adds
# a little delay between things. (Just personal preferance)

import math
import time

# A while True loop that will keep running until the desired input is given 
# The try except block allows to check for something like a value error 
    
while True:
    try:

        # Just setting up variables, not strictly neccessary 
        d1 = 0.0
        d2 = 0.0
        d3 = 0.0

        good_widgets = 0

        stand_time_part = 0.0

        number_hours_shift = 0

        machine_relib = 0.0

        machine_effic = 0.0

        total_widgets = 0.0

        # Simple welcome message with one guideline 
        print("Welcome to Asher's Machine Calculator!\n")
        print("Please only enter in numbers with a decimal point when prompted otherwise the program will not function as intended.", end = '')

        # Input: For d1 -> d3 getting the scrap percetange
        d1 = float(input("\nPlease enter the scrap percentage for step 1 (0.0 -> 1.0): "))
        if d1 < 0.0 or d1 >= 1.0:
            print("\nPlease enter in a a positive value from 0.0 to 1.0 ")
            time.sleep(.5)
            continue
        
        d2 = float(input("\nPlease enter the scrap percentage for step 2 (0.0 -> 1.0): "))
        if d2 < 0.0 or d2 >= 1.0:
            print("\nPlease enter in a a positive value from 0.0 to 1.0 ")
            time.sleep(.5)
            continue

        d3 = float(input("\nPlease enter the scrap percentage for step 3 (0.0 -> 1.0): "))
        if d3 < 0.0 or d3 >= 1.0:
            print("\nPlease enter in a a positive value from 0.0 to 1.0 ")
            time.sleep(.5)
            continue

        # Input: getting the amount of good widgets the user wishes to have at the end
        good_widgets = int(input("\nPlease enter how many good widgets are required as output for step 3 per shift: "))
        
        if good_widgets <= 0:
            print("\nPlease enter in a positive number")
            time.sleep(.5)
            continue 
        
        # Input: Getting how long it will take to process one widget
        stand_time_part = float(input("\nPlease enter the standard time per part (in hours, ex: 9.2): "))
        
        if stand_time_part <= 0: 
            print("\nPlease enter in a positive number")
            time.sleep(.5)
            continue

        # Input: Getting how long the shifts are (in hours)
        number_hours_shift = int(input("\nPlease enter the number of hours per shift (0 -> 24): "))

        if number_hours_shift <= 0 or number_hours_shift > 24:
            print("\nPlease enter in a positive whole number (0 -> 24)")
            time.sleep(.5)
            continue

        # Input: Getting the machine reliabilty
        machine_relib = float(input("\nPlease enter the machine reliability % (0 -> 1): "))
        if machine_relib <= 0.0 or machine_relib > 1.0:
            print("\nPlease enter in a a positive value from 0.0 to 1.0 ")
            time.sleep(.5)
            continue
        
        # Input: Getting the machine efficiency
        machine_effic = float(input("\nPlease enter the machine efficiency % (0.0 -> 1.0): "))
        if machine_effic <= 0.0 or machine_effic > 1.0:
            print("\nPlease enter in a a positive value from 0.0 to 1.0 ")
            time.sleep(.5)
            continue

        # Loop will break once all the input is valid
        break
    # Checks if the value type is bad 
    except ValueError:
        print("Please enter in a valid input")

# Calculation starts here
print("\nCalculating total widgets....\n")
time.sleep(1)

# Calculating total widgets needed accounting for scrap percentages
total_widgets = good_widgets / ((1 - d1)*(1 - d2)*(1 - d3))

# Calculating total machines needed 
total_machines = (stand_time_part * total_widgets) / (machine_effic * number_hours_shift * machine_relib)

# Output: Displaying the required amount of machines as a fraction and a rounded whole number 
print(f"The calculated required amount of fractional machines is {total_machines:.2f} machines.")
time.sleep(.5)
print(f"The calculated WHOLE number of machines is {math.ceil(total_machines)} machines.")
time.sleep(.5)
print(f"The calculated WHOLE number of machines is {math.ceil(total_machines):.1f} machines.")
time.sleep(1)

# End message 
print("\n\nThank you for using my program!")