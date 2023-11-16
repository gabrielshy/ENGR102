####################################################################
# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# I have not given or received any unauthorized aid on this assignment.
# Class and Section: ENGR 102 556
# Assignment: Lab10b_Act1
# Name: Francis Gabriel Anos
# Date: 11/15/21
####################################################################

gametext = open('game.txt','r')

gamelist = gametext.readlines()
gamelen = len(gamelist)
coinlist = []

i = 0
for i in range(gamelen):
    current = gamelist[i]
    coin = open('coins.txt','w')
    if i <= 612:
        if current[0] == 'c':
            if current[5] == '+':
                number = str(current[6:8])
                coin.writelines(number + '\n')
                coinlist.append(current[5:8])
                coin.flush()
            else:
                number = str(current[6:8])
                coin.writelines(number + '\n')
                coinlist.append(current[5:8])
                coin.flush()
        if current[0] == 'j':
            if current[5] == '+':
                value = int(current[6:8]) - 1
                i += value
            else:
                value = int(current[6:8]) - 1
                i -= value
        if current[0] == 'n':
            pass
    else:
        break

gametext.close()
coin.close()

totalcoins = 0
coinlen = len(coinlist)
for i in range(coinlen):
    current = coinlist[i]
    if current[0] == '+':
        number = int(current[1:3])
        totalcoins += number
    else:
        number = int(current[1:3])
        totalcoins -= number

print("Total Number of Coins:", totalcoins)