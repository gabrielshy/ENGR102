####################################################################
# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# Class and Section: ENGR 102 556
# Assignment: Lab4b_Act1
# Date: 9/15/21
####################################################################

A = float(input("Enter number 1: "))
B = float(input("Enter number 2: "))
C = float(input("Enter number 3: "))

if A < B and A < C:
    print("The smallest number is:", A)
elif B < A and B < C:
    print("The smallest number is:", B)
elif C < A and C < B:
    print("The smallest number is:", C)
else:
    print("Invalid")