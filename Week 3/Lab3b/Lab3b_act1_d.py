####################################################################
# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# Class and Section: ENGR 102 556
# Assignment: Lab3b_Act1
# Date: 9/8/21
####################################################################

print("This program calculates pressure of an ideal gas given moles, volume (m^3), and temperature (K)")

moles = float(input("Please enter moles: "))
volume = float(input("Please enter volume (m^3): "))
temp = float(input("Please enter temperature (K): "))

nRT = float(moles*8.314*temp)
pressure = float(nRT/volume)
print(pressure,"kPa")