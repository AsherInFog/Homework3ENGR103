##########################################################################
# Program Filename: Lec6_3_Global_vs_Local_Vars.py
# Author: Dr. David Porter
# Date: January 22, 2026
# Description: Example of global versus local variable scope.
# Input: Varied
# Output: Varied
##########################################################################
# This is a global variable because it is defined in the main body
# of the program.
y = 400
##########################################################################
# Function: fake_func
# Description: Defines local variable "y" and its value
# Parameters: None
# Return values: y
# Pre-Conditions: None
# Post-Conditions: Returns value of y
##########################################################################
def fake_func():
# This is a local variable because it is defined
# inside a function.
# To change the value of the global y from inside the function
# you have to use the keyword "global"
    global y
    y = 300
    return y
##########################################################################
# Function: main
# Description: Main program control
# Parameters: None
# Return values: None
# Pre-Conditions: None
# Post-Conditions: Prints the values of local "y" and global "y"
##########################################################################
def main():
# Printing the value of y
    print("The value of y inside the function is", fake_func())
    print("The value of y in the global space is", y)
# Call main function to start program execution
main()