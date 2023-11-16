####################################################################
# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# I have not given or received any unauthorized aid on this assignment.
# Class and Section: ENGR 102 556
# Assignment: Lab7_Act3
# Name: Francis Gabriel Anos
# Date: 10/6/21
####################################################################

import math

vectorA = input("Enter the elements for Vector A: ")
vectorB = input("Enter the elements for Vector B: ")

vector_listA = vectorA.split()
vector_listB = vectorB.split()
AplusB = []
AminusB = []
form = '{0:.4f}'

# Magnitude of A
if len(vector_listA) == 2:
    a = float(vector_listA[0])
    b = float(vector_listA[1])
    magnitudeA = math.sqrt(pow(a, 2) + pow(b, 2))
    print("The magnitude of Vector A is ", form.format(magnitudeA))
elif len(vector_listA) == 3:
    a = float(vector_listA[0])
    b = float(vector_listA[1])
    c = float(vector_listA[2])
    magnitudeA = math.sqrt(pow(a, 2) + pow(b, 2) + pow(c, 2))
    print("The magnitude of Vector A is ", form.format(magnitudeA))
else:
    print("Enter 3 or less values")

# Magnitude of B
if len(vector_listB) == 2:
    a = float(vector_listB[0])
    b = float(vector_listB[1])
    magnitudeB = math.sqrt(pow(a, 2) + pow(b, 2))
    print("The magnitude of Vector A is ", form.format(magnitudeB))
elif len(vector_listB) == 3:
    a = float(vector_listB[0])
    b = float(vector_listB[1])
    c = float(vector_listB[2])
    magnitudeB = math.sqrt(pow(a, 2) + pow(b, 2) + pow(c, 2))
    print("The magnitude of Vector A is ", form.format(magnitudeB))
else:
    print("Enter 3 or less values")

# A + B
for i in range(len(vector_listA)):
    x = float(vector_listA[i]) + float(vector_listB[i])
    AplusB.append(x)

# A - B
for i in range(len(vector_listA)):
    x = float(vector_listA[i]) - float(vector_listB[i])
    AminusB.append(x)

print("A + B is ", AplusB)
print("A - B is ", AminusB)

# Dot Product
if len(vector_listA) and len(vector_listB) == 1:
    dota = float(vector_listA[0]) * float(vector_listB[0])
    print("The dot product is ", dota)
elif len(vector_listA) and len(vector_listB) == 2:
    dota = float(vector_listA[0]) * float(vector_listB[0])
    dotb = float(vector_listA[1]) * float(vector_listB[1])
    print("The dot product is ", dota + dotb)
elif len(vector_listA) and len(vector_listB) == 3:
    dota = float(vector_listA[0]) * float(vector_listB[0])
    dotb = float(vector_listA[1]) * float(vector_listB[1])
    dotc = float(vector_listA[2]) * float(vector_listB[2])
    print("The dot product is ", dota + dotb + dotc)
else:
    print("Error: Sets must contain the same number of values")