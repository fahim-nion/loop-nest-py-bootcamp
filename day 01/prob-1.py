'''
Practice Problem - 1: “Swapping Two Variables” Using multiple assignments, 
we can swap the values of two variables without needing a temporary variable.
'''

a = 10
b = 20

print("before changing a is",a)
print("before changing b is",b)

# a = b = a #but this is wrong too

a,b = b,a

print("after changing a will be",a)
print("after changing b will be",b)