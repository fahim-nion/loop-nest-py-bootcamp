'''
1. You are given a tuple:

`info = ("Tahsin", "CSE", 2025)`

Print only the name and graduation year using slicing.

**Expected Output:**

`Tahsin 2025`
'''

info = ("Tahsin", "CSE", 2025)

info_sliced_tup = (info[::2])

print(info_sliced_tup[0],info_sliced_tup[1])
