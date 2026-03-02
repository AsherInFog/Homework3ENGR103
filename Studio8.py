##########################################################################
# Program Filename: Studio8_2D_Lists.py
# Author: Floppa
# Date: March 2, 2026
# Description: Tracks time a student spends in class each day of the
#              workweek using a 2D list. Prints daily and weekly schedules.
# Input: Number of classes per day, hours and minutes for each class
# Output: Daily schedule and weekly schedule in decimal hours
##########################################################################

def get_valid_input(prompt):
    """Gets a valid integer between 1 and 100 from the user."""
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 100:
                return value
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def get_day_classes(day):
    """Asks user for class info for one day. Returns a list of hours per class."""
    print(f"\n--- {day} ---")
    
    # Ask for number of classes (0 is valid)
    while True:
        try:
            num_classes = int(input(f"How many classes do you have on {day}? "))
            if 0 <= num_classes <= 100:
                break
            else:
                print("Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # If 0 classes, return [0] as a placeholder
    if num_classes == 0:
        return [0]

    day_classes = []
    for i in range(num_classes):
        print(f"  Class {i + 1}:")
        hours = get_valid_input(f"    How many hours does class {i + 1} last? ")
        minutes = get_valid_input(f"    How many minutes does class {i + 1} last? ")
        total_hours = hours + minutes / 60
        day_classes.append(total_hours)

    return day_classes

def print_daily_schedule(schedule, days):
    """Prints the detailed daily schedule showing hours per class."""
    print("\n========== DAILY SCHEDULE ==========")
    for i in range(len(days)):
        print(f"\n{days[i]}:")
        if schedule[i] == [0]:
            print("  No classes")
        else:
            for j in range(len(schedule[i])):
                print(f"  Class {j + 1}: {schedule[i][j]:.2f} hours")

def print_weekly_schedule(schedule, days):
    """Prints the weekly schedule showing total hours per day."""
    print("\n========== WEEKLY SCHEDULE ==========")
    for i in range(len(days)):
        if schedule[i] == [0]:
            total = 0
        else:
            total = sum(schedule[i])
        print(f"  {days[i]}: {total:.2f} hours")

def main():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
    # 2D list: each element is a list of hours per class for that day
    weekly_schedule = []

    print("Welcome! Let's track your weekly class schedule.")
    print("Enter hours and minutes as whole numbers between 1 and 100.\n")

    for day in days:
        day_data = get_day_classes(day)
        weekly_schedule.append(day_data)

    print_daily_schedule(weekly_schedule, days)
    print_weekly_schedule(weekly_schedule, days)

main()