'''Password Retry System (while loop)
Task:
Ask the user to input a password using a while loop. Keep asking until they enter the correct password: "python123".
Sample Output:
Enter password: hello
Incorrect! Try again.
Enter password: python123
Access granted!
'''

password = "python123"
while True:
    inp = input("Enter Password: ")
    if inp == password:
        print("Access Granted!")
        break
    else:
        print("Incorrect! Try again")