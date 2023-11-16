####################################################################
# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# Class and Section: ENGR 102 556
# Assignment: Lab6_Act1
# Date: 9/29/21
####################################################################

n = int(input("Enter a positive integer to compute the Collatz sequence: "))
i = int(0)
print("Here is the Collatz sequence starting at: ", n)

digits = [n,]

while n != 1:
    i += 1
    if n % 2 == 0:
        n = int(n / 2)
    else:
        n = int(3 * n + 1)
    digits.append(n)

print(", ".join(map(str,digits)))
print("It took", i,"iterations to reach 1")