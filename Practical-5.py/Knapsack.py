def knapsack(wt, val, n, W):
    # Create DP table
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                dp[i][w] = max(
                    val[i - 1] + dp[i - 1][w - wt[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


# Input number of items
n = int(input("Enter number of items: "))

# Input weights
wt = list(map(int, input("Enter weights: ").split()))

# Input values
val = list(map(int, input("Enter values: ").split()))

# Input knapsack capacity
W = int(input("Enter knapsack capacity: "))

# Calculate maximum value
result = knapsack(wt, val, n, W)

# Display result
print("Maximum value:", result)