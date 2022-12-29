from art import *

# Calculator
# Add
def add(n1, n2):
    return n1 + n2

# Substract
def substract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = { "+": add,
               "-": substract,
               "*": multiply,
               "/": divide
               }

def do_calculation(num1):
    print(logo)
    should_continue = 'y'
    while should_continue == 'y':
        if num1 is None:
            num1 = float(input("What's the first number? "))
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        calculate_function = operations[operation]
        answer = calculate_function(num1,num2)
        print(f"{num1} {operation} {num2} = {answer}")

        should_continue = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start new calculation, or type 's' to stop the program: ")
    if should_continue == 'n':
        do_calculation(None)
    elif should_continue == 's':
        print("Goodbye!")

do_calculation(None)



