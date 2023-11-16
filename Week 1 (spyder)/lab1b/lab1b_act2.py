"""
By submitting this assignment, I agree to the following:
“Aggies do not lie, cheat, or steal, or tolerate those who do”
Created on Tue Aug 31 17:20:37 2021

@author: anosf
"""

from math import *
import math
# Below is the calculation for Force
newtons = 2*5

# Below is the calculation for Wavelength
# The radian variable converts 25 deg to a radian
radian = math.radians(25)
wavelength = 2*0.025*sin(radian)/1

# Below is the calculation for Radon-222
# The 'time' variable calculates the power
time = -5/3.8
radon = 3*(2)**time

# Below is the calculation for Pressure - (volume changed to 150.0, because it's 0.15 raised to the 3rd power)
nRT =  5*8.3144626*425
pressure = nRT/150.0

print("Force:",newtons,"N")
print("Wavelength:",wavelength,"nm")
print("Radon-222:",radon,"g")
print("Pressure:",pressure,"kPa")