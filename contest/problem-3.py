'''
3. String Slicing

● Problem: "The Palindrome Checker (Part 1)"

○ Description: A palindrome is a word that reads the same forwards and backward
(e.g., "level"). Write a program that takes a single lowercase word as input. Use
string slicing to create a reversed version of the word. Print both the original
and the reversed word. (The actual comparison is not required yet, just the
reversal).
○ Input Example: "madam"
○ Expected Output: madam (Original), madam (Reversed)

'''

inp = input("Enter the string:").lower()

pal = inp[-1::-1]

print(f"{inp} (Original), {pal}(Reversed)")