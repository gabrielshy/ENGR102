####################################################################
# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# Class and Section: ENGR 102 556
# Assignment: Lab4b_Act4
# Date: 9/15/21
####################################################################

A = float(input("Please enter the coefficient A: "))
B = float(input("Please enter the coefficient B: "))
C = float(input("Please enter the coefficient C: "))

if A == 0 and B == 0:
    print("You entered an invalid combination of coefficients")
else:
    s = B * B - 4 * A * C
    if s == 0:
        print("The root is x =", -B / (2 * A))
    elif s > 0:
        r1, r2 = (-B + s ** 0.5) / (2 * A), (-B - s ** 0.5) / (2 * A)
        print("The root are x =", r1,"and x =", r2)
    else:
        r1, r2 = (-B + (-s) ** 0.5) / (2 * A), (-B - (-s) ** 0.05) / (2 * A)
        print("The root are x =", r1,"and x =", r2)