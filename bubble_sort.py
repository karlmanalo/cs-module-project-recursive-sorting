def bubble_sort(arr):
    swaps_occurred = True
    while swaps_occurred:
        swaps_occurred = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps_occurred = True
    return arr

def recursive_bubble_sort(arr, unsorted_length):
    
    for i in range(unsorted_length - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            
    if unsorted_length > 0:
        recursive_bubble_sort(arr, unsorted_length - 1)