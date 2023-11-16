####################################################################
# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# I have not given or received any unauthorized aid on this assignment.
# Class and Section: ENGR 102 556
# Assignment: Lab10b_Act2
# Name: Francis Gabriel Anos
# Date: 11/15/21
####################################################################

filename = input("Please enter the output filename:")
p = float(input("Please enter the principal amount:"))
n = int(input("Please enter the term length (months):"))
i = float(input("Please enter the annual interest rate:"))

j = i/12
m = p * j / (1 - (1 + j)**-n)

file = open(filename, "w")
topbar = ["Month, ", "Total Accured interest, ", "Loan Balance \n"]
file.writelines(topbar)
row_one = ["0",",","$","0.00",",","$",p," \n"]
s = ' '.join([str(elem) for elem in row_one])
file.writelines(s)

t=0
for j in range(n):
    tai = (p * i/12)
    t = t + tai
    p = (p - m) + tai
    st = ""
    # the '$' sign won't let the number show in excel, but it shows in wordpad
    ls = [j+1,",","$",t,",","$",p," \n"]
    st = ' '.join([str(elem) for elem in ls])
    file.writelines(st)
file.close()