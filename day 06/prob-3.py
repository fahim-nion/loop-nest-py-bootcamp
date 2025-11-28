'''
### ✅ **Problem 3: User Profile Generator**

Create a function called `create_profile()` that takes:

- name (string), age (int), and skills (list of strings)
- Returns a dictionary like this:

```python
{
  'name': 'Anika',
  'age': 21,
  'skills': ['Python', 'HTML', 'CSS']
}

```
'''


def create_profile(name,age,skills):
    res_dict = {
        "name" : name,
        "age" : age,
        "skills" : skills
    }
    
    return res_dict

print(create_profile("Fahim",23,['Python', 'HTML', 'CSS']))