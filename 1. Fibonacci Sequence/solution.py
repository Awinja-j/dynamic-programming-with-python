def fibonacci(n, memo):
    if n in memo:
        return memo[n]
    if n <= 1:
        result = n
    else:
        result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    memo[n] = result
    return result

# Create a memoization dictionary
memo = {}

# Calculate the 10th Fibonacci number
result = fibonacci(10, memo)
print(result)
