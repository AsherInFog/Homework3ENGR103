##########################################################################
# Program Filename: Homework5.py
# Author: Asher Charlton
# Date: Feb 4th, 2026
# Description: This program simulates a DMV customer service system.
#              It randomly assigns each customer a service type based on
#              historical probabilities, assigns them to the server with
#              the lowest current load, and reports per-customer and
#              per-server summary tables including server utilization.
# Input: Number of customers (int > 0), number of DMV servers (int > 0),
#        shift length in minutes (float > 0)
# Output: Customer table (Customer ID, Service ID, DMV Server ID,
#         Running Total Service Time) and Server table (Server ID,
#         Total Service Time, Utilization %)
##########################################################################

import random

SERVICE_TIMES = [18.63, 36.21, 5.97]

SERVICE_PROBS = [0.30, 0.50, 1.00]


##########################################################################
# Function: int_input
# Description: Gets a valid positive integer from the user
# Parameters: prompt
# Return values: value
# Pre-Conditions: N/A
# Post-Conditions: returns a valid integer greater than 0
##########################################################################
def int_input(prompt):

    while True:
        user_input = input(prompt)
        try:
            value = int(user_input)
        except ValueError:
            print("Your input must be an integer greater than 0, please try again")
            continue

        if value > 0:
            return value
        else:
            print("Your number must be greater than 0, please try again")


##########################################################################
# Function: get_float_input
# Description: Gets a valid positive float from the user
# Parameters: prompt
# Return values: value
# Pre-Conditions: N/A
# Post-Conditions: returns a valid float greater than 0
##########################################################################
def get_float_input(prompt):

    while True:
        user_input = input(prompt)
        try:
            value = float(user_input)
        except ValueError:
            print("Your input must be a number and greater than 0, please try again")
            continue

        if value > 0:
            return value
        else:
            print("Your input must be a number and greater than 0, please try again")


##########################################################################
# Function: assign_service
# Description: Randomly picks a service ID for a customer based on probabilities
# Parameters: None
# Return values: service_id
# Pre-Conditions: SERVICE_PROBS must be defined
# Post-Conditions: returns a service ID of 0, 1, or 2
##########################################################################
def assign_service():

    rand_val = random.random()
    for i in range(len(SERVICE_PROBS)):
        if rand_val <= SERVICE_PROBS[i]:
            return i


##########################################################################
# Function: assign_server
# Description: Finds the server with the lowest total service time
# Parameters: server_times
# Return values: min_server
# Pre-Conditions: server_times must be a non-empty list
# Post-Conditions: returns the index of the least busy server
##########################################################################
def assign_server(server_times):

    min_time = server_times[0]
    min_server = 0

    for server_id in range(1, len(server_times)):
        if server_times[server_id] < min_time:
            min_time = server_times[server_id]
            min_server = server_id

    return min_server


##########################################################################
# Function: simulate_customers
# Description: Runs the full simulation and tracks each customer's results
# Parameters: num_customers, num_servers
# Return values: customer_services, customer_servers, running_totals, server_times
# Pre-Conditions: SERVICE_TIMES and SERVICE_PROBS must be defined
# Post-Conditions: returns four lists with all the simulation data
##########################################################################
def simulate_customers(num_customers, num_servers):

    server_times = []
    for i in range(num_servers):
        server_times.append(0.0)

    customer_services = []
    customer_servers = []
    running_totals = []

    for i in range(num_customers):
        service_id = assign_service()
        server_id = assign_server(server_times)
        server_times[server_id] += SERVICE_TIMES[service_id]

        customer_services.append(service_id)
        customer_servers.append(server_id)
        running_totals.append(server_times[server_id])

    return customer_services, customer_servers, running_totals, server_times


##########################################################################
# Function: print_customer_table
# Description: Prints the customer info table with service and server assignments
# Parameters: num_customers, customer_services, customer_servers, running_totals
# Return values: None
# Pre-Conditions: all four lists must be the same length
# Post-Conditions: prints the customer table to the screen
##########################################################################
def print_customer_table(num_customers, customer_services, customer_servers, running_totals):

    header = f"{'Customer ID':>12}  {'Service ID':>12}  {'DMV Server ID':>14}  {'Total Service Time':>18}"
    separator = "-" * len(header)

    print()
    print(header)
    print(separator)

    for cust_id in range(num_customers):
        print(f"{cust_id:>12}  {customer_services[cust_id]:>12}  "
              f"{customer_servers[cust_id]:>14}  {running_totals[cust_id]:>18.2f}")

    print(separator)


##########################################################################
# Function: print_server_table
# Description: Prints the server summary table with total time and utilization
# Parameters: server_times, shift_length
# Return values: None
# Pre-Conditions: shift_length must be greater than 0
# Post-Conditions: prints the server table to the screen
##########################################################################
def print_server_table(server_times, shift_length):

    header = f"{'DMV Server ID':>14}  {'Total Service Time':>18}  {'Utilization (%)':>15}"
    separator = "-" * len(header)

    print()
    print(header)
    print(separator)

    for server_id in range(len(server_times)):
        utilization = (server_times[server_id] / shift_length) * 100
        print(f"{server_id:>14}  {server_times[server_id]:>18.2f}  {utilization:>15.2f}")

    print(separator)


##########################################################################
# Function: main
# Description: Main program control
# Parameters: None
# Return values: None
# Pre-Conditions: N/A
# Post-Conditions: prints simulation results to the user
##########################################################################
def main():

    num_customers = int_input("Enter the number of customers: ")
    num_servers = int_input("Enter the number of DMV servers: ")
    shift_length = get_float_input("Enter the shift length in minutes: ")

    customer_services, customer_servers, running_totals, server_times = simulate_customers(
        num_customers, num_servers
    )

    print_customer_table(num_customers, customer_services, customer_servers, running_totals)
    print_server_table(server_times, shift_length)


# Call main function to start program execution.
main()