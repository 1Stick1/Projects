def calculator():
    a = float(input("Enter number 1: "))    
    b = float(input("Enter number 2: "))
    while True:
        iteration = input("Choose iteration: ")
        match iteration:
            case '+':
                return a + b
            case '-':
                return a - b
            case '/':
                return a / b
            case '*':
                return a * b


print(calculator())