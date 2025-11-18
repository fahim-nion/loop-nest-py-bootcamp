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
    if opt == 1:
        addi