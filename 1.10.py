# Lambda functions
add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b if b != 0 else "Error: Division by zero"

# User input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

# Invoking appropriate lambda function
if op == '+':
    result = add(num1, num2)
elif op == '-':
    result = sub(num1, num2)
elif op == '*':
    result = mul(num1, num2)
elif op == '/':
    result = div(num1, num2)
else:
    result = "Invalid operator"

print("Result:", result)
