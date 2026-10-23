def merge(arr, left, mid, right):
    temp = []
    i = left
    j = mid + 1

    # Compare elements from both halves
    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    # Add remaining elements from left half
    while i <= mid:
        temp.append(arr[i])
        i += 1

    # Add remaining elements from right half
    while j <= right:
        temp.append(arr[j])
        j += 1

    # Copy sorted elements back to original array
    for k in range(len(temp)):
        arr[left + k] = temp[k]


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


# Take input from the user
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("Original array:", arr)

# Call Merge Sort
merge_sort(arr, 0, len(arr) - 1)

print("Sorted array:", arr)


# Merge Sort
# Time Complexity:
# Best Case    : O(n log n)
# Average Case : O(n log n)
# Worst Case   : O(n log n)
#
# Space Complexity:
# O(n)