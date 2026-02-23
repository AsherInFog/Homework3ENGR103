#########################################################################
# Program Filename: Homework4.py
# Author: Asher Charlton 
# Date: Feb 9th , 2026
# Description: This program calculates and displays a learning curve
#              based on user inputs. It iterates through cycles using
#              the formula y = k * x^n until the cycle time reaches
#              the goal time, then reports the learning percent.
# Input: Goal cycle time (minutes), first cycle time (minutes), slope (negative number)
# Output: Cycle number and time for each cycle, success message, and the learning percent
##########################################################################
import time

##########################################################################
# Function: welcome
# Description: prints a simple welcome message to the user
# Parameters: None
# Return values: None
# Pre-Conditions: N/A
# Post-Conditions: Prints messages to user
##########################################################################
def welcome():
    print("\n=============================================")
    print(" Welcome to Asher's Learning Curve Calculator")
    print("=============================================")
    time.sleep(.5)


##########################################################################
# Function: goal_cycle_input
# Description: Gets input from the user for the goal cycle time
# Parameters: None
# Return values: goal_cycle
# Pre-Conditions: N/A
# Post-Conditions: returns the input of goal_cycle
##########################################################################
def goal_cycle_input():
    while True:
        try:
            goal_cycle = float(input("\nPlease enter the GOAL cycle time in minutes: "))
            if goal_cycle <= 0:
                print("\nERROR, please enter in a value greater than 0")
                time.sleep(.5)
                continue
        
        except ValueError:
            print("\nERROR, please enter in a NUMBER greater than 0")
            time.sleep(.5)
            continue
        break
    return goal_cycle


##########################################################################
# Function: first_cycle_input
# Description: gets the input for the first cycle time
# Parameters: goal cycle
# Return values: first cycle
# Pre-Conditions: that there was an input for goal cycle
# Post-Conditions: returns the input first cycle (thats bigger than the goal cycle)
##########################################################################
def first_cycle_input(goal_cycle):
    while True:
        try:
            first_cycle = float(input("\nPlease enter in the FIRST cycle time in minutes (should be greater than the goal cycle time): "))
            if first_cycle <= 0:
                print("\nERROR, please enter in a value greater than 0")
                time.sleep(.5)
                continue
            if first_cycle <= goal_cycle:
                print("\nERROR, the input for the first cycle must be greater than the goal cycle, try again")
                exit()
        except ValueError:
            print("\nERROR, please enter in a NUMBER greater than 0")
            time.sleep(.5)
            continue
        break
    return first_cycle


##########################################################################
# Function: slope_input
# Description: gets the input for the slope
# Parameters: None
# Return values: slope input
# Pre-Conditions: N/A
# Post-Conditions: returns the input for the slope 
##########################################################################
def slope_input():
    while True:
        try:
            slope = float(input("\nPlease enter in the slope as a number less than 0: "))
            if slope >= 0:
                print("\nERROR, please enter in value LESS than 0")
                time.sleep(.5)
                continue

        except ValueError:
            print("\nERROR, please enter in a NUMBER less than 0")
            time.sleep(.5)
            continue
        break
    return slope


##########################################################################
# Function: calc_cycle_time
# Description: calculates the cycle 
# Parameters: first_cycle, number_cycle, slope
# Return values: returns the calculation 
# Pre-Conditions: needs to use the input for the first_cycle, the number_cycle, and the slope
# Post-Conditions: returns the calculated cycle 
##########################################################################
def calc_cycle_time(first_cycle, number_cycle, slope):
    return first_cycle * (number_cycle ** slope)


##########################################################################
# Function: number_cycle
# Description: This is where the cycle is printed out along with the calculation,
#              asks the user if they want to cotinue if the cycle hits 100, and once the cycle
#              is less than or equals the goal cycle it will stop and print out the learning curve
#              as a percentage
# Parameters: first_cycle, slope, goal_cycle
# Return values: None
# Pre-Conditions: needs the first_cycle, slope, and goal_cycle, to do the calculations 
# inside the function
# Post-Conditions: N/A
##########################################################################
def number_cycle(first_cycle, slope, goal_cycle):
    cycle = 1
    while True:
        cycle_time = calc_cycle_time(first_cycle, cycle, slope)
        print(f"Cycle: {cycle}\t{cycle_time:.3f}")

        if cycle_time <= goal_cycle:
            print("\nThe desired cycle time has been achieved")
            time.sleep(1)
            print("\nThank you for using my program!")
            learning_percent = (2 ** slope) * 100
            print(f"The learning percent is {learning_percent:.1f}%")
            break

        if cycle % 100 == 0:
            choice = input("\n100 cycles or more have been reached, would you like to continue? (n = no, y = yes): ")
            if choice.lower() == 'n':
                print("\nYou have chosen to quit")
                time.sleep(1)
                print("\nThank you for using my program!")
                break
            elif choice.lower() == 'y':
                print("\nContinuing...")
                time.sleep(1)

        cycle += 1


##########################################################################
# Function: main
# Description: Main program control
# Parameters: None
# Return values: None
# Pre-Conditions: N/A
# Post-Conditions: Prints different messages to user
##########################################################################
def main():
    welcome()
    goal_cycle = goal_cycle_input()
    first_cycle = first_cycle_input(goal_cycle)
    slope = slope_input()
    number_cycle(first_cycle, slope, goal_cycle)

main()