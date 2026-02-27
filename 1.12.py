x = 10   # Global variable

def outer():
    y = 20   # Local variable of outer(), nonlocal for inner()

    def inner():
        nonlocal y
        global x

        x = x + 5      # Modifying global variable
        y = y + 5      # Modifying nonlocal variable

        z = 30         # Local variable of inner()
        print("Inside inner()")
        print("Local variable z:", z)
        print("Nonlocal variable y:", y)
        print("Global variable x:", x)

    inner()
    print("\nInside outer()")
    print("Nonlocal variable y after inner():", y)

# Function call
outer()
print("\nOutside all functions")
print("Global variable x after function call:", x)
