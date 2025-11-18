import math 
def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
def modulus(a,b):
    return a%b
def avg(a,b):
    avrg = (a+b)/2
    return avrg


while True:
    print("Welcome to Python Mini Calculator!")
    
    print(
        '''Choose an option:
            1. Add
            2. Subtract
            3. Multiply
            4. Divide
            5. Modulus
            6. Average of numbers
            7. Maximum number
            8. Exit
        '''
    )
    opt = int(input("Enter your choice: "))
    fir = float(input("Enter your first number:"))
    sec = float(input("Enter your second number:"))
    if opt == 1:
        print(f"Result: {round(addition(fir,sec),2)}")
        choice = input('''Do you want to continue? (yes/no): yes
                        ''')
        if choice.lower() == "yes":
            continue
        else:
            break
    if opt == 2:
        print(f"Result: {round(subtraction(fir,sec),2)}")
        choice = input('''Do you want to continue? (yes/no): yes
                        ''')
        if choice.lower() == "yes":
            continue
        else:
            break
    if opt == 3:
        print(f"Result: {round(multiplication(fir,sec),2)}")
        choice = input('''Do you want to continue? (yes/no): yes
                        ''')
        if choice.lower() == "yes":
            continue
        else:
            break
    if opt == 4:
        if a/b == math.inf:
            print("can not divided by zero")
        else:
            print(f"Result: {round(division(fir,sec),2)}")
            choice = input('''Do you want to continue? (yes/no): yes
                        ''')
            if choice.lower() == "yes":
                continue
            else:
                break
    if opt == 5:
        print(f"Result: {round(modulus(fir,sec),2)}")
        choice = input('''Do you want to continue? (yes/no): yes
                        ''')
        if choice.lower() == "yes":
            continue
        else:
            break
    if opt == 6:
        print(f"Result: {round(avg(fir,sec),2)}")
        choice = input('''Do you want to continue? (yes/no): yes
                        ''')
        if choice.lower() == "yes":
            continue
        else:
            break
    if opt == 7:
        print(f"Result:{max(fir,sec)}")
        choice = input('''Do you want to continue? (yes/no): yes
                        ''')
        if choice.lower() == "yes":
            continue
        else:
            break
    if opt == 8:
        break

