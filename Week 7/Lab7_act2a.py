####################################################################
# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# Class and Section: ENGR 102 556
# Assignment: Lab7_Act2a
# Date: 10/6/21
####################################################################

prices = input("Enter three or more prices separated by spaces: ")

price_list = prices.split()
price_list = sorted(price_list, key = len)
price_list = list(map(float, price_list))

for i in price_list:
    print(f'$ {i:10.2f}')