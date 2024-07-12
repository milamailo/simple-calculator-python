import os
from . import operations

def clear_screen():
    # Check if the operating system is Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Unix systems (Linux, macOS)
    else:
        _ = os.system('clear')

def display_menu():
    print("\nSelect an operation to perform:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiate")
    print("6. Modulo")
    print("7. Integer Divide")
    print("8. Negate")
    print("9. Increment")
    print("10. Decrement")
    print("11. Exit")

def user_input(num_of_inputs):
    inputs = []
    if num_of_inputs == 2:
        inputs.append(float(input("Enter first number: ")))
        inputs.append(float(input("Enter second number: ")))
    elif num_of_inputs == 1:
        inputs.append(float(input("Enter the number: ")))
    return inputs

def get_operation_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1-11): "))
            if 1 <= choice <= 11:
                return choice
            else:
                print("Please enter a number between 1 and 11.")
        except ValueError:
            print("Invalid choice. Please enter a number.")

def cli_menu():
    clear_screen()
    while True:
        display_menu()
        choice = get_operation_choice()
        clear_screen()
        match choice:
            case 1:
                num1, num2 = user_input(2)
                print("Result:", operations.add(num1, num2))
            case 2:
                num1, num2 = user_input(2)
                print("Result:", operations.subtract(num1, num2))
            case 3:
                num1, num2 = user_input(2)
                print("Result:", operations.multiply(num1, num2))
            case 4:
                num1, num2 = user_input(2)
                result = operations.divide(num1, num2)
                print("Result:", result)
            case 5:
                num1, num2 = user_input(2)
                print("Result:", operations.power(num1, num2))
            case 6:
                num1, num2 = user_input(2)
                print("Result:", operations.modulo(num1, num2))
            case 7:
                num1, num2 = user_input(2)
                print("Result:", operations.int_divide(num1, num2))
            case 8:
                num = user_input(1)[0]
                print("Result:", operations.negate(num))
            case 9:
                num = user_input(1)[0]
                print("Result:", operations.increment(num))
            case 10:
                num = user_input(1)[0]
                print("Result:", operations.decrement(num))
            case 11:
                print("Exiting the calculator...")
                break
            case _:
                print("Invalid choice. Please try again.")
        input("Press any key to continue...")  # Pause and wait for user input
        clear_screen()