'''
### ✅ **Problem 4: Even Number Finder**

Write a function called `even_numbers_in_range(start, end)` that:

- Takes two numbers and returns a **list** of even numbers between them using a loop.

Example:

```python
even_numbers_in_range(2, 10)
# Output: [2, 4, 6, 8, 10]
```
'''


def even_numbers_in_range(start,end):
    even_list = []
    for i in range(start,end+1):
        if i%2==0:
            even_list.append(i)
    return even_list

print(even_numbers_in_range(2,10))

'''
Output:
[2, 4, 6, 8, 10]

'''

