####################################################################
# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
#
# Name(s): Abdullah Balbaid, Kaeri Salazar, and Gabriel Anos
# Class and Section: ENGR 102 556
# Assignment: Lab3a_Act2
# Date: 9/21/21
# Group: 13
####################################################################

form= '{:.2f}'

def interpolate(t,t1,t2,dx1,dy1,dz1,dx2,dy2,dz2) :
    dx = ((dx2 - dx1) / (t2 - t1)) * (t - t1) + dx1
    dy = ((dy2 - dy1) / (t2 - t1)) * (t - t1) + dy1
    dz = ((dz2 - dz1) / (t2 - t1)) * (t - t1) + dz1

    dx = form.format(dx)
    dy = form.format(dy)
    dz = form.format(dz)
    print("At time", t, "seconds the object is at", end='')
    print('(', dx, ', ',dy , ', ', dz, ')', sep='')

print("                ----------> Position calculator 3D <----------")
print("       -----> Time <-----")
t1= float(input("Enter first time   -->"))
t2= float(input("Enter second time   -->"))
print("       -----> First Position <-----")
dx1= float(input("Enter the position of X dimension   -->"))
dy1= float(input("Enter the position of Y dimension   -->"))
dz1= float(input("Enter the position of Z dimension   -->"))
print("       -----> Second Position <-----")
dx2= float(input("Enter the position of X dimension   -->"))
dy2= float(input("Enter the position of Y dimension   -->"))
dz2= float(input("Enter the position of Z dimension   -->"))
t=t1
interpolate(t,t1,t2,dx1,dy1,dz1,dx2,dy2,dz2)
t+=0.2
interpolate(t,t1,t2,dx1,dy1,dz1,dx2,dy2,dz2)
t+=0.3
interpolate(t,t1,t2,dx1,dy1,dz1,dx2,dy2,dz2)
t+=0.3
interpolate(t,t1,t2,dx1,dy1,dz1,dx2,dy2,dz2)
t+=0.2
interpolate(t,t1,t2,dx1,dy1,dz1,dx2,dy2,dz2)