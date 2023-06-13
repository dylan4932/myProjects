# time_complexity = O(n^2)
# space_complexity = O(1)

def bubble_sort(arr):
    """
    >>> bubble_sort([5, 2, 8, 3, 1, 9, 4, 7, 6])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr