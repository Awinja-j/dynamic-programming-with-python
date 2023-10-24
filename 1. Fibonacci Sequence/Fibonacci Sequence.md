Fibonacci Sequence

Fibonacci Memoization: 

The Fibonacci sequence is a classic example of a recursive problem that benefits from memoization. By storing computed Fibonacci numbers in an array or dictionary, you can dramatically reduce the number of recursive calls needed.

Finonacci Tabulation:

Memoization using an array is commonly referred to as "tabulation" rather than "memoization." 

Tabulation is a bottom-up dynamic programming approach, and it involves creating an array to store results for subproblems in a specific order. You don't use recursion in this approach, and you calculate results iteratively.

```
Define the Tabulation Array: 
Create an array to store results for subproblems. The size of the array depends on the problem you are solving, and it is often initialized with an initial value. You typically start from the base case and work your way up.

Initialize Base Cases: 
Initialize the base cases in the tabulation array. These are the simplest subproblems and don't rely on the results of any other subproblems.

Iteratively Calculate and Store Results: 
Use loops to iteratively calculate results for subproblems and store them in the array. You build up the solution from the base cases to the desired result. The order in which you fill in the array depends on the problem you're solving.

Access Cached Results: 
To check if a result for a specific subproblem is already in the array, you can simply access the array at the appropriate index.

```

The fib array is used to store results for Fibonacci numbers from 0 to n. The base cases are initialized in the array, and then the loop iteratively calculates and stores the results. When you want to check if a result is already in the array, you simply access fib[n].

Tabulation is particularly efficient and avoids recursion entirely, making it suitable for problems where you can compute the results iteratively and you know the order in which the subproblems should be solved.