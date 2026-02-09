##########################################################################
# Program Filename: Studio4.py
# Author: Asher Charlton 
# Date: 01-02-2026
# Description: This program will take input for the average ozone level across
# 8 hours and then output the level of safeness based on the WHO system
# Input: Average ozone level across 8 hours
# Output: The quality
##########################################################################
import sys


# Simple welcome message
def welcome_message():
    
    print("=" * 40)
    print("Welcome to Asher's Ozone Quality Program ")
    print("=" * 40)

# This function gets the input for the ozone qualtiy from the user
def ozone_input():
    while True:
        try:
            ozone_value = float(input("\nPlease enter in the average ozone level across 8 hours (0 - 500): "))
            if ozone_value < 0 or ozone_value > 500:
                print("\nPlease enter in an a value from 0 --> 500")
            else:
                return ozone_value
        except ValueError:
            print("\nPlease enter in a valid value from 0 to 500")

def rating(ozone_value):
    if ozone_value <= 50:
        return "Good"
    elif ozone_value <= 100:
        return "Moderate"
    elif ozone_value <= 150:
        return "Unhealthy for Sensitive Groups"
    elif ozone_value <= 200:
        return "Unhealthy"
    elif ozone_value <= 300:
        return "Very Unhealthy"
    else:
        return "Hazardous"


def main():

    welcome_message()
    ozone = ozone_input()
    final_rating = rating(ozone)

    print(f"\nOzone level is: {ozone} um/3")
    print(f"\nThe WHO rating is {final_rating}. ")
main()


