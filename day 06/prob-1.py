'''
### ✅ **Problem 1: Student Grade Calculator**

Create a function called `calculate_grade()` that:

- Takes a student’s name and marks of 3 subjects as input.
- Calculates the average and determines the grade:
    - A if avg ≥ 80
    - B if avg ≥ 70
    - C if avg ≥ 60
    - F otherwise
- Return a dictionary like this:

```python
{
  'name': 'Rafi',
  'average': 76.33,
  'grade': 'B'
}
```

'''


def calculate_grade(name,marks):
    grade_sheet ={
        "name" : None,
        "average" : None,
        "grade" : None
    }
    avg = round(marks/3,2)
    if avg>=80:
        grade = "A"
    elif 70<=avg<=79:
        grade = "B"
    elif 60<=avg<=69:
        grade = "C"
    else:
        grade = "F"
        
    grade_sheet["name"] = name
    grade_sheet["average"] = avg
    grade_sheet["grade"] = grade
    
    print(grade_sheet)

calculate_grade("Fahim",225)

'''
output:
{'name': 'Fahim', 'average': 75.0, 'grade': 'B'}
'''