'''
9. Dictionaries and List Comprehension (Optional Challenge)

● Problem: "Voting Tally"

○ Description: You are given a list of votes, where each element is the name of a
candidate. Write a program to count the total votes for each candidate and store
the results in a dictionary, where the key is the candidate's name and the value
is their total vote count. Print the dictionary.

○ Input Example: votes = ["Alice", "Bob", "Alice", "Charlie",
"Bob", "Alice"]
○ Expected Output: {'Alice': 3, 'Bob': 2, 'Charlie': 1}


'''

votes = ["Alice", "Bob", "Alice", "Charlie",
"Bob", "Alice"]

count_al = votes.count("Alice")
count_Bob = votes.count("Bob")
count_char = votes.count("Charlie")

dic = {
    "Alice":count_al,
    "Bob":count_Bob,
    "Charlie":count_char
    }

print(dic)