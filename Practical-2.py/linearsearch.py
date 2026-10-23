def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


# Input array
arr = list(map(int, input("Enter elements separated by space: ").split()))

# Element to search
key = int(input("Enter the element to search: "))

# Perform linear search
result = linear_search(arr, key)

# Display result
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")