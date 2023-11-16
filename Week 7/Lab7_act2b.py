####################################################################
# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# I have not given or received any unauthorized aid on this assignment.
# Class and Section: ENGR 102 556
# Assignment: Lab7_Act2b
# Date: 10/6/21
####################################################################

values = input("Enter three or more values separated by spaces: ")
separator = input("Enter a two-character separator: ")

value_list = values.split()

print((f' {separator} ').join(map(str, value_list)))