####################################################################
# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# Class and Section: ENGR 102 556
# Assignment: Lab3b_Act1
# Date: 9/8/21
####################################################################

from math import *
import math

print("This program calculates wavelength given distance and angle in degrees in first order diffraction")

distance = float(input("Please enter distance between crystal layers (nm): "))
angle = float(input("Please enter angle in degrees: "))
radian = math.radians(angle)

wavelength = 2*distance*sin(radian)/1
print("The wavelength is","%.4f" % wavelength,"nm")