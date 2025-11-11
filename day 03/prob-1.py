'''
> **Practice Problem-1:** Merge and Sort Lists

> You are given two lists of numbers:
list1 = [7, 2, 9]
list2 = [4, 1, 6]

# Create a single list that combines both lists and returns a sorted list in ascending order.
'''

list1 = [7, 2, 9]
list2 = [4, 1, 6]

list1.extend(list2)
list1.sort()
print(list1)