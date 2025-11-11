'''
Practice Problem-4: 
Find Common Hobbies

You are given two sets of hobbies from two friends:
friend_1 = {"reading", "traveling", "gaming"}
friend_2 = {"photography", "traveling", "gaming"}

'''
friend_1 = {"reading", "traveling", "gaming"}
friend_2 = {"photography", "traveling", "gaming"}

common = friend_1 & friend_2

print(common)

'''
output:

{'gaming', 'traveling'}

'''