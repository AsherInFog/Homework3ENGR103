#########################################################################
# Program Filename: Studio6.py
# Author: Asher Charlton 
# Date: Feb 16th , 2026
# Description:
# Output:
##########################################################################

def welcome():
    
    print("\nWelcome to Asher's Studio 6 program!")


def nonnegative_int(prompt):
    while True:
        user_inp = input(prompt)
        try:
            value = int(user_inp)
            if value <= 0:
                print("Enter a non negative number")
            else:
                return value
        except ValueError:
            print("Please enter a valid number")


def class_duration(class_num, day_name):
    hours = nonnegative_int(f"{day_name} - Class # {class_num}: hours? ")
    minutes = nonnegative_int(f"{day_name} - Class # {class_num}: minutes? ")
                            
    return hours * 60 + minutes



def main():
    welcome()

    days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
    daily_hours = []

    for day in days:
        num_classes = nonnegative_int(f"How many classes on {day}? ")

        total_minutes = 0
        for i in range(1, num_classes + 1):
            total_minutes += class_duration(i,day)
        
        total_hours_decimal = total_minutes / 60.0
        daily_hours.append(total_hours_decimal)

        print(f"Total time in class on {day}: {total_hours_decimal:.2f} hours\n")

    print("Weekly schuedle (hours in class):")

    for i in range(len(days)):
        print(f"{days[i]}: {daily_hours[i]:2f} hours")

main()
