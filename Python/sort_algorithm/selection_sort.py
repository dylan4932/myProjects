# Time complexity = O(n^2)
# Space complexity = O(1)
def selection_sort(arr):
    """
    >>> selection_sort([5, 2, 8, 3, 1, 9, 4, 7, 6])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
