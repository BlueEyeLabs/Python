from functools import reduce

# Function to demonstrate map()
def square_numbers(numbers):
    return list(map(lambda x: x**2, numbers))

# Function to demonstrate filter()
def filter_even(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

# Function to demonstrate reduce()
def product_of_numbers(numbers):
    return reduce(lambda x, y: x * y, numbers)

# Main function to call all three
def main():
    numbers = [1, 2, 3, 4, 5, 6]

    # Call map
    squared = square_numbers(numbers)
    print("Squared numbers:", squared)

    # Call filter
    evens = filter_even(numbers)
    print("Even numbers:", evens)

    # Call reduce
    product = product_of_numbers(numbers)
    print("Product of numbers:", product)

# Entry point
if __name__ == "__main__":
    main()
