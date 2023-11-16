####################################################################
# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# Class and Section: ENGR 102 556
# Assignment: Lab3b_Act1
# Date: 9/8/21
####################################################################

print("This program calculates Radon-222 given time in days, initial grams, and a half-life of 3.8 days")

days = float(input("Please enter days: "))
g = float(input("Please enter initial grams: "))
halflife = 3.8

time = -days/halflife
radon = g*2**time
print("The Radon-222 is","%.2f" % radon,"g")