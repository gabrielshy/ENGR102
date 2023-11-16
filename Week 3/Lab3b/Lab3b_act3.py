:####################################################################
# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# Class and Section: ENGR 102 556
# Assignment: Lab3b_Act3
# Date: 9/14/21
####################################################################
import math
from math import *

d = input("Please enter the number of digits of precision for pi:")

pi = float(math.pi)
form = '{0:.'+d+'f}'
print(f"The value of pi to", d,"is:", form.format(pi))
