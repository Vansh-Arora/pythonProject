from SortingTechniques.helper import swap


def bubble_sort(input_array):
    n = len(input_array)
    for i in range(n-1):
        for j in range(n-i-1):
            if input_array[j] > input_array[j+1]:
                swap(input_array, j, j+1)
    returnSorting-20250101
Sorting-20250102
Sorting-20250103
Sorting-20250104
Sorting-20250105
Sorting-20250106
Sorting-20250107
Sorting-20250108
Sorting-20250109
Sorting-20250110
Sorting-20250111
Sorting-20250112
Sorting-20250113
Sorting-20250114
