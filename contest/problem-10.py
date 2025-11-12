'''
10. Integration Challenge: String Slicing, Methods, and Lists
● Problem: "Initial Generator"
○ Description: Given a person's full name (e.g., "Marie Curie").
1. Use a string method to split the full name into a list of words (first
name, last name, etc.).
2. Use string slicing to get the first letter of each word.
3. Combine these first letters to form and print the person's initials in
uppercase, without any spaces or periods.
○ Input Example: "albert einstein
○ Expected Output: AE
'''

inp = input("enter str:")

myl = inp.split(" ")

fir = (myl[0])
sec = (myl[1])

out = fir[0].upper()+sec[0].upper()

print(out)