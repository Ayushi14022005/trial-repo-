def fibonacci(n):
    # Create a list to store the Fibonacci sequence
    fib_sequence = [0, 1]

    # Check for valid input
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return fib_sequence
