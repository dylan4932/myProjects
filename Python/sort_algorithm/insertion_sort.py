# Time complexity = O(n^2)
# space complexity = O(1)

def insertion_sort(arr):
    """
    >>> insertion_sort([5, 2, 8, 3, 1, 9, 4, 7, 6])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
