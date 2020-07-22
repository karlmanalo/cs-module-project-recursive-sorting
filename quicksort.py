def partition(arr):

    pivot = arr[0]
    left = []
    right = []

    for x in arr[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    
    return left, pivot, right

def quicksort(arr):

    if len(arr) == 0:
        return arr

    left, pivot, right = partition(arr)
    return quicksort(left) + [pivot] + quicksort(right)

a = [14,5,46,3,42,43,44,12,13]

print(quicksort(a))