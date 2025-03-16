from Sorting_techniques.helper import swap


def bubble_sort(input_array):
    n = len(input_array)
    for i in range(n-1):
        for j in range(n-i-1):
            if input_array[j] > input_array[j+1]:
                swap(input_array, j, j+1)
    return