def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)

        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)


# Take input from the user
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("Original array:", arr)

# Call Quick Sort
quick_sort(arr, 0, len(arr) - 1)

print("Sorted array:", arr)



# Time Complexity:
# Best Case    : O(n log n)
# Average Case : O(n log n)
# Worst Case   : O(n^2)
#
# Space Complexity:
# O(log n) (Recursion Stack)