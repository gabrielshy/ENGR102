####################################################################
# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# Class and Section: ENGR 102 556
# Assignment: Lab4b_Act2
# Date: 9/15/21
####################################################################

a = 1/7
print('a =', a)
b = a * 7
print('b = a * 7 =', b) # yes, b is equal to 1.0

c = 2 * a
d = 5 * a
f = c + d
print('f = 2 * a + 5 * a =', f) # no, f is equal to 0.9999999999999999

from math import sqrt
x = sqrt(1/3)
print('x =', x)
y = x * x * 3
print('y = x * x * 3 =', y)
z = x * 3 * x
print('z = x * 3 * x =', z) # y is equal to 1.0 but z is equal to 0.9999999999999999

TOL = 1e-10
if abs(b-f) < TOL:
    print('b and f are equal within tolerance of', TOL)
else:
    print('b and f are NOT equal within tolerance of', TOL)

m = 0.1
print('m =', m)
n = 3 * m
print('n = 3 * m = 0.3', n == 0.3)
p = 7 * m
print('p = 7 * m = 0.7', p == 0.7)
q = n + p
print('q = 1', q == 1)
