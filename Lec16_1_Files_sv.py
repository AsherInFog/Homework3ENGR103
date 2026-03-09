##########################################################################
# Program Filename: Lec16_1_Files_sv.py
# Author: Asher Charlton
# Date: March 6, 2026
# Description: Writing data to and reading data from a CSV file
# Input: A 2D list
# Output: Data written to a CSV file
##########################################################################

import csv

FILENAME = "Students.csv"

##########################################################################
# Function: write_data
# Description: Writes data to a CSV file.
# Parameters: students (a 2D list)
# Return values: None
# Pre-Conditions: N/A
# Post-Conditions: N/A
##########################################################################
def write_data(filename, students):
    with open(filename, "w", newline = "") as file:
        writer = csv.writer(file)
        for row in students:
            writer.writerow(row)

    print("CSV file written successfully!\n")

##########################################################################
# Function: read_data
# Description: Reads data from a CSV file.
# Parameters: None
# Return values: None
# Pre-Conditions: N/A
# Post-Conditions: N/A
##########################################################################
def read_data(filename):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

##########################################################################
# Function: append_data
# Description: Adds a new student record to the CSV file.
# Parameters: filename, name, score, major
# Return values: None
# Pre-Conditions: N/A
# Post-Conditions: N/A
##########################################################################
def append_data(filename, name, score, major):
    with open(filename, "a", newline = "") as file:
        writer = csv.writer(file)
        writer.writerow([name, score, major])

    print("\nNew student record added to", filename)

##########################################################################
# Function: main
# Description: Main program control
# Parameters: None
# Return values: None
# Pre-Conditions: N/A
# Post-Conditions: N/A
##########################################################################
def main():
    students = [
                ["Alice", 91, "Industrial Engineering"],
                ["Bob", 85, "Mechanical Engineering"],
                ["Carlos", 88, "Computer Science"]
               ]

    write_data(FILENAME, students)

    print("Reading data from", FILENAME + ":")
    read_data(FILENAME)

    append_data(FILENAME, "Asher", 95, "Applied Compute Science")

    print("\nReading updated data from", FILENAME + ":")
    read_data(FILENAME)

main()