'''
1. Basic Math & Data Types

● Problem: "The Change Maker"

○ Description: Write a program that takes three integer inputs: the cost of an item,
the amount paid, and the quantity of items purchased. Calculate and print the
total change the customer should receive. If the amount paid is less than the
total cost, print "Insufficient Funds".

○ Input Example: cost = 10, paid = 50, quantity = 3
○ Expected Output: 20

'''


cost = int(input("Enter Cost: "))
paid = int(input("Buyer Paid: "))
quantity = int(input("The quantity: "))

rtrn = paid - (cost * quantity)

if rtrn > 0:
    print(rtrn)
else:
    print("Insufficient Funds")