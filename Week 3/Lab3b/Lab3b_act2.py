####################################################################
# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# Class and Section: ENGR 102 556
# Assignment: Lab3b_Act2
# Date: 9/8/21
####################################################################

from math import *
from math import sqrt
import math

def output(area):
    circle = sqrt(area/math.pi)
    print("A circle with the area","%.2f" % area,"has the radius","%.3f" % circle)

    etriangle = 2/3*(3**(3/4))*sqrt(area)
    print("An equilateral triangle with the area", "%.2f" % area, "has a side length of", "%.3f" % etriangle)

    square = sqrt(area)
    print("A circle with the area", "%.2f" % area, "has a side length", "%.3f" % square)

    pentagon = 6.68740304*sqrt(area)/8.77166394
    print("A regular pentagon with the area", "%.2f" % area, "has a side length", "%.3f" % pentagon)

    dodecagon = math.sqrt(area*(2-math.sqrt(3))*3)/3
    print("A dodecagon with the area", "%.2f" % area, "has a side length", "%.3f" % dodecagon)

    return

area = float(input("Please enter the area (two decimal points): "))
output(area)