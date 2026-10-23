def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Input sorted array
arr = list(map(int, input("Enter elements in sorted order: ").split()))

# Element to search
key = int(input("Enter the element to search: "))

# Perform binary search
result = binary_search(arr, key)

# Display result
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")