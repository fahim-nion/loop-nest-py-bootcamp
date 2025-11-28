'''
### ✅ **Problem 2: Unique Fruits Organizer**

You have the following list of fruits:

```python
fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'kiwi']

```

- Remove duplicates using a **set**
- Convert it back to a list and sort alphabetically
- Print the final clean fruit list
'''

fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'kiwi']
updated_fruits = set(fruits)
sorted(updated_fruits)
print(list(updated_fruits))

'''
output:

['orange', 'kiwi', 'banana', 'apple']
'''
