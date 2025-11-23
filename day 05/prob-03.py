'''Problem 3: Even or Odd Checker
Description:
একটি ফাংশন লিখো  নামে, যেটি একটি সংখ্যা ইনপুট হিসেবে নিবে এবং বলবে এটি Even নাকি Odd।
Example:
check_even_odd(10) ➞ "Even"
check_even_odd(7)  ➞ "Odd" '''

def check_even_odd(val):
    if val % 2==0:
        print("Even")
    else:
        print("Odd")

check_even_odd(10)
check_even_odd(7)

'''
output:
Even
Odd

'''