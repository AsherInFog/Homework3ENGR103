##########################################################################
# Program Filename: Lec7_2_ErrorHandling.py
# Author: Asher Charlton 
# Date: January 25, 2026
# Description: Example of error handling
# Input: Varied
# Output: Varied
##########################################################################
# Import sys module.
import sys
##########################################################################
# Function: check_input
# Description:
# Parameters: None
# Return values: None
# Pre-Conditions: N/A
# Post-Conditions: Prints different messages to user
##########################################################################
def check_input():
# Try...except block to catch incorrect user input
    try:
# Ask user for input.
        inp_num = float(input("Input a number: "))
# If the user input is valid, this statement is executed.
        print(f"You entered {inp_num}. Good input!")
    except:
# If the user input is invalid, this statement is executed.
        print("Input Error! Please restart the program and try again.")
#Exit the program
sys.exit()
##########################################################################
# Function: main
# Description: Main program control
# Parameters: None
# Return values: None
# Pre-Conditions: N/A
# Post-Conditions: N/A
##########################################################################
def main():
    check_input()
# Call main function to start program execution.
main()
