'''
🧠 Problem 5: Simple Grading System
📝 Task:
Take a number input from the user (between 0 to 100) and print the grade according to the following rule:
80–100 → A+
70–79 → A
60–69 → A-
50–59 → B
40–49 → C
33–39 → D
0–32 → F
🎯 Example:
Enter your score: 75
Your grade: A
'''
marks = 72

if marks >= 80:
    print("Grade: A+")
elif marks >= 70:
    print("Grade: A")
elif marks >= 60:
    print("Grade: A-")
else:
    print("Grade: Below Average")
