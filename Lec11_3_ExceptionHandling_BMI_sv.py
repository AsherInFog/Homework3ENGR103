##########################################################################
# Program Filename: Lec11_3_ExceptionHandling_BMI.py
# Author: Asher Charlton 
# Date: February 12, 2026
# Description: More examples of exception handling
# Input: Varied
# Output: Varied
##########################################################################

##########################################################################
# Function: get_weight
# Description: Asks the user to enter their weight (in pounds)
# Parameters: None
# Return values: weight
# Pre-Conditions: N/A
# Post-Conditions: Prints different messages to user
##########################################################################
def get_weight():
    while True:
        try:
            weight = float(input("Please enter your weight in pounds: "))
            if weight <= 0:
                print("Weight must be a positive value")
                continue
            return weight
        except ValueError:
            print("Invalid input, please enter a NUMERIC value for weight")

##########################################################################
# Function: get_height
# Description: Asks the user to enter their height (in inches)
# Parameters: None
# Return values: height
# Pre-Conditions: N/A
# Post-Conditions: Prints different messages to user
##########################################################################
def get_height():
    while True:
        try:
            height = float(input("Please enter your height in inches: "))
            if height <= 0:
                print("Height must be a positive value")
                continue
            return height
        except ValueError:
            print("Invalid input, please enter a NUMERIC value for height")

##########################################################################
# Function: main
# Description: Main program control
# Parameters: None
# Return values: None
# Pre-Conditions: N/A
# Post-Conditions: Prints different messages to user
##########################################################################
def main():
    
    weight = get_weight()
    height = get_height()

    try:
        bmi = (weight / (height ** 2)) * 703
        
        print(f"\nResults:")
        print(f"Weight: {weight} lbs")
        print(f"Height: {height} inches")
        print(f"Your calculated BMI is: {bmi:.2f}")
        
    except ZeroDivisionError:
        print("Error, height cannot be zero")

main()