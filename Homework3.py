##########################################################################
# Program Filename: Homework3_Asher_Charlton.py
# Author: Asher Charlton 
# Date: January 22, 2026
# Description: Example of global versus local variable scope.
# Input: Varied
# Output: Varied
##########################################################################
import math

def welcome_msg():
    print("{===============================================}")
    print("  Welcome to Asher's Quality Control Program!")
    print("{===============================================}")

def moi_sample():
    interest = []
    for i in range(1, 6):
        while True:
            try:
                val = float(input(f"Please enter the value for measure {i}: "))
            except ValueError:
                print("\nInvalid input. Please enter a NUMBER.")
                continue
            interest.append(val)
            break

    return interest


# Function that calculates the average sample
def avg_sample_calc(values):
    avg = sum(values) / len(values)
    return avg


def moi_goal_average():
    while True:
        try:
            moi = float(input("Please input the measure of interest's goal average: "))
            if moi <= 0:
                print("\nPlease enter in a nunber greater than 0")
                continue
        except ValueError:
            print("\nInvalid Input. Please enter a NUMBER")
            continue
        break
    return moi
    

def goal_standard_deviation():
    while True:
        try:
            gsd = float(input("Please enter the goal standard deviation: "))
            if gsd < 0:
                print("\nPlease enter in a posive number")
                continue
        except ValueError:
            print("\nInvalid input. Please enter a NUMBER")
            continue
        break
    return gsd
            

def lowerbound_calc(moi, gsd, n):
    lower = moi - ((3 * gsd)/math.sqrt(n))
    return lower

def upperbound_calc(moi, gsd, n):
    upper = moi + ((3 * gsd)/math.sqrt(n))
    return upper


def main():
    welcome_msg()
   
    interest = moi_sample()
    avg = avg_sample_calc(interest)
    moi = moi_goal_average()
    gsd = goal_standard_deviation()

    n = len(interest)
    lower = lowerbound_calc(moi, gsd, n)
    upper = upperbound_calc(moi, gsd, n)

    print(f"\n\nYour lower bound is {lower:.2f}")
    print(f"Your average is {avg:.2f}")
    print(f"Your upper bound is {upper:.2f}")
    print("\n\nThank you for using my program!")

main()


