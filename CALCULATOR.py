def calculator():
    no1 = int(input("Enter the first number: "))
    no2 = int(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    if operation == '+':
        result = no1 + no2
    elif operation == '-':
        result = no1 - no2
    elif operation == '*':
        result = no1 * no2
    elif operation == '/':
        if no2 != 0:
            result = no1 / no2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operation!"

    return f"{no1} {operation} {no2} = {result}"

print(calculator())