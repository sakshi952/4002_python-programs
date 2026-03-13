# Program to demonstrate basic exception handling in Python

try:
    # Taking input from user
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid integers.")

else:
    print("Result is:", result)

finally:
    print("Execution completed.")
