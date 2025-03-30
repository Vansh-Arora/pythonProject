def insertion_sort(arr):
    n = len(arr)
    i = 1
    while i < n:
        element = arr[i]
        j = i-1
        if element < arr[j]:
            while j > -1 and element < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = element
        i += 1
    return
