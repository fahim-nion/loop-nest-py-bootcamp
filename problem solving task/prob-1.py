'''
Given a year, determine whether it is a leap year.If it is a leap year, return the Boolean True, otherwise return False.

'''

yr = int(input("Enter a year: "))

if yr%400 == 0:
    print(True)
elif yr%4 == 0 and yr%100!= 0:
    print(True)
else:
    print(False)