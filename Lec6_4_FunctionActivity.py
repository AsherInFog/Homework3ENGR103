#########################################################################
# Program Filename: Lec6_4_FunctionActivity.py
# Author: Asher Charlton 
# Date: January 22, 2026
# Description: Converting a sequential program into a program with functions.
# Input: Gas pressure, gas moles, and gas temperature
# Output: Gas volume
##########################################################################
# INSTRUCITONS:
# 1. Conver the sequential set of instructions below into a program
# that uses one function.
# 2. Define the function compute_gas_volume that returns the volume of a
# gas given the parameters pressure, temperature, and moles.
# 3. Use the gas equation PV = nRT, where:
# - P is pressure in Pascals,
# - V is volume in cubic meters,
# - n is number of moles,
# - R is the gas constant 8.3144621 (J / (mol*K)), and
# - T is temperature in Kelvin.
# 4. Print the result for gas_volume with 3 digits of precision.
# 5. ADD THE FUNCTION HEADER AS NEEDED, BUT YOU CAN CHANGE THE INFO LATER.
##########################################################################
# Function: TBD
# Description: TBD
# Parameters: TBD
# Return values: TBD
# Pre-Conditions: TBD
# Post-Conditions: TBD
##########################################################################

def compute_gas_volume(gas_pressure, gas_temperature, gas_moles, gas_volume):
    GAS_CONST = 8.3144621
    gas_pressure = 0.0
    gas_moles = 0.0
    gas_temperature = 0.0
    gas_volume = (gas_moles * GAS_CONST * gas_temperature) / gas_pressure
    final = print(f'Gas volume: {gas_volume:.3f} m^3')

    return gas_pressure, gas_temperature, gas_moles, gas_volume, final

compute_gas_volume(9.3,5.3,2.3,8.4)
