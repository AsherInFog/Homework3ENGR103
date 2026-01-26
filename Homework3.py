##########################################################################
# Program Filename: Homework3_Asher_Charlton.py
# Author: Asher Charlton 
# Date: January 22, 2026
# Description: Example of global versus local variable scope.
# Input: Varied
# Output: Varied
##########################################################################

def welcome_msg():
    print("{===============================================}")
    print("  Welcome to Asher's Quality Control Program!")
    print("{===============================================}")

welcome_msg()

def measure_of_int():
    interest = []
    for i in range(1, 6):
        while True:
            try:
                val = float(input(f"Please enter the value for measure {i} (decimal): "))
            except ValueError:
                print("Invalid input. Please enter a decimal number.")
                continue
            interest.append(val)
            break

    return interest

def sample_calc():
    values = measure_of_int()
    avg = sum(values) / len(values)
    print(f"Average of the {len(values)} measures: {avg:.2f}")
    return avg

sample_calc()
    
