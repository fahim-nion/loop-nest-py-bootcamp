'''
8. Advanced Strings & List Manipulation

● Problem: "CSV Line Cleaner"

○ Description: You are given a string representing a dirty line from a CSV file
(Comma Separated Values). The line has leading/trailing spaces and the data is
separated by commas.
1. Use a string method to remove any surrounding whitespace from the
entire line.
2. Use a string method to split the line into a list of individual data points.
3. Print the resulting list.
○ Input Example: " ID001, John Doe , active, 25 "
○ Expected Output: ['ID001', 'John Doe ', 'active', '25'] (Note:
internal spaces are kept)

'''


line = input("Enter the string: ")

clean_line = line.strip() #shamne ar pechoner space removed
data_list = clean_line.split(",")

print(data_list)
