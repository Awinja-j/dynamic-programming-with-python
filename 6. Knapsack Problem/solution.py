def knapsack(values, weights, capacity):
    '''
    Solves the 0/1 Knapsack problem using dynamic programming.
    
    values: a list of values of items
    weights: a list of weights of items
    capacity: the maximum weight the knapsack can hold
    '''

    # Get the number of items
    num_items = len(values)

    # Create a dictionary to store intermediate results
    memoization = {}

    # Initialize the memoization dictionary for the base case
    for current_capacity in range(capacity + 1):
        memoization[(0, current_capacity)] = 0
        
    # Fill the memoization dictionary using dynamic programming
    for i in range(1, num_items + 1):
        for current_capacity in range(capacity + 1):
            if weights[i - 1] <= current_capacity:
                # We can either include the current item or exclude it
                include_item = values[i - 1] + memoization[(i - 1, current_capacity - weights[i - 1])]
                exclude_item = memoization[(i - 1, current_capacity)]
                # Choose the maximum value
                memoization[(i, current_capacity)] = max(include_item, exclude_item)
            else:
                # If the current item is too heavy to include, exclude it
                memoization[(i, current_capacity)] = memoization[(i - 1, current_capacity)]

    # The result is stored in the bottom-right cell of the memoization table
    return memoization[(num_items, capacity)]

# Example usage:
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
result = knapsack(values, weights, capacity)
print("Maximum value that can be achieved:", result)
