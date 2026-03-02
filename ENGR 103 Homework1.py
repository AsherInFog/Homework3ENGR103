##########################################################################
# Program Filename: ENGR 103 Homework1.py
# Author: Asher Charlton 
# Date: January 14, 2026
# Description: Machine Calculator Thingy // Not finished yet please update description later //
# Input: // // // // 
# Output:  // // // // 
##########################################################################

import math

print("\t\t\tWelcome to Asher's Machine Calculator!")
print("Please only enter in numbers with a decimal point when prompted otherwise the program will not function as intended.\n")

while True:
    try:
        
        d1 = 0.0
        d2 = 0.0
        d3 = 0.0

        good_widgets = 0

        stand_time_part = 0.0

        number_hours_shift = 0 

        machine_relib = 0.0

        machine_effic = 0.0

        total_widgets = 0

        d1 = float(input("\nPlease enter the scrap percentage for step 1 (0 -> 1): "))
        if d1 <= 0:
            print("\nPlease enter a positive number")
            continue

        d2 = float(input("\nPlease enter the scrap percentage for step 2 (0 -> 1): "))
        if d2 <= 0:
            print("\nPlease enter a positive number")
            continue

        d3 = float(input("\nPlease enter the scrap percentage for step 3 (0 -> 1): "))
        if d3 <= 0:
            print("\nPlease enter a positive number")
            continue


        good_widgets = int(input("\nPlease enter how many good widgets are required as output for step 3 per shift: "))
        
        if good_widgets <= 0:
            print("\nPlease enter in a positive number")
            continue 

        stand_time_part = float(input("\nPlease enter the standard time per part (in hours, ex: 9.2): "))
        
        if stand_time_part <= 0: 
            print("\nPlease enter in a positive number")
            continue

        number_hours_shift = int(input("\nPlease enter the number of hours per shift:  "))

        if number_hours_shift <= 0:
            print("\nPlease enter in a positive number")
            continue

        machine_relib = float(input("\n\nPlease enter the machine reliability % (0 -> 1): "))
        if machine_relib <= 0:
            print("\nPlease enter in a positive number")
            continue

        machine_effic = float(input("\nPlease enter the machine efficiency % (0 -> 1)"))
        if machine_effic <= 0:
            print("Please enter in a positive number")
            continue

        total_widgets = good_widgets / (pow(math.prod(1),2)*(1-d1)*(1-d2)*(1-d3))

        print(f"Your total widgets are", "total_widgets:.2f")

        break
    except ValueError:
        print("Please enter in a valid input")

    


# Calculations

