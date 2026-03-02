##########################################################################
# Program Filename: studio2.py
# Author: Asher Charlton 
# Date: January 12, 2026
# Description: Working with mathematical expressions
# Input: Varied
# Output:  Varied
##########################################################################

# Math Expression Program 

#problem_1 = 20 / 2 + 4 + 5.5 + 3 * 4
#problem_2 = 20 / (2 + 4 + 5.5) + 2 / 4
#problem_3 = 20 / 2 + 4 + 5.5 + 2/4
#problem_4 = 25 % 5 * 6 + 12 % 36
#problem_5 = 25 % 5 * (6 + 12) % 36
#problem_6 = 2 * (45.0 + 10) / 3
#problem_7 = 2 * 45.0 + 10.0 // 12
#problem_8 = 2 * 45.0 + 10 // 12
#problem_9 = 2 ** 8 / (6 +12) * 2

#print(f"{problem_1:.3f}")
#print(f"{problem_2:.3f}")
#print(f"{problem_3:.3f}")
#print(f"{problem_4:.3f}")
#print(f"{problem_5:.3f}")
#print(f"{problem_6:.3f}")
#print(f"{problem_7:.3f}")
#print(f"{problem_8:.3f}")
#print(f"{problem_9:.3f}")

# Miles Per Gallon Program

print("Hello, welcome to Asher's Studio 2, Miles Per Gallon Progam\n")


while True:
    try:
        MILES = 100000
        mpg = int(input("Please enter your miles per gallon (positive integer): "))
        if mpg <= 0:
            print("\nPlease enter a value greater than 0\n")
            continue

        lifetime_milage = MILES / mpg
        print(f"The amount of gallons you used (100,000 miles) is {lifetime_milage:.2f}")

        four_fifty = lifetime_milage * 4.50
        two_fifty = lifetime_milage * 2.50

        print(f"\nThe cost for 100,000 miles when gas is 4.50 a gallon is {four_fifty:.2f}")
        print(f"The cost for 100,000 miles when gas is 2.50 a gallon is {two_fifty:.2f}\n")
        break

    except ValueError:
        print("\nPlease enter a valid integer\n")

        
    