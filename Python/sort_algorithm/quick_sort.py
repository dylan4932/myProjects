# Step 1 . Define a function called quick_sort that takes an input list
# and additional parameters low and high to indicate the range of elements to be sorted.

# Step 2. Define the base case: if the low index is greater than or equal to the high index,
# return as the list is already sorted.

# Step 3. Choose a pivot element from the list. The pivot can be any element, but commonly
# the middle element is chosen.

# Step 4. Partition the list by rearranging the elements such that all elements smaller than
# the pivot are on the left side, and all elements greater than the pivot are on the right side.
# - Initialize two pointers, i and j, pointing to the low index and high index respectively.
# - Compare the elements at i and j with the pivot. Increment i if the element is smaller than
# the pivot and decrement j if the element is greater than the pivot.
# - If i is less than or equal to j, swap the elements at indices i and j and move both pointers.
# - Repeat the above steps until i is greater than j.
# - After the loop, swap the pivot element with the element at index j (the partitioning index).

# Step 5. Recursively call the quick_sort function on the two sub-arrays formed by the partitioning
# index. For the left sub-array, set high as j - 1, and for the right sub-array, set low as j + 1.


# Time complexity = O(n*log(n))
# Worst case [O(n^2)] when the array elements are properly ascending or descending

def quick_sort(arr, low, high):
    """
    >>>
    >>> quick_sort([5, 2, 8, 3, 1, 9, 4, 7, 6], 0, 8)
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    if low < high:
        partition_index = partition(arr, low, high)
        quick_sort(arr, low, partition_index - 1)
        quick_sort(arr, partition_index + 1, high)
    return arr

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] < pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]
    return j
