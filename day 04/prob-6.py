'''
### 🎂 **Problem 6: Age Group Identifier**

**📝 Task:**

Ask the user to input their age. Based on the age, print what category they belong to:

- 0–12 → Child
- 13–19 → Teenager
- 20–35 → Young Adult
- 36–59 → Adult
- 60+ → Senior Citizen
'''

age = int(input("Enter your age: "))

if 0 <= age <= 12:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")
elif 20 <= age <= 35:
    print("Young Adult")
elif 36 <= age <= 59:
    print("Adult")
elif age >= 60:
    print("Senior Citizen")
else:
    print("Invalid age entered.")
