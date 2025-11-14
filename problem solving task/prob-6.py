''' 3. Sum of Numbers (for loop)

**Task:**

Write a program using a `for` loop to calculate the sum of numbers from 1 to 100.

**Expected Output:**

`5050`

'''

N = int(input("Enter Num :"))

sum = 0
for i in range(N+1):
    sum+=i
print(sum)