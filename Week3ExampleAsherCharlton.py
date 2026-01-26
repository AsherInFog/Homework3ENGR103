##########################################################################
# Program Filename: Lec5_2_InClassActivities_sv.py
# Author: Asher Charlton 
# Date: January 21, 2026
# Description: Activites to practice writing functions.
# Input: Varied
# Output: Varied
##########################################################################
# Import the math module.
import math
##########################################################################
# Function: print_pi
# Description: Prints the value of pi
# Parameters: None
# Return values: None
# Pre-Conditions: The math module must be imported
# Post-Conditions: Prints value of pi
##########################################################################

def print_pi():
    pi = print(math.pi)

##########################################################################
# Function: return_pi
# Description: Returns the value of pi
# Parameters: None
# Return values: func_pi
# Pre-Conditions: The math module must be imported
# Post-Conditions: Returns value of pi
##########################################################################

def return_pi():
    func_pi = math.pi
    return func_pi

##########################################################################
# Function: return_pi2
# Description: Returns the value of pi w/o defining the local variable func_pi
# Parameters: None
# Return values: math.pi
# Pre-Conditions: The math module must be imported
# Post-Conditions: Returns value of pi
##########################################################################

def return_pi2():
    return math.pi

##########################################################################
# Function: main
# Description: Main program control
# Parameters: None
# Return values: None
# Pre-Conditions: Value of radius provided by user must be a number
# Post-Conditions: Prints value of circumference rounded to two digits
##########################################################################
# Call main function to start program execution

def main():
    radius = float(input("\nPlease enter the raidus of a circle as a whole numeber: "))
    circumference = 2 * return_pi2() * radius
    print(f"\nThe circumference is: {math.ceil(circumference):.2f}")

main()