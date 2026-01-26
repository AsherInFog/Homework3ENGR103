##########################################################################
# Program Filename: Lec6_1_PostageCalc_Seq.py
# Author: Dr. David Porter
# Date: January 22, 2026
# Description: Calculates # of stamps per 5 sheets of paper
# Input: Number of sheets of paper to mail
# Output: Number of stamps to use as postage
##########################################################################
# Importing math module.
import math
# Request number of sheets of paper.
sheets = int(input("Enter the number of sheets of paper to mail: "))
# Calculate the number of stamps.
# Rule of thumb is one stamp per 5 sheets of paper.
stamps = sheets / 5
# Print number of stamps rounded up
# using a function from math module.
print("The number of stamps needed is", math.ceil(stamps))