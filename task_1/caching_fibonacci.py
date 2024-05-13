def caching_fibonacci():
    """
    Function to create and return the fibonacci function with caching
    """
    cache = {}  # Initialize an empty cache dictionary

    def fibonacci(n):
        """
        Function to calculate the nth Fibonacci number
        """
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            # Calculate Fibonacci number recursively and store it in cache
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

# Example of use:
fib = caching_fibonacci()

# Calculate Fibonacci numbers using the fib function
print(fib(10))  # Output: 55
print(fib(15))  # Output: 610