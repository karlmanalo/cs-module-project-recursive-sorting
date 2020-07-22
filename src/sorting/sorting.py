# TO-DO: complete the helper function below to merge 2 sorted arrays

def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Create pointers

    j, k = 0, 0

    for i in range(len(merged_arr)):
        # Compare the values at each pointer and find the lowest value.
        # Add the lowest value to the merged array and increment the pointer
        # to which this value corresponds.

        # Check if the pointer is out of range of its respective array. If so,
        # increment.

        if k > len(arrB) - 1:
            merged_arr[i] = arrA[j]
            j += 1
        elif j > len(arrA) - 1:
            merged_arr[i] = arrB[k]
            k += 1

        # Now both pointers are in bounds for their respective arrays. Perform
        # comparisons of value at pointer, add to merged array, and increment
        # pointer.

        elif arrA[j] < arrB[k]:
            merged_arr[i] = arrA[j]
            j += 1
        else:
            merged_arr[i] = arrB[k]
            k += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively

def merge_sort(arr):

    # Check if the array is one element or less. By definition these arrays
    # are already sorted.
    if len(arr) <= 1:
        return arr

    # Get midpoint index
    midpoint = len(arr) // 2

    # Sort each half recursively
    left, right = merge_sort(arr[:midpoint]), merge_sort(arr[midpoint:])

    # Merge the two halves
    arr = merge(left, right)

    return arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
# Your code here

# def merge_sort_in_place(arr, l, r):
    # Your code here

