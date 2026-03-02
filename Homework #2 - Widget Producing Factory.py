##########################################################################
# Program Filename: Homework #2 - Widget Producing Factory
# Author: Asher Charlton
# Date: 1/12/2026
# Description:
# Input:
# Output:
##########################################################################


# Imports

import math

# Variables:

# These variables are for what % are going to break during each step

while True:
    try:

        d1 = 0.0
        d2 = 0.0
        d3 = 0.0

        O_three = 0

        stand_time_part = 0.0

        number_hours_shift = 0

        machine_relib = 0.0

        machine_effic = 0.0

        print("Welcome to Asher's Machine Calculator!\n")
        print("Please only enter in numbers with a decimal point when prompted otherwise the program will not function as intended.", end = '')

        d1 = float(input("\nPlease enter the scrap percentage for step 1 (0 -> 1): "))
        d2 = float(input("\nPlease enter the scrap percentage for step 2 (0 -> 1): "))
        d3 = float(input("\nPlease enter the scrap percentage for step 3 (0 -> 1): "))

        if d1 or d2 or d3 <= 0:
            print("\nPlease enter in a valid number")
            continue

        O_three = int(input("\nPlease enter how many good widgets are required as output for step 3 per shift: "))
        
        if O_three <= 0:
            print("\nPlease enter in a positive number")
            continue 

        stand_time_part = float(input("\nPlease enter the standard time per part (in hours, ex: 9.2): "))
        
        if stand_time_part <= 0: 
            print("\nPlease enter in a positive number")
            continue

        number_hours_shift = int(input("\nPlease enter the number of hours per shift:  "))

        if number_hours_shift <= 0:
            print("\nPlease enter in a positive number")

        machine_relib = float(input("\n\nPlease enter the machine reliability % (0 -> 1): "))
        machine_effic = float(input("\nPlease enter the machine efficiency % (0 -> 1)"))

        break
    except ValueError:
        print("Please enter in valid input")

    


# Calculations

