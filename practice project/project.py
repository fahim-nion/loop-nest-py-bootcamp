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
    if opt == 1:
        division(fir,sec)
    if opt == 1:
        modulus(fir,sec)
    if opt == 1:
        avg(fir,sec)
    if opt == 1:
        maximum(fir,sec)
    if opt == 8:
        break
    
def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b