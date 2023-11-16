####################################################################
# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# Class and Section: ENGR 102 556
# Assignment: Lab3b_Act1
# Date: 9/8/21
####################################################################

print("Newton's Second Law Calculator")
print("This program will calculate the applied force given mass and acceleration")

mass = float(input("Please enter the mass (kg): "))
acceleration = float(input("Please enter the acceleration (m/s^2): "))

force = mass*acceleration
print("The force is","%.1f" % force,"N")