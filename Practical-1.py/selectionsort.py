def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Take input from the user
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("Original array:", arr)

selection_sort(arr)

print("Sorted array:", arr)


# Time Complexity:
# Best Case    : O(n^2)
# Average Case : O(n^2)
# Worst Case   : O(n^2)
#
# Space Complexity:
# O(1)