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

import random

SERVICE_TIMES = [18.63, 36.21, 5.97]

SERVICE_PROBS = [0.30, 0.50, 1.00]

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


def get_float_input(prompt):
    
    while True:
        user_input = input(prompt)
        try:
            value = float(user_input)
        except ValueError:
            print("Your input must be a number and greater than 0, please try again")
        
        if value > 0:
            return value
        else:
            print("Your input must be a number and greater than 0, please try again")


def assign_service():

    rand_val = random.random()
    for service_id, threshold in enumerate(SERVICE_PROBS):
        if rand_val <= threshold:
            return service_id


def assign_server(server_times):

    min_time = server_times[0]
    min_server = 0

    for server_id in range(1, len(server_times)):
        if server_times[server_id] < min_time:
            min_time = server_times[server_id]
            min_server = server_id

    return min_server


def simulate_customers(num_customers, num_servers):

    server_times = []
    for _ in range(num_servers):
        server_times.append(0.0)
    
    customer_services = []
    customer_servers = []
    running_totals = []

    for _ in range(num_customers):
        service_id = assign_service()
        server_id = assign_server(server_times)
        server_times[server_id] += SERVICE_TIMES[service_id]

        customer_services.append(service_id)
        customer_servers.append(server_id)
        running_totals.append(server_times[server_id])

    return customer_services, customer_servers, running_totals, server_times

def print_customer_table(num_customers, customer_services, customer_servers, running_totals):
    """
    Prints the customer information table showing Customer ID, Service ID,
    DMV Server ID, and the running total service time for the assigned server.
    """
    header = f"{'Customer ID':>12}  {'Service ID':>12}  {'DMV Server ID':>14}  {'Total Service Time':>18}"
    separator = "-" * len(header)

    print()
    print(header)
    print(separator)

    for cust_id in range(num_customers):
        print(f"{cust_id:>12}  {customer_services[cust_id]:>12}  "f"{customer_servers[cust_id]:>14}  {running_totals[cust_id]:>18.2f}")

    print(separator)


def print_server_table(server_times, shift_length):
    """
    Prints the DMV server summary table showing Server ID, total service time,
    and utilization percentage for each server.
    shift_length: length of the shift in minutes (used to compute utilization).
    """
    header = f"{'DMV Server ID':>14}  {'Total Service Time':>18}  {'Utilization (%)':>15}"
    separator = "-" * len(header)

    print()
    print(header)
    print(separator)

    for server_id in range(len(server_times)):
        utilization = (server_times[server_id] / shift_length) * 100
        print(f"{server_id:>14}  {server_times[server_id]:>18.2f}  {utilization:>15.2f}")

    print(separator)


def main():
    """
    Main function: collects user inputs, runs the simulation,
    and prints the customer and server output tables.
    """
    num_customers = int_input("Enter the number of customers: ")
    num_servers = int_input("Enter the number of DMV servers: ")
    shift_length = get_float_input("Enter the shift length in minutes: ")

    customer_services, customer_servers, running_totals, server_times = simulate_customers(
        num_customers, num_servers
    )

    print_customer_table(num_customers, customer_services, customer_servers, running_totals)
    print_server_table(server_times, shift_length)


main()