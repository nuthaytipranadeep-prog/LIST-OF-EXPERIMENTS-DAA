def iterative_factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    return fact


# Input
n = int(input("Enter a number: "))

# Calculate factorial
result = iterative_factorial(n)

# Display result
print("Factorial of", n, "is:", result)