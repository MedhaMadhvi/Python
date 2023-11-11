# Write a Python program to create a class named Calculator with methods for basic arithmetic operations like add, subtract, multiply, and divide. Also, implement operator overloading by defining special methods like add, sub, mul and truediv for the Calculator class.
class Calculator:
    def __init__(self, value):
        self.value = value

    def add(self, other):
        return self.value + other

    def subtract(self, other):
        return self.value - other

    def multiply(self, other):
        return self.value * other

    def divide(self, other):
        if other == 0:
            return "Division by zero is not allowed"
        return self.value / other

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.subtract(other)

    def __mul__(self, other):
        return self.multiply(other)

    def __truediv__(self, other):
        return self.divide(other)

# Perform arithmetic operations
first_value = float(input("Enter the first value: "))
calculator = Calculator(first_value)
operation = input("Enter the operation (+, -, *, /): ")
second_value = float(input("Enter the second value: "))

if operation == "+":
    result = calculator + second_value
elif operation == "-":
    result = calculator - second_value
elif operation == "*":
    result = calculator * second_value
elif operation == "/":
    result = calculator / second_value
else:
    result = "Invalid operation."

print(f"Result: {result}")