####################################################################
# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# Class and Section: ENGR 102 556
# Assignment: Lab6_Act2
# Date: 9/29/21
####################################################################

input1 = int(input("Enter an integer: "))
sum1 = int(0)
product1 = int(1)

for i in range(input1 + 1):
    sum1 += i

for i in range(input1):
    i += 1
    product1 *= i

print("The sum of all integers from 0 to", input1,"is", sum1)
print("The sum of all integers from 1 to", input1,"is", product1)