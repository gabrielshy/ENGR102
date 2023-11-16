####################################################################
# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# Class and Section: ENGR 102 556
# Assignment: Lab5b_Act1
# Date: 9/22/21
####################################################################

# Input value for the x value
# This is asking the user for an input strain between 0 and 0.27
strain = float(input("Please input the strain between 0 and 0.27: "))

# These define the set graph / points
strainAx = 0
strainAy = 0
strainBx = 0.01
strainBy = 43
strainCx = 0.06
strainCy = 43.5
strainDx = 0.18
strainDy = 60
strainEx = 0.27
strainEy = 51

# This 'def' is to compile the formulas for the equations
def output(strain):
    if strain >= 0 and strain <= 0.01:
        slopeAB = (strainBy - strainAy) / (strainBx - strainAx)
        stress = strainAy + (slopeAB) * (strain - strainAx)
        print("The stress is approximately:", stress)
    elif strain > 0.01 and strain <= 0.06:
        slopeBC = (strainCy - strainBy) / (strainCx - strainBx)
        stress = strainBy + (slopeBC) * (strain - strainBx)
        print("The stress is approximately:", stress)
    elif strain > 0.06 and strain <= 0.18:
        slopeCD = (strainDy - strainCy) / (strainDx - strainCx)
        stress = strainCy + (slopeCD) * (strain - strainCx)
        print("The stress is approximately:", stress)
    elif strain > 0.18 and strain <= 0.27:
        slopeDE= (strainEy - strainDy) / (strainEx - strainDx)
        stress = strainDy + (slopeDE) * (strain - strainDx)
        print("The stress is approximately:", stress)
    else:
        print("Invalid input")

# This is outputting the equations using the input value
output(strain)