##########################################################################
# Program Filename: Lec6_2_PostageCalc_Funcs.py
# Author: Dr. David Porter
# Date: January 22, 2026
# Description: Calculates # of stamps per 5 sheets of paper w/ functions.
# Input: Number of sheets of paper to mail
# Output: Number of stamps to use as postage
##########################################################################
# Import math module.
import math
##########################################################################
# Function: request_sheets
# Description: Asks user for number of sheets to mail
# Parameters: None
# Return values: sheets
# Pre-Conditions: sheets must be a number
# Post-Conditions: Returns number of sheets
##########################################################################
def request_sheets():
# Request number of sheets of paper.
sheets = int(input("Enter the number of sheets of paper to mail: "))
# Use keyword return to return a value from your function.
return sheets
##########################################################################
# Function: calc_stamps
# Description: Calculates number of stamps based on number of sheets
# Parameters: no_sheets
# Return values: stamps
# Pre-Conditions: no_sheets must be a number
# Post-Conditions: Returns number of stamps
##########################################################################
def calc_stamps(no_sheets):
stamps = no_sheets / 5
return stamps
##########################################################################
# Function: main
# Description: Main program control
# Parameters: None
# Return values: None
# Pre-Conditions: N/A
# Post-Conditions: Prints number of stamps rounded up
##########################################################################
def main():
# In your main code you can call your function by name.
# To take the value and use it, you set a variable equal
# to your function name.
no_sheets = request_sheets()
no_stamps = calc_stamps(no_sheets)
# # Or you can nest the function calls.
# # Use PythonTutor to see how the transfer of program
# # control works with this format.
# no_stamps = calc_stamps(request_sheets())
# Print the number of stamps.
print("The number of stamps needed is", math.ceil(no_stamps))
# Call main function to start program execution
main()
