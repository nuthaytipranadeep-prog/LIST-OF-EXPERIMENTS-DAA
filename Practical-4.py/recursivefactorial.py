def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * recursive_factorial(n - 1)


# Input
n = int(input("Enter a number: "))

# Check for negative number
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = recursive_factorial(n)
    print("Factorial of", n, "is:", result)