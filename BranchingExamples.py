##########################################################################
# Program Filename: Lec7_1_BranchingExamples.py
# Author: Asher Charlton 
# Date: January 25, 2026
# Description: Example of single, double, and multiple selection
# Input: Varied
# Output: Varied
##########################################################################
##########################################################################
# Function: branch_exs
# Description: Different branching examples
# Parameters: None
# Return values: None
# Pre-Conditions: N/A
# Post-Conditions: Prints different messages based on user input
##########################################################################
def branch_exs():
# Single selection example.
    inp_num1 = float(input("Input the number 1: "))
# Print if the user follows instructions.
# Continue program execution otherwise.
    if inp_num1 == 1:
        print("Way to go!")
# Double selection example.
inp_num2 = float(input("Input a number larger than 10: "))
# Print if the user follows instructions.
if inp_num2 > 10:
    print("Way to go!")
# Print if the user does not.
else:
    print("Follow directions!")
# Multiple selection example.
print("Think of a number. ", end="")
inp_size = input("Is your number \"small\", \"medium\", or \"large\"? ")
# Echo user input if it matches one of the if statements.
if inp_size == "small":
    print("You said \"small\".")
elif inp_size == "medium":
    print("You said \"medium\".")
elif inp_size == "large":
    print("You said \"large\".")
# Print this otherwise.
else:
    print("Follow Directions!")
##########################################################################
# Function: main
# Description: Main program control
# Parameters: None
# Return values: None
# Pre-Conditions: N/A
# Post-Conditions: N/A
##########################################################################
def main():
    branch_exs()
# Call main function to start program execution.
main()