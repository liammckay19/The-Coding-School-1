# and or not <-- are logical operators
x = True
y = True
z = False

print(x and y)  # True
print(y and z)  # False
print(z and x)  # False

print(not z)  # True
print(not (x or z) and y)  # False


print(x or z)  # True
print(not (x or z))  # False
print(False and y)  # False