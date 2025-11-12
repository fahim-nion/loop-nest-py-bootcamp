'''
7. Sets
● Problem: "Unique Visitors"

○ Description: You are tracking visitors to a website. Given two lists of visitor IDs
from two different days (day1_visitors and day2_visitors). Write a
program that uses sets to find and print the total count of unique visitors
across both days.

○ Input Example:
■ day1_visitors = [101, 105, 108, 101, 109]
■ day2_visitors = [108, 102, 105, 110]

○ Expected Output: 6 (IDs: 101, 105, 108, 109, 102, 110)
'''

day1_visitors = [101, 105, 108, 101, 109]
day2_visitors = [108, 102, 105, 110]

unique = set(day1_visitors) | set(day2_visitors)
count = len(unique)

print(f"{count} IDs: {tuple(unique)}")