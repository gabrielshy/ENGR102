z = 0
x = 1
z += x
print(z)

z = 0
y = 10
x = y
y += x
x = 1
x += 1
x += 1
x += 1
x += 1
y += x
z += y
print(z)

x = y
y += x
x = y
y += x
x = 1
x += 1
y += x
z = 0
z += y
print(z)

z = 0
y = 10
x = y
x = y
y *= x
y *= x
y *= x
y *= x
y *= x
y *= x
y *= x
y *= x
z += y
print(z)

z = 0
y = 10
x = y
x += 1
x += 1
x += 1
x += 1
y += x
x = y
y = 10
y *= x
x = y
y = 10
y *= x
x = y
y = 10
y += x
x = y
y = 10
y += x
x = y
y = 10
y += x
x = y
y = 10
y += x
x = y
y = 10
y += x
x = y
y = 10
y += x
x = y
x = 1
x += 1
x += 1
x += 1
x += 1
x += 1
x += 1
x += 1
y += x
z += y
print(z)