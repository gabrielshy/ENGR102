####################################################################
# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# Class and Section: ENGR 102 556
# Assignment: Lab6_Act3
# Date: 9/29/21
####################################################################

n = input("Enter a four-digit integer: ")

if len(n) != 4:
    print("Error: Incorrect number of digits")

def ascend(n):
    return int("".join(sorted([i for i in str(n)])))

def descend(n):
    return int("".join(sorted([i for i in str(n)], reverse = True)))

counter = 0
iterations = [n,]

while n != 6174:
    counter += 1
    n = descend(n) - ascend(n)
    iterations.append(n)

print(" < ".join(map(str,iterations)))
print("The number of times it took the input to get to 6174 was: ", counter)