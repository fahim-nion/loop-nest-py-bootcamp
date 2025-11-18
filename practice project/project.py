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
    fir = int(input("Enter your first number:"))
    sec = int(input("Enter your second number:"))
    if opt == 1:
        print(f"Result: {addition(fir,sec)}")
        choice = input('''Do you want to continue? (yes/no): yes
                        ''')
        if choice.lower() == "yes":
            continue
        else:
            break
    if opt == 2:
        print(f"Result: {subtraction(fir,sec)}")
        choice = input('''Do you want to continue? (yes/no): yes
                        ''')
        if choice.lower() == "yes":
            continue
        else:
            break
    if opt == 1:
        multiplication(fir,sec)
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