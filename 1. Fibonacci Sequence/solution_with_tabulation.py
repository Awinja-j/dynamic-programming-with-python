def fibonacci_tabulation(n):
    if n <= 1:
        return n

    # Create an array to store Fibonacci numbers from 0 to n
    fib = [0] * (n + 1) #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    print(fib)

    # Base cases
    fib[0] = 0
    fib[1] = 1

    # fib now looks like [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Calculate and store Fibonacci numbers iteratively
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    # The nth Fibonacci number is now in fib[n]
    return fib[n]

result = fibonacci_tabulation(10)
print(result)
