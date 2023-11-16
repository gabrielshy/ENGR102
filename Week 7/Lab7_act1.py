####################################################################
# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# Class and Section: ENGR 102 556
# Assignment: Lab7_Act1
# Date: 10/6/21
####################################################################

name = input("What is your name? ")
cut_name = name[1:]

if name[0] == "F" or "f":
    print(f"{name}, {name}, Bo-B{cut_name}")
    print(f"Banana-Fana Fo-{cut_name}")
    print(f"Me Mi Mo-M{cut_name}")
elif name[0] == "B" or "b":
    print(f"{name}, {name}, Bo-{cut_name}")
    print(f"Banana-Fana Fo-F{cut_name}")
    print(f"Me Mi Mo-M{cut_name}")
elif name[0] == "M" or "m":
    print(f"{name}, {name}, Bo-B{cut_name}")
    print(f"Banana-Fana Fo-F{cut_name}")
    print(f"Me Mi Mo-{cut_name}")
else:
    print(f"{name}, {name}, Bo-B{cut_name}")
    print(f"Banana-Fana Fo-F{cut_name}")
    print(f"Me Mi Mo-M{cut_name}")