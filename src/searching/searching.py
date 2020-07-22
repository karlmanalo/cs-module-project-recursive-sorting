# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):

    # Handling empty arrays
    if len(arr) == 0:
        return -1

    # Setting midpoint 
    midpoint = (start + end) // 2

    if target == arr[midpoint]:
        return midpoint

    # Recursion if target is not found at midpoint
    # If target is less than the midpoint, search from the beginning
    # of the array to one element before the midpoint (subtract 1 from 
    # the index because we've already compared the target to the midpoint's
    # value in the beginning of this if statement)
    elif target < arr[midpoint]:
        return binary_search(arr, target, start, midpoint - 1)

    # If target is greater than the midpoint, search from the midpoint
    # (plus one) to the end of the array
    else:
        return binary_search(arr, target, midpoint + 1, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here

