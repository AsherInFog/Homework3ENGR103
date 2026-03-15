##########################################################################
# Program Filename: FinalProject.py
# Author: Asher Charlton
# Date: March 13, 2026
# Description: This program analyzes a production line by collecting
#              workstation processing times and computing key performance
#              metrics including total time, cycle time, bottleneck
#              station, and line efficiency
# Input: Number of workstations, processing time for each workstation,
#        menu choices, station number and new time for improvements
# Output: Production line metrics displayed in a tabular format
##########################################################################


##########################################################################
# Function: float_input
# Description: asks the user for a positive float and keeps asking until
#              they enter something valid
# Parameters: prompt is the input message to display
# Return values: value is the validated float
# Pre-Conditions: prompt is a string
# Post-Conditions: returns a float greater than 0
##########################################################################
def float_input(prompt):
    # keeps looping until a valid positive float is entered
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a value greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a number.")


##########################################################################
# Function: int_input
# Description: asks the user for a positive integer and keeps asking until
#              they enter something valid
# Parameters: prompt is the input message to display
# Return values: value is the validated integer
# Pre-Conditions: prompt is a string
# Post-Conditions: returns an integer greater than 0
##########################################################################
def int_input(prompt):
    # keeps looping until a valid positive integer is entered
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a value greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a number.")


##########################################################################
# Function: display_menu
# Description: prints the 4 menu options to the screen
# Parameters: None
# Return values: None
# Pre-Conditions: N/A
# Post-Conditions: prints menu to screen
##########################################################################
def display_menu():
    # prints all 4 menu options
    print()
    print("1. Enter workstation times")
    print("2. Display production metrics")
    print("3. Improve a workstation")
    print("4. Exit")


##########################################################################
# Function: workstation_times
# Description: asks the user for the number of workstations and then
#              collects a processing time for each one and stores them in a list
# Parameters: None
# Return values: times is the list of processing times
# Pre-Conditions: N/A
# Post-Conditions: returns a list of floats greater than 0
##########################################################################
def workstation_times():
    # collects workstation count and times, returns the list
    num_stations = int_input("Enter number of workstations: ")
    times = []
    for i in range(num_stations):
        t = float_input(f"Enter processing time (in minutes) for workstation {i + 1}: ")
        times.append(t)
    return times


##########################################################################
# Function: display_metrics
# Description: calculates and prints total time, cycle time, line efficiency,
#              and bottleneck station in a tabular format
# Parameters: times is the list of workstation processing times
# Return values: None
# Pre-Conditions: times is a non-empty list of floats greater than 0
# Post-Conditions: prints production line metrics to the screen
##########################################################################
def display_metrics(times):
    # calculates all four metrics then prints them out
    total = 0
    for i in range(len(times)):
        total += times[i]

    cycle = times[0] # starts with the first one and see if there's anything bigger
    bottleneck = 0
    for i in range(len(times)):
        if times[i] > cycle:
            cycle = times[i]
            bottleneck = i

    efficiency = (total / (len(times) * cycle)) * 100 # efficieny percentage

    print()
    print("------ PRODUCTION LINE METRICS ------")
    print(f'{"Total Processing Time:":>22} {total:.2f} minutes')
    print(f'{"Cycle Time:":>22} {cycle:.2f} minutes')
    print(f'{"Line Efficiency:":>22} {efficiency:.2f}%')
    print(f'{"Bottleneck Station:":>22} Station {bottleneck + 1}')
    print("-" * 36)


##########################################################################
# Function: improve_workstation
# Description: asks the user to pick a station and enter a new lower time
#              then updates that station in the list
# Parameters: times is the list of workstation processing times
# Return values: None
# Pre-Conditions: times is a non-empty list of floats greater than 0
# Post-Conditions: updates one element in the times list
##########################################################################
def improve_workstation(times):
    # gets a station number and new time, updates the list
    station = int_input("Enter station number to improve: ")
    if station < 1 or station > len(times): # have to make sure the entered station number actually exists!
        print("Invalid station number.")
        return
    new_time = float_input("Enter new processing time (in minutes): ")
    times[station - 1] = new_time
    print("Station updated successfully.")


##########################################################################
# Function: main
# Description: runs the main menu loop and calls the right function
#              based on what the user picks
# Parameters: None
# Return values: None
# Pre-Conditions: N/A
# Post-Conditions: program runs until user selects option 4
##########################################################################
def main():
    # main loop, keeps going until the user exits
    times = [] # just empty until they enter something
    choice = ""

    while choice != "4":
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            times = workstation_times()
        elif choice == "2":
            if len(times) == 0:
                print("No station data available.")
            else:
                display_metrics(times)
        elif choice == "3":
            if len(times) == 0:
                print("No station data available.")
            else:
                improve_workstation(times)
        elif choice == "4":
            print("Goodbye!")
        else:
            print("Invalid option. Please choose 1-4.")


main()