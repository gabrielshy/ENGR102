####################################################################
# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# Class and Section: ENGR 102 556
# Assignment: Lab4b_Act3
# Date: 9/15/21
####################################################################

from math import *

def output_until50(days):
    if days <= 0:
        print("Invalid number")
    elif days <= 10:
        widgets = days * 10
        print("The total number of widgets produced on day", days,"is:", widgets)
    elif days > 10 and days < 50:
        widgets = (0.5 * days ** 2) + (0.5 * days) + 45
        print("The total number of widgets produced on day", days,"is:", widgets)
    elif days >= 50 and days <= 100:
        over = 50
        widgets = 1320
        widgets2 = widgets + over*(days-50)
        print("The total number of widgets produced on day", days,"is:", widgets2)
    elif days >= 101:
        print("The maximum number of days is 100, and the maximum amount of widgets produced is 3820.0")
    else:
        print("Invalid")

days = float(input("Please enter a positive value for day:"))
output_until50(days)