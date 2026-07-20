# Procedural Programming Example: Factorial Calculator

def get_number():                       # Procedure 1-- Get the integer value  
    """Get a positive integer from the user."""
    try:
        num = int(input("Enter a positive integer: "))
        if num < 0:
            raise ValueError("Number must be non-negative.")
        return num
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None

def calculate_factorial(n):             # Procedure 2-- Calculate Factorial
    """Calculate factorial using a loop."""
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def display_result(n, fact):          # Procedure 3-- Display Result
    """Display the factorial result."""
    print(f"The factorial of {n} is {fact}")

def main():
    """Main procedure controlling the flow."""
    num = get_number()                       # Calling Procedure 1
    if num is not None:
        fact = calculate_factorial(num)      # Calling Procedure 2
        display_result(num, fact)            # Calling Procedure 3

# Run the program
if __name__ == "__main__":
    main()
