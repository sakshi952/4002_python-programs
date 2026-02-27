
import logging

# Configure logging
logging.basicConfig(
    filename="error_log.txt",   # Log file name
    level=logging.ERROR,        # Log only error level messages
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    # Generate arithmetic exception (division by zero)
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result:", result)

except ZeroDivisionError as e:
    print("Arithmetic Exception occurred! Cannot divide by zero.")
    logging.error("ZeroDivisionError occurred", exc_info=True)

except ValueError as e:
    print("Invalid input! Please enter integers only.")
    logging.error("ValueError occurred", exc_info=True)

finally:
    print("Program execution completed.")
