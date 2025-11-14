'''
🔁 Problem 2: Repeat Until User Says ‘stop’
📝 Task:
Keep asking the user to enter any word until they type 'stop'.
Print "Loop Ended" when the loop stops.
🎯 Example Output:
Enter a word: hello
Enter a word: world
Enter a word: stop
Loop Ended

'''

command = "stop"

while True:
    inp = input("enter a word:")
    if inp.lower() == command:
        print("Loop ended")
        break
    print(inp)