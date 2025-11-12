'''
4. Lists - Basic Operations

● Problem: "Inventory Sorter"

○ Description: You are given a list of product names. Write a program to sort the
list alphabetically and then print the third item in the sorted list.
○ Input Example: products = ["Keyboard", "Mouse", "Monitor",
"Webcam", "Speaker"]
○ Expected Output: Keyboard

'''

products = ["Keyboard", "Mouse", "Monitor",
"Webcam", "Speaker"]  
sorted_products = sorted(products)
# print(sorted_products)  #output: ['Keyboard', 'Monitor', 'Mouse', 'Speaker', 'Webcam']

print(sorted_products[3]) #output: Speaker [as per the question said 3rd product]

print(sorted_products[0]) #output: Keyboard