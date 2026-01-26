#########################################################################
# Program Filename: Studio3.py
# Author: Asher Charlton 
# Date: January 22, 2026
# Description: X
# Input: X
# Output: X
##########################################################################

def calc_and_print():
    
    mpg = float(input("How many miles per gallon do you get?: "))
    cost_gas = float(input("How much does your gas cost per gallon?: "))
    gallons_needed = 100000/ mpg
    total_cost = gallons_needed * cost_gas
    print(f"Your total cost at 100,000 miles at {cost_gas:.2f} per gallon is ${total_cost:.2f} ")

calc_and_print()

