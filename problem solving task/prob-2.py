'''
N an integer, Without using any string methods, try to print the following: 123...N
'''

N = int(input("Enter a number: "))
string1 = ''
for i in range(1, N+1):
    string1+=str(i)
print(string1)