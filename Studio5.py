#########################################################################
# Program Filename: Studio5.py
# Author: Asher Charlton 
# Date: Feb 9th , 2026
# Description: This is a program that generates a random number from 1 - 10, 
# then the user has to guess that number, they have 5 guesses, and te
# Input: 
# Output: 
##########################################################################

import random

def generate_answer():
    return random.randint(1, 10)

def main():
    answer = generate_answer()
    max_guesses = 5
    guess_num = 1

    while guess_num <= max_guesses:
        guess = int(input("Guess a whole nunber from 1 to 10: "))

        if guess == answer:
            print("Correct!")
            return
        else:
            print("Wrong!")
            guess_num += 1

    print("You used all 5 guesses, boohoo")
    print(f"The correct answer was {answer}")

main()