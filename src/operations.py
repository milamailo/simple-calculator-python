def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero"

def power(num1, num2):
    return num1 ** num2

def modulo(num1, num2):
    return num1 % num2

def int_divide(num1, num2):
    if num2 != 0:
        return num1 // num2
    else:
        return "Error: Division by zero"

def negate(num):
    return -num

def increment(num):
    return num + 1

def decrement(num):
    return num - 1
