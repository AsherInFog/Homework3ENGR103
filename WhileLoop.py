##########################################################################
# Program Filename: Lec8_1_WhileLoop.py
# Author: Asher Charlton
# Date: January 25, 2026
# Description: Example of a while loop structure
# Input: None
# Output: Varied
##########################################################################
##########################################################################
# Function: main
# Description: Main program control
# Parameters: None
# Return values: None
# Pre-Conditions: N/A
# Post-Conditions: N/A
##########################################################################
def main():
# Initializing a counter variable.
# to control the while loop.
    test_var = 3
# While loop.
# Notice the difference in behavior.
# when using '>' vs. '>='.
    while test_var >= 1:
        print("test_var =", test_var)
# Must remember to update part of the loop condition
# so that it will eventually be false.
# What happens if this were +=1 instead of -=1?
    test_var -= 1
# Call main function to start program execution.
main()