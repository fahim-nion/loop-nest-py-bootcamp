'''
Print the first 10 Fibonacci numbers
'''

initial = 0
nxt = 1
for _ in range(10):
    print(initial)
    tmp = initial
    initial = nxt
    nxt = tmp + nxt