# Step 1. Define a function called merge_sort that takes an input list as a parameter.

# Step 2. Define the base case: if the length of the list is 1 or less, return the list
# as it is already sorted.

# Step 3. Split the list into two halves, approximately equal in size. You can use integer
# division // to divide the length by 2.

# Step 4. Recursively call the merge_sort function on the two halves of the list.

# Step 5. Define a helper function called merge that takes two sorted lists as parameters
# and merges them into a single sorted list.

# Step 6. Initialize two pointers, i and j, to track the indices of the two lists.

# Step 7. Compare the elements at the current indices of the two lists and append the smaller
# element to the result list.

# Step 8. Move the pointer of the list from which the element was taken.

# Step 9. Repeat steps 7-8 until all elements from both lists have been processed.

# Step 10. Append any remaining elements from either list to the result list.

# Time complexity = O(n*log(n)). Divide and conquer sorting
# Space complexity = O(n)
def merge_sort(arr):
    """
    >>> merge_sort([5, 2, 8, 3, 1, 9, 4, 7, 6])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) >> 1
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged



