'''
6. Dictionaries - Basic Lookups

● Problem: "Price Checker"

○ Description: You have a dictionary that stores item names (keys) and their
prices (values). Given the dictionary and a specific item_name, write a program
to print the price of that item. If the item is not in the dictionary, print "Item Not
Found".
○ Input Example:
■ prices = {"apple": 0.50, "banana": 0.25, "orange":
0.75}
■ item_name = "banana"
○ Expected Output: 0.25


'''

prices = {
    "apple": 0.50, 
    "banana": 0.25, 
    "orange":0.75
    }

item_name = input("which product you wanna know the price of: ").lower()

if item_name in prices:
    print(prices[item_name])
else:
    print("Item Not Found")