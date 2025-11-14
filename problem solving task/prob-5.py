'''Find the factorial of a number using loop'''

N = int(input("Enter a num: "))

fac = 1
for i in range(1, N+1):
    fac = fac*i
print(fac)