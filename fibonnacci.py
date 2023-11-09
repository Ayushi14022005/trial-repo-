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
 # Generate the Fibonacci sequence up to the nth term
    for i in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    return fib_sequence

# Get the first 10 terms of the Fibonacci sequence
n = 10
result = fibonacci(n)
print(result)
