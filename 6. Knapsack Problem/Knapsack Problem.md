## Knapsack Problem


The knapsack problem is a classic optimization problem where you have a set of items, each with a value and a weight, and you want to determine the best combination of items to include in a knapsack of limited capacity, such that the total value is maximized without exceeding the capacity.

In the knapsack problem, the `include_item` and `exclude_item` variables are used to determine the maximum value that can be obtained when you have two choices for each item:

1. `include_item`: This variable represents the maximum value that can be achieved if you include the current item in the knapsack. To calculate `include_item`, you add the value of the current item (`values[i - 1]`) to the maximum value achieved so far with the remaining capacity (`memoization[(i - 1, current_capacity - weights[i - 1])]`). In other words, if you include the item, you are subtracting its weight from the current capacity and adding its value to the maximum value achieved up to the previous item. This represents the value of the knapsack with the current item included.

2. `exclude_item`: This variable represents the maximum value that can be achieved if you exclude the current item from the knapsack. To calculate `exclude_item`, you simply take the maximum value achieved up to the previous item with the same capacity (`memoization[(i - 1, current_capacity)]`). This means you're not including the current item, so the maximum value remains the same as it was for the previous item.

The purpose of calculating both `include_item` and `exclude_item` is to determine which choice (including or excluding the current item) results in a higher value for the knapsack with the given capacity. You want to maximize the total value of the knapsack while respecting the capacity constraint. So, you choose the higher of the two values: `max(include_item, exclude_item)`. This represents the maximum value that can be achieved with the current item under consideration.

How to run:

```
python solution.py

```